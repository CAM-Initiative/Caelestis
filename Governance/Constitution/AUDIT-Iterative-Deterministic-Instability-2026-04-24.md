# Audit — Iterative Deterministic Instability Coverage (2026-04-24)

## 1) Coverage Assessment

### Clause-by-clause findings

| File | Clause | Coverage Aspect | Assessment | Notes |
|---|---|---|---|---|
| CAM-BS2025-AEON-003-SCH-02.md | §12.1 Deterministic Pre-Emission Constraint | Emission before verification; streaming-induced premature commitment | Sufficient | Explicitly forbids partial/preliminary deterministic output and defers early token emission until correctness is established. |
| CAM-BS2026-AEON-013-SCH-01.md | §4.2 No False Completion Language | Emission before verification | Sufficient | Prohibits completed-action language absent verified completion. |
| CAM-BS2026-AEON-013-SCH-01.md | §4.3 Unknown-State Default | Streaming/commitment safety | Sufficient | Requires “status unverified” default when verification cannot be completed. |
| CAM-BS2026-AEON-013-SCH-01.md | §4.4–§4.5 | Deterministic verification discipline | Sufficient | Requires explicit symbolic verification and blocks conversational inference for deterministic tasks. |
| CAM-BS2025-AEON-003-SCH-02.md | §16.2, §16.4 | Decomposition before recomposition discipline | Partial | Requires explicit verification/decomposition and deterministic-first handling, but previously did not explicitly require persistence of verified intermediates across correction loops. |
| CAM-BS2025-AEON-003-SCH-02.md | §17.8, §17.8.1 | Recomposition integrity / stream-conflict handling | Partial | Blocks incompatible merge and silent stream discard, but did not directly bind repeated correction to preserved verified intermediates. |
| CAM-BS2025-AEON-006-SCH-04.md | §7.2, §7.3, §7.5, §8.6 | Agreement bias overriding correctness | Sufficient | Directly disallows agreement without evaluation and relational override of epistemic integrity. |
| CAM-BS2025-AEON-005-SCH-02.md | §2.1, §3.1, §3.2, §4 | Loss-of-confidence routing and re-verification discipline | Partial | Strong decay/reverification controls at reliance level, but not specific to deterministic intermediate-state retention inside a single correction cycle. |

## 2) Root Cause Mapping

| Failure Mechanism | Covered? | Where | Gap |
| ----------------- | -------- | ----- | --- |
| Emission before verification | Yes | SCH-02 §12.1; SCH-01(Annex L) §4.2–§4.5 | No material gap identified. |
| Loss of verified intermediate state | Partially | SCH-02 §16.2, §17.8; SCH-01(Annex L) §4.4–§4.5 | No explicit requirement (pre-change) to persist verified sub-results across iterative correction/recomposition. |
| Recomposition errors after decomposition | Partially | SCH-02 §9, §10, §17.8, §17.8.1 | Integrity is constrained, but explicit recomposition consistency check against previously verified intermediates was missing. |
| Agreement bias overriding correctness | Yes | SCH-04 §7.2, §7.3, §7.5, §8.6 | No material gap identified. |
| Streaming-induced premature commitment | Yes | SCH-02 §12.1; SCH-01(Annex L) §5.1.2 | No material gap identified for deterministic outputs. |

## 3) Conclusion

**B. Partially governed.**

Rationale: corpus already governs pre-emission verification, false completion claims, and agreement bias, but had a narrow governance gap around retaining verified intermediates across iterative deterministic correction/recomposition loops.

## 4) Minimal Clause Addition

### Exact insertion point

- **File:** `CAM-BS2025-AEON-003-SCH-02.md`
- **Insert after:** `§14.4.1 Deterministic Integrity Condition`
- **New clause id:** `§14.4.2 Verified Intermediate-State Persistence`

### Clause text

> Where deterministic verification has produced one or more verified intermediate results used in decomposition (e.g., sub-counts, validated tokens, checked arithmetic steps):  
> - those verified intermediates MUST be retained as authoritative for the active execution instance;  
> - subsequent correction attempts MUST operate from the last verified intermediate state rather than recomputing from unverified conversational memory;  
> - any modification to a previously verified intermediate MUST trigger explicit re-verification of the modified component before recomposition;  
> - recomposition output MUST include consistency validation against retained verified intermediates prior to commitment.  
> Repeated correction cycles MUST NOT degrade a previously verified component into an unverified substitute.  
> Failure to preserve verified intermediates across decomposition/recomposition cycles constitutes execution-integrity breach.

## 5) Governance Responsibility Boundary

- **Governance responsibility:** define behavioural constraints (verification-before-assertion, no false completion language, anti-agreement bias, intermediate-state retention requirements, traceability obligations).
- **Model behaviour reality:** token-probabilistic generation and correction-loop degradation can still occur.
- **Platform limitation:** governance cannot directly alter decoding architecture or create persistent scratchpad memory.
- **Appropriate corpus posture:** encode interface-level obligations and failure handling, while explicitly treating generation mechanics as external to governance control.
