#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import subprocess
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
INDICES_DIR = REPO_ROOT / ".github" / "Indices"
FILES = [
    "CAM.Governance.Symbolic-Structures.Index.json",
    "CAM.Governance.Symbolic-Structures.Index.md",
    "CAM.Governance.Symbolic-Structures.Registry.json",
]


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def main() -> int:
    INDICES_DIR.mkdir(parents=True, exist_ok=True)

    before: dict[str, str] = {}
    for name in FILES:
        path = INDICES_DIR / name
        if path.exists():
            before[name] = sha256(path)

    subprocess.run(["python", str(REPO_ROOT / ".github" / "scripts" / "build-symbolic-structures-index.py")], check=True, cwd=REPO_ROOT)

    summary: dict[str, list[str]] = {"scanned": [], "generated": [], "updated": [], "unchanged": [], "missing": []}
    for name in FILES:
        path = INDICES_DIR / name
        summary["scanned"].append(name)
        if not path.exists():
            summary["missing"].append(name)
            print(f"INDICES_STATUS missing {name}")
            continue
        now = sha256(path)
        if name not in before:
            summary["generated"].append(name)
            print(f"INDICES_STATUS generated {name}")
        elif before[name] != now:
            summary["updated"].append(name)
            print(f"INDICES_STATUS updated {name}")
        else:
            summary["unchanged"].append(name)
            print(f"INDICES_STATUS unchanged {name}")

    print("INDICES_SUMMARY " + json.dumps(summary, sort_keys=True))
    if summary["missing"]:
        print("ERROR: symbolic index generation did not produce all required .github/Indices files")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
