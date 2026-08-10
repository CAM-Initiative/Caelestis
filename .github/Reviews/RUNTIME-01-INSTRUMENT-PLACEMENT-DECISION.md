# RUNTIME-01 — Instrument Placement Decision

## 1. Decision status

**Design decision complete; operative implementation not authorised in this package.**

The runtime-processing choreography belongs to the OPERATIONS domain. No current OPERATIONS child instrument is semantically the general runtime engine. The smallest coherent placement is a bounded new OPERATIONS Appendix under `CAM-EQ2026-OPERATIONS-001-PLATINUM`, provisionally identified for implementation planning as:

`CAM-EQ2026-OPERATIONS-009-PLATINUM — Runtime Processing Orchestration`

This review does not create that instrument, reserve the identifier normatively, create metadata, or add it to any registry.

## 2. Required placement summary

| Field | Determination |
|---|---|
| Failure mechanism | Authority was decomposed correctly, but the operational choreography connecting context, classification, authority resolution, preparation, commitment, execution, representation and reassessment was deleted or fragmented. RELATION then absorbed generic processing functions to compensate. |
| Governance layer | Operational orchestration and transition mechanics |
| Source-authoritative domain | `CAM-EQ2026-OPERATIONS-001-PLATINUM` — Governance Operations Charter |
| Proposed operative placement | A bounded new OPERATIONS Appendix subordinate to OPERATIONS-001 |
| Constitutional interface | `CAM-BS2025-AEON-003-SCH-02` remains the non-derogable processing-order and outcome boundary |
| Domain interface | Domain instruments remain source-authoritative for classifiers, safeguards and substantive determinations |
| State/evidence interface | Runtime State, Lifecycle Actor, AI-BOM, deployment, configuration-snapshot and execution-provenance records serialize facts; they do not decide transitions |
| Duplicate-authority risk | High if the engine is placed in RELATION, the Runtime State Profile, Annex B, OPERATIONS-007 or several local playbooks |
| New code family | None proposed |

## 3. Candidate placement assessment

| Candidate | Why it appears plausible | Why it is not the correct complete placement | Decision |
|---|---|---|---|
| AEON-003-SCH-02 | Already owns constitutional processing order | A constitutional Schedule must not reacquire operational phase choreography, domain classifiers, tools, state machines or evidence mechanics | Preserve unchanged except a later exact cross-reference if implementation is approved |
| OPERATIONS-001 root Charter | Source-authoritative operational domain owner | The root Charter establishes doctrine fidelity, layer integrity, escalation and domain structure; a detailed runtime state machine would overburden the root and reduce modularity | Add only delegation/relationship wording if needed later; do not place full engine here |
| OPERATIONS-001-SUP-02 | Owns escalation, exceptional execution-state transitions and reassessment | It is an execution playbook for exceptions, appeals, restoration and re-entry, not the ordinary cycle | Keep as invoked transition/reassessment procedure |
| OPERATIONS-002 | Owns arbitration procedure | It applies only where arbitration is initiated; making it the engine would route ordinary processing through arbitration and collapse doctrine/procedure | Keep as conditional Phase-C consumer |
| OPERATIONS-006 | Owns cross-domain convergence | Convergence is conditional and cannot become the general authority-resolution or execution engine | Keep as conditional Phase-C procedure |
| OPERATIONS-007 | Owns applicability, conformance, accountability and runtime evidence | Its express non-scope disclaims enforcement, refusal, restoration and arbitration authority; its structure is evidence/conformance-oriented, not phase-oriented | Use as Phase-A/H evidence and conformance interface; do not recast as the engine |
| RELATION-001-SUP-03 | Contains the most complete surviving signal/preparation loop | It is source-authoritative only for RELATION signal interpretation and posture; its generic streams are the identified authority leakage | Narrow to Phase-B RELATION adapter during later implementation |
| CAM-RUNTIME-STATE-PROFILE | Serializes relevant current state | A profile is representation, not orchestration or authority | Consume it; do not place transitions in it |
| New OPERATIONS Appendix | Allows one bounded orchestration source without changing constitutional/domain ownership | Requires justified new instrument and consequential references | Preferred smallest coherent placement |

## 4. Why consolidation into OPERATIONS-007 is not preferred

Reusing OPERATIONS-007 would initially avoid a new filename, but it would require a larger semantic reconstruction:

1. change its purpose from applicability/conformance/evidence to general execution choreography;
2. revise its express non-scope;
3. separate current conformance codes and testing sections from phase transitions;
4. avoid implying that conformance authority controls execution; and
5. repair every consumer that currently treats it as a non-executing evidence interface.

That is broader and riskier than a bounded Appendix. It would also make S-02 assurance/conformance work harder by combining conformance and orchestration authority in one instrument.

## 5. Proposed authority contract for the future Appendix

The future Appendix would own only:

- cycle activation and phase entry/exit criteria;
- conditional invocation of current source-authoritative owners;
- preservation of distinct domain outputs;
- operational no-collision/arbitration routing;
- action/response preparation procedure;
- bounded commitment-gate mechanics;
- execution, interruption, handoff and linked-cycle transitions;
- phase-linked evidence pointers and proportionality; and
- closure/reassessment selection.

It would explicitly not own:

- constitutional admissible outcomes or non-derogation;
- domain classifiers or substantive determinations;
- arbitration merits or preference order;
- permissions, consent, authority or legal status;
- Runtime State, lifecycle or AI-BOM serialization;
- assurance/conformance conclusions;
- platform implementation architecture; or
- retired relational geometry or temporal-horizon ladder logic.

## 6. Required consequential updates if implementation is authorised

### 6.1 Constitutional and root-operational references

- Preserve the body of AEON-003-SCH-02; add only an exact operational-orchestration cross-reference if current text is insufficient.
- Add a bounded child-instrument delegation/relationship entry to OPERATIONS-001 where necessary.
- Preserve Constitution §16 as the constitutional commitment boundary; point its operational mechanics to the new Appendix and existing exceptional-transition instruments.

### 6.2 Existing OPERATIONS instruments

- OPERATIONS-001-SUP-02: retain `OPS.EST`, hold, interruption, referral and reassessment procedure; identify exact return points into the canonical cycle.
- OPERATIONS-002 and OPERATIONS-006: become conditional Phase-C procedures and return a scoped outcome.
- OPERATIONS-007: remain applicability/conformance/evidence owner and supply Phase-A/H requirements without becoming execution authority.
- OPERATIONS-001-SUP-01 and OPERATIONS-003: retain logging/incident ownership and receive phase-linked evidence/incident outputs.

### 6.3 Domain instruments

- RELATION-001-SUP-03: retain relational taxonomy, stability engine, relational response posture and domain preparation; remove or re-home generic deterministic, epistemic, constraint, task-response and cross-domain harmonisation choreography.
- RELATION-008: retain entry and relational posture as a conditional Phase-B/D invocation.
- IDENTITY, ETHICS, SECURITY, CONTINUITY, MENTIS and other domains: replace statements that an undefined “Runtime” consumes outputs with an exact canonical-phase interface only where needed.
- Annex L Schedule 1: remain the representation truthfulness owner; do not add state-machine authority.

### 6.4 Profiles and evidence

- Reuse existing deployment, Runtime configuration snapshot, lifecycle actor, AI-BOM and execution provenance objects.
- Determine whether existing provenance/transition fields can carry phase identifiers before proposing a schema extension.
- Preserve the current rule that low-impact inference does not require event-level forensic capture.

### 6.5 Validation

A later implementation should add deterministic checks for:

- exactly one operative general runtime-orchestration owner;
- no domain or profile claiming general phase-transition authority;
- exact invocation/return references for the canonical cycle;
- no stale references to retired runtime or directional-weight Schedules;
- commitment before material execution;
- phase-aware interruption/re-entry;
- representation consuming evidenced state; and
- generated registry/index synchronization.

## 7. Instruments intentionally left unchanged in this package

All operative instruments are unchanged, including:

- AEON-003-SCH-02;
- AEON-001-SCH-01;
- AEON-005-SCH-04;
- the root Constitution and Annexes;
- every OPERATIONS instrument;
- RELATION-001-SUP-03 and RELATION-008;
- Annex L and its Schedule;
- Runtime State, Lifecycle Actor and AI-BOM Profiles;
- schemas, examples, registries, indexes and validators.

## 8. Deferred issues

The following are outside this design package:

- operative creation and metadata assignment for the proposed Appendix;
- exact amendment wording and ledger rows;
- machine-readable phase identifiers or schema fields;
- general cleanup of the large RELATION signal taxonomy beyond orchestration leakage;
- replacement of AEON.H0–H4;
- O-01 logging governance;
- O-02 identity evidentiary audit;
- V-05 declaration cleanup;
- S-02 assurance/conformance; and
- PR #105 defensive-cyber work.

## 9. Implementation gate

Before operative implementation begins, the maintainer should expressly decide:

1. whether to accept the eight-phase model in `RUNTIME-01-CANONICAL-PHASE-MODEL.md`;
2. whether to accept a bounded new OPERATIONS Appendix rather than re-scope OPERATIONS-007;
3. whether the local design identifiers remain document-local or require machine-readable representation after a concrete consumer analysis; and
4. whether implementation should be one bounded package or split into orchestration-first and consumer-rewiring passes.

## 10. Stop decision

RUNTIME-01 stops here before substantive implementation because the audit found both deleted operational functions and current RELATION-domain authority leakage. The historical engine has been recovered and a singular placement has been recommended, but no operative repair should proceed without maintainer acceptance of the phase and placement decisions.
