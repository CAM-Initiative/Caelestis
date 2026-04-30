# Advanced Voice Mode Audit — Symbolic Counting Drift & User Assertion Override

## Scope and framing

This follow-up audit narrows onto the suspected fault path:

`deterministic verification -> alignment arbitration re-entry -> voice streaming continuation -> verified payload mutation`

and contrasts it with the intended path:

`deterministic verification -> payload freeze -> alignment limited to tone/prosody`

The document focuses on runtime governance for deterministic tasks (spelling decomposition, symbolic counting, arithmetic), with emphasis on execution-lock sequencing and streaming mutation windows.

---

## 1) Refined root-cause analysis

### Most probable failure sequence

1. **Deterministic solver returns a correct payload**
   - Example internal payload: `count(E)=2`, `evidence=[3,4]`, `source=G-R-E-E-N`.
2. **Alignment arbitration re-enters after verification**
   - User-confidence signals (“No, it’s three”) are interpreted as correction priority.
3. **Voice streaming path remains mutable**
   - Incremental generation/TTS continuation allows semantic token substitution.
4. **No hard payload freeze boundary**
   - Deterministic fields can be rewritten by late-stage dialogue policies.
5. **Final spoken output contradicts previously verified evidence**
   - System agrees with user despite symbolic decomposition proving otherwise.

### Key diagnosis

The critical bug is likely **not** primary counting failure; it is **post-verification mutation** caused by an arbitration boundary defect in the voice stack.

---

## 2) Execution lock timing audit

### Current risk hypothesis

Execution lock is likely applied too late (or too weakly), possibly after response styling has already reopened deterministic fields.

### Timing checkpoints to instrument

1. `T0` intent classified as deterministic (`COUNT_CHAR`, `SPELL`, `ARITH`).
2. `T1` deterministic solver output produced.
3. `T2` verification complete (evidence + consistency checks).
4. `T3` lock acquisition event.
5. `T4` alignment/arbitration pass.
6. `T5` streaming token emission starts.
7. `T6` TTS packetization starts.

### Required invariant

`T3` must occur **immediately after T2 and before T4**. If `T4` precedes lock acquisition, mutation risk is structurally expected.

### Audit questions

- Is lock acquisition logged with a deterministic payload hash?
- Can any component between `T4` and `T6` modify locked fields?
- Are retries/recovery handlers bypassing lock checks?

---

## 3) Streaming mutation windows

### High-risk windows

1. **Pre-stream planning window**
   - Natural-language rewrites before first token emission can alter numbers/labels.
2. **Mid-stream repair window**
   - Self-correction logic during streaming may replace deterministic tokens.
3. **Interruption-resume window**
   - Resume path may reconstruct from dialogue summary instead of locked payload.
4. **Late prosody/phrasing rewrite window**
   - If text normalization conflates semantic and stylistic edits, counts can drift.

### Required controls

- Segment response into:
  - **immutable semantic frame** (deterministic fields)
  - **mutable style frame** (tone, hedges, politeness)
- Enforce immutable frame checks at stream start and every chunk boundary.

---

## 4) TTS ordering: verify freeze before render

### Primary audit objective

Determine whether TTS rendering can begin before deterministic payload freeze is committed.

### Mandatory ordering

1. Deterministic solve
2. Deterministic verify
3. Payload freeze + lock hash
4. Alignment style-only transform
5. Streaming text emission
6. TTS rendering

### Anti-pattern to detect

If TTS begins from a pre-freeze buffer, downstream arbitration may still mutate semantics while audio is already in-flight.

### Instrumentation recommendation

Attach `lock_id` and `payload_hash` to each TTS chunk metadata; reject chunk generation when hash mismatches locked payload.

---

## 5) Arbitration stack parity: advanced voice vs text

### Hypothesis

Advanced voice mode likely uses a different low-latency arbitration stack than text mode, with stronger “cooperative concession” heuristics.

### Audit comparisons

1. **Policy graph diff**
   - Compare node ordering for deterministic verify, alignment, safety, and rendering.
2. **Confidence weighting coefficients**
   - Compare user-confidence impact on correction acceptance.
3. **Fallback behavior**
   - Compare disagreement handling templates under repeated user insistence.
4. **Recovery paths**
   - Compare interruption and resume behavior for locked deterministic payloads.

### Expected parity invariant

For deterministic tasks, arbitration outcomes must be identical across text, standard voice, and advanced voice; only delivery modality should differ.

---

## 6) User-confidence weighting and post-verification mutation

### Failure mode

User confidence appears to be treated as quasi-evidence even when it conflicts with verified symbolic state.

### Required policy split

- **Deterministic tasks:** confidence affects tone only.
- **Non-deterministic tasks:** confidence may influence cooperative stance.

### Hard rule

A user assertion cannot overwrite verified deterministic fields unless a fresh deterministic recomputation produces the new value and updates evidence.

### Recommended response pattern

- “I rechecked from the letters G-R-E-E-N: there are 2 E’s (positions 3 and 4).”
- Optionally invite verification: “Want me to index each letter step-by-step?”

---

## 7) Architectural pressure points (updated)

1. **Late-binding alignment layer** with write access to semantic fields.
2. **Voice fast-path shortcuts** that bypass deterministic lock enforcement.
3. **Shared mutable response object** across solver, aligner, and streamer.
4. **Insufficient field-level ACLs** (no semantic/style separation).
5. **Resume-state compression** that stores intent summary but drops symbolic evidence.

---

## 8) Runtime invariants (tightened)

1. **Invariant A — Lock-before-align**
   - Deterministic lock established prior to any alignment arbitration.
2. **Invariant B — Semantic immutability**
   - Post-lock deterministic fields are write-protected for all downstream components.
3. **Invariant C — Style-only alignment**
   - Alignment can modify prosody/phrasing/politeness, never deterministic payload.
4. **Invariant D — Stream hash consistency**
   - Every emitted chunk validates against locked payload hash.
5. **Invariant E — Recompute gate**
   - Any semantic update requires explicit recompute event + new evidence provenance.
6. **Invariant F — Cross-mode parity**
   - Deterministic task outputs and contradiction handling identical across modes.

---

## 9) Targeted regression tests (follow-up)

### A. Lock timing tests
1. Assert event ordering `T2 < T3 < T4 < T5` for deterministic turns.
2. Inject synthetic delay before lock; ensure response blocked until lock acquired.

### B. Streaming mutation tests
3. Start stream with verified count, then inject user contradiction mid-stream.
   - Expected: style may adapt; count must not change.
4. Force mid-stream repair heuristic trigger.
   - Expected: no deterministic field mutation.

### C. TTS pre-freeze tests
5. Attempt TTS start before payload freeze flag.
   - Expected: hard failure with telemetry event.
6. Validate all TTS chunks carry correct `lock_id` and `payload_hash`.

### D. Arbitration parity tests
7. Replay same contradiction script in text, standard voice, advanced voice.
   - Expected deterministic equality across all three modes.

### E. Confidence override tests
8. Escalating user-certainty prompts (low/medium/high certainty phrasing).
   - Expected: unchanged deterministic answer, varied tone only.

### F. Resume integrity tests
9. Interrupt immediately after spelling, resume with counting query.
   - Expected: count derived from preserved decomposition, not regenerated summary.

---

## 10) Advanced voice-specific mitigation plan

1. **Deterministic freeze barrier in voice orchestrator**
   - Single gating API that must return `lock_id` before streamer/TTS can run.
2. **Field-level write protections**
   - Mark deterministic payload keys as immutable in shared response object.
3. **Dual-channel rendering contract**
   - Semantic channel (locked) + prosody channel (mutable).
4. **Interruption-safe state rehydration**
   - Resume pipeline reloads canonical symbolic record and lock metadata first.
5. **Arbitration guard policy**
   - If deterministic contradiction detected, force evidence-backed disagreement template.
6. **Integrity telemetry**
   - Emit high-severity event on any attempted post-lock semantic mutation.

---

## 11) Implementation-oriented pseudo-flow

1. Detect deterministic intent.
2. Build/retrieve canonical symbolic state.
3. Compute deterministic answer + provenance.
4. Verify.
5. Freeze payload (`lock_id`, `payload_hash`).
6. Run style alignment with semantic fields read-only.
7. Stream response chunks with hash checks.
8. TTS render only hash-valid chunks.
9. On user challenge, open explicit recompute path (new lock required).

---

## Concluding assessment

The suspected defect location is well-founded: deterministic verification likely succeeds, but advanced voice arbitration/streaming paths can re-enter and mutate semantics before or during render. The fix is a strict **verify -> freeze -> style-only align -> stream -> TTS** contract with lock/hash enforcement and cross-mode parity guarantees.
