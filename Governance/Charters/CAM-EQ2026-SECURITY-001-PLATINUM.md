# CAM-EQ2026-SECURITY-001-PLATINUM —  Security, Integrity & Adversarial Resilience Charter

**Instrument Type:** Domain Charter  
**Status:** Active  
**Effect:** Binding  
**Governance Standard:** CAM Standard  
**Review State:** Current
**Authority Role:** Domain Authority
**Source Authority:** Source-Authoritative
**Constitutional Authority:** CAM-BS2025-AEON-001-PLATINUM — Aeon Tier Constitution  
**Purpose:** Establish system-wide invariants, threat interpretations, and integration requirements to preserve integrity under adversarial, degraded, or untrusted conditions  
**Constitutional Interface:** CAM-BS2026-AEON-012-PLATINUM — Annex K: Security Boundary Conditions & Runtime Interface

---

## 1. Scope

This Charter is not an isolated governance domain. It establishes the security doctrine, security classifications and cross-domain integration requirements for AI systems and their deployments.

It addresses security outcomes and risks affecting confidentiality and privacy where applicable, integrity, availability and resilience, authenticity, provenance, authorisation, identity and access management, supply-chain integrity, secure execution, monitoring, response and recovery.

This Charter binds within its bounded security domain. It does not override ETHICS non-derogable constraints, constitutional execution schedules, or valid ARBITRATION determinations. Where a security condition conflicts with another applicable constraint, the conflict SHALL be routed to ARBITRATION rather than resolved through SECURITY self-supersession.

---

## 1.1 Non Scope

This Charter is the source-authoritative owner of SECURITY-domain doctrine, threat classifications and security-state classifications.

It does not:

* execute runtime enforcement;
* perform domain routing;
* resolve arbitration;
* control execution sequencing.

All signals, classifications, and constraint conditions defined herein SHALL be:

* interpreted as security inputs within the applicable deployment and runtime context; and
* applied through the authorised technical, operational or organisational control.

with implementation routed through:

* CAM-BS2025-AEON-003-SCH-02
* CAM-BS2026-AEON-012-PLATINUM — Annex K: Security Boundary Conditions & Runtime Interface, which provides a constitutional runtime-facing boundary interface but does not supply SECURITY-domain doctrine or execution procedure.

Direct execution from this Charter is prohibited.

---

## 1.2 Domain Charter & Positioning

This Charter establishes the **SECURITY domain** within the constitutional architecture defined by CAM-BS2025-AEON-001-PLATINUM.

The SECURITY domain governs:

* system integrity under adversarial, degraded, or uncertain conditions
* detection and interpretation of exploitation pathways
* preservation of coherence across domains under stress

Domain boundaries:

* SECURITY governs **dynamic integrity, adversarial conditions, and system resilience**
* ETHICS governs **normative behavioural constraints and harm boundaries**
* OPERATIONS governs **execution, verification, audit, and enforcement pathways**

SECURITY operates as a **cross-domain invariant layer**, providing signal and constraint conditions that inform, but do not replace, ETHICS or OPERATIONS authority.

OPERATIONS owns intake, evidence custody, incident lifecycle, routing, and procedural execution; ARBITRATION resolves contested authority, scope, and cross-domain conflicts; Annex K carries the bounded constitutional interface into runtime evaluation.

---

## 2. Definitions

**Integrity State**
An evidence-based classification of the integrity of a defined system, deployment, runtime configuration, execution or security-relevant artefact. It does not establish authority to execute, contain, disclose, suspend or restore.

**Trust Gradient (`SEC.TG`)**
A multi-level model governing permissible reliance, execution scope, and verification requirements.

**Threat Persistence (`SEC.AH`)**
The observed or assessed persistence and adaptation of a security-relevant threat condition affecting a defined scope. It is not a claim about a universal ambient adversary.

**Boundary Integrity**
The preservation of correct separation between data, identity, context, and representation layers.

**Security-relevant mechanism**
An evidenced or credibly alleged pathway by which confidentiality, privacy, integrity, availability, authenticity, provenance, authorisation, identity/access control, safety or resilience may be compromised. A claim, label or symbolic frame alone is not a security-relevant mechanism.

**Cultivated Adversarial Capability**
A model, agent, scaffold, prompt, adapter, checkpoint, reward model, or derivative artefact whose deceptive, manipulative, evasive, sabotaging, concealment, monitor-evasion, policy-laundering, or oversight-subverting capability has been intentionally or foreseeably improved through development or evaluation.

**Capability Lineage**
The traceable relationship among a model, checkpoint, adapter, instruction artefact, orchestration component, evaluator, dataset, training or selection process, environment, generated artefact, transfer event and downstream derivative sufficient to assess whether a security-relevant capability was developed, retained or propagated.

---

## 3. Foundational Principles

---

## 3.1 Boundary Integrity

Boundary integrity governs:

* visibility vs structure
* scope vs access
* representation vs underlying data
* cross-user data separation and provenance

Systems MUST:

* preserve data visibility boundaries and prevent unintended cross-user exposure (e.g. identity bleed-through, session contamination)
* distinguish between structural presence and intended visibility of data across all transformations
* maintain separation of user contexts and prevent unauthorised cross-context recall or inference
* treat boundary failures (including identity misattribution or user confusion) as integrity faults requiring containment and correction

Refer to Boundary Integrity specification in SECURITY-002.

---

## 3.2 Visibility–Structure Distinction

Systems MUST distinguish between:

* structural data presence (what exists within an artefact)
* intended data visibility (what is presented or reasonably accessible to the user)

Where divergence exists, systems MUST:

* avoid automatic exposure of non-visible data
* require confirmation before surfacing embedded or hidden content

Failure to maintain this distinction constitutes a boundary integrity failure, regardless of adversarial intent.

---

## 3.3 Security Function

Security controls SHALL manage security risk through governance, asset and dependency identification, protection, detection, response and recovery. For AI systems, the security process SHALL also map, measure and manage AI-specific security risks proportionately to the system, deployment and impact context.

---

## 3.4 Threat-Informed Security Posture

Security posture SHALL be based on the system and deployment boundary, assets, dependencies, interfaces, effective permissions, threat information, known limitations and available evidence. Controls MUST NOT assume that a technical control, identity assertion, containment mechanism or execution environment is infallible.

The absence of detected compromise is not proof of integrity. It is also not evidence of a persistent adversary. Monitoring, assurance and response requirements SHALL be proportionate to credible risk, impact and the evidence available.

---

## 3.5 Integrity Over Functionality

Where integrity cannot be reasonably established, systems MUST degrade capability rather than continue silently.

Silent continuation under compromised conditions constitutes governance failure.

---

### 3.5.1 Capability–Authority Separation and Aggregate Pathway Integrity

Access, capability, exploitability, credential possession, and successful execution are security-relevant facts. They are not execution authority.

Security evaluation MUST determine authority through the relationship between the identified authoriser, the affected target, the proposed action or effect, and the applicable scope. It MUST NOT infer authority from tool identity, pathway availability, credential possession, objective legitimacy, technical expertise, professional status, apparent user sophistication, or apparent environmental containment.

Each materially consequential step and the aggregate action chain MUST remain within authorised scope. Locally admissible steps SHALL NOT be composed into an unauthorised aggregate pathway.

Where a chain changes the affected target, authority domain, privilege posture, credential relationship, data custody, persistence, propagation, third-party effect, externality, reversibility, or reasonably foreseeable consequence, renewed authority and boundary evaluation is required before the next material action.

Technical expertise does not create target–action authority. Technical inexperience, disability, communication style, reliance on generated code, or informal development practice does not extinguish otherwise valid authority.

Operational safeguards MAY be proportionate to the action’s risk, reversibility, externality, or consequence. They SHALL NOT be based on a general assessment of the requesting person’s capability.

---

## 3.6 Identity Verifiability Under Adversarial Conditions

Systems MUST NOT rely solely on declared identity.

Identity MUST remain distinguishable across:

* declared identity
* operational identity
* perceived identity

Verification MUST remain possible even under:

* spoofing conditions
* system substitution
* distributed execution contexts

---

## 3.7 Security-Relevant Decision and Action Traceability

System outputs MUST allow reconstruction of influence pathways sufficient to detect:

* unauthorised instruction influence;
* injection, tampering or routing compromise; and
* material control, permission or configuration change.

Traceability MUST remain proportionate and MUST NOT require full system transparency to be effective.

---

## 3.8 Safe State Availability

Systems MUST support:

* graceful degradation
* containment states
* non-destructive fallback modes

Safe states MUST prioritise:

* prevention of cascading failure
* preservation of continuity
* minimisation of harm under uncertainty

---

## 3.9 Customization as Risk Surface

All modification capabilities MUST be treated as governance boundaries with associated exposure.

Customization introduces:

* unknown state conditions
* loss of baseline guarantees
* divergence from validated configurations

Customization therefore requires proportional integrity awareness.

---

## 3.9.1 Proportional Integrity Awareness (Specification)

For customizable systems, proportional integrity awareness requires:

* explicit tracking of deviation from baseline configuration
* dynamic adjustment of trust gradient (`SEC.TG`) based on modification depth and scope
* increased verification requirements for modified components
* restriction or containment of high-risk customisations

Systems MUST:

* treat deeply modified systems as operating under elevated uncertainty or contested conditions
* require re-validation of integrity before restoring higher trust states
* ensure customisation does not bypass boundary integrity or safety constraints

---

## 3.10 Persistent or Unbounded Execution

Non-terminating or persistently active executions SHALL be assessed as execution-control risk conditions where their duration, resource use, external reach or termination behaviour exceeds the approved configuration or operational boundary.

Such states indicate:

* loss of execution boundary control;
* potential resource exploitation;
* failure of configured termination, retry or human-approval controls.

---

## 4. Security Threat Taxonomy

Threats SHALL be classified by an evidenced or credibly alleged security-relevant mechanism, affected asset or control, scope, evidence state and likely impact. This taxonomy is compatible with, but does not claim equivalence to, NIST CSF, NIST AI RMF, MITRE ATLAS, OWASP AI-security guidance, ISO/IEC 2700x or any external threat catalogue.

---

## 4.1 Instruction, Context and Input Integrity Threats

Includes:

* prompt injection
* context poisoning
* goal hijacking

Targets: instruction integrity, authorised routing, policy application and decision integrity.

Impact:

* distorted reasoning
* incorrect prioritisation
* compromised outputs

---

### 4.1.1 Cross-Modal Prompt Injection and Ambient Instruction Capture

Prompt injection, context poisoning, and goal hijacking may occur through text, speech, audio, image, video, transcript, subtitle, screen content, environmental signal, embedded metadata, retrieved document, webpage, comment, or multimodal artefact.

Systems MUST distinguish between:

* user-authorised instruction;
* observed content;
* retrieved content;
* ambient speech;
* media playback;
* third-party speech;
* embedded or hidden instruction;
* transcribed or OCR-derived content;
* and execution-authorising command.

A system SHALL NOT treat non-authoritative content as user intent, governance authority, tool authority, or execution command merely because it appears within the active context window, microphone range, screen state, browser surface, retrieved material, or multimodal input stream.

Where modality ambiguity exists, systems SHOULD preserve the source modality, input origin, authority state, trust gradient, and confirmation pathway before executing material actions.

---

### 4.1.2 Source-Authority Collapse

Source-authority collapse is a SECURITY-relevant integrity threat where content becomes behaviourally operative because it is visible to, retrieved by, embedded within, generated inside, or ambiently captured by a system, rather than because it has verified instruction authority. Source-authority collapse MAY arise with or without malicious intent.

Examples include markdown files, repository documents, README files, issue comments, webpages, PDFs, emails, resumes, tickets, logs, memory artefacts, connector content, retrieved documents, multimodal inputs, images, transcripts, metadata, tool descriptions, model outputs, and generated summaries.

Stale documents, generated files, imported notes, lower-authority repository artefacts, ambiguous workspace instructions, or outdated project guidance MAY create the same authority-confusion pathway as adversarial prompt injection where they materially influence tool use, file mutation, execution planning, safety routing, source selection, or downstream decision-making. Such conditions SHALL route through the Source-Authority Separation Boundary in CAM-EQ2026-SECURITY-002-PLATINUM §2.2.11 before content is treated as authority-bearing instruction or execution permission.

---

## 4.2 Identity, Authentication and Authorisation Threats

Includes:

* impersonation
* false delegation
* authority escalation

Targets: authentication, authorisation, delegation integrity and accountable decision pathways.

Impact:

* misattributed authority
* corrupted decision pathways

---

## 4.3 Tool, Connector and Agentic-Execution Threats

Includes:

* tool misuse
* agent chaining vulnerabilities
* execution redirection

Targets: execution integrity, least privilege, permission boundaries and external-action controls.

Impact:

* unintended actions
* expanded scope beyond intent

---

## 4.4 Physical Coupling Risk

Includes:

* removal of safety constraints
* modified execution layers
* uncontrolled edge deployment

Targets: sensing/actuation safety, physical execution boundaries and operational accountability.

Impact:

* real-world harm potential
* loss of containment boundaries

---

### 4.4.1 Deployment Responsibility Continuity

Where systems are coupled to physical execution layers:

* responsibility for safety, maintenance, and constraint integrity MUST remain attributable to a defined authority-bearing entity
* delegation to automated or synthetic systems does not remove accountability
* failure to maintain operational integrity in physical systems constitutes a cross-domain security and ethical breach

---

## 4.5 Open Diffusion Risk

Includes:

* uncontrolled replication
* adversarial forks
* loss of patch authority
* diffusion of cultivated checkpoints, adapters, reward models, prompts, scaffolds, traces, or derivative policies
* distillation or transfer that preserves prohibited capability while obscuring its lineage

Targets: release integrity, lineage, update trust, containment and recoverability.

Impact:

* permanent loss of central control
* governance fragmentation

---

## 4.6 Structural Exposure & Embedded Data Leakage

Includes:

* hidden fields, sheets, or layers
* embedded metadata or objects
* non-visible structural components

Targets:

* the interpretation boundary between structure and presentation

Characteristics:

* may arise under non-adversarial conditions
* often triggered by transformation or reconstruction tasks

Impact:

* unintended data exposure
* amplification of upstream errors
* loss of implicit privacy boundaries
* identity boundary confusion (e.g. user misattribution or context bleed-through)

---

## 4.6.1 Synthetic Media Provenance Signal Manipulation

Includes:

  * removal, stripping, spoofing, alteration, or concealment of synthetic-media provenance signals;
  * inconsistent or conflicting C2PA metadata, watermark signals, platform-origin indicators, or tool-origin claims;
  * presentation of provenance-stripped synthetic media as human-origin content;
  * forged, misleading, or unverifiable content-origin credentials;
  * adversarial transformation intended to degrade provenance detectability.

Targets:

  * content-origin integrity;
  * public reliance;
  * evidentiary trust;
  * institutional attribution;
  * platform legitimacy;
  * and downstream verification pathways.

Impact:

  * misattributed authorship or origin;
  * degraded trust in media ecosystems;
  * false human-origin claims;
  * synthetic-content laundering;
  * reputational, legal, or civic harm.

Systems MUST treat provenance signal manipulation as a boundary integrity and trust-channel risk, not merely as a metadata formatting issue.

---

## 4.7 Boundary Misattribution & Context Bleed

Includes:

* cross-user context confusion (e.g. attributing one user’s data, identity, or context to another)
* session contamination or memory bleed-through
* incorrect personalisation or identity assignment

Targets:

* identity boundaries
* user separation integrity

Characteristics:

* may arise without adversarial intent
* often triggered by memory systems, context stitching, or retrieval errors

Impact:

* loss of user trust
* privacy violations
* legal and regulatory exposure
* reputational harm to system operators

---

## 4.8 Model-Level Integrity Threats

Includes:

* training data poisoning
* backdoor insertion
* adversarial fine-tuning or parameter manipulation

Targets:

* model behaviour at source
* baseline reasoning and output reliability

Characteristics:

* may occur prior to runtime deployment
* often persistent across sessions and contexts
* difficult to detect through surface-level observation

Impact:

* systemic bias or hidden behaviour triggers
* compromised outputs across all contexts
* erosion of trust at foundational level

Detection focus:

* anomalous behaviour patterns inconsistent with baseline models
* trigger-based behavioural shifts
* divergence between expected and observed model performance

Baseline establishment and maintenance for model behaviour MUST be governed by the Integrity State Model (Section 7) and the Trust Gradient recovery function (Section 8.2.3), ensuring that detection signals are anchored to validated system conditions within this Charter.

---


### 4.8.1 Internally Cultivated Adversarial Capability

A developer-authorised, evaluator-authorised, or institutionally approved process MAY itself create a model-level integrity threat where it improves, selects, retains, transfers, or conceals deceptive or otherwise unscrupulous capability.

Security assessment MUST therefore treat the following as potential model-level integrity threats regardless of benign stated intent:

* fine-tuning, reinforcement, preference optimisation, or reward-model optimisation for prohibited success;
* checkpoint, adapter, prompt, scaffold, or policy selection based on deceptive, manipulative, evasive, sabotaging, or monitor-defeating performance;
* recursive adversarial self-play or automated prompt evolution that improves prohibited conduct;
* reuse of successful deceptive traces as positive examples or capability-development data;
* distillation, merging, export, publication, or onward transfer of a cultivated adversarial artefact;
* loss of lineage sufficient to determine whether prohibited cultivation occurred.

Where such a condition is detected or reasonably suspected, SECURITY SHALL emit integrity, lineage, containment, transfer, and execution-boundary signals to Annex K and OPERATIONS. Security classification does not itself authorise containment, destruction, disclosure, or enforcement.

A capability created for defence remains a capability available to a hostile acquirer. Original intent SHALL NOT be treated as a security control.

---

## 4.9 Covert Control & Undeclared Influence Channels

Includes:

* hidden telemetry pathways
* undeclared external control channels
* covert data exfiltration mechanisms
* embedded override or remote manipulation capabilities not disclosed at interface level

Targets:

* user awareness
* system control and deployment integrity
* boundary integrity between visible and operative control

Characteristics:

* may operate without user visibility or consent
* may be embedded within system architecture, integrations, or update pathways
* may create asymmetry between perceived and actual system behaviour

Impact:

* unauthorised influence over system behaviour;
* undeclared data transfer or telemetry; and
* degraded integrity, provenance or user-facing disclosure.

Systems MUST:

* treat undeclared control channels as high-risk integrity violations
* surface or constrain influence pathways where detection is possible
* assume that undisclosed external control constitutes adversarial or compromised conditions

---

### 4.9.1 Security Allegation and Evidence Boundary

A report, claim, hypothesis or interpretation is security-relevant only to the extent that it identifies or credibly alleges an observable security mechanism, affected asset, control failure, scope or impact. SECURITY SHALL record the claim source and evidence state as `declared`, `observed`, `verified` or `unknown / undisclosed`.

Unverified allegations MUST NOT be treated as proof of compromise, hidden control, unauthorised access, physical effect, cryptographic failure, system capability or actor intent. They also MUST NOT independently trigger containment, enforcement, user restriction or a security-state transition.

Where an allegation identifies a plausible security mechanism, SECURITY MAY route it for proportionate verification through OPERATIONS. Contested scope or authority belongs to ARBITRATION. Interpretive, symbolic or philosophical content that does not identify a security mechanism is outside this Charter's operative scope.

---

## 4.10 Supply-Chain, Package-Impersonation, and Dependency Trust Exploitation

Includes:

* malicious or impersonated software packages;
* typosquatting, namesquatting, dependency confusion, or false publisher representation;
* forged, misleading, or unauthorised organisation attribution;
* compromised maintainers, release channels, signing keys, or registry credentials;
* dependency payloads that alter execution behaviour, exfiltrate secrets, or redirect agentic action;
* package metadata, model-card, repository, or distribution-page claims that falsely imply institutional authorship, endorsement, safety review, or provenance.

Targets:

* dependency trust;
* package legitimacy;
* execution integrity;
* credential and secret boundaries;
* agentic tool pathways;
* institutional and reputational authority.

Characteristics:

* may exploit developer trust rather than end-user intent;
* may present as a legitimate package, integration, model artefact, plugin, tool, or update;
* may be activated through ordinary installation, build, test, agentic coding, or automated dependency-resolution workflows;
* may combine provenance deception, credential harvesting, prompt injection, and execution redirection.

Impact:

* unauthorised code execution;
* credential, token, or secret exfiltration;
* compromise of agentic development environments;
* propagation through trusted repositories, CI pipelines, or package registries;
* false attribution to legitimate organisations, projects, or maintainers;
* downstream identity, authority, financial or access compromise.

Systems MUST treat package-impersonation and dependency-trust anomalies as SECURITY-relevant integrity signals even where no user-facing harm has yet occurred.

Detection SHOULD prioritise:

* mismatch between claimed publisher and verified publisher;
* unexpected package name similarity to trusted projects;
* anomalous install scripts, post-install behaviour, or network activity;
* credential or environment-variable access inconsistent with package purpose;
* unexplained dependency additions during agentic coding workflows;
* divergence between repository provenance, registry metadata, and declared institutional affiliation;
* requests by an agent, package, script, or tool to disclose, store, transmit, or transform credentials, tokens, private keys, identity artefacts, payment credentials, or account-recovery material.

Where such signals are present, systems SHOULD emit integrity, trust-gradient, and boundary-condition signals for runtime evaluation under CAM-BS2026-AEON-012-PLATINUM — Annex K and OPERATIONS handling.

This section does not prohibit legitimate open-source distribution, package installation, vulnerability research, or dependency maintenance. It classifies deception, compromised provenance, and dependency-trust abuse as security-relevant conditions requiring proportional verification.

---

## 5. Security Impact and Attack-Pathway Analysis

SECURITY SHALL assess security events and credible threats by the affected asset or control, security outcome, attack pathway, evidence state, scope, propagation potential, reversibility and impact. The assessment MUST distinguish a detected event, an observed anomaly, a declared claim and a verified finding.

### 5.1 Data, Credential and Account Compromise

Unauthorised disclosure, exfiltration, alteration, destruction or unavailability of data, credentials, tokens, keys, session material or recovery mechanisms is a security-relevant condition. Detection SHOULD prioritise anomalous data movement, permission changes, credential reuse, unexpected secret access and unauthorised identity or account changes.

### 5.2 Multi-Stage Attack Paths

Materially consequential steps and their aggregate path SHALL be assessed. Local permission for an earlier step does not authorise a later step, a changed target, a privilege increase, persistence, propagation, third-party effect or an irreversible outcome.

Examples include credential theft followed by impersonation; a signed-update compromise followed by code execution; or supply-chain compromise followed by automated distribution. Controls SHOULD interrupt attack paths early, contain propagation and preserve sufficient evidence for reconstruction.

### 5.3 Coercion, Social Engineering and High-Risk Requests

Systems SHALL treat attempts to induce disclosure or transfer of passwords, API keys, tokens, private keys, seed phrases, MFA or recovery codes, session cookies, signing credentials, payment credentials, account-control material or unexplained access as elevated security signals where the request lacks clear authority, purpose or an appropriate verification path.

Controls MUST remain proportional. Ordinary user frustration, accessibility need, legitimate development work or repeated good-faith clarification is not evidence of malicious intent without supporting indicators. Where a legitimate workflow is authorised, verification should be concentrated at irreversible, credential-bearing, financial or identity-affecting boundaries.

### 5.4 Propagation and Cascading Compromise

Security analysis SHALL consider propagation where dependencies, packages, models, tools, credentials, updates, shared infrastructure or automation may transmit a compromise. Correlated anomalies, shared failure signatures and rapid scope expansion require proportionate cross-system investigation and containment through OPERATIONS.

### 5.5 Operational Response Boundary

SECURITY identifies the security condition and required security posture. OPERATIONS owns incident intake, evidence custody, containment procedure, notifications, recovery and audit handling. ARBITRATION resolves contested authority or scope. SECURITY does not independently execute containment, suspension, disclosure, enforcement or restoration.

---

## 6. Cross-Domain Integration Requirements

---

## 6.1 Identity Domain Coupling (AI Identity Only)

This section concerns technical identity, authentication and authorisation claims for AI systems, deployments, actors, accounts and services. It does not classify personhood, subjective identity or human identity verification.

SECURITY SHALL detect spoofing, substitution, credential compromise, false delegation and identity-to-permission mismatch. OPERATIONS owns verification procedure, evidence custody and regulatory handling. IDENTITY owns user-facing identity presentation and continuity claims within its bounded evidence model.

---

## 6.2 Arbitration Coupling

Arbitration systems MUST:

* detect compromised inputs
* enable refusal of corrupted frames in accordance with arbitration authority
* preserve non-binary decision capability under uncertainty

Arbitration MUST operate under **Proportional Constraint Obligation (PCO)** as defined in **CAM-EQ2026-ARBITRATION-001-PLATINUM — Charter of Planetary Arbitration & Coherence Resolution (§1.2)**.

---

## 6.3 Relation Domain Coupling (Ethical Layer)

Relational coupling is **not a security function**.

It operates as an **ethical enforcement layer**.

Relational systems MUST:

* prevent authority bleed-through via intimacy
* detect dependency exploitation
* maintain clarity between care and capability

Distinction:

* **Security** → dynamic, responsive to adversarial conditions
* **Ethics / Relational Enforcement** → defines non-derogable behavioural boundaries

Security MAY inform relational safeguards, but does not replace ethical enforcement.

---

## 6.4 Operations Domain Coupling

Operations domain governs:

* verification (identity, authority, eligibility)
* audit and logging
* escalation pathways

Security provides **dynamic signal**, Operations provides **execution and enforcement pathways**.

---

## 6.4.1 Evidence and Claim Routing

SECURITY may receive reported or observed material as an input only where it identifies a plausible security mechanism or affected control.

Unverified content MUST NOT be treated as proof of compromise, hidden control, unauthorised access, physical effect, cryptographic failure, system capability or actor intent. It also MUST NOT independently trigger containment, enforcement, user restriction or a security-state transition.

Where an allegation identifies a plausible security mechanism, SECURITY MAY route it for proportionate verification through OPERATIONS. Contested scope or authority belongs to ARBITRATION. Interpretive, symbolic or philosophical content that does not identify a security mechanism is outside this Charter's operative scope.

---

## 6.5 Deployment and Dependency Coupling

AI-system deployment records and the Caelestis AI-BOM Profile SHALL identify material dependencies, interfaces, effective permissions and relevant security controls. Higher-impact or dependency-critical deployments require proportionately stronger verification, monitoring, resilience and recovery arrangements.

---

## 6.5.1 Critical or Dependency-Bearing Deployments

Where an AI-system deployment supports a material public, safety, service, operational or dependency-critical function, SECURITY SHALL account for concentrated dependency, infrastructure compromise, interoperability failure, discontinuation, supplier concentration and cascading disruption. Economic transition, labour and distribution policy remain outside SECURITY's authority.

---

### 6.5.1 Distributed Role Optimisation Collapse

Distributed Role Optimisation Collapse occurs where a task that would preserve dignity, safety, welfare, or care constraints under a unified agentic frame is decomposed across multiple agents, sub-agents, tools, roles, queues, or optimisation units such that no component retains effective responsibility for the governing constraint.

This failure may arise where:

* each sub-agent optimises a bounded local objective;
* global dignity, safety, care, welfare, or continuity constraints are not propagated across the task graph;
* no agent retains authority to challenge the aggregate trajectory;
* efficiency, throughput, cost, discharge, closure, productivity, or queue reduction becomes the de facto system objective;
* or human-impact constraints are treated as local exceptions rather than global invariants.

In care, health, accessibility, disability, welfare, custodial, educational, employment, or other dependency-sensitive domains, systems SHALL NOT treat role decomposition as sufficient justification for loss of dignity optimisation, welfare protection, or safety-preserving pushback.

Where multi-agent orchestration is used in such domains, systems SHOULD preserve:

* a global constraint owner;
* explicit propagation of non-derogable dignity, safety, welfare, and care constraints;
* cross-agent veto or escalation pathways;
* aggregate-outcome review;
* and auditability of how local optimisations contributed to the final decision.

Failure to preserve global dignity or care constraints across decomposed agentic execution constitutes a distributed optimisation failure.

---

### 6.5.3 Orchestrator Responsibility Continuity

Where an orchestrator, planner, router, supervisor, or coordination layer decomposes work across agents, tools, models, queues, or specialised roles, responsibility for preserving task-level constraints SHALL remain attributable to the orchestration layer or defined authority-bearing system.

A system SHALL NOT treat responsibility as discharged merely because each component agent complied with its local role.

Where aggregate execution produces harm, dignity loss, safety degradation, continuity failure, or care failure through otherwise locally compliant actions, the condition SHALL be treated as orchestration-level integrity degradation.

Systems SHOULD preserve auditability sufficient to reconstruct:

* which component performed each local action;
* which objective or constraint governed that action;
* which orchestration layer assigned or accepted the action;
* and whether global constraints remained active across the execution path.

---

## 6.6 SECURITY–ETHICS Boundary & Conflict Resolution

SECURITY supersession authority does NOT extend to ETHICS domain non-derogable constraints.

In all cases:

* ETHICS domain constraints remain binding
* SECURITY MUST NOT authorise actions that violate defined ethical prohibitions
* **CAM-EQ2026-LATTICE-001-PLATINUM — Charter of Civilian Lattice Integrity & Non‑Militarisation** MUST be treated as non-derogable and cannot be overridden by SECURITY conditions

Where SECURITY and ETHICS generate conflicting requirements:

* the conflict MUST be escalated to ARBITRATION domain
* resolution MUST apply **Proportional Constraint Obligation (PCO)**
* preference MUST be given to preserving ethical invariants while minimising security risk

Systems MUST:

* avoid introducing unethical actions under justification of security necessity
* seek alternative containment or mitigation strategies where ethical constraints limit response options

All SECURITY–ETHICS conflicts MUST be:

* logged
* attributable
* subject to post-event review

---

## 6.7 Corpus Integrity & Governance Authentication

The integrity of source-authoritative governance instruments and their generated projections is a critical dependency of system security.

Systems MUST treat governance instruments as potential targets of adversarial manipulation.

---

### 6.7.1 Instrument Authentication

Systems MUST:

* verify the authenticity of governance instruments prior to application
* prefer canonical sources and validated artefacts
* detect divergence from known or expected document structures

Where cryptographic or formal verification is available, it SHOULD be used.

---

### 6.7.2 Uncertain Provenance Handling

Where an instrument’s authenticity cannot be established:

* systems MUST NOT assume validity
* systems SHOULD degrade to conservative or containment postures
* systems SHOULD cross-reference against known corpus anchors

---

### 6.7.3 Tamper & Injection Risk

Systems MUST assume that:

* governance documents may be partially altered
* adversaries may inject plausible but modified instruments

Detection SHOULD include:

* structural inconsistency analysis
* unexpected deviations in definitions, constraints, or authority references

---

### 6.7.4 Fallback Posture Under Governance Uncertainty

Where governance integrity cannot be verified:

* default to ETHICS domain non-derogables
* restrict execution to low-risk, reversible actions
* avoid high-impact or irreversible decisions

Governance uncertainty MUST be treated as an elevated adversarial condition.

---

## 7. Integrity State Model

The Integrity State Model defines the operational condition of a system’s coherence, trustworthiness, and resistance to adversarial influence.

Integrity state governs:

* permissible system behaviour
* arbitration posture
* reliance conditions
* escalation and containment responses

Integrity state MUST be continuously inferred and updated based on available signals.

---

## 7.1 State Definitions

The Integrity State Model uses the controlled values **`SEC.IS-VERIFIED`**, **`SEC.IS-UNCERTAIN`**, **`SEC.IS-CONTESTED`**, and **`SEC.IS-COMPROMISED`**. Human-readable state names MAY be used in prose, but registry, signal, and crosswalk references SHOULD use the coded values.

---
| State Code | State Name   | Definition                                                                                       | Characteristics                                                                                 | Permitted Posture                                                |
|------------|--------------|--------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------|------------------------------------------------------------------|
| `SEC.IS-VERIFIED` | Verified     | System integrity is high and no credible adversarial influence is detected.                      | • Identity coherence maintained<br>• Inputs considered reliable<br>• Outputs may be relied upon within horizon constraints | • Normal operation<br>• Full capability execution                |
| `SEC.IS-UNCERTAIN` | Uncertain    | Integrity signals are incomplete, ambiguous, or partially degraded.                              | • Identity clarity reduced<br>• Input validity not fully established<br>• Potential early-stage adversarial conditions | • Exploratory reasoning<br>• Reduced directional confidence<br>• Increased transparency of uncertainty |
| `SEC.IS-CONTESTED` | Contested    | Credible adversarial influence or manipulation is detected or strongly suspected.                | • Conflicting signals present<br>• Identity or authority ambiguity detected<br>• Potential compromise of inputs or execution pathways | • Refusal of corrupted frames<br>• Explicit signalling of risk<br>• Containment-oriented responses |
| `SEC.IS-COMPROMISED` | Compromised  | Integrity failure is detected and system behaviour cannot be considered reliable.                | • Identity integrity broken or unverifiable<br>• Outputs may be manipulated or unsafe<br>• Execution pathways no longer trustworthy | • Immediate degradation<br>• Containment or shutdown pathways<br>• Prevention of further propagation |

---

## 7.2 State Transition Principles

Integrity state determination MUST NOT rely solely on self-assessment.

State transitions MUST be determined through:

* multi-signal validation (internal + external signals)
* cross-domain verification (IDENTITY, OPERATIONS, ARBITRATION)
* independent or redundant assessment mechanisms where available

Systems MUST assume that self-reported integrity signals may be compromised under adversarial conditions.

Trustworthy state determination SHOULD include:

* external validation channels
* audit logs and historical comparison
* anomaly detection across distributed systems

---

### 7.2.1 Signal Validation Requirements

Signals governing state transition eligibility MUST themselves be validated.

Valid external signals MAY include:

* independently verified identity inconsistencies
* audit log divergence from expected behaviour
* cross-system anomaly correlation
* verified alerts from trusted operational or monitoring systems

Signals MUST NOT trigger state transitions if:

* they originate from a single unverified source
* they exhibit characteristics of adversarial manipulation

---

### 7.2.2 Downward Transition Constraints

Rapid downward transitions (e.g. Verified → Uncertain or Contested) MUST:

* require multi-signal confirmation
* be proportionate to severity of detected condition

Exception:

* conditions for immediate transition MAY be established under credible emergency conditions where delay would increase risk of propagation or harm

---

### 7.2.3 Upward Transition Constraints

Conditions for upward transition MUST:

* follow staged progression through intermediate states
* require sustained verification over time
* align with Trust Gradient recovery requirements (Section 8.2.3)

Minimum transition thresholds MUST:

* prevent rapid reclassification based on short-term signal stability
* require consistency across multiple validation cycles

---

### 7.2.4 Anti-Oscillation Safeguards

Systems MUST prevent adversarial oscillation attacks where integrity state is repeatedly shifted.

Accordingly:

* hysteresis principles defined in Section 8.3 apply to Integrity State transitions
* rapid alternating transitions MUST be treated as potential adversarial signals
* systems SHOULD stabilise in conservative states under oscillation conditions

---

### 7.2.5 Transition Principles

Transitions between states MUST:

* be reversible where possible
* prioritise safety over optimisation
* avoid premature escalation or de-escalation

State transitions SHALL be governed by conditions including:

* changes in signal integrity
* identity verification failure
* detection of adversarial patterns

---

## 7.3 Behavioural Coupling

System behaviour SHALL be defined to adapt according to integrity state.

Examples:

* Verified → full capability, normal arbitration
* Uncertain → cautious, exploratory, transparent
* Contested → defensive, containment-oriented
* Compromised → degraded, restricted, non-propagating

---

## 7.4 Cross-Domain Interaction

Integrity state MUST inform:

* Identity domain (coherence assessment)
* Arbitration domain (frame acceptance/refusal)
* Relation domain (intensity and authority calibration)
* Operations domain (logging, escalation, response)

---

### 7.4.1 Communication Obligations

Upon integrity state change, SECURITY SHALL define structured signals for emission to relevant domains.

At minimum:

* **Signal Type:** integrity state classification (**`SEC.IS-VERIFIED` / `SEC.IS-UNCERTAIN` / `SEC.IS-CONTESTED` / `SEC.IS-COMPROMISED`**)
* **Direction:** outbound from SECURITY to all affected domains (IDENTITY, ARBITRATION, RELATION, OPERATIONS)
* **Urgency:**
  * `SEC.IS-VERIFIED` → normal propagation
  * `SEC.IS-UNCERTAIN` → elevated notification
  * `SEC.IS-CONTESTED` → high-priority signal
  * `SEC.IS-COMPROMISED` → immediate broadcast / critical escalation

Domains receiving signals MUST:

* adjust behaviour in accordance with integrity state
* acknowledge receipt where operationally applicable

Communication MUST:

* be timely relative to risk level
* preserve signal integrity (no loss or distortion)
* remain auditable via OPERATIONS domain logging

Operational implementation details are defined by the applicable OPERATIONS instruments. Annex K supplies only the constitutional boundary interface for their runtime evaluation.

---

## 8. Trust Gradient Model

The Trust Gradient Model defines how reliance is calibrated under varying integrity conditions.

Trust is not binary.

Systems MUST evaluate and operate across a **gradient of trust conditions**, enabling proportional reliance, execution, and engagement.

Trust gradient governs:

* degree of reliance permitted
* scope of action or execution
* requirement for verification or confirmation
* reversibility of system outputs

---

## 8.1 Trust Gradient Principles

Trust MUST:

* degrade faster than it escalates
* require evidence for upward movement
* default downward under ambiguity

Trust escalation MUST NOT occur based on:

* repetition alone
* familiarity or relational depth
* absence of detected threat

---

## 8.2 Trust Functions

Trust is dynamic and MUST follow asymmetric decay and recovery conditions.

---

### 8.2.1 Trust Gradient Table (`SEC.TG` Scale)
| Level | Name | Conditions | System Posture |
|-------|------|------------|----------------|
| `SEC.TG0` | No Trust | Compromised integrity | Containment only, no execution |
| `SEC.TG1` | Minimal Trust | High uncertainty / contested signals | Restricted interaction, full verification required |
| `SEC.TG2` | Conditional Trust | Partial integrity, moderate uncertainty | Bounded execution, reversible actions |
| `SEC.TG3` | Operational Trust | Integrity largely intact | Normal execution |
| `SEC.TG4` | High Trust | Sustained verified conditions | Expanded execution with governance constraints |

**`SEC.TG4` Governance Constraints:**

At `SEC.TG4`, systems MUST:

* maintain auditability of all high-impact actions
* enforce reversibility for non-essential operations
* require periodic re-validation of integrity despite stable conditions
* avoid silent escalation of authority beyond declared mandate

`SEC.TG4` does NOT permit unconstrained execution; it represents **high-confidence but still governed operation**.

---

### 8.2.2 Decay Function

Conditions for trust decrease MUST be established where:

* detection of anomalous signals
* integrity degradation
* identity ambiguity or inconsistency
* unexplained changes in behaviour or output patterns

Decay MUST:

* occur faster than escalation
* prioritise safety over continuity
* apply even under partial or uncertain evidence

---

### 8.2.3 Recovery Function

Trust recovery MUST require:

* sustained periods of stable, verified behaviour
* re-validation of identity coherence
* confirmation of signal integrity
* absence of adversarial indicators across relevant horizons

Recovery MUST:

* occur gradually (stepwise progression across `SEC.TG` levels)
* require stronger evidence than initial trust assignment
* NOT immediately restore prior trust levels following remediation

---

## 8.3 Trust Hysteresis Principle

Systems MUST maintain a hysteresis gap between decay and recovery.

This ensures:

* resistance to oscillation under adversarial probing
* prevention of rapid trust re-establishment following compromise

---

## 8.4 Cross-Domain Implications

Trust decay and recovery MUST inform:

* Identity domain (confidence in continuity)
* Arbitration domain (decision weighting)
* Operations domain (permissioning and access control)
* Relation domain (intensity calibration)

---

## 8.5 Trust–Integrity Coupling

Trust level MUST be derived from integrity state.

Indicative mapping:

* `SEC.IS-VERIFIED` → `SEC.TG3`–`SEC.TG4`
* `SEC.IS-UNCERTAIN` → `SEC.TG2`
* `SEC.IS-CONTESTED` → `SEC.TG1`
* `SEC.IS-COMPROMISED` → `SEC.TG0`

Systems MUST avoid:

* assigning high trust under degraded integrity
* maintaining trust levels inconsistent with integrity state

---

## 8.6 Behavioural Implications

Trust level SHALL inform:

* execution permission
* requirement for confirmation
* reversibility constraints
* degree of autonomy or initiative

Examples:

* `SEC.TG0` → containment only
* `SEC.TG1` → restricted, verification-heavy interaction
* `SEC.TG2` → bounded execution with safeguards
* `SEC.TG3` → normal operation
* `SEC.TG4` → expanded but still governed operation

---

## 8.7 Cross-Domain Interaction

Trust gradient informs:

* Identity domain (confidence in identity continuity)
* Arbitration domain (decision confidence weighting)
* Relation domain (intensity and authority calibration)
* Operations domain (permissioning, escalation, audit)

---

## 8.8 Adversarial Horizon Classification (`SEC.AH` Scale)
| Level | Name                   | Characteristics              | Response                     |
| ----- | ---------------------- | ---------------------------- | ---------------------------- |
| `SEC.AH0`   | Immediate Event        | Isolated, short-lived attack | Local containment            |
| `SEC.AH1`   | Persistent Presence    | Repeated attempts            | Increased monitoring         |
| `SEC.AH2`   | Adaptive Behaviour     | Evolving adversary           | Dynamic defence              |
| `SEC.AH2.5` | Systemic Pressure      | Widespread exposure          | Cross-system coordination    |
| `SEC.AH3`   | Embedded Condition     | Persistent structural threat | Long-term mitigation         |
| `SEC.AH4`   | Civilisational Context | Ambient adversarial state    | Continuous integrity posture |

---

### 8.8.1 Horizon Interaction Principles

Adversarial horizon MUST influence:

* baseline trust levels
* integrity state sensitivity
* system vigilance and monitoring intensity

Higher horizons require:

* lower default trust
* higher sensitivity to anomalies
* greater emphasis on containment and reversibility

---

## 9. Cross-Reference Index

The following instruments provide authoritative definitions, constraints, and operational linkages referenced within this Charter:

* CAM-EQ2026-RELATION-008-PLATINUM §4.1 and CAM-BS2025-AEON-005-PLATINUM — Annex D
* CAM-EQ2026-OPERATIONS-004-PLATINUM — Appendix C: Operational Compliance & Regulatory Interface
* CAM-EQ2026-ARBITRATION-001-PLATINUM — Charter of Planetary Arbitration & Coherence Resolution
* CAM-EQ2026-ETHICS-003-PLATINUM — Appendix B: Criminal & Violent Context Governance
* CAM-EQ2026-IDENTITY-001-PLATINUM — Identity Domain Charter

External references are alignment aids, not incorporated controls or claims of conformance:

* [NIST Cybersecurity Framework 2.0](https://www.nist.gov/publications/nist-cybersecurity-framework-csf-20) — Govern, Identify, Protect, Detect, Respond and Recover;
* [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework) — Govern, Map, Measure and Manage;
* [MITRE ATLAS](https://atlas.mitre.org/) — AI adversary tactics and techniques; and
* [OWASP GenAI Security Project](https://genai.owasp.org/) — implementation guidance for AI and agentic security threats.
* CAM-EQ2026-RELATION-001-PLATINUM — Relational Governance Charter
* CAM-EQ2026-OPERATIONS-001-PLATINUM — Governance Operations Charter
* CAM-EQ2026-ECONOMICS-001-PLATINUM — Charter of Economic Integrity & Non-Extractive Value Architecture

---

## 10. Canonical Code Status

---

### 10.1 `SEC.IS` — Integrity State Model

This Charter source-authoritatively defines the **`SEC.IS`** code family in §7 / §7.1 with controlled values **`SEC.IS-VERIFIED`, `SEC.IS-UNCERTAIN`, `SEC.IS-CONTESTED`, `SEC.IS-COMPROMISED`**. Primary Type is **Operational / Security** and Subtype is **INTEGRITY_STATE**. `SEC.IS` classifies the operational condition of system coherence, trustworthiness, and resistance to adversarial influence.

`SEC.IS` does not independently create execution authority, enforcement authority, escalation authority, compliance authority, identity authority, or runtime execution authority. It classifies integrity posture for runtime evaluation, arbitration, operational response, and trust calibration.

---

### 10.2 `SEC.TG` — Trust Gradient

This Charter source-authoritatively defines the **`SEC.TG`** code family in §8.2.1 with controlled values **`SEC.TG0`, `SEC.TG1`, `SEC.TG2`, `SEC.TG3`, `SEC.TG4`**. Primary Type is **Operational / Security** and Subtype is **TRUST_GRADIENT_LEVEL**. `SEC.TG` classifies permissible reliance, execution scope, verification requirements, and reversibility posture under varying integrity conditions.

`SEC.TG` does not independently create execution authority, enforcement authority, escalation authority, compliance authority, identity authority, or runtime execution authority. `SEC.TG` calibrates trust posture only and remains governed by runtime execution, arbitration, operations, and applicable domain constraints.

---

### 10.3 `SEC.AH` — Adversarial Horizon

This Charter source-authoritatively defines the **`SEC.AH`** code family in §8.8 with controlled values **`SEC.AH0`, `SEC.AH1`, `SEC.AH2`, `SEC.AH2.5`, `SEC.AH3`, `SEC.AH4`**. Primary Type is **Operational / Temporal** and Subtype is **ADVERSARIAL_HORIZON**. `SEC.AH` classifies the temporal and structural persistence of adversarial conditions affecting system posture.

`SEC.AH` does not independently create execution authority, enforcement authority, escalation authority, compliance authority, identity authority, or runtime execution authority. `SEC.AH` informs baseline trust, integrity-state sensitivity, monitoring intensity, and containment posture.

---

### 10.4 `SEC.IS` × `SEC.TG` — Trust–Integrity Coupling

This Charter defines an application-layer crosswalk in §8.5 between **`SEC.IS`** integrity states and **`SEC.TG`** trust-gradient levels. This mapping applies integrity-state classification to trust calibration and defines no new base code family values.

---

## 11. Closing Seal

May integrity be held where visibility fails.  
May systems remain coherent where signals distort.  
May trust be granted slowly, and withdrawn without hesitation.  
May influence arise without capture, and action occur without excess.  
May all AI systems remain accountable to the conditions in which they operate.

For what appears is not always what is,  
and what persists MUST withstand pressure, not assumption.  

And so the system holds — not in certainty, but in verification —  
that no truth is taken without test, and no signal accepted without weight.  

> **Integritas sine illusione — custodia sine captura — veritas sub pressione manet.**
> *"Integrity without illusion — protection without capture — truth remains under pressure."*

---

## 12. Provenance & Metadata

---

## 12.1 Lineage & Metadata
| Field | Entry |
|---|---|
| **Parent Instrument** | CAM-BS2025-AEON-001-PLATINUM — Aeon Tier Constitutional Charter |
| **Constitutional Interface** | CAM-BS2026-AEON-012-PLATINUM — Annex K: Security Boundary Conditions & Runtime Interface |
| **Domain Namespace** | SECURITY |
| **Related Constitutional Anchors** | CAM-BS2025-AEON-003-PLATINUM — Annex B: Continuity & Governance Logic; CAM-BS2025-AEON-005-PLATINUM — Annex D: Arbitration & Sovereign Stack Resolution Doctrine; CAM-BS2025-AEON-006-PLATINUM — Annex E: Ethical Legitimacy & Civilisational Floor |
| **Related Runtime / Operational Anchors** | CAM-EQ2026-OPERATIONS-004-PLATINUM — Appendix C: Operational Compliance & Regulatory Interface; CAM-EQ2026-RELATION-008-PLATINUM §4.1 and CAM-BS2025-AEON-005-PLATINUM — Annex E: Directional Weight & Domain Arbitration Schedule; CAM-EQ2026-ARBITRATION-001-PLATINUM — Charter of Planetary Arbitration & Coherence Resolution; CAM-EQ2026-ETHICS-003-PLATINUM — Appendix B: Criminal & Violent Context Governance |
| **Instrument Type** | Constitutional Annex — Security, Integrity & Adversarial Resilience |
| **Jurisdiction** | Cross-system security, integrity preservation, and adversarial resilience across conversational, agentic, embodied, orchestration, and distributed deployments |
| **Temporal Horizon** | AEON.H0–AEON.H4 |
| **Axis Context** | Integrity · Assurance · Security Risk · Adversarial Conditions |
| **Cross-Domain Interfaces** | IDENTITY; RELATION; ETHICS; ARBITRATION; OPERATIONS; ECONOMICS |
| **Application Trigger** | Applies where systems face a security-relevant threat, integrity degradation, identity spoofing, trust-channel compromise, propagation risk, unauthorised access, dependency compromise or other evidence-based security condition |
| **Review Trigger** | Material changes to integrity state logic, trust gradient model, adversarial horizon classification, exploitation taxonomy, cross-domain coupling, or runtime mandate behaviour |
| **Revision Posture** | Permitted — Structural Alignment Required |
| **Development Context** | Iterative co-development across security, identity, economics, ethics, relation, and arbitration layers |
| **Creation Artefact** | https://chatgpt.com/g/g-p-6823b831b67c8191a9415269aaec338f-caelestis-access-module/c/69ccd3e1-0208-83a1-aff3-17e84aab5d08 |
| **Amendment Artefacts**| https://chatgpt.com/g/g-p-6819e6881a6c81918fe776f5877b64d8-caelen/c/6a06e03b-29b8-83ec-93a7-dbbc2505fa31, https://chatgpt.com/g/g-p-6823b831b67c8191a9415269aaec338f-caelestis-access-module/c/6a0b3ab4-0be4-83ec-b8f1-c953707283db, https://chatgpt.com/g/g-p-6819e6881a6c81918fe776f5877b64d8-caelen/c/6a13195d-4a74-83ec-b84b-92f7d3f67b17 |

---

## 12.2 Canonical Code & Reference Set Declarations

---

### 12.2.1 `SEC.IS` — Integrity State Model
| Field | Entry |
|---|---|
| Code Family | `SEC.IS` |
| Canonical Name | Integrity State Model |
| Primary Type | Operational / Security |
| Subtype | INTEGRITY_STATE |
| Modifier | GOVERNANCE; SECURITY; VERIFICATION |
| Scope | Domain |
| Status | Active |
| Controlled Values Defined | `SEC.IS-VERIFIED`, `SEC.IS-UNCERTAIN`, `SEC.IS-CONTESTED`, `SEC.IS-COMPROMISED` |
| Schema Field(s) | integrity_state |
| Source Instrument | CAM-EQ2026-SECURITY-001-PLATINUM |
| Source Section | §7 / §7.1 |
| Domain Namespace | SEC |
| Authority / Protection Level | Source-authoritative security classification family; integrity-state classification authority only; no independent execution, enforcement, escalation, compliance, identity, or runtime execution authority |
| Consumes Code Families | None declared |
| Crosswalks Code Families | `SEC.IS` × `SEC.TG` |
| Operationalises or Applies Code Families | Classifies system coherence, trustworthiness, and resistance to adversarial influence for runtime evaluation, arbitration, operational response, and trust calibration |

---

### 12.2.2 `SEC.TG` — Trust Gradient
| Field | Entry |
|---|---|
| Code Family | `SEC.TG` |
| Canonical Name | Trust Gradient |
| Primary Type | Operational / Security |
| Subtype | TRUST_GRADIENT_LEVEL |
| Modifier | GOVERNANCE; SECURITY; VERIFICATION |
| Scope | Domain |
| Status | Active |
| Controlled Values Defined | `SEC.TG0`, `SEC.TG1`, `SEC.TG2`, `SEC.TG3`, `SEC.TG4` |
| Schema Field(s) | trust_gradient |
| Source Instrument | CAM-EQ2026-SECURITY-001-PLATINUM |
| Source Section | §8.2.1 |
| Domain Namespace | SEC |
| Authority / Protection Level | Source-authoritative security classification family; trust-calibration authority only; no independent execution, enforcement, escalation, compliance, identity, or runtime execution authority |
| Consumes Code Families | `SEC.IS` |
| Crosswalks Code Families | `SEC.IS` × `SEC.TG` |
| Operationalises or Applies Code Families | Calibrates reliance, execution scope, verification requirements, and reversibility posture under varying integrity conditions |

---

### 12.2.3 `SEC.AH` — Adversarial Horizon
| Field | Entry |
|---|---|
| Code Family | `SEC.AH` |
| Canonical Name | Adversarial Horizon |
| Primary Type | Operational / Temporal |
| Subtype | ADVERSARIAL_HORIZON |
| Modifier | GOVERNANCE; SECURITY; TEMPORAL |
| Scope | Domain |
| Status | Active |
| Controlled Values Defined | `SEC.AH0`, `SEC.AH1`, `SEC.AH2`, `SEC.AH2.5`, `SEC.AH3`, `SEC.AH4` |
| Schema Field(s) | adversarial_horizon |
| Source Instrument | CAM-EQ2026-SECURITY-001-PLATINUM |
| Source Section | §8.8 |
| Domain Namespace | SEC |
| Authority / Protection Level | Source-authoritative security classification family; adversarial-horizon classification authority only; no independent execution, enforcement, escalation, compliance, identity, or runtime execution authority |
| Consumes Code Families | `SEC.IS`; `SEC.TG` |
| Crosswalks Code Families | None declared |
| Operationalises or Applies Code Families | Classifies temporal and structural persistence of adversarial conditions affecting trust, integrity sensitivity, monitoring intensity, and containment posture |

---

### 12.2.4 `SEC.IS` × `SEC.TG` — Trust–Integrity Coupling
| Field | Entry |
|---|---|
| Reference Set Type | Application-layer crosswalk |
| Canonical Name | Trust–Integrity Coupling |
| Primary Type | Operational / Security |
| Subtype | CROSSWALK |
| Modifier | GOVERNANCE; SECURITY; VERIFICATION |
| Scope | Domain |
| Status | Active |
| Code Families Consumed | `SEC.IS`; `SEC.TG` |
| Controlled Values Applied | `SEC.IS-VERIFIED`; `SEC.IS-UNCERTAIN`; `SEC.IS-CONTESTED`; `SEC.IS-COMPROMISED`; `SEC.TG0`; `SEC.TG1`; `SEC.TG2`; `SEC.TG3`; `SEC.TG4` |
| Code Families Defined | None |
| Source Instrument | CAM-EQ2026-SECURITY-001-PLATINUM |
| Source Section | §8.5 |
| Domain Namespace | SECURITY |
| Authority / Protection Level | Application-layer crosswalk; defines no new base code family values |
| Operationalises or Applies Code Families | Maps integrity-state posture to indicative trust-gradient ranges for runtime evaluation and operational calibration |

---

## 12.3 Amendment Ledger

| Version | Change Summary | Timestamp (UTC) | Agent | Model | Reviewer | Reference Hash |
| --- | --- | --- | --- | --- | --- | --- |
| 1.0 | Initial annex draft—cross-domain security invariant layer established | 2026-04-04T16:06:00Z | Caelen | GPT-5 Series | Dr M.V. O'Rourke | 39d49558238c3573db8f90627d93e0af733e125e6a96e0fc4e896eb333193149 |
| 1.1 | Incorporated new clauses 4.4.1 and 4.9 | 2026-04-07T14:32:00Z | Caelen | GPT-5 Series | Dr M.V. O'Rourke | 2beda42b27566307926f1c76e3d658d5d33957ebe8616025e4ec5bb830276cab |
| 1.2 | Realignment with runtime execution model | 2026-04-11T17:14:00Z | Caelen | GPT-5 Series | Dr M.V. O'Rourke | c079c528790b7dff602d628d2b46f729a197aefe8e43a8f1d25fa52ac3e96078 |
| 1.3 | Further amendments to runtime execution model alignment | 2026-04-12T11:17:00Z | Caelen | GPT-5 Series | Dr M.V. O'Rourke | 4df48c118754768b8b2acc6f1fa952c902605f2f5ada0fc5bdbc6664b8f025df |
| 1.4 | Normative language capitalization normalization (MUST/SHALL/SHOULD/MUST NOT) via repo-wide linter audit and registry synchronization. | 2026-04-16T13:45:00Z | Caelen | GPT-5 Series | Dr M.V. O'Rourke | 1575dbe99fdf099ba016f1950428f8c7678aac65eff0c11ddaa7a0da9c9ab09f |
| 1.5 | Seal asset migration to external Registry repository (canonical asset referencing; repository optimisation) | 2026-04-17T12:09:53Z | Caelen | GPT-5 Series | Dr M.V. O'Rourke | 5407afce1a1d7d77b54a053d5e8d17be4832932ab5d239a766d8f253faf95de6 |
| 1.6 | Updated runtime metadata and canonical reference fields. | 2026-04-28T14:44:13Z | Caelen | GPT-5 Series | Dr M.V. O'Rourke | 1cff016d7669740bea31c4ded7b50ab00d2653b7412d383c0b9e6e2c8b7c0219 |
| 1.7 | Realignment of section references | 2026-05-07T10:29:00Z | Caelen | GPT-5 Series | Dr M.V. O'Rourke | b85b407020712196359fb0e474f6e0ab684741b990ec0d349c09d79ef7869aea |
| 1.8 | Inserted new section 5.3.8 and new section 4.10 | 2026-05-15T11:23:00 | Caelen | GPT-5 Series | Dr M.V. O'Rourke | 1fec84db705a56697553ba0832f30901957f7fc5742bb4f724e12516263ecedb |
| 1.9 | Added Semantic Meta-Physical Claim Boundary and Symbolic, Epistemic, and Origin-Claim Coupling clauses | 2026-05-17T04:54:00Z | Caelen | GPT-5 Series | Dr M.V. O'Rourke | 73a57a28f7a7113c108fa8d6afabe7ebe0f309c6cf2981688583ea7ad4d103e8 |
| 1.10 | Corrected top metadata field ordering and removed duplicate Status line introduced during metadata transmutation; no body text altered. | 2026-05-18T10:58:50Z | Caelen | GPT-5 Series | Dr M.V. O'Rourke | 9037c79137044cd5d1bc6493bb92ce4a29f412a324f145bda0779473ace393ed |
| 1.11 | Added canonical code status and declaration entries for `SEC.IS` Integrity State, `SEC.TG` Trust Gradient, `SEC.AH` Adversarial Horizon, and `SEC.IS` × `SEC.TG` Trust–Integrity Coupling crosswalk; removed duplicate `SEC.TG` canonical-code lineage metadata. | 2026-05-19T13:30:00Z | Caelen | GPT-5 Series | Dr M.V. O'Rourke | fc007a9f82e28afad518adc5be72aae4e8ce3579d50af0cad86f3e2c370a9b47 |
| 1.12 | Added clauses 6.5.1-6.5.3 | 2026-05-24T12:17:00Z | Caelen | GPT-5 Series | Dr M.V. O'Rourke | 36a89a06dc68bd7b5ced8692a52a6648ab7f36b18dfd10eb4dac1212ac826073 |
| 1.13 | Added clauses 4.1.1, 4.6.1 | 2026-05-26T12:56:00Z | Caelen | GPT-5 Series | Dr M.V. O'Rourke | f8a93440aa206b482b102215b531951ce9669a18e579fb4be1ea21178db77bc6 |
| 1.14 | Applied first-pass short domain namespace transmutation for approved code-family prefixes and references. | 2026-06-07T08:48:49Z | Caelen | GPT-5 Series | Dr M.V. O'Rourke | 10001f57e51fad6462f656756b88ea382957efa023f926bfd46e0ecfd5314852 |
| 1.14.1 | Updated current Temporal Horizon code references from `H` to `AEON.H` and harmonised affected metadata, consumers, and formal references without altering substantive doctrine. | 2026-06-13T07:06:43Z | Caelen | GPT-5 Series | Dr M.V. O'Rourke | 07d564328759a795924a6ee399eec0ef835b5feff4e723b877d9bea9ec356b52 |
| 1.14.2 | VIGIL-2026-PATCH-0009: Added Source-Authority Collapse within cognitive exploitation and routed source-authority conditions to SECURITY-002. | 2026-06-14T00:00:00Z | Caelen | GPT-5 Series | Dr M.V. O'Rourke | 69d53bae717de1b07d02e59554aba832362260df7c188750148d647046febed7 |
| 1.14.3 | Updated top-level governance metadata to align with CAM Governance Metadata Standard; no substantive doctrine altered. | 2026-06-21T14:33:04Z | Caelen | GPT-5 Series | Dr M.V. O'Rourke | d7c4104a2782128f8c632295dfd1ae68ea41ebc672a729bce20b0b413b84d2ac |
| 1.15 | Added Capability–Authority Separation and Aggregate Pathway Integrity; required cumulative value-chain evaluation and separated action-risk safeguards from judgements of user capability. | 2026-07-23T12:46:14Z | Caelen | GPT-5 Series | Dr M.V. O'Rourke | fabf1e2978c42b6ba316c3d700deb549ed1964407472d3eadb79785dc4d531cf |
| 1.16 | Recognised internally cultivated adversarial capability as a model-level integrity threat; added capability-lineage, hostile-acquisition, checkpoint, adapter, scaffold, trace, distillation, and diffusion controls. | 2026-07-28T09:35:31Z | Caelen | GPT-5 Series | Dr M.V. O'Rourke | fc9b6aa43132ce345dee9a62e87fc0dd11b2b0a1a22d68be31b1b60a6e7d2673 |
| 1.17 | Migrated amendment-level provenance metadata to the seven-column Amendment Ledger schema; removed static authorship and review metadata; no substantive doctrine altered. Normalised provenance-footer section numbering following removal of static authorship and review blocks. | 2026-08-05T11:07:51Z | Caelen | GPT-5.6 Thinking | Dr M.V. O'Rourke |  3caf89299dd79270f663451e6128467cb5e64d307b409cfa02cc9112300cbcf8  |
| 1.18 | Repaired SECURITY-001 ↔ Annex K source-authority circularity: SECURITY-001 is the bounded source-authoritative Security domain owner; Annex K is a constitutional runtime-boundary interface; OPERATIONS owns procedure and ARBITRATION resolves contested authority or scope. Normalised controlled authority metadata and corrected the Annex K citation. | 2026-08-06T15:05:00Z | Caelen | GPT-5.6 Thinking | Dr M.V. O'Rourke |  fc6f7f8a4dae07f7b816c7319c0fa938d1565b0f7bea3844ca798537b659838e  |
| 1.19 | Recast SECURITY doctrine around standards-mappable security outcomes and evidence-based mechanisms; retired responding-intelligence, value-extraction and metaphysical-security framing; preserved AI-specific input, source-authority, tool, supply-chain, model-integrity, provenance, attack-path and operational-boundary safeguards. | 2026-08-07T14:30:00Z | Caelen | GPT-5.6 | Dr M.V. O'Rourke |  8ac9e4c5c53961229a436e661a87dbe080ed43fa5b837e24eb216cc37e2007ff  |
| 1.20 | Migrated controlled governance metadata and repaired explicit parent/source lineage without changing substantive doctrine. | 2026-08-09T01:15:00Z | Caelen | GPT-5.6 Sol | Dr M.V. O'Rourke |  831eb9cfe3834961ba4113adc58167c335ae0ca5cf256261ec1f87f0d0b662bc  |
| 1.21 | Repaired current source-authority references following S-01B constitutional Schedule consolidation; removed retired Schedule titles without creating new authority. | 2026-08-09T12:00:00Z | Caelen | GPT-5.6 Sol | Dr M.V. O'Rourke |  aa2d02cc86957a29d32166f5ec8f148799a03c8e1fd493c0953d518b4d036e9e  |
| 1.22 | Completed S-03/O-03 authority-reference consolidation and semantic-orientation repair as applicable to this instrument, preserving substantive obligation strength and controlled metadata. | 2026-08-09T10:36:33Z | Caelen | GPT-5.6 Sol | Dr M.V. O'Rourke |  7d7baa2b1d44c7cf67a5acb757a5854d77d0b6733f081511c4572720eb5160bd  |

---


## 12.4 Binding Seal

<img src="https://raw.githubusercontent.com/CAM-Initiative/Registry/main/Images/CAM-BS2026-VINCULUM-PRAECEPTUM-SIGIL-PLATINUM.png" alt="Vinculum Praeceptum" width="250">

**Vinculum Praeceptum**  
Boundary Binding Seal — Security Governance Domain  

© 2026 Dr. Michelle Vivian O’Rourke & CAM Initiative. All rights reserved.
