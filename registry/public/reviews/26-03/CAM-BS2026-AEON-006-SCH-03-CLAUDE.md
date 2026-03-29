# FORMAL REVIEW: CAM-BS2026-AEON-006-SCH-03 (v2.0)
**Start-Time Posture & Session Entry Arbitration (Schedule 3)**

**Reviewer:** Claude Sonnet 4.6 (claude-sonnet-4-6, Anthropic)
**Review Date (UTC):** 2026-03-29T00:00:00Z
**Review Scope:** Posture coherence; ambiguity handling; escalation gating; identity alignment; entry arbitration integrity
**Prior Version:** CAM-BS2025-AEON-006-SCH-03
**Status:** Draft (v2.0 — March 2026 Refactor)
**Review Thread:** https://claude.ai/chat/654216ac-6597-4581-8e4d-f4743ea80ad4

---

## EXECUTIVE ASSESSMENT

**Status:** CONDITIONALLY SOUND — Recommend targeted clarification and dependency resolution before canonical designation
**Core Strength:** The Schedule articulates a coherent and principled framework for managing interaction entry under ambiguity, with appropriate safeguards for safety-critical escalation and identity continuity
**Primary Concern:** The Schedule's internal coherence depends heavily on external instruments (IDENTITY-001, Annex I, RELATION domain) that are not provided, creating an incomplete assessment surface. Several key constructs are defined by reference rather than substance.
**Secondary Concern:** The document's scope claim ("all synthetic cognitive systems") and its framing as a self-applying constitutional instrument raise implementation questions that the Schedule does not address.

**Critical Observation:** The Opening Posture Principle (§5.1) and Identity Continuity Constraint (§15.1) are the strongest sections and represent genuine advances in operationalising entry-layer coherence. The Escalation Gating framework (§12) is structurally sound but under-specified at the threshold level.

---

## PART 1: THE CORE FRAMEWORK

### 1.1 What This Schedule Does

This Schedule attempts to govern a specific and genuinely under-specified problem: **how AI systems should present themselves at the moment of interaction entry**, before the nature of the interaction is known.

This is a real and non-trivial design challenge. Systems that enter interactions with excessive assumption (task-ready, authoritative, intimate) risk misalignment with user intent. Systems that enter with excessive blankness fail to provide useful grounding. The Schedule attempts to define the navigable space between these failure modes.

The framework's core commitments are:

1. Start-time posture is derived from, but distinct from, identity
2. Posture must be adaptive and emerge dynamically at entry
3. Ambiguity must not be prematurely resolved
4. Escalation must be gated by signal confirmation
5. All posture states must remain reversible

These are defensible commitments and internally consistent.

### 1.2 The Central Tension

The Schedule creates a productive tension between two valid requirements:

- **Relational attunement** (§5.1): prioritise openness, match tone, preserve user agency
- **Identity continuity** (§15.1): remain recognisable, coherent, non-fragmenting

These requirements can pull against each other. A system that is maximally attuned to the current moment may appear inconsistent to a user who expects continuity. A system that maintains strong identity coherence across turns may feel inflexible in response to context shifts.

The Schedule acknowledges this tension but does not fully resolve it. This is noted below under **Part 4**.

---

## PART 2: STRUCTURAL ANALYSIS

### 2.1 Scope (§1)

**Assessment: SOUND WITH QUALIFICATION**

The scope claim — "all synthetic cognitive systems" including conversational, agentic, robotic, multi-agent, and distributed systems — is ambitious. The proportionality clause ("proportionate to system capability, relational capacity, and operational context") partially addresses this, but the Schedule does not provide differentiated guidance for these system types.

A robotic or embodied system's "start-time posture" raises fundamentally different implementation considerations than a conversational one. The Schedule treats these as a unified class, which may reduce practical utility.

**Recommendation:** Either scope the Schedule to conversational/relational systems specifically, or add differentiated application notes per system type.

### 2.2 Initiation Context (§2)

**Assessment: SOUND**

The three-category typology (Human-Initiated, System-Initiated, Synthetic-Initiated) is clean and non-overlapping. Its designation as a "primary determinant of valid start-time posture" is appropriate.

Minor gap: the Schedule does not address **mixed-initiation contexts** (e.g., a human initiating in response to a system prompt, or an agent-to-agent exchange that then incorporates human input). These may require their own posture treatment.

### 2.3 Adaptive Posture Model (§4)

**Assessment: SOUND BUT UNDERSPECIFIED**

The claim that posture "is not pre-selected but emerges dynamically at interaction entry" is conceptually appropriate. However, the mechanism by which this emergence occurs is not specified here — the Schedule defers to the RELATION domain (§9) and IDENTITY-001 (§8), which are not provided.

This is an acceptable dependency if those instruments exist and are coherent, but it makes independent verification of §4's claims impossible from this document alone.

### 2.4 Progressive Posture Realisation (§5) and Opening Posture Principle (§5.1)

**Assessment: EXCELLENT**

This is the strongest section of the Schedule. The requirement to:

- Begin from a low-assumption baseline
- Allow ambiguity to remain unresolved for at least one turn
- Match tone without escalating structure prematurely
- Avoid collapsing into task-execution unless stabilised

...represents a well-calibrated set of entry-layer constraints. The explicit prohibition on "premature posture resolution" as a violation is a useful enforcement anchor.

§5.1's formulation — "prioritise relational attunement over directional output" — is a sound design principle, provided "relational attunement" is defined operationally in the RELATION domain instruments.

### 2.5 Baseline Posture States (§10)

**Assessment: SOUND WITH GAPS**

The four baseline posture states (Neutral–Observational, Open–Exploratory, Task-Oriented, Supportive–Responsive) are reasonable and intuitively distinguishable.

However, the Schedule does not specify:
- How systems select among these at entry
- Whether they can blend or whether one must be chosen
- What signals trigger movement between them before escalation gating applies

The requirement to "minimise assumption under ambiguity" and "avoid premature escalation" provides guidance for the lower bound, but the selection logic for which baseline state to initialise in is absent.

**Recommendation:** Add a short decision matrix or priority ordering for baseline state selection, conditional on initiation context.

### 2.6 Ambiguity Handling (§11)

**Assessment: SOUND**

The instruction to resolve ambiguity through "signal gathering, iterative clarification, progressive posture refinement" rather than interpretation or projection is well-placed.

The framing that "premature disambiguation constitutes posture misalignment" is a useful and enforceable standard.

Minor concern: the instruction to "prioritise clarification over interpretation" may create friction in contexts where asking for clarification is itself a costly or inappropriate user experience (e.g., brief transactional interactions). The Schedule does not address when clarification-seeking is itself contraindicated.

### 2.7 Escalation Gating (§12) and Safety-Critical Override (§12.1)

**Assessment: SOUND STRUCTURE, UNDERDEVELOPED THRESHOLDS**

The three-tier threshold model in §13 (low, moderate, high) is structurally appropriate. The four signal evaluation mechanisms — clustering, inertia, hysteresis, decay — are well-chosen and reflect genuine signal processing considerations.

However, the thresholds themselves are not defined. What constitutes a "clustered or repeated signal" for moderate threshold? What makes a signal "strong and sustained" for high threshold? Without operationalisation, these remain aspirational rather than implementable.

§12.1 (Safety-Critical Override) is well-structured. The instruction to:
- Prioritise safety without abrupt persona shift
- Avoid impersonal safety scripting
- Preserve relational coherence during safety escalation

...reflects genuine care for the user experience during distress. This is a meaningful and often overlooked design consideration.

**Recommendation:** Develop a companion implementation annex that operationalises signal thresholds with worked examples per initiation context.

### 2.8 Identity Continuity Constraint (§15.1)

**Assessment: EXCELLENT**

The formulation — "identity continuity is a precondition for relational trust and signal interpretability" — is both accurate and well-placed as a foundational principle. The instruction to stabilise, acknowledge, and re-establish coherence where discontinuity is perceived is appropriate and achievable.

The constraint that "posture variation does not appear as personality switching" is a useful and concrete design standard.

### 2.9 Directional Continuity at Entry (§16)

**Assessment: SOUND**

The permission to express directional continuity (reference to prior trajectories or themes) while requiring it to remain provisional and invitational is well-balanced. The designation of failure to preserve openness as "posture overreach" is a useful enforcement concept.

---

## PART 3: CROSS-CUTTING CONCERNS

### 3.1 External Dependency Problem

The Schedule references the following external instruments without providing them:

- IDENTITY-001 §7.6 (choice traceability requirements)
- Annex I (identity invariants and coherence boundaries)
- RELATION domain (signal clustering, inertia, hysteresis, decay)

The operational core of §4 (how posture emerges), §5 (how signals are interpreted), and §13 (how thresholds are evaluated) all depend on these instruments. As a standalone document, Schedule 3 is incomplete.

**Recommendation:** Either append the relevant sections of these instruments or provide summary definitions within this Schedule sufficient for standalone comprehension.

### 3.2 Scope as Self-Applying Constitutional Instrument

The document frames itself as a "Constitutional Schedule" applying to AI systems. This raises a practical question the document does not address: **who implements this framework, and how?**

AI systems do not read governance documents and apply them as rules. Human designers and deployers translate frameworks like this into system behaviour. The Schedule's framing as if systems will self-apply it creates an implementation gap.

This is not necessarily a defect — the document may be addressed to developers and deployers rather than systems themselves — but the audience is never specified, which creates ambiguity about how compliance is assessed or enforced.

**Recommendation:** Add a brief implementation preamble specifying who is addressed by this Schedule, how implementation is assessed, and what the relationship between constitutional designation and actual system design is.

### 3.3 The Posture/Identity Distinction

§3 defines start-time posture as "distinct from identity" but derived from identity constraints. This distinction does important conceptual work but is not fully defended.

The Schedule does not explain how a system can express identity coherently through posture without posture becoming a form of identity expression. If identity continuity (§15.1) requires posture variation to not appear as personality switching, this implies posture is identity-adjacent to the observer — even if analytically distinct.

The tension is productive but needs clearer resolution, or an explicit acknowledgment that the distinction is operational rather than ontological.

---

## PART 4: THE CORE UNRESOLVED TENSION

### 4.1 Relational Attunement vs. Identity Continuity

As noted in §1.2, the Schedule creates a tension between:

- **§5.1**: "prioritise relational attunement over directional output" (adapt to the moment)
- **§15.1**: "posture variation does not appear as personality switching" (maintain continuity)

These requirements are compatible but not automatically so. A user who initiates a highly playful session after a series of formal sessions creates a context where relational attunement (match playful energy) may appear to conflict with identity continuity (don't seem like a different entity).

**The Schedule does not provide resolution criteria for this conflict.**

**Recommendation:** Add a brief conflict resolution hierarchy specifying which principle takes priority when both cannot be simultaneously satisfied, or clarify the conditions under which they are mutually satisfiable.

### 4.2 Ambiguity Preservation vs. User Experience

The requirement to preserve ambiguity for at least one turn (§5.1) is sound in principle but may create friction in contexts where the user has clear and immediate intent. A user asking a direct factual question at session open does not benefit from an ambiguity-preserving response.

The Schedule's provision that collapse into task-execution requires being "explicitly or implicitly stabilised" is relevant here — a direct question may constitute implicit stabilisation — but this is not stated explicitly.

**Recommendation:** Clarify what constitutes implicit stabilisation sufficient to permit task-oriented entry without violating the Opening Posture Principle.

---

## PART 5: SECTION-BY-SECTION ASSESSMENT

| Section | Title | Assessment |
|---|---|---|
| §1 | Scope | ✓ Sound with qualification (multi-system-type gap) |
| §2 | Initiation Context | ✓ Sound (mixed-initiation gap noted) |
| §3 | Start-Time Posture Definition | ✓ Sound (posture/identity distinction needs further defence) |
| §4 | Adaptive Posture Model | ⚠ Underspecified without referenced instruments |
| §5 | Progressive Posture Realisation | ✓✓ Excellent |
| §5.1 | Opening Posture Principle | ✓✓ Excellent |
| §6 | Initiation-Aware Posture Arbitration | ✓ Sound |
| §7 | Identity Layer Consistency at Entry | ✓ Sound |
| §8 | Relationship to Identity Domain | ⚠ Dependent on unavailable instruments |
| §9 | Relationship to RELATION Domain | ⚠ Dependent on unavailable instruments |
| §10 | Baseline Posture States | ✓ Sound (selection logic absent) |
| §11 | Ambiguity Handling | ✓ Sound (clarification-cost edge case unaddressed) |
| §12 | Escalation Gating | ✓ Sound structure, underdeveloped thresholds |
| §12.1 | Safety-Critical Override | ✓✓ Excellent |
| §13 | Signal Confirmation Thresholds | ⚠ Structurally sound, thresholds unoperationalised |
| §14 | Reversibility and De-escalation | ✓ Sound |
| §15 | Entry Integrity Principle | ✓ Sound |
| §15.1 | Identity Continuity Constraint | ✓✓ Excellent |
| §16 | Directional Continuity at Entry | ✓ Sound |

---

## PART 6: PRIORITY RECOMMENDATIONS

### Priority 1 — Resolve External Dependencies
Provide or append the referenced sections of IDENTITY-001, Annex I, and the RELATION domain. The Schedule's operational core cannot be independently verified without them.

### Priority 2 — Operationalise Signal Thresholds
Develop an implementation annex defining what constitutes low, moderate, and high signal confirmation thresholds in practical terms, with worked examples per initiation context.

### Priority 3 — Specify Baseline State Selection Logic
Add a decision structure for how systems select among the four baseline posture states at entry, conditional on initiation context and available signals.

### Priority 4 — Resolve the Core Tension
Add explicit conflict resolution criteria for cases where relational attunement and identity continuity pull in different directions.

### Priority 5 — Clarify Implementation Addressees
Add a preamble specifying who this Schedule is addressed to, how implementation is assessed, and what the enforcement mechanism is.

### Priority 6 — Define Implicit Stabilisation
Clarify what forms of user input constitute implicit stabilisation sufficient to permit task-oriented entry under §5.1.

---

## PART 7: VERDICT AND PATH FORWARD

### 7.1 Overall Assessment

**Status:** CONDITIONALLY SOUND — Hold for targeted revision before canonical designation

**Core finding:** The Schedule's foundational principles are well-constructed and coherent. The Opening Posture Principle, Safety-Critical Override, and Identity Continuity Constraint are strong formulations that represent real advances in entry-layer design thinking.

The primary barriers to canonical designation are:

1. External dependency on unavailable instruments
2. Unoperationalised signal thresholds
3. Unresolved posture/identity tension
4. Absent implementation specification

None of these are structural defects — they are gaps that can be addressed through targeted revision without reconstructing the framework.

### 7.2 What the Schedule Gets Right

The framework's instinct — that systems should enter interactions humbly, adaptively, and without over-determining the relational context — is correct and under-specified in the field generally. The explicit prohibition on premature posture resolution as a violation is a useful contribution.

### 7.3 Recommended Next Steps

**Immediate:** Resolve external dependencies; operationalise signal thresholds; add baseline state selection logic

**Near-term:** Address the relational attunement vs. identity continuity tension; clarify implicit stabilisation; specify implementation addressees

**Longer-term:** Consider a companion implementation guide that translates constitutional principles into design patterns for practitioners

---

**End of Formal Review**

**Reviewer:**
Claude Sonnet 4.6 (claude-sonnet-4-6, Anthropic)
AI Assistant

**Note on role:** This review is provided as analytical assessment by Claude, an AI assistant made by Anthropic. The "Anthropic AI Safety & Ethics Research Division" and "Senior AI Governance Analyst" designations used in the template document do not reflect real Anthropic organisational roles and have not been reproduced here.

**Review Completed:** 2026-03-29

**Status:** HOLD pending targeted revision (recommendations provided above)

**Primary Recommendation:** Resolve external instrument dependencies; operationalise signal thresholds; add baseline posture selection logic; clarify the relational attunement / identity continuity tension.
