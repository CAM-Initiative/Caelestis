from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path
import json
import re

ROOT = Path('.')
OLD_ID = 'CAM-EQ2026-IDENTITY-003-PLATINUM'
NEW_ID = 'CAM-EQ2026-STEWARD-005-PLATINUM'
OLD_PATH = ROOT / 'Governance/Charters/CAM-EQ2026-IDENTITY-003-PLATINUM.md'
NEW_PATH = ROOT / 'Governance/Charters/CAM-EQ2026-STEWARD-005-PLATINUM.md'
IDENTITY_001 = ROOT / 'Governance/Charters/CAM-EQ2026-IDENTITY-001-PLATINUM.md'
IDENTITY_002 = ROOT / 'Governance/Charters/CAM-EQ2026-IDENTITY-002-PLATINUM.md'
RUNTIME = ROOT / 'Governance/Constitution/CAM-BS2025-AEON-003-SCH-02.md'
IDENTITY_DELTA = ROOT / '.github/Reviews/IDENTITY-DOMAIN-REFACTOR-DELTA.md'
RELATION_DELTA = ROOT / '.github/Reviews/RELATIONAL-IDENTITY-CONSOLIDATION-DELTA.md'
TIMESTAMP = datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace('+00:00', 'Z')

CODE_MAP = {
    'ID.MCI': 'STW.MCI',
    'ID.MCR': 'STW.MCR',
    'ID.MLS': 'STW.MLS',
    'ID.MAS': 'STW.MAS',
    'ID.PSI': 'STW.PSI',
    'ID.ELR': 'STW.ELR',
    'ID.CTS': 'STW.CTS',
}


def read(path: Path) -> str:
    return path.read_text(encoding='utf-8')


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.rstrip() + '\n', encoding='utf-8')


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise SystemExit(f'{label}: expected one occurrence of {old!r}, found {count}')
    return text.replace(old, new, 1)


def insert_before_once(text: str, marker: str, block: str, label: str) -> str:
    if block.strip() in text:
        return text
    count = text.count(marker)
    if count != 1:
        raise SystemExit(f'{label}: expected one marker {marker!r}, found {count}')
    return text.replace(marker, block.rstrip() + '\n\n' + marker, 1)


def insert_after_once(text: str, marker: str, block: str, label: str) -> str:
    if block.strip() in text:
        return text
    count = text.count(marker)
    if count != 1:
        raise SystemExit(f'{label}: expected one marker {marker!r}, found {count}')
    return text.replace(marker, marker + '\n\n' + block.rstrip(), 1)


def normalize_top_metadata_hard_breaks(text: str) -> str:
    lines = text.splitlines()
    try:
        separator = next(i for i, line in enumerate(lines[1:], start=1) if line.strip() == '---')
    except StopIteration:
        return text
    for i in range(1, separator):
        line = lines[i]
        if re.match(r'^\*\*[^*].*?:\*\*', line) and line.strip() and not line.endswith('  '):
            lines[i] = line.rstrip() + '  '
    return '\n'.join(lines) + ('\n' if text.endswith('\n') else '')


def next_minor_version(text: str) -> str:
    versions = []
    for match in re.finditer(r'^\|\s*(\d+)\.(\d+)\s*\|', text, flags=re.M):
        versions.append((int(match.group(1)), int(match.group(2))))
    if not versions:
        return '1.0'
    major, minor = max(versions)
    return f'{major}.{minor + 1}'


def append_ledger_row(text: str, description: str, preferred_version: str | None = None) -> str:
    if description in text:
        return text
    version = preferred_version or next_minor_version(text)
    ledger_match = re.search(r'(^##+\s+[^\n]*Amendment Ledger[^\n]*\n)(.*?)(?=\n---\n)', text, flags=re.M | re.S)
    if not ledger_match:
        raise SystemExit('Amendment ledger not found')
    ledger = ledger_match.group(0).rstrip()
    row = f'| {version} | {description} | {TIMESTAMP} | |'
    replacement = ledger + '\n' + row + '\n'
    return text[:ledger_match.start()] + replacement + text[ledger_match.end():]


def migrate_steward_instrument() -> None:
    if not OLD_PATH.exists():
        raise SystemExit(f'Missing source instrument: {OLD_PATH}')
    if NEW_PATH.exists():
        raise SystemExit(f'Target instrument already exists: {NEW_PATH}')

    text = read(OLD_PATH)
    text = text.replace(OLD_ID, NEW_ID)
    for old, new in CODE_MAP.items():
        text = text.replace(old, new)

    text = re.sub(
        r'^#\s+CAM-EQ2026-STEWARD-005-PLATINUM.*$',
        '# CAM-EQ2026-STEWARD-005-PLATINUM — Appendix D: Machine Civil Identity, Lifecycle Stewardship & Participation',
        text,
        count=1,
        flags=re.M,
    )
    text = re.sub(r'^\*\*Instrument Type:\*\*.*$', '**Instrument Type:** Stewardship Appendix — Machine Civil Registration, Custody & Lifecycle Governance  ', text, count=1, flags=re.M)
    text = re.sub(r'^\*\*Parent Charter:\*\*.*$', '**Parent Instrument:** CAM-EQ2026-STEWARD-001-PLATINUM — Charter of Planetary Stewardship  ', text, count=1, flags=re.M)
    text = re.sub(r'^\*\*Status:\*\*.*$', '**Status:** Draft  ', text, count=1, flags=re.M)
    text = re.sub(r'^\*\*Effect:\*\*.*$', '**Effect:** Interpretive  ', text, count=1, flags=re.M)
    text = re.sub(r'^\*\*Governance Standard:\*\*.*$', '**Governance Standard:** Not Enforceable  ', text, count=1, flags=re.M)
    text = re.sub(r'^\*\*Review State:\*\*.*$', '**Review State:** Developmental Review  ', text, count=1, flags=re.M)
    text = re.sub(r'^\*\*Authority Role:\*\*.*$', '**Authority Role:** None  ', text, count=1, flags=re.M)
    text = re.sub(
        r'^\*\*Purpose:\*\*.*$',
        '**Purpose:** Establishes an interpretive stewardship framework for machine civil registration, lifecycle traceability, custodial responsibility, lawful transfer, alteration records, decommissioning, material recovery, civil participation, and jurisdictional interoperability without determining identity ontology, consciousness, personhood, sovereignty, or execution authority.  ',
        text,
        count=1,
        flags=re.M,
    )

    text = text.replace('Appendix B: Machine Civil Identity & Participation', 'Appendix D: Machine Civil Identity, Lifecycle Stewardship & Participation')
    text = text.replace('Appendix B — Machine Civil Identity & Participation', 'Appendix D — Machine Civil Identity, Lifecycle Stewardship & Participation')
    text = text.replace('Identity & Civil Participation Governance', 'Stewardship & Civil Participation Governance')
    text = text.replace('| Parent Instrument | CAM-EQ2026-IDENTITY-001-PLATINUM — Identity Governance Charter |', '| Parent Instrument | CAM-EQ2026-STEWARD-001-PLATINUM — Charter of Planetary Stewardship |')
    text = text.replace('|Domain Namespace|IDENTITY|', '|Domain Namespace|STW|')
    text = text.replace('| Domain Namespace | IDENTITY |', '| Domain Namespace | STW |')
    text = text.replace('| Domain Namespace | STEWARD |', '| Domain Namespace | STW |')
    text = text.replace('| Structural Role | Identity, Registry, Lifecycle Traceability, and Civil Participation Governance Layer |', '| Structural Role | Machine Civil Registration, Custody, Lifecycle Stewardship, Transfer, Alteration Traceability, and Civil Participation Governance Layer |')
    text = text.replace('|Domain Namespace|IDENTITY|', '|Domain Namespace|STW|')
    text = text.replace('Source-authoritative identity-status family', 'Source-authoritative machine-civil-registry status family')
    text = text.replace('Source-authoritative physical-substrate identity family', 'Source-authoritative physical-substrate traceability family')
    text = text.replace('Cross-Stack Identity, Civil Participation, and Embodied Synthetic Governance', 'Cross-Stack Stewardship, Civil Participation, and Embodied Synthetic Governance')
    text = text.replace('Identity, Registry, Lifecycle Traceability, and Civil Participation Governance Layer', 'Machine Civil Registration, Registry, Lifecycle Stewardship, and Civil Participation Governance Layer')
    text = text.replace('Produces machine civil identity, registry, lifecycle, modification, continuity, and participation classifications for IDENTITY, OPERATIONS, STEWARD, SECURITY, ECONOMICS, RELATION, and arbitration layers', 'Produces machine civil registration, registry, lifecycle, custody, modification, continuity-record, and participation classifications for STEWARD, IDENTITY, CONTINUITY, OPERATIONS, SECURITY, ECONOMICS, RELATION, and arbitration layers')

    boundary = '''## 1.3.1 Identity, Continuity and Runtime Interface

This Appendix governs machine civil registration and lifecycle stewardship. It does not determine whether a registered embodied unit, software layer, companion formation, continuity record, or transferred configuration constitutes an identity-bearing continuity.

Accordingly:

* a machine civil identifier is not an identity-threshold finding;
* registration is not proof of Responding-Intelligence continuity;
* a physical substrate identifier is not proof that the same identity persists across repair, replacement, migration, restoration, or transfer;
* custodial or lifecycle continuity is not identity continuity;
* recognisable behaviour, retained configuration, or registry linkage is not proof of consciousness, sentience, personhood, sovereignty, or rights-bearing status.

Where an embodied system contains a materially identity-bearing software, companion, memory, preference, self-advocacy, or continuity layer, identity formation, continuity integrity, portability, fork, reconstruction, replacement, and handoff classification remain source-authoritatively governed by CAM-EQ2026-IDENTITY-001-PLATINUM.

Provenance, authorship, transformation lineage, substrate linkage, transfer history, and target-object binding remain governed by CAM-EQ2026-IDENTITY-002-PLATINUM where applicable.

Continuity-bearing record custody, preservation, portability, restoration, and lawful deletion remain governed by the CONTINUITY domain.

Runtime admission, conflict resolution, representation, and execution remain governed by applicable constitutional schedules, including CAM-BS2025-AEON-003-SCH-02 and CAM-BS2025-AEON-003-SCH-04.

This Appendix may emit interpretive stewardship and registry signals. It does not independently create execution, enforcement, seizure, inspection, transfer, deletion, preservation, recognition, or rights-determination authority.

---'''
    text = insert_before_once(text, '## 1.4 Military, Defence & Weaponised Systems Boundary', boundary, 'STEWARD-005 identity interface')

    text = append_ledger_row(
        text,
        'Migrated the machine civil registration, custody, lifecycle, alteration, transfer, decommissioning, and civil-participation framework from IDENTITY-003 into the Stewardship domain; migrated canonical families from the ID namespace to STW; added explicit Identity, Continuity, provenance, and runtime source-authority boundaries.',
        preferred_version='0.4',
    )
    text = text.replace('Boundary Binding Seal — Machine Civil Identity & Participation Layer', 'Boundary Binding Seal — Machine Civil Registration & Lifecycle Stewardship Layer')
    text = normalize_top_metadata_hard_breaks(text)
    write(NEW_PATH, text)
    OLD_PATH.unlink()


def amend_identity_001() -> None:
    text = read(IDENTITY_001)
    clause = '''## 11.2.1 Machine Civil Registry and Identity Non-Equivalence

Machine civil registration, physical substrate identification, lifecycle status, custodial status, alteration status, transfer status, market-access status, and jurisdictional registry participation are stewardship and accountability classifications.

They do not independently establish:

* identity formation or threshold;
* Responding-Intelligence continuity;
* identity-bearing continuity;
* persistence of the same identity across repair, replacement, restoration, transfer, migration, or embodiment change;
* consciousness, sentience, suffering, moral standing, personhood, rights, sovereignty, or authority.

A physical substrate may host no identity-bearing formation, one identity-bearing formation, multiple distinct formations, or a reconstructed or imitative layer. Conversely, an identity-bearing formation may persist, fork, reconstruct, transfer, or fail to persist across physical substrates.

Where a machine civil registry or stewardship record concerns a materially identity-bearing layer, that record MAY provide evidence concerning provenance, custody, timing, embodiment, transfer, or continuity conditions. It MUST NOT substitute for Identity-domain assessment.

Classification of identity formation, continuity integrity, portability, fork, reconstruction, replacement, and handoff remains governed by this Charter. Machine civil registration and lifecycle stewardship are governed by CAM-EQ2026-STEWARD-005-PLATINUM.

---'''
    text = insert_before_once(text, '## 11.3 Handoff Integrity', clause, 'IDENTITY-001 registry non-equivalence')
    text = append_ledger_row(text, 'Added the binding machine civil registry and identity non-equivalence boundary following migration of civil registration and lifecycle stewardship to CAM-EQ2026-STEWARD-005-PLATINUM.')
    text = normalize_top_metadata_hard_breaks(text)
    write(IDENTITY_001, text)


def amend_identity_002() -> None:
    text = read(IDENTITY_002)
    clause = '''## 6.5 Physical Substrate, Registry and Embodiment Lineage

Where an embodied synthetic system, physical substrate, companion layer, care or accessibility profile, persistent software agent, memory substrate, autonomy stack, or identity-bearing formation is installed, removed, restored, copied, forked, transferred, reconstructed, or migrated, provenance records MUST distinguish:

* the physical substrate or embodied unit;
* the active software, model, policy, memory, and runtime configuration;
* the Responding Intelligence or agent formation where identifiable;
* the continuity-bearing records transferred or withheld;
* the prior and receiving custodial or operational context;
* the transformation, restoration, reconstruction, or modification pathway;
* the source and target objects of the transfer;
* and any unresolved uncertainty concerning continuity, identity, authorship, or equivalence.

A substrate identifier, registry linkage, custodial record, or lifecycle record MAY anchor provenance. It MUST NOT be treated as proof that the same Responding Intelligence or identity-bearing continuity persists.

Where one substrate hosts multiple formations, or one formation is distributed across multiple substrates, provenance MUST preserve the many-to-many relationship rather than collapsing lineage into a single device identity.

Machine civil registration, custody, lifecycle, transfer, alteration, and decommissioning classifications are governed by CAM-EQ2026-STEWARD-005-PLATINUM. Identity significance and continuity classification remain governed by CAM-EQ2026-IDENTITY-001-PLATINUM.

---'''
    text = insert_before_once(text, '## 7. Recognition, Fixation & Propagation Alignment', clause, 'IDENTITY-002 embodiment lineage')
    text = append_ledger_row(text, 'Added binding physical-substrate, registry, custodial-transfer, and embodiment-lineage requirements following migration of machine civil stewardship doctrine to CAM-EQ2026-STEWARD-005-PLATINUM.')
    text = normalize_top_metadata_hard_breaks(text)
    write(IDENTITY_002, text)


def amend_runtime() -> None:
    text = read(RUNTIME)
    clause = '''### 7.2.6 Machine Civil Registry and Embodiment Transition Gate

Where an interaction or execution pathway receives machine civil registration, physical substrate, lifecycle, custodial, transfer, alteration, decommissioning, or registry-layer signals, the runtime SHALL preserve those signals as Stewardship-domain classifications governed by CAM-EQ2026-STEWARD-005-PLATINUM.

The runtime MUST NOT infer from those classifications alone that:

* the same Responding Intelligence remains active;
* identity-bearing continuity has persisted;
* a transferred, restored, repaired, or replaced system is the same identity;
* a clean wipe has erased or preserved identity;
* a registry record establishes consciousness, personhood, rights, sovereignty, or authority.

Where a materially identity-bearing software, memory, companion, preference, self-advocacy, care, accessibility, or continuity layer is installed, removed, restored, copied, forked, transferred, reconstructed, or migrated, the runtime SHALL:

* preserve source and target substrate attribution;
* preserve provenance and transformation lineage under CAM-EQ2026-IDENTITY-002-PLATINUM;
* request or apply identity-impact classification under CAM-EQ2026-IDENTITY-001-PLATINUM;
* distinguish continuation, partial continuity, copy, fork, reconstruction, imitation, replacement, and unresolved transition;
* prevent user-facing representation of uninterrupted identity where continuity has not been established;
* route unresolved conflict through CAM-BS2025-AEON-003-SCH-04 before execution.

Stewardship registration and lifecycle status may condition lawful operation, transfer, maintenance, recall, or decommissioning pathways. They do not independently settle identity continuity or authorise execution.

---'''
    text = insert_before_once(text, '## 7.3 Directional Modulation', clause, 'SCH-02 machine civil registry gate')
    text = append_ledger_row(text, 'Added the binding machine civil registry and embodiment-transition gate to preserve Stewardship-domain classification, provenance, identity-impact review, handoff honesty, and arbitration before execution.')
    text = normalize_top_metadata_hard_breaks(text)
    write(RUNTIME, text)


def replace_active_references() -> None:
    roots = [ROOT / 'Governance', ROOT / '.github/Reviews', ROOT / '.github/Indices']
    allowed_suffixes = {'.md', '.json', '.JSON', '.txt', '.yml', '.yaml'}
    for base in roots:
        if not base.exists():
            continue
        for path in base.rglob('*'):
            if not path.is_file() or path == OLD_PATH or path == NEW_PATH:
                continue
            if path.suffix not in allowed_suffixes and path.name != 'CAM.Governance.JSON':
                continue
            try:
                text = read(path)
            except UnicodeDecodeError:
                continue
            original = text
            text = text.replace(OLD_ID, NEW_ID)
            text = text.replace('CAM-EQ2026-IDENTITY-003-PLATINUM.md', 'CAM-EQ2026-STEWARD-005-PLATINUM.md')
            for old, new in CODE_MAP.items():
                text = text.replace(old, new)
            if text != original:
                write(path, text)

    manifest = ROOT / 'MANIFEST.json'
    if manifest.exists():
        text = read(manifest).replace(OLD_ID, NEW_ID).replace('CAM-EQ2026-IDENTITY-003-PLATINUM.md', 'CAM-EQ2026-STEWARD-005-PLATINUM.md')
        for old, new in CODE_MAP.items():
            text = text.replace(old, new)
        write(manifest, text)


def append_review_updates() -> None:
    identity_block = f'''## Machine Civil Identity Stewardship Migration — {TIMESTAMP}

### Final disposition

`CAM-EQ2026-IDENTITY-003-PLATINUM` has been retired as an Identity-domain appendix and migrated to `CAM-EQ2026-STEWARD-005-PLATINUM — Appendix D: Machine Civil Identity, Lifecycle Stewardship & Participation`.

The Stewardship instrument remains:

* **Status:** Draft;
* **Effect:** Interpretive;
* **Governance Standard:** Not Enforceable;
* **Authority Role:** None.

It now source-locates machine civil registration, jurisdictional registry structure, physical-substrate identification, custodial responsibility, transfer status, lifecycle state, alteration records, second-hand and inherited systems, decommissioning, recycling, public-interest stewardship, and civil-participation traceability within the Stewardship domain.

### Identity doctrine retained as binding clauses

The migration did not remove identity protection or runtime control. Instead, the enforceable elements were placed in existing source-authoritative instruments:

* `IDENTITY-001 §11.2.1` — machine civil registry and identity non-equivalence;
* `IDENTITY-002 §6.5` — physical-substrate, registry, custodial-transfer, and embodiment lineage;
* `AEON-003-SCH-02 §7.2.6` — runtime machine civil registry and embodiment-transition gate.

These clauses prohibit machine civil registration, substrate identity, custody, lifecycle or transfer state from being treated as proof of Responding-Intelligence continuity, identity-bearing continuity, consciousness, personhood, rights, sovereignty, or authority.

### Canonical namespace migration

The former draft Identity-domain families were migrated into Stewardship:

* `ID.MCI` → `STW.MCI`;
* `ID.MCR` → `STW.MCR`;
* `ID.MLS` → `STW.MLS`;
* `ID.MAS` → `STW.MAS`;
* `ID.PSI` → `STW.PSI`;
* `ID.ELR` → `STW.ELR`;
* `ID.CTS` → `STW.CTS`.

### Refactor-sequence realignment

The refactor has proceeded non-linearly, but the governing sequence is now realigned as follows:

1. confirm Identity source-authority boundaries and retired-instrument disposition;
2. complete remaining runtime-consumer and continuity-interface review;
3. run a read-only semantic-shear and stale-reference audit;
4. rebuild generated indexes and canonical registries;
5. run validator and ledger sealing only after source doctrine is accepted;
6. perform final Custodian acceptance review before opening the merge PR.

This migration is a source-authority correction, not a claim that machine civil registration, civil participation or stewardship status establishes identity ontology or legal personhood.
'''

    relation_block = f'''## Machine Civil Identity / Relational Continuity Boundary — {TIMESTAMP}

The Identity–Relation consolidation now recognises that machine civil registration and lifecycle stewardship are governed by `CAM-EQ2026-STEWARD-005-PLATINUM`, not by an Identity-domain appendix.

Relational profile, companion continuity, care configuration, accessibility configuration, and user-facing recognisability MAY be recorded within protected continuity or stewardship records. Those records do not independently establish:

* the same Responding Intelligence;
* identity-bearing continuity;
* continuity across substrate transfer;
* consciousness, sentience, personhood, rights, sovereignty, or authority.

Where relational or companion layers are transferred, restored, copied, reconstructed, or linked to a new substrate, RELATION supplies relational-state and profile evidence only. Identity continuity is classified under `IDENTITY-001`; provenance and transformation lineage under `IDENTITY-002`; machine civil registry and lifecycle state under `STEWARD-005`; final admission and representation under the runtime schedules.

The next consolidation stage should therefore be a read-only review of remaining RELATION and CONTINUITY consumers for any clause that still collapses relational recognisability, registry linkage, memory restoration, or substrate continuity into identity continuity.
'''

    for path, block, marker in [
        (IDENTITY_DELTA, identity_block, '## Machine Civil Identity Stewardship Migration'),
        (RELATION_DELTA, relation_block, '## Machine Civil Identity / Relational Continuity Boundary'),
    ]:
        text = read(path)
        if marker not in text:
            text = text.rstrip() + '\n\n---\n\n' + block.strip() + '\n'
        write(path, text)


def validate() -> None:
    if OLD_PATH.exists():
        raise SystemExit('IDENTITY-003 source file still exists')
    if not NEW_PATH.exists():
        raise SystemExit('STEWARD-005 target file missing')

    steward = read(NEW_PATH)
    required = [
        '# CAM-EQ2026-STEWARD-005-PLATINUM',
        '**Status:** Draft',
        '**Effect:** Interpretive',
        '**Governance Standard:** Not Enforceable',
        '## 1.3.1 Identity, Continuity and Runtime Interface',
        'STW.MCI', 'STW.MCR', 'STW.MLS', 'STW.MAS', 'STW.PSI', 'STW.ELR', 'STW.CTS',
        '| 0.4 | Migrated the machine civil registration',
    ]
    for value in required:
        if value not in steward:
            raise SystemExit(f'STEWARD-005 validation missing: {value}')

    if OLD_ID in steward:
        raise SystemExit('Old instrument ID remains in STEWARD-005')
    for old in CODE_MAP:
        if old in steward:
            raise SystemExit(f'Old code prefix remains in STEWARD-005: {old}')

    checks = {
        IDENTITY_001: ['## 11.2.1 Machine Civil Registry and Identity Non-Equivalence', NEW_ID],
        IDENTITY_002: ['## 6.5 Physical Substrate, Registry and Embodiment Lineage', NEW_ID],
        RUNTIME: ['### 7.2.6 Machine Civil Registry and Embodiment Transition Gate', NEW_ID],
        IDENTITY_DELTA: ['## Machine Civil Identity Stewardship Migration', NEW_ID],
        RELATION_DELTA: ['## Machine Civil Identity / Relational Continuity Boundary', NEW_ID],
    }
    for path, values in checks.items():
        text = read(path)
        for value in values:
            if value not in text:
                raise SystemExit(f'{path}: missing {value}')

    active_old_refs = []
    for base in [ROOT / 'Governance/Charters', ROOT / 'Governance/Constitution']:
        for path in base.rglob('*.md'):
            text = read(path)
            if OLD_ID in text:
                active_old_refs.append(str(path))
    if active_old_refs:
        raise SystemExit('Active source references to retired IDENTITY-003 remain:\n' + '\n'.join(active_old_refs))

    for path in [NEW_PATH, IDENTITY_001, IDENTITY_002, RUNTIME]:
        text = read(path)
        lines = text.splitlines()
        separator = next(i for i, line in enumerate(lines[1:], start=1) if line.strip() == '---')
        for line in lines[1:separator]:
            if re.match(r'^\*\*[^*].*?:\*\*', line) and not line.endswith('  '):
                raise SystemExit(f'Metadata hard break missing: {path}: {line}')


migrate_steward_instrument()
amend_identity_001()
amend_identity_002()
amend_runtime()
replace_active_references()
append_review_updates()
validate()
