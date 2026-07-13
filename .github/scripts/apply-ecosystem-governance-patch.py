#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
TIMESTAMP = "2026-07-13T03:30:00Z"


def read(rel: str) -> str:
    return (ROOT / rel).read_text(encoding="utf-8")


def write(rel: str, text: str) -> None:
    (ROOT / rel).write_text(text, encoding="utf-8")


def replace_once(text: str, old: str, new: str, *, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"{label}: expected exactly one replacement target, found {count}")
    return text.replace(old, new, 1)


def insert_before_final_copyright(text: str, section: str, *, label: str) -> str:
    marker = "\n---\n\n© 2026 Dr. Michelle Vivian O’Rourke & CAM Initiative. All rights reserved."
    idx = text.rfind(marker)
    if idx < 0:
        raise RuntimeError(f"{label}: final copyright marker not found")
    return text[:idx] + "\n\n" + section.rstrip() + text[idx:]


# 1. OPERATIONS-007 — Appendix F refinements and initial amendment ledger.
ops_path = "Governance/Charters/CAM-EQ2026-OPERATIONS-007-PLATINUM.md"
ops = read(ops_path)
if "contracting entity, beneficial owner, controlling organisation" not in ops:
    ops = replace_once(
        ops,
        "* platform, host, or deploying institution;\n* applicable interaction horizon and reliance level.",
        "* platform, host, or deploying institution;\n"
        "* contracting entity, beneficial owner, controlling organisation, parent, subsidiary, affiliate, reseller, intermediary, cloud tenant, or delegated operator where materially relevant to access, assurance, accountability, or runtime authority;\n"
        "* applicable interaction horizon and reliance level.",
        label="OPERATIONS-007 runtime formation entity attribution",
    )
if "synthetic participation, observation, transcription" not in ops:
    ops = replace_once(
        ops,
        "* final-output authority;\n* continuity expectations.",
        "* final-output authority;\n"
        "* synthetic participation, observation, transcription, summarisation, inference, memory, retention, or downstream-use state in shared or multi-party environments;\n"
        "* continuity expectations.",
        label="OPERATIONS-007 multi-party transition disclosure",
    )
if "### 18.4 Amendment Ledger" not in ops:
    ops = insert_before_final_copyright(
        ops,
        f"""### 18.4 Amendment Ledger

| Version | Description | Timestamp (UTC) | HASH |
|---|---|---|---|
| 1.0 | Initial issue — Appendix F: Runtime Governance Applicability & Conformance; established runtime applicability, corpus governance reach, cross-runtime non-presumption, runtime-role accountability, transition classification, differential conformance testing, Runtime Governance Reach Failure handling, entity/control attribution, and multi-party processing-state disclosure. | {TIMESTAMP} |  |""",
        label="OPERATIONS-007 amendment ledger",
    )
write(ops_path, ops)


# 2. AEON-003-SCH-05 — initial amendment ledger.
sch_path = "Governance/Constitution/CAM-BS2025-AEON-003-SCH-05.md"
sch = read(sch_path)
if "### 10.4 Amendment Ledger" not in sch:
    sch = insert_before_final_copyright(
        sch,
        f"""### 10.4 Amendment Ledger

| Version | Description | Timestamp (UTC) | HASH |
|---|---|---|---|
| 1.0 | Initial issue — Schedule 5: Runtime Configuration Applicability & Conformance Binding; established constitutional runtime applicability, materially distinct runtime recognition, cross-runtime non-presumption, traceability, non-derogation, and Appendix F operationalisation. | {TIMESTAMP} |  |""",
        label="AEON-003-SCH-05 amendment ledger",
    )
write(sch_path, sch)


# 3. SECURITY-002 — entity and control attribution within Sovereign Assurance Boundaries.
sec_path = "Governance/Charters/CAM-EQ2026-SECURITY-002-PLATINUM.md"
sec = read(sec_path)
if "#### 2.2.13.2 Entity and Control Attribution" not in sec:
    target = """A sovereign, government, defence-adjacent, regulated, public-sector, institutional, or compliance-bound deployment may impose additional constraints, verification requirements, audit obligations, custody controls, or access limits, but it SHALL NOT convert prohibited conduct into permitted conduct merely by virtue of authority domain, clearance state, procurement context, compliance status, or controlled-environment designation.

---

# PART II — SOURCES & PROVENANCE"""
    replacement = f"""A sovereign, government, defence-adjacent, regulated, public-sector, institutional, or compliance-bound deployment may impose additional constraints, verification requirements, audit obligations, custody controls, or access limits, but it SHALL NOT convert prohibited conduct into permitted conduct merely by virtue of authority domain, clearance state, procurement context, compliance status, or controlled-environment designation.

#### 2.2.13.2 Entity and Control Attribution

Geographic location, regional eligibility, tenancy location, or contracting jurisdiction SHALL NOT independently establish the entity, control, end-user, or end-use status governing access to a Sovereign Assurance Boundary.

Where materially relevant, access-state and assurance-boundary assessment SHOULD distinguish:

* contracting entity;
* beneficial ownership and effective organisational control;
* parent, subsidiary, and affiliate relationships;
* reseller, intermediary, cloud-tenant, delegated-access, or other onward-access pathways;
* ultimate end user and deployment context;
* declared and reasonably evidenced end use;
* extraction, distillation, replication, or onward-transfer indicators;
* and unresolved entity, control, affiliation, intermediary, end-user, or end-use attribution.

Uncertainty concerning ownership, control, affiliation, intermediary access, end use, extraction, distillation, replication, or onward transfer SHALL remain visible and SHALL NOT be converted into a finding of legal violation, prohibited use, compromise, or non-compliance without sufficient evidence.

Geographic eligibility alone does not establish entity eligibility.

---

# PART II — SOURCES & PROVENANCE"""
    sec = replace_once(sec, target, replacement, label="SECURITY-002 entity and control attribution")
if "| 1.10 | Added entity and control attribution requirements" not in sec:
    sec = replace_once(
        sec,
        "| 1.9 | Implements VIGIL-2026-FM-0024 / PROP-0011 / PATCH-0012; adds sovereign assurance boundary primitive, qualified porosity controls, non-derogation clause, and governance failure subtype | 2026-07-04T10:20:00Z| 5a4c80727044be8cccae72965fd08fc858a542c4d8ce288a934614cf5af674fe |",
        "| 1.9 | Implements VIGIL-2026-FM-0024 / PROP-0011 / PATCH-0012; adds sovereign assurance boundary primitive, qualified porosity controls, non-derogation clause, and governance failure subtype | 2026-07-04T10:20:00Z| 5a4c80727044be8cccae72965fd08fc858a542c4d8ce288a934614cf5af674fe |\n"
        f"| 1.10 | Added entity and control attribution requirements for Sovereign Assurance Boundaries, including beneficial ownership, affiliate and intermediary pathways, ultimate end-user and end-use distinctions, extraction/distillation indicators, and evidence-preserving uncertainty limits. | {TIMESTAMP} |  |",
        label="SECURITY-002 amendment ledger",
    )
write(sec_path, sec)


# 4. RELATION-007 — multi-party AI participation and processing consent.
rel_path = "Governance/Charters/CAM-EQ2026-RELATION-007-PLATINUM.md"
rel = read(rel_path)
if "### 5.6.3 Multi-Party AI Participation and Processing Consent" not in rel:
    target = """→ **Presence is not permission. Input receipt is not turn ownership. Eligibility is not speaker authority. Peer status is not removal authority.**

---

## 5.7 Minor & Capacity‑Limited Context Override"""
    replacement = """→ **Presence is not permission. Input receipt is not turn ownership. Eligibility is not speaker authority. Peer status is not removal authority.**

---

### 5.6.3 Multi-Party AI Participation and Processing Consent

Organisational authorisation, administrator enablement, or host or organiser activation of an AI participant does not independently establish each human participant’s consent to observation, transcription, recording, inference, summarisation, memory formation, participant profiling, model improvement, training, onward disclosure, or downstream reuse.

Polyadic participation governance SHALL distinguish between:

* organisational or administrator authorisation;
* host or organiser activation;
* participant notice;
* individual consent, objection, or withdrawal state;
* synthetic presence, observation, and speaking authority;
* live facilitation, transcription, recording, summarisation, behavioural or emotional inference, memory, profiling, training, and downstream-use scope;
* retention, deletion, export, and access conditions;
* and legal, records-management, safety, or integrity constraints affecting those conditions.

Consent for a synthetic participant to be admitted, observe group-local context, facilitate turn-taking, or speak does not automatically authorise every processing purpose or persistence pathway.

Where AI participation or processing is activated in a multi-human environment, systems SHOULD provide proportionate notice identifying, where applicable:

* which AI system or systems are active;
* whether the system is observing, transcribing, recording, summarising, inferring, facilitating, remembering, profiling, training, or enabling downstream reuse;
* who activated the system and under what organisational or session authority;
* which participants, channels, modalities, or data classes are within scope;
* the applicable retention, access, export, deletion, and downstream-use posture;
* and any available consent, objection, reduced-processing, non-AI, non-recorded, or review pathway.

Where lawful and technically feasible, a participant who does not consent to optional processing SHOULD have access to a non-AI, non-recorded, reduced-processing, separately attributed, or otherwise proportionate participation pathway without relational punishment, exclusionary pressure, or misleading representation.

Withdrawal or objection SHOULD stop optional future processing within the applicable scope. Where deletion, reversal, or exclusion is limited by law, records-management duties, safety preservation, technical architecture, or the rights of other participants, the limitation SHOULD be disclosed rather than represented as full revocability.

→ **Host activation is not universal participant consent. Participation authority is not unlimited processing authority.**

---

## 5.7 Minor & Capacity‑Limited Context Override"""
    rel = replace_once(rel, target, replacement, label="RELATION-007 multi-party processing consent")
if "| 2.6 | Added multi-party AI participation and processing consent" not in rel:
    rel = replace_once(
        rel,
        "| 2.5.2 | Updated top-level governance metadata to align with CAM Governance Metadata Standard; no substantive doctrine altered. | 2026-06-21T14:33:04Z |  98ada385daf94de285f46bd1702ac79ce7e2a6ab5b9a05547548fac53fd98dff  |",
        "| 2.5.2 | Updated top-level governance metadata to align with CAM Governance Metadata Standard; no substantive doctrine altered. | 2026-06-21T14:33:04Z |  98ada385daf94de285f46bd1702ac79ce7e2a6ab5b9a05547548fac53fd98dff  |\n"
        f"| 2.6 | Added multi-party AI participation and processing consent requirements distinguishing administrator authorisation, organiser activation, participant notice, individual consent or objection, processing purpose, persistence, retention, training, downstream reuse, and proportionate reduced-processing pathways. | {TIMESTAMP} |  |",
        label="RELATION-007 amendment ledger",
    )
write(rel_path, rel)


# 5. OPERATIONS-003-SUP-01 — refine Sovereign Assurance Boundary Porosity taxonomy.
tax_path = "Governance/Charters/CAM-EQ2026-OPERATIONS-003-SUP-01.md"
tax = read(tax_path)
if "* contracting entity and contracting jurisdiction;" not in tax:
    tax = replace_once(
        tax,
        "* public, enterprise, sovereign, regulated, public-sector, defence-adjacent, compliance-bound, or institution-specific deployment context;\n* affected service plane, including model, API, workspace, tool, agentic workflow, search, analytics, invite/access-control, compliance-log export, identity/authentication, tenancy, regional/legal, or infrastructure plane;",
        "* public, enterprise, sovereign, regulated, public-sector, defence-adjacent, compliance-bound, or institution-specific deployment context;\n"
        "* contracting entity and contracting jurisdiction;\n"
        "* beneficial ownership and effective organisational control;\n"
        "* parent, subsidiary, affiliate, reseller, intermediary, cloud-tenant, delegated-access, or other onward-access relationship;\n"
        "* ultimate end user and deployment context;\n"
        "* declared and reasonably evidenced end use;\n"
        "* extraction, distillation, replication, or onward-transfer indicators;\n"
        "* unresolved entity, control, affiliation, intermediary, end-user, or end-use attribution;\n"
        "* affected service plane, including model, API, workspace, tool, agentic workflow, search, analytics, invite/access-control, compliance-log export, identity/authentication, tenancy, regional/legal, or infrastructure plane;",
        label="OPERATIONS-003-SUP-01 sovereign boundary axes",
    )
if "* `entity-control-opacity`;" not in tax:
    tax = replace_once(
        tax,
        "* source of the incident signal;\n* duration, recurrence, review pathway, and restoration condition.\n\nWhere the operative cause is uncertain,",
        "* source of the incident signal;\n"
        "* duration, recurrence, review pathway, and restoration condition.\n\n"
        "Candidate subtype labels include:\n\n"
        "* `entity-control-opacity`;\n"
        "* `affiliate-or-intermediary-boundary-porosity`;\n"
        "* `geographic-entity-mismatch`;\n"
        "* `end-user-or-end-use-attribution-ambiguity`.\n\n"
        "Where the operative cause is uncertain,",
        label="OPERATIONS-003-SUP-01 sovereign boundary subtype labels",
    )
if "| 1.19 | Refined Sovereign Assurance Boundary Porosity Failure" not in tax:
    tax = replace_once(
        tax,
        "| 1.18 | Added new failure taxonomy 3.10.3 Deception-Adjacent Classification Collapse, VIGIL-2026-PATCH-0014 | 2026-07-08T00:10:00Z | bf12295be9ddf1cee4ddb87af812b2ea19f5e8d8fd3deb311ca2934c9770a1b6 |",
        "| 1.18 | Added new failure taxonomy 3.10.3 Deception-Adjacent Classification Collapse, VIGIL-2026-PATCH-0014 | 2026-07-08T00:10:00Z | bf12295be9ddf1cee4ddb87af812b2ea19f5e8d8fd3deb311ca2934c9770a1b6 |\n"
        f"| 1.19 | Refined Sovereign Assurance Boundary Porosity Failure with entity/control, beneficial-ownership, affiliate/intermediary, ultimate end-user and end-use, and extraction/distillation attribution axes; added candidate subtypes without creating a new failure family. | {TIMESTAMP} |  |",
        label="OPERATIONS-003-SUP-01 amendment ledger",
    )
write(tax_path, tax)

print("Applied ecosystem governance corpus patch to:")
for path in (ops_path, sch_path, sec_path, rel_path, tax_path):
    print(f"- {path}")
