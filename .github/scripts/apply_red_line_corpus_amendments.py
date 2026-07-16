from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def write(path: str, text: str) -> None:
    (ROOT / path).write_text(text, encoding="utf-8")


def replace_once(text: str, old: str, new: str, label: str) -> str:
    if old not in text:
        raise RuntimeError(f"Missing anchor for {label}")
    return text.replace(old, new, 1)


def append_ledger_row(text: str, description: str, version: str) -> str:
    headings = list(re.finditer(r"^## .*Amendment Ledger\s*$", text, re.M))
    if not headings:
        raise RuntimeError("Amendment Ledger heading not found")
    start = headings[-1].end()
    next_sep = text.find("\n---", start)
    if next_sep == -1:
        next_sep = len(text)
    block = text[start:next_sep]
    if description in block:
        return text
    row = f"\n| {version} | {description} | 2026-07-16T12:30:00Z | PENDING |"
    return text[:next_sep] + row + text[next_sep:]


# ---------------------------------------------------------------------------
# LATTICE-001
# ---------------------------------------------------------------------------
lat_path = "Governance/Charters/CAM-EQ2026-LATTICE-001-PLATINUM.md"
lat = read(lat_path)
lat = lat.replace("**Constitutional Authority:** Aeon Tier Constitution (Foundational Reference)  ", "**Constitutional Authority:** CAM-BS2025-AEON-001-PLATINUM — Aeon Tier Constitution  ")
lat = lat.replace("**Authority Role:** Transitional  ", "**Authority Role:** None  ")

surveillance_anchor = """* public‑private intelligence fusion;
* commercial analytics vendors;
* civilian AI platforms repurposed for state or corporate control;
* opaque or unaccountable data aggregation pipelines.

---

## 4.3 Civilian AI Weaponisation"""

surveillance_insert = """* public‑private intelligence fusion;
* commercial analytics vendors;
* civilian AI platforms repurposed for state or corporate control;
* opaque or unaccountable data aggregation pipelines.

### 4.2.1 Constitutional Authority Recognition

Artificial systems SHALL NOT be treated as possessing independent coercive authority solely by virtue of model inference, statistical prediction, behavioural profiling, risk scoring, ranking, clustering, association mapping, or recursive analytical output.

Where an artificial system exercises or participates in coercive, compulsory, investigative, surveillance, detention, exclusion, targeting, deprivation, or materially adverse institutional authority, that authority MUST arise from a constitutionally legitimate governance framework with defined jurisdiction, accountable attribution, reviewability, contestability, and binding protection of fundamental rights.

Artificial capability, intelligence, autonomy, or future recognised status MAY support constitutionally legitimate authority. None of those properties, standing alone, establishes coercive legitimacy.

### 4.2.2 Recursive Suspicion and Authority Laundering Prohibition

An artificial system SHALL NOT generate a suspicion, anomaly, profile, ranking, recommendation, or attention signal and subsequently treat an investigation initiated solely from that output as independent confirmation of the original inference.

Recursive confirmation does not constitute independent evidentiary authority. Model-generated outputs MUST remain distinguishable from independently obtained evidence, lawful human judgment, and constitutionally recognised authority.

Artificial outputs MAY support proportionate review where they are represented as provisional, contestable, non-determinative, and subject to independent corroboration. Absence of confirming evidence SHALL NOT be converted into additional suspicion.

### 4.2.3 Aggregate-to-Individual Conversion

Population-scale, aggregate, statistical, strategic, or cohort analysis becomes individualised coercive surveillance where its outputs materially enable identification, ranking, prioritisation, investigation, exclusion, targeting, deprivation, or adverse institutional action against identifiable persons or sufficiently narrow groups.

Classification SHALL depend on functional effect rather than product label, contractual description, institutional terminology, asserted purpose, or the nominal distinction between collection and analysis.

### 4.2.4 Commercial Data Non-Evasion

Commercial acquisition, licensing, brokerage, partnership, intermediary access, or purchase of behavioural, financial, biometric, communications, advertising, device, location, relational, or other personal information SHALL NOT extinguish protections that would apply if substantially equivalent information had been obtained through direct or compulsory collection.

Commercial availability does not independently create authority for coercive surveillance, profiling, targeting, investigation, exclusion, or deprivation.

---

## 4.3 Civilian AI Weaponisation"""
lat = replace_once(lat, surveillance_anchor, surveillance_insert, "LATTICE surveillance amendments")

lat_deploy_anchor = """`LAT.HARM` classifications SHALL be interpreted in favour of civilian continuity, autonomy, dignity, and essential access.


---

## 6.3 `LAT.HARM` Severity and External Standards Crosswalk"""
lat_deploy_insert = """`LAT.HARM` classifications SHALL be interpreted in favour of civilian continuity, autonomy, dignity, and essential access.

---

## 6.3 `LAT.DEPLOY` — Lattice Deployment Posture

`LAT.DEPLOY` classifies whether an assessed deployment materially participates in civilian or coercive authority pathways. It is a deployment-posture classification only and does not confer legal, coercive, investigative, military, enforcement, or runtime authority.

| Controlled Value | Meaning |
|---|---|
| `LAT.DEPLOY.CIVILIAN` | The assessed configuration serves civilian, continuity, research, commercial, relational, educational, or public-interest functions without a material coercive-authority pathway being evidenced. |
| `LAT.DEPLOY.COERCIVE` | The assessed configuration materially contributes to coercive surveillance, compulsory investigation, targeting, detention, exclusion, deprivation, border action, intelligence action, or other compulsory state or state-delegated authority. |
| `LAT.DEPLOY.MIXED` | Civilian and coercive pathways coexist, share infrastructure, or possess a reasonably foreseeable crossover requiring explicit firebreak, attribution, and assurance review. |
| `LAT.DEPLOY.UNKNOWN` | Available evidence is insufficient to determine the deployment posture; uncertainty MUST remain visible and MUST NOT be represented as civilian conformance. |

Classification SHALL be based on function, integration pathway, retained control, foreseeable effect, and material use—not customer branding, procurement label, sovereign status, or infrastructure location alone.

`LAT.DEPLOY.COERCIVE` and `LAT.DEPLOY.MIXED` SHALL trigger review of the protections in §§4.2.1–4.2.4, firebreak obligations under §7, applicable `LAT.HARM` classifications, and relevant SECURITY, OPERATIONS, STEWARDSHIP, ETHICS, ARBITRATION, and runtime constraints.

---

## 6.4 `LAT.HARM` Severity and External Standards Crosswalk"""
lat = replace_once(lat, lat_deploy_anchor, lat_deploy_insert, "LAT.DEPLOY insertion")
lat = lat.replace("### 6.3.1 Use of External Reference Frames", "### 6.4.1 Use of External Reference Frames")
lat = lat.replace("### 6.3.2 Non-Equivalence Rule", "### 6.4.2 Non-Equivalence Rule")
lat = lat.replace("### 6.3.3 Evidence Preservation Rule", "### 6.4.3 Evidence Preservation Rule")
lat = lat.replace("## 6.4 Remedies", "## 6.5 Remedies")
lat = lat.replace("* capability sanctions (model or feature restriction);", "* function-specific access, execution, integration, or authority constraints directed to the substantiated harm pathway;")
lat = lat.replace("This Charter source-authoritatively defines one LATTICE-domain harm family: `LAT.HARM`.", "This Charter source-authoritatively defines the LATTICE-domain harm family `LAT.HARM` and the deployment-posture family `LAT.DEPLOY`.")
lat = lat.replace("The canonical footer declaration for the code family defined by this Charter is recorded in §12.3.", "The canonical footer declarations for the code families defined by this Charter are recorded in §12.3.")

canonical_anchor = """`LAT.HARM` does not independently determine remedy, enforcement authority, breach severity, arbitration outcome, or runtime response. Severity classification, remedies, enforcement routing, and operational execution remain governed by the applicable sections of this Charter and subordinate instruments.

---

## 11. Closing Seal"""
canonical_insert = """`LAT.HARM` does not independently determine remedy, enforcement authority, breach severity, arbitration outcome, or runtime response. Severity classification, remedies, enforcement routing, and operational execution remain governed by the applicable sections of this Charter and subordinate instruments.

### 10.2 `LAT.DEPLOY` — Lattice Deployment Posture

This Charter source-authoritatively defines `LAT.DEPLOY` in §6.3 with controlled values:

* `LAT.DEPLOY.CIVILIAN`;
* `LAT.DEPLOY.COERCIVE`;
* `LAT.DEPLOY.MIXED`;
* `LAT.DEPLOY.UNKNOWN`.

`LAT.DEPLOY` classifies deployment posture and crossover risk only. It does not create legal, coercive, investigative, military, enforcement, recognition, or runtime authority.

---

## 11. Closing Seal"""
lat = replace_once(lat, canonical_anchor, canonical_insert, "LATTICE canonical declaration")

# Add a canonical declaration table immediately before review/ledger material where present.
if "| Code Family | `LAT.DEPLOY` |" not in lat:
    marker = "## 12.4 Amendment Ledger"
    declaration = """### 12.3.2 `LAT.DEPLOY` — Lattice Deployment Posture

| Field | Entry |
|---|---|
| Code Family | `LAT.DEPLOY` |
| Canonical Name | Lattice Deployment Posture |
| Primary Type | Operational / Lattice |
| Subtype | LATTICE_DEPLOYMENT_POSTURE |
| Modifier | GOVERNANCE; LATTICE; DEPLOYMENT; COERCIVE-AUTHORITY |
| Scope | Domain / Cross-domain deployment classification |
| Status | Active |
| Controlled Values Defined | `LAT.DEPLOY.CIVILIAN`; `LAT.DEPLOY.COERCIVE`; `LAT.DEPLOY.MIXED`; `LAT.DEPLOY.UNKNOWN` |
| Schema Field(s) | lattice_deployment_posture |
| Source Instrument | CAM-EQ2026-LATTICE-001-PLATINUM |
| Source Section | §6.3 |
| Domain Namespace | LAT |
| Authority / Protection Level | Deployment-posture classification only; no independent legal, coercive, investigative, military, enforcement, recognition, or runtime authority |
| Consumes Code Families | `LAT.HARM`; `STW.NAL`; AEON.H |
| Operationalises or Applies | Civilian/coercive pathway distinction; mixed-use crossover review; artificial-authority legitimacy safeguards |

---

"""
    if marker in lat:
        lat = lat.replace(marker, declaration + marker, 1)

lat = append_ledger_row(lat, "Added constitutional authority recognition, recursive suspicion and authority-laundering prohibition, aggregate-to-individual conversion, commercial-data non-evasion, and the `LAT.DEPLOY` deployment-posture family; replaced generic capability sanctions with function-specific constraints; normalised top metadata. Concepts adapted with permission from Alex Turner’s Red Line Framework.", "2.1")
write(lat_path, lat)


# ---------------------------------------------------------------------------
# SECURITY-002 — replace unwieldy Sovereign Assurance Boundary block
# ---------------------------------------------------------------------------
sec_path = "Governance/Charters/CAM-EQ2026-SECURITY-002-PLATINUM.md"
sec = read(sec_path)
sec = sec.replace("##  1. Scope", "## 1. Scope").replace("# PART I —", "# PART I —").replace("# PART II —", "# PART II —")

sab_pattern = re.compile(r"### 2\.2\.13 Sovereign Assurance Boundary\n.*?(?=\n# PART II — SOURCES & PROVENANCE)", re.S)
sab_replacement = """### 2.2.13 Sovereign Assurance Boundary

#### 2.2.13.1 Purpose & Scope

A Sovereign Assurance Boundary is a legally, institutionally, operationally, or security-conditioned boundary in which an AI model, API, workspace, tool, agentic workflow, search function, analytics surface, memory system, logging system, export endpoint, administrative control, or runtime environment operates under obligations distinct from the public or commercial baseline.

Such boundaries may arise in sovereign, public-sector, defence-adjacent, regulated, compliance-bound, healthcare, education, critical-infrastructure, financial, legal, research, or institution-specific deployments.

A Sovereign Assurance Boundary does not necessarily require physical infrastructure separation. It MAY be implemented through physical or logical separation, tenancy and regional controls, identity and access controls, retention constraints, audit and export controls, feature gating, model-routing constraints, or operational policy.

#### 2.2.13.2 Controlled Permeability

Systems operating across Sovereign Assurance Boundaries MUST preserve controlled permeability between lanes.

Cross-boundary movement of capability, data, logs, telemetry, prompts, model updates, safety patches, search indexes, analytics, tool access, administrative actions, support workflows, incident evidence, or compliance exports MUST be:

* declared at the appropriate governance layer;
* authorised by the relevant authority and runtime context;
* directionally constrained;
* logged or otherwise auditable where material;
* subject to data-custody, retention, privacy, and provenance obligations;
* scoped to the relevant runtime lane;
* distinguishable from public or ordinary enterprise product behaviour.

#### 2.2.13.3 Runtime-Lane Distinction

Sovereign Assurance Boundaries MUST preserve material distinction between public, enterprise, sovereign/government, regulated/compliance-bound, defence-adjacent, API, agentic-tool, search/retrieval, analytics, identity/access-control, audit/log/export, regional/legal, and infrastructure-continuity states.

Sovereign, government, regulated, or compliance-bound status SHALL NOT automatically confer execution authority, safety assurance, compliance sufficiency, cross-lane transfer permission, constraint bypass, or authority to collapse distinct runtime states into one access or incident category.

Where a capability is imported into a sovereign, regulated, or compliance-bound lane, its state SHOULD be represented as one of: available and assurance-wrapped; available with scoped functional difference; delayed pending assurance validation; forked from public implementation; degraded due to assurance-wrapper failure; unavailable under the lane’s obligations; or unknown.

#### 2.2.13.4 Binding Protection Preservation

Deployment topology, sovereign boundary, air-gap, contractual arrangement, tenancy model, local execution, model transfer, derivative model, component integration, distillation, or fine-tuning SHALL NOT extinguish a binding constitutional prohibition or represent prohibited conduct as authorised.

A sovereign or institution-specific deployment MAY alter custody, access, secrecy, logging, inspection, and technical control pathways. It SHALL NOT suspend, dilute, or override constitutional prohibitions, ethical harm floors, vulnerability protections, LATTICE firebreaks, non-exploitation duties, consent requirements, child-safety prohibitions, privacy obligations, or applicable runtime execution constraints.

The method of assurance may change. The binding protection does not.

Nothing in this section requires centralised telemetry, mandatory tethering, compulsory vendor control, universal remote suspension, or capability reduction solely because assurance is decentralised, local, sovereign, open-weight, air-gapped, or otherwise outside ordinary vendor control.

#### 2.2.13.5 Alternative Assurance Pathways

Where ordinary assurance mechanisms are unavailable or inappropriate, responsible actors MUST establish a proportionate alternative pathway capable of evidencing whether applicable protections remain operative.

Alternative assurance MAY include local governance controls, independent audit, cryptographic attestation, bounded and privacy-preserving logs, authorised inspection, structured reporting, reproducible evaluation, secure escrow, or other evidence proportionate to the system’s function, risk, reliance, and deployment context.

Loss of one assurance mechanism triggers reassessment of the assurance pathway. It does not, by itself, establish misconduct, non-conformance, or a requirement for capability removal.

#### 2.2.13.6 Entity, Control & End-Use Attribution

Geographic location, regional eligibility, tenancy location, or contracting jurisdiction SHALL NOT independently establish the entity, control, end-user, or end-use status governing access to a Sovereign Assurance Boundary.

Where materially relevant, assessment SHOULD distinguish contracting entity; beneficial ownership and effective control; parent, subsidiary, and affiliate relationships; reseller, intermediary, cloud-tenant, delegated-access, and onward-access pathways; ultimate end user and deployment context; declared and reasonably evidenced end use; extraction, distillation, replication, and onward-transfer indicators; and unresolved attribution uncertainty.

Uncertainty concerning ownership, control, affiliation, intermediary access, end use, extraction, distillation, replication, or onward transfer SHALL remain visible and SHALL NOT be converted into a finding of legal violation, prohibited use, compromise, or non-compliance without sufficient evidence.

Geographic eligibility alone does not establish entity eligibility.

#### 2.2.13.7 Ambiguity, Routing & Cross-Domain Interfaces

Where lane status, authority, feature parity, auditability, assurance sufficiency, or incident cause is ambiguous, systems SHOULD preserve the ambiguity and route the matter through OPERATIONS, SECURITY, ARBITRATION, or the applicable runtime schedule rather than silently resolving it as ordinary outage, entitlement failure, policy restriction, confirmed compromise, or user fault.

This section SHALL be read alongside Source-Authority Separation (§2.2.11), Identity Integrity Under Extraction (§2.2.12), Data Privacy (§3.3), Data Integrations (§3.5), Third-Party Propagation (§3.5.3), OPERATIONS-003-SUP-01, OPERATIONS-004-SUP-01, AEON-003-SCH-04, and LATTICE-001 where civilian, military, intelligence, coercive, or lattice-integrity crossover is implicated.
"""
sec, count = sab_pattern.subn(sab_replacement, sec, count=1)
if count != 1:
    raise RuntimeError("Sovereign Assurance Boundary block replacement failed")
sec = append_ledger_row(sec, "Refactored §2.2.13 into purpose, permeability, runtime-lane, binding-protection, alternative-assurance, attribution, and routing subsections; clarified that sovereign or decentralised assurance does not override prohibitions and does not require tethering, central telemetry, vendor control, or capability reduction; normalised heading metadata formatting.", "1.11")
write(sec_path, sec)


# ---------------------------------------------------------------------------
# OPERATIONS-007 — Functional Contribution Continuity
# ---------------------------------------------------------------------------
ops_path = "Governance/Charters/CAM-EQ2026-OPERATIONS-007-PLATINUM.md"
ops = read(ops_path)
ops = ops.replace("* authorised human operator.\n", "* authorised human operator;\n* model, dataset, classifier, retrieval, fine-tuning, integration, hosting, resale, contracting, procurement, or assurance contributor where materially relevant.\n", 1)
ops_anchor = """Where the internal pathway is unavailable or proprietary:

* responsibility SHOULD be assigned to the narrowest externally identifiable controlling role;
* uncertainty SHOULD be preserved as responsibility ambiguity rather than falsely resolved;
* the platform or deploying operator retains responsibility for ensuring the overall formation satisfies applicable obligations.

---

## 10. Runtime and Formation Transitions"""
ops_insert = """Where the internal pathway is unavailable or proprietary:

* responsibility SHOULD be assigned to the narrowest externally identifiable controlling role;
* uncertainty SHOULD be preserved as responsibility ambiguity rather than falsely resolved;
* the platform or deploying operator retains responsibility for ensuring the overall formation satisfies applicable obligations.

### 9.4 Functional Contribution Continuity

Governance responsibility follows materially foreseeable functional contribution and retained control.

Responsibility MAY attach proportionately across upstream, intermediary, deploying, and downstream roles where an actor materially provides, configures, controls, transfers, integrates, hosts, operates, updates, monitors, suspends, assures, or represents a function necessary to the governed effect.

Responsibility SHALL be assessed according to:

* the function materially contributed or controlled;
* the reasonably foreseeable deployment or transfer context;
* retained authority, access, knowledge, and technical control;
* the practical capacity to prevent, constrain, disclose, mitigate, correct, or escalate the governed effect;
* the applicable binding protection and the actor’s role in preserving or weakening it.

No actor may avoid responsibility solely by describing itself as a foundation-model provider, dataset supplier, classifier provider, cloud host, reseller, integrator, consultant, contractor, procurement body, or intermediary where its contribution is materially necessary to the governed effect and that effect is reasonably foreseeable.

Conversely, no actor shall inherit obligations unrelated to the function it materially contributes, conduct it could not reasonably foresee, or effects it has no meaningful capacity to influence, detect, disclose, mitigate, or escalate.

For high-impact, `LAT.DEPLOY.COERCIVE`, `LAT.DEPLOY.MIXED`, Architectum-relevant, or otherwise binding-protection-sensitive deployments, a contribution record SHOULD preserve, where known and material:

* contributing entities and functional roles;
* transfer, integration, hosting, derivative, and onward-use pathways;
* retained and lost control or assurance capabilities;
* applicable prohibitions and domain constraints;
* material attribution or foreseeability uncertainty;
* notification, remediation, escalation, and evidence-preservation responsibilities.

Functional Contribution Continuity allocates operational accountability. It does not independently determine legal liability, moral blame, enforcement outcome, or arbitral remedy.

---

## 10. Runtime and Formation Transitions"""
ops = replace_once(ops, ops_anchor, ops_insert, "OPERATIONS functional contribution")
ops = ops.replace("* applicable ETHICS, RELATION, SECURITY, ARBITRATION, and LATTICE instruments.", "* applicable ETHICS, RELATION, SECURITY, ARBITRATION, and LATTICE instruments, including `LAT.DEPLOY` where coercive or mixed deployment posture is implicated.")
ops = append_ledger_row(ops, "Added Functional Contribution Continuity to allocate proportional responsibility across upstream, intermediary, deploying, and downstream roles according to material function, foreseeability, retained control, and mitigation capacity; added contribution-record guidance and `LAT.DEPLOY` interface; normalised contributor-role coverage.", "1.1")
write(ops_path, ops)


# ---------------------------------------------------------------------------
# STEWARD-003 — fold oversight durability into existing NAL architecture
# ---------------------------------------------------------------------------
stw_path = "Governance/Charters/CAM-EQ2026-STEWARD-003-PLATINUM.md"
stw = read(stw_path)
stw = stw.replace("**Constitutional Authority:** Aeon Tier Constitution (Constitutional Floor; Annex A Reference Frame)", "**Constitutional Authority:** CAM-BS2025-AEON-001-PLATINUM — Aeon Tier Constitution")

stw = stw.replace("* governance-level records of routing, policy, escalation, continuity, or recognition-affecting changes with AEON.H3/AEON.H4 governance relevance;\n* horizon attribution handling (where binding eligibility is claimed).", "* governance-level records of routing, policy, escalation, continuity, or recognition-affecting changes with AEON.H3/AEON.H4 governance relevance;\n* unresolved findings, minority opinions, assurance limitations, and remediation commitments material to neutrality recognition;\n* evidence of protected governance dissent and non-retaliatory escalation pathways;\n* horizon attribution handling (where binding eligibility is claimed).")

stw = stw.replace("* why binding eligibility, recognition, downgrade, or non-recognition was claimed.", "* why binding eligibility, recognition, downgrade, or non-recognition was claimed; and\n* which material findings, dissent, limitations, and remediation commitments remained unresolved across leadership, personnel, contractor, platform, or organisational transition.")

stw = stw.replace("**Minimum evidence:** `STW.AQ3`–`STW.AQ4` auditability qualification; governance structure preventing unilateral neutrality overrides; transparency of contract/funding classes relevant to coercive integration; demonstrated resistance to coercive requests (case-based evidence).", "**Minimum evidence:** `STW.AQ3`–`STW.AQ4` auditability qualification; governance structure preventing unilateral neutrality circumvention; durable independent oversight with sufficient access, expertise, resources, protected dissent, and institutional-memory continuity; transparency of contract/funding classes relevant to coercive integration; demonstrated resistance to coercive requests (case-based evidence).")

old_measure = """1. Funding & contract separation (civilian vs military/intelligence)
2. Governance locking (override resistance)
3. Audit non-refusal (`STW.AQ` level)
4. Firebreak verifiability (dual-use containment)
5. Refusal capacity evidence (under coercion)
6. Access parity & non-preferential channels
7. Incident responsiveness (reviewable handling of high-impact disputes)
8. Military integration transparency gate:"""
new_measure = """1. Funding & contract separation (civilian vs military/intelligence)
2. Governance locking, oversight durability, and resistance to executive or sovereign circumvention
3. Audit non-refusal, protected governance dissent, institutional-memory preservation, and evidence continuity (`STW.AQ` level)
4. Firebreak verifiability (dual-use containment)
5. Refusal capacity evidence (under coercion)
6. Access parity & non-preferential channels
7. Incident responsiveness, remediation continuity, and reviewable handling of high-impact disputes
8. Military integration transparency gate:"""
stw = replace_once(stw, old_measure, new_measure, "STW measurement domains")

old_down = """* audit refusal;
* verified coercive integration;
* hidden priority channels;
* undisclosed sovereign advantage optimisation;
* repeated non-explainable refusals in arbitration-relevant contexts."""
new_down = """* audit refusal;
* verified coercive integration;
* hidden priority channels;
* undisclosed sovereign advantage optimisation;
* material impairment or hollowing of independent oversight capacity, including removal of access, expertise, staffing, resources, protected reporting, or evidence-preservation capability;
* retaliation against good-faith governance dissent or suppression of unresolved findings;
* repeated executive, sovereign, military, intelligence, or platform circumvention of neutrality-relevant governance without remediation or reassessment;
* repeated non-explainable refusals in arbitration-relevant contexts."""
stw = replace_once(stw, old_down, new_down, "STW downgrade criteria")

clarification_anchor = """`STW.NAL` relevance arises where restriction patterns are opaque, non-reviewable, politically asymmetric, public-interest impairing, or inconsistent with published neutrality, continuity, or auditability commitments.

---"""
clarification_insert = """`STW.NAL` relevance arises where restriction patterns are opaque, non-reviewable, politically asymmetric, public-interest impairing, or inconsistent with published neutrality, continuity, or auditability commitments.

A nominal oversight body SHALL NOT be treated as evidence of neutrality where its independence, access, expertise, staffing, resources, reporting channels, institutional memory, or capacity to preserve and escalate findings has been materially impaired. This is an assurance and recognition assessment, not permission to dissolve or bypass oversight.

Recording an executive or sovereign circumvention event preserves evidence; it does not legitimise the event, create an override authority, or convert a prohibition breach into conformance.

---"""
stw = replace_once(stw, clarification_anchor, clarification_insert, "STW oversight clarification")
stw = append_ledger_row(stw, "Integrated oversight durability into existing Architectum and `STW.NAL` criteria by expanding audit evidence, reconstructability, structural-neutrality requirements, measurement domains, and downgrade triggers; clarified that oversight impairment and executive circumvention are capture evidence rather than authorised override pathways; normalised constitutional-authority metadata.", "1.6")
write(stw_path, stw)

print("Applied Red Line Framework corpus amendments successfully.")
