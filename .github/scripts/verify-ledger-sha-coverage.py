#!/usr/bin/env python3
import json
import re
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
LAW_VERIFY_SCRIPT = REPO_ROOT / ".github" / "scripts" / "verify-law-manifest-integrity.py"

SCOPES = {
    "Constitution": (REPO_ROOT / "Governance" / "Constitution", REPO_ROOT / "Governance" / "Constitution" / "constitution.index.json"),
    "Charters": (REPO_ROOT / "Governance" / "Charters", REPO_ROOT / "Governance" / "Charters" / "charters.index.json"),
}

EXCLUDED_IDS = {"CAM-BS2025-AEON-003-SCH-01", "CAM-BS2025-AEON-003-SCH-03"}
AMENDMENT_HEADING_RE = re.compile(r"^##+\s+.*amendment\s+ledger", re.IGNORECASE | re.MULTILINE)
NEXT_HEADING_RE = re.compile(r"^##+\s+", re.MULTILINE)
VERSION_RE = re.compile(r"^\d+\.\d+$")


def ledger_bounds(text: str):
    m = AMENDMENT_HEADING_RE.search(text)
    if not m:
        return None
    tail = text[m.end():]
    nxt = NEXT_HEADING_RE.search(tail)
    end = (m.end() + nxt.start()) if nxt else len(text)
    return m.start(), end


def latest_ledger_hash(text: str):
    b = ledger_bounds(text)
    if not b:
        return None
    section = text[b[0]:b[1]]
    latest = None
    for line in section.splitlines():
        s = line.strip()
        if not s.startswith("|"):
            continue
        cols = [c.strip() for c in s.strip("|").split("|")]
        if not cols or not VERSION_RE.match(cols[0]):
            continue
        while len(cols) < 4:
            cols.append("")
        latest = cols[-1].strip()
    return latest


def infer_id(md_text: str, path: Path) -> str:
    for line in md_text.splitlines()[:20]:
        if line.startswith("# ") and line[2:].startswith("CAM-"):
            return line[2:].split()[0]
    return path.stem


def fail(msg: str):
    print(f"ERROR: {msg}")


def verify_law_manifest() -> int:
    proc = subprocess.run([sys.executable, str(LAW_VERIFY_SCRIPT)], cwd=REPO_ROOT)
    return proc.returncode


def main() -> int:
    failures = []
    for scope_name, (folder, json_path) in SCOPES.items():
        if not json_path.exists():
            failures.append(f"{scope_name}: missing JSON index {json_path.relative_to(REPO_ROOT)}")
            continue
        payload = json.loads(json_path.read_text(encoding='utf-8'))
        json_by_id = {str(i.get('id') or '').strip(): i for i in payload.get('items', [])}

        for md in sorted(folder.glob('*.md')):
            if md.name.endswith('Index.md'):
                continue
            text = md.read_text(encoding='utf-8')
            doc_id = infer_id(text, md)
            if doc_id in EXCLUDED_IDS:
                continue

            has_ledger = ledger_bounds(text) is not None
            if not has_ledger:
                continue

            doc_hash = latest_ledger_hash(text)
            if doc_hash in (None, '', '-', '—'):
                failures.append(f"{scope_name}:{doc_id}: latest ledger SHA is blank/placeholder in {md.relative_to(REPO_ROOT)}")
                continue

            item = json_by_id.get(doc_id)
            if not item:
                failures.append(f"{scope_name}:{doc_id}: missing in {json_path.relative_to(REPO_ROOT)}")
                continue

            json_hash = str(item.get('HASH') or '').strip()
            if not json_hash:
                failures.append(f"{scope_name}:{doc_id}: JSON HASH is blank in {json_path.relative_to(REPO_ROOT)}")
                continue
            if json_hash != doc_hash:
                failures.append(
                    f"{scope_name}:{doc_id}: JSON HASH mismatch ({json_hash}) != ledger HASH ({doc_hash})"
                )

    if failures:
        for f in failures:
            fail(f)
        return 1

    law_status = verify_law_manifest()
    if law_status != 0:
        return law_status

    print('Ledger SHA coverage (Constitution/Charters) and Law manifest integrity passed.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
