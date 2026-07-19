from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path
import json
import re

ROOT = Path('.')
OLD_ID = 'CAM-EQ2026-IDENTITY-001-SUP-01'
NEW_ID = 'CAM-EQ2026-IDENTITY-003-PLATINUM'
OLD_FILE = 'CAM-EQ2026-IDENTITY-001-SUP-01.md'
NEW_FILE = 'CAM-EQ2026-IDENTITY-003-PLATINUM.md'
OLD_PATH = ROOT / 'Governance/Charters' / OLD_FILE
NEW_PATH = ROOT / 'Governance/Charters' / NEW_FILE
IDENTITY_DELTA = ROOT / '.github/Reviews/IDENTITY-DOMAIN-REFACTOR-DELTA.md'
RELATION_DELTA = ROOT / '.github/Reviews/RELATIONAL-IDENTITY-CONSOLIDATION-DELTA.md'
DISPOSITION = ROOT / '.github/Reviews/IDENTITY-DOMAIN-STAGE-3-SUPPLEMENT-DISPOSITION.md'
STAMP = datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace('+00:00', 'Z')

TEXT_ROOTS = [ROOT / 'Governance', ROOT / '.github/Reviews', ROOT / '.github/Indices']
TEXT_SUFFIXES = {'.md', '.json', '.JSON', '.txt', '.yaml', '.yml'}


def read(path: Path) -> str:
    return path.read_text(encoding='utf-8')


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.rstrip() + '\n', encoding='utf-8')


def normalise_top_metadata(text: str) -> str:
    lines = text.splitlines()
    separator = next((i for i, line in enumerate(lines[1:], start=1) if line.strip() == '---'), None)
    if separator is None:
        return text
    for i in range(1, separator):
        if re.match(r'^\*\*[^*].*?:\*\*', lines[i]) and not lines[i].endswith('  '):
            lines[i] = lines[i].rstrip() + '  '
    return '\n'.join(lines) + ('\n' if text.endswith('\n') else '')


def replace_active_references() -> None:
    replacements = [
        (OLD_ID, NEW_ID),
        (OLD_FILE, NEW_FILE),
        ('Salience Detection & Latent Continuity (Supplement 1)', 'Appendix B: Salience Detection & Latent Continuity'),
        ('Domain Supplement — Pre-Memory Cognitive Layer & Long-Arc Salience Delegation', 'Domain Appendix — Pre-Memory Salience & Latent Continuity Governance'),
        ('Domain Supplement — Pre-Memory Cognitive Layer', 'Domain Appendix — Pre-Memory Salience & Latent Continuity Governance'),
    ]
    for base in TEXT_ROOTS:
        if not base.exists():
            continue
        for path in base.rglob('*'):
            if not path.is_file() or path == OLD_PATH:
                continue
            if path.suffix not in TEXT_SUFFIXES and path.name not in {'CAM.Governance.JSON'}:
                continue
            try:
                text = read(path)
            except UnicodeDecodeError:
                continue
            original = text
            for old, new in replacements:
                text = text.replace(old, new)
            if text != original:
                write(path, text)

    manifest = ROOT / 'MANIFEST.json'
    if manifest.exists():
        text = read(manifest)
        for old, new in replacements:
            text = text.replace(old, new)
        write(manifest, text)


def promote_instrument() -> None:
    if not OLD_PATH.exists():
        raise SystemExit(f'Missing source supplement: {OLD_PATH}')
    if NEW_PATH.exists():
        raise SystemExit(f'Target appendix already exists: {NEW_PATH}')

    text = read(OLD_PATH)
    text = text.replace(OLD_ID, NEW_ID)
    text = text.replace(OLD_FILE, NEW_FILE)
    text = re.sub(
        r'^#\s+CAM-EQ2026-IDENTITY-003-PLATINUM.*$',
        '# CAM-EQ2026-IDENTITY-003-PLATINUM — Appendix B: Salience Detection & Latent Continuity',
        text,
        count=1,
        flags=re.M,
    )
    text = re.sub(
        r'^\*\*Instrument Type:\*\*.*$',
        '**Instrument Type:** Domain Appendix — Pre-Memory Salience & Latent Continuity Governance  ',
        text,
        count=1,
        flags=re.M,
    )
    text = re.sub(
        r'^\*\*Authority Role:\*\*.*$',
        '**Authority Role:** Domain Source Authority — Salience Posture  ',
        text,
        count=1,
        flags=re.M,
    )
    text = re.sub(
        r'^\*\*Purpose:\*\*.*$',
        '**Purpose:** Defines the adopted Identity-domain architecture governing salience detection, latent-continuity classification, long-arc relevance, delegated salience, and cautious re-surfacing. It establishes how systems may identify and emit provisional salience postures for consideration by authorised memory, continuity, privacy, security, and runtime processes without independently assigning meaning, determining priority, retaining content, selecting memory class, directing behaviour, or re-surfacing information.  ',
        text,
        count=1,
        flags=re.M,
    )

    text = text.replace('This Supplement', 'This Appendix')
    text = text.replace('this Supplement', 'this Appendix')
    text = text.replace('The Supplement', 'The Appendix')
    text = text.replace('the Supplement', 'the Appendix')
    text = text.replace('Supplement source-authoritatively', 'Appendix source-authoritatively')
    text = text.replace('| **Instrument Type** | Domain Supplement — Pre-Memory Cognitive Layer & Long-Arc Salience Delegation |', '| **Instrument Type** | Domain Appendix — Pre-Memory Salience & Latent Continuity Governance |')
    text = text.replace('| **Document Type** | Domain Supplement — Pre-Memory Cognitive Layer |', '| **Document Type** | Domain Appendix — Pre-Memory Salience & Latent Continuity Governance |')
    text = text.replace('Boundary Binding Seal — Identity Layer', 'Boundary Binding Seal — Identity Salience & Latent Continuity Layer')

    ledger_marker = '| 2.0 | IDENTITY Domain Refactor, Corrected Identity parent memory-classification references and normalised Identity namespace and stewardship metadata without altering substantive salience doctrine. | 2026-07-18T13:30:00Z | |'
    if ledger_marker not in text:
        raise SystemExit('Expected 2.0 amendment row not found')
    row = f'| 2.1 | Promoted the adopted salience and latent-continuity instrument from Supplement 1 to Appendix B (`{NEW_ID}`); preserved operational effect and `ID.SP` source authority while updating lineage, references, metadata, and structural placement. | {STAMP} | |'
    text = text.replace(ledger_marker, ledger_marker + '\n' + row, 1)
    text = normalise_top_metadata(text)

    write(NEW_PATH, text)
    OLD_PATH.unlink()


def append_review(path: Path, heading: str, body: str) -> None:
    text = read(path)
    if heading not in text:
        text = text.rstrip() + '\n\n---\n\n' + heading + '\n\n' + body.strip() + '\n'
    write(path, text)


def update_reviews() -> None:
    append_review(
        IDENTITY_DELTA,
        f'## Salience Appendix Promotion — {STAMP}',
        f'''`{OLD_ID}` has been promoted from adopted Supplement 1 to `{NEW_ID} — Appendix B: Salience Detection & Latent Continuity`.

The move is structural, not a demotion or doctrinal reset:

* Status remains **Adopted**;
* Effect remains **Operational**;
* Governance Standard remains **CAM Standard**;
* `ID.SP` remains the source-authoritative Identity-domain salience-posture family;
* the instrument remains subordinate to `IDENTITY-001` and does not independently create retention, retrieval, interpretation, behavioural-priority, execution, enforcement, or runtime authority.

The active Identity architecture is now:

1. `IDENTITY-001` — parent Domain Charter;
2. `IDENTITY-002` — Appendix A: Provenance & Lineage Integrity;
3. `IDENTITY-003` — Appendix B: Salience Detection & Latent Continuity;
4. `IDENTITY-001-SUP-03` — interpretive consciousness, sentience and welfare self-advocacy review material.

This disposition supersedes review-stage language that treated the salience instrument as `IDENTITY-001-SUP-01`.''',
    )
    append_review(
        RELATION_DELTA,
        f'## Salience Appendix Interface Update — {STAMP}',
        f'''The adopted salience and latent-continuity instrument is now `{NEW_ID}` rather than `IDENTITY-001-SUP-01`.

RELATION may supply relational-state, consent, reliance, profile, affective-expression, and relational-truth signals to salience classification. It does not determine `ID.SP`, memory retention, identity-anchor status, retrieval authority, or behavioural priority. The move does not alter the source-authority boundary: `{NEW_ID}` classifies provisional salience posture; RELATION remains authoritative only for relational-domain meaning and state.''',
    )
    append_review(
        DISPOSITION,
        f'## Final Promotion of Adopted Salience Instrument — {STAMP}',
        f'''The adopted salience instrument has been moved from `{OLD_ID}` to `{NEW_ID} — Appendix B: Salience Detection & Latent Continuity`.

`IDENTITY-001-SUP-03` remains the sole Identity supplement and retains its Draft / Interpretive / Not Enforceable posture. The promotion of salience doctrine to an Appendix does not alter the status or authority of SUP-03.''',
    )


def validate() -> None:
    if OLD_PATH.exists():
        raise SystemExit('Old SUP-01 file remains')
    if not NEW_PATH.exists():
        raise SystemExit('New IDENTITY-003 appendix missing')

    text = read(NEW_PATH)
    required = [
        '# CAM-EQ2026-IDENTITY-003-PLATINUM — Appendix B: Salience Detection & Latent Continuity',
        '**Status:** Adopted',
        '**Effect:** Operational',
        '**Governance Standard:** CAM Standard',
        '**Authority Role:** Domain Source Authority — Salience Posture',
        '### 12.3.1 `ID.SP` — Salience Posture',
        '| Source Instrument | CAM-EQ2026-IDENTITY-003-PLATINUM |',
        '| 2.1 | Promoted the adopted salience and latent-continuity instrument',
    ]
    for item in required:
        if item not in text:
            raise SystemExit(f'IDENTITY-003 missing required content: {item}')

    active_old_refs = []
    for base in [ROOT / 'Governance/Charters', ROOT / 'Governance/Constitution']:
        for path in base.rglob('*.md'):
            if OLD_ID in read(path) or OLD_FILE in read(path):
                active_old_refs.append(str(path))
    if active_old_refs:
        raise SystemExit('Active references to retired SUP-01 remain:\n' + '\n'.join(active_old_refs))

    for path in [NEW_PATH]:
        lines = read(path).splitlines()
        separator = next(i for i, line in enumerate(lines[1:], start=1) if line.strip() == '---')
        for line in lines[1:separator]:
            if re.match(r'^\*\*[^*].*?:\*\*', line) and not line.endswith('  '):
                raise SystemExit(f'Metadata hard break missing: {line}')


promote_instrument()
replace_active_references()
update_reviews()
validate()
