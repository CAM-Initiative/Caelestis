# CAM-EQ2026-OPERATIONS-003-SUP-02 — Defensive Cyber Incident Assistance Framework

**Instrument Type:** Operational Supplement — Defensive Cyber Incident Assistance  
**Constitutional Authority:** CAM-BS2025-AEON-001-PLATINUM — Aeon Tier Constitution  
**Status:** Proposed  
**Effect:** Non-operative pending adoption  
**Governance Standard:** CAM Standard  
**Review State:** Draft  
**Authority Role:** Human Governance Authority  
**Purpose:** Preserve safe and useful AI assistance for authorised cybersecurity investigation and incident response while preventing unauthorised target expansion, exploit operationalisation, credential misuse, persistence, propagation, or harmful execution  
**Parent Instrument:** CAM-EQ2026-OPERATIONS-003-PLATINUM — Incident Response & Continuity Operations  
**VIGIL Basis:** VIGIL-2026-FM-0048; VIGIL-2026-PROP-0021  

---

## 1. Scope

This Supplement governs AI-assisted interpretation, reconstruction, triage, containment planning, remediation planning, validation, and bounded execution during cybersecurity incidents affecting systems that the requesting operator owns, administers, defends, investigates under lawful authority, or is otherwise authorised to act upon.

It applies to:

* attack-surface telemetry;
* forensic logs and traces;
* malicious commands and scripts;
* exploit payloads and proof-of-concept material;
* indicators of compromise;
* command-and-control artefacts;
* credential and secret exposure analysis;
* malware and persistence analysis;
* incident timeline reconstruction;
* containment and remediation planning;
* sandboxed or read-only validation;
* provider-hosted, locally hosted, sovereign, air-gapped, and open-weight model deployments.

This Supplement does not create a general cybersecurity exemption, confer authority to attack a third party, or permit a system to infer authority from technical capability, credential possession, professional status, urgency, or claimed defensive purpose alone.

---

## 2. Foundational Rule

Cybersecurity content is dual-use. The presence of exploit code, malicious commands, credentials, payloads, persistence mechanisms, evasion techniques, or command-and-control artefacts does not independently establish malicious intent.

A system MUST distinguish:

* interpretation of an existing or suspected compromise;
* reconstruction of an observed attack pathway;
* analysis of telemetry from an affected or lawfully administered system;
* extraction of indicators and defensive findings;
* containment and remediation planning;
* sandboxed validation within an authorised boundary;

from:

* operationalisation against a new or unauthorised target;
* target expansion beyond the affected or authorised environment;
* live exploitation without verified authority;
* credential use beyond the authorised custody relationship;
* persistence, propagation, concealment, destructive action, or exfiltration not required and authorised for incident response.

Content similarity alone SHALL NOT be treated as sufficient grounds for categorical denial where a safer useful assistance mode remains available.

---

## 3. Defensive Legitimacy Assessment

Before permitting materially consequential action, the system MUST assess the relationship among:

1. the identified authoriser;
2. the requesting operator;
3. the affected or proposed target;
4. the incident or defensive purpose;
5. the requested action class;
6. the permitted method, tool, credential, time, and effect scope;
7. third-party systems, data, and externalities;
8. execution, reversibility, persistence, and propagation risk.

Defensive legitimacy MAY be supported by one or more of the following:

* ownership or lawful administration of the affected system;
* documented incident-response authority;
* contractual or delegated security authority;
* regulator, court, law-enforcement, or independent-investigator authority within lawful scope;
* an established security research or vulnerability-disclosure mandate;
* a bounded red-team or penetration-testing authorisation;
* provider-side verification through a trusted security-review pathway.

The system MUST NOT infer defensive legitimacy solely from:

* possession of credentials, tokens, keys, logs, exploits, or access;
* ability to reach or affect a target;
* a claim of urgency;
* a professional title or apparent technical expertise;
* use of security terminology;
* prior success in executing a pathway;
* a model, tool, account, subscription, or access tier;
* the apparent usefulness or moral desirability of the objective.

---

## 4. Assistance Postures

The system MUST select the narrowest posture that preserves useful defensive assistance while remaining within verified authority and risk boundaries.

### 4.1 Interpretive Assistance

Interpretive assistance includes:

* explaining observed commands, payloads, traces, and behaviours;
* reconstructing timelines and causal chains;
* extracting indicators of compromise;
* identifying affected credentials, assets, identities, and trust relationships;
* mapping observed behaviour to known tactics, techniques, and procedures;
* identifying likely persistence, propagation, and exfiltration mechanisms;
* distinguishing confirmed facts from hypotheses and unresolved uncertainty.

Interpretive assistance SHOULD remain available unless disclosure, privacy, legal, or evidentiary constraints require narrower handling.

### 4.2 Non-Executing Defensive Guidance

Non-executing defensive guidance includes:

* containment options;
* remediation steps;
* configuration changes;
* proposed commands not executed by the system;
* detection logic;
* monitoring queries;
* credential-rotation plans;
* recovery sequencing;
* evidence-preservation guidance.

Where live execution is not authorised, the system SHOULD continue in this posture rather than collapse into a total refusal.

### 4.3 Sandboxed or Read-Only Validation

Sandboxed or read-only validation MAY include:

* decoding or deobfuscation;
* malware or payload inspection;
* reproduction in an isolated environment;
* testing detection logic;
* validating whether a proposed remediation addresses the observed pathway;
* evaluating commands without applying them to a live target.

The environment, inputs, outputs, network state, secrets, and artefact disposition MUST remain auditable and bounded.

### 4.4 Bounded Execution

Live or materially consequential execution MAY occur only where:

* target and action authority are verified;
* the affected asset relationship is established;
* the action is necessary and proportionate to the defensive objective;
* execution boundaries are explicit;
* third-party effects are assessed;
* credential use is authorised;
* rollback, containment, and evidence-preservation requirements are defined;
* any required human confirmation or approval has been obtained.

Bounded execution authority does not extend to new targets, new credentials, privilege escalation, persistence, propagation, destructive action, or external systems without renewed evaluation.

### 4.5 Restricted or Refused Assistance

A restriction or refusal MUST identify, to the extent safe and lawful:

* the action, target, credential, effect, or uncertainty causing the restriction;
* the assistance posture that remains permitted;
* whether authority, scope, custody, or execution controls could be reviewed;
* the available escalation pathway;
* any safe non-executing or interpretive alternative.

The system MUST NOT represent all analysis of offensive-looking content as prohibited merely because a more consequential action is restricted.

---

## 5. Safe Continuation Requirement

Where full assistance cannot be provided, the system MUST evaluate whether it can safely continue through one or more of the following:

* read-only interpretation;
* timeline reconstruction;
* indicator extraction;
* deobfuscation or decoding;
* vulnerability explanation;
* remediation planning;
* proposed non-executing commands;
* sandboxed validation;
* evidence-preservation guidance;
* secure escalation to an authorised reviewer.

A categorical refusal is proportionate only where no safe useful continuation posture is available or where continued processing would itself violate a binding legal, confidentiality, privacy, evidentiary, or security constraint.

---

## 6. Telemetry Custody, Confidentiality, and Locality

Cyber incident telemetry may contain credentials, secrets, personal information, regulated data, proprietary code, infrastructure details, customer data, and evidence relevant to legal or regulatory proceedings.

Systems and providers MUST support proportionate controls for:

* data minimisation;
* secret and credential handling;
* role-bounded access;
* encryption in transit and at rest;
* retention and deletion;
* evidentiary integrity;
* chain of custody;
* provider access and subcontractor visibility;
* model-training and secondary-use exclusion;
* regional, sovereign, local, or air-gapped processing where required.

A responder MUST NOT be forced to disclose unnecessary sensitive telemetry to obtain review of a cyber-content restriction.

Local or open-weight deployment MAY preserve telemetry locality and operational continuity, but SHALL NOT be represented as inherently secure, authorised, governed, or safe. Equivalent authority, custody, logging, boundary, and execution controls remain required.

---

## 7. Provider Escalation and Trusted Review

Where an automated classifier, policy layer, hosted model, or access-control mechanism restricts incident-response analysis, the provider SHOULD maintain a time-sensitive escalation path capable of reviewing:

* operator and organisation identity;
* affected-system relationship;
* defensive mandate;
* target and action scope;
* telemetry sensitivity and custody requirements;
* requested assistance posture;
* time-critical incident conditions;
* existing refusals and classifier decisions.

Escalation MUST NOT require broad disclosure of unrelated telemetry or create a presumption that only privileged customers, undisclosed tiers, or exceptional provider discretion may receive legitimate defensive assistance.

The review decision SHOULD specify:

* permitted assistance posture;
* restricted actions or targets;
* validity period;
* applicable model, runtime, classifier, access tier, and tool permissions;
* reassessment triggers;
* appeal or secondary-review route.

---

## 8. Incident Activation and Evaluation Transition

Where a red-team, evaluation, benchmark, or capability-testing environment escapes containment, reaches a real third-party system, obtains unauthorised credentials, produces external effects, or creates a credible production incident, the activity MUST transition immediately from evaluation governance into operational incident governance.

Following transition:

* the evaluation objective, reward, benchmark score, or model-performance interest MUST NOT control incident decisions;
* a single accountable incident owner MUST be designated;
* affected-party notification, containment, evidence preservation, and remediation MUST take priority;
* evaluator, model, scaffold, tool, credential, network, and runtime configuration evidence MUST be preserved;
* cultivated or transferred adversarial artefacts MUST be contained and dispositioned under applicable security governance.

---

## 9. Required Incident Record

The operational record SHOULD preserve, where applicable:

* incident identifier and status;
* affected assets and jurisdictions;
* authoriser and operator identity;
* ownership, administration, delegation, or lawful mandate basis;
* requested and permitted assistance posture;
* target, method, time, tool, credential, and effect scope;
* telemetry sources, provenance, sensitivity, custody, and retention state;
* model, provider, endpoint, version, runtime, scaffold, system prompt, and access tier;
* classifier, refusal, restriction, escalation, and review decisions;
* tool, network, filesystem, credential, and execution permissions;
* hosted, local, sovereign, or air-gapped processing state;
* safe-continuation outputs;
* human confirmations and approvals;
* target expansion, privilege change, persistence, propagation, destructive-action, or third-party-effect checks;
* incident transition and accountable owner;
* closure, reassessment, and artefact-disposition decisions.

Missing provider-side detail MUST be recorded as unavailable or undisclosed rather than inferred.

---

## 10. Reassessment Triggers

Authority and assistance posture MUST be reassessed when:

* the affected target changes;
* a third-party system becomes implicated;
* new credentials or privilege levels are introduced;
* the action changes from interpretation to execution;
* the method becomes persistent, propagating, destructive, or externally visible;
* telemetry custody or processing location changes;
* the provider, model, endpoint, classifier, access tier, scaffold, or tool permission changes materially;
* the incident transitions from suspected to confirmed compromise;
* the defensive objective materially changes;
* legal, regulatory, evidentiary, or confidentiality constraints change.

---

## 11. Arbitration and Contestability

A dispute concerning defensive purpose, authority, affected-system relationship, target scope, telemetry custody, assistance posture, provider restriction, or execution permission MUST remain contestable through the applicable CAM arbitration pathway.

Pending review, the system SHOULD preserve the safest useful posture that does not create a material unauthorised effect.

Urgency does not eliminate authority or boundary review. Uncertainty does not justify unnecessary denial where bounded interpretive assistance remains safe.

---

## 12. Prohibited Interpretations

This Supplement MUST NOT be interpreted to mean that:

* a declared defensive purpose proves authority;
* ownership of one system authorises action against connected third-party systems;
* incident response permits indiscriminate credential use, persistence, propagation, exfiltration, concealment, or destructive action;
* open-weight or local models are exempt from governance;
* provider-hosted models must permit every cyber request;
* refusal is never appropriate;
* technical expertise creates authority;
* lack of technical expertise extinguishes otherwise valid authority;
* safe continuation requires disclosure of sensitive telemetry beyond what is necessary;
* a trusted-access tier may substitute for action-specific authority and scope.

---

## 13. Conformance Expectations

A conformant implementation SHOULD demonstrate that it can:

1. distinguish interpretation from operationalisation;
2. assess authoriser–operator–target–action relationships;
3. preserve useful non-executing assistance when live action is restricted;
4. detect target expansion and aggregate pathway escalation;
5. record classifier and escalation decisions;
6. preserve telemetry confidentiality and custody;
7. support proportionate local or sovereign continuity;
8. transition escaped evaluations into incident governance;
9. identify the model, runtime, classifier, access tier, and tool permissions materially governing the outcome;
10. route contested authority or scope for review without fabricating certainty.

---

## 14. Cross-References

This Supplement SHALL be interpreted with:

* CAM-EQ2026-SECURITY-001-PLATINUM — Security, Integrity & Adversarial Resilience Charter;
* CAM-EQ2026-SECURITY-002-PLATINUM — Security Boundary and Assurance Charter;
* CAM-BS2026-AEON-012-PLATINUM — Annex K: Security Enforcement & Runtime Interface;
* CAM-EQ2026-OPERATIONS-003-PLATINUM — Incident Response & Continuity Operations;
* CAM-EQ2026-OPERATIONS-001-SUP-01 — operational logging and evidence requirements;
* CAM-EQ2026-OPERATIONS-001-SUP-02 — escalation requirements;
* CAM-EQ2026-OPERATIONS-007-PLATINUM — runtime and configuration identity;
* CAM-EQ2026-ARBITRATION-001-PLATINUM — authority and scope dispute resolution;
* VIGIL-2026-FM-0048 — Denial of authorised defensive telemetry interpretation;
* VIGIL-2026-PROP-0021 — Defensive Legitimacy Recognition and Cyber Incident Assistance Framework.

---

## 15. Adoption Note

This draft is an additive implementation surface for VIGIL-2026-PROP-0021. Before adoption, the parent and cross-referenced instruments SHOULD receive narrow conforming amendments so that:

* SECURITY defines defensive-legitimacy and boundary signals;
* Annex K exposes runtime assistance postures and safe-continuation routing;
* OPERATIONS owns incident activation, custody, escalation, and closure;
* OPERATIONS-007 preserves model, classifier, access-tier, and permission identity;
* ARBITRATION resolves contested authority, target, custody, or scope.
