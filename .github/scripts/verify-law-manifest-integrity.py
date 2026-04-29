#!/usr/bin/env python3
import hashlib
import json
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
LAWS_DIR = REPO_ROOT / "Governance" / "Laws"
MANIFEST_PATH = REPO_ROOT / "MANIFEST.json"


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def main() -> int:
    if not MANIFEST_PATH.exists():
        print(f"ERROR: Missing manifest: {MANIFEST_PATH.relative_to(REPO_ROOT)}")
        return 1

    payload = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    files = payload.get("files", [])
    manifest_law = {
        entry.get("path"): entry.get("sha256")
        for entry in files
        if str(entry.get("path", "")).startswith("Governance/Laws/") and str(entry.get("path", "")).endswith(".md") and str(entry.get("path", "")) != "Governance/Laws/CAM-Laws-Index.md"
    }

    actual_law_paths = sorted(
        p.relative_to(REPO_ROOT).as_posix()
        for p in LAWS_DIR.glob("*.md")
        if p.name != "CAM-Laws-Index.md"
    )

    failures: list[str] = []

    for rel_path in actual_law_paths:
        if rel_path not in manifest_law:
            failures.append(f"missing MANIFEST entry for law file: {rel_path}")
            continue
        actual = sha256_file(REPO_ROOT / rel_path)
        expected = (manifest_law.get(rel_path) or "").strip()
        if actual != expected:
            failures.append(f"MANIFEST sha256 mismatch for {rel_path}: expected {expected}, computed {actual}")

    actual_set = set(actual_law_paths)
    manifest_set = set(manifest_law.keys())
    for extra in sorted(manifest_set - actual_set):
        failures.append(f"MANIFEST contains extra/untracked law file entry: {extra}")

    if failures:
        for item in failures:
            print(f"ERROR: {item}")
        return 1

    print("Law manifest integrity verification passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
