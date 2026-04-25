#!/usr/bin/env python3
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "lib"))


import argparse
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
LINT_SCRIPT = REPO_ROOT / ".github" / "scripts" / "lint_amendment_ledger.py"


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Compute/fill Amendment Ledger SHA-256 hashes using the same logic as CI",
    )
    parser.add_argument("--base", default="HEAD~1")
    parser.add_argument("--head", default="HEAD")
    parser.add_argument("--staged", action="store_true", help="Process staged files (for hook usage)")
    parser.add_argument("--check", action="store_true", help="Validate only, do not modify files")
    args = parser.parse_args()

    cmd = [sys.executable, str(LINT_SCRIPT)]
    if args.staged:
        cmd.append("--staged")
    else:
        cmd.extend(["--base", args.base, "--head", args.head])
    if not args.check:
        cmd.append("--fix")

    proc = subprocess.run(cmd, cwd=REPO_ROOT)
    return proc.returncode


if __name__ == "__main__":
    raise SystemExit(main())
