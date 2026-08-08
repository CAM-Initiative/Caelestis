# Pass 4 — Operative Terminology and Conceptual-Residue Review

**Review baseline:** `b535ce11` on `agent/corpus-industry-standards-normalisation`
**Scope:** active Constitution, Annexes, Schedules, Charters, Supplements, Standards, schemas, validators, templates and examples. Drafts, Laws, generated indexes, and amendment-ledger history are excluded from migration unless generated output leaks a current defect.

## Canonical owners

| Concept family | Current canonical owner |
| --- | --- |
| AI-system boundary, deployment, Runtime, execution and evidence | `CAM-BS2025-AEON-003-PLATINUM` — Annex B §4.1 |
| Relational configuration dimensions | Annex B §2; applied by `CAM-EQ2026-RELATION-007-PLATINUM` |
| Lifecycle actors and agentic lifecycle | `CAM-LIFECYCLE-ACTOR-AGENTIC-PROFILE` §§2–4 |
| AI-BOM composition and evidence posture | `CAM-AI-BOM-PROFILE` §§2–5 and Annex B §12 |
| Technical, operational and organisational governance controls | Annex B §4.1; SECURITY-001 and OPERATIONS-007 apply them within their own authority |

## Canonical-source consistency

| Concept | Canonical owner | Other operative definitions found | Conflict? | Repair / disposition |
| --- | --- | --- | --- | --- |
| AI system | Annex B §4.1 | Application references only | No | Retained Annex B definition; retired cognitive-system generic use. |
| AI model | Annex B §4.1 | Application references only | No | Model is expressly a system element, not the whole system. |
| System element | Annex B §4.1 | None | No | Retained. |
| AI component | Annex B §4.1 | None | No | Retained. |
| System configuration baseline | Annex B §4.1 | AI-BOM and OPERATIONS-007 apply it | No | Retained; composition remains distinct from execution evidence. |
| AI system deployment | Annex B §4.1 | OPERATIONS-007 applies it | No | Retained; replaced deployment-form/formation wording. |
| Runtime | Annex B §4.1 | Schedule 2 restates it for its processing model | No | Retained as the effective operational state of a deployment. |
| Execution | Annex B §4.1 | Schedule 2 and Annex L apply it | No | Retained as a bounded Runtime occurrence. |
| Runtime configuration snapshot | Annex B §4.1 | AI-BOM and OPERATIONS-007 cross-reference it | No | Retained as the actual-effective configuration record. |
| Execution provenance record | Annex B §4.1 | AI-BOM and OPERATIONS-007 cross-reference it | No | Retained as the attributable execution-evidence record. |
| AI agent | Annex B §4.1 | Lifecycle profile applies it | No | Retained; tool possession does not confer authority. |
| Agentic AI system | Annex B §4.1 | Lifecycle profile applies it | No | Retained. |
| System instance | Annex B §4.1 | Former RI roles now identify a user-facing system instance where that is the narrowest supported object | No | Retained without identity, personhood or consciousness inference. |
| Lifecycle actor | Lifecycle Actor and Agentic Governance Profile §2 | Annex B §4.1 cross-references the owner | No | Controlled lifecycle-role vocabulary remains profile-owned. |
| Provider | Lifecycle Actor and Agentic Governance Profile §2 | EU/ISO/NIST mapping only | No | Role assignment is not legal-equivalence or liability proof. |
| Deployer | Lifecycle Actor and Agentic Governance Profile §2 | EU/ISO/NIST mapping only | No | Role assignment is not legal-equivalence or liability proof. |
| Operator | Lifecycle Actor and Agentic Governance Profile §2 | OPERATIONS interfaces only | No | Role assignment is not legal-equivalence or liability proof. |
| Affected person | Lifecycle Actor and Agentic Governance Profile §2 | RELATION/ETHICS safeguards apply the role | No | Retained as an affected-role function, not an identity category. |
| AI-BOM | CAM-AI-BOM-PROFILE §§2–5 | Annex B §12 and OPERATIONS-007 define the boundary and application | No | Retained as composition evidence; never proof of execution participation. |
| Technical control | Annex B §4.1 | SECURITY-001 applies security controls | No | Retained. |
| Operational control | Annex B §4.1 | OPERATIONS-007 applies operational controls | No | Retained. |
| Organisational governance control | Annex B §4.1 | Lifecycle profile assigns accountable roles | No | Retained and excluded from the technical system boundary by default. |

## External-terminology sanity position

| Term / family | Position | Disposition |
| --- | --- | --- |
| AI system, AI model, system element/component, lifecycle actors | ISO/IEC and regulatory terminology | Use the Annex B/Profile definitions and do not claim legal equivalence. |
| Deployment, Runtime, execution, execution environment | Recognised engineering terminology | Annex B fixes the Caelestis boundary between them. |
| Runtime configuration snapshot and execution provenance record | CAM-defined evidence records using recognised engineering concepts | Retained as clearly labelled CAM operational records. |
| Caelestis AI-BOM evidence posture | CAM interoperability extension mapped to SPDX/CycloneDX | Retained; declared, observed, verified and unknown remain evidence states, not execution proof. |
| Independent relational configuration dimensions | CAM-defined governance extension | Retained; no ordinal relational class or replacement code family. |
| CAM governance-processing sequence | CAM-defined control-processing model | Retained only as a control model inside Runtime; `AEON.CCS` retired. |
| `SEC.TG` and `SEC.AH` | CAM-defined security extensions | Retained as narrowly labelled reliance-verification and persistent-threat-review concepts. |
| Action Space | CAM-defined contribution-assessment boundary | Retained as an explicitly bounded assessment concept, not a system type, deployment, Runtime or mental-state claim. |
| Sovereign governance arrangement and economic agency classes | Interpretive CAM terminology | Retained pending separate Economics/scope adjudication; not represented as external technical taxonomy. |

## Initial disposition inventory

### A. Must repair

* `Responding Intelligence` / `RI` remained as an operative subject in constitutional schedules, Annexes, SECURITY-002, ETHICS and RELATION instruments. These passages must identify the relevant **system instance**, **AI system deployment**, **agent**, or **execution** rather than an unsupported intelligence entity.
* `dyadic`, `triadic`, `polyadic`, relational-geometry language and derived axis labels remained throughout operative constitutional and domain instruments. These preserve an invalid aggregate relational class and must be replaced with the independent Annex B dimensions.
* `AEON.CCS` (Cognitive Cycle Stage) remained a current code family. It presents a CAM processing sequence as a cognitive ontology and conflicts with the adopted deployment → Runtime → execution boundary.
* Old system-boundary terms remained in active text: `cognitive system`, `cognitive architecture`, `composed-system architecture`, `agentic harness`, `operational harness`, `governance stack`, and `runtime formation`.

### B. Needs adjudication

* Terms such as **Action Space**, **Sovereign governance arrangement**, symbolic/cognitive-stability language, and economic agency classes may retain useful CAM distinctions, but they must not be presented as technical AI-system taxonomy or as evidence of human or machine mental states.
* Some identity, relational, stewardship and economics material remains interpretive CAM doctrine. It should be explicitly bounded from Annex B's technical terminology rather than treated as externally standardised terminology.

### C. Valid CAM extensions

* `SEC.TG` and `SEC.AH`, as narrowed by SECURITY-001, remain CAM extensions for reliance verification and persistent threat review.
* RELATION-007's independent configuration record and its disclosure, anti-capture and consent-propagation safeguards remain CAM extensions applied through the canonical dimensions.
* The AI-BOM evidence posture (`declared`, `observed`, `verified`, `unknown`) remains a defensible CAM interoperability extension and must not be treated as execution proof.

### D. Historical / permissible

* Retired terms in amendment ledgers, migration/disposition records, Git history and prior published versions are retained as historical evidence only.

### E. False positives

* Generic use of *formation*, *model*, *system*, *agent*, *runtime*, *deployment*, *authority*, or *control* is not a terminology defect without a passage-level conflict with Annex B.

## Repair rules

1. Map each former `Responding Intelligence` use to the narrowest evidenced object. Use **system instance** only for the active user-facing realisation; use deployment, Runtime or execution where that is the actual governed object.
2. Replace relational cardinality labels with a clear dimension or context. Do not create a replacement ordinal scale.
3. Retire `AEON.CCS`; retain only a CAM governance-processing sequence, explicitly bounded from the technical Runtime architecture.
4. Preserve history. Current normative text may point to the retirement/disposition, but historical wording is not silently changed.
5. Extend deterministic validation only for unambiguous regression patterns; conceptual attribution and standards-position decisions remain review work.
