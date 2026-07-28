#!/usr/bin/env python3
from difflib import SequenceMatcher
from pathlib import Path
import re
import subprocess

ROOT = Path(__file__).resolve().parents[2]
OLD = "origin/policy/civilisational-wealth-governance"
BAD_TS = "2026-07-26T00:00:00Z"
GOOD_TS = "2026-07-28T09:35:31Z"
REPORT = ROOT / ".github" / "Indices" / "branch-deletion-source-audit.txt"
EXCLUDED = {
    "Governance/Constitution/CAM-BS2025-AEON-003-SCH-01.md": "generated schedule",
    "Governance/Constitution/CAM-BS2025-AEON-003-SCH-03.md": "generated schedule",
    "Governance/Charters/CAM-EQ2026-OPERATIONS-008-PLATINUM.md": "current main contains the later complete red-team charter",
}
LEDGER_RE = re.compile(r"^##+\s+.*amendment\s+ledger", re.I | re.M)
NEXT_RE = re.compile(r"^##+\s+", re.M)
VERSION_RE = re.compile(r"^\d+(?:\.\d+)+$")
HEX_RE = re.compile(r"^[0-9a-f]{64}$")


def cmd(args, check=True):
    p = subprocess.run(args, cwd=ROOT, text=True, capture_output=True)
    if check and p.returncode:
        raise RuntimeError(p.stderr.strip() or p.stdout.strip())
    return p


def show(ref, path):
    p = cmd(["git", "show", f"{ref}:{path}"], False)
    return p.stdout if p.returncode == 0 else None


def split_ledger(text):
    if text is None:
        return None, None
    m = LEDGER_RE.search(text)
    if not m:
        return text, None
    tail = text[m.end():]
    n = NEXT_RE.search(tail)
    end = m.end() + n.start() if n else len(text)
    return text[:m.start()] + text[end:], text[m.start():end]


def lines(text):
    out = []
    for raw in (text or "").replace("\r\n", "\n").split("\n"):
        value = re.sub(r"\s+", " ", raw.replace("\u00a0", " ").strip())
        if not value or value == "---":
            continue
        out.append(value)
    return out


def contains(haystack, needle):
    if not needle:
        return True
    width = len(needle)
    return any(haystack[i:i + width] == needle for i in range(len(haystack) - width + 1))


def added_blocks(base, old):
    a, b = lines(base), lines(old)
    result = []
    for tag, _i1, _i2, j1, j2 in SequenceMatcher(a=a, b=b, autojunk=False).get_opcodes():
        if tag in {"insert", "replace"} and j2 > j1:
            result.append(b[j1:j2])
    return result


def rows(ledger):
    result = []
    for raw in (ledger or "").splitlines():
        s = raw.strip()
        if not s.startswith("|"):
            continue
        cells = [c.strip() for c in s.strip("|").split("|")]
        if not cells or not VERSION_RE.match(cells[0]):
            continue
        while len(cells) < 4:
            cells.append("")
        result.append({"version": cells[0], "description": cells[1], "timestamp": cells[2], "hash": cells[3].lower()})
    return result


cmd(["git", "fetch", "origin", "main", "policy/civilisational-wealth-governance"])
base = cmd(["git", "merge-base", "HEAD", OLD]).stdout.strip()
changed = cmd([
    "git", "diff", "--name-only", "--diff-filter=ACMR", f"{base}..{OLD}", "--",
    ":(glob)Governance/Charters/*.md", ":(glob)Governance/Constitution/*.md",
]).stdout.splitlines()

body_failures, ledger_failures, verified, excluded = [], [], [], []
files_audited = 0
blocks_checked = 0

for path in sorted(set(p.strip() for p in changed if p.strip())):
    if path.endswith("Index.md"):
        continue
    if path in EXCLUDED:
        excluded.append(f"{path} — {EXCLUDED[path]}")
        continue
    files_audited += 1
    old_text = show(OLD, path)
    base_text = show(base, path)
    current_text = (ROOT / path).read_text(encoding="utf-8") if (ROOT / path).exists() else None
    old_body, old_ledger = split_ledger(old_text)
    base_body, _ = split_ledger(base_text)
    current_body, current_ledger = split_ledger(current_text)

    if current_text is None:
        body_failures.append(f"{path}: file missing")
    elif base_text is None:
        blocks_checked += 1
        if not contains(lines(current_body), lines(old_body)):
            body_failures.append(f"{path}: independently added instrument not preserved")
    else:
        current_lines = lines(current_body)
        for number, block in enumerate(added_blocks(base_body, old_body), 1):
            blocks_checked += 1
            if not contains(current_lines, block):
                body_failures.append(f"{path}: missing amendment block {number}: {' / '.join(block[:3])[:380]}")

    current_by_description = {}
    for row in rows(current_ledger):
        current_by_description.setdefault(row["description"], []).append(row)
    for old_row in rows(old_ledger):
        if old_row["timestamp"] != BAD_TS:
            continue
        matches = current_by_description.get(old_row["description"], [])
        if len(matches) != 1:
            ledger_failures.append(f"{path}: expected one corrected row for {old_row['description']!r}; found {len(matches)}")
            continue
        row = matches[0]
        verified.append(f"{path} | {row['version']} | {row['timestamp']} | {row['hash']} | {row['description']}")
        if row["timestamp"] != GOOD_TS:
            ledger_failures.append(f"{path}: timestamp {row['timestamp']} != {GOOD_TS}")
        if not HEX_RE.match(row["hash"]):
            ledger_failures.append(f"{path}: corrected row is not sealed")

placeholder = cmd(["grep", "-R", "--line-number", "--fixed-strings", BAD_TS, "Governance/Charters", "Governance/Constitution"], False)
if placeholder.returncode == 0:
    ledger_failures.append("Incorrect placeholder timestamp remains:\n" + placeholder.stdout.strip())

status = "PASS" if not body_failures and not ledger_failures else "FAIL"
content = [
    f"BRANCH DELETION SOURCE AUDIT: {status}", "",
    f"Repair branch HEAD: {cmd(['git', 'rev-parse', 'HEAD']).stdout.strip()}",
    f"Old branch HEAD: {cmd(['git', 'rev-parse', OLD]).stdout.strip()}",
    f"Merge base: {base}",
    f"Source files audited: {files_audited}",
    f"Old-branch amendment blocks checked: {blocks_checked}",
    f"Corrected red-team ledger rows verified: {len(verified)}", "",
    "BODY COVERAGE FAILURES", "======================", *(body_failures or ["None"]), "",
    "LEDGER FAILURES", "===============", *(ledger_failures or ["None"]), "",
    "CORRECTED RED-TEAM ROWS", "=======================", *(verified or ["None"]), "",
    "EXCLUSIONS", "==========", *(excluded or ["None"]), "",
]
REPORT.write_text("\n".join(content), encoding="utf-8")
