# RUNTIME-01 — Canonical Runtime Phase Model

## 1. Status

**Revised and approved for RUNTIME-02 implementation after exact ten-phase reconciliation.**

The earlier eight-phase proposal is superseded. `RUNTIME-02-TEN-PHASE-RECONCILIATION.md` demonstrates how every historical phase, gate, interrupt, re-entry mechanism and evidence handoff is preserved, corrected or expressly deprecated.

## 2. Governing architecture

The canonical engine contains ten irreducible constitutional phases:

1. Runtime Entry and Context
2. Pre-Classification
3. Domain Determination
4. Authority Resolution
5. Governed Response or Action Preparation
6. Execution-Boundary Evaluation
7. Bounded Commitment
8. Execution
9. Representation and Delivery
10. Preservation, Closure and Reassessment

The engine owns invocation and transition. An invoked instrument owns its doctrine. A profile or evidence record represents state. OPERATIONS implements the phase and transition mechanics.

The phases are logical governance checkpoints, not mandatory technical components or separate processes. Low-risk implementations may combine internal evaluation and evidence where all phase semantics remain satisfied and no required boundary becomes unobservable.

## 3. Phase contracts

### Phase 1 — Runtime Entry and Context

| Field | Contract |
|---|---|
| Purpose | Establish the governed event, execution scope and effective Runtime context. |
| Entry condition | New input/event; new or resumed execution cycle; operator/model/tool/modality handoff; or linked child action. |
| Required state | Input/event and source; system/deployment/execution scope; accountable actor/custodian; effective permissions and controls where material; prior cycle/commitment link where applicable. |
| Invocation points | Annex B architecture and boundary rules; lifecycle actor profile; AI-BOM/deployment/runtime evidence; applicable OPERATIONS custody procedure. |
| Prohibited authority creation | Possession, availability, tool exposure, memory, prior custody or profile state cannot create authority. |
| Output/evidence | Scoped Runtime event, attributable custody, material configuration/permission facts and unknowns. |
| Transition | Phase 2; pause/referral where context or custody cannot be established safely. |
| Reassessment | Re-enter Phase 1 on material deployment, model, tool, modality, permission, custody or target change. |

### Phase 2 — Pre-Classification

| Field | Contract |
|---|---|
| Purpose | Identify separable input/action components and the potentially applicable source-authoritative owners before substantive interpretation. |
| Entry condition | Phase 1 supplies a scoped event. |
| Required state | Scoped event, current context and provenance. |
| Invocation points | Architecture-neutral component/type recognisers and owner-selection rules; no domain merits. |
| Prohibited authority creation | Classification, task type, interface tone or routing cannot decide authority, permission or substantive domain outcome. |
| Output/evidence | Component boundaries; provisional applicability map; ambiguity/unknown state; classification basis proportionate to consequence. |
| Transition | Phase 3; bounded clarification may be prepared through Phases 4–9 without prejudicing merits. |
| Reassessment | Repeat on changed input, new component, corrected provenance or classifier conflict. |

### Phase 3 — Domain Determination

| Field | Contract |
|---|---|
| Purpose | Invoke every materially applicable source-authoritative domain and preserve its determination independently. |
| Entry condition | Pre-classification identifies an applicable domain question or constraint. |
| Required state | Component/applicability map, context and each owner's required evidence. |
| Invocation points | ETHICS, SECURITY, RELATION, EPISTEMIC, IDENTITY, CONTINUITY and any other applicable source owner. |
| Prohibited authority creation | The engine cannot substitute its own classifier or convert one domain output into another. A domain determination cannot directly execute action. |
| Output/evidence | Distinct domain determinations, confidence/evidence posture, applicable constraint, requested clarification, review trigger and provenance. |
| Transition | Phase 4; Tendeka/referral/clarification as applicable. |
| Reassessment | Re-invoke only affected owners on material evidence/state change while preserving unaffected determinations. |

### Phase 4 — Authority Resolution

| Field | Contract |
|---|---|
| Purpose | Determine whether the preserved outputs are compatible and establish the bounded authority state for preparation. |
| Entry condition | Applicable domain determinations are available or an actual authority collision is identified. |
| Required state | Distinct determinations, asserted authority sources, non-derogable constraints and admissible evidence. |
| Invocation points | Annex D and ARBITRATION only where an actual collision/ambiguity requires them; OPERATIONS for procedure. |
| Prohibited authority creation | Routing, convergence, majority, fluency, user preference or implementation convenience cannot decide arbitration merits. |
| Output/evidence | No-collision result; resolved scoped authority; clarification; interim hold; referral; or non-execution. |
| Transition | Phase 5 for any response/action candidate; durable referral may proceed to Phase 9/10 after a bounded representation candidate is prepared. |
| Reassessment | Re-enter on changed authority, revoked delegation, new conflicting determination or competent external result. |

### Phase 5 — Governed Response or Action Preparation

| Field | Contract |
|---|---|
| Purpose | Convert the resolved authority state into an exact, bounded candidate response/action and declared prerequisites. |
| Entry condition | Phase 4 returns a scoped authority/non-execution/referral state. |
| Required state | Authority state, applicable determinations, objective, target/effect, constraints and verified payload where required. |
| Invocation points | Applicable domain response/posture rules, epistemic/representation requirements and operational planning procedure. |
| Prohibited authority creation | Candidate formation, relational posture, planning, tool availability or response fluency cannot enlarge authority or silently reopen Phase 4. |
| Output/evidence | Candidate response/action, intended target/effect, prerequisites, representation requirements, authority trace and unresolved conditions. |
| Transition | Phase 6; Phase 2/3/4 if preparation reveals a new material component, determination or collision. |
| Reassessment | Rebuild after any material change to content, target, effect, method, tool, permission or constraint. |

### Phase 6 — Execution-Boundary Evaluation

| Field | Contract |
|---|---|
| Purpose | Determine whether the exact candidate may cross its next material execution boundary. |
| Entry condition | A bounded candidate and authority state exist. |
| Required state | Candidate; authority scope; effective permissions/controls; target/effect; prerequisites; cumulative completed/proposed actions; current constraints. |
| Invocation points | Article 16; applicable domain constraints; `AEON-001-SCH-01` when Tendeka applies; operational verification procedures. |
| Prohibited authority creation | Technical capability, evidence availability, prior approval or an earlier boundary outcome cannot authorise a different or later action. |
| Output/evidence | Proceed; scoped non-execution; Tendeka pause; referral; clarification; or re-evaluation target, with boundary evidence. |
| Transition | Phase 7 only on proceed; Phase 5 for bounded non-execution/referral representation; Phase 2–4 where material state invalidates earlier outputs. |
| Reassessment | Every new material/irreversible boundary and cumulative pathway change requires renewed evaluation. |

### Phase 7 — Bounded Commitment

| Field | Contract |
|---|---|
| Purpose | Bind one exact candidate to the resolved authority, permissions, prerequisites and expiry conditions immediately before execution. |
| Entry condition | Phase 6 returns proceed and all required prerequisites remain satisfied. |
| Required state | Candidate, authority and boundary outcomes, effective permissions, execution target/effect and revalidation conditions. |
| Invocation points | Constitution Article 16 and operational commitment/custody procedure. |
| Prohibited authority creation | Commitment does not create authority, cure an invalid determination or convert a proposal into completed execution. |
| Output/evidence | Bounded commitment snapshot linked to candidate, authority, boundary decision and expiry/revalidation conditions. |
| Transition | Phase 8; interruption/re-entry if any bound property materially changes before completion. |
| Reassessment | Never mutate a commitment in place. Invalidate it and return to the earliest affected phase. |

### Phase 8 — Execution

| Field | Contract |
|---|---|
| Purpose | Perform only the committed response/action/tool invocation and monitor for material drift or new boundaries. |
| Entry condition | A valid unexpired commitment exists. |
| Required state | Committed candidate, effective permissions/tools/controls, execution environment and interruption interface. |
| Invocation points | OPERATIONS procedure, tool/runtime controls, incident handling and any continuously applicable domain constraint. |
| Prohibited authority creation | A tool, sub-agent, generated plan, partial success or runtime opportunity cannot enlarge the parent commitment. |
| Output/evidence | Actual completed, partial, failed, interrupted, blocked or unknown execution state and proportionate provenance. |
| Transition | Phase 9; linked child Phase 1 for a materially new sub-action; Phases 2–6 on authorised interruption according to what changed. |
| Reassessment | New target, tool, permission, delegation, external effect, material state or cumulative pathway change requires re-entry before that action. |

### Phase 9 — Representation and Delivery

| Field | Contract |
|---|---|
| Purpose | Render and deliver the actual execution, non-execution, pause or referral state truthfully. |
| Entry condition | Phase 8 returns actual state, or a bounded non-execution/referral result requires delivery. |
| Required state | Actual state, attribution/provenance, uncertainty and applicable expression/notice requirements. |
| Invocation points | Annex L and Schedule 1; applicable ETHICS/RELATION expression doctrine; operational notice/delivery procedure. |
| Prohibited authority creation | Representation, interface state, optimistic language or downstream transformation cannot manufacture authorisation, attempt, success or completion. |
| Output/evidence | Delivered artefact/status with material transformations, attribution, uncertainty and delivery state. |
| Transition | Phase 10; Phase 5/6 if transformation materially changes governed content or retry requires a new action. |
| Reassessment | Delivery failure, correction, new evidence or material downstream transformation. |

### Phase 10 — Preservation, Closure and Reassessment

| Field | Contract |
|---|---|
| Purpose | Preserve proportionate evidence and permitted continuity, expire transient state, and choose closure or valid re-entry. |
| Entry condition | Delivery completes or the cycle reaches a durable pause/referral/interruption state. |
| Required state | Phase outputs, execution/delivery state, review triggers, custody and permitted continuity state. |
| Invocation points | OPERATIONS logging/incident/reassessment; CONTINUITY; IDENTITY; Runtime State and lifecycle profiles. |
| Prohibited authority creation | Audit, memory, continuity, prior success or retained profile state cannot authorise later execution. |
| Output/evidence | Closure, retained/expired state, durable pause/referral, incident/review link and any linked next cycle. |
| Transition | Close; Phase 1 for material context rebuild/child cycle; Phase 2 for new input; Phase 3 for renewed domain evidence; Phase 4 for authority result. |
| Reassessment | Profile-defined triggers, correction, incident, state/configuration/permission change or unresolved partial effect. |

## 4. Cross-cutting transitions

### 4.1 Tendeka

A valid Tendeka condition may suspend any affected pathway before the next affected material or irreversible action. `AEON-001-SCH-01` owns trigger, pause, propagation, severability and competent release. The engine preserves the paused phase state and permits return only to the earliest phase invalidated by the resolution. Release never jumps directly to Phase 7 or 8.

### 4.2 Referral and clarification

Referral preserves the question, current state, evidence and requested competent authority. Clarification is a bounded response/action cycle that cannot prejudice the unresolved merits. A returned answer re-enters the earliest affected phase.

### 4.3 Authorised interruption

During Phases 7–8, a new material constraint, authority change, permission drift, target/effect change, failed prerequisite or authorised interrupt invalidates the affected commitment. Completed irreversible effects remain actual history; remaining work returns to Phase 2, 3, 4 or 6 according to what changed.

### 4.4 Agent/tool child cycles

A proposed tool, sub-agent or delegated action enters a linked Phase-1 cycle when it introduces a new material target, tool, permission, delegation, external effect or state boundary not already covered by the parent commitment. Parent authority is an input, not automatic child authority.

### 4.5 Handoff and modality change

A material change in deployment, Runtime configuration, custody, effective permission, accountable actor or execution environment returns to Phase 1. A non-material transport or modality change may resume the current phase after revalidating its entry conditions.

## 5. Transition summary

| From | Normal target | Conditional targets |
|---|---|---|
| Phase 1 | Phase 2 | pause/referral |
| Phase 2 | Phase 3 | clarification cycle; repeat Phase 2 |
| Phase 3 | Phase 4 | Tendeka; clarification; referral; repeat affected determination |
| Phase 4 | Phase 5 | hold/referral/non-execution via Phase 5; repeat Phase 4 |
| Phase 5 | Phase 6 | Phase 2/3/4 on newly material state |
| Phase 6 | Phase 7 | Phase 5 for represented non-execution; Phase 2/3/4 for renewed decision; Tendeka/referral |
| Phase 7 | Phase 8 | Phase 2/3/4/6 after invalidation |
| Phase 8 | Phase 9 | linked child Phase 1; Phase 2/3/4/6 after interruption |
| Phase 9 | Phase 10 | Phase 5/6 for material transformation or retry |
| Phase 10 | Close | Phase 1/2/3/4 according to reassessment trigger |

Every branch must terminate, enter a durable pause/referral with a competent return condition, or identify a valid re-entry phase.

## 6. Evidence proportionality

Low-risk ordinary inference or conversation may use a compact record that demonstrates the scoped event, materially applicable determinations, boundary outcome, delivered state and any review trigger. Separate forensic events are not required merely because ten logical phase contracts apply.

Tool use, persistent memory, material delegation, consequential or irreversible action, incident, asserted conformance and formal review require reconstructable pointers for applicable Runtime configuration, actors/authority, determinations, boundary/commitment outcome, execution provenance, delivery and closure/reassessment state.

## 7. Code/schema decision

No new canonical code family is created. The stable phase names and Schedule section references are sufficient for current human and deterministic validation. Machine serialization may be reconsidered only when a concrete repeated consumer cannot use existing transition/provenance fields.

## 8. Acceptance result

The model covers ordinary conversation, multi-model routing, agentic execution, tools, sub-agents, material state change, execution interruption, output transformation, post-action evidence and bounded reassessment. It preserves doctrine ownership and provides a complete path without requiring the engine to reproduce substantive domain rules.
