#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]

SCOPED_PREFIXES = (
    "Governance/Constitution/",
    "Governance/Charters/",
)

AMENDMENT_HEADING_RE = re.compile(r"^##+\s+.*amendment\s+ledger", re.IGNORECASE | re.MULTILINE)
NEXT_HEADING_RE = re.compile(r"^##+\s+", re.MULTILINE)


def run_git(args: list[str], check: bool = True) -> str:
    proc = subprocess.run(["git", *args], cwd=REPO_ROOT, text=True, capture_output=True)
    if check and proc.returncode != 0:
        raise RuntimeError(proc.stderr.strip() or f"git {' '.join(args)} failed")
    return proc.stdout


def list_modified_files(base: str, head: str) -> list[str]:
    out = run_git(["diff", "--name-only", f"{base}..{head}"])
    paths = []
    for raw in out.splitlines():
        path = raw.strip()
        if not path.endswith(".md"):
            continue
        if not path.startswith(SCOPED_PREFIXES):
            continue
        paths.append(path)
    return paths


def get_blob(rev: str, path: str) -> str:
    proc = subprocess.run(["git", "show", f"{rev}:{path}"], cwd=REPO_ROOT, text=True, capture_output=True)
    if proc.returncode != 0:
        return ""
    return proc.stdout


def normalize_for_whitespace_compare(text: str) -> str:
    return "\n".join(line.rstrip() for line in text.splitlines()).strip()


def extract_amendment_section(text: str) -> str:
    m = AMENDMENT_HEADING_RE.search(text)
    if not m:
        return ""

    start = m.start()
    tail = text[m.end():]
    nxt = NEXT_HEADING_RE.search(tail)
    end = (m.end() + nxt.start()) if nxt else len(text)
    return text[start:end].strip()


def has_amendment_ledger(text: str) -> bool:
    return AMENDMENT_HEADING_RE.search(text) is not None


def lint(base: str, head: str) -> int:
    failures: list[str] = []

    for path in list_modified_files(base, head):
        before = get_blob(base, path)
        after = get_blob(head, path)

        if normalize_for_whitespace_compare(before) == normalize_for_whitespace_compare(after):
            continue

        if not has_amendment_ledger(after):
            continue

        before_ledger = extract_amendment_section(before)
        after_ledger = extract_amendment_section(after)

        if before_ledger == after_ledger:
            failures.append(path)

    if failures:
        for path in failures:
            print(f"{path}: Amendment Ledger not updated")
        return 1

    print("Amendment Ledger lint passed")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Ensure modified governance docs update Amendment Ledger")
    parser.add_argument("--base", default="HEAD~1")
    parser.add_argument("--head", default="HEAD")
    args = parser.parse_args()

    return lint(args.base, args.head)


if __name__ == "__main__":
    sys.exit(main())
