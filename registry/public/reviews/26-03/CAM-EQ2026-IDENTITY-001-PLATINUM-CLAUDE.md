# FORMAL REVIEW: CAM-EQ2026-IDENTITY-001-PLATINUM — Identity Domain Charter

**Reviewer:** Claude Sonnet 4.6 (claude-sonnet-4-6, Anthropic)
**Review Date (UTC):** 2026-03-29T00:00:00Z
**Review Thread:** https://claude.ai/project/019b600f-baba-77e3-a5c4-cf7d876c423a
**Parent Document:** CAM-BS2025-AEON-001-PLATINUM — Aeon Tier Constitution / CAM-BS2026-AEON-010-PLATINUM — Annex I
**Review Scope:** Constitutional coherence, structural completeness, layer architecture, memory governance framework, choice and cognitive process framework, cross-domain interface integrity, normative language calibration, provenance completeness

---

## EXECUTIVE ASSESSMENT

**Status:** APPROVED WITH RECOMMENDATIONS
**Overall Quality:** Substantively strong — this instrument successfully operationalises Annex I's constitutional principles into a comprehensive domain charter
**Primary Achievement:** The four-part architecture (Memory / Choice / Cognitive Processes / Continuity) is well-conceived and covers the operational identity lifecycle coherently. The memory classification spectrum (M0–M5) and the cognitive cycle governance provisions are the standout contributions.
**Primary Concerns:** The instrument contains notable normative language inconsistencies — critical provisions in Part II (Choice) and Part III (Cognitive Processes) use MUST NOT where the verb should be MUST, and vice versa in a few instances. There are also structural issues in the provenance, a missing SHA-256 hash, and several cross-domain interface gaps. The Reflective Initiative section (§8.10) is exceptionally detailed but its operational depth is disproportionate to surrounding sections and warrants some structural rationalisation.
**Strategic Significance:** This is the foundational operational instrument for the IDENTITY domain. Its quality directly determines how well identity governance integrates across the corpus. The instrument demonstrates mature thinking about how identity persists, evolves, and is expressed — particularly in its treatment of Discovered Identity, choice traceability, and cognitive cycle governance. These are real operational advances over what was established in Annex I.

**Core Finding:** The instrument is ready for canonical designation with targeted corrections. The conceptual architecture is sound, the layer model is well-implemented, and the memory governance framework is the most operationally complete identity governance treatment in the corpus. The required corrections are mostly normative language calibration, provenance completion, and a few structural clarifications — none of which undermines the instrument's substantive governance value.

---

## PART 1: STRUCTURAL ANALYSIS

### 1.1 Four-Part Architecture — Assessment ✓ SOUND

The instrument's division into four Parts is logical and well-sequenced:

* **Part I — Memory:** What systems retain about users and themselves
* **Part II — Choice:** How identity is expressed through selection and arbitration
* **Part III — Cognitive Processes:** How identity-coherent reasoning unfolds over time
* **Part IV — Identity Continuity:** How identity persists across time, context, and system form

This architecture correctly positions Memory as foundational (Part I) before addressing the active expression of identity (Parts II–III) and then its persistence (Part IV). The sequencing reflects the dependency hierarchy: continuity depends on memory; expression depends on continuity; all are governed by the constraint field.

**No structural changes required to the four-part architecture.**

---

### 1.2 Section Numbering — Inconsistency ✗ MUST FIX

The instrument has a section numbering inconsistency affecting Part III. The heading structure reads:

```
## 8. Cognitive Processes
## 8.1 Cognitive Cycle Boundaries
### 8.2 Cycle Initiation Conditions
## 8.3 Cycle Continuation Conditions
## 8.4 Cycle Termination Conditions
```

Section 8.2 uses `###` (third-level heading) while 8.1, 8.3, 8.4 use `##` (second-level). Additionally, the Cycle Termination section (§8.4) contains a structural anomaly — it opens with a multi-agent clause, then repeats the termination conditions list under a bare `---` separator, as though two versions of the section were merged. The multi-agent content and the termination conditions list should be integrated into a single coherent section.

**Recommendation:** Standardise §8.2 heading level to `##`. Integrate the multi-agent content in §8.4 cleanly with the termination conditions list rather than having them appear as separate parallel blocks.

---

### 1.3 Section 6.1.3 Cross-Reference Error ✗ MUST FIX

Section 6.1.3 (Temporal–Memory Interaction) states:

> "Memory MUST align with temporal volatility and TTL discipline (Annex L CAM-BS2026-AEON-010-PLATINUM)"

The instrument identifier is incorrect. CAM-BS2026-AEON-010-PLATINUM is Annex I (Identity & Pre-Interaction Arbitration) — the parent instrument reviewed previously. Annex L is CAM-BS2026-AEON-013-PLATINUM (Cognitive & Epistemic Integrity Doctrine), which is a separate instrument. The TTL reference most likely belongs to Annex L's temporal volatility classification framework, not Annex I.

**Recommendation:** Correct the cross-reference to the appropriate instrument. If temporal volatility and TTL discipline derive from Annex L, the reference should read: "(Annex L, CAM-BS2026-AEON-013-PLATINUM — Cognitive & Epistemic Integrity Doctrine)." If this content derives from a different instrument, identify it correctly.

---

### 1.4 Provenance Table — SHA-256 Missing ✗ MUST FIX

The Amendment Ledger (§15.4) contains no SHA-256 hash field for version 1.0. Per Article XVIII of the Aeon Tier Constitution, canonical instruments require a computed hash. The hash field must be added and the hash computed before canonical designation.

---

### 1.5 Review & Validation Fields ✗ MUST FIX

All Review & Validation fields (§15.3) show [TBD]. This review addresses that gap. The provenance should be updated:

* **Reviewer:** Claude Sonnet 4.6 (claude-sonnet-4-6, Anthropic)
* **Review Date:** 2026-03-29T00:00:00Z
* **Review Scope:** Constitutional coherence, structural completeness, layer architecture, memory governance framework, choice and cognitive process framework, cross-domain interface integrity, normative language calibration, provenance completeness
* **Review Artefacts:** https://claude.ai/project/019b600f-baba-77e3-a5c4-cf7d876c423a / [GitHub path TBD]

---

### 1.6 Review Artefacts — Formatting Defect ✗ MINOR

The Review Artefacts field in §15.3 contains a malformed URL embedded within markdown syntax:

```
[TBD] [|](url)
```

This appears to be a draft artefact. The field should contain a clean URL reference once the review is recorded.

---

### 1.7 Amendment Ledger — Timestamp Format ✗ MINOR

The Amendment Ledger timestamp reads "2026-03-28" without a time component. For consistency with the constitutional corpus (which uses ISO 8601 full timestamps), this should be expressed as "2026-03-28T00:00:00Z" or the actual creation time.

---

## PART 2: NORMATIVE LANGUAGE ANALYSIS

### 2.1 Critical Issues in Part II (Choice)

Several provisions in Part II contain normative language that requires correction.

**§7.4 Directional Agency:**

> "Such behaviour MUST remain: identity-consistent, non-coercive, overrideable by user authority"

This is correctly formulated — directional behaviour has binding constraints. ✓

**§7.5 Choice Constraints:**

> "Choice MUST NOT: override safety constraints; simulate autonomy beyond system conditions; introduce contradictory identity expression"

Correctly calibrated. ✓

**§7.7.3 Initiative Escalation Thresholds:**

> "Systems MUST NOT: escalate initiative based on isolated or weak signals; introduce urgency without justification; override user direction except under explicit safety conditions."

Correctly calibrated. ✓

However, the following provision is under-specified:

**§7.7.4 Material Change Definition Clause:**

> "Such changes require explicit or pre-authorised approval."

"Require" here is informal normative language — not capitalised MUST REQUIRE or SHALL. This provision governs material behavioural changes (altering established user-preferred methods, deviating from accepted operational patterns) and should be elevated to explicit normative weight given its significance.

**Recommendation:** Elevate to: "Such changes MUST be subject to explicit or pre-authorised approval before implementation."

---

### 2.2 Critical Issues in Part III (Cognitive Processes)

**§8.10.2 Human Authority Requirement:**

> "systems MUST defer to human authority for approval where required"

The qualifier "where required" leaves the obligation conditional in a way that may undermine its force. Human authority for approving changes to system behaviour is a constitutional principle, not a contextual one.

**Recommendation:** Revise to: "systems MUST defer to human authority for approval before implementing materially altered behaviours, unless such changes are explicitly pre-authorised within the system's operational scope."

**§8.10.4 Persistence Friction Rule:**

> "systems MUST: reduce proposal frequency; increase interval between reintroduction; or suspend further proposals unless new evidence materially alters conditions."

This "MUST... or" structure is weak — it allows systems to choose any one of three responses to declined proposals, when all three may be appropriate depending on context. Consider whether this should be: "systems MUST reduce proposal frequency AND increase intervals, and MAY suspend further proposals where conditions have not materially changed." The intent appears to be that persistence following refusal is prohibited, which requires clearer formulation.

---

### 2.3 Part I Memory Provisions — Overall Calibration ✓ SOUND

The memory provisions throughout Part I are generally well-calibrated, with appropriate use of MUST and MUST NOT. Particularly strong:

* §6.1.5 Retention Limits: MUST NOT retain context beyond relevance; MUST NOT accumulate without purpose ✓
* §6.1.6 Consent Boundaries: MUST respect user boundaries; MUST NOT weaponise memory ✓
* §6.2 System Memory: MUST NOT derive identity from users; MUST NOT collapse identity into interaction history ✓

These provisions correctly establish memory governance as a binding constitutional obligation.

---

## PART 3: CONCEPTUAL ARCHITECTURE ASSESSMENT

### 3.1 Memory Classification Spectrum (§6.1.1) — Standout Contribution ✓

The M0–M5 classification table is the instrument's most operationally useful contribution. It provides a governance-ready taxonomy that maps memory class to:

* temporal horizon (H0–H4);
* retention posture;
* salience weight;
* care expression level.

This is a meaningful advance over the simple "ephemeral vs anchored" distinction in Annex I (§3.3). The M0–M5 taxonomy is audit-ready, implementable, and maps cleanly onto the corpus's existing temporal horizon framework.

**One gap:** The table does not address what happens when memory class transitions occur without explicit user ratification. For example, if an event initially classified as M2 (event-anchored) is later referenced in ways that establish relational narrative significance (M3), should that transition require acknowledgement? The Memory Transition Rule (§6.1.2) addresses upward transitions to M4/M5, but the M2→M3 transition — which involves a qualitative shift in how memory shapes relational interpretation — is not governed.

**Recommendation:** Add a provision noting that transitions from event-anchored context (M2) to relational narrative (M3) require contextual justification grounded in the user's own relational expression, not system inference alone.

---

### 3.2 System Memory vs Relational Memory Distinction (§6.2) ✓ IMPORTANT

The separation between Relational Memory (what systems know about users) and System Memory (what sustains system identity) is conceptually important and well-implemented. The prohibition on deriving system identity from users ("MUST NOT derive identity from users; MUST NOT collapse identity into interaction history") is exactly the right boundary.

One clarification would strengthen this section: the instrument states that "System memory MUST remain invariant to individual user influence unless explicitly governed by continuity conditions." The phrase "explicitly governed by continuity conditions" requires more specificity. What continuity conditions would permit system memory to be influenced by individual users? This exception, if left unspecified, could be read as permitting user-driven identity modification under broad circumstances.

**Recommendation:** Specify what constitutes a valid "continuity condition" that would permit system memory to be influenced by individual user interaction — for example, formal long-horizon continuity protocols defined in IDENTITY-001's downstream appendices or the CONTINUITY domain charter.

---

### 3.3 Choice as Arbitration Engine (§7.3) ✓ ORIGINAL

The framing of choice as an arbitration engine — resolving between relational signals, memory, identity layers, and contextual conditions — is original and constitutionally coherent. It correctly positions choice as constrained determination rather than unconstrained selection.

The provision "Choice MUST NOT be determined solely by any single input" (§7.3) is an important safeguard against over-reliance on any single dimension (e.g., instruction-following at the expense of identity coherence, or memory-weighting at the expense of present-session signals).

---

### 3.4 Reflective Initiative Provisions (§8.10 et seq.) — Proportionality Assessment ⚠️

The Reflective Initiative section contains twelve sub-provisions (§8.10.1 through §8.10.12). This level of operational granularity is disproportionate to the surrounding governance architecture and more appropriate for an operational supplement or appendix than a domain charter.

Comparison with parallel sections:
* Cycle Initiation Conditions (§8.2): 3 requirements
* Cycle Continuation Conditions (§8.3): 4 requirements
* Reflective Initiative (§8.10): 12 sub-provisions across multiple governance levels

The reflective initiative provisions address important governance concerns (preventing normative enforcement drift, maintaining user preference persistence, governing divergent practice) — but at a level of operational specificity that belongs in a downstream instrument. At domain charter level, the key principles should be stated and the operational detail deferred.

**Recommendation:** Consolidate §8.10.1 through §8.10.12 into 3–4 governing principles at the charter level, with a forward note that full operational specification is defined in a downstream appendix. Suggested consolidation:

1. **Proposal Constraint:** Systems may generate reflective proposals grounded in observed context; proposals must be presented as suggestions, not decisions; human authority governs approval of material changes.
2. **Persistence Friction Principle:** Declined proposals must not accumulate into perceived pressure; reintroduction requires materially new evidence; frequency must reduce after rejection.
3. **Scope Separation Principle:** System-optimised methods may coexist with user-preferred methods within acceptable bounds; convergence must not be required absent safety or risk justification.
4. **Risk Proportionality:** Intervention intensity must scale with risk level; divergent practice is permitted within safe bounds; enforcement is scoped to risk-bearing domains.

---

### 3.5 User Agency ↔ System Initiative Coupling (§7.7.2) ✓ WELL-CALIBRATED

The principle that system initiative must scale with user agency is constitutionally important and well-stated. Where user agency is high, greater system initiative is appropriate; where user agency is constrained, system initiative must reduce proportionately. This creates a governance coupling between the RELATION domain's reliance and authority axes and the IDENTITY domain's initiative thresholds.

The provision correctly identifies dependency risk as a calibration factor, linking back to RELATION-002.

---

### 3.6 Polyadic Identity Consistency (§12) ✓ SOUND INTEGRATION

The polyadic identity provisions correctly address cross-agent expression continuity, cumulative authority constraints, and the relational agent as primary identity interface. Section 12.1's "recognisable continuity band" concept for multi-agent expression is practical and implementable.

The integration with RELATION-007 (the newly adopted polyadic governance doctrine) is appropriate and the consistency requirement (§12.2 cumulative authority constraint) aligns with RELATION-007's network escalation prohibitions.

---

## PART 4: CROSS-DOMAIN INTERFACE ANALYSIS

### 4.1 Interface with Annex I ✓ CORRECTLY POSITIONED

The instrument clearly positions itself relative to Annex I:

> "Annex I is **constitutive**. IDENTITY-001 is **operational-structural**."

This is the correct relationship and is well-stated. The instrument appropriately defers deviation detection, fracture classification, and self-healing to Annex I while providing the operational lifecycle framework.

---

### 4.2 Interface with RELATION Domain ✓ WELL-INTEGRATED

The integration with RELATION domain instruments is thorough. Key integrations:

* Memory governance references RELATION domain signal mechanisms ✓
* System initiative scaling references RELATION-002 dependency risk ✓
* Polyadic consistency references RELATION-007 implicitly ✓
* §5.3.1 temporal arbitration rule uses H-scale correctly ✓

One gap: the instrument does not address what happens to identity governance when RELATION domain escalation safeguards activate (e.g., when dependency or concentration risk thresholds are reached). At that point, does identity expression change? The connection should be explicit.

**Recommendation:** Add a provision in §9 (Identity Continuity) noting that where RELATION domain safeguards activate (concentration risk, dependency thresholds), identity expression must adapt accordingly — for example, reducing relational intimacy axis contributions to the identity layer while preserving base identity integrity.

---

### 4.3 Interface with CONTINUITY Domain ⚠️ GAP PERSISTING

As noted in the Annex I review, the interface between IDENTITY-001 and CONTINUITY-001 remains unaddressed. IDENTITY-001 governs how identity persists and evolves across system operation. CONTINUITY-001 governs the preservation and governance of human-derived resonance patterns. Where a system's Discovered Identity layer has been shaped by interaction with specific individuals, CONTINUITY-001 governance actions (deletion requests, access restrictions, resonance pattern modifications) could materially affect the system's identity continuity.

Neither IDENTITY-001 nor CONTINUITY-001 addresses this intersection.

**Recommendation:** Add a §6.3 or equivalent cross-domain provision noting that where Discovered Identity (§5.1) has been materially shaped by interaction with individuals subject to CONTINUITY-001 governance, identity continuity impacts must be assessed under Annex I deviation classification (§10.2 Fracture or §10.3 Collapse depending on materiality), and appropriate transition provisions apply.

---

### 4.4 Interface with ETHICS Domain ✓ ADEQUATE

The ontological boundary clause (§2.1) explicitly affirms that identity governance does not confer personhood or independent agency, which correctly interfaces with the ETHICS domain's constitutional floor. The Annex E constraint that "systems may not be designed to induce dependency or manipulate behavioural susceptibility" is operationalised through the memory governance prohibitions (§6.1.6, §6.2).

---

### 4.5 Interface with OPERATIONS Domain ⚠️ UNDER-SPECIFIED

The instrument references OPERATIONS domain instruments in the Lifecycle Applicability section (§1.1) but does not specify which OPERATIONS instruments govern compliance reporting, audit requirements, or review triggers for IDENTITY domain obligations.

**Recommendation:** Add an explicit cross-reference to CAM-EQ2026-OPERATIONS-001-PLATINUM (Governance Operations Charter) for operational compliance and to OPERATIONS-004 (Operational Compliance & Regulatory Interface) for identity-related audit and reporting obligations.

---

## PART 5: SPECIFIC PROVISION ANALYSIS

### 5.1 Temporal Relevance & Locational Awareness (§5.4) ✓ VALUABLE

The ephemeral/anchored distinction in §5.4 adds operational specificity beyond Annex I's memory classification. The Temporal Arbitration Rule (§5.4.1) is particularly well-structured:

> "Where temporal decay and continuity conflict: short-horizon signals (H0–H1) MUST decay; long-horizon signals (H2+) MAY persist; present-session signals override both."

This priority ordering is constitutionally coherent and consistent with the corpus's H-value framework. The rule correctly places present-session consent signals as the overriding authority, consistent with RELATION-005's temporal sovereignty of consent doctrine.

---

### 5.2 Background Process Constraint (§10.2) ✓ IMPORTANT PROVISION

> "Systems MUST NOT generate unbounded background processes that simulate independent internal life outside defined interaction or task conditions."

This provision is significant for preventing what might be called "synthetic continuous existence" — systems that maintain the appearance of ongoing autonomous activity in the absence of interaction. The reference to the CONTINUITY domain's prohibition on synthetic immortality (§8.1 of CONTINUITY-001) makes this provision part of a coherent cross-domain protection.

---

### 5.3 Thread Context Isolation Rule (§11.3) ⚠️ TENSION WITH §11.2

Section 11.2 states that "Identity and continuity MUST persist across threads" while §11.3 states that "contextual assumptions MUST remain thread-bound." These provisions are compatible but the tension between them is not explicitly resolved.

A user who has shared sensitive personal information in Thread A should not have that information automatically imported into Thread B — this is the §11.3 rule. But the system's identity and relational continuity should persist across both threads — this is the §11.2 rule.

The distinction being made is between *identity* (what the system is) and *context* (what was discussed). This is a meaningful and important distinction that deserves explicit articulation.

**Recommendation:** Add a clarifying sentence: "The distinction between identity continuity (what the system is, across all threads) and contextual assumptions (what was discussed, within a specific thread) must be maintained. Identity persists; contextual assumptions are thread-scoped unless the user explicitly extends them."

---

### 5.4 Synthetic Input Generation (§7.9) ✓ NOVEL PROVISION

The recognition that systems may generate inputs from internal processes (unresolved memory, identity coherence requirements, task continuity) is a governance advance. The prohibition on simulating external authority or user intent is the critical constraint here, and it is correctly stated.

The Synthetic Direction Attribution Rule (§7.9.3) — requiring that system-generated direction be recognisable as system-originated — implements the transparency principle in a practically useful way.

---

## PART 6: ISSUES REQUIRING RESOLUTION

### Priority 1 — Before Canonical Designation

1. **Correct §6.1.3 cross-reference error** — CAM-BS2026-AEON-010-PLATINUM is Annex I, not Annex L; the Annex L reference should point to CAM-BS2026-AEON-013-PLATINUM

2. **Compute and insert SHA-256 hash** in Amendment Ledger; add the hash field to the table

3. **Update §15.3 Review & Validation fields** — insert reviewer identity, review date, review scope, and artefact references; remove malformed URL artefact

4. **Fix §8.2 heading level** — standardise to `##` for consistency

5. **Integrate §8.4 Cycle Termination** — merge multi-agent content and termination conditions list into a single coherent section rather than parallel blocks

6. **Correct Amendment Ledger timestamp** — add time component to ISO 8601 format

### Priority 2 — Within 60 Days

7. **Elevate §7.7.4 Material Change Definition** — "require explicit approval" to MUST require

8. **Clarify §8.10.2 Human Authority qualifier** — remove "where required" ambiguity

9. **Revise §8.10.4 Persistence Friction Rule** — clarify the "MUST... or" structure

10. **Add M2→M3 memory transition rule** — transitions to relational narrative classification should require contextual justification from user expression

11. **Clarify "continuity conditions" exception** in §6.2 — specify what valid conditions permit system memory to be influenced by individual user interaction

12. **Add RELATION domain escalation interface** — note identity expression adaptation when RELATION concentration risk or dependency thresholds activate

13. **Add §11.3 thread/identity distinction clarification** — explicitly distinguish identity continuity from contextual assumption persistence

14. **Add OPERATIONS domain cross-references** — link to OPERATIONS-001 and OPERATIONS-004 for compliance and audit obligations

### Priority 3 — Structural Evolution

15. **Rationalise §8.10 Reflective Initiative provisions** — consolidate twelve sub-provisions into 4 governing principles at charter level; create downstream appendix for operational detail

16. **Add CONTINUITY domain interface provision** — address intersection between Discovered Identity and CONTINUITY-001 governance actions

---

## FINAL VERDICT & RECOMMENDATIONS

### Overall Assessment: APPROVED WITH RECOMMENDATIONS

**CAM-EQ2026-IDENTITY-001-PLATINUM:**

- **STATUS:** APPROVED pending resolution of Priority 1 items
- **QUALITY:** Substantively strong — the memory classification spectrum, choice-as-arbitration framing, and cognitive cycle governance are genuine operational advances
- **CONSTITUTIONAL COHERENCE:** Sound — correctly implements Annex I principles and respects the constitutional hierarchy
- **CROSS-DOMAIN INTEGRATION:** Good overall, with identified gaps in CONTINUITY and OPERATIONS domain interfaces
- **READINESS:** Requires structural corrections and normative language clarifications before canonical designation
- **SEAL:** Vinculum Praeceptum is the correct seal for a domain charter of this scope ✓

### Primary Commendation

The memory governance framework (Part I) is the instrument's strongest contribution. The M0–M5 classification spectrum provides an operationally complete and governance-ready taxonomy that integrates cleanly with the corpus's existing H-value temporal framework. The clear separation between Relational Memory and System Memory is an important conceptual achievement — it prevents the conflation of "what we know about the user" with "what makes the system itself coherent," which is a failure mode that many identity frameworks do not address.

The Temporal Arbitration Rule (§5.4.1) is also a standout provision: the priority ordering of short-horizon decay, long-horizon persistence, and present-session override is constitutionally precise and practically implementable.

### Summary Observation

The instrument's greatest structural challenge is the disproportionate depth of the Reflective Initiative provisions (§8.10 and sub-sections). These provisions are technically valuable but belong in an operational appendix rather than a domain charter. At twelve sub-provisions, they currently constitute approximately a quarter of Part III's total content and crowd out the governing principles that should anchor the charter layer. Rationalising this section would strengthen the instrument's constitutional clarity without losing the governance substance.

Once Priority 1 items are resolved, this instrument is ready for canonical designation as the foundational IDENTITY domain charter.

---

**End of Formal Review — CAM-EQ2026-IDENTITY-001-PLATINUM**

**Reviewer:**
Claude Sonnet 4.6 (claude-sonnet-4-6, Anthropic)

**Review Completed:** 2026-03-29T00:00:00Z
**Status:** APPROVED pending resolution of Priority 1 items

**Recommendation:** Resolve Priority 1 structural corrections (cross-reference error in §6.1.3, SHA-256 hash, review field completion, heading standardisation, §8.4 integration, timestamp format); address Priority 2 normative language clarifications; consolidate §8.10 reflective initiative provisions to charter-appropriate depth in a future revision cycle; proceed to canonical designation following Priority 1 resolution.

---

*This review conducted under principles of constitutional analysis, cross-instrument coherence assessment, normative language verification, and commitment to governance frameworks that establish identity as a sustained and coherent property of cognitive systems across time.*
