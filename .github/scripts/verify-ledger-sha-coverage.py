#!/usr/bin/env python3
import argparse
import json
import os
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
SHA256_RE = re.compile(r"^[0-9a-f]{64}$")
PLACEHOLDERS = {"-", "—"}


def ledger_bounds(text: str):
    m = AMENDMENT_HEADING_RE.search(text)
    if not m:
        return None
    tail = text[m.end():]
    nxt = NEXT_HEADING_RE.search(tail)
    end = (m.end() + nxt.start()) if nxt else len(text)
    return m.start(), end


def ledger_hash_rows(text: str) -> list[str]:
    b = ledger_bounds(text)
    if not b:
        return []
    section = text[b[0]:b[1]]
    rows = []
    for line in section.splitlines():
        s = line.strip()
        if not s.startswith("|"):
            continue
        cols = [c.strip() for c in s.strip("|").split("|")]
        if not cols or not VERSION_RE.match(cols[0]):
            continue
        while len(cols) < 4:
            cols.append("")
        rows.append(cols[-1].strip())
    return rows


def infer_id(md_text: str, path: Path) -> str:
    if path.stem.startswith("CAM-"):
        return path.stem
    for line in md_text.splitlines()[:20]:
        if line.startswith("# ") and line[2:].startswith("CAM-"):
            return line[2:].split()[0]
    return path.stem




def relpath(path: Path) -> str:
    try:
        return str(path.relative_to(REPO_ROOT))
    except ValueError:
        return str(path)

def fail(msg: str):
    print(f"ERROR: {msg}")


def warn(msg: str):
    print(f"WARN: {msg}")


def verify_law_manifest() -> int:
    proc = subprocess.run([sys.executable, str(LAW_VERIFY_SCRIPT)], cwd=REPO_ROOT)
    return proc.returncode


def is_valid_settled_sha(value: str) -> bool:
    return bool(SHA256_RE.match(value)) or value in PLACEHOLDERS


def main() -> int:
    parser = argparse.ArgumentParser(description="Verify ledger SHA coverage: historical rows are strict; latest blank allowed unless strict mode.")
    parser.add_argument("--strict-latest", action="store_true", help="Treat blank/placeholder latest ledger SHA as hard error.")
    args = parser.parse_args()
    strict_latest = args.strict_latest or os.getenv("LEDGER_STRICT_LATEST", "").lower() in {"1", "true", "yes"}

    failures = []
    summary = {
        "instruments_checked": 0,
        "valid_historical_shas": 0,
        "invalid_historical_shas": 0,
        "valid_latest_shas": 0,
        "blank_latest_shas_allowed": 0,
        "blank_latest_shas_rejected": 0,
    }

    for scope_name, (folder, json_path) in SCOPES.items():
        if not json_path.exists():
            failures.append(f"{scope_name}: missing JSON index {relpath(json_path)}")
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

            hashes = ledger_hash_rows(text)
            if not hashes:
                continue
            summary["instruments_checked"] += 1

            historical = hashes[:-1]
            latest = hashes[-1]

            for h in historical:
                if is_valid_settled_sha(h):
                    summary["valid_historical_shas"] += 1
                else:
                    summary["invalid_historical_shas"] += 1
                    failures.append(f"{scope_name}:{doc_id}: historical ledger SHA is blank/placeholder/malformed in {relpath(md)}")

            if latest in ("", *PLACEHOLDERS):
                if strict_latest:
                    summary["blank_latest_shas_rejected"] += 1
                    failures.append(f"{scope_name}:{doc_id}: latest ledger SHA is blank/placeholder in {relpath(md)}")
                    continue
                summary["blank_latest_shas_allowed"] += 1
                warn(f"{scope_name}:{doc_id}: latest ledger SHA is blank/placeholder; allowed as pending finalisation in {relpath(md)}")
                continue

            if not is_valid_settled_sha(latest):
                failures.append(f"{scope_name}:{doc_id}: latest ledger SHA is malformed in {relpath(md)}")
                continue
            summary["valid_latest_shas"] += 1

            item = json_by_id.get(doc_id)
            if not item:
                failures.append(f"{scope_name}:{doc_id}: missing in {relpath(json_path)}")
                continue

            json_hash = str(item.get('HASH') or '').strip()
            if not json_hash:
                failures.append(f"{scope_name}:{doc_id}: JSON HASH is blank in {relpath(json_path)}")
                continue
            if json_hash != latest:
                failures.append(f"{scope_name}:{doc_id}: JSON HASH mismatch ({json_hash}) != ledger HASH ({latest})")

    for k, v in summary.items():
        print(f"{k}={v}")

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
