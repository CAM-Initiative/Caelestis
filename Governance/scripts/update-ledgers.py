#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import re
import subprocess
from datetime import datetime, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
SCOPED_PREFIXES = ("Governance/Constitution/", "Governance/Charters/")
AMENDMENT_HEADING_RE = re.compile(r"^##+\s+.*amendment\s+ledger", re.IGNORECASE | re.MULTILINE)
NEXT_HEADING_RE = re.compile(r"^##+\s+", re.MULTILINE)
VERSION_RE = re.compile(r"^\d+\.\d+$")


def run_git(args: list[str], check: bool = True) -> str:
    proc = subprocess.run(["git", *args], cwd=REPO_ROOT, text=True, capture_output=True)
    if check and proc.returncode != 0:
        raise RuntimeError(proc.stderr.strip() or f"git {' '.join(args)} failed")
    return proc.stdout


def list_modified_files(base: str, head: str) -> list[str]:
    out = run_git(["diff", "--name-only", f"{base}..{head}"])
    files: list[str] = []
    for raw in out.splitlines():
        path = raw.strip()
        if not path.endswith(".md"):
            continue
        if not path.startswith(SCOPED_PREFIXES):
            continue
        files.append(path)
    return files


def get_blob(rev: str, path: str) -> str:
    proc = subprocess.run(["git", "show", f"{rev}:{path}"], cwd=REPO_ROOT, text=True, capture_output=True)
    if proc.returncode != 0:
        return ""
    return proc.stdout


def ledger_bounds(text: str) -> tuple[int, int] | None:
    m = AMENDMENT_HEADING_RE.search(text)
    if not m:
        return None
    tail = text[m.end():]
    nxt = NEXT_HEADING_RE.search(tail)
    end = (m.end() + nxt.start()) if nxt else len(text)
    return (m.start(), end)


def extract_ledger(text: str) -> str:
    b = ledger_bounds(text)
    if not b:
        return ""
    return text[b[0]:b[1]]


def split_row(line: str) -> list[str]:
    return [c.strip() for c in line.strip().strip("|").split("|")]


def parse_versions(ledger_text: str) -> list[str]:
    versions: list[str] = []
    for line in ledger_text.splitlines():
        stripped = line.strip()
        if not stripped.startswith("|"):
            continue
        cols = split_row(stripped)
        if not cols:
            continue
        first = cols[0]
        if first.lower() == "version" or set(first) <= {"-"}:
            continue
        if VERSION_RE.match(first):
            versions.append(first)
    return versions


def major(version: str) -> int:
    return int(version.split(".")[0])


def minor_bump(version: str) -> str:
    m, n = version.split(".")
    return f"{m}.{int(n) + 1}"


def find_last_version_row_idx(lines: list[str], start: int, end: int) -> int | None:
    last_idx = None
    for idx in range(start, end):
        stripped = lines[idx].strip()
        if not stripped.startswith("|"):
            continue
        cols = split_row(stripped)
        if cols and VERSION_RE.match(cols[0]):
            last_idx = idx
    return last_idx


def append_minor_row(text: str, description: str, timestamp_utc: str) -> str:
    bounds = ledger_bounds(text)
    if not bounds:
        return text
    start, end = bounds
    lines = text.splitlines(keepends=True)

    cursor = 0
    start_idx = end_idx = None
    for i, ln in enumerate(lines):
        ls, le = cursor, cursor + len(ln)
        if start_idx is None and le > start:
            start_idx = i
        if end_idx is None and ls >= end:
            end_idx = i
            break
        cursor = le
    if start_idx is None:
        return text
    if end_idx is None:
        end_idx = len(lines)

    last_idx = find_last_version_row_idx(lines, start_idx, end_idx)
    if last_idx is None:
        return text
    cols = split_row(lines[last_idx].strip())
    if not cols or not VERSION_RE.match(cols[0]):
        return text

    next_version = minor_bump(cols[0])
    row = f"| {next_version} | {description} | {timestamp_utc} |  |\n"
    lines.insert(last_idx + 1, row)
    return "".join(lines)


def replace_last_hash_cell(text: str, hash_value: str) -> str:
    bounds = ledger_bounds(text)
    if not bounds:
        return text
    start, end = bounds
    lines = text.splitlines(keepends=True)

    cursor = 0
    start_idx = end_idx = None
    for i, ln in enumerate(lines):
        ls, le = cursor, cursor + len(ln)
        if start_idx is None and le > start:
            start_idx = i
        if end_idx is None and ls >= end:
            end_idx = i
            break
        cursor = le
    if start_idx is None:
        return text
    if end_idx is None:
        end_idx = len(lines)

    last_idx = find_last_version_row_idx(lines, start_idx, end_idx)
    if last_idx is None:
        return text

    line = lines[last_idx]
    parts = [p for p in line.rstrip("\n").split("|")]
    if len(parts) < 6:
        return text
    parts[-2] = f" {hash_value} "
    lines[last_idx] = "|".join(parts) + ("\n" if line.endswith("\n") else "")
    return "".join(lines)


def normalize_for_hash(text: str) -> str:
    normalized = text.replace("\r\n", "\n").replace("\r", "\n")
    return "\n".join(line.rstrip() for line in normalized.split("\n"))


def compute_latest_row_hash(text: str) -> str:
    blanked = replace_last_hash_cell(text, "")
    return hashlib.sha256(normalize_for_hash(blanked).encode("utf-8")).hexdigest()


def process_file(path: str, base: str, head: str) -> None:
    before = get_blob(base, path)
    after_commit = get_blob(head, path)
    current_path = REPO_ROOT / path
    if not current_path.exists():
        return
    current = current_path.read_text(encoding="utf-8")
    if not extract_ledger(current):
        return

    before_ledger = extract_ledger(before)
    after_ledger = extract_ledger(after_commit)
    before_versions = parse_versions(before_ledger)
    after_versions = parse_versions(after_ledger)

    major_bump_detected = False
    if before_versions and after_versions:
        major_bump_detected = major(after_versions[-1]) > major(before_versions[-1])

    if (before_ledger == after_ledger) and (not major_bump_detected):
        ts = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
        current = append_minor_row(
            current,
            description="Automated amendment ledger entry via update-ledgers.py",
            timestamp_utc=ts,
        )

    latest_hash = compute_latest_row_hash(current)
    current = replace_last_hash_cell(current, latest_hash)
    current_path.write_text(current, encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Update amendment ledgers for modified governance instruments")
    parser.add_argument("--base", required=True)
    parser.add_argument("--head", required=True)
    args = parser.parse_args()

    for path in list_modified_files(args.base, args.head):
        process_file(path, args.base, args.head)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
