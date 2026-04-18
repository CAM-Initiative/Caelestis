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
VERSION_CELL_RE = re.compile(r"^\d+\.\d+$")


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


def parse_ledger_versions(section: str) -> list[str]:
    versions: list[str] = []
    for line in section.splitlines():
        stripped = line.strip()
        if not stripped.startswith("|"):
            continue
        cols = [c.strip() for c in stripped.strip("|").split("|")]
        if not cols:
            continue
        first = cols[0]
        if first.lower() == "version":
            continue
        if set(first) <= {"-"}:
            continue
        if VERSION_CELL_RE.match(first):
            versions.append(first)
    return versions


def is_minor_only_increment(previous: str, current: str) -> bool:
    prev_major, prev_minor = previous.split(".")
    curr_major, curr_minor = current.split(".")
    if prev_major != curr_major:
        return False
    return int(curr_minor) == int(prev_minor) + 1


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
            continue

        before_versions = parse_ledger_versions(before_ledger)
        after_versions = parse_ledger_versions(after_ledger)
        if len(after_versions) >= 2:
            previous_version = after_versions[-2]
            current_version = after_versions[-1]
            if not is_minor_only_increment(previous_version, current_version):
                failures.append(f"{path}: Amendment version must increment MINOR only (no MAJOR bump)")
        elif before_versions and after_versions:
            previous_version = before_versions[-1]
            current_version = after_versions[-1]
            if previous_version != current_version and not is_minor_only_increment(previous_version, current_version):
                failures.append(f"{path}: Amendment version must increment MINOR only (no MAJOR bump)")

    if failures:
        for failure in failures:
            if ": " in failure:
                print(failure)
            else:
                print(f"{failure}: Amendment Ledger not updated")
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
