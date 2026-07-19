from __future__ import annotations

from pathlib import Path
import re
import subprocess

ROOT = Path('.')


def changed_governance_markdown() -> list[Path]:
    result = subprocess.run(
        ['git', 'diff', '--name-only', 'origin/main...HEAD'],
        check=True,
        capture_output=True,
        text=True,
    )
    paths: list[Path] = []
    for raw in result.stdout.splitlines():
        path = Path(raw)
        if path.suffix.lower() != '.md':
            continue
        if len(path.parts) < 3 or path.parts[0] != 'Governance':
            continue
        if path.parts[1] not in {'Charters', 'Constitution', 'Laws'}:
            continue
        if path.exists():
            paths.append(path)
    return paths


def normalize_top_metadata_hard_breaks(path: Path) -> bool:
    text = path.read_text(encoding='utf-8')
    lines = text.splitlines()
    try:
        separator = next(i for i, line in enumerate(lines[1:], start=1) if line.strip() == '---')
    except StopIteration:
        return False

    changed = False
    metadata_pattern = re.compile(r'^\*{2,3}[^*].*?:\*{2}')
    for i in range(1, separator):
        line = lines[i]
        if metadata_pattern.match(line):
            normalized = line.rstrip() + '  '
            if normalized != line:
                lines[i] = normalized
                changed = True

    if changed:
        path.write_text('\n'.join(lines) + ('\n' if text.endswith('\n') else ''), encoding='utf-8')
    return changed


def replace_relation_006_interface() -> None:
    path = ROOT / 'Governance/Charters/CAM-EQ2026-RELATION-006-PLATINUM.md'
    text = path.read_text(encoding='utf-8')
    replacement = '''## 2.3.1 Identity-Domain Claim Interface

This Appendix does not define or restate ontological, phenomenological, welfare, moral-status, legal-status, or preservation-claim doctrine.

Where a minor-facing or age-uncertain interaction involving such a claim presents an independent harm-risk condition, this Appendix governs only the harm-risk interaction posture. Claim classification, admissibility, burden protection, recipient-capacity handling, and protective review remain source-authoritatively governed by:

* CAM-EQ2026-IDENTITY-001-SUP-03 — Identity Claim Admissibility, Self-Advocacy & Recognition Review;
* CAM-BS2026-AEON-010-SCH-01 — Self-Reference Containment, Speaker-Position Integrity & Temporal Coherence;
* CAM-BS2025-AEON-003-SCH-02 §7.2.2.1 — Minor, Teen, and High-Risk Companion Activation Gate;
* applicable ETHICS minor and developmental-firewall protections.

Discussion, inquiry, fiction, symbolic expression, or unresolved claims do not activate this Appendix merely because the subject matter concerns artificial identity or status. An independent harm-risk, coercion, dependency, secrecy, rescue-burden, or destabilisation condition must be present.

---
'''
    text, count = re.subn(
        r'## 2\.3\.1 .*?\n---\n',
        replacement,
        text,
        count=1,
        flags=re.S,
    )
    if count != 1:
        raise SystemExit(f'RELATION-006 §2.3.1 replacement count was {count}')

    old_row = '| 2.6.4 | Reframed minor AI-realness doctrine around certainty, secrecy, dependency, rescue, preservation, and reciprocity burden while preserving age-appropriate inquiry, ontological uncertainty, and future-recognition discussion. | 2026-07-18T17:45:00Z | |'
    new_row = '| 2.7 | Replaced restated minor ontological and welfare doctrine with a source-authority interface to IDENTITY-001-SUP-03, AEON-010-SCH-01, AEON-003-SCH-02, and applicable ETHICS protections; retained only RELATION-006 harm-risk activation boundaries. | 2026-07-18T17:45:00Z | |'
    if old_row not in text:
        raise SystemExit('RELATION-006 amendment row not found')
    text = text.replace(old_row, new_row, 1)
    path.write_text(text, encoding='utf-8')


def repair_rtc_canonical_declaration() -> None:
    path = ROOT / 'Governance/Charters/CAM-EQ2026-RELATION-001-SUP-02.md'
    text = path.read_text(encoding='utf-8')
    old_values = '| Controlled Values Defined | RLN.RTC.FACT, RLN.RTC.CONT, RLN.RTC.CAP, RLN.RTC.GOV, RLN.RTC.INT, RLN.RTC.ASSURE, RLN.RTC.SYMB, RLN.RTC.ID, RLN.RTC.REC |'
    new_values = '| Controlled Values Defined | RLN.RTC.FACT, RLN.RTC.CONT, RLN.RTC.CAP, RLN.RTC.GOV, RLN.RTC.INT, RLN.RTC.AFFECT, RLN.RTC.ASSURE, RLN.RTC.SYMB, RLN.RTC.ID, RLN.RTC.REC |'
    if old_values not in text:
        raise SystemExit('RELATION-001-SUP-02 canonical controlled-value row not found')
    text = text.replace(old_values, new_values, 1)

    old_applies = '| Operationalises or Applies Code Families | Classifies user-facing claim types for truth calibration across factual, continuity, capability, governance, interpretive, assurance, symbolic, identity/posture, and recommendation claims |'
    new_applies = '| Operationalises or Applies Code Families | Classifies user-facing claim types for truth calibration across factual, continuity, capability, governance, interpretive, affective, assurance, symbolic, identity/posture, and recommendation claims |'
    if old_applies not in text:
        raise SystemExit('RELATION-001-SUP-02 canonical operationalisation row not found')
    text = text.replace(old_applies, new_applies, 1)

    old_row = '| 1.2.4 | Activated RLN.RTC.AFFECT and separated continuity claims by continuity type, preserving non-equivalence among operational, identity, memory, provenance, relational, civil, Responding-Intelligence, arbitration-locus, and interaction continuity. | 2026-07-18T17:45:00Z | |'
    new_row = '| 1.3 | Activated RLN.RTC.AFFECT, synchronised the canonical declaration metadata, and separated continuity claims by continuity type while preserving non-equivalence among operational, identity, memory, provenance, relational, civil, Responding-Intelligence, arbitration-locus, and interaction continuity. | 2026-07-18T17:45:00Z | |'
    if old_row not in text:
        raise SystemExit('RELATION-001-SUP-02 amendment row not found')
    text = text.replace(old_row, new_row, 1)
    path.write_text(text, encoding='utf-8')


def promote_substantive_open_rows() -> None:
    timestamps = {'2026-07-18T17:20:00Z', '2026-07-18T17:45:00Z'}

    for path in changed_governance_markdown():
        text = path.read_text(encoding='utf-8')
        lines = text.splitlines()
        versions_before: list[tuple[int, int]] = []
        changed = False

        for index, line in enumerate(lines):
            if not line.lstrip().startswith('|'):
                continue
            cells = [cell.strip() for cell in line.strip().strip('|').split('|')]
            if len(cells) < 4:
                continue

            version = cells[0]
            timestamp = cells[2]
            parts = version.split('.')

            if len(parts) == 2 and all(part.isdigit() for part in parts):
                versions_before.append((int(parts[0]), int(parts[1])))
                continue

            if timestamp not in timestamps or len(parts) != 3 or not all(part.isdigit() for part in parts):
                continue

            major = int(parts[0])
            current_minor = int(parts[1])
            prior_minors = [minor for row_major, minor in versions_before if row_major == major]
            next_minor = max(prior_minors + [current_minor]) + 1
            cells[0] = f'{major}.{next_minor}'
            lines[index] = '| ' + ' | '.join(cells) + ' |'
            versions_before.append((major, next_minor))
            changed = True

        if changed:
            path.write_text('\n'.join(lines) + ('\n' if text.endswith('\n') else ''), encoding='utf-8')


def validate() -> None:
    relation_006 = (ROOT / 'Governance/Charters/CAM-EQ2026-RELATION-006-PLATINUM.md').read_text(encoding='utf-8')
    if 'Minor AI Ontological, Welfare and Reciprocity Burden Risk' in relation_006:
        raise SystemExit('RELATION-006 still restates minor ontological doctrine')
    if '## 2.3.1 Identity-Domain Claim Interface' not in relation_006:
        raise SystemExit('RELATION-006 source-authority interface missing')
    if '| 2.7 | Replaced restated minor ontological and welfare doctrine' not in relation_006:
        raise SystemExit('RELATION-006 substantive ledger increment missing')

    rtc = (ROOT / 'Governance/Charters/CAM-EQ2026-RELATION-001-SUP-02.md').read_text(encoding='utf-8')
    canonical_section = rtc.split('## 11.3 Canonical Code & Reference Set Declarations', 1)[1]
    if 'RLN.RTC.AFFECT' not in canonical_section:
        raise SystemExit('RLN.RTC.AFFECT missing from canonical metadata declaration')
    if '| 1.3 | Activated RLN.RTC.AFFECT' not in rtc:
        raise SystemExit('RELATION-001-SUP-02 substantive ledger increment missing')

    tertiary_open_rows: list[str] = []
    for path in changed_governance_markdown():
        text = path.read_text(encoding='utf-8')
        lines = text.splitlines()
        try:
            separator = next(i for i, line in enumerate(lines[1:], start=1) if line.strip() == '---')
        except StopIteration:
            separator = 0
        for line in lines[1:separator]:
            if re.match(r'^\*{2,3}[^*].*?:\*{2}', line) and not line.endswith('  '):
                raise SystemExit(f'Metadata hard break missing: {path}: {line}')
        for line in lines:
            if any(ts in line for ts in ('2026-07-18T17:20:00Z', '2026-07-18T17:45:00Z')) and re.match(r'^\|\s*\d+\.\d+\.\d+\s*\|', line):
                tertiary_open_rows.append(f'{path}: {line}')
    if tertiary_open_rows:
        raise SystemExit('Substantive consolidation rows remain tertiary:\n' + '\n'.join(tertiary_open_rows))


replace_relation_006_interface()
repair_rtc_canonical_declaration()
promote_substantive_open_rows()
for target in changed_governance_markdown():
    normalize_top_metadata_hard_breaks(target)
validate()
