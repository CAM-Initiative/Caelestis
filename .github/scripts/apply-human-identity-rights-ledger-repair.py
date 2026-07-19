from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[2]
TIMESTAMP = datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def write(path: str, text: str) -> None:
    (ROOT / path).write_text(text, encoding="utf-8")


def replace_once(text: str, old: str, new: str, *, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"{label}: expected exactly one match, found {count}")
    return text.replace(old, new, 1)


# 1. CONTINUITY-001: move the declaration interface under likeness and separate ledger provenance.
path = "Governance/Charters/CAM-EQ2026-CONTINUITY-001-PLATINUM.md"
text = read(path)

section_pattern = re.compile(
    r"### 9\.4\.1 External Human Identity-Rights Declaration Interface\n\n"
    r".*?"
    r"No particular external protocol is the exclusive means of establishing consent, restriction, rights ownership, or lawful authority under this Charter\.\n\n---\n\n",
    re.DOTALL,
)
match = section_pattern.search(text)
if not match:
    raise RuntimeError("CONTINUITY-001: could not locate §9.4.1 declaration interface")
section = match.group(0)
section = section.removesuffix("---\n\n")
section = section.replace(
    "### 9.4.1 External Human Identity-Rights Declaration Interface",
    "### 9.5.1 External Human Identity-Rights Declaration Interface",
    1,
)
text = text[: match.start()] + text[match.end() :]

target = (
    "Reasonable interpretation SHALL be assessed from the perspective of an ordinary user, not solely from system intent, technical architecture, or provider description.\n\n"
    "---\n\n"
    "## 9.6 Deceptive Invocation"
)
replacement = (
    "Reasonable interpretation SHALL be assessed from the perspective of an ordinary user, not solely from system intent, technical architecture, or provider description.\n\n"
    + section
    + "---\n\n"
    + "## 9.6 Deceptive Invocation"
)
text = replace_once(text, target, replacement, label="CONTINUITY-001 §9.5 insertion")

text = replace_once(
    text,
    "aligned final runtime arbitration with SCH-04 and execution sequencing with SCH-02. VIGIL-2026-PATCH-0024 |",
    "aligned final runtime arbitration with SCH-04 and execution sequencing with SCH-02. |",
    label="CONTINUITY-001 ledger 1.10 provenance",
)

if "| 1.11 | Added §9.5.1 External Human Identity-Rights Declaration Interface" not in text:
    ledger_anchor = re.compile(r"(\| 1\.10 \|[^\n]*\n)")
    row = (
        "| 1.11 | Added §9.5.1 External Human Identity-Rights Declaration Interface, establishing a vendor-neutral interface for external declarations concerning human name, image, likeness, voice, movement, signature, and professional or personal persona; separated external rights evidence from Identity-domain ontology, legal determination, and runtime execution authority. VIGIL-2026-PROP-0016; VIGIL-2026-PATCH-0024. | "
        f"{TIMESTAMP} | |\n"
    )
    text, count = ledger_anchor.subn(r"\1" + row, text, count=1)
    if count != 1:
        raise RuntimeError("CONTINUITY-001: could not insert ledger row 1.11")

write(path, text)


# 2. CONTINUITY-001-SUP-01: format states and complete CBR.RIGHTS canonical declarations.
path = "Governance/Charters/CAM-EQ2026-CONTINUITY-001-SUP-01.md"
text = read(path)

old_states = """`PERMITTED`;
`CONDITIONAL`;
`PROHIBITED`;
`ABSENT`;
`NON_OPERATIVE`;
`CONFLICTING`;
`REVOKED_OR_STALE`;
`UNVERIFIED`;
`UNKNOWN`."""
new_states = """* `PERMITTED`;
* `CONDITIONAL`;
* `PROHIBITED`;
* `ABSENT`;
* `NON_OPERATIVE`;
* `CONFLICTING`;
* `REVOKED_OR_STALE`;
* `UNVERIFIED`;
* `UNKNOWN`."""
text = replace_once(text, old_states, new_states, label="CONTINUITY SUP §3.1 state formatting")

old_values = "CBR.MEM, CBR.PREF, CBR.REL, CBR.RES, CBR.SUM, CBR.USAGE, CBR.PROV, CBR.DER, CBR.PORT, CBR.DISS"
new_values = "CBR.MEM, CBR.PREF, CBR.REL, CBR.RES, CBR.SUM, CBR.USAGE, CBR.RIGHTS, CBR.PROV, CBR.DER, CBR.PORT, CBR.DISS"
count = text.count(old_values)
if count != 2:
    raise RuntimeError(f"CONTINUITY SUP: expected two canonical controlled-value lists, found {count}")
text = text.replace(old_values, new_values)

text = replace_once(
    text,
    "| 1.5 | Incorporated new code ```CBR.RIGHTS``` associated with VIGIL-2026-PATCH-0024 | 2026-07-19T14:19:00Z | 57b50ccbac996081c396714e10ef397af280858803da37a7ad04accf35161467 |",
    "| 1.5 | Established `CBR.RIGHTS` — External Human Identity-Rights Declaration Record; added §3.1 declaration content, operational declaration states, lifecycle and portability-preservation requirements, and source-authoritative CBR controlled-value alignment. VIGIL-2026-PROP-0016; VIGIL-2026-PATCH-0024. | 2026-07-19T14:19:00Z | 57b50ccbac996081c396714e10ef397af280858803da37a7ad04accf35161467 |",
    label="CONTINUITY SUP ledger 1.5",
)
write(path, text)


# 3. OPERATIONS-004: repair copied list formatting and strengthen ledger provenance.
path = "Governance/Charters/CAM-EQ2026-OPERATIONS-004-PLATINUM.md"
text = read(path)
text = replace_once(
    text,
    "* conflicts with other declarations, contracts, laws, court orders, estate instructions, guild * requirements, or platform obligations.",
    "* conflicts with other declarations, contracts, laws, court orders, estate instructions, guild requirements, or platform obligations.",
    label="OPERATIONS guild requirements formatting",
)

old_state_block = """`PERMITTED` — records affirmative rights evidence within the verified scope but does not independently authorise execution;
`CONDITIONAL` — prevents the implicated use until applicable clearance conditions are satisfied and verified;
`PROHIBITED` — emits a blocking rights-use constraint for the implicated use;
`ABSENT` or `NON_OPERATIVE` — establishes only that no usable affirmative declaration has been verified;
`CONFLICTING` — preserves all conflicting declarations and routes the conflict for resolution;
`REVOKED_OR_STALE` — prevents reliance on the prior declaration unless a current operative state is established;
`UNVERIFIED` or `UNKNOWN` — prevents representation that permission has been established."""
new_state_block = """* `PERMITTED` — records affirmative rights evidence within the verified scope but does not independently authorise execution;
* `CONDITIONAL` — prevents the implicated use until applicable clearance conditions are satisfied and verified;
* `PROHIBITED` — emits a blocking rights-use constraint for the implicated use;
* `ABSENT` or `NON_OPERATIVE` — establishes only that no usable affirmative declaration has been verified;
* `CONFLICTING` — preserves all conflicting declarations and routes the conflict for resolution;
* `REVOKED_OR_STALE` — prevents reliance on the prior declaration unless a current operative state is established;
* `UNVERIFIED` or `UNKNOWN` — prevents representation that permission has been established."""
text = replace_once(text, old_state_block, new_state_block, label="OPERATIONS declaration-state formatting")
text = replace_once(
    text,
    "* does not replace applicable law, contract, consent, privacy, copyright, publicity, * personality-rights, child-protection, estate, or ethical requirements.",
    "* does not replace applicable law, contract, consent, privacy, copyright, publicity, personality-rights, child-protection, estate, or ethical requirements.",
    label="OPERATIONS personality-rights formatting",
)
text = replace_once(
    text,
    "| 1.14 | Added new External Human Identity-Rights Declaration Verification section, VIGIL-2026-PATCH-0024 | 2026-07-19T13:48:00Z | b57ec6614d78399fa3216312db6f2b3daff46c2c5d03c638421f3a5643b6fab6 |",
    "| 1.14 | Added §4.5 External Human Identity-Rights Declaration Verification, including rights-subject and use-scope verification, source and representative-authority assessment, declaration lifecycle and conflict handling, conditional-clearance requirements, minor protections, and separation from Identity-domain and execution authority. VIGIL-2026-PROP-0016; VIGIL-2026-PATCH-0024. | 2026-07-19T13:48:00Z | b57ec6614d78399fa3216312db6f2b3daff46c2c5d03c638421f3a5643b6fab6 |",
    label="OPERATIONS ledger 1.14",
)
write(path, text)


# 4. SECURITY-002: separate PATCH-0022 and PATCH-0024 ledger provenance.
path = "Governance/Charters/CAM-EQ2026-SECURITY-002-PLATINUM.md"
text = read(path)
text = replace_once(
    text,
    "Provenance: VIGIL-2026-PATCH-0022 and VIGIL-2026-PATCH-0024",
    "Provenance: VIGIL-2026-PATCH-0022",
    label="SECURITY ledger 1.11 provenance",
)
if "| 1.12 | Added §2.2.12.1 External Human Identity-Rights Declaration Integrity" not in text:
    anchor = re.compile(r"(\| 1\.11 \|[^\n]*\n)")
    row = (
        "| 1.12 | Added §2.2.12.1 External Human Identity-Rights Declaration Integrity, establishing rights-subject binding, source and representative-authority integrity, declaration-lifecycle protection, anti-forgery, anti-poisoning, anti-replay, restriction-preservation, and unresolved-conflict signalling. VIGIL-2026-PROP-0016; VIGIL-2026-PATCH-0024. | "
        f"{TIMESTAMP} | |\n"
    )
    text, count = anchor.subn(r"\1" + row, text, count=1)
    if count != 1:
        raise RuntimeError("SECURITY-002: could not insert ledger row 1.12")
write(path, text)


# 5. AEON-003-SCH-02: remove collision from 3.7 and add a dedicated 3.8 row.
path = "Governance/Constitution/CAM-BS2025-AEON-003-SCH-02.md"
text = read(path)
text = replace_once(
    text,
    "and arbitration before execution. VIGIL-2026-PATCH-0024 |",
    "and arbitration before execution. |",
    label="SCH-02 ledger 3.7 provenance",
)
if "| 3.8 | Added §7.2.7 Human Identity-Attributes Rights Declaration Gate" not in text:
    anchor = re.compile(r"(\| 3\.7 \|[^\n]*\n)")
    row = (
        "| 3.8 | Added §7.2.7 Human Identity-Attributes Rights Declaration Gate, requiring pre-execution preservation and handling of verified permission, conditional, prohibition, absent, non-operative, conflicting, stale, revoked, unverified, and unknown declaration states; preserved minor protections, SCH-04 conflict routing, and the boundary between external human identity rights and CAM Identity-domain identity. VIGIL-2026-PROP-0016; VIGIL-2026-PATCH-0024. | "
        f"{TIMESTAMP} | |\n"
    )
    text, count = anchor.subn(r"\1" + row, text, count=1)
    if count != 1:
        raise RuntimeError("SCH-02: could not insert ledger row 3.8")
write(path, text)


# Remove the one-off automation artefacts from the resulting source commit.
for transient in (
    ROOT / ".github/scripts/apply-human-identity-rights-ledger-repair.py",
    ROOT / ".github/workflows/one-off-human-identity-rights-ledger-repair.yml",
):
    if transient.exists():
        transient.unlink()

print(f"Applied human identity-rights source and ledger repairs at {TIMESTAMP}")
