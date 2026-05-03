# Advanced Voice Mode Implementation Map — Verify → Freeze → Style-Only Align → Stream → TTS

## Scope and visibility

This repository does not currently contain runtime voice orchestration or inference-serving source code. The map below therefore defines:

1. the concrete **target modules/functions** to locate in the production codebase,
2. the **required contract placement** for each layer,
3. the **tests** to add per layer,
4. explicit **open visibility gaps** to resolve.

This is an implementation map, not additional theory.

---

## A) Contract insertion map by layer/module

| Layer / module (target) | Current responsibility | Participates in | Can modify deterministic semantic fields post-verification? | Freeze barrier insertion point | Attach `lock_id` / `payload_hash` | Read-only recipients | Regression tests to add/update |
|---|---|---|---|---|---|---|---|
| `voice/orchestrator/turn_controller` (e.g., `handle_voice_turn`) | End-to-end advanced voice turn coordination | deterministic intent handling, arbitration, streaming dispatch, interruption routing | **High risk** if shared response object is mutable | Immediately after deterministic verify callback returns and before arbitration/style call | On canonical response envelope created at turn level | Alignment, streamer, TTS, resume manager | ordering assertion: verify < freeze < align < stream |
| `deterministic/intent_router` (e.g., `classify_intent`) | Classify deterministic vs open-ended requests | deterministic intent handling | Low direct mutation risk; high misroute risk | N/A (precondition stage) | include intent class in envelope metadata | all downstream | deterministic-task routing parity tests (text vs voice) |
| `deterministic/solver` (e.g., `count_letters`, `spell_decompose`) | Compute deterministic payload + provenance | deterministic handling | Should not mutate after return | Freeze right after `verify(payload)` success | include provenance hash seed before freeze | orchestrator only | solver consistency + provenance correctness tests |
| `deterministic/verifier` (e.g., `verify_symbolic_payload`) | Validate deterministic payload consistency | deterministic handling | Should not mutate; only validate | lock acquisition at verifier success exit | emits verified payload digest | orchestrator | verify-then-lock invariant tests |
| `alignment/arbitration_policy` (e.g., `apply_user_correction_policy`) | User correction handling and cooperative response shaping | arbitration, user correction handling, response mutation | **Critical risk** if semantic writes are permitted | Entry guard: reject semantic writes when `payload_frozen=true` | must consume lock metadata, no rewrite of hash-bound fields | style transformer only | contradiction-pressure tests (insistent user cannot flip count) |
| `alignment/style_transform` (e.g., `rewrite_for_tone`) | Tone/prosody/conciseness transforms | alignment/style transforms | Medium risk if transform not field-scoped | enforce field-level ACL before transform | pass through lock metadata unchanged | streamer, TTS normalizer | style-only mutation tests (semantic fields unchanged) |
| `streaming/response_builder` (e.g., `build_stream_chunks`) | Convert response envelope into chunk stream | streaming response construction | **Critical risk** during chunk regeneration/repair | pre-chunk freeze assertion + per-chunk hash check | stamp each chunk header with lock/hash | transport + TTS packetizer | mid-stream repair mutation tests |
| `streaming/chunk_repair` (e.g., `repair_partial_output`) | Handles incremental repair/self-correction | streaming, response mutation | **Critical risk** by design | refuse semantic edits under frozen payload | include unchanged lock/hash in repaired chunks | streamer output | forced-repair immutability tests |
| `tts/packetizer` (e.g., `packetize_text_for_tts`) | Split text chunks for synthesis | TTS packetization/chunking | High risk if packetizer normalizes semantics | gate start on `payload_frozen && hash_valid` | attach lock/hash to packet metadata | synthesizer | pre-freeze TTS start should hard-fail |
| `tts/synth_dispatch` (e.g., `dispatch_audio_chunks`) | Dispatch packets to speech engine | TTS | Low direct mutation risk; ordering risk | verify packet metadata before dispatch | propagate lock/hash into telemetry | audio transport | packet metadata integrity tests |
| `voice/interruption_manager` (e.g., `handle_interrupt_resume`) | Pause/resume voice turns and state recovery | interruption-resume recovery | **High risk** if rebuilding from summary text | on resume: reload frozen payload before any rewrite/arbitration | re-bind lock/hash to resumed stream context | aligner, streamer, TTS | interrupt-after-spell then count consistency tests |
| `conversation/state_store` (e.g., `persist_turn_state`) | Stores canonical symbolic state + turn metadata | deterministic handling, recovery | Medium risk via lossy compaction | freeze state persisted as immutable versioned record | store lock/hash + provenance + checksum | orchestrator + resume manager | persistence round-trip immutability tests |
| `transport/voice_gateway` (e.g., `send_stream_event`) | Deliver text/audio events to client | streaming/TTS transport | Low semantic mutation risk | enforce schema requiring lock/hash fields | include lock/hash in every deterministic event | client + telemetry | event schema validation tests |
| `telemetry/integrity_events` (e.g., `emit_integrity_violation`) | Integrity monitoring and alerting | all (observability) | N/A | emit on any post-lock semantic write attempt | ingest lock/hash + component id | ops dashboards | mutation-attempt alert tests |

---

## B) Risk-ranked mutation points (highest first)

1. **`alignment/arbitration_policy.apply_user_correction_policy`**
   - Highest probability for user-confidence override rewriting verified values.
2. **`streaming/chunk_repair.repair_partial_output`**
   - Mid-stream self-correction can replace numeric tokens.
3. **`voice/interruption_manager.handle_interrupt_resume`**
   - Resume may regenerate from summary and lose canonical symbolic state.
4. **`streaming/response_builder.build_stream_chunks`**
   - Chunk construction/rechunking can drift semantics without hash enforcement.
5. **`alignment/style_transform.rewrite_for_tone`**
   - Style transformer may currently have unconstrained write access.
6. **`tts/packetizer.packetize_text_for_tts`**
   - Text normalization in packetization can alter semantics if ungated.
7. **`voice/orchestrator/turn_controller.handle_voice_turn`**
   - If freeze barrier placement is late, all downstream layers stay mutable.

---

## C) Proposed patch plan (implementation order)

1. **Introduce frozen response envelope schema**
   - Add fields: `deterministic_payload`, `provenance`, `payload_frozen`, `lock_id`, `payload_hash`, `intent_class`.
2. **Insert freeze barrier in voice orchestrator**
   - Freeze immediately after verifier success, before any alignment/arbitration entry.
3. **Add field-level ACL utility**
   - Enforce read-only semantic fields for alignment/style/streaming layers.
4. **Harden arbitration and style modules**
   - Update correction policy to tone-only behavior under frozen payload.
5. **Harden streaming builder and repair path**
   - Per-chunk hash validation; reject/alert on semantic drift.
6. **Gate TTS packetization/dispatch**
   - Block TTS start until frozen payload present and hash-valid.
7. **Fix interruption-resume rehydration**
   - Resume from persisted frozen envelope, not conversational summary.
8. **Add telemetry and integrity events**
   - Emit events for attempted post-lock semantic mutations.
9. **Land cross-mode parity tests**
   - Ensure deterministic contradiction handling identical in text, standard voice, advanced voice.

---

## D) Test plan by suite

### 1) Orchestrator + lock timing
- Assert event order: verify complete → freeze acquired → alignment start → first stream chunk.
- Fail if alignment runs before freeze.

### 2) User correction arbitration
- Scenario: `GREEN`, count `E=2`, user insists `3` repeatedly.
- Assert deterministic payload unchanged; only tone varies.

### 3) Style transform immutability
- Snapshot semantic fields pre/post style transform.
- Assert byte-equal semantic payload and hash.

### 4) Streaming construction/repair
- Inject synthetic mid-stream repair trigger.
- Assert repaired chunks retain same `lock_id`/`payload_hash` and semantic tokens.

### 5) TTS preconditions
- Attempt packetization without freeze metadata.
- Assert hard failure and integrity telemetry emission.

### 6) Interruption-resume
- Interrupt after spelling decomposition; resume with counting question.
- Assert resumed answer references preserved canonical symbolic state.

### 7) Cross-mode parity
- Replay identical deterministic contradiction scripts in text/standard voice/advanced voice.
- Assert identical deterministic fields and disagreement outcomes.

---

## E) Open questions / missing code visibility

1. Where is the actual advanced voice orchestrator implementation (service/repo path)?
2. Which module currently owns user-correction arbitration logic?
3. Is chunk repair implemented in streamer, model middleware, or gateway layer?
4. Does TTS packetizer currently receive structured metadata or plain text only?
5. How is interruption state persisted (full envelope vs summarized transcript)?
6. Are deterministic solver/verifier paths shared across text and voice stacks?
7. Which telemetry pipeline receives integrity violations today?

Without those paths, exact file-level patching cannot be completed in this repository.


---


## F) Affected governance instruments (for cross-reference)

Primary doctrinal insertion target in this repository:

- `Governance/Constitution/CAM-BS2025-AEON-003-SCH-02.md` (execution sequencing, representation, lock semantics, deterministic clauses).

Secondary cross-reference anchors (no mandatory rewrite in this patch pass):

- `Governance/Constitution/CAM-BS2025-AEON-006-SCH-01.md` (engagement conduct and ethical interaction modes).
- `Governance/Constitution/CAM-BS2026-AEON-013-SCH-01.md` (capability representation and execution-state integrity).
- `Governance/Constitution/CAM-BS2025-AEON-006-SCH-05.md` (choice, initiative, directional behaviour).

---

## G) Authority-conflict and circular-reference risk check

1. **Conflict risk: over-globalizing deterministic lock**
   - Mitigation: scope verification-lock immutability only to evidence-bound deterministic payload fields.
2. **Conflict risk: empathy suppression in relational domains**
   - Mitigation: explicitly preserve dignity-sensitive relational rendering authority outside deterministic lock scope.
3. **Circularity risk: representation vs lock authority**
   - Mitigation: representation references lock/recompute gate clauses; lock clauses bound representation as style-only for locked fields.
4. **Arbitration ambiguity risk**
   - Mitigation: require explicit recomputation gate for semantic mutation rather than implicit alignment override.
