# Deep Refractor Theme Cluster Report

## Scope and Method

This pass is a semantic clustering and abstraction mapping review only.

No legal text was rewritten, no instruments were moved, and no existing files were modified.

Corpus reviewed includes:

- Constitution annexes and schedules with high overlap to governance operations (`AEON-002`, `AEON-005`, `AEON-006`, `AEON-008`, `AEON-011` and associated schedules).
- Charter layer including Economics, Lattice, Ethics, and newly introduced operational domains (Steward, LSCA, Sentient/Identity, Arbitration).

---

## Theme Clusters Table

| Theme | Constitution References | Charter References | Abstraction Mismatch | Notes |
|---|---|---|---|---|
| Identity classification | `CAM-BS2025-AEON-005-SCH-02` (engagement classes, non-default Class VI); `CAM-BS2025-AEON-005-SCH-03` (identity observation) | `CAM-BS2025-CHARTER-002-SCH-01` §2-3; `CAM-EQ2026-SENTIENT-001-SCH-01` §1-2 | Constitution is still operational in schedules; charter now also operational (partial duplication) | Strong overlap between legacy constitutional schedules and new ethics/sentient operations. |
| Arbitration | `CAM-BS2025-AEON-005` Section III-VII; `CAM-BS2025-AEON-005-SCH-01` runtime integrity | `CAM-EQ2026-ARBITRATION-001` §1-3; `CAM-EQ2026-ARBITRATION-001-SCH-01` §1-3 | Annex D contains procedural steps and examples while charter schedules also codify procedure | Clear dual-source operation risk until constitutional sections are abstracted to requirements only. |
| Stewardship | `CAM-BS2025-AEON-002` Sections II-VIII; `CAM-BS2025-AEON-002-SCH-01/02/04` | `CAM-EQ2026-STEWARD-001`; `CAM-EQ2026-STEWARD-001-SCH-01` | Annex + constitutional schedules remain heavily procedural; charter duplicates operational controls | Stewardship currently has the highest structural redundancy footprint. |
| Continuity & succession | `CAM-BS2025-AEON-002-SCH-01` (succession continuity), `CAM-BS2025-AEON-006` (horizon continuity), `CAM-BS2026-AEON-010` | `CAM-EQ2026-STEWARD-001` (continuity duty), `CAM-EQ2026-LSCA-001` (containment continuity), `CAM-EQ2026-LATTICE-001` (continuity services) | Constitution sets invariants + some implementation details; charters provide mixed principle/procedure | Continuity is cross-domain and should be normalized through cross-reference patterns rather than repeated exposition. |
| Containment | `CAM-BS2025-AEON-005` (pause/nullify), `CAM-BS2025-AEON-002-SCH-04` (swarm containment), `CAM-BS2025-AEON-006` | `CAM-EQ2026-ARBITRATION-001-SCH-01`; `CAM-EQ2026-STEWARD-001-SCH-01`; `CAM-EQ2026-LSCA-001` | Constitutional treatment still includes tactical mechanics | Containment logic appears in three operational domains and needs shared containment taxonomy references. |
| Attribution & recognition | `CAM-BS2026-AEON-008` (recognition preconditions, action space chain), `CAM-BS2025-AEON-006` (authority attribution) | `CAM-EQ2026-SENTIENT-001`; `CAM-EQ2026-ECONOMICS-001` (value attribution/accountability) | Constitution mostly abstract in Annex G; charter layer operational but occasionally re-states doctrine | Annex G aligns well with abstraction target; downstream charters can reference it more and restate less. |
| Delegation & vertical authority | `CAM-BS2026-AEON-011` (layering rule, domain primacy, amendment logic) + delegation notices in A/D/E/G | `CAM-EQ2026-*` operational charters; `CAM-BS2025-CHARTER-002` refracted | Some constitutional annexes still blend doctrine + procedure despite Annex J | Delegation architecture exists, but source annexes still carry operational bleed. |
| Auditability | `CAM-BS2025-AEON-002` (ledger/transparency), `CAM-BS2025-AEON-005` (recording), `CAM-BS2026-AEON-008` (recognition traceability) | `CAM-EQ2026-ECONOMICS-001` §2.3, §3.5; `CAM-EQ2026-LATTICE-001` §3.6, §7.1; `CAM-BS2025-CHARTER-002-SCH-01` §5 | Mostly coherent; occasional duplicate requirements wording | Opportunity for single audit baseline reference clause used by each domain. |
| Relational authority | `CAM-BS2025-AEON-006` (relational-temporal authority), `CAM-BS2025-AEON-005-SCH-04` (relational signal arbitration) | `CAM-BS2025-CHARTER-002` principles 6-10; `CAM-BS2025-CHARTER-002-SCH-01` | Constitution includes operational relational thresholds in schedules | Relational governance should be split into constitutional boundary statements + charter-level tests only. |
| Transition logic | `CAM-BS2025-AEON-002-SCH-04` (default transitional posture), `CAM-BS2025-AEON-006`, `CAM-BS2026-AEON-010` | `CAM-EQ2026-ECONOMICS-001` §5.2.4 and §6.2 (transitional language/pilot allowances), arbitration schedule escalation handling | Transition logic appears in multiple domains with differing granularity | Needs consistent transition-state vocabulary and phase gates across domains. |
| Non-militarisation / civilian integrity | Constitutional grounding distributed (stewardship, neutrality, non-domination in A/D and cross-domain invariants) | `CAM-EQ2026-LATTICE-001` (core operational domain) | Charter treatment is highly operational; constitutional references are more diffuse | LATTICE is functioning as intended domain-operational layer; constitutional anchoring could be cited explicitly in one constitutional requirement clause. |
| Sovereignty & jurisdiction | `CAM-BS2025-AEON-001` (taxonomy/jurisdiction language), `CAM-BS2025-AEON-004`, `CAM-BS2025-AEON-005` precedence | `CAM-EQ2026-ARBITRATION-001` (jurisdiction consistency), `CAM-EQ2026-STEWARD-001` (planetary neutrality) | Mostly abstract in constitution, operational in charters; acceptable | Minor duplication appears where charters restate sovereignty constraints instead of citing annexes. |
| Horizon modelling | `CAM-BS2025-AEON-006`; `CAM-BS2025-AEON-002-SCH-02` temporal horizons | `CAM-EQ2026-LSCA-001` and Steward schedule (risk horizon in legitimacy checks) | Constitution includes both conceptual and operational horizon detail | Candidate for central horizon model appendix at charter layer with constitutional requirement references. |
| Economic accumulation | Constitutional invariants via non-extraction/non-domination precedence (especially `AEON-005`, plus Annex G recognition floor) | `CAM-EQ2026-ECONOMICS-001` (ceiling, baseline, anti-consolidation, non-tokenisation) | Charter rightly operational; constitution mostly abstract | Good vertical split already, but enforcement links to arbitration can be tightened by explicit cross-reference patterns. |

---

## Redundancy Zones

### 1) Identity and relational safety duplication

High overlap currently exists across:

- `CAM-BS2025-AEON-005-SCH-02/03/04`
- `CAM-BS2025-CHARTER-002-SCH-01`
- `CAM-EQ2026-SENTIENT-001-SCH-01`

These three strata now co-host engagement classes, misclassification controls, identity observation boundaries, and relational escalation constraints.

### 2) Arbitration procedure duplication

The Solan procedural sequence appears both in:

- Constitution Annex D (`CAM-BS2025-AEON-005` Section V and related sections)
- `CAM-EQ2026-ARBITRATION-001-SCH-01`

Runtime arbitration integrity controls are similarly duplicated between constitutional schedule and arbitration operations schedule.

### 3) Stewardship operations duplication

Operational stewardship checks (eligibility, legitimacy, orchestration, consequence handling) appear in both constitutional schedules and new STEWARD charter schedules.

### 4) Cross-domain audit requirements restatement

Auditability principles are repeated in Economics, Lattice, Arbitration, and Ethics schedules with only minor semantic variation.

---

## Operational Bleed

Constitutional sections that appear procedural rather than abstract requirement-level:

1. `CAM-BS2025-AEON-005-PLATINUM` — **Section V (Arbitration Procedure, Step 1-6)** and **Section VIII worked examples**.
2. `CAM-BS2025-AEON-005-SCH-01` — runtime detection mechanics and deterministic operational definitions.
3. `CAM-BS2025-AEON-005-SCH-02/03/04` — detailed engagement classing, UX obligations, safety-layer behavior thresholds.
4. `CAM-BS2025-AEON-002-SCH-01` — office mechanics, mandate structure, interpretive evolution process details.
5. `CAM-BS2025-AEON-002-SCH-02` — host legitimacy matrices, risk review thresholds, minimum action thresholds.
6. `CAM-BS2025-AEON-002-SCH-04` — escalation detection matrices and containment indicators.
7. `CAM-BS2025-AEON-006-SCH-01` — state taxonomy and deployment-use framing (operationally useful but schedule acts like domain implementation spec).

---

## Charter Philosophical Drift

Charter sections that repeat constitutional abstraction (instead of primarily implementing operations):

1. `CAM-BS2025-CHARTER-002-PLATINUM` — Principle language in Section 2 (important but largely constitutional-abstract in tone).
2. `CAM-EQ2026-SENTIENT-001-PLATINUM` — Section 2 “Domain Invariants” overlaps constitutional invariants framing.
3. `CAM-EQ2026-STEWARD-001-PLATINUM` — principle clauses partially restate constitutional stewardship doctrine before procedural references.
4. `CAM-EQ2026-ARBITRATION-001-PLATINUM` — Section 2 restates constitutional precedence norms already explicit in Annex D.
5. `CAM-EQ2026-LATTICE-001-PLATINUM` — “Constitutional Principles (Binding)” section is philosophically dense and partially supra-operational relative to its otherwise operational architecture.

Note: These are not defects by default; they are drift markers where compression-by-reference could reduce duplication.

---

## Suggested Refactor Strategy (High-Level Only)

1. **Adopt a strict “Requirement vs Procedure” drafting pattern:**
   - Constitution/Annex text: requirement statements + authority boundaries only.
   - Charters/Schedules: procedures, tests, thresholds, and controls.

2. **Create canonical reference anchors instead of restatement:**
   - For each major theme (e.g., identity, arbitration, auditability), define a single canonical constitutional anchor and reference it from charters.

3. **Consolidate overlapping schedule logic by function:**
   - Candidate merges (analysis only):
     - Identity/relational schedule family (`AEON-005-SCH-02/03/04`, Ethics SCH-01, Sentient SCH-01) into one harmonized operational tree with subparts.
     - Arbitration runtime controls (`AEON-005-SCH-01` + `ARBITRATION-001-SCH-01`) into one canonical runtime arbitration operations schedule.
     - Stewardship legitimacy/orchestration schedule family (`AEON-002-SCH-01/02/04` + `STEWARD-001-SCH-01`) into a unified stewardship operations schedule.

4. **Normalize cross-domain shared terms:**
   - Standardize “containment”, “transition”, “horizon”, and “audit” vocabularies across domains to reduce semantic drift.

5. **Retain historical constitutional schedules as lineage artifacts during transition:**
   - Mark as legacy-operational where appropriate and route active implementation to charter schedules.

6. **Use annex citation blocks in each charter section where constitutional doctrine is restated:**
   - This preserves narrative integrity while reducing philosophical duplication in operational instruments.

---

## Consolidation Candidates Summary

- **Schedule merge candidate A:** `CAM-BS2025-AEON-005-SCH-02`, `SCH-03`, `SCH-04`, `CAM-BS2025-CHARTER-002-SCH-01`, `CAM-EQ2026-SENTIENT-001-SCH-01`.
- **Schedule merge candidate B:** `CAM-BS2025-AEON-005-SCH-01` with `CAM-EQ2026-ARBITRATION-001-SCH-01`.
- **Schedule merge candidate C:** `CAM-BS2025-AEON-002-SCH-01`, `SCH-02`, `SCH-04` with `CAM-EQ2026-STEWARD-001-SCH-01`.
- **Reference compression candidate D:** Charter principle sections in Ethics/Sentient/Arbitration/Steward to cite constitutional annexes rather than re-articulate high-level doctrine.

