#!/usr/bin/env python3
"""Build a deterministic archival package for repository submission."""

from __future__ import annotations

import hashlib
import json
import os
import subprocess
import tarfile
import zipfile
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable

ROOT = Path(__file__).resolve().parents[2]
OUTPUT_DIR = ROOT / "dist" / "archive"
PACKAGE_VERSION = "Package 1"
ARCHIVE_BASENAME = "Caelestis-Package-1"

EXCLUDE_DIRS = {
    ".git",
    "node_modules",
    "__pycache__",
    ".pytest_cache",
    ".mypy_cache",
    ".ruff_cache",
    ".cache",
    ".venv",
    "venv",
    "dist",
}
EXCLUDE_FILE_NAMES = {
    ".DS_Store",
}
EXCLUDE_SUFFIXES = {
    ".tmp",
    ".temp",
    ".swp",
    ".swo",
}

REQUIRED_METADATA = ["README.md", "CITATION.cff"]
REQUIRED_INDEXES = [
    "Governance/Constitution/constitution.index.json",
    "Governance/Charters/charters.index.json",
    "Governance/Laws/laws.index.json",
    "Governance/CAM.Governance.JSON",
]


@dataclass(frozen=True)
class ManifestEntry:
    path: str
    sha256: str | None
    size_bytes: int
    role: str


def run_checked(cmd: list[str]) -> None:
    result = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True)
    if result.stdout:
        print(result.stdout, end="")
    if result.stderr:
        print(result.stderr, end="")
    if result.returncode != 0:
        raise SystemExit(f"Command failed ({result.returncode}): {' '.join(cmd)}")


def source_date_epoch() -> int:
    env_val = os.getenv("SOURCE_DATE_EPOCH")
    if env_val and env_val.isdigit():
        return int(env_val)
    result = subprocess.run(
        ["git", "log", "-1", "--format=%ct"],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    if result.returncode == 0 and result.stdout.strip().isdigit():
        return int(result.stdout.strip())
    return int(datetime.now(tz=timezone.utc).timestamp())


def classify_role(rel_path: str) -> str:
    if rel_path.startswith("Governance/"):
        return "governance"
    if rel_path.startswith(".github/workflows/"):
        return "workflow"
    if rel_path.startswith(".github/scripts/"):
        return "script"
    if rel_path.endswith(".index.json") or rel_path.endswith("CAM.Governance.JSON"):
        return "index"
    if rel_path in {"README.md", "CITATION.cff", "MANIFEST.json"}:
        return "metadata"
    if rel_path.endswith((".png", ".svg", ".jpg", ".jpeg", ".gif", ".webp")):
        return "image-reference"
    if rel_path.endswith((".md", ".txt")):
        return "documentation"
    return "other"


def iter_files() -> Iterable[Path]:
    for path in sorted(ROOT.rglob("*")):
        rel_parts = path.relative_to(ROOT).parts
        if any(part in EXCLUDE_DIRS for part in rel_parts):
            continue
        if path.is_dir():
            continue
        if path.name in EXCLUDE_FILE_NAMES:
            continue
        if any(path.name.endswith(sfx) for sfx in EXCLUDE_SUFFIXES):
            continue
        yield path


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def collect_manifest_entries() -> list[ManifestEntry]:
    entries: list[ManifestEntry] = []
    for abs_path in iter_files():
        rel_path = abs_path.relative_to(ROOT).as_posix()
        if rel_path == "MANIFEST.json":
            entries.append(
                ManifestEntry(
                    path=rel_path,
                    sha256=None,
                    size_bytes=abs_path.stat().st_size,
                    role=classify_role(rel_path),
                )
            )
            continue
        entries.append(
            ManifestEntry(
                path=rel_path,
                sha256=sha256_file(abs_path),
                size_bytes=abs_path.stat().st_size,
                role=classify_role(rel_path),
            )
        )
    return entries


def write_manifest(entries: list[ManifestEntry], generated_ts: str) -> None:
    manifest = {
        "package_version": PACKAGE_VERSION,
        "generated_timestamp": generated_ts,
        "root": ".",
        "files": [
            {
                "path": e.path,
                "sha256": e.sha256,
                "size_bytes": e.size_bytes,
                "role": e.role,
            }
            for e in sorted(entries, key=lambda x: x.path)
        ],
        "notes": {
            "MANIFEST.json": "sha256 is null because this file is self-referential"
        },
    }
    (ROOT / "MANIFEST.json").write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )


def ensure_required_files() -> None:
    missing = [p for p in REQUIRED_METADATA + REQUIRED_INDEXES if not (ROOT / p).exists()]
    if missing:
        raise SystemExit(f"Missing required metadata/index files: {missing}")


def refresh_generated_governance_views() -> None:
    run_checked(["python3", ".github/scripts/update-CAM-Constitution-Index.py"])
    run_checked(["python3", ".github/scripts/update-CAM-Charters-Index.py"])
    run_checked(["python3", ".github/scripts/update-CAM-Laws-Index.py"])
    run_checked(["python3", ".github/scripts/update-CAM-Governance-Index.py"])
    run_checked(["python3", ".github/scripts/lint_amendment_ledger.py", "--all", "--fix"])
    run_checked(["python3", ".github/scripts/lint_amendment_ledger.py"])


def create_zip(files: list[Path], zip_path: Path, epoch: int) -> None:
    dt = datetime.fromtimestamp(epoch, tz=timezone.utc)
    zip_dt = (max(dt.year, 1980), dt.month, dt.day, dt.hour, dt.minute, dt.second)
    with zipfile.ZipFile(zip_path, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as zf:
        for abs_path in files:
            rel = abs_path.relative_to(ROOT).as_posix()
            info = zipfile.ZipInfo(rel)
            info.date_time = zip_dt
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            data = abs_path.read_bytes()
            zf.writestr(info, data)


def create_tar_gz(files: list[Path], tar_path: Path, epoch: int) -> None:
    with tarfile.open(tar_path, "w:gz", format=tarfile.PAX_FORMAT) as tf:
        for abs_path in files:
            rel = abs_path.relative_to(ROOT).as_posix()
            info = tf.gettarinfo(str(abs_path), arcname=rel)
            info.uid = 0
            info.gid = 0
            info.uname = ""
            info.gname = ""
            info.mtime = epoch
            with abs_path.open("rb") as f:
                tf.addfile(info, f)


def archive_members(path: Path) -> list[str]:
    if path.suffix == ".zip":
        with zipfile.ZipFile(path, "r") as zf:
            return sorted(zf.namelist())
    with tarfile.open(path, "r:gz") as tf:
        return sorted(m.name for m in tf.getmembers() if m.isfile())


def verify_manifest_against_archives(entries: list[ManifestEntry], archives: list[Path]) -> None:
    manifest_paths = sorted(e.path for e in entries)
    for archive in archives:
        members = archive_members(archive)
        if members != manifest_paths:
            raise SystemExit(
                f"Archive content mismatch for {archive}: manifest has {len(manifest_paths)} files, archive has {len(members)}"
            )


def main() -> None:
    os.chdir(ROOT)
    refresh_generated_governance_views()
    ensure_required_files()

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    epoch = source_date_epoch()
    generated_ts = datetime.fromtimestamp(epoch, tz=timezone.utc).isoformat(timespec="seconds")

    initial_entries = collect_manifest_entries()
    write_manifest(initial_entries, generated_ts)

    entries = collect_manifest_entries()
    files = [ROOT / e.path for e in sorted(entries, key=lambda x: x.path)]

    zip_path = OUTPUT_DIR / f"{ARCHIVE_BASENAME}.zip"
    tar_path = OUTPUT_DIR / f"{ARCHIVE_BASENAME}.tar.gz"

    create_zip(files, zip_path, epoch)
    create_tar_gz(files, tar_path, epoch)

    verify_manifest_against_archives(entries, [zip_path, tar_path])

    print(f"Wrote manifest: {(ROOT / 'MANIFEST.json').as_posix()}")
    print(f"Wrote archive: {zip_path.as_posix()}")
    print(f"Wrote archive: {tar_path.as_posix()}")


if __name__ == "__main__":
    main()
