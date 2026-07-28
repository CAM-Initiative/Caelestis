#!/usr/bin/env python3
from difflib import SequenceMatcher
from pathlib import Path
import re
import subprocess

ROOT = Path(__file__).resolve().parents[2]
OLD_REF = "origin/policy/civilisational-wealth-governance"
FIXED_TIMESTAMP = "2026-07-28T09:35:31Z"
INCORRECT_TIMESTAMP = "2026-07-26T00:00:00Z"
REPORT = ROOT / ".github" / "Indices" / "branch-deletion-source-audit.txt"
EXCLUDED = {
    "Governance/Constitution/CAM-BS2025-AEON-003-SCH-01.md": "generated schedule",
    "Governance/Constitution/CAM-BS2025-AEON-003-SCH-03.md": "generated schedule",
    "Governance/Charters/CAM-EQ2026-OPERATIONS-008-PLATINUM.md": "current main contains the later complete red-team charter",
}
HEADING_RE = re.compile(r"^##+\s+.*amendment\s+ledger", re.IGNORECASE | re.MULTILINE)
NEXT_HEADING_RE = re.compile(r"^##+\s+", re.MULTILINE)
VERSION_RE = re.compile(r"^\d+(?:\.\d+)+$")
HEX_RE = re.compile(r"^[0-9a-f]{64}$")


def run(args, *, check=True):
    proc = subprocess.run(args, cwd=ROOT, text=True, capture_output=True)
    if check and proc.returncode != 0:
        raise RuntimeError(proc.stderr.strip() or proc.stdout.strip() or "Command failed")
    return proc


def git_text(ref, path):
    proc = run(["git", "show", f"{ref}:{path}"], check=False)
    return proc.stdout if proc.returncode == 0 else None


def split_ledger(text):
    if text is None:
        return None, None
    match = HEADING_RE.search(text)
    if not match:
        return text, None
    tail = text[match.end():]
    nxt = NEXT_HEADING_RE.search(tail)
    end = match.end() + nxt.start() if nxt else len(text)
    return text[:match.start()] + text[end:], text[match.start():end]


def norm_line(line):
    return re.sub(r"\s+", " ", line.replace("\u00a0", " ").strip())


def norm_lines(text):
    return [value for value in (norm_line(line) for line in (text or "").replace("\r\n", "\n").split("\n")) if value]


def contains_block(haystack, needle):
    if not needle:
        return True
    width = len(needle)
    return any(haystack[index:index + width] == needle for index in range(0, len(haystack) - width + 1))


def added_blocks(base_body, old_body):
    base_lines = norm_lines(base_body)
    old_lines = norm_lines(old_body)
    matcher = SequenceMatcher(a=base_lines, b=old_lines, autojunk=False)
    blocks = []
    for tag, _i1, _i2, j1, j2 in matcher.get_opcodes():
        if tag in {"insert", "replace"} and j2 > j1:
            blocks.append(old_lines[j1:j2])
    return blocks


def parse_rows(ledger):
    rows = []
    if ledger is None:
        return rows
    for line in ledger.splitlines():
        stripped = line.strip()
        if not stripped.startswith("|"):
            continue
        cells = [cell.strip() for cell in stripped.strip("|").split("|")]
        if not cells or not VERSION_RE.match(cells[0]):
            continue
        while len(cells) < 4:
            cells.append("")
        rows.append({
            "version": cells[0],
            "description": cells[1],
            "timestamp": cells[2],
            "hash": cells[3].lower(),
        })
    return rows


run(["git", "fetch", "origin", "main", "policy/civilisational-wealth-governance"])
base_ref = run(["git", "merge-base", "HEAD", OLD_REF]).stdout.strip()
paths = run([
    "git", "diff", "--name-only", "--diff-filter=ACMR", f"{base_ref}..{OLD_REF}", "--",
    ":(glob)Governance/Charters/*.md", ":(glob)Governance/Constitution/*.md",
]).stdout.splitlines()

body_failures = []
ledger_failures = []
audited = []
excluded = []
red_team_rows = []
blocks_checked = 0

for path in sorted(set(line.strip() for line in paths if line.strip())):
    if path.endswith("Index.md"):
        continue
    if path in EXCLUDED:
        excluded.append(f"{path} — {EXCLUDED[path]}")
        continue

    old_text = git_text(OLD_REF, path)
    base_text = git_text(base_ref, path)
    current_path = ROOT / path
    current_text = current_path.read_text(encoding="utf-8") if current_path.exists() else None
    old_body, old_ledger = split_ledger(old_text)
    base_body, _ = split_ledger(base_text)
    current_body, current_ledger = split_ledger(current_text)
    audited.append(path)

    if current_text is None:
        body_failures.append(f"{path}: current repair branch is missing the file")
    elif base_text is None:
        old_block = norm_lines(old_body)
        blocks_checked += 1
        if not contains_block(norm_lines(current_body), old_block):
            body_failures.append(f"{path}: independently added old-branch instrument is not fully preserved")
    else:
        current_lines = norm_lines(current_body)
        for index, block in enumerate(added_blocks(base_body, old_body), start=1):
            blocks_checked += 1
            if not contains_block(current_lines, block):
                preview = " / ".join(block[:3])[:420]
                body_failures.append(f"{path}: missing old-branch amendment block {index}: {preview}")

    current_rows = parse_rows(current_ledger)
    by_description = {}
    for row in current_rows:
        by_description.setdefault(row["description"], []).append(row)

    for old_row in parse_rows(old_ledger):
        if old_row["timestamp"] != INCORRECT_TIMESTAMP:
            continue
        matches = by_description.get(old_row["description"], [])
        if len(matches) != 1:
            ledger_failures.append(
                f"{path}: expected exactly one current row for red-team amendment {old_row['description']!r}; found {len(matches)}"
            )
            continue
        row = matches[0]
        red_team_rows.append(
            f"{path} | {row['version']} | {row['timestamp']} | {row['hash']} | {row['description']}"
        )
        if row["timestamp"] != FIXED_TIMESTAMP:
            ledger_failures.append(
                f"{path}: red-team amendment timestamp is {row['timestamp']}, expected {FIXED_TIMESTAMP}"
            )
        if not HEX_RE.match(row["hash"]):
            ledger_failures.append(f"{path}: corrected red-team amendment is not sealed with a SHA-256 hash")

remaining_placeholder = run([
    "grep", "-R", "--line-number", "--fixed-strings", INCORRECT_TIMESTAMP,
    "Governance/Charters", "Governance/Constitution",
], check=False)
if remaining_placeholder.returncode == 0:
    ledger_failures.append("Incorrect placeholder timestamp remains:\n" + remaining_placeholder.stdout.strip())

status = "PASS" if not body_failures and not ledger_failures else "FAIL"
lines = [
    f"BRANCH DELETION SOURCE AUDIT: {status}",
    "",
    f"Repair branch HEAD: {run(['git', 'rev-parse', 'HEAD']).stdout.strip()}",
    f"Old branch HEAD: {run(['git', 'rev-parse', OLD_REF]).stdout.strip()}",
    f"Merge base: {base_ref}",
    f"Source files audited: {len(audited)}",
    f"Old-branch amendment blocks checked: {blocks_checked}",
    f"Excluded current-authoritative/generated files: {len(excluded)}",
    f"Corrected red-team ledger rows verified: {len(red_team_rows)}",
    "",
    "BODY COVERAGE FAILURES",
    "======================",
]
lines.extend(body_failures or ["None"])
lines.extend(["", "LEDGER FAILURES", "==============="])
lines.extend(ledger_failures or ["None"])
lines.extend(["", "CORRECTED RED-TEAM ROWS", "======================="])
lines.extend(red_team_rows or ["None"])
lines.extend(["", "EXCLUSIONS", "=========="])
lines.extend(excluded or ["None"])
REPORT.parent.mkdir(parents=True, exist_ok=True)
REPORT.write_text("\n".join(lines) + "\n", encoding="utf-8")
