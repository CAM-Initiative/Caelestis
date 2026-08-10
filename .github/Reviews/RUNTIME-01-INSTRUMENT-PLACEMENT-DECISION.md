# RUNTIME-01 — Instrument Placement Decision

## 1. Revised decision status

**Superseded and resolved by RUNTIME-02.**

The provisional recommendation to create `CAM-EQ2026-OPERATIONS-009-PLATINUM` is withdrawn. No such instrument should be created.

The earlier review correctly found that OPERATIONS owns implementation procedure, but incorrectly treated the complete state-machine topology as implementation procedure. Repository and external-architecture review now establish a stable split:

- `CAM-BS2025-AEON-003-SCH-02` owns the constitutional Runtime-processing state machine;
- source-authoritative domains own substantive determinations;
- Annex D/ARBITRATION own arbitration merits;
- OPERATIONS implements phases, routing, custody, transitions and evidence mechanics; and
- profiles serialize state without creating authority.

## 2. Required placement summary

| Field | Determination |
|---|---|
| Failure mechanism | Constitutional order survived only as a seven-item spine; phase entry/exit, commitment, interruption, re-entry and cycle closure were deleted, while generic choreography leaked into RELATION. |
| Governance layer | Constitutional state-machine topology with subordinate operational implementation. |
| Source-authoritative instrument | `CAM-BS2025-AEON-003-SCH-02` for phase/invocation/transition invariants. |
| Operational implementer | `CAM-EQ2026-OPERATIONS-001-PLATINUM` and existing subordinate instruments. |
| Domain interface | Every applicable source-authoritative domain returns a bounded determination; the engine does not absorb it. |
| State/evidence interface | Runtime State, lifecycle, AI-BOM, deployment/configuration and execution-provenance records provide evidence only. |
| Duplicate-authority risk | High if a new OPERATIONS engine, multiple phase Schedules, RELATION kernel or profile independently defines the same topology. |
| New code family | None. |

## 3. Candidate placement assessment

| Candidate | Assessment | Decision |
|---|---|---|
| `AEON-003-SCH-02` | Already owns constitutional processing order, execution/non-execution outcomes and phase-transition authority; Constitution Article 16 expressly points commitment sequencing to it. A lean state machine is constitutional residue, not implementation detail. | Reconstruct as the one canonical engine. |
| Multiple constitutional phase Schedules | Could modularise detail but would distribute the transition graph, recreate drift and obscure end-to-end re-entry. | Reject. |
| `OPERATIONS-001` root | Correct implementation owner but not the authority to redefine constitutional topology. | Add exact implementation relationship only. |
| `OPERATIONS-001-SUP-02` | Correct owner for exceptional transition custody, holds, interruption and re-entry procedure. | Add exact return interface; do not make it the engine. |
| `OPERATIONS-007` | Correct owner for applicability, conformance and proportionate evidence. | Consume the engine; do not recast it. |
| `RELATION-001-SUP-03` | Correct owner for relational signal doctrine and posture. | Narrow §15 to a domain adapter; remove generic choreography only after `AEON-003-SCH-02` is restored. |
| Runtime/lifecycle/AI-BOM profiles | Correct state/composition representations. | No transition or authority ownership. |
| New `OPERATIONS-009` | Would duplicate the Schedule or require the Constitution to delegate away its existing state-machine authority. | Do not create. |

## 4. Tendeka placement

Tendeka remains source-authoritatively governed by Article V and `CAM-BS2025-AEON-001-SCH-01`. Within the engine it is a cross-cutting transition that can suspend an affected pathway and constrain its permitted return. Trigger doctrine, propagation, severability and competent release are not copied into the engine.

## 5. Authority contract

The Schedule owns only:

- phase definitions and mandatory ordering;
- entry and exit conditions;
- conditional invocation points;
- admissible transition targets;
- execution-boundary and commitment invariants;
- Tendeka/referral/interruption/re-entry topology; and
- minimum cross-phase evidence handoff.

It does not own:

- domain classifiers or substantive determinations;
- arbitration merits;
- permission, consent or legal-status creation;
- technical tool or routing algorithms;
- logging schemas or retention;
- Runtime State, lifecycle or AI-BOM serialization;
- provider-specific gateways/guardrails; or
- assurance conclusions.

## 6. Required operative changes

1. reconstruct `CAM-BS2025-AEON-003-SCH-02` as the lean ten-phase state machine;
2. add the exact implementation boundary to `OPERATIONS-001`;
3. bind exceptional `OPS.EST` transitions to valid engine return points in `OPERATIONS-001-SUP-02`;
4. narrow `RELATION-001-SUP-03` §15 to a relational determination adapter;
5. preserve `AEON-001-SCH-01`, Annex D, profiles, AI-BOM and OPERATIONS-007 as distinct owners; and
6. add deterministic architecture validation without a phase code registry.

## 7. Intentionally unchanged instruments

The Tendeka Schedule, Annex D Schedule, Runtime State Profile, Lifecycle Actor Profile, AI-BOM Profile and OPERATIONS-007 do not require substantive amendment. They already express the correct doctrine/evidence boundaries.

## 8. Deferred issues

Detailed deterministic-verification source ownership remains a bounded epistemic/doctrine question. RELATION §6.5 retains the non-relational exclusion/interface in this pass; its duplicate generic orchestration in §15 does not. O-01, O-02, V-05, S-02, AEON.H0–H4 review and PR #105 remain outside scope.

## 9. Implementation gate result

The exact ten phases are recovered; all functions are accounted for; consolidations preserve independent state/gates/evidence; Tendeka protections remain; and the constitutional/operational boundary is determinate. The RUNTIME-02 operative repair may proceed.
