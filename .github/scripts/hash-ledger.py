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
    parser.add_argument("--report", action="store_true", help="Alias of --check for dry-run reporting")
    parser.add_argument("--all", action="store_true", help="Scan all scoped governance files")
    args = parser.parse_args()

    print("Ledger hash step started")

    before = subprocess.run(
        ["git", "diff", "--name-only"],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
        check=False,
    )

    cmd = [sys.executable, str(LINT_SCRIPT)]
    if args.all:
        cmd.append("--all")
    if args.staged:
        cmd.append("--staged")
    else:
        cmd.extend(["--base", args.base, "--head", args.head])
    if not (args.check or args.report):
        cmd.append("--fix")

    proc = subprocess.run(cmd, cwd=REPO_ROOT)
    if proc.returncode != 0:
        print(f"ERROR: Ledger hash step failed with exit code {proc.returncode}", file=sys.stderr)
        return proc.returncode

    after = subprocess.run(
        ["git", "diff", "--name-only"],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    before_set = {p.strip() for p in before.stdout.splitlines() if p.strip()}
    after_set = {p.strip() for p in after.stdout.splitlines() if p.strip()}
    updated_files = sorted(after_set - before_set)
    print(f"Ledger hash step completed (files updated: {len(updated_files)})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
