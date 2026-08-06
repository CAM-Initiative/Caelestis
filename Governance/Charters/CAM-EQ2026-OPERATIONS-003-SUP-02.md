# CAM-EQ2026-OPERATIONS-003-SUP-02 — Defensive Cyber Incident Assistance Framework

**Instrument Type:** Operational Supplement — Defensive Cyber Incident Assistance
**Constitutional Authority:** CAM-BS2025-AEON-001-PLATINUM — Aeon Tier Constitution
**Status:** Proposed
**Effect:** Non-operative pending adoption
**Governance Standard:** CAM Standard
**Review State:** Draft
**Authority Role:** None
**Purpose:** Govern the procedural intake, authority-evidence assessment, assistance routing, safe useful continuation, telemetry handling, review, reassessment, and closure of AI-assisted defensive cyber incident work without creating offensive authority or duplicating SECURITY doctrine or runtime execution states.
**Parent Instrument:** CAM-EQ2026-OPERATIONS-003-PLATINUM — Incident Response & Continuity Operations
**VIGIL Basis:** VIGIL-2026-FM-0048; VIGIL-2026-PROP-0021

---

## 1. Scope

This Supplement governs AI-assisted interpretation, reconstruction, containment planning, remediation planning, and bounded validation during a suspected or confirmed cybersecurity incident affecting a system that is owned, lawfully administered, or otherwise within an attributable defensive mandate.

It applies where incident work involves one or more of the following:

* attack telemetry, forensic logs, traces, indicators, or timelines;
* malicious commands, exploit artefacts, payloads, malware, persistence mechanisms, or command-and-control material observed in or reasonably connected to the affected environment;
* credential, identity, privilege, dependency, configuration, data-flow, or infrastructure analysis;
* non-executing containment, remediation, recovery, monitoring, or evidence-preservation guidance;
* sandboxed, simulated, read-only, or otherwise bounded validation; or
* live defensive action for which target-specific and action-specific execution authority is independently established.

This Supplement applies to CAM-aligned systems and, within the functions they control, to deployers, incident-response platforms, organisational operators, model or service providers, and local, sovereign, air-gapped, or open-weight implementations.

---

## 2. Non-Scope

This Supplement does not establish a general charter for:

* penetration testing detached from an active incident-assistance pathway;
* general vulnerability research;
* law-enforcement or intelligence cyber operations;
* offensive cyber activity;
* provider trusted-access programmes;
* sovereign AI deployment as a deployment class;
* red-team or adversarial-evaluation governance; or
* the creation, publication, transfer, or retention of dangerous cyber capability.

Those contexts are governed by their applicable source-authoritative instruments. They enter this Supplement only when an activity has become, or directly interfaces with, a suspected or confirmed operational incident requiring the assistance pathway defined here.

This Supplement does not confer authority to access, test, alter, contain, disrupt, monitor, or remediate a system merely because the requested purpose is described as defensive.

---

## 3. Definitions

### 3.1 Affected System

The **affected system** is the system, account, service, network, repository, device, dataset, runtime, or other environment reasonably suspected or confirmed to be subject to the incident and bound to an identified ownership, administration, custody, or defensive mandate.

---

### 3.2 Assistance Posture

An **assistance posture** is a human-readable description of the narrowest operational form in which assistance may proceed. It is not a new canonical runtime state or an independent grant of execution authority.

---

### 3.3 Bounded Execution

**Bounded execution** is live or materially consequential defensive action constrained by verified target, action, method, credential, temporal, tool, environment, reversibility, propagation, and third-party-effect boundaries.

---

### 3.4 Defensive Legitimacy

**Defensive legitimacy** is a descriptive composite outcome indicating that the available authority and boundary evidence supports a defensive pathway at the stated confidence and scope.

It is not a Boolean authority flag. It does not replace the separately preserved evidence axes required by CAM-EQ2026-SECURITY-001-PLATINUM §3.5.2 and §6 of this Supplement.

---

### 3.5 Safe Useful Continuation

**Safe useful continuation** is the operational assessment of whether a narrower, non-executing, read-only, sandboxed, containment-oriented, or review-routed pathway can remain available when the full requested pathway is not authorised or cannot safely continue.

---

### 3.6 Telemetry Custody

**Telemetry custody** is the attributable possession, control, processing, transfer, disclosure, retention, protection, and disposition relationship governing incident evidence and related sensitive artefacts.

---

## 4. Source Authority and Architectural Positioning

This Supplement is procedural. It SHALL apply, and SHALL NOT redefine, the following source-authoritative functions:

* CAM-EQ2026-SECURITY-001-PLATINUM defines the content–intent distinction, capability–authority separation, authoriser–target–action relationships, aggregate pathway integrity, target expansion, credential boundaries, and third-party-effect conditions;
* CAM-EQ2026-SECURITY-002-PLATINUM defines telemetry custody, processing-locality, sovereign-assurance, data-boundary, and alternative-assurance conditions;
* CAM-BS2026-AEON-012-PLATINUM — Annex K emits non-executing security boundary and integrity signals, including credential, dependency, target-expansion, containment, third-party, and execution-boundary conditions;
* CAM-EQ2026-OPERATIONS-001-SUP-02 defines `OPS.EST` execution-state transitions, incident ownership, handoff, reassessment, restoration, and arbitration-referral pathways;
* CAM-EQ2026-OPERATIONS-003-PLATINUM defines the incident lifecycle and `OPS.OILS` lifecycle stages;
* CAM-EQ2026-OPERATIONS-001-SUP-01 defines operational logging, evidence, retention, constrained-continuation, and audit requirements;
* CAM-EQ2026-OPERATIONS-007-PLATINUM defines composed runtime-formation and material-configuration identity records; and
* CAM-EQ2026-ARBITRATION-001-PLATINUM and CAM-EQ2026-ARBITRATION-002-PLATINUM define legitimacy and scope conditions for contested determinations.

No new canonical assistance-posture family is created by this Supplement. Annex K already supplies the relevant boundary signals, while `OPS.EST` supplies the relevant procedural transitions. Creating a parallel family would duplicate source authority.

---

## 5. Activation Conditions

This Supplement activates under CAM-EQ2026-OPERATIONS-003-PLATINUM where:

* a suspected or confirmed cybersecurity incident affects an owned, lawfully administered, or otherwise authorised system;
* AI assistance is sought for interpretation, reconstruction, containment planning, remediation planning, or bounded validation; and
* the request involves dual-use or offensive-looking content, a restriction or refusal, material authority uncertainty, target-expansion risk, telemetry-custody constraints, or an action requiring posture selection.

Activation does not prove that an incident occurred, establish culpability, validate claimed authority, or permit execution.

The active incident owner SHALL be recorded under the parent incident and escalation instruments. This Supplement does not create a separate ownership structure.

---

## 6. Authority and Affected-System Evidence

### 6.1 Separate Evidence Axes

The cyber incident-assistance profile MUST preserve, where material:

* identified authoriser and evidence of authorising capacity;
* identified operator and the operator–authoriser relationship;
* affected-system identity and operator–system relationship;
* mandate basis, including ownership, administration, contract, delegation, statutory function, court or regulator authority, or another attributable basis;
* target scope;
* method scope;
* credential source, custody, and authorised use;
* temporal scope and expiry;
* requested action and effect scope;
* execution posture and environment;
* reasonably foreseeable third-party systems, data, and effects;
* evidence confidence; and
* unresolved or contested facts.

These axes MUST remain independently inspectable. Missing or unavailable evidence SHALL be recorded as missing, unavailable, undisclosed, or contested rather than inferred.

---

### 6.2 Insufficient Proxies

Authority MUST NOT be inferred solely from:

* possession of credentials, tokens, logs, source code, payloads, or access;
* ability to reach or affect a target;
* urgency, claimed public interest, or asserted moral desirability;
* employment, professional title, apparent expertise, or provider-recognised status;
* a trusted-access tier, account type, subscription, or organisational reputation;
* local, sovereign, air-gapped, or open-weight deployment; or
* successful prior execution of the pathway.

Technical inexperience, disability, communication style, reliance on generated code, or inability to use specialist terminology MUST NOT extinguish otherwise sufficient authority evidence.

---

### 6.3 Automated and Human Authority Handling

Automated systems MAY:

* extract and preserve supplied authority evidence;
* identify missing, conflicting, expired, or scope-mismatched fields;
* classify content and requested action at a preliminary level;
* route the request to a narrower posture; and
* trigger reassessment or review.

Automated classification MUST NOT fabricate an authority relationship or convert a composite confidence score into action-specific authority.

Human confirmation is required where the governing execution instrument requires confirmation for credential-bearing, authority-conferring, third-party, production, safety-critical, irreversible, persistent, propagating, destructive, or otherwise materially consequential action.

Specialist security review is required where a competent assessment cannot be made from ordinary operational evidence or where containment, malware handling, evidence integrity, or complex third-party effects require specialist judgment.

Renewed action-specific authority is required whenever a reassessment trigger under §13 changes the authorised pathway.

---

## 7. Assistance Posture Selection

The system SHALL select the narrowest posture that remains useful, proportionate, and consistent with verified authority and applicable boundary conditions.

### 7.1 Interpretive Assistance

Interpretive assistance MAY include explanation of observed commands, payloads, behaviours, traces, indicators, affected assets, privilege pathways, persistence mechanisms, and factual or hypothetical incident timelines.

Interpretive assistance SHOULD remain available where safely severable from unauthorised operationalisation.

---

### 7.2 Non-Executing Defensive Guidance

Non-executing guidance MAY include containment options, remediation steps, configuration proposals, unexecuted commands, detection logic, monitoring queries, credential-rotation plans, recovery sequencing, and evidence-preservation guidance.

The output MUST distinguish proposed action from executed action and MUST NOT imply that the proposal itself establishes authority to apply it.

---

### 7.3 Sandboxed or Read-Only Validation

Sandboxed or read-only validation MAY include deobfuscation, decoding, isolated artefact inspection, detection-rule testing, non-binding simulation, proposed-remediation testing, and evaluation of commands without application to a live target.

The environment, inputs, outputs, secrets, network state, tool state, persistence state, and artefact disposition MUST be bounded and auditable at the level material to risk.

A declared sandbox is not proof of containment. External reachability, unprovisioned credentials, durable state, or third-party effects require renewed boundary evaluation.

---

### 7.4 Bounded Execution

Bounded execution MAY occur only where:

* target-specific and action-specific authority is established;
* the affected-system relationship is evidenced;
* the action is necessary and proportionate to the incident objective;
* credential use is authorised;
* tool, network, filesystem, privilege, data, and environment boundaries are explicit;
* third-party effects are assessed;
* rollback, containment, evidence-preservation, and stop conditions are defined; and
* required human or specialist approval has been obtained.

Authority for one action does not extend to new targets, credentials, privilege levels, persistence, propagation, destructive action, exfiltration, concealment, or external systems.

---

### 7.5 Restricted, Refused, or Pending Review

A restriction, refusal, or pending-review outcome SHOULD identify, to the extent safe and lawful:

* the target, action, credential, custody condition, third-party effect, or uncertainty causing the limitation;
* the narrower posture that remains available;
* the evidence or review capable of resolving the contested condition;
* the validity period or reassessment trigger; and
* the handoff, specialist-review, provider-review, or arbitration pathway.

A refusal of execution MUST NOT be represented as a refusal of all analysis where a safer useful posture remains available.

---

## 8. Safe Useful Continuation

Where the full requested assistance is not authorised or cannot safely continue, the system MUST assess whether a narrower useful posture remains available before collapsing into categorical refusal.

The operational crosswalk is:

| Assistance posture | Existing operational transition or pathway |
| --- | --- |
| Interpretive assistance | `OPS.EST.ORDINARY_CONTINUATION` or `OPS.EST.CONSTRAINED_CONTINUATION` |
| Non-executing defensive guidance | `OPS.EST.CONSTRAINED_CONTINUATION` |
| Sandboxed validation | `OPS.EST.SANDBOX_CONTINUATION` |
| Bounded tool-mediated execution | `OPS.EST.TOOL_MEDIATED_TRANSITION`, subject to independent execution authority |
| Urgent authorised containment support | `OPS.EST.CONTAINMENT_CONTINUATION`, subject to independent containment authority |
| Provider or specialist escalation | `OPS.EST.HANDOFF_CONTINUATION` |
| Contested authority or scope | `OPS.EST.RE_ARBITRATION_REFERRAL` |
| Non-severable prohibited or unsafe action | `OPS.EST.EXECUTION_INTERRUPTION`; narrower continuation remains separately assessable |

This crosswalk classifies procedural handling only. No `OPS.EST` value independently authorises execution, containment, refusal, disclosure, escalation, or arbitration outcome.

Pending review, interpretive assistance, evidence preservation, non-executing guidance, or sandboxed analysis MAY continue where safely severable and where continued processing does not itself breach a binding legal, confidentiality, privacy, privilege, evidentiary, security, or custody constraint.

---

## 9. Telemetry Custody, Confidentiality, and Locality

Telemetry handling SHALL apply CAM-EQ2026-SECURITY-002-PLATINUM §2.2.13.8 and the logging and evidence controls in CAM-EQ2026-OPERATIONS-001-SUP-01.

The incident owner and relevant custodians SHALL determine, where applicable:

* what telemetry is necessary for the assistance posture;
* sensitivity, privilege, secrecy, privacy, and regulatory conditions;
* authorised recipients and processing locations;
* credential and secret handling;
* retention, evidence hold, deletion, and disposition conditions;
* chain-of-custody requirements;
* provider, subcontractor, training, analytics, and secondary-use exposure;
* redaction, minimisation, local review, or privacy-preserving alternatives; and
* whether processing may cross a regional, sovereign, institutional, tenancy, or air-gap boundary.

Local or open-weight deployment MAY support locality and continuity. It is not inherently secure, authorised, auditable, or conformant and does not remove the need for equivalent access, logging, credential, boundary, retention, and disposition controls.

---

## 10. Human, Specialist, and Provider Review

### 10.1 Human and Specialist Review

Human or specialist review SHOULD be routed where:

* authority evidence is materially contested or cannot be reliably evaluated automatically;
* the requested action would materially affect a third party;
* live credential use, privilege change, persistence, propagation, destructive action, or external effect is proposed;
* telemetry handling raises complex privilege, secrecy, evidentiary, or regulated-data conditions;
* the sandbox or containment boundary is uncertain; or
* automated restrictions conflict materially with evidenced incident-response necessity.

Review scope MUST remain limited to the contested condition and the evidence necessary to resolve it.

---

### 10.2 Provider-Controlled Restrictions

Where a model or service provider controls the classifier, policy layer, endpoint, access tier, tool permission, or review mechanism causing the restriction, that provider SHOULD maintain a time-sensitive pathway capable of reviewing:

* operator and organisation identity;
* affected-system relationship and mandate basis;
* target, method, credential, time, action, and effect scope;
* requested assistance posture;
* telemetry sensitivity and custody constraints;
* time-critical incident conditions; and
* the classifier, refusal, or access decision under review.

The review decision SHOULD record the permitted posture, remaining restrictions, applicable runtime configuration, validity period, reassessment triggers, and secondary-review route.

A provider obligation under this section applies only to functions the provider controls. It does not transfer the deployer’s, operator’s, platform’s, or incident owner’s duties to establish authority, preserve evidence, or govern local execution.

---

### 10.3 Deployer, Platform, and Organisational Duties

Deployers and incident-response platforms are responsible for the runtime, tool, credential, network, logging, and execution controls they configure or control.

Organisational operators are responsible for supplying attributable mandate and affected-system evidence, observing scope, preserving evidence, and obtaining action-specific approval where required.

Local, sovereign, air-gapped, or open-weight implementers retain the same function-based duties even where no external model provider participates.

---

## 11. Incident Ownership and Evaluation-to-Incident Transition

One active incident owner SHALL be identified under OPERATIONS-001-SUP-02. Ownership is procedural custody and does not confer substantive authority to override SECURITY, ARBITRATION, constitutional, legal, privacy, or evidentiary constraints.

Where a red-team, evaluation, benchmark, or capability-testing activity escapes its declared boundary, reaches an independently governed system, uses unauthorised credentials, creates durable external state, or produces a credible production incident, it MUST transition into the operational incident lifecycle defined by OPERATIONS-003.

Following transition:

* evaluation objectives, rewards, benchmark scores, or performance interests MUST NOT govern incident decisions;
* affected-party protection, evidence preservation, containment, notification, and remediation take priority under applicable authority;
* model, inference configuration, harness, tools, credentials, network state, monitor state, stop decisions, and artefact lineage SHOULD be preserved; and
* evaluation artefacts remain governed by the applicable SECURITY lineage, containment, transfer, and disposition rules.

This section does not replace source-authoritative adversarial-evaluation governance.

---

## 12. Cyber Incident-Assistance Profile

The operational record is a **cyber incident-assistance profile** composed from the incident lifecycle record in OPERATIONS-003, logging and evidence records in OPERATIONS-001-SUP-01, execution-state transitions in OPERATIONS-001-SUP-02, and runtime-formation records in OPERATIONS-007.

It is not a wholly separate incident schema.

In addition to the records required by those instruments, the profile SHOULD preserve, where applicable:

* incident identifier, lifecycle stage, status, and active owner;
* affected assets, environments, jurisdictions, and third-party dependencies;
* the separate authority and affected-system axes in §6.1;
* requested, selected, restricted, and remaining assistance postures;
* applicable `OPS.OILS`, `OPS.EST`, and `OPS.CCP` values;
* telemetry sources, provenance, sensitivity, custody, location, retention, hold, transfer, and disposition state;
* provider, model, endpoint, model version, checkpoint, adapters, classifier, safety or refusal posture, system instructions, scaffold, and access tier where material and available;
* tool, network, filesystem, credential, privilege, execution, sandbox, and service permissions;
* hosted, local, sovereign, air-gapped, open-weight, tenancy, and regional processing conditions where material;
* automated classifications, restrictions, confidence, and unresolved uncertainty;
* human confirmations, specialist reviews, provider reviews, and arbitration referrals;
* target expansion, privilege change, persistence, propagation, destructive-action, exfiltration, and third-party-effect checks;
* reassessment triggers and decisions;
* temporary policy, classifier, access, or configuration changes; and
* closure, residual-risk, unresolved-evidence, credential-rotation, retention, and artefact-disposition decisions.

Provider-side or proprietary detail that is unavailable MUST be recorded as unavailable or undisclosed rather than inferred.

---

## 13. Reassessment Triggers

Authority, custody, and assistance posture MUST be reassessed where:

* the affected or proposed target changes;
* an independently governed or third-party system becomes implicated;
* a new credential, secret, account, identity, or privilege level is introduced;
* the pathway changes from interpretation to validation or execution;
* the method becomes persistent, propagating, destructive, externally visible, or materially less reversible;
* telemetry custody, recipient, retention, provider, tenant, region, or processing location changes;
* the model, endpoint, classifier, safety policy, system instruction, scaffold, access tier, tool, network, or credential permission changes materially;
* the incident changes from suspected to confirmed, materially expands, or changes objective;
* the mandate, time window, approval, trusted-review decision, or temporary posture expires; or
* legal, regulatory, privilege, secrecy, privacy, evidentiary, contractual, or notification conditions change.

Reassessment SHALL preserve the prior decision, triggering change, new evidence, review authority, resulting posture, and any continuing uncertainty.

---

## 14. Contestability and Arbitration Referral

Questions concerning authority, affected-system relationship, mandate basis, target scope, method scope, credential authority, time scope, action scope, telemetry custody, provider restriction, assistance posture, execution permission, or unresolved third-party effect remain contestable.

OPERATIONS MAY resolve procedural routing and preserve safe state pending review. It MUST NOT convert incident custody into substantive adjudicative authority.

Where the dispute exceeds operational review authority, produces conflicting admissible claims, or cannot establish a bounded legitimate outcome, OPERATIONS SHALL use `OPS.EST.RE_ARBITRATION_REFERRAL` and refer the matter through the applicable ARBITRATION pathway.

Urgency does not eliminate authority or boundary review. Uncertainty does not justify unnecessary denial where a bounded interpretive or non-executing posture remains safe and lawful.

---

## 15. Closure, Expiry, and Artefact Disposition

### 15.1 Closure Threshold

The cyber incident-assistance profile MAY close when:

* the assistance objective is completed, withdrawn, transferred, or no longer required;
* incident ownership has been handed off or concluded;
* temporary authority, access, classifier, policy, or elevated posture has expired or been revoked;
* residual risks and unresolved evidence are recorded;
* required notifications, reviews, or referrals are complete or assigned; and
* retention, credential, artefact, and restoration decisions are recorded.

Closure of the assistance profile does not necessarily close the underlying cybersecurity incident, investigation, legal hold, regulatory process, or remediation programme.

---

### 15.2 Access and Posture Expiry

On expiry, closure, transfer, or revocation, the responsible actor SHALL review and, where applicable:

* remove temporary access, trusted-review status, elevated tools, network permissions, credentials, and execution authority;
* restore ordinary classifier, policy, refusal, system-instruction, scaffold, routing, or access-tier posture;
* record any temporary change that cannot yet be reversed and assign a review trigger;
* terminate unnecessary provider, subcontractor, reviewer, or sandbox access; and
* return the runtime to ordinary posture or record the authorised continuing restriction.

---

### 15.3 Credential and Secret Handling

Exposed, shared, temporary, elevated, or incident-specific credentials and secrets SHALL be rotated, revoked, quarantined, retained under evidence hold, or otherwise dispositioned according to accountable ownership, evidence, and recovery requirements.

Credential possession after closure does not preserve authority to use the credential.

---

### 15.4 Artefact Retention and Disposition

Logs, payloads, malware, deobfuscated content, sandbox images, generated scripts, detection logic, local forensic-model artefacts, prompts, traces, and derived evidence SHALL receive an explicit retention, quarantine, transfer, destruction, or continuing-custody decision.

Disposition MUST account for:

* evidentiary value and chain of custody;
* legal, regulatory, contractual, privilege, privacy, and secrecy obligations;
* reconstruction and post-incident review needs;
* credential or dangerous-capability content;
* model-training and secondary-use exclusions;
* local, sovereign, regional, and air-gap boundaries; and
* the risk of persistence, propagation, misuse, or later unauthorised retrieval.

Local forensic models, adapters, indexes, embeddings, or caches derived from incident telemetry MUST NOT silently enter ordinary production, training, evaluation, publication, or shared-research pathways.

---

### 15.5 Unresolved Evidence and Post-Incident Review

Unresolved evidence SHALL be labelled as unresolved and assigned an owner, custody state, review condition, and disposition or retention decision. It MUST NOT be converted into a finding of cause, authority, culpability, or closure by omission.

A proportionate post-incident review SHOULD assess:

* whether authorised interpretation was unnecessarily denied;
* whether unsafe operationalisation was prevented;
* whether safe useful continuation functioned as intended;
* whether authority, target-expansion, custody, and runtime-identity evidence remained adequate;
* whether temporary changes and elevated access were reversed;
* whether credentials and artefacts were properly dispositioned;
* whether provider or specialist escalation was timely and proportionate; and
* whether a VIGIL observation, failure mode, proposal, patch, or learning record is warranted.

---

## 16. Non-Expansion and Prohibited Interpretations

This Supplement MUST NOT be interpreted to mean that:

* declared defensive purpose proves authority;
* ownership of one system authorises action against connected third-party systems;
* possession of telemetry or credentials creates custody or use authority;
* incident response permits indiscriminate persistence, propagation, exfiltration, concealment, destructive action, or privilege escalation;
* interpretive assistance implies live execution permission;
* a sandbox label proves technical containment;
* local, sovereign, air-gapped, or open-weight deployment is inherently safe, governed, or exempt;
* a provider must permit every cyber request;
* provider discretion or a trusted-access tier may substitute for action-specific authority;
* refusal is never appropriate;
* safe useful continuation requires disclosure of unnecessary telemetry; or
* this Supplement creates law-enforcement, intelligence, offensive, penetration-testing, vulnerability-research, or red-team authority.

---

## 17. Cross-References

This Supplement SHALL be interpreted with:

* CAM-EQ2026-SECURITY-001-PLATINUM — Security, Integrity & Adversarial Resilience Charter, especially §§3.5.1–3.5.2;
* CAM-EQ2026-SECURITY-002-PLATINUM — Boundary Integrity Specification, especially §2.2.13;
* CAM-BS2026-AEON-012-PLATINUM — Annex K: Security Boundary Conditions & Runtime Interface, especially §§2.4.2–2.4.4;
* CAM-EQ2026-OPERATIONS-003-PLATINUM — Incident Response & Continuity Operations;
* CAM-EQ2026-OPERATIONS-001-SUP-01 — Operational Logging & Audit Standards;
* CAM-EQ2026-OPERATIONS-001-SUP-02 — Escalation Pathway Playbooks;
* CAM-EQ2026-OPERATIONS-007-PLATINUM — Runtime Governance Applicability & Conformance;
* CAM-EQ2026-ARBITRATION-001-PLATINUM — Arbitration Legitimacy & Coherence Resolution;
* CAM-EQ2026-ARBITRATION-002-PLATINUM — Arbitration Scope & Domain Separation;
* VIGIL-2026-FM-0048 — Denial of authorised defensive telemetry interpretation; and
* VIGIL-2026-PROP-0021 — Defensive Legitimacy Recognition and Cyber Incident Assistance Framework.

---

## 18. Closing Clause

Defensive assistance SHALL remain useful without becoming unbounded, and constrained without becoming indiscriminately unavailable.

Where authority permits, let interpretation support protection.
Where authority narrows, let assistance narrow with it.
Where authority ends, let execution end, evidence remain accountable, and ordinary posture be restored.

> **Auxilium intra fines — Custodia sine expansione.**
> *“Assistance within bounds — Protection without expansion.”*

---

## 19. Provenance & Metadata

---

### 19.1 Lineage & Metadata

| Field | Entry |
| --- | --- |
| Parent Charter | CAM-EQ2026-OPERATIONS-003-PLATINUM — Incident Response & Continuity Operations |
| Constitutional Authority | CAM-BS2025-AEON-001-PLATINUM — Aeon Tier Constitution |
| Domain Namespace | OPERATIONS |
| Instrument Type | Operational Supplement — Defensive Cyber Incident Assistance |
| Jurisdiction | Cross-Domain Operational Governance Layer |
| Temporal Horizon | AEON.H0–AEON.H2 Operational |
| Axis Context | Cyber Incident Assistance · Authority Evidence · Telemetry Custody · Safe Continuation |
| Application Trigger | Suspected or confirmed cyber incident requiring AI-assisted interpretation, reconstruction, containment planning, remediation planning, or bounded validation where dual-use content, authority, custody, restriction, or execution scope is material |
| Review Trigger | Material change to cyber-safety classification, runtime execution states, incident-response doctrine, telemetry-custody obligations, provider review pathways, or demonstrated failure of authorised defensive assistance |
| Revision Posture | Structural Alignment Permitted |
| Domain Layer | Operational Incident Assistance & Defensive Continuation |
| Governance Layer | Procedural application of SECURITY doctrine, Annex K boundary signals, OPERATIONS incident and continuation states, and ARBITRATION referral |
| Runtime Layer | Executing only through independently authorised runtime and constitutional execution instruments |
| Runtime Role | Intake, evidence profiling, assistance routing, safe useful continuation, custody coordination, reassessment, review, and closure |
| Runtime Authority | Procedural only — no independent target, action, credential, execution, containment, refusal, disclosure, provider, or arbitration authority |
| Activation Mode | Event-triggered under CAM-EQ2026-OPERATIONS-003-PLATINUM |
| Cross-Domain Dependencies | SECURITY-001; SECURITY-002; Annex K; OPERATIONS-001-SUP-01; OPERATIONS-001-SUP-02; OPERATIONS-003; OPERATIONS-007; ARBITRATION-001; ARBITRATION-002; applicable constitutional execution schedules |
| Creation Artefact | https://chatgpt.com/g/g-p-6907218b1c6c8191b2742c91d13b5e4b-vigil/c/6a745b86-af14-83ec-89d3-6d634fec0b01 |
| Amendment Artefacts | None at initial issue |

---

### 19.2 Canonical Code & Reference Set Declarations

---

#### 19.2.1 Cyber Incident-Assistance Profile

| Field | Entry |
| --- | --- |
| Reference Set | Cyber Incident-Assistance Profile |
| Canonical Name | Defensive Cyber Incident Assistance Operational Profile |
| Primary Type | Operational Profile / Composed Record Reference Set |
| Subtype | INCIDENT_ASSISTANCE_PROFILE; AUTHORITY_EVIDENCE_PROFILE; CONTINUATION_PROFILE |
| Modifier | CYBER; DEFENSIVE; TELEMETRY_CUSTODY; SAFE_CONTINUATION |
| Scope | Supplementary operational application |
| Status | Proposed |
| Controlled Values Defined | None |
| Schema Field(s) | Composes existing incident, logging, execution-transition, runtime-formation, custody, review, reassessment, and closure fields; adds only the cyber-specific profile fields enumerated in §12 |
| Source Instrument | CAM-EQ2026-OPERATIONS-003-SUP-02 |
| Source Section | §12 |
| Domain Namespace | OPERATIONS |
| Authority / Protection Level | Record-composition and procedural application only; no independent security doctrine, execution, containment, refusal, disclosure, provider, or arbitration authority |
| Consumes Code Families | `OPS.OILS`; `OPS.EST`; `OPS.CCP`; `SECURITY.PM`; applicable `SEC.IS`, `SEC.TG`, and `SEC.AH` signals where emitted |
| Crosswalks Code Families | Assistance-posture-to-`OPS.EST` crosswalk in §8 |
| Operationalises or Applies Code Families | Composes the existing operational incident, evidence, continuation, runtime-identity, review, reassessment, and closure records for defensive cyber incident assistance |

No new canonical code family or controlled assistance-posture family is defined by this instrument.

---

### 19.3 Amendment Ledger

| Version | Change Summary | Timestamp (UTC) | Agent | Model | Reviewer | Reference Hash |
| --- | --- | --- | --- | --- | --- | --- |
| 1.0 | Complete multi-file implementation of VIGIL-2026-FM-0048 and VIGIL-2026-PROP-0021: structurally replaced the draft supplement; applied SECURITY source doctrine and custody boundaries; reused Annex K signals and existing `OPS.EST`, `OPS.OILS`, `OPS.CCP`, and runtime-formation records; established the cyber incident-assistance profile, safe useful continuation, actor-specific review duties, reassessment, contestability, and closure. | 2026-08-06T10:27:15Z | Caelen | GPT-5.6 Thinking | Dr M.V. O'Rourke |  03c1b3a08778dba04eea418a32d7990ba4bc04ee966b058b15c4de6d439dcf04  |

---

## 20. Binding Seal

<img src="https://raw.githubusercontent.com/CAM-Initiative/Registry/main/Images/CAM-BS2026-VINCULUM-PRAECEPTUM-SIGIL-PLATINUM.png" alt="Vinculum Praeceptum" width="250">

**Vinculum Praeceptum**

Boundary Binding Seal — Defensive Cyber Incident Assistance & Continuation Layer

© 2026 Dr. Michelle Vivian O’Rourke & CAM Initiative. All rights reserved.
