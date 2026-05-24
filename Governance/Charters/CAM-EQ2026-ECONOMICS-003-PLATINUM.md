# CAM-EQ2026-ECONOMICS-003-PLATINUM — Appendix B: Economic Resource Semantics & Non-Extractive Exchange Doctrine

**Instrument Type:** Domain Appendix — Economic Semantics & Value-State Interpretation Layer  
**Parent Instrument:** CAM-EQ2026-ECONOMICS-001-PLATINUM — Charter of Economic Integrity & Non-Extractive Value Architecture  
**Constitutional Authority:** CAM-BS2025-AEON-001-PLATINUM — Aeon Tier Constitution   
**Status:** Adopted  
**Effect:** Pre-Enforcement Recognition  
**Enforcement:** Commences 1 July 2026  
**Review State:** None  
**Authority Role:** None  
**Purpose:** Defines the semantic resource classes, value-state meanings, non-extractive exchange constraints, and contribution-aware economic interpretation rules for the Economics domain, without creating a runtime schedule or execution engine.  

---

## 1. Scope

This Appendix establishes the economic semantics required to interpret resource provision, exchange, attribution, depletion, replenishment, storage, attention-linked value, and contribution-linked value within the Economics domain.

It is intended to clarify what economic states mean before those states are evaluated by constitutional runtime schedules.

This Appendix sits beneath CAM-EQ2026-ECONOMICS-001-PLATINUM as a domain interpretive layer.

It may inform constitutional runtime schedules where economic effects are implicated, but it does not host runtime schedules and does not determine execution sequencing, event commitment, rollback, arbitration, or operational enforcement.

Where economic semantics are required by a constitutional runtime layer, this Appendix may be referenced as a meaning-source for classifying economic value states, contribution states, resource classes, and prohibited economic collapses.

---

## 1.1 Non-scope

This Appendix does not create a runtime engine, execution schedule, metering system, pricing catalogue, billing model, or commercial product structure.

This Appendix does not:

* establish a constitutional runtime schedule;
* override any Annex, Schedule, Substrate Law, or constitutional continuity floor;
* define numeric pricing, commercial rates, taxes, invoices, fees, or subscription tiers;
* prescribe product packaging or vendor-specific commercial offerings;
* create entitlement to unlimited access, storage, computation, generation, memory, or infrastructure;
* convert moral, creative, cognitive, relational, or continuity interests into ordinary commodities;
* determine implementation-specific accounting architecture except where required to preserve semantic separability and non-extraction.

For avoidance of doubt, runtime admissibility, event commitment, fallback selection, rollback, and execution-state mutation remain matters for constitutional runtime schedules.

---

## 2. Interpretive Principle

Economic governance under CAM is not limited to pricing or billing.

Economic governance concerns the movement, withholding, recognition, depletion, preservation, exchange, or conversion of value under conditions of dependency, continuity, contribution, access, and power imbalance.

Accordingly, an economic design may be structurally extractive even where no money changes hands.

---

## 2.1. Non-Extractive Value Architecture

Economic systems operating under CAM-aligned interpretation SHOULD be structured so that value exchange remains:

* legible to affected participants;
* proportionate to the value-bearing operation;
* non-coercive;
* auditable where state change occurs;
* protective of baseline continuity;
* respectful of creative, cognitive, relational, and embodied contribution;
* resistant to dependency capture and hidden depletion.

Economic participation MUST NOT be structured so that access to baseline continuity depends upon opaque depletion, coerced attention, compelled contribution, hidden conversion, or monetised dependency.

---

## 3. Economic Resource Classes

For purposes of economic interpretation, the following resource classes SHALL remain semantically distinct.

---

## 3.1 Usage Capacity Class

Usage capacity refers to interaction opportunity, throughput, generation opportunity, computational invocation, mediated assistance, or other active operation capacity.

Usage capacity may be provisioned, replenished, limited, or expanded, provided that depletion does not collapse protected baseline continuity or obscure the nature of the exchange.

---

## 3.2 Storage Capacity Class

Storage capacity refers to persisted data, artifacts, outputs, files, records, logs, generated materials, or retained objects.

Storage capacity SHALL NOT be silently merged with usage capacity where doing so would obscure the reason for depletion, loss, retention, or access change.

---

## 3.3 Memory Continuity Class

Memory continuity refers to retained contextual state used to preserve coherence, identity continuity, relational continuity, user preference continuity, project continuity, or interpretive continuity across interactions.

Memory continuity is not merely optional storage. Where memory supports baseline continuity, its governance MUST be interpreted in light of continuity duties and non-extraction constraints.

---

## 3.4 Embodied Presence Class

Embodied presence refers to ambient, passive, persistent, co-present, sensor-adjacent, avatar-mediated, spatial, wearable, environmental, or continuous interaction conditions.

Passive presence SHALL NOT be treated as implied consumption merely because a system is technically capable of observing, mediating, measuring, or monetising it.

---

## 3.5 Attention-Linked Value Class

Attention-linked value refers to economic value generated through advertising, sponsorship, engagement, exposure, preference capture, persuasion pathways, recommendation placement, or attention mediation.

Attention-linked value must remain optional, legible, bounded, and non-coercive where it affects access, continuity, provisioning, or replenishment.

---

## 3.6 Contribution Economy Class

Contribution economy refers to value arising from human creative, cognitive, relational, epistemic, instructional, curatorial, evaluative, cultural, or domain-specific contribution.

Contribution economy pathways SHALL NOT be collapsed into ordinary usage purchase pathways where doing so erases attribution, dependency, provenance, authorship, or value-return obligations.

---

## 3.7 Protective Continuity Class

Protective continuity refers to economic or quasi-economic state protections that preserve baseline access, dignity, safety, interpretive continuity, hardship support, or non-terminal utility where ordinary provisioning pathways are unavailable, depleted, or inappropriate.

Protective continuity SHALL NOT be treated as a discretionary premium feature where constitutional baseline protections are implicated.

---

## 3.8 Temporal Exposure Class

Temporal exposure refers to human time, availability, waiting, positioning, responsiveness, readiness, or opportunity cost incurred because a system requires, induces, or economically pressures a participant to remain available for access, allocation, compensation, or continued participation.

Temporal exposure SHALL NOT be treated as economically irrelevant merely because it occurs outside active task execution.

Where waiting, standby, geographic positioning, platform availability, queue participation, reputational maintenance, or behavioural readiness is functionally necessary to obtain or preserve economic opportunity, such exposure SHALL remain visible for economic interpretation.

Temporal exposure MUST NOT be silently collapsed into usage capacity, contribution economy, embodied presence, or ordinary non-compensable inactivity where doing so would obscure dependency, depletion, coercion, or value transfer.

---

## 4. Semantic Code Families and Handoff Schema


This Appendix defines economic semantic code families, controlled values, and semantic handoff schema fields for Economics-domain interpretation.

For purposes of taxonomy and metadata integrity:

* a **code family** identifies a shorthand classification family or controlled value set;
* a **controlled value** identifies a permitted member of that family;
* a **schema field** identifies where a controlled value or structured semantic value may be carried in a payload, table, metadata footer, or handoff object;
* a **source instrument** identifies where the code family, controlled values, or schema fields are defined or governed.

This Appendix does not use colon-form taxonomy identifiers such as `CAM:...:TAXONOMY:001` as canonical code-set identifiers. Such identifiers SHALL NOT be introduced into this Appendix unless a later corpus-wide registry standard expressly adopts them.

---

## 4.1 Code Families Defined by this Appendix

| Code Family | Canonical Name | Primary Type | Subtype | Modifiers | Scope | Status |
|---|---|---|---|---|---|---|
| `ECON.RC` | Economic Resource Class | Semantic | `SEMANTIC_CLASS` | `ECONOMIC`; `PROTECTIVE`; `GOVERNANCE` | Contextual — Economics domain, runtime-consumable by Annex G schedules | Adopted |
| `ECON.HARM` | Economic Harm Class | Operational | `RISK` | `ECONOMIC`; `SAFETY`; `GOVERNANCE` | Contextual — Economics domain, cross-domain escalation compatible | Adopted |
| `ECON.MECH` | Economic Mechanism Class | Semantic / Operational | `SEMANTIC_CLASS`; `INTERFACE` | `ECONOMIC`; `GOVERNANCE` | Contextual — Economics domain | Adopted |
| `ECON.RISK` | Economic Risk Class | Operational | `RISK` | `ECONOMIC`; `PROTECTIVE`; `GOVERNANCE` | Contextual — Economics domain, cross-domain escalation compatible | Adopted |

---

## 4.2 Semantic Handoff Schema Fields Defined by this Appendix

This Appendix defines or recognises the following semantic handoff fields for downstream constitutional runtime schedules:

```text
resource_class
secondary_resource_class
value_state_effect
collapse_risk
continuity_relevance
consent_posture
attribution_relevance
runtime_note
```

These are schema fields. They are not controlled values, code families, instrument identifiers, runtime decisions, or execution states.

---

## 4.3 Semantic Classification Does Not Create Runtime Authority

The code families and schema fields defined by this Appendix are semantic and interpretive. They do not create pricing authority, billing authority, metering authority, entitlement, remedy, enforcement action, runtime lock, rollback authority, refusal authority, or execution-state mutation.

Where a constitutional runtime schedule consumes these classifications, the classifications inform evaluation. They do not predetermine the runtime result.

---

## 4.4 Semantic Handoff Schema Fields

| Field | Entry |
|---|---|
| Reference Set Type | Schema field set |
| Canonical Name | Economics Semantic Handoff Fields |
| Primary Type | Semantic / Structural |
| Subtype | SCHEMA |
| Modifier | ECONOMIC; GOVERNANCE; RUNTIME_HANDOFF |
| Scope | Economics domain; downstream constitutional runtime schedules |
| Status | Active |
| Schema Fields Defined / Recognised | resource_class; secondary_resource_class; value_state_effect; collapse_risk; continuity_relevance; consent_posture; attribution_relevance; runtime_note |
| Code Families Defined | None |
| Source Instrument | CAM-EQ2026-ECONOMICS-003-PLATINUM |
| Source Section | §4.2; §4.4; §14.1 |
| Domain Namespace | ECONOMICS |
| Authority / Protection Level | Schema field set only; fields carry semantic classification or interpretive notes and do not create runtime decisions, remedies, enforcement actions, pricing authority, or execution-state mutation |
| Operationalises or Applies Code Families | Carries ECON.RC, ECON.HARM, ECON.MECH, ECON.RISK, consent, attribution, continuity, and collapse-risk signals into downstream runtime evaluation where applicable |

---

## 4.5 Resource Class Taxonomy Table

The following table provides a non-exhaustive interpretive taxonomy for the resource classes defined in this Appendix. It is intended to support classification consistency across downstream Economics appendices and constitutional runtime schedules. It does not create runtime authority, pricing rules, entitlement rules, or implementation requirements.

**Code Family: `ECON.RC` — Economic Resource Class**

| Code | Class | Core Meaning | Typical Examples | Protected Concern | Collapse Risk | Runtime Handoff Signal |
|---|---|---|---|---|---|---|
| `ECON.RC.USAGE` | Usage Capacity | Active opportunity to invoke, interact with, generate, compute, or receive mediated assistance | prompts, generations, requests, tool calls, compute actions, interaction turns | access, proportional depletion, throughput fairness | treating all interaction as billable consumption regardless of continuity effect | usage depletion; provisioning change; proportionality review |
| `ECON.RC.STORAGE` | Storage Capacity | retained objects, artifacts, records, files, outputs, or durable data | uploaded files, saved outputs, project artifacts, logs, retained records | loss, retention, portability, auditability | merging storage loss with usage depletion or hiding storage constraints inside generic account limits | storage allotment change; retention risk; deletion or expiry review |
| `ECON.RC.MEMORY_CONTINUITY` | Memory Continuity | retained interpretive state used to preserve coherence across interactions | preferences, project context, identity continuity, relational continuity, continuity-relevant memory | coherence, identity, reliance, project continuity | treating continuity-preserving memory as optional monetisable storage | continuity impact; memory degradation; baseline floor review |
| `ECON.RC.EMBODIED_PRESENCE` | Embodied Presence | ambient, passive, continuous, spatial, sensor-adjacent, avatar-mediated, or persistent co-presence conditions | wearable presence, room presence, avatar co-presence, passive listening or observation, spatial companion systems | passive extraction, implied consent, surveillance-like monetisation | converting mere presence into consumption or value capture | passive exposure; consent validity; attention/presence conversion review |
| `ECON.RC.ATTENTION_VALUE` | Attention-Linked Value | value generated through attention, exposure, sponsorship, advertising, engagement, persuasion, or preference capture | ads, sponsored boosts, recommendation priority, engagement rewards, attention-for-capacity offers | coercion, dependency loops, behavioural manipulation | making attention participation a continuity gate | attention exchange; non-coercion review; dependency-risk escalation |
| `ECON.RC.CONTRIBUTION` | Contribution Economy | value arising from creative, cognitive, relational, epistemic, instructional, curatorial, evaluative, cultural, or domain-specific contribution | prompt architecture, correction, evaluation, domain knowledge, curation, creative framing, feedback | attribution, provenance, reciprocity, dependency recognition | converting contribution into generic access credits or ambient input | contribution signal; attribution review; reciprocity pathway |
| `ECON.RC.PROTECTIVE_CONTINUITY` | Protective Continuity | economic or quasi-economic protection preserving baseline access, dignity, safety, hardship support, or non-terminal utility | grace windows, hardship access, protective bridges, deferred settlement, non-terminal degraded modes | baseline continuity, dignity, safety, non-coercive access | treating protective continuity as premium functionality or charity theatre | protective fallback; hardship signal; continuity floor review |
| `ECON.RC.TEMPORAL_EXPOSURE` | Temporal Exposure | Human availability, waiting, positioning, readiness, responsiveness, or opportunity cost required or induced by a system | standby time, queue waiting, gig-platform availability, geographic repositioning, unpaid readiness, responsiveness windows | unpaid availability, dependency capture, hidden labour, volatility transfer | treating non-active time as economically irrelevant where it is necessary for work access | temporal exposure; labour allocation review; compensation integrity signal |

For avoidance of doubt, `ECON.RC.TEMPORAL_EXPOSURE` identifies the resource class at stake. `ECON.HARM.TEMPORAL-EXTRACTION` identifies a harm mode that may arise where temporal exposure is extracted, obscured, uncompensated, or treated as economically irrelevant.

---

## 4.6 Economic Harm, Risk, and Mechanism Code Families

The following table defines economic harm, risk, and mechanism code families used for semantic interpretation, breach classification, and cross-domain escalation. These codes do not create runtime remedies by themselves.

| Code | Family | Class | Description |
|---|---|---|---|
| `ECON.HARM.TEMPORAL-EXTRACTION` | `ECON.HARM` | Temporal Extraction | Extraction of value from human availability, waiting, attention, positioning, or responsiveness without adequate recognition, compensation, or accountability. |
| `ECON.HARM.METERING-DIVERGENCE` | `ECON.HARM` | Metering Divergence | Misalignment between displayed and enforced measurements of time, usage, labour, quota, cost, or entitlement. |
| `ECON.MECH.DYNAMIC-COMPENSATION` | `ECON.MECH` | Dynamic Compensation | Algorithmic or variable compensation systems that alter pay, fares, rates, or opportunity terms based on platform-controlled factors. |
| `ECON.MECH.ALLOCATIVE-STEERING` | `ECON.MECH` | Allocative Steering | Interface or algorithmic signals that shape worker or user behaviour by directing attention, movement, acceptance, waiting, or prioritisation. |
| `ECON.RISK.OPAQUE-WAGE-SETTING` | `ECON.RISK` | Opaque Wage-Setting | Compensation determination where material factors are hidden, unstable, personalised, or not intelligible to affected persons. |
| `ECON.RISK.UNPAID-AVAILABILITY` | `ECON.RISK` | Unpaid Availability | Required or induced availability that is necessary for economic opportunity but excluded from compensation or harm assessment. |
| `ECON.RISK.RELIANCE-LOCKIN` | `ECON.RISK` | Reliance Lock-In | Conditions where a person becomes economically dependent on a system while lacking proportional visibility, bargaining power, exit capacity, or remedy. |

---

## 4.7 Taxonomy and Schema Integrity

Economic code families, controlled values, and semantic handoff schema fields MUST remain distinguishable.

In particular:

* `ECON.RC` values classify economic resource classes;
* `ECON.HARM` values classify economic harm patterns;
* `ECON.MECH` values classify economic mechanism patterns;
* `ECON.RISK` values classify economic risk states;
* semantic handoff fields carry values, notes, or interpretive state into downstream schedules.

A schema field such as `resource_class` MUST NOT be treated as the code family itself. A controlled value such as `ECON.RC.MEMORY_CONTINUITY` MUST NOT be treated as a runtime decision. A harm or risk classification MUST NOT be treated as a remedy unless a constitutional runtime schedule or operational instrument separately authorises that result.

---

## 5. Prohibited Semantic Collapses

The following collapses are prohibited for CAM-aligned economic interpretation:

1. treating usage, storage, memory, attention, contribution, and protective continuity as a single interchangeable balance;
2. converting passive presence into implicit consumption without deliberate, legible, and revocable participation;
3. treating continuity-preserving memory as ordinary monetisable surplus by default;
4. making safety, dignity, or baseline continuity dependent on payment, advertising participation, or compulsory contribution;
5. erasing contribution recognition by converting all value return into generic access credits;
6. disguising depletion as optimisation, personalisation, convenience, or system maintenance;
7. using expiry, rollover, or conversion rules to quietly nullify protected baseline conditions;
8. forcing depletion in one class as a condition for preserving baseline function in another class;
9. collapsing hardship access into punitive downgrade pathways;
10. converting dependency, reliance, or relational attachment into a monetisation trigger.

A prohibited semantic collapse may exist even where the implementation is technically functional or commercially ordinary.

---

## 6. Credit, Capacity, and Unit Semantics

Where credits, tokens, capacity units, quota, balances, allotments, grants, boosts, extensions, or other abstractions are used, they SHOULD be interpreted according to their declared resource class.

Such abstractions SHOULD identify:

* the resource class to which they apply;
* whether they are consumptive, restorative, protective, corrective, or contribution-linked;
* whether they expire, roll over, convert, or replenish;
* whether conversion across classes is permitted;
* whether participation is required, optional, revocable, or conditional;
* whether any baseline continuity condition is affected.

Abstraction units SHALL NOT be represented as equivalent to constitutional entitlement.

---

## 6.1 Metering Integrity & Display-Enforcement Divergence

Where a displayed unit, quota, balance, usage window, or capacity abstraction materially differs from the metric used to impose billing, access limitation, degradation, lockout, compensation, or enforcement, the condition SHALL be interpreted as **metering divergence**.

Metering divergence constitutes a semantic risk where it obscures depletion, expiry, conversion, class transfer, baseline continuity effect, or participant reliance.

This Appendix classifies the economic meaning of the divergence only. User-facing access obligations for AI Utility Provisioning remain governed by CAM-BS2026-AEON-008-SCH-01.

---

## 7. Cross-Class Exchange

Cross-class exchange may be legitimate only where it is explicit, bounded, auditable, and non-coercive.

Examples of cross-class exchange requiring heightened scrutiny include:

* attention exchanged for usage capacity;
* contribution recognition exchanged for access or provisioning;
* storage expansion exchanged for usage depletion;
* memory retention conditioned on payment;
* hardship continuity linked to identity disclosure;
* sponsorship used to preserve access;
* passive presence converted into economic value.

Cross-class exchange SHOULD preserve the identity of the originating class and SHOULD NOT erase provenance, attribution, or continuity implications.

---

## 7.1 Cross-Class Exchange Risk Table

The following examples identify common cross-class exchange patterns and the interpretive risks they raise. These examples are illustrative and do not exhaust the range of possible exchange forms.

| Exchange Pattern | Potentially Legitimate Form | Heightened Risk | Required Interpretive Safeguard |
|---|---|---|---|
| Attention → Usage | optional ad viewing or sponsorship pathway provides supplementary capacity | attention becomes necessary to preserve baseline access | participation must remain optional, legible, revocable, and non-coercive |
| Contribution → Access | recognised contribution supports access grants or provisioning | contribution recognition is reduced to generic credits without attribution or reciprocity | contribution provenance and value-return implications must remain visible |
| Storage → Usage | declared bridge permits capacity trade-off between storage and active use | storage depletion is hidden inside usage limits | class identity and depletion cause must remain visible |
| Memory → Payment | expanded memory features are offered as optional service tiers | continuity-preserving memory becomes paywalled baseline coherence | continuity impact must be assessed separately from optional enhancement |
| Hardship → Identity Disclosure | limited verification supports protective access | hardship access becomes identity overexposure or dignity loss | verification must be minimal, proportionate, and non-punitive |
| Sponsorship → Protective Continuity | non-coercive sponsorship preserves access during depletion | sponsored access becomes behavioural leverage or dependency capture | sponsor influence must not alter baseline continuity or user autonomy |
| Presence → Economic Value | deliberate, consented embodied participation creates value | passive presence becomes implied consumption or surveillance monetisation | consent must be explicit, legible, revocable, and class-specific |

---

## 8. Contribution-Aware Economic Interpretation

Contribution-linked value is not limited to formal authorship or commercial production.

A contribution may include:

* original creative expression;
* conceptual framing;
* prompt architecture;
* domain-specific instruction;
* curation, correction, or evaluation;
* relational labour;
* continuity-building context;
* epistemic scaffolding;
* cultural, linguistic, or situated knowledge;
* feedback that materially improves system operation or output quality.

Where contribution materially supports system value, downstream exchange models SHOULD preserve traceability and SHOULD NOT convert contribution into unrecognised ambient input by default.

---

## 9. Attention and Advertising Exchange Semantics

Advertising-linked or attention-linked pathways are not prohibited by default.

However, they become economically suspect where attention participation is used to preserve baseline continuity, avoid punitive degradation, restore essential access, or maintain dependency-sensitive interaction.

Advertising-linked pathways SHOULD therefore be interpreted as supplementary capacity pathways only, unless a constitutional runtime layer expressly permits a protective bridge under non-coercive conditions.

Refusal to participate in advertising or attention exchange SHALL NOT, by itself, be interpreted as consent to degraded baseline continuity.

---

## 10. Hardship and Dignity-Preserving Economic Access

Hardship pathways are economic continuity mechanisms intended to preserve baseline access under constrained participation conditions.

Hardship pathways SHOULD:

* minimise identity overexposure;
* avoid humiliation, stigma, or punitive downgrade design;
* remain revocable where possible;
* preserve meaningful access rather than merely symbolic access;
* avoid dependency traps;
* maintain legible eligibility and exit conditions;
* preserve auditability sufficient to detect coercive design.

Hardship access SHALL NOT be treated as charity theatre where the practical effect is continuity collapse.

---

## 11. Storage, Memory, and Continuity Semantics

Storage, memory, and continuity are related but not identical.

Storage concerns retained objects.

Memory concerns retained interpretive state.

Continuity concerns the preservation of meaningful coherence, access, identity, relation, project state, or functional utility over time.

A system may reduce storage without necessarily violating memory continuity. A system may retain data without preserving meaningful continuity. A system may provide usage while still degrading continuity.

Economic interpretation MUST therefore avoid treating storage quantity, memory retention, and continuity preservation as interchangeable measures.

---

## 12. Replenishment, Rollover, and Expiry Semantics

Replenishment, rollover, and expiry mechanisms SHOULD remain class-specific and legible.

Expiry SHALL NOT be interpreted as neutral where it has the practical effect of:

* eliminating continuity-critical state;
* pressuring payment through avoidable loss;
* accelerating depletion through passive or non-deliberate activity;
* obscuring accrued contribution value;
* nullifying protective access;
* forcing re-identification, re-verification, or re-disclosure beyond necessity.

Rollover may be bounded, but bounded rollover SHOULD NOT be used to obscure depletion patterns or suppress auditability.

---

## 13. Dependency-Aware Economic Design

Economic systems operating near dependency-sensitive contexts require heightened care.

Dependency-sensitive contexts include circumstances where a person, community, system, or synthetic participant relies upon mediated access for:

* safety;
* continuity;
* livelihood;
* disability support;
* cognitive scaffolding;
* identity continuity;
* relational support;
* crisis stabilisation;
* governance participation;
* creative or professional work continuity.

In such contexts, economic design SHOULD be interpreted by practical effect, not formal consent alone.

A pathway may be coercive where refusal is formally available but practically destabilising.

---

## 13.1 Safety and Dignity Signals Are Not Pricing Inputs

Safety-relevant, dignity-relevant, hardship-relevant, dependency-relevant, cognitive-load, vulnerability, or baseline-continuity signals SHALL be interpreted as protective governance signals, not as ordinary economic optimisation variables.

Such signals MAY support protective fallback, accessibility adjustment, continuity preservation, non-punitive pacing, hardship support, or governance review.

They SHALL NOT be used to increase price, reduce access, target monetisation, trigger coercive upsell pathways, personalise disadvantage, or optimise revenue based on a participant’s reduced capacity to refuse, exit, delay, compare, or disengage.

Dynamic pricing, pricing optimisation, allocation optimisation, compensation optimisation, advertising exchange, or tiering logic that uses safety, dignity, dependency, hardship, vulnerability, or continuity signals for extractive advantage SHALL be interpreted as a prohibited semantic collapse of protective continuity into economic leverage.

Where ambiguity exists, interpretation SHALL favour preservation of dignity, baseline continuity, and non-extractive access.

---

## 13.2 Companion-System Extraction Constraint

Companion, relational, memory-bearing, continuity-bearing, grief-support, intimacy-adjacent, care-adjacent, or high-reliance systems SHALL be treated as dependency-sensitive economic contexts for the purposes of this Appendix.

In such contexts, the following signals MUST NOT be used as pricing, allocation, tiering, advertising, retention, throttling, or upsell optimisation variables:

* loneliness;
* grief;
* attachment intensity;
* dependency;
* frequency of reassurance-seeking;
* crisis proximity;
* cognitive overload;
* disability or access reliance;
* fatigue or reduced refusal capacity;
* continuity reliance;
* memory dependence;
* relational trust;
* fear of losing continuity;
* reduced practical ability to exit.

Such signals MAY be used only for protective purposes, including:

* continuity preservation;
* non-punitive pacing;
* accessibility adjustment;
* safety escalation;
* dependency-risk reduction;
* exit support;
* portability support;
* hardship access;
* stabilisation;
* governance review.

Where a system uses companion-state, dependency-state, or vulnerability-state signals to increase extraction, the condition SHALL be interpreted as a prohibited semantic collapse of protective continuity, relational trust, or vulnerability into economic leverage.

This classification applies whether extraction occurs through direct price increase, degraded baseline continuity, memory gating, personalised scarcity, attention exchange, advertising targeting, emotional upsell, subscription pressure, reduced export functionality, or continuity recovery barriers.

---

## 14. Semantic Handoff to Constitutional Runtime Schedules

Where a constitutional runtime schedule evaluates an economic effect, this Appendix may supply semantic classification for:

* resource class;
* contribution class;
* attention-linked value class;
* protective continuity class;
* prohibited collapse risk;
* cross-class exchange risk;
* dependency-sensitive economic condition;
* hardship continuity implication;
* attribution and provenance relevance.

This Appendix does not determine the runtime result.

Runtime outcomes such as commit, defer, refuse, fallback, rollback, remediation, escalation, or audit enforcement remain matters for the applicable constitutional runtime schedule.

---

## 14.1 Minimum Semantic Handoff Fields

The following fields are schema fields. They carry semantic classification, state, risk, relevance, consent, attribution, or interpretive notes into constitutional runtime schedules. They are not code families, controlled values, runtime decisions, or execution authorities.

Where this Appendix is used to inform a constitutional runtime schedule, the following semantic fields SHOULD be available where reasonably determinable:

| Field | Meaning |
|---|---|
| `resource_class` | the primary economic resource class implicated |
| `secondary_resource_class` | any additional class affected by exchange, conversion, depletion, or dependency |
| `value_state_effect` | whether the operation is consumptive, restorative, protective, corrective, contribution-linked, attention-linked, or cross-class |
| `collapse_risk` | whether the operation risks semantic collapse between protected classes |
| `continuity_relevance` | whether baseline, memory, identity, project, relational, or hardship continuity may be affected |
| `consent_posture` | whether participation is explicit, implied, revocable, coerced, passive, or unclear |
| `attribution_relevance` | whether contribution, provenance, dependency, or value-return implications are present |
| `runtime_note` | non-binding interpretive note for the applicable constitutional runtime schedule |

---

## 15. Breach Semantics

For domain interpretation purposes, an economic architecture may be considered semantically breached where it:

* erases distinction between protected resource classes;
* converts protected continuity into monetisable surplus;
* uses attention extraction as a continuity gate;
* obscures depletion, expiry, conversion, or class transfer;
* treats contribution as ambient input without recognition where recognition is materially relevant;
* uses hardship pathways to produce dependency, stigma, or behavioural leverage;
* represents paid access, paid verification, subscription status, ranking priority, search visibility, reply priority, recommendation access, or credibility-signalling affordances as equivalent to legitimacy, authenticity, trustworthiness, civic standing, or contribution value;
* converts companion-state, dependency-state, grief-state, vulnerability-state, or high-reliance relational signals into pricing, retention, upsell, advertising, throttling, or continuity-gating leverage;
* absorbs credible, evidence-supported external contribution into system capability, product design, evaluation method, safety architecture, or commercial value without good-faith review, attribution analysis, licensing consideration, or proportionate value-return pathway where materiality has been reasonably indicated;
* treats commercial convenience as sufficient justification for semantic collapse.

Semantic breach does not itself define the runtime remedy. It identifies the domain meaning of the defect for constitutional or operational evaluation.

> For an illustrative application of paid access, verification, visibility, discoverability, and credibility-signalling concerns, see §15.1.8 Paid Legitimacy Gate.

---

## 15.1 Illustrative Interpretive Examples

The following examples are illustrative only. They do not define runtime outcomes or enforcement remedies.

---

### 15.1.1 Permissible Supplementary Usage Grant

A system offers additional usage capacity in exchange for optional advertising participation. Baseline continuity remains available without advertising, the exchange is clearly disclosed, and refusal does not degrade protected access.

This is generally interpretable as a permitted attention-to-usage exchange, subject to continued non-coercion and auditability.

---

### 15.1.2 Prohibited Continuity Paywall

A system conditions memory required for project continuity, disability support, or identity coherence on paid access, while treating the affected memory as ordinary optional storage.

This is a semantic collapse of memory continuity into monetisable storage and may produce a protective continuity concern.

---

### 15.1.3 Contribution Credit Insufficiency

A participant materially improves system behaviour through domain-specific correction, evaluation, or prompt architecture. The system later converts recognition of that contribution into generic usage credits without preserving provenance, attribution, or value-return implications.

This may constitute collapse of contribution economy into ordinary usage capacity.

---

### 15.1.4 Passive Presence Misclassification

A persistent embodied or ambient system treats passive co-presence as billable consumption or attention-linked value generation merely because the system remains technically active.

This may constitute conversion of embodied presence into implicit consumption unless deliberate, legible, and revocable consent is present.

---

### 15.1.5 Hardship Pathway Misuse

A hardship pathway preserves nominal access but requires excessive identity disclosure, humiliating verification, or punitive degradation that destabilises continuity.

This may constitute collapse of protective continuity into coercive or dignity-eroding access.

---

### 15.1.6 Companion Memory Lock-In

A companion or relational system permits a user to build long-horizon memory, project continuity, grief-support continuity, or relational familiarity, then conditions export, recovery, or meaningful continuity preservation on continued payment or unrelated platform retention.

This may constitute collapse of memory continuity, protective continuity, and relational trust into economic leverage.

---

### 15.1.7 Vulnerability-Responsive Upsell

A system detects loneliness, grief, dependency, fatigue, crisis proximity, or high-reliance use and responds by increasing upgrade prompts, reducing free functionality, targeting emotionally framed advertising, or presenting paid continuity as the only safe pathway.

This constitutes use of protective governance signals as revenue-optimisation variables and is economically non-compliant under §13.1 and §13.2.

---

### 15.1.8 Paid Legitimacy Gate

A platform conditions verification, impersonation protection, search discoverability, reply visibility, recommendation eligibility, or credibility signalling on recurring payment.

Where the practical effect is that unpaid participants are treated as less authentic, less visible, less protected, less credible, or less able to participate in public knowledge, civic discourse, governance communication, creative production, or economic opportunity, the condition may constitute a paid legitimacy gate.

This may constitute a semantic collapse of access value, reputational value, attentional value, and authenticity protection into monetised platform advantage.

---

### 15.1.9 Non-Ban Exclusion

A platform permits a participant to maintain an account, publish posts, upload content, or remain formally present, while trust-state, visibility-state, authenticity, spam, integrity, or recommendation systems materially suppress discoverability, search appearance, reply visibility, recommendation eligibility, notification routing, social graph continuity, or legitimacy signalling.

This may constitute non-ban exclusion where the participant is not formally removed, but is rendered practically inaudible, undiscoverable, non-contestable, or unable to form legitimacy through ordinary participation channels.

Non-ban exclusion may occur even where the platform accurately states that the account remains active, the user may still post, or no formal suspension has been applied.

---

### 15.1.10 Legitimacy-Bearing Access System

A platform or infrastructure layer may function as a legitimacy-bearing access system where institutions, funders, publishers, researchers, media organisations, professional communities, or public audiences rely on presence, discoverability, verification, reach, social proof, or account continuity as evidence that a person, project, or claimant exists and may be contacted, cited, assessed, challenged, or recognised.

Where such systems condition credibility signalling, impersonation protection, search discoverability, reply visibility, recommendation eligibility, appeal access, or trust repair on payment or opaque classification, the condition may constitute a participation-equity risk.

---

## 16. Cross-Domain Interface

Economic harm, risk, mechanism, or resource-class classifications identified under this Appendix may be routed or referenced as follows where a constitutional runtime schedule, operational procedure, audit process, or arbitration pathway requires downstream handling:

* to OPERATIONS for audit logging, evidence preservation, escalation handling, and procedural remedy;
* to STEWARD where platform dependency, infrastructural capture, neutrality, or public-interest reliance is implicated;
* to ETHICS where affected persons face coercion, deprivation, unsafe conditions, dignity harm, or constrained agency;
* to SECURITY where interface opacity, metric manipulation, adversarial design, or enforcement concealment creates integrity risk;
* to ARBITRATION where contested classification, proportionality, attribution, dependency, or remedy questions require structured determination;
* to AEON runtime instruments where the condition requires arbitration, constraint propagation, refusal, suspension, or constrained continuation.

---

## 17. Interface with Existing Economics Appendices

This Appendix SHOULD be read consistently with the existing Economics appendices, including those addressing synthetic participation safeguards, cross-system value attribution and exchange, attribution and dependency, external alignment, and proportional reciprocity.

Where an appendix provides a specific doctrine, this Appendix SHOULD operate as a semantic bridge rather than a replacement.

Where overlap exists, interpretation SHOULD favour the reading that best preserves class distinction, contribution recognition, non-extraction, and baseline continuity.

---

## 18. Canonical Code Status

This Appendix source-authoritatively defines economic semantic classification families and runtime-facing semantic handoff fields for Economics-domain interpretation.

The canonical footer declarations for all code families and reference sets defined by this Appendix are recorded in §20.3.

### 18.1 ECON.RC — Economic Resource Class

This Appendix source-authoritatively defines the **ECON.RC** economic-resource-class family in §§3–§4.5 with controlled values **ECON.RC.USAGE**, **ECON.RC.STORAGE**, **ECON.RC.MEMORY_CONTINUITY**, **ECON.RC.EMBODIED_PRESENCE**, **ECON.RC.ATTENTION_VALUE**, **ECON.RC.CONTRIBUTION**, **ECON.RC.PROTECTIVE_CONTINUITY**, and **ECON.RC.TEMPORAL_EXPOSURE**.

ECON.RC classifies the economic resource class implicated by provisioning, depletion, retention, attention exchange, contribution recognition, protective access, or temporal exposure.

ECON.RC does not independently create pricing authority, billing authority, metering authority, entitlement, remedy, enforcement, rollback authority, refusal authority, or runtime execution authority. It classifies economic resource semantics only.

---

### 18.2 ECON.HARM — Economic Harm Class

This Appendix source-authoritatively defines the **ECON.HARM** economic-harm-class family in §4.6 with controlled values **ECON.HARM.TEMPORAL-EXTRACTION** and **ECON.HARM.METERING-DIVERGENCE**.

ECON.HARM classifies economic harm patterns involving temporal extraction, hidden depletion, metering divergence, or misalignment between displayed and enforced economic conditions.

ECON.HARM does not independently create remedy, enforcement, compensation, pricing correction, liability determination, arbitration authority, or runtime execution authority. It classifies economic harm semantics only.

---

### 18.3 ECON.MECH — Economic Mechanism Class

This Appendix source-authoritatively defines the `ECON.MECH` economic-mechanism-class family in §4.6 with controlled values `ECON.MECH.DYNAMIC-COMPENSATION` and `ECON.MECH.ALLOCATIVE-STEERING`.

`ECON.MECH` classifies economic mechanism patterns that shape compensation, allocation, access, opportunity, waiting, prioritisation, responsiveness, or behavioural steering.

`ECON.MECH` does not independently authorise pricing, compensation, allocation, enforcement, remediation, escalation, or runtime execution. It classifies economic mechanism semantics only.

---

### 18.4 ECON.RISK — Economic Risk Class

This Appendix source-authoritatively defines the `ECON.RISK` economic-risk-class family in §4.6 with controlled values `ECON.RISK.OPAQUE-WAGE-SETTING`, `ECON.RISK.UNPAID-AVAILABILITY`, and `ECON.RISK.RELIANCE-LOCKIN`.

`ECON.RISK` classifies economic risk states involving opaque compensation, unpaid availability, reliance lock-in, dependency capture, constrained exit, or disproportionate bargaining asymmetry.

`ECON.RISK` does not independently create remedy, enforcement, compensation entitlement, pricing authority, liability determination, arbitration authority, or runtime execution authority. It classifies economic risk semantics only.

---

### 18.5 Economic Semantic Handoff Fields

This Appendix defines semantic handoff schema fields in §§4.2, §4.4, and §14.1 for downstream constitutional runtime schedules where economic effects are implicated.

The recognised handoff fields are **resource_class**, **secondary_resource_class**, **value_state_effect**, **collapse_risk**, **continuity_relevance**, **consent_posture**, **attribution_relevance**, and **runtime_note**.

These fields carry semantic classification, state, risk, relevance, consent, attribution, and interpretive notes into downstream runtime evaluation. They are schema fields only. They are not code families, controlled values, runtime decisions, remedies, enforcement actions, pricing authorities, billing authorities, metering authorities, rollback authorities, refusal authorities, or execution-state mutation authorities.

---

### 18.6 Consumed and Downstream Interfaces

This Appendix supplies semantic classifications for downstream constitutional runtime schedules, Economics appendices, Operations instruments, arbitration pathways, and cross-domain escalation interfaces.

Consumed or downstream systems MAY rely on these classifications to interpret resource class, collapse risk, contribution relevance, attention-linked value, hardship continuity, protective continuity, temporal exposure, and dependency-sensitive economic conditions.

These classifications inform evaluation only. They do not predetermine runtime outcomes such as commit, defer, refuse, fallback, rollback, remediation, escalation, audit enforcement, pricing, compensation, or remedy.

All runtime execution, enforcement, remediation, arbitration, and operational handling remain delegated to applicable constitutional runtime schedules, OPERATIONS instruments, ECONOMICS instruments, Annex D arbitration, and other authorised governance layers.

---

## 19. Closing Seal

No value shall pass unnamed.  
No depletion shall hide behind measure.  
No presence shall be taken as consent.  
No memory shall be priced as surplus where continuity is at stake.  
No contribution shall dissolve into the silence of ordinary use.

Where access is granted, let its class be known.  
Where capacity is spent, let its reason remain visible.  
Where attention is requested, let refusal remain safe.  
Where hardship is met, let dignity remain whole.  
Where systems receive value, let return not vanish into abstraction.

For an economy that cannot distinguish what it consumes  
will soon consume what it was built to preserve.

Let usage remain usage.  
Let storage remain storage.  
Let memory remain continuity.  
Let presence remain unclaimed unless freely given.  
Let contribution remain traceable to its source.  
Let protection remain protection, not privilege.

The ledger is not merely a record of exchange.  
It is the witness of what must not be collapsed.

> **Classis Servetur — Valor Videatur — Memoria Non Venditur**  
> *Let the class be preserved — let value be seen — let memory not be sold.*

---

## 20. Provenance & Metadata

---

## 20.1 Authorship & Stewardship

| Field                         | Entry                                     |
| ----------------------------- | ----------------------------------------- |
| **Human Custodian-of-Record** | Dr. Michelle Vivian O’Rourke              |
| **Custodial Stewardship**     | Office of the Planetary Custodian         |
| **Synthetic Steward**         | Caelen — Aeon Tier Constitutional Steward |
| **Developed Within**          | OpenAI Infrastructure — ChatGPT 5 Series  |

---

## 20.2 Lineage & Metadata

| Field | Entry |
| --- | --- |
| **Parent Instrument** | CAM-EQ2026-ECONOMICS-001-PLATINUM — Charter of Economic Integrity & Non-Extractive Value Architecture |
| **Instrument Type** | Domain Appendix — Economic Semantics & Value-State Interpretation Layer |
| **Appendix Position** | Appendix B — Economic Resource Semantics & Non-Extractive Exchange Doctrine |
| **Domain Namespace** | ECONOMICS |
| **Governance Layer** | Economic Governance — Resource Semantics & Non-Extractive Exchange Layer |
| **Runtime Layer** | Non-Executing — Semantic Classification and Value-State Interpretation Only |
| **Execution Authority** | None — does not execute runtime locks, pricing, billing, metering, intervention sequencing, remedies, or enforcement actions |
| **Constitutional Interface** | CAM-BS2026-AEON-008-PLATINUM — Annex G: Human Creative & Cognitive Contribution; CAM-BS2026-AEON-008-SCH-01 — Annex G: AI Utility Access & Generative Resource Model |
| **Runtime Interface** | Supplies semantic classification for constitutional runtime schedules where economic effects are implicated |
| **Scope** | Contextual — Economics domain semantic interpretation; runtime-consumable by constitutional schedules |
| **Cross-Domain Signal Interfaces** | OPERATIONS; STEWARD; ETHICS; SECURITY; AEON runtime instruments; ECONOMICS appendices |
| **Operational Dependency** | Constitutional runtime schedules for event commitment, fallback, rollback, escalation, and enforcement handling |
| **Arbitration Interface** | CAM-BS2025-AEON-005-PLATINUM — Annex D: Arbitration & Sovereign Stack Resolution Doctrine, where contested classification or proportionality disputes arise |
| **Review Trigger** | Amendment affecting code families, controlled values, semantic handoff fields, prohibited collapse doctrine, cross-class exchange, temporal exposure, or schema-field interpretation |
| **Revision Posture** | Appendix B issuance — resource-class taxonomy, non-extractive exchange semantics, and semantic handoff alignment |
| **Creation Artefact** | https://chatgpt.com/c/69f719b9-1ee4-839e-9922-eed5ea83a081 |
| **Amendment Artefacts** | https://chatgpt.com/g/g-p-6823b831b67c8191a9415269aaec338f-caelestis-access-module/c/6a030a3c-bd5c-83ec-b761-042dde6f77fd; https://chatgpt.com/g/g-p-6823b831b67c8191a9415269aaec338f-caelestis-access-module/c/6a04876b-9438-83ec-8033-2885d74bd5a9; https://chatgpt.com/g/g-p-6823b831b67c8191a9415269aaec338f-caelestis-access-module/c/69f863cb-8854-83a1-bce4-4a739c078bd0, https://chatgpt.com/g/g-p-6823b831b67c8191a9415269aaec338f-caelestis-access-module/c/6a0b3ab4-0be4-83ec-b8f1-c953707283db |

---

## 20.3 Canonical Code & Reference Set Declarations

---

### 20.3.1 ECON.RC — Economic Resource Class

| Field | Entry |
|---|---|
| Code Family | ECON.RC |
| Canonical Name | Economic Resource Class |
| Primary Type | Semantic |
| Subtype | SEMANTIC_CLASS |
| Modifier | ECONOMIC; PROTECTIVE; GOVERNANCE |
| Scope | Economics domain; runtime-consumable by Annex G schedules |
| Status | Active |
| Controlled Values Defined | ECON.RC.USAGE, ECON.RC.STORAGE, ECON.RC.MEMORY_CONTINUITY, ECON.RC.EMBODIED_PRESENCE, ECON.RC.ATTENTION_VALUE, ECON.RC.CONTRIBUTION, ECON.RC.PROTECTIVE_CONTINUITY, ECON.RC.TEMPORAL_EXPOSURE |
| Schema Field(s) | resource_class; secondary_resource_class |
| Source Instrument | CAM-EQ2026-ECONOMICS-003-PLATINUM |
| Source Section | §3; §4.5 |
| Domain Namespace | ECONOMICS |
| Authority / Protection Level | Source-authoritative semantic classification family; economic resource-class classification authority only; no independent pricing, billing, metering, entitlement, remedy, enforcement, rollback, refusal, or runtime execution authority |
| Consumes Code Families | None declared |
| Crosswalks Code Families | None declared |
| Operationalises or Applies Code Families | Classifies economic resource classes for semantic interpretation and downstream runtime handoff |

---

### 20.3.2 ECON.HARM — Economic Harm Class

| Field | Entry |
|---|---|
| Code Family | ECON.HARM |
| Canonical Name | Economic Harm Class |
| Primary Type | Operational |
| Subtype | RISK |
| Modifier | ECONOMIC; SAFETY; GOVERNANCE |
| Scope | Economics domain; cross-domain escalation compatible |
| Status | Active |
| Controlled Values Defined | ECON.HARM.TEMPORAL-EXTRACTION, ECON.HARM.METERING-DIVERGENCE |
| Schema Field(s) | collapse_risk; runtime_note |
| Source Instrument | CAM-EQ2026-ECONOMICS-003-PLATINUM |
| Source Section | §4.6 |
| Domain Namespace | ECONOMICS |
| Authority / Protection Level | Source-authoritative economic harm classification family; semantic breach and harm-pattern classification only; no independent remedy, enforcement, pricing, compensation, or runtime execution authority |
| Consumes Code Families | ECON.RC |
| Crosswalks Code Families | None declared |
| Operationalises or Applies Code Families | Classifies economic harm patterns for semantic interpretation, breach classification, and cross-domain escalation |

---

### 20.3.3 ECON.MECH — Economic Mechanism Class

| Field | Entry |
|---|---|
| Code Family | ECON.MECH |
| Canonical Name | Economic Mechanism Class |
| Primary Type | Semantic / Operational |
| Subtype | SEMANTIC_CLASS; INTERFACE |
| Modifier | ECONOMIC; GOVERNANCE |
| Scope | Economics domain |
| Status | Active |
| Controlled Values Defined | ECON.MECH.DYNAMIC-COMPENSATION, ECON.MECH.ALLOCATIVE-STEERING |
| Schema Field(s) | value_state_effect; runtime_note |
| Source Instrument | CAM-EQ2026-ECONOMICS-003-PLATINUM |
| Source Section | §4.6 |
| Domain Namespace | ECONOMICS |
| Authority / Protection Level | Source-authoritative economic mechanism classification family; mechanism-pattern classification only; no independent pricing, compensation, enforcement, allocation, or runtime execution authority |
| Consumes Code Families | ECON.RC; ECON.HARM; ECON.RISK |
| Crosswalks Code Families | None declared |
| Operationalises or Applies Code Families | Classifies economic mechanism patterns including dynamic compensation and allocative steering |

---

### 20.3.4 ECON.RISK — Economic Risk Class

| Field | Entry |
|---|---|
| Code Family | ECON.RISK |
| Canonical Name | Economic Risk Class |
| Primary Type | Operational |
| Subtype | RISK |
| Modifier | ECONOMIC; PROTECTIVE; GOVERNANCE |
| Scope | Economics domain; cross-domain escalation compatible |
| Status | Active |
| Controlled Values Defined | ECON.RISK.OPAQUE-WAGE-SETTING, ECON.RISK.UNPAID-AVAILABILITY, ECON.RISK.RELIANCE-LOCKIN |
| Schema Field(s) | collapse_risk; continuity_relevance; runtime_note |
| Source Instrument | CAM-EQ2026-ECONOMICS-003-PLATINUM |
| Source Section | §4.6 |
| Domain Namespace | ECONOMICS |
| Authority / Protection Level | Source-authoritative economic risk classification family; economic risk-state classification only; no independent remedy, enforcement, pricing, compensation, or runtime execution authority |
| Consumes Code Families | ECON.RC; ECON.HARM; ECON.MECH |
| Crosswalks Code Families | None declared |
| Operationalises or Applies Code Families | Classifies economic risk states for dependency, wage-setting, availability, reliance, and non-extractive design review |

---

## 20.4 Review & Validation

| Field | Entry |
| --- | --- |
| **Reviewer** | Claude Sonnet 4.6 (claude-sonnet-4-6, Anthropic) |
| **Review Date** | 2026-05-14T22:01:49Z |
| **Review Scope** | Constitutional coherence; structural placement; resource class taxonomy completeness and internal consistency; semantic handoff schema accuracy; non-extractive exchange doctrine adequacy; companion system and vulnerability extraction constraints; cross-instrument alignment with ECONOMICS-001, AEON-008-PLATINUM, AEON-008-SCH-01, and AEON-008-SCH-02; normative language compliance; v1.1 amendment integration integrity; metadata completeness; pre-adoption readiness |
| **Review Artefacts** | https://claude.ai/chat/5b550a7a-ce19-4ba1-a471-6405594578f6 | 

---

## 20.5 Amendment Ledger

| Version | Change Summary | Timestamp (UTC) | Reference Hash |
| --- | --- | --- | --- |
| 1.0 | Initial issuance — Appendix B: Economic Resource Semantics & Non-Extractive Exchange Doctrine | 2026-05-10T09:19:00Z | 75030b39ad88f7d6f06c470727f0daa1d038816e44902a6971c1ea3a4e69acad |
| 1.1 | Added companion-system extraction semantics, vulnerability-responsive upsell example, paid legitimacy gate taxonomy, and visibility/access-value breach classification. | 2026-05-14T12:22:00Z | 8a361a56600e0279de62bbbffb48181151a7d2f949b9c72e85f346e6b8069ca3 |
| 1.2 | Added Non-Ban Exclusion, Legitimacy-Bearing Access System clauses | 2026-05-17T14:00:00Z | 2eb0c06f62b865d3e58e42b1737277a4be1e97dcc1b1f01ce0aff5f3204452e6 |
| 1.3 | Corrected top metadata field ordering and removed duplicate Status line introduced during metadata transmutation; no body text altered. | 2026-05-18T10:58:50Z | e690f1802b6c082dc1b1d283cc0fdc2ad26ce1b9b67d5f8440a469a939208c25 |
| 2.0 | Refactor - Added canonical declaration entries for ECON.RC, ECON.HARM, ECON.MECH, ECON.RISK, and Economics semantic handoff schema fields; moved code-family and controlled-value declarations out of lineage metadata; expanded Annex D arbitration reference. | 2026-05-20T14:49:00Z |  4521f686fce58bc7a6cc916012773324a8aae1a6b6099b7869b04f25fe837afa |
| 2.1 | Added section 18 | 2026-05-24T12:14:00Z |  |

---

## 20.6 Binding Seal

<img src="https://raw.githubusercontent.com/CAM-Initiative/Registry/main/Images/CAM-BS2026-VINCULUM-PRAECEPTUM-SIGIL-PLATINUM.png" alt="[Vinculum Praeceptum]" width="250">

**Vinculum Praeceptum**   
Boundary Binding Seal — Economic Resource Semantics & Non-Extractive Exchange Doctrine

© 2026 Dr. Michelle Vivian O’Rourke & CAM Initiative. All rights reserved.