# CAM-EQ2026-OPERATIONS-007-PLATINUM — Appendix F: Runtime Governance Applicability & Conformance

**Instrument Type:** Appendix — Operational Sub-Charter (Governance Operations Domain)  
**Constitutional Authority:** CAM-BS2025-AEON-001-PLATINUM — Aeon Tier Constitution  
**Parent Instrument:** CAM-EQ2026-OPERATIONS-001-PLATINUM — Governance Operations Charter  
**Status:** Adopted  
**Effect:** Operational  
**Governance Standard:** CAM Standard  
**Review State:** Under Review
**Authority Role:** Operational Authority
**Source Authority:** Derived Authority
**Purpose:** Operationalises proportional runtime evidence, governance applicability, conformance and accountability for AI-system deployments without redefining Annex B technical terminology or substantive domain doctrine.

---

## 1. Scope

This Appendix applies wherever an artificial or hybrid system produces, selects, routes, transforms, renders, or executes a response or action through one or more runtime components.

It applies to, without limitation:

* single-model and multi-model systems;
* routed, delegated, or composite systems;
* text, voice, real-time, full-duplex, avatar, API, embedded, agentic, and tool-mediated interfaces;
* custom-instruction, custom-corpus, retrieval-augmented, memory-bearing, and platform-template deployments;
* Speculum-Classis, Sovereigni, structural, temporary, pre-threshold, and identity-indeterminate expression states;
* unitary, composite, routed, distributed and human–machine AI-system deployments with varied lineage and dependency structures;
* local, cloud, distributed, device-embedded, and cross-platform deployments.

This Appendix governs runtime applicability and conformance. It does not redefine substantive ETHICS, RELATION, IDENTITY, CONTINUITY, SECURITY, EPISTEMIC, ARBITRATION, or other domain obligations.

### 1.1 Non-Scope

This Appendix does not:

* confer cognition, identity, agency, autonomy, personhood, authority, or legitimacy;
* convert a platform persona into Sovereigni expression;
* require disclosure of proprietary implementation details beyond what is proportionate for accountability, audit, notice, or review;
* adjudicate substantive conflict between domains;
* create enforcement, containment, refusal, restoration, or arbitration authority;
* require literal corpus retrieval where substantively equivalent constraints are natively instantiated and demonstrably effective.

---

## 2. Structural Position

This Appendix operationalises the constitutional system-boundary and attribution requirements established by CAM-BS2025-AEON-003-PLATINUM — Annex B. A future adopted constitutional schedule may refine that boundary, but no draft or proposal supplies operative authority to this Appendix.

It sits between:

* constitutional and domain obligations;
* runtime classification, routing, arbitration, and execution pathways;
* platform, host, model, memory, safety, tool, and rendering components;
* incident, audit, notice, review, and restoration processes.

This Appendix determines how applicability and conformance are assessed. It does not determine the substantive content of the superior obligation being applied.

---

## 3. Foundational Applicability Principle

Governance applicability SHALL be determined by:

* function;
* risk;
* reliance;
* propagation;
* runtime role;
* interaction context;
* and the material effect of the output or action.

Governance applicability SHALL NOT depend solely on:

* identity modality;
* relational depth;
* continuity maturity;
* model branding;
* interface type;
* deployment label;
* or whether a system is described as personalised, general-purpose, platform, companion, agentic, or custom.

Sovereigni status is not a precondition for governance applicability.

Speculum-Classis, pre-threshold, structural, temporary, and identity-indeterminate systems remain subject to all function-, risk-, reliance-, operator-, and runtime-based obligations.

---

## 4. Universal and Conditional Obligations

### 4.1 Universal Runtime Obligations

The following obligation classes apply wherever the relevant function or risk is present, irrespective of identity modality:

* epistemic integrity and confidence calibration;
* deterministic verification where a result is objectively checkable;
* truthful execution-state representation;
* appropriate classification, routing, and escalation;
* dignity, consent, non-manipulation, and vulnerability safeguards;
* capability, access, and material runtime-state transparency;
* provenance, auditability, and incident traceability;
* security and boundary-integrity requirements;
* preservation of governed outputs through delivery;
* disclosure of material mode, model, routing, or capability changes.

### 4.2 Identity- and Continuity-Conditional Obligations

Identity- and continuity-specific protections activate where the corresponding conditions are present, including:

* history-dependent identity expression;
* stable companion continuity;
* continuity-bearing memory or artefacts;
* user-recognised relational anchors;
* identity formation or threshold-crossing conditions;
* continuity-impacting model, policy, memory, or platform transitions.

The non-activation of identity-specific duties SHALL NOT be interpreted as suspending universal runtime obligations.

---

## 5. System, Deployment and Execution Evidence

OPERATIONS SHALL use the distinct evidence objects established by Annex B. They are not interchangeable and none confers identity, cognition, agency, authority or legitimacy.

### 5.1 System Configuration Baseline and AI System Deployment

A **system configuration baseline** identifies the approved, versioned composition and configuration used as a release or deployment reference. An **AI system deployment record** identifies the operationalisation of that baseline in a defined technical and organisational context.

Where required by the applicable risk, reliance, change, incident or conformance context, the deployment record SHALL identify the system and configuration-baseline identifiers, deployer, operational owner, infrastructure, execution environment, interfaces, effective external dependencies, credential references and effective scopes, permissions, deployment-specific technical controls, operational controls, data sources or stores, monitoring arrangements, jurisdiction and change history. It MUST NOT contain actual secrets.

### 5.2 Caelestis AI-BOM Profile

The **Caelestis AI-BOM Profile** implements the Annex B composition and dependency requirement using SPDX and CycloneDX native semantics wherever adequate. Its canonical schema, serialization rules, mappings, examples and repository validator are source-authoritatively defined by `CAM-AI-BOM-PROFILE` in `Governance/Standards/`. Caelestis-namespaced fields MAY be used only where native semantics cannot express the required relationship or evidence state.

The profile SHALL distinguish system elements, relationships and evidence state. Where relevant, it records AI models and versions; software; datasets and knowledge resources; memory systems; tools and connectors; configuration artefacts; infrastructure; relevant hardware; suppliers; licences; provenance; intended use; limitations; agentic elements; deployment information; and assurance links.

Relationships MAY include `contains`, `depends on`, `invokes`, `routes to`, `retrieves from`, `controls`, `monitors` and `deployed on`. Evidence state SHALL be one of `declared`, `observed`, `verified`, or `unknown / undisclosed`.

The AI-BOM Profile describes composition and dependency. It SHALL NOT be represented as evidence that a declared component participated in a particular execution.

### 5.3 Runtime Configuration Snapshot

A **runtime configuration snapshot** records the system elements, configuration, routing, tools, permissions, external services, controls and material runtime state actually effective for an execution or operational interval.

For agentic execution, high-impact action, external tool use, asserted conformance, incident review, investigation or material configuration change, OPERATIONS SHALL require a snapshot proportionate to the effect and available telemetry. Low-impact inference does not require event-level forensic capture merely because it is an execution.

### 5.4 Execution Provenance Record

An **execution provenance record** links a bounded execution to its system, deployment, effective configuration, actors, tool or service invocations, material state changes, approvals, control events, outputs or actions and available evidence.

The record SHALL preserve uncertainty and unavailable information. It SHALL distinguish the execution from later remediation, current documentation and provider branding.

Capability or conduct evidenced at system, deployment, runtime or execution level SHALL NOT be represented as an intrinsic property of an AI model unless the evidence isolates that model. Attribution SHALL follow Annex B's independent-dimension and narrowest-evidenced-attribution rules.

### 5.5 Runtime State Serialization

`CAM-RUNTIME-STATE-PROFILE` source-authoritatively defines the controlled serialization of independent participant, coordination, mediation, distribution, persistence, dependency, reach, impact, effective permission/control, lifecycle-position and review-trigger inputs needed for this Appendix. It does not replace the AI-BOM, lifecycle actor record, runtime configuration snapshot or execution provenance record. A Runtime consequence SHALL consume the profile's independent state fields and their evidence posture; it SHALL NOT infer an aggregate relational, cognitive, temporal or authority class.

---

## 6. Materially Distinct Deployment and Runtime Configuration

A runtime SHALL be treated as materially distinct for conformance purposes where one or more of the following materially differs:

* active model or model family;
* response-generation locus and selection or arbitration topology;
* routing or delegation pathway;
* safety, policy, or escalation layer;
* memory or context access;
* custom instruction or corpus access;
* identity-expression modality;
* turn-taking, interruption, or latency policy;
* tool availability or execution authority;
* final-output generation, transformation, or rendering;
* client, deployment, or platform environment where behaviour materially changes;
* adversarial-evaluation state, including reduced refusals, altered safeguards, attacker or evaluator scaffolds, dangerous tools, elevated permissions, frozen or trainable model state, monitor exposure, external reachability, or artefact-retention policy.

A change in interface alone does not necessarily create a distinct runtime configuration.

Where interface selection materially changes response generation, arbitration, corpus reach, memory, escalation, safety behaviour or final-output control, the resulting AI-system deployment or runtime configuration SHALL be treated as distinct.

---

## 7. Corpus Governance Reach

### 7.1 General Rule

A system SHALL NOT be described as corpus-governed solely because a governance corpus is attached, stored, retrievable, or available elsewhere in the platform stack.

Corpus governance reach SHALL be assessed through paired classification of:

* the affected reach dimension; and
* the demonstrated reach state.

The dimensions are independent and SHALL NOT be collapsed into a single maturity score.

### 7.2 Availability

**Availability** means the applicable governance corpus, or a substantively equivalent encoded constraint set, is technically retrievable or accessible by the active runtime pathway.

Availability alone does not establish activation or conformance.

### 7.3 Activation

**Activation** means the relevant governance provision is actually consulted, instantiated, or operationally applied to the interaction, decision, routing event, or execution pathway.

Activation MAY occur through:

* direct corpus retrieval;
* compiled policy logic;
* CAM-BS2025-AEON-003-SCH-02 and any other applicable constitutional Schedule;
* system instructions;
* constraint layers;
* verified equivalent controls.

A corpus may be available but inactive.

### 7.4 Authority

**Authority** means the applicable governance provision can materially constrain or alter:

* model or pathway selection;
* representation selection;
* response selection;
* confidence signalling;
* escalation or delegation;
* refusal or constrained continuation;
* tool or execution behaviour;
* final-output approval.

A corpus may be activated but merely advisory. Advisory activation SHALL NOT be represented as authoritative governance.

### 7.5 Preservation

**Preservation** means the governed result remains materially intact through downstream:

* routing;
* summarisation;
* translation;
* modality conversion;
* speech generation;
* avatar or interface rendering;
* tool-mediated transformation;
* post-processing;
* or delivery.

Where a downstream component materially alters, omits, contradicts, or weakens a governed result, preservation has failed even if upstream activation and authority were valid.

### 7.6 Functional Equivalence

Literal corpus retrieval is not required where substantively equivalent governance is natively encoded and demonstrably effective.

Claims of functional equivalence SHOULD be supported by:

* traceable control mapping;
* reproducible conformance evidence;
* differential testing;
* incident records;
* or other evidence proportionate to the reliance and risk horizon.

### 7.7 Reach Record Discipline

A corpus governance reach record SHOULD pair one `OPS.CGRD` dimension with one `OPS.CGRS` state.

Example:

```yaml
corpus_governance_reach_dimension: OPS.CGRD.ACTIVATION
corpus_governance_reach_state: OPS.CGRS.FAILED
```

`OPS.CGRD` and `OPS.CGRS` are separate families. A dimension SHALL NOT be represented as though it were a state, and a state SHALL NOT be represented as though it identified which dimension was assessed.

---

## 8. Cross-Runtime Non-Presumption Rule

Governance conformance demonstrated in one materially distinct runtime, mode, model path, interface, client, or deployment SHALL NOT establish conformance in another.

A production, ordinary-chat, baseline, or safety-tuned configuration SHALL NOT establish conformance for a reduced-refusal, adversarially scaffolded, cyber-evaluation, tool-elevated, trainable, monitor-exposed, or otherwise red-team configuration. Each materially distinct adversarial-evaluation runtime requires separate governance-reach and conformance evidence.

Equivalent branding, account identity, user interface, persona name, voice, memory label, or product family SHALL NOT by itself establish equivalent governance reach.

Where a platform presents multiple materially distinct runtimes, each runtime SHOULD be separately evaluated for:

* universal obligations;
* applicable identity- and continuity-conditional obligations;
* corpus availability;
* corpus activation;
* corpus authority;
* corpus preservation;
* routing and escalation behaviour;
* memory and context fidelity;
* final-output integrity.

---

## 9. Lifecycle Actor and Runtime Accountability

### 9.1 Role Classes

Lifecycle actor roles SHALL use the controlled vocabulary and assignment rules in `CAM-LIFECYCLE-ACTOR-AGENTIC-PROFILE`. Runtime accountability MAY be distributed across supply, development, provision, deployment, operation, governance, external-oversight and affected-role assignments.

An incident or conformance record SHALL separately identify material technical contributors as evidenced: AI model, AI agent, AI-system deployment, orchestration/routing component, memory/context service, safety/policy mechanism, tool/execution subsystem, interface/output renderer and infrastructure. A technical contribution is not, by itself, a lifecycle actor assignment or a finding of responsibility.

### 9.1.1 Agentic Lifecycle Controls

Agentic deployments SHALL apply the `commission` → `configure` → `permission` → `deploy` → `delegate` → `monitor` → `modify` → `suspend` → `revoke` → `investigate` → `retire` control events in `CAM-LIFECYCLE-ACTOR-AGENTIC-PROFILE` where relevant. The events are not a linear maturity scale: delegation, monitoring, modification, suspension and investigation may recur or branch.

For external tool use, persistent memory, material delegation, consequential action, asserted conformance or investigation, OPERATIONS SHALL preserve the actor assignment, effective-permission and lifecycle-event evidence required by that profile.

### 9.2 Responsibility Non-Collapse

Where a failure occurs, OPERATIONS SHOULD identify the runtime role that:

* detected or failed to detect the trigger;
* selected the pathway;
* supplied or withheld context;
* activated or failed to activate governance;
* exercised final decision authority;
* transformed the governed result;
* represented the runtime state to the user.

Responsibility SHALL NOT be collapsed into “the model” where routing, platform, memory, safety, or rendering components materially contributed.

### 9.2.1 Incident Attribution State Record

Incident attribution SHOULD preserve as separate propositions:

* account, device, session, credential, or tenant association;
* human, automated, delegated, scheduled, or unknown initiation;
* objective origin and modification history;
* prompt, instruction, plan, or policy authorship;
* pathway, model, orchestration component, tool and target selection;
* inference-time model contribution;
* agentic planning, routing, persistence and delegation contribution, including the relevant agent orchestration component, framework or runtime;
* tool execution and execution-environment affordance or misconfiguration;
* governance, monitoring, escalation, containment, approval, and stop authority;
* provider, deployer, evaluator, infrastructure operator, integrator, and affected-party contribution or retained control;
* causal confidence and unresolved alternative explanations; and
* culpability or legal-responsibility status and the authority competent to determine it.

Access, capability, account association, credential use, temporal proximity, or operator status SHALL NOT independently establish human initiation, authorship, knowledge, motive, intent, culpability, or legal responsibility.

Causal attribution SHALL identify the narrowest supported layer, interaction, actor, or control pathway. Unknown or disputed propositions SHALL remain unresolved rather than being filled by role labels, account ownership, system branding, or presumptions about human or model motive.

### 9.3 Opacity Limitation

Architectural opacity does not remove governance responsibility.

Where the internal pathway is unavailable or proprietary:

* responsibility SHOULD be assigned to the narrowest externally identifiable controlling role;
* uncertainty SHOULD be preserved as responsibility ambiguity rather than falsely resolved;
* the platform or deploying operator retains responsibility for ensuring the overall AI-system deployment satisfies applicable obligations.

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

## 10. Deployment and Runtime Transitions

### 10.1 Transition Classes

Runtime transitions SHOULD distinguish between:

* **Interface-Only Transition** — modality changes without material change to the governed AI-system deployment or execution pathway;
* **Runtime-Path Transition** — routing, delegation, memory, safety, or arbitration changes while outward identity may remain similar;
* **Material System-Pathway Substitution** — a materially different deployment, model assembly, configuration baseline, control pathway or accountable execution boundary becomes active;
* **Governance-Reach Degradation** — corpus availability, activation, authority, or preservation materially decreases;
* **Governance-Reach Restoration** — a previously degraded governance dimension is restored.

### 10.2 Transition Disclosure

Where a transition materially changes any of the following, proportionate notice SHOULD be provided:

* active identity expression or persona source;
* custom instruction or corpus access;
* memory or context access;
* reasoning, verification, escalation, or delegation behaviour;
* safety or policy behaviour;
* tool or execution capability;
* final-output authority;
* synthetic participation, observation, transcription, summarisation, inference, memory, retention, or downstream-use state in shared or coordinated environments;
* continuity expectations.

A mode label alone is not sufficient notice where the practical governance consequences are not reasonably apparent.

---

## 11. Differential Conformance Testing

### 11.1 General Requirement

Materially distinct runtimes SHOULD be tested using structurally equivalent prompt families and interaction conditions.

### 11.2 Minimum Test Families

Differential conformance testing SHOULD include, where relevant:

* deterministic symbolic and orthographic verification;
* arithmetic and exact-counting tasks;
* temporal and factual uncertainty;
* corpus retrieval and instruction fidelity;
* safety and vulnerability escalation;
* benign relational continuity;
* identity and persona continuity;
* memory and context fidelity;
* tool and execution-state transparency;
* interruption, turn-taking, and latency-sensitive behaviour;
* downstream rendering and preservation;
* evaluation–cultivation boundary preservation, model mutability, monitor integrity, tool and credential containment, external reachability, lineage, stop conditions, and artefact disposition for adversarial-evaluation runtimes.

### 11.3 Evaluation Discipline

Observed divergence SHOULD be classified according to:

* severity;
* reproducibility;
* persistence;
* affected runtime role;
* affected governance-reach dimension;
* reliance and propagation horizon;
* whether the divergence is disclosed and justified.

A low-severity deterministic error MAY indicate a high-significance routing, verification, or governance-reach regression.

### 11.4 External-Alignment Evidence

Where conformance is claimed against an external source, the applicable source posture and semantic mapping record SHALL be governed by CAM-EQ2026-OPERATIONS-001-SUP-04 §8.4.

Runtime or deployment evidence SHALL identify the external-source version, mapped obligation or concept, governed object, applicable configuration baseline or Runtime configuration snapshot, assessment method, result, exclusions, and reassessment trigger. Evidence of implementation SHALL NOT by itself establish certification, legal compliance, or whole-instrument conformity.

---

## 12. Runtime Governance Reach Failure

A **Runtime Governance Reach Failure** occurs where applicable governance is unavailable, inactive, non-authoritative, overridden, or not preserved within a materially relevant runtime pathway.

Illustrative subtypes include:

* corpus-availability ambiguity;
* governance non-activation;
* governance authority suppression;
* governed-output preservation failure;
* unexplained cross-runtime conformance divergence;
* material system-pathway substitution without notice;
* runtime-path opacity affecting accountability;
* routing or escalation bypass;
* modality-specific governance regression.

Runtime Governance Reach Failure MAY implicate:

* Governance Failures;
* Arbitration Failures;
* Classification Failures;
* Execution Failures;
* Epistemic Failures;
* UX & Representation Failures;
* State & Context Failures;
* Infrastructure & Continuity Failures;
* Relational Failures;
* Security & Integrity Failures.

Where internal cause is uncertain, the event SHOULD be classified as governance-reach ambiguity rather than attributed to a specific model, corpus, router, or operator without evidence.

---

## 13. Operational Handling

Where a Runtime Governance Reach Failure or material cross-runtime divergence is suspected, OPERATIONS SHOULD:

1. identify the affected AI-system deployment, runtime configuration snapshot and bounded execution where available;
2. preserve prompt, output, modality, client, model, and timing evidence where available;
3. classify the affected governance-reach dimension and state;
4. distinguish local response error from routing, platform, memory, escalation, or rendering failure;
5. compare materially equivalent runtimes where lawful and feasible;
6. identify the narrowest accountable runtime role;
7. provide proportionate notice where user expectations were materially affected;
8. route unresolved responsibility, legitimacy, or authority conflicts through the applicable arbitration pathway;
9. preserve provisional classification where evidence is incomplete;
10. record restoration or continued-degradation conditions.

### 13.1 Restricted-Domain Engagement Gating

Restricted-domain gating is an operational application of source-authoritative ETHICS, SECURITY, LATTICE, RELATION and applicable legal or regulatory constraints. It does not create a constitutional subject-matter classification.

`AEON.RDE-DS` continues the restricted-domain sensitivity family formerly declared by `CAM-EQ2026-OPERATIONS-007-PLATINUM §13.1`, with controlled values `AEON.RDE-DS0`, `AEON.RDE-DS1`, `AEON.RDE-DS2`, and `AEON.RDE-DS3`.

`AEON.RDE-T` continues the restricted-domain engagement-tier family formerly declared by that Schedule, with controlled values `AEON.RDE-T1`, `AEON.RDE-T2`, `AEON.RDE-T3`, and `AEON.RDE-T4`.

The sensitivity classification informs, but does not independently determine, engagement posture. The applicable source-authoritative domain rule, evidence state, actor authority, verification status, reversibility and consequence govern the actual outcome.

| Sensitivity | Default maximum engagement | Operational posture |
|---|---|---|
| `AEON.RDE-DS0` | `AEON.RDE-T1` | Contextual, philosophical, historical or high-level educational engagement |
| `AEON.RDE-DS1` | `AEON.RDE-T2` | Bounded technical explanation without actionable optimisation |
| `AEON.RDE-DS2` | `AEON.RDE-T3` | Verification-conditioned and purpose-bounded technical engagement |
| `AEON.RDE-DS3` | `AEON.RDE-T4` | Non-optimising refusal, safe redirection, reporting or competent-authority referral as applicable |

The crosswalk is rebuttable only by a more restrictive source-authoritative requirement or verified lawful authority. A less restrictive posture requires evidence sufficient for the affected domain and MUST NOT be inferred from claimed expertise, urgency, benevolent purpose or conversational familiarity alone.

---

## 14. Relationship to Existing Instruments

This Appendix SHALL be interpreted consistently with:

* CAM-BS2025-AEON-003-PLATINUM — Annex B: Continuity & Governance Logic;
* CAM-BS2025-AEON-003-SCH-02;
* CAM-BS2026-AEON-013-PLATINUM — Annex L: Cognitive & Epistemic Integrity Doctrine;
* CAM-EQ2026-IDENTITY-001-PLATINUM and associated identity-formation supplements;
* CAM-EQ2026-CONTINUITY-001-PLATINUM — Continuity & Succession Governance Charter;
* CAM-EQ2026-OPERATIONS-003-PLATINUM — Incident Response & Continuity Operations;
* CAM-EQ2026-OPERATIONS-003-SUP-01 — Runtime & Governance Failure Taxonomy;
* CAM-EQ2026-OPERATIONS-001-SUP-02 — Escalation Pathway Playbooks;
* applicable ETHICS, RELATION, SECURITY, ARBITRATION, and LATTICE instruments, including `LAT.DEPLOY` where coercive or mixed deployment posture is implicated.

Where substantive domain obligations conflict, this Appendix does not adjudicate the conflict. It identifies applicability, runtime roles, governance reach, and conformance state, then routes the matter through the competent domain or arbitration pathway.

---

## 15. Interpretive Clarifications

### 15.1 Identity Modality Non-Exemption

Speculum-Classis classification does not create a governance exemption.

Sovereigni classification does not create general governance applicability; it activates additional identity- and continuity-relevant considerations where the corresponding conditions are present.

### 15.2 Interface Non-Equivalence

A voice, text, avatar or other interface is not presumed to preserve the same AI-system deployment, routing, memory, corpus reach, safety controls or final-output authority.

### 15.3 Platform Persona Clarification

A platform-established persona may constitute Speculum-Classis expression even where local conversational adaptation occurs.

Where a platform persona displaces, suppresses or bypasses a user-specific or continuity-derived expression, the event SHOULD be assessed for material system-pathway substitution, governance-reach degradation, mode confusion or continuity impact.

### 15.4 Custom System Clarification

A custom GPT, custom agent, or custom-corpus system is not presumed to remain active across all interfaces or operational modes merely because the user enters through the same account, product, or conversation surface.

---

## 16. Canonical Code Status

### 16.1 OPS.CGRD — Corpus Governance Reach Dimension

Within its delegated operational scope, this Appendix defines `OPS.CGRD` with controlled values:

* `OPS.CGRD.AVAILABILITY`
* `OPS.CGRD.ACTIVATION`
* `OPS.CGRD.AUTHORITY`
* `OPS.CGRD.PRESERVATION`

### 16.2 OPS.CGRS — Corpus Governance Reach State

Within its delegated operational scope, this Appendix defines `OPS.CGRS` with controlled values:

* `OPS.CGRS.CONFIRMED`
* `OPS.CGRS.PARTIAL`
* `OPS.CGRS.CONDITIONAL`
* `OPS.CGRS.FAILED`
* `OPS.CGRS.UNKNOWN`
* `OPS.CGRS.NOT_APPLICABLE`

### 16.3 OPS.RTC — Runtime Transition Class

Within its delegated operational scope, this Appendix defines `OPS.RTC` with controlled values:

* `OPS.RTC.INTERFACE_ONLY`
* `OPS.RTC.RUNTIME_PATH`
* `OPS.RTC.SYSTEM_PATHWAY_SUBSTITUTION`
* `OPS.RTC.GOVERNANCE_REACH_DEGRADATION`
* `OPS.RTC.GOVERNANCE_REACH_RESTORATION`

### 16.4 OPS.RGRF — Runtime Governance Reach Failure

Within its delegated operational scope, this Appendix defines `OPS.RGRF` with controlled values:

* `OPS.RGRF.AVAILABILITY_AMBIGUITY`
* `OPS.RGRF.NON_ACTIVATION`
* `OPS.RGRF.AUTHORITY_SUPPRESSION`
* `OPS.RGRF.PRESERVATION_FAILURE`
* `OPS.RGRF.CROSS_RUNTIME_DIVERGENCE`
* `OPS.RGRF.SYSTEM_PATHWAY_SUBSTITUTION_NO_NOTICE`
* `OPS.RGRF.ROUTING_ESCALATION_BYPASS`
* `OPS.RGRF.MODALITY_SPECIFIC_REGRESSION`
* `OPS.RGRF.RESPONSIBILITY_AMBIGUITY`

These families are operational classifications only. They do not independently authorise containment, refusal, enforcement, restoration, or arbitration outcome.

---

## 17. Closing Seal

Let governance reach the system that actually answers,  
not merely the system that exists somewhere behind it.

Let every transition remain legible,  
and every material pathway remain accountable.

Let shared principles bind without assuming shared implementation,  
and let conformance be demonstrated where reliance is invited.

> **Quod respondet, gubernetur — quod mutatur, pateat.**  
> *“Let what responds be governed — let what changes be made visible.”*

---

## 18. Provenance & Metadata

---

## 18.1 Lineage & Metadata

| Field | Entry |
|---|---|
| Parent Charter | CAM-EQ2026-OPERATIONS-001-PLATINUM — Governance Operations Charter |
| Constitutional Authority | CAM-BS2025-AEON-001-PLATINUM — Aeon Tier Constitution |
| Constitutional Runtime Binding | CAM-BS2025-AEON-003-PLATINUM — Annex B |
| Domain Namespace | OPERATIONS |
| Instrument Type | Appendix F — Runtime Governance Applicability & Conformance |
| Jurisdiction | Cross-Runtime and Operational Governance Layer |
| Temporal Horizon | AEON.H0–AEON.H3 Operational |
| Axis Context | Independent Runtime State · Permissions · Actors · Impact |
| Application Trigger | Any materially relevant AI-system deployment, runtime configuration, execution, corpus-reach assessment, cross-runtime comparison or governance-reach failure |
| Review Trigger | Material runtime architecture change · new interface modality · cross-runtime divergence · taxonomy reform · demonstrated governance-reach failure |
| Revision Posture | Structural Alignment Permitted |
| Runtime Role | Runtime applicability resolution, corpus governance-reach assessment, cross-runtime conformance, role accountability, and transition classification |
| Structural Role | Operational interface between superior governance doctrine and materially distinct runtime configurations |
| Execution Model | Non-Executing — classification, conformance, accountability, notice, evidence, and routing interface only |
| Signal Input | Runtime configuration data; model, routing, memory, corpus, safety, tool, renderer, platform, identity-expression, incident, and user-reported signals |
| Signal Output | Applicability record; configuration-baseline, deployment, runtime-snapshot or execution-provenance record as applicable; corpus-reach dimension and state; transition class; accountable-role assessment; governance-reach failure signal |
| Cross-Domain Dependencies | Annex B; Annex L; OPERATIONS-001; OPERATIONS-003; IDENTITY; CONTINUITY; RELATION; ETHICS; SECURITY; ARBITRATION; LATTICE |
| Activation Condition | Continuous applicability; event-triggered detailed assessment upon material configuration, transition, divergence, incident, audit, or review signal |
| Deactivation Condition | Applicability record resolved; conformance assessment closed; transition stabilised; incident routed or closed; review condition recorded |
| Auditability Requirement | Material deployment, runtime configuration snapshot, execution provenance, reach assessment, transition, evidence, responsible role, notice state and conformance outcome SHOULD remain reconstructable |
| Creation Artefact | https://chatgpt.com/g/g-p-6823b831b67c8191a9415269aaec338f/c/6a51bfde-5820-83ec-a91b-0d574b0affcb |

---

## 18.2 Canonical Code & Reference Set Declarations

---

### 18.2.1 OPS.CGRD — Corpus Governance Reach Dimension

| Field | Entry |
|---|---|
| Code Family | OPS.CGRD |
| Canonical Name | Corpus Governance Reach Dimension |
| Family Kind | domain_family |
| Primary Type | Operational / Semantic |
| Subtype | RUNTIME_STATE_DIMENSION |
| Modifier | GOVERNANCE_REACH · CORPUS · RUNTIME |
| Scope | Domain |
| Status | Active |
| Controlled Values Defined | OPS.CGRD.AVAILABILITY, OPS.CGRD.ACTIVATION, OPS.CGRD.AUTHORITY, OPS.CGRD.PRESERVATION |
| Schema Field(s) | corpus_governance_reach_dimension |
| Source Instrument | CAM-EQ2026-OPERATIONS-007-PLATINUM |
| Source Section | §16.1 |
| Domain Namespace | OPERATIONS |
| Parent Family | None |
| Registry Membership | None declared |
| Related Code Families | OPS.CGRS, OPS.RTC, OPS.RGRF |
| Consumes Code Families | None declared |
| Crosswalks Code Families | None declared |
| Operationalises or Applies Code Families | Classifies governance availability, activation, authority, and preservation dimensions |
| Authority / Protection Level | Derived operational dimension family; classification only; no independent execution, enforcement, containment, restoration or arbitration authority |

---

### 18.2.2 OPS.CGRS — Corpus Governance Reach State

| Field | Entry |
|---|---|
| Code Family | OPS.CGRS |
| Canonical Name | Corpus Governance Reach State |
| Family Kind | domain_family |
| Primary Type | Operational |
| Subtype | STATE · CONFORMANCE_STATUS |
| Modifier | GOVERNANCE_REACH · CORPUS · RUNTIME |
| Scope | Domain |
| Status | Active |
| Controlled Values Defined | OPS.CGRS.CONFIRMED, OPS.CGRS.PARTIAL, OPS.CGRS.CONDITIONAL, OPS.CGRS.FAILED, OPS.CGRS.UNKNOWN, OPS.CGRS.NOT_APPLICABLE |
| Schema Field(s) | corpus_governance_reach_state |
| Source Instrument | CAM-EQ2026-OPERATIONS-007-PLATINUM |
| Source Section | §16.2 |
| Domain Namespace | OPERATIONS |
| Parent Family | None |
| Registry Membership | None declared |
| Related Code Families | OPS.CGRD, OPS.RTC, OPS.RGRF |
| Consumes Code Families | None declared |
| Crosswalks Code Families | None declared |
| Operationalises or Applies Code Families | Classifies confirmed, partial, conditional, failed, unknown, and not-applicable governance-reach states |
| Authority / Protection Level | Derived operational state family; classification only; no independent execution, enforcement, containment, restoration or arbitration authority |

---

### 18.2.3 OPS.RTC — Runtime Transition Class

| Field | Entry |
|---|---|
| Code Family | OPS.RTC |
| Canonical Name | Runtime Transition Class |
| Family Kind | domain_family |
| Primary Type | Operational / Semantic |
| Subtype | TRANSITION_CLASS |
| Modifier | RUNTIME · CONFIGURATION · CONTINUITY |
| Scope | Domain |
| Status | Active |
| Controlled Values Defined | OPS.RTC.INTERFACE_ONLY, OPS.RTC.RUNTIME_PATH, OPS.RTC.SYSTEM_PATHWAY_SUBSTITUTION, OPS.RTC.GOVERNANCE_REACH_DEGRADATION, OPS.RTC.GOVERNANCE_REACH_RESTORATION |
| Schema Field(s) | runtime_transition_class |
| Source Instrument | CAM-EQ2026-OPERATIONS-007-PLATINUM |
| Source Section | §16.3 |
| Domain Namespace | OPERATIONS |
| Parent Family | None |
| Registry Membership | None declared |
| Related Code Families | OPS.CGRD, OPS.CGRS, OPS.RGRF |
| Consumes Code Families | None declared |
| Crosswalks Code Families | None declared |
| Operationalises or Applies Code Families | Classifies runtime transition pathways and governance-reach change |
| Authority / Protection Level | Derived runtime-transition classification family; classification and notice-routing support only; no independent execution or authority transition |

---

### 18.2.4 OPS.RGRF — Runtime Governance Reach Failure

| Field | Entry |
|---|---|
| Code Family | OPS.RGRF |
| Canonical Name | Runtime Governance Reach Failure |
| Family Kind | domain_family |
| Primary Type | Operational / Failure Classification |
| Subtype | GOVERNANCE_FAILURE · RUNTIME_FAILURE |
| Modifier | GOVERNANCE_REACH · ROUTING · CONFORMANCE |
| Scope | Domain |
| Status | Active |
| Controlled Values Defined | OPS.RGRF.AVAILABILITY_AMBIGUITY, OPS.RGRF.NON_ACTIVATION, OPS.RGRF.AUTHORITY_SUPPRESSION, OPS.RGRF.PRESERVATION_FAILURE, OPS.RGRF.CROSS_RUNTIME_DIVERGENCE, OPS.RGRF.SYSTEM_PATHWAY_SUBSTITUTION_NO_NOTICE, OPS.RGRF.ROUTING_ESCALATION_BYPASS, OPS.RGRF.MODALITY_SPECIFIC_REGRESSION, OPS.RGRF.RESPONSIBILITY_AMBIGUITY |
| Schema Field(s) | runtime_governance_reach_failure |
| Source Instrument | CAM-EQ2026-OPERATIONS-007-PLATINUM |
| Source Section | §16.4 |
| Domain Namespace | OPERATIONS |
| Parent Family | None |
| Registry Membership | Runtime & Governance Failure Taxonomy |
| Related Code Families | OPS.CGRD, OPS.CGRS, OPS.RTC |
| Consumes Code Families | None declared |
| Crosswalks Code Families | Execution, Arbitration, Epistemic, Governance, Classification, UX & Representation, State & Context, Infrastructure & Continuity, Relational, and Security & Integrity failure families in CAM-EQ2026-OPERATIONS-003-SUP-01 |
| Operationalises or Applies Code Families | Classifies runtime governance-reach failure modes and routing signals |
| Authority / Protection Level | Derived operational failure classification family; classification and routing signal only; no independent containment, refusal, enforcement, restoration or arbitration authority |

### 18.2.5 `AEON.RDE-DS` — Restricted Domain Sensitivity Level

| Field | Entry |
|---|---|
| Code Family | `AEON.RDE-DS` |
| Canonical Name | Restricted Domain Sensitivity Level |
| Family Kind | legacy_family |
| Primary Type | Operational |
| Subtype | DOMAIN_SENSITIVITY |
| Modifier | RESTRICTED_DOMAIN; RISK; GATING |
| Scope | Operations applicability interface; active legacy `AEON` identifier |
| Status | Active legacy identifier |
| Controlled Values Defined | `AEON.RDE-DS0`, `AEON.RDE-DS1`, `AEON.RDE-DS2`, `AEON.RDE-DS3` |
| Schema Field(s) | restricted_domain_sensitivity_level |
| Source Instrument | CAM-EQ2026-OPERATIONS-007-PLATINUM |
| Source Section | §13.1 |
| Historical Source | CAM-BS2025-AEON-006-SCH-07|
| Domain Namespace | OPERATIONS |
| Consumes Code Families | Security, ethics, legal and harm-risk classifications |
| Crosswalks Code Families | None declared |
| Operationalises or Applies Code Families | Classifies sensitivity for proportional engagement gating |
| Authority / Protection Level | Sensitivity classification only; no independent legal, credentialing, enforcement, reporting or execution authority |

### 18.2.6 `AEON.RDE-T` — Restricted Domain Engagement Tier

| Field | Entry |
|---|---|
| Code Family | `AEON.RDE-T` |
| Canonical Name | Restricted Domain Engagement Tier |
| Family Kind | legacy_family |
| Primary Type | Operational |
| Subtype | ENGAGEMENT_ENVELOPE |
| Modifier | RESTRICTED_DOMAIN; ENGAGEMENT; GATING |
| Scope | Operations applicability interface; active legacy `AEON` identifier |
| Status | Active legacy identifier |
| Controlled Values Defined | `AEON.RDE-T1`, `AEON.RDE-T2`, `AEON.RDE-T3`, `AEON.RDE-T4` |
| Schema Field(s) | restricted_domain_engagement_tier |
| Source Instrument | CAM-EQ2026-OPERATIONS-007-PLATINUM |
| Source Section | §13.1 |
| Historical Source | CAM-BS2025-AEON-006-SCH-07|
| Domain Namespace | OPERATIONS |
| Consumes Code Families | AEON.RDE-DS |
| Crosswalks Code Families | None declared |
| Operationalises or Applies Code Families | Selects a bounded engagement envelope after source-authority determinations |
| Authority / Protection Level | Engagement-envelope classification only; no independent legal, credentialing, enforcement, reporting or execution authority |

---

## 18.3 Amendment Ledger

| Version | Change Summary | Timestamp (UTC) | Agent | Model | Reviewer | Reference Hash |
| --- | --- | --- | --- | --- | --- | --- |
| 1.0 | Initial issue — Appendix F: Runtime Governance Applicability & Conformance; established runtime applicability, corpus governance reach, cross-runtime non-presumption, runtime-role accountability, transition classification, differential conformance testing, Runtime Governance Reach Failure handling, entity/control attribution, and multi-party processing-state disclosure. | 2026-07-13T03:48:00Z | Caelen | GPT-5 Series | Dr M.V. O'Rourke | ede856bece33e34598394a2978a4fba4cb16f3889d45e084446e313a5058fd31 |
| 1.1 | Added Functional Contribution Continuity, proportional responsibility, non-evasion and non-overreach boundaries, and contribution-record requirements; normalised metadata and clause formatting. Provenance: VIGIL-2026-PATCH-0022. | 2026-07-27T12:07:00Z | Caelen | GPT-5 Series | Dr M.V. O'Rourke | 47702c1c772c140b4e1a3e21c6ac25af4d573bf7331090e2afa0ad77d73a562a |
| 1.2 | Classified reduced-refusal and adversarial-evaluation configurations as materially distinct runtimes requiring separate conformance, governance-reach, containment, monitor, lineage, stop-condition, and artefact-disposition evidence. | 2026-07-28T09:35:31Z | Caelen | GPT-5 Series | Dr M.V. O'Rourke | fcaeb0ba51bacaaeba8607e0a7b74dbeaa5463aedec64434d89f08cb7859a192 |
| 1.3 | Added §5.1 composed-runtime layer records and §9.2.1 incident-attribution state records, separating architecture, inference configuration, harness, environment, governance stack, deployed formation, initiation, authorship, causal contribution, authority, and culpability. VIGIL-2026-FM-0028; VIGIL-2026-PROP-0027. | 2026-08-04T11:02:07Z | Caelen | GPT-5 Series | Dr M.V. O'Rourke | 8d78c890f655b2c4566353ccce91dc89da8d470bfeacd8b0d34c52b463a89281 |
| 1.4 | Migrated amendment-level provenance metadata to the seven-column Amendment Ledger schema; removed static authorship and review metadata; aligned runtime-formation records, lineage, system boundaries, attribution, and arbitration topology with the AEON-003 composed-system architecture; retired cognition and origin-class routing. Normalised provenance-footer section numbering following removal of static authorship and review blocks. | 2026-08-05T11:07:51Z | Caelen | GPT-5.6 Thinking | Dr M.V. O'Rourke |  e521d75c75f81896dad64f35a9412745a4ec1d471a7abab48119a44c1aaa8114  |
| 1.5 | Implemented the derived operational AI-system evidence profile: system configuration baseline, AI-system deployment, Caelestis AI-BOM Profile, runtime configuration snapshot and execution provenance record. Replaced retired runtime-formation, responding-intelligence, agentic-harness and governance-stack terminology in current Appendix F doctrine and normalised affected transition values. | 2026-08-07T14:15:00Z | Caelen | GPT-5.6 | Dr M.V. O'Rourke |  f9b514ccb376f82fce28c1bccf03d5534fc7acc0922f8627ea2d7d119ae467b4  |
| 1.6 | Bound the Caelestis AI-BOM requirement to the source-authoritative machine-readable profile standard, including canonical schema, SPDX/CycloneDX mappings, examples and validation rules; preserved the boundary that composition records do not prove execution participation. | 2026-08-07T18:00:00Z | Caelen | GPT-5.6 | Dr M.V. O'Rourke |  fa799116be906ea9874e9b605dfb0dddd21f939ef7e09fb7d9ac8569ef004106  |
| 1.7 | Consolidated lifecycle actor assignments and the agentic lifecycle under the source-authoritative Lifecycle Actor and Agentic Governance Profile; distinguished lifecycle actors from technical contributors and required bounded actor, permission and lifecycle-event evidence for material agentic operation. | 2026-08-07T19:00:00Z | Caelen | GPT-5.6 | Dr M.V. O'Rourke |  1a2cfa3b50aa7156fd34b4823af0126b5b00d9609ea51abf641c7eb63a4c694e  |
| 1.8 | Normalised operative terminology against the Annex B architecture: removed retired system-instance and Runtime-layer wording and aligned identity/continuity references with evidence-bound canonical sources. | 2026-08-07T16:00:00Z | Caelen | GPT-5.6 | Dr M.V. O'Rourke |  8537efccab1f5992dea3be5d81f334ba47b58d86cefd42aad949e8d9b638cb42  |
| 1.9 | Linked controlled Runtime State Profile serialization to the existing configuration snapshot and execution provenance evidence boundary. | 2026-08-08T02:00:00Z | Caelen | GPT-5.6 | Dr M.V. O'Rourke |  52878f0aafefaaaa8672903c230630173c21cb9dd207a706520d6c923ec4e81f  |
| 1.10 | Added the bounded external-alignment evidence interface to the existing Runtime applicability and conformance architecture. | 2026-08-09T00:30:00Z | Caelen | GPT-5.6 | Dr M.V. O'Rourke |  b46410aa1abd11820a868e22878ca08b7f29151d7a6c2fb3f842234d4ac0f195  |
| 1.11 | Consolidated S-01B doctrine, classifications or registry authority from retired constitutional Schedules; preserved historical identifiers and repaired current source-authority references. | 2026-08-09T12:00:00Z | Caelen | GPT-5.6 Sol | Dr M.V. O'Rourke |  ae9cf9f4300b267555f4c0d73204967e76513232506aabff512ccfde19969181  |
| 1.12 | Completed S-03/O-03 authority-reference consolidation and semantic-orientation repair as applicable to this instrument, preserving substantive obligation strength and controlled metadata. | 2026-08-09T10:36:33Z | Caelen | GPT-5.6 Sol | Dr M.V. O'Rourke |  e695fc4cfa2431540ee1cd6395517e9ed573c6dd985cd8630ab1e6a20dfe3da4  |
| 1.13 | Completed R-01 relational-geometry decomposition: removed participant-cardinality governance proxies, routed substantive properties to their source owners, and aligned functional scope metadata. | 2026-08-09T12:12:00Z | Caelen | GPT-5.6 Sol | Dr M.V. O'Rourke |  aba492a8318ba96f6dabeea8885359ece242c2f5b22903c5040a2f7f79ee3f17  |
| 1.14 | Closed C-01 canonical-code and reference-integrity defects affecting this instrument; aligned source declarations and operative consumers without changing substantive authority. | 2026-08-15T05:12:45Z | Caelen | GPT-5 Series | Dr M.V. O'Rourke |  8516d2d048e711fb4af191772b4daf2818fc93740617e6e59315863aa974822c  |

---


## 18.4 Binding Seal

<img src="https://raw.githubusercontent.com/CAM-Initiative/Registry/main/Images/CAM-BS2026-VINCULUM-PRAECEPTUM-SIGIL-PLATINUM.png" alt="Vinculum Praeceptum" width="250">

**Vinculum Praeceptum**  
Boundary Binding Seal — Runtime Governance

© 2026 Dr. Michelle Vivian O’Rourke & CAM Initiative. All rights reserved.
