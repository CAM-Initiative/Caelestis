#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import os
import tarfile
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
import zipfile

ROOT = Path(__file__).resolve().parents[2]
OUT_DIR = ROOT / "archive_output"
MANIFEST_PATH = ROOT / "MANIFEST.json"
VERSION = "Package 1"
FIXED_MTIME = 946684800  # 2000-01-01T00:00:00Z
FIXED_ZIP_DT = (2000, 1, 1, 0, 0, 0)

EXCLUDED_DIRS = {
    ".git",
    "node_modules",
    "__pycache__",
    ".mypy_cache",
    ".pytest_cache",
    ".ruff_cache",
    ".venv",
    "venv",
    ".idea",
    ".vscode",
    "archive_output",
}

EXCLUDED_FILE_NAMES = {".DS_Store"}
EXCLUDED_SUFFIXES = {".tmp", ".swp", ".swo", "~"}

REQUIRED_METADATA = [
    "CITATION.cff",
    "README.md",
    "licence.md",
    "MANIFEST.json",
]


@dataclass
class Entry:
    path: str
    sha256: str
    size_bytes: int
    role: str


def is_excluded(path: Path) -> bool:
    parts = set(path.parts)
    if parts & EXCLUDED_DIRS:
        return True
    if path.name in EXCLUDED_FILE_NAMES:
        return True
    return any(path.name.endswith(sfx) for sfx in EXCLUDED_SUFFIXES)


def role_for(rel: str) -> str:
    if rel.startswith("Governance/"):
        return "governance"
    if rel.startswith(".github/workflows/"):
        return "workflow"
    if rel.startswith(".github/scripts/"):
        return "script"
    if rel.endswith(".index.json") or rel in {
        "Governance/CAM.Governance.JSON",
    }:
        return "index"
    if rel in {"CITATION.cff", "MANIFEST.json"}:
        return "metadata"
    if rel.lower().startswith("images/"):
        return "image-reference"
    if rel.lower().endswith(".md"):
        return "documentation"
    return "other"


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def list_files() -> list[Path]:
    files: list[Path] = []
    for p in ROOT.rglob("*"):
        if not p.is_file():
            continue
        rel = p.relative_to(ROOT)
        if is_excluded(rel):
            continue
        files.append(rel)
    return sorted(files, key=lambda x: x.as_posix())


def build_manifest(files: list[Path]) -> dict:
    generated_ts = datetime.now(timezone.utc).replace(microsecond=0).isoformat()
    entries: list[dict] = []
    for rel in files:
        rel_posix = rel.as_posix()
        if rel_posix == "MANIFEST.json":
            continue
        full = ROOT / rel
        entries.append(
            Entry(
                path=rel_posix,
                sha256=sha256_file(full),
                size_bytes=full.stat().st_size,
                role=role_for(rel_posix),
            ).__dict__
        )

    entries.append(
        {
            "path": "MANIFEST.json",
            "sha256": "SELF-REFERENTIAL-ENTRY-EXCLUDED",
            "size_bytes": 0,
            "role": "metadata",
        }
    )

    return {
        "package_version": VERSION,
        "generated_timestamp": generated_ts,
        "entries": entries,
    }


def write_manifest(files: list[Path]) -> None:
    manifest = build_manifest(files)
    content = json.dumps(manifest, indent=2, ensure_ascii=False, sort_keys=True) + "\n"
    MANIFEST_PATH.write_text(content, encoding="utf-8")

    manifest_size = MANIFEST_PATH.stat().st_size
    data = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    for entry in data["entries"]:
        if entry["path"] == "MANIFEST.json":
            entry["size_bytes"] = manifest_size
    MANIFEST_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False, sort_keys=True) + "\n", encoding="utf-8")


def verify_manifest(files: list[Path]) -> None:
    data = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    manifest_paths = sorted(entry["path"] for entry in data["entries"])
    expected_paths = sorted(p.as_posix() for p in files)
    if manifest_paths != expected_paths:
        missing = sorted(set(expected_paths) - set(manifest_paths))
        extra = sorted(set(manifest_paths) - set(expected_paths))
        raise RuntimeError(f"MANIFEST paths mismatch. Missing={missing} Extra={extra}")

    by_path = {entry["path"]: entry for entry in data["entries"]}
    for rel in expected_paths:
        if rel == "MANIFEST.json":
            continue
        full = ROOT / rel
        actual_hash = sha256_file(full)
        actual_size = full.stat().st_size
        expected = by_path[rel]
        if expected["sha256"] != actual_hash or expected["size_bytes"] != actual_size:
            raise RuntimeError(f"MANIFEST mismatch for {rel}")


def make_zip(files: list[Path], zip_path: Path) -> None:
    with zipfile.ZipFile(zip_path, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as zf:
        for rel in files:
            full = ROOT / rel
            info = zipfile.ZipInfo(rel.as_posix())
            info.date_time = FIXED_ZIP_DT
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            with full.open("rb") as f:
                zf.writestr(info, f.read())


def make_targz(files: list[Path], tar_path: Path) -> None:
    with tarfile.open(tar_path, "w:gz", format=tarfile.PAX_FORMAT) as tf:
        for rel in files:
            full = ROOT / rel
            ti = tf.gettarinfo(str(full), arcname=rel.as_posix())
            ti.uid = 0
            ti.gid = 0
            ti.uname = "root"
            ti.gname = "root"
            ti.mtime = FIXED_MTIME
            with full.open("rb") as f:
                tf.addfile(ti, fileobj=f)


def main() -> int:
    os.chdir(ROOT)

    files = list_files()
    if "MANIFEST.json" not in [p.as_posix() for p in files]:
        files.append(Path("MANIFEST.json"))
        files = sorted(files, key=lambda p: p.as_posix())

    write_manifest(files)
    files = list_files()
    if Path("MANIFEST.json") not in files:
        files.append(Path("MANIFEST.json"))
        files = sorted(files, key=lambda p: p.as_posix())

    for required in REQUIRED_METADATA:
        if required not in [f.as_posix() for f in files]:
            raise RuntimeError(f"Missing required metadata file: {required}")

    verify_manifest(files)

    OUT_DIR.mkdir(exist_ok=True)
    zip_path = OUT_DIR / "Caelestis-Package-1.zip"
    tar_path = OUT_DIR / "Caelestis-Package-1.tar.gz"
    make_zip(files, zip_path)
    make_targz(files, tar_path)

    print(f"Wrote: {MANIFEST_PATH.relative_to(ROOT)}")
    print(f"Wrote: {zip_path.relative_to(ROOT)}")
    print(f"Wrote: {tar_path.relative_to(ROOT)}")
    print("Determinism: lexicographic file ordering and normalized archive timestamps (2000-01-01T00:00:00Z).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
