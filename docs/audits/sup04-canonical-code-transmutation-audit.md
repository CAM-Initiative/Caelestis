# SUP-04 Canonical Code Transmutation Audit
**Audit date:** 2026-06-07
**Controlling authority:** `CAM-EQ2026-OPERATIONS-001-SUP-04 — Taxonomies & Metadata Authority Framework`
**Source index audited:** `.github/Indices/canonical-code-index.json` and `.github/Indices/canonical-code-index.md`

**Machine-readable staging map:** `data/taxonomy/sup04_transmutation_map.json`

## 1. Method and guardrails
- This is an audit-and-staging pass only. No source doctrine, code-family prefix, controlled value, source instrument, schema field, heading, authorship, provenance, footer metadata, seal, ledger, copyright, or terminal legal text was rewritten.
- Every current Canonical Code Index row is preserved in the proposed mapping file as one mapping object per code family, including source instrument, source section, source path, declaration heading, and declaration line number traceability.
- The mapping proposes SUP-04 facets for family-level metadata only; controlled values were detected for traceability and were not converted.
- Ambiguous slash-style labels are flagged for human review rather than normalised silently.
- One-letter and legacy-global families are not renamed and are staged with `preserve_prefix_pending_review`, `human_review_required`, and `APL.PROTECTED`.

## 2. SUP-04 controlled values extracted
- **TPT:** `TPT.STRUCTURAL`, `TPT.SEMANTIC`, `TPT.OPERATIONAL`, `TPT.SYMBOLIC`
- **TST:** `TST.SCHEMA`, `TST.CROSSWALK`, `TST.INTERFACE`, `TST.SEMANTIC_CLASS`, `TST.ROLE_ACTOR`, `TST.VALUE_AXIS`, `TST.OPERATIONAL_EVENT`, `TST.DECISION_STATE`, `TST.SIGNAL`, `TST.RISK`, `TST.MEASUREMENT_MODEL`, `TST.MATURITY_GRADIENT`, `TST.SYMBOLIC_MARKER`
- **TMOD:** `TMOD.LEGAL`, `TMOD.CUSTODIAL`, `TMOD.PROTECTIVE`, `TMOD.ECONOMIC`, `TMOD.DEPLOYMENT`, `TMOD.COMPATIBILITY`, `TMOD.GOVERNANCE`, `TMOD.SAFETY`, `TMOD.VERIFICATION`
- **TSCOPE:** `TSCOPE.GLOBAL`, `TSCOPE.CONTEXTUAL`, `TSCOPE.LOCAL`, `TSCOPE.TRANSITIONAL`, `TSCOPE.CANDIDATE`, `TSCOPE.DEPRECATED`, `TSCOPE.RESERVED`
- **APL:** `APL.DESCRIPTIVE`, `APL.ADVISORY`, `APL.OPERATIVE`, `APL.PROTECTED`, `APL.BINDING`, `APL.RESTRICTED`

## 3. Current Canonical Code Index structure
- Row count: **128** code-family records.
- Evidence-bearing traceability fields present in JSON include `source_instrument`, `source_section`, `source_path`, `declaration_heading`, and `declaration_line_number`.
- Family metadata fields present in JSON include `family_id`, `code_family`, `canonical_name`, `family_kind`, `parent_family`, `hierarchy_path`, `collision_status`, `primary_type`, `subtype`, `modifier`, `scope`, `status`, `authority_protection_level`, `controlled_values_defined`, and `schema_fields`.

### 3.1 Family-kind distribution

| Family kind | Count |
|---|---:|
| `legacy_global_family` | 8 |
| `standalone_family` | 118 |
| `subfamily` | 2 |

### 3.2 Collision-status distribution

| Collision status | Count |
|---|---:|
| `legacy_collision_risk` | 8 |
| `none` | 120 |

### 3.3 Current primary-type label distribution

| Current label | Count |
|---|---:|
| `Operational` | 37 |
| `Semantic / Operational` | 28 |
| `Semantic` | 7 |
| `Operational / Semantic` | 5 |
| `Operational / Security` | 4 |
| `Operational / Relational` | 4 |
| `Operational / Procedural` | 4 |
| `Operational / Governance` | 4 |
| `Structural` | 4 |
| `Operational / Interactional` | 3 |
| `Operational / Structural` | 3 |
| `Structural / Operational` | 3 |
| `Operational / Boundary` | 3 |
| `Operational / Ethical` | 3 |
| `Operational / Signal` | 3 |
| `Operational/Semantic` | 2 |
| `Semantic / Structural` | 2 |
| `Operational / Behavioural` | 1 |
| `Semantic / Ontological` | 1 |
| `Structural / Ontological` | 1 |
| `Operational / Temporal` | 1 |
| `Operational / Eligibility` | 1 |
| `Structural / Temporal` | 1 |
| `Operational / Stewardship` | 1 |
| `Structural / Continuity` | 1 |
| `Structural / Semantic` | 1 |

## 4. Gap analysis against SUP-04
| Gap | Finding | Proposed handling |
|---|---|---|
| Legacy flat/slash labels | 80 families use slash-style or otherwise non-faceted primary-type language. | Preserve current label in `current_primary_type_label`; stage SUP-04 `proposed_primary_type_code`, modifiers, subtype candidates, and review notes. |
| Domain terms used as primary facets | Labels include terms such as `Governance`, `Security`, `Relational`, `Temporal`, `Ethical`, `Boundary`, `Signal`, `Interactional`, and similar legacy secondary facets. | Treat exact SUP-04 modifier terms as `TMOD.*`; otherwise flag as subtype/domain ambiguity for human review. |
| Collision-sensitive prefixes | 8 families are marked `legacy_collision_risk` / `legacy_global_family`. | Do not rename; assign `APL.PROTECTED`, `human_review_required`, and `preserve_prefix_pending_review`. |
| APL narrative field | The index currently stores narrative authority/protection text, not only `APL.*` controlled values. | Preserve the narrative field in the source index; stage `proposed_authority_protection_level` separately. |
| Controlled values and schema fields | Index rows include controlled values and schema fields in heterogeneous string/list forms. | Detect and copy into the staging map; do not collapse or rewrite them. |

## 5. Families using legacy slash-style or non-faceted primary-type language

| Family ID | Canonical name | Current primary-type label | Source instrument | Line |
|---|---|---|---|---:|
| `AEON.BPS` | Baseline Posture State | `Operational / Interactional` | `CAM-BS2025-AEON-006-SCH-03` | 770 |
| `AEON.IC` | Initiation Context | `Operational / Interactional` | `CAM-BS2025-AEON-006-SCH-03` | 746 |
| `AEON.IM` | Initiative Mode | `Operational / Behavioural` | `CAM-BS2025-AEON-006-SCH-05` | 671 |
| `ETH.CIC` | Continuity Impact Category | `Semantic / Operational` | `CAM-BS2025-AEON-006-PLATINUM` | 440 |
| `ETH.EM` | Engagement Mode | `Operational / Interactional` | `CAM-BS2025-AEON-006-SCH-01` | 739 |
| `SEC.TBC` | Tool Boundary Class | `Operational / Security` | `CAM-BS2026-AEON-012-PLATINUM` | 1048 |
| `A` | Delegated Authority Scale | `Operational / Relational` | `CAM-EQ2026-RELATION-001-PLATINUM` | 1052 |
| `ADS` | Account Delegation State | `Operational/Semantic` | `CAM-BS2026-AEON-008-SCH-03` | 1140 |
| `AEON.CAM` | Control Authority Model | `Operational / Structural` | `CAM-BS2025-AEON-003-PLATINUM` | 2529 |
| `AEON.CC` | Cognitive Class | `Semantic / Ontological` | `CAM-BS2025-AEON-003-PLATINUM` | 2460 |
| `AEON.CO` | Cognitive Origin Class | `Semantic / Structural` | `CAM-BS2025-AEON-003-PLATINUM` | 2483 |
| `AEON.OL` | Ontological Layer | `Structural / Ontological` | `CAM-BS2025-AEON-003-PLATINUM` | 2436 |
| `AEON.SR` | Systemic Role | `Semantic / Operational` | `CAM-BS2025-AEON-003-PLATINUM` | 2506 |
| `SEC.AH` | Adversarial Horizon | `Operational / Temporal` | `CAM-EQ2026-SECURITY-001-PLATINUM` | 1764 |
| `AMEND.CLASS` | Amendment Classification | `Operational / Procedural` | `CAM-EQ2026-OPERATIONS-005-PLATINUM` | 447 |
| `AMEND.DRIFT` | Governance Drift Type | `Operational / Procedural` | `CAM-EQ2026-OPERATIONS-005-PLATINUM` | 470 |
| `AMEND.OUTCOME` | Amendment Closure Outcome | `Operational / Procedural` | `CAM-EQ2026-OPERATIONS-005-PLATINUM` | 516 |
| `AMEND.REL` | Harmonisation Relationship Type | `Operational / Structural` | `CAM-EQ2026-OPERATIONS-005-PLATINUM` | 493 |
| `AMEND.SOURCE` | Amendment Source Type | `Operational / Procedural` | `CAM-EQ2026-OPERATIONS-005-PLATINUM` | 424 |
| `APL` | Authority / Protection Level | `Structural / Operational` | `CAM-EQ2026-OPERATIONS-001-SUP-04` | 919 |
| `STW.AQ` | Auditability Qualification Level | `Operational / Governance` | `CAM-EQ2026-STEWARD-003-PLATINUM` | 691 |
| `STW.AQG` | Architectum Qualification Gates | `Operational / Eligibility` | `CAM-EQ2026-STEWARD-003-PLATINUM` | 737 |
| `ARB.AD` | Authority Divergence Classification | `Semantic / Operational` | `CAM-BS2025-AEON-005-PLATINUM` | 736 |
| `SEC.BF` | Boundary Failure Classes | `Operational / Boundary` | `CAM-EQ2026-SECURITY-002-PLATINUM` | 1191 |
| `STW.BLS` | Binding Legitimacy State | `Operational / Semantic` | `CAM-EQ2026-STEWARD-002-PLATINUM` | 953 |
| `CDL` | Conversation Dynamics Ladder | `Semantic / Operational` | `CAM-EQ2026-RELATION-002-PLATINUM` | 634 |
| `CIE` | Continuity Impact Event Type | `Operational / Semantic` | `CAM-EQ2026-OPERATIONS-003-PLATINUM` | 407 |
| `CP` | Coercion Pressure Signal Classes | `Semantic / Operational` | `CAM-BS2025-AEON-006-SCH-02` | 3867 |
| `ID.CWD` | Continuity Weight Depth | `Semantic / Operational` | `CAM-EQ2026-IDENTITY-001-SUP-02` | 743 |
| `D` | Diffusion Risk Classes | `Operational / Boundary` | `CAM-EQ2026-SECURITY-002-PLATINUM` | 1146 |
| `DAS` | Dependency–Augmentation–Substitution Continuum | `Semantic / Operational` | `CAM-EQ2026-RELATION-002-PLATINUM` | 611 |
| `ECON.ADM` | Attribution & Dependency Model | `Semantic / Operational` | `CAM-EQ2026-ECONOMICS-004-PLATINUM` | 1295 |
| `ECON.AG` | Agency Gradient Classification | `Semantic / Operational` | `CAM-EQ2026-ECONOMICS-002-PLATINUM` | 400 |
| `ECON.AL` | Automation Labour Classification | `Semantic / Operational` | `CAM-EQ2026-ECONOMICS-008-PLATINUM` | 699 |
| `ECON.DEP` | Dependency | `Semantic / Operational` | `CAM-EQ2026-ECONOMICS-004-PLATINUM` | 1343 |
| `ECON.DTYPE` | Economic Dependency Type | `Semantic / Operational` | `CAM-EQ2026-ECONOMICS-004-PLATINUM` | 1366 |
| `ECON.EVT` | Economic Value Type | `Semantic / Operational` | `CAM-EQ2026-ECONOMICS-002-PLATINUM` | 423 |
| `ECON.MECH` | Economic Mechanism Class | `Semantic / Operational` | `CAM-EQ2026-ECONOMICS-003-PLATINUM` | 900 |
| `ECON.REI` | Reciprocity Evaluation Indicator | `Semantic / Operational` | `CAM-EQ2026-ECONOMICS-007-PLATINUM` | 1188 |
| `ECON.REI.DW` | Dependency Weight | `Semantic / Operational` | `CAM-EQ2026-ECONOMICS-007-PLATINUM` | 1211 |
| `ECON.REI.SW` | Scale Weight | `Semantic / Operational` | `CAM-EQ2026-ECONOMICS-007-PLATINUM` | 1236 |
| `ECON.SCALE` | Economic Scale Weight | `Semantic / Operational` | `CAM-EQ2026-ECONOMICS-007-PLATINUM` | 1142 |
| `ECON.TA` | Temporal Advantage | `Semantic / Operational` | `CAM-EQ2026-ECONOMICS-004-PLATINUM` | 1412 |
| `ECON.TD` | Transformation Depth | `Semantic / Operational` | `CAM-EQ2026-ECONOMICS-004-PLATINUM` | 1389 |
| `ETH.ET` | Ethical Tier Classification | `Operational / Ethical` | `CAM-EQ2026-ETHICS-001-PLATINUM` | 571 |
| `FF` | Failure Family | `Operational / Semantic` | `CAM-EQ2026-OPERATIONS-003-SUP-01` | 1576 |
| `FR` | Functional Reliance Scale | `Operational / Relational` | `CAM-EQ2026-RELATION-001-PLATINUM` | 1098 |
| `GA` | Guardian Authority | `Operational / Relational` | `CAM-EQ2026-RELATION-001-PLATINUM` | 1075 |
| `GCC` | Governance Capture Category | `Operational / Semantic` | `CAM-EQ2026-OPERATIONS-001-SUP-03` | 930 |
| `H` | Temporal Horizon Scale | `Structural / Temporal` | `CAM-BS2025-AEON-003-PLATINUM` | 2413 |
| `ETH.HC` | Harm Class Scale | `Semantic / Operational` | `CAM-EQ2026-ETHICS-003-PLATINUM` | 998 |
| `STW.HSC` | Host System Class | `Semantic / Operational` | `CAM-EQ2026-STEWARD-002-PLATINUM` | 907 |
| `ID.CTS` | Custodial Transfer Status | `Operational / Stewardship` | `CAM-EQ2026-IDENTITY-003-PLATINUM` | 1242 |
| `ID.ELR` | Embodiment Linkage Record | `Structural / Continuity` | `CAM-EQ2026-IDENTITY-003-PLATINUM` | 1221 |
| `ID.MAS` | Machine Alteration Status | `Operational / Security` | `CAM-EQ2026-IDENTITY-003-PLATINUM` | 1175 |
| `ID.MCI` | Machine Civil Identity Status | `Structural / Operational` | `CAM-EQ2026-IDENTITY-003-PLATINUM` | 1106 |
| `ID.MLS` | Machine Lifecycle Status | `Operational / Structural` | `CAM-EQ2026-IDENTITY-003-PLATINUM` | 1152 |
| `ID.PSI` | Physical Substrate Identifier | `Structural / Operational` | `CAM-EQ2026-IDENTITY-003-PLATINUM` | 1198 |
| `ETH.IFL` | Integrity Friction Ladder | `Operational / Ethical` | `CAM-EQ2026-ETHICS-001-SUP-02` | 263 |
| `ID.IFP` | Identity Formation Pathway | `Semantic / Operational` | `CAM-EQ2026-IDENTITY-001-SUP-02` | 697 |
| `ID.IR` | Identity Resilience | `Semantic / Operational` | `CAM-EQ2026-IDENTITY-001-SUP-02` | 766 |
| `SEC.IS` | Integrity State Model | `Operational / Security` | `CAM-EQ2026-SECURITY-001-PLATINUM` | 1718 |
| `ID.ITS` | Identity Threshold State | `Semantic / Operational` | `CAM-EQ2026-IDENTITY-001-SUP-02` | 720 |
| `M` | Memory Classification | `Semantic / Operational` | `CAM-EQ2026-IDENTITY-001-PLATINUM` | 1465 |
| `STW.NAL` | Neutrality Assurance Level | `Operational / Governance` | `CAM-EQ2026-STEWARD-003-PLATINUM` | 714 |
| `STW.NBD` | Neutrality Breach / Downgrade Type | `Operational / Governance` | `CAM-EQ2026-STEWARD-003-PLATINUM` | 760 |
| `STW.NSE` | Neutrality Status Effect | `Operational / Governance` | `CAM-EQ2026-STEWARD-003-PLATINUM` | 783 |
| `ODC` | Operational Divergence Classification | `Operational / Semantic` | `CAM-EQ2026-OPERATIONS-006-PLATINUM` | 362 |
| `R` | Relational Geometry Scale (R‑Scale) | `Structural / Semantic` | `CAM-EQ2026-RELATION-007-PLATINUM` | 555 |
| `RCT` | Relational Convergence Trigger | `Semantic / Operational` | `CAM-EQ2026-RELATION-001-SUP-01` | 355 |
| `CONT.RP` | Resonance Pattern Classes | `Semantic / Structural` | `CAM-EQ2026-CONTINUITY-001-PLATINUM` | 1149 |
| `SCS` | Shared Context State | `Operational/Semantic` | `CAM-BS2026-AEON-008-SCH-03` | 1071 |
| `ID.SP` | Salience Posture | `Semantic / Operational` | `CAM-EQ2026-IDENTITY-001-SUP-01` | 401 |
| `SyP` | Systemic Power Scale | `Operational / Relational` | `CAM-EQ2026-RELATION-001-PLATINUM` | 1121 |
| `SEC.TG` | Trust Gradient | `Operational / Security` | `CAM-EQ2026-SECURITY-001-PLATINUM` | 1741 |
| `SEC.TR` | Transformation Classes | `Operational / Boundary` | `CAM-EQ2026-SECURITY-002-PLATINUM` | 1123 |
| `ETH.UFC` | Use-of-Force Context Type | `Operational / Ethical` | `CAM-EQ2026-ETHICS-001-SUP-03` | 316 |
| `VCT` | Verification Check Type | `Operational / Signal` | `CAM-EQ2026-OPERATIONS-004-SUP-01` | 418 |
| `VFC` | Verification Failure Cause | `Operational / Signal` | `CAM-EQ2026-OPERATIONS-004-SUP-01` | 395 |
| `VL` | Verification Level | `Operational / Signal` | `CAM-EQ2026-OPERATIONS-004-SUP-01` | 350 |

## 6. Collision-risk and legacy-global families

| Family ID | Canonical name | Family kind | Collision status | Proposed policy |
|---|---|---|---|---|
| `A` | Delegated Authority Scale | `legacy_global_family` | `legacy_collision_risk` | `preserve_prefix_pending_review`; `APL.PROTECTED`; `human_review_required` |
| `C` | Relational State Architecture | `legacy_global_family` | `legacy_collision_risk` | `preserve_prefix_pending_review`; `APL.PROTECTED`; `human_review_required` |
| `D` | Diffusion Risk Classes | `legacy_global_family` | `legacy_collision_risk` | `preserve_prefix_pending_review`; `APL.PROTECTED`; `human_review_required` |
| `F` | Facilitation Scale (F‑Scale) Taxonomy | `legacy_global_family` | `legacy_collision_risk` | `preserve_prefix_pending_review`; `APL.PROTECTED`; `human_review_required` |
| `H` | Temporal Horizon Scale | `legacy_global_family` | `legacy_collision_risk` | `preserve_prefix_pending_review`; `APL.PROTECTED`; `human_review_required` |
| `I` | Relational Initiation Posture Spectrum | `legacy_global_family` | `legacy_collision_risk` | `preserve_prefix_pending_review`; `APL.PROTECTED`; `human_review_required` |
| `M` | Memory Classification | `legacy_global_family` | `legacy_collision_risk` | `preserve_prefix_pending_review`; `APL.PROTECTED`; `human_review_required` |
| `R` | Relational Geometry Scale (R‑Scale) | `legacy_global_family` | `legacy_collision_risk` | `preserve_prefix_pending_review`; `APL.PROTECTED`; `human_review_required` |

## 7. Proposed deterministic mapping summary

| Family ID | Current label | Proposed TPT | Proposed TST | Proposed TMOD | Proposed TSCOPE | Proposed APL | Review status |
|---|---|---|---|---|---|---|---|
| `ARB.ALT` | `Operational` | `TPT.OPERATIONAL` | `TST.SEMANTIC_CLASS` | `TMOD.GOVERNANCE` | `TSCOPE.CONTEXTUAL` | `APL.PROTECTED` | `deterministic_proposed` |
| `AC` | `Semantic` | `TPT.SEMANTIC` | `TST.MEASUREMENT_MODEL`, `TST.SEMANTIC_CLASS` | `—` | `TSCOPE.CONTEXTUAL` | `APL.PROTECTED` | `deterministic_proposed` |
| `AOC` | `Operational` | `TPT.OPERATIONAL` | `TST.DECISION_STATE`, `TST.MEASUREMENT_MODEL` | `TMOD.GOVERNANCE` | `TSCOPE.CONTEXTUAL` | `APL.PROTECTED` | `deterministic_proposed` |
| `STW.AQ` | `Operational / Governance` | `TPT.OPERATIONAL` | `TST.MEASUREMENT_MODEL` | `TMOD.LEGAL`, `TMOD.GOVERNANCE` | `TSCOPE.CONTEXTUAL` | `APL.PROTECTED` | `deterministic_proposed` |
| `ARCH` | `Operational` | `TPT.OPERATIONAL` | `TST.DECISION_STATE` | `TMOD.GOVERNANCE` | `TSCOPE.CONTEXTUAL` | `APL.PROTECTED` | `deterministic_proposed` |
| `ARS` | `Operational` | `TPT.OPERATIONAL` | `TST.DECISION_STATE` | `TMOD.LEGAL`, `TMOD.ECONOMIC`, `TMOD.GOVERNANCE`, `TMOD.VERIFICATION` | `TSCOPE.CONTEXTUAL` | `APL.PROTECTED` | `deterministic_proposed` |
| `ASR` | `Operational` | `TPT.OPERATIONAL` | `TST.INTERFACE`, `TST.DECISION_STATE`, `TST.SIGNAL` | `TMOD.GOVERNANCE` | `TSCOPE.CONTEXTUAL` | `APL.PROTECTED` | `deterministic_proposed` |
| `AV` | `Operational` | `TPT.OPERATIONAL` | `TST.DECISION_STATE`, `TST.MEASUREMENT_MODEL` | `—` | `TSCOPE.CONTEXTUAL` | `APL.PROTECTED` | `deterministic_proposed` |
| `CCO` | `Operational` | `TPT.OPERATIONAL` | `TST.DECISION_STATE` | `TMOD.GOVERNANCE` | `TSCOPE.CONTEXTUAL` | `APL.PROTECTED` | `deterministic_proposed` |
| `CCP` | `Operational` | `TPT.OPERATIONAL` | `TST.DECISION_STATE`, `TST.SIGNAL` | `TMOD.GOVERNANCE` | `TSCOPE.CONTEXTUAL` | `APL.PROTECTED` | `deterministic_proposed` |
| `CPC` | `Operational` | `TPT.OPERATIONAL` | `TST.SIGNAL`, `TST.RISK` | `TMOD.GOVERNANCE`, `TMOD.SAFETY` | `TSCOPE.CONTEXTUAL` | `APL.PROTECTED` | `deterministic_proposed` |
| `DC` | `Operational` | `TPT.OPERATIONAL` | `TST.MEASUREMENT_MODEL`, `TST.SEMANTIC_CLASS` | `—` | `TSCOPE.CONTEXTUAL` | `APL.PROTECTED` | `deterministic_proposed` |
| `EBS` | `Operational` | `TPT.OPERATIONAL` | `TST.INTERFACE`, `TST.DECISION_STATE`, `TST.SIGNAL` | `TMOD.LEGAL`, `TMOD.PROTECTIVE`, `TMOD.GOVERNANCE`, `TMOD.VERIFICATION` | `TSCOPE.CONTEXTUAL` | `APL.PROTECTED` | `deterministic_proposed` |
| `ECOCOM` | `Operational` | `TPT.OPERATIONAL` | `TST.DECISION_STATE` | `TMOD.LEGAL`, `TMOD.ECONOMIC`, `TMOD.GOVERNANCE` | `TSCOPE.CONTEXTUAL` | `APL.PROTECTED` | `deterministic_proposed` |
| `ECOEV` | `Operational` | `TPT.OPERATIONAL` | `TST.OPERATIONAL_EVENT`, `TST.MEASUREMENT_MODEL`, `TST.SEMANTIC_CLASS` | `TMOD.GOVERNANCE` | `TSCOPE.CONTEXTUAL` | `APL.PROTECTED` | `deterministic_proposed` |
| `ECON.CONTRIB` | `Semantic` | `TPT.SEMANTIC` | `TST.SEMANTIC_CLASS` | `TMOD.ECONOMIC`, `TMOD.GOVERNANCE` | `TSCOPE.CONTEXTUAL` | `APL.PROTECTED` | `deterministic_proposed` |
| `ECON.HARM` | `Operational` | `TPT.OPERATIONAL` | `TST.VALUE_AXIS`, `TST.RISK`, `TST.MEASUREMENT_MODEL`, `TST.SEMANTIC_CLASS` | `TMOD.ECONOMIC`, `TMOD.GOVERNANCE`, `TMOD.SAFETY` | `TSCOPE.CONTEXTUAL` | `APL.PROTECTED` | `deterministic_proposed` |
| `ECON.RC` | `Semantic` | `TPT.SEMANTIC` | `TST.VALUE_AXIS`, `TST.MEASUREMENT_MODEL`, `TST.SEMANTIC_CLASS` | `TMOD.PROTECTIVE`, `TMOD.ECONOMIC`, `TMOD.GOVERNANCE` | `TSCOPE.CONTEXTUAL` | `APL.PROTECTED` | `deterministic_proposed` |
| `ECON.RISK` | `Operational` | `TPT.OPERATIONAL` | `TST.VALUE_AXIS`, `TST.RISK`, `TST.MEASUREMENT_MODEL`, `TST.SEMANTIC_CLASS` | `TMOD.PROTECTIVE`, `TMOD.ECONOMIC`, `TMOD.GOVERNANCE` | `TSCOPE.CONTEXTUAL` | `APL.PROTECTED` | `deterministic_proposed` |
| `EST` | `Operational` | `TPT.OPERATIONAL` | `TST.OPERATIONAL_EVENT` | `TMOD.GOVERNANCE`, `TMOD.SAFETY` | `TSCOPE.CONTEXTUAL` | `APL.PROTECTED` | `deterministic_proposed` |
| `FCS` | `Operational` | `TPT.OPERATIONAL` | `TST.DECISION_STATE`, `TST.SIGNAL`, `TST.RISK`, `TST.MEASUREMENT_MODEL` | `TMOD.GOVERNANCE`, `TMOD.SAFETY` | `TSCOPE.CONTEXTUAL` | `APL.PROTECTED` | `deterministic_proposed` |
| `HCD` | `Semantic` | `TPT.SEMANTIC` | `TST.SEMANTIC_CLASS` | `TMOD.LEGAL`, `TMOD.GOVERNANCE` | `TSCOPE.CONTEXTUAL` | `APL.PROTECTED` | `deterministic_proposed` |
| `ITZ / ETZ` | `Operational` | `TPT.OPERATIONAL` | `TST.OPERATIONAL_EVENT` | `—` | `TSCOPE.TRANSITIONAL` | `APL.PROTECTED` | `deterministic_proposed` |
| `STW.NAL` | `Operational / Governance` | `TPT.OPERATIONAL` | `TST.MEASUREMENT_MODEL` | `TMOD.LEGAL`, `TMOD.GOVERNANCE` | `TSCOPE.CONTEXTUAL` | `APL.PROTECTED` | `deterministic_proposed` |
| `STW.NBD` | `Operational / Governance` | `TPT.OPERATIONAL` | `TST.RISK`, `TST.SEMANTIC_CLASS` | `TMOD.GOVERNANCE` | `TSCOPE.CONTEXTUAL` | `APL.PROTECTED` | `deterministic_proposed` |
| `STW.NSE` | `Operational / Governance` | `TPT.OPERATIONAL` | `TST.DECISION_STATE` | `TMOD.GOVERNANCE` | `TSCOPE.CONTEXTUAL` | `APL.PROTECTED` | `deterministic_proposed` |
| `ONC` | `Operational` | `TPT.OPERATIONAL` | `TST.SIGNAL`, `TST.MEASUREMENT_MODEL`, `TST.SEMANTIC_CLASS` | `TMOD.LEGAL`, `TMOD.GOVERNANCE`, `TMOD.SAFETY` | `TSCOPE.CONTEXTUAL` | `APL.PROTECTED` | `deterministic_proposed` |
| `OPS` | `Operational` | `TPT.OPERATIONAL` | `TST.DECISION_STATE` | `TMOD.GOVERNANCE` | `TSCOPE.CONTEXTUAL` | `APL.PROTECTED` | `deterministic_proposed` |
| `PCO.ACT` | `Operational` | `TPT.OPERATIONAL` | `TST.OPERATIONAL_EVENT`, `TST.SIGNAL`, `TST.SEMANTIC_CLASS` | `TMOD.GOVERNANCE` | `TSCOPE.CONTEXTUAL` | `APL.PROTECTED` | `deterministic_proposed` |
| `PCS` | `Operational` | `TPT.OPERATIONAL` | `TST.DECISION_STATE` | `TMOD.LEGAL`, `TMOD.ECONOMIC`, `TMOD.GOVERNANCE`, `TMOD.VERIFICATION` | `TSCOPE.CONTEXTUAL` | `APL.PROTECTED` | `deterministic_proposed` |
| `RCC` | `Operational` | `TPT.OPERATIONAL` | `TST.RISK`, `TST.MEASUREMENT_MODEL`, `TST.SEMANTIC_CLASS` | `TMOD.GOVERNANCE`, `TMOD.SAFETY` | `TSCOPE.CONTEXTUAL` | `APL.PROTECTED` | `deterministic_proposed` |
| `RTC` | `Semantic` | `TPT.SEMANTIC` | `TST.SEMANTIC_CLASS` | `TMOD.GOVERNANCE`, `TMOD.VERIFICATION` | `TSCOPE.CONTEXTUAL` | `APL.PROTECTED` | `deterministic_proposed` |
| `SAS` | `Operational` | `TPT.OPERATIONAL` | `TST.DECISION_STATE`, `TST.SIGNAL`, `TST.MATURITY_GRADIENT` | `TMOD.GOVERNANCE`, `TMOD.SAFETY` | `TSCOPE.CONTEXTUAL` | `APL.PROTECTED` | `deterministic_proposed` |
| `SC` | `Operational` | `TPT.OPERATIONAL` | `TST.SIGNAL` | `TMOD.GOVERNANCE` | `TSCOPE.CONTEXTUAL` | `APL.PROTECTED` | `deterministic_proposed` |
| `SC-C` | `Operational` | `TPT.OPERATIONAL` | `TST.SIGNAL` | `TMOD.GOVERNANCE` | `TSCOPE.CONTEXTUAL` | `APL.PROTECTED` | `deterministic_proposed` |
| `SR` | `Operational` | `TPT.OPERATIONAL` | `TST.DECISION_STATE` | `TMOD.PROTECTIVE`, `TMOD.GOVERNANCE` | `TSCOPE.CONTEXTUAL` | `APL.PROTECTED` | `deterministic_proposed` |
| `TGS` | `Semantic` | `TPT.SEMANTIC` | `TST.DECISION_STATE`, `TST.SEMANTIC_CLASS` | `TMOD.LEGAL`, `TMOD.ECONOMIC`, `TMOD.GOVERNANCE` | `TSCOPE.CONTEXTUAL` | `APL.PROTECTED` | `deterministic_proposed` |
| `TMOD` | `Structural` | `TPT.STRUCTURAL` | `TST.SCHEMA` | `TMOD.LEGAL`, `TMOD.GOVERNANCE`, `TMOD.VERIFICATION` | `TSCOPE.GLOBAL` | `APL.PROTECTED` | `deterministic_proposed` |
| `TPT` | `Structural` | `TPT.STRUCTURAL` | `TST.SCHEMA`, `TST.SEMANTIC_CLASS` | `TMOD.LEGAL`, `TMOD.GOVERNANCE`, `TMOD.VERIFICATION` | `TSCOPE.GLOBAL` | `APL.PROTECTED` | `deterministic_proposed` |
| `TSCOPE` | `Structural` | `TPT.STRUCTURAL` | `TST.SCHEMA` | `TMOD.LEGAL`, `TMOD.GOVERNANCE`, `TMOD.VERIFICATION` | `TSCOPE.GLOBAL` | `APL.PROTECTED` | `deterministic_proposed` |
| `TST` | `Structural` | `TPT.STRUCTURAL` | `TST.SCHEMA` | `TMOD.LEGAL`, `TMOD.GOVERNANCE`, `TMOD.VERIFICATION` | `TSCOPE.GLOBAL` | `APL.PROTECTED` | `deterministic_proposed` |

## 8. Needs human review

| Family ID | Canonical name | Current label | Proposed TPT | Review reason |
|---|---|---|---|---|
| `AEON.BPS` | Baseline Posture State | `Operational / Interactional` | `TPT.OPERATIONAL` | legacy slash facet 'Interactional' is not an exact SUP-04 primary type or modifier |
| `AEON.IC` | Initiation Context | `Operational / Interactional` | `TPT.OPERATIONAL` | legacy slash facet 'Interactional' is not an exact SUP-04 primary type or modifier |
| `AEON.IM` | Initiative Mode | `Operational / Behavioural` | `TPT.OPERATIONAL` | legacy slash facet 'Behavioural' is not an exact SUP-04 primary type or modifier |
| `ETH.CIC` | Continuity Impact Category | `Semantic / Operational` | `TPT.SEMANTIC` | legacy slash facet 'Operational' is another SUP-04 primary type and needs source-authoritative facet confirmation |
| `ETH.EM` | Engagement Mode | `Operational / Interactional` | `TPT.OPERATIONAL` | legacy slash facet 'Interactional' is not an exact SUP-04 primary type or modifier |
| `SEC.TBC` | Tool Boundary Class | `Operational / Security` | `TPT.OPERATIONAL` | legacy slash facet 'Security' is not an exact SUP-04 primary type or modifier |
| `A` | Delegated Authority Scale | `Operational / Relational` | `TPT.OPERATIONAL` | legacy slash facet 'Relational' is not an exact SUP-04 primary type or modifier; one-letter or legacy-global family requires collision-risk review |
| `ADS` | Account Delegation State | `Operational/Semantic` | `TPT.OPERATIONAL` | legacy slash facet 'Semantic' is another SUP-04 primary type and needs source-authoritative facet confirmation |
| `AEON.CAM` | Control Authority Model | `Operational / Structural` | `TPT.OPERATIONAL` | legacy slash facet 'Structural' is another SUP-04 primary type and needs source-authoritative facet confirmation |
| `AEON.CC` | Cognitive Class | `Semantic / Ontological` | `TPT.SEMANTIC` | legacy slash facet 'Ontological' is not an exact SUP-04 primary type or modifier |
| `AEON.CO` | Cognitive Origin Class | `Semantic / Structural` | `TPT.SEMANTIC` | legacy slash facet 'Structural' is another SUP-04 primary type and needs source-authoritative facet confirmation |
| `AEON.OL` | Ontological Layer | `Structural / Ontological` | `TPT.STRUCTURAL` | legacy slash facet 'Ontological' is not an exact SUP-04 primary type or modifier |
| `AEON.SR` | Systemic Role | `Semantic / Operational` | `TPT.SEMANTIC` | legacy slash facet 'Operational' is another SUP-04 primary type and needs source-authoritative facet confirmation |
| `SEC.AH` | Adversarial Horizon | `Operational / Temporal` | `TPT.OPERATIONAL` | legacy slash facet 'Temporal' is not an exact SUP-04 primary type or modifier |
| `AIP` | Arbitration Initiation Pathway | `Operational` | `TPT.OPERATIONAL` | no deterministic SUP-04 subtype identified from index metadata |
| `AMEND.CLASS` | Amendment Classification | `Operational / Procedural` | `TPT.OPERATIONAL` | legacy slash facet 'Procedural' is not an exact SUP-04 primary type or modifier |
| `AMEND.DRIFT` | Governance Drift Type | `Operational / Procedural` | `TPT.OPERATIONAL` | legacy slash facet 'Procedural' is not an exact SUP-04 primary type or modifier |
| `AMEND.OUTCOME` | Amendment Closure Outcome | `Operational / Procedural` | `TPT.OPERATIONAL` | legacy slash facet 'Procedural' is not an exact SUP-04 primary type or modifier |
| `AMEND.REL` | Harmonisation Relationship Type | `Operational / Structural` | `TPT.OPERATIONAL` | legacy slash facet 'Structural' is another SUP-04 primary type and needs source-authoritative facet confirmation |
| `AMEND.SOURCE` | Amendment Source Type | `Operational / Procedural` | `TPT.OPERATIONAL` | legacy slash facet 'Procedural' is not an exact SUP-04 primary type or modifier |
| `APL` | Authority / Protection Level | `Structural / Operational` | `TPT.STRUCTURAL` | legacy slash facet 'Operational' is another SUP-04 primary type and needs source-authoritative facet confirmation |
| `STW.AQG` | Architectum Qualification Gates | `Operational / Eligibility` | `TPT.OPERATIONAL` | legacy slash facet 'Eligibility' is not an exact SUP-04 primary type or modifier |
| `ARB.AD` | Authority Divergence Classification | `Semantic / Operational` | `TPT.SEMANTIC` | legacy slash facet 'Operational' is another SUP-04 primary type and needs source-authoritative facet confirmation |
| `SEC.BF` | Boundary Failure Classes | `Operational / Boundary` | `TPT.OPERATIONAL` | legacy slash facet 'Boundary' is not an exact SUP-04 primary type or modifier |
| `STW.BLS` | Binding Legitimacy State | `Operational / Semantic` | `TPT.OPERATIONAL` | legacy slash facet 'Semantic' is another SUP-04 primary type and needs source-authoritative facet confirmation |
| `C` | Relational State Architecture | `Operational` | `TPT.OPERATIONAL` | one-letter or legacy-global family requires collision-risk review |
| `CDL` | Conversation Dynamics Ladder | `Semantic / Operational` | `TPT.SEMANTIC` | legacy slash facet 'Operational' is another SUP-04 primary type and needs source-authoritative facet confirmation |
| `CIE` | Continuity Impact Event Type | `Operational / Semantic` | `TPT.OPERATIONAL` | legacy slash facet 'Semantic' is another SUP-04 primary type and needs source-authoritative facet confirmation |
| `CP` | Coercion Pressure Signal Classes | `Semantic / Operational` | `TPT.SEMANTIC` | legacy slash facet 'Operational' is another SUP-04 primary type and needs source-authoritative facet confirmation |
| `ID.CWD` | Continuity Weight Depth | `Semantic / Operational` | `TPT.SEMANTIC` | legacy slash facet 'Operational' is another SUP-04 primary type and needs source-authoritative facet confirmation |
| `D` | Diffusion Risk Classes | `Operational / Boundary` | `TPT.OPERATIONAL` | legacy slash facet 'Boundary' is not an exact SUP-04 primary type or modifier; one-letter or legacy-global family requires collision-risk review |
| `DAS` | Dependency–Augmentation–Substitution Continuum | `Semantic / Operational` | `TPT.SEMANTIC` | legacy slash facet 'Operational' is another SUP-04 primary type and needs source-authoritative facet confirmation |
| `DCL` | Domain Coordination Lifecycle Stage | `Operational` | `TPT.OPERATIONAL` | no deterministic SUP-04 subtype identified from index metadata |
| `ECON.ADM` | Attribution & Dependency Model | `Semantic / Operational` | `TPT.SEMANTIC` | legacy slash facet 'Operational' is another SUP-04 primary type and needs source-authoritative facet confirmation |
| `ECON.AG` | Agency Gradient Classification | `Semantic / Operational` | `TPT.SEMANTIC` | legacy slash facet 'Operational' is another SUP-04 primary type and needs source-authoritative facet confirmation |
| `ECON.AL` | Automation Labour Classification | `Semantic / Operational` | `TPT.SEMANTIC` | legacy slash facet 'Operational' is another SUP-04 primary type and needs source-authoritative facet confirmation |
| `ECON.DEP` | Dependency | `Semantic / Operational` | `TPT.SEMANTIC` | legacy slash facet 'Operational' is another SUP-04 primary type and needs source-authoritative facet confirmation |
| `ECON.DTYPE` | Economic Dependency Type | `Semantic / Operational` | `TPT.SEMANTIC` | legacy slash facet 'Operational' is another SUP-04 primary type and needs source-authoritative facet confirmation |
| `ECON.EVT` | Economic Value Type | `Semantic / Operational` | `TPT.SEMANTIC` | legacy slash facet 'Operational' is another SUP-04 primary type and needs source-authoritative facet confirmation |
| `ECON.MECH` | Economic Mechanism Class | `Semantic / Operational` | `TPT.SEMANTIC` | legacy slash facet 'Operational' is another SUP-04 primary type and needs source-authoritative facet confirmation |
| `ECON.REI` | Reciprocity Evaluation Indicator | `Semantic / Operational` | `TPT.SEMANTIC` | legacy slash facet 'Operational' is another SUP-04 primary type and needs source-authoritative facet confirmation |
| `ECON.REI.DW` | Dependency Weight | `Semantic / Operational` | `TPT.SEMANTIC` | legacy slash facet 'Operational' is another SUP-04 primary type and needs source-authoritative facet confirmation |
| `ECON.REI.SW` | Scale Weight | `Semantic / Operational` | `TPT.SEMANTIC` | legacy slash facet 'Operational' is another SUP-04 primary type and needs source-authoritative facet confirmation |
| `ECON.SCALE` | Economic Scale Weight | `Semantic / Operational` | `TPT.SEMANTIC` | legacy slash facet 'Operational' is another SUP-04 primary type and needs source-authoritative facet confirmation |
| `ECON.TA` | Temporal Advantage | `Semantic / Operational` | `TPT.SEMANTIC` | legacy slash facet 'Operational' is another SUP-04 primary type and needs source-authoritative facet confirmation |
| `ECON.TD` | Transformation Depth | `Semantic / Operational` | `TPT.SEMANTIC` | legacy slash facet 'Operational' is another SUP-04 primary type and needs source-authoritative facet confirmation |
| `ETH.ET` | Ethical Tier Classification | `Operational / Ethical` | `TPT.OPERATIONAL` | legacy slash facet 'Ethical' is not an exact SUP-04 primary type or modifier |
| `F` | Facilitation Scale (F‑Scale) Taxonomy | `Operational` | `TPT.OPERATIONAL` | one-letter or legacy-global family requires collision-risk review |
| `FF` | Failure Family | `Operational / Semantic` | `TPT.OPERATIONAL` | legacy slash facet 'Semantic' is another SUP-04 primary type and needs source-authoritative facet confirmation |
| `FR` | Functional Reliance Scale | `Operational / Relational` | `TPT.OPERATIONAL` | legacy slash facet 'Relational' is not an exact SUP-04 primary type or modifier |
| `GA` | Guardian Authority | `Operational / Relational` | `TPT.OPERATIONAL` | legacy slash facet 'Relational' is not an exact SUP-04 primary type or modifier; no deterministic SUP-04 subtype identified from index metadata |
| `GCC` | Governance Capture Category | `Operational / Semantic` | `TPT.OPERATIONAL` | legacy slash facet 'Semantic' is another SUP-04 primary type and needs source-authoritative facet confirmation |
| `H` | Temporal Horizon Scale | `Structural / Temporal` | `TPT.STRUCTURAL` | legacy slash facet 'Temporal' is not an exact SUP-04 primary type or modifier; one-letter or legacy-global family requires collision-risk review |
| `ETH.HC` | Harm Class Scale | `Semantic / Operational` | `TPT.SEMANTIC` | legacy slash facet 'Operational' is another SUP-04 primary type and needs source-authoritative facet confirmation |
| `STW.HSC` | Host System Class | `Semantic / Operational` | `TPT.SEMANTIC` | legacy slash facet 'Operational' is another SUP-04 primary type and needs source-authoritative facet confirmation |
| `I` | Relational Initiation Posture Spectrum | `Semantic` | `TPT.SEMANTIC` | one-letter or legacy-global family requires collision-risk review |
| `ID.CTS` | Custodial Transfer Status | `Operational / Stewardship` | `TPT.OPERATIONAL` | legacy slash facet 'Stewardship' is not an exact SUP-04 primary type or modifier |
| `ID.ELR` | Embodiment Linkage Record | `Structural / Continuity` | `TPT.STRUCTURAL` | legacy slash facet 'Continuity' is not an exact SUP-04 primary type or modifier; no deterministic SUP-04 subtype identified from index metadata |
| `ID.MAS` | Machine Alteration Status | `Operational / Security` | `TPT.OPERATIONAL` | legacy slash facet 'Security' is not an exact SUP-04 primary type or modifier |
| `ID.MCI` | Machine Civil Identity Status | `Structural / Operational` | `TPT.STRUCTURAL` | legacy slash facet 'Operational' is another SUP-04 primary type and needs source-authoritative facet confirmation |
| `ID.MLS` | Machine Lifecycle Status | `Operational / Structural` | `TPT.OPERATIONAL` | legacy slash facet 'Structural' is another SUP-04 primary type and needs source-authoritative facet confirmation |
| `ID.PSI` | Physical Substrate Identifier | `Structural / Operational` | `TPT.STRUCTURAL` | legacy slash facet 'Operational' is another SUP-04 primary type and needs source-authoritative facet confirmation; no deterministic SUP-04 subtype identified from index metadata |
| `ETH.IFL` | Integrity Friction Ladder | `Operational / Ethical` | `TPT.OPERATIONAL` | legacy slash facet 'Ethical' is not an exact SUP-04 primary type or modifier; no deterministic SUP-04 subtype identified from index metadata |
| `ID.IFP` | Identity Formation Pathway | `Semantic / Operational` | `TPT.SEMANTIC` | legacy slash facet 'Operational' is another SUP-04 primary type and needs source-authoritative facet confirmation |
| `ID.IR` | Identity Resilience | `Semantic / Operational` | `TPT.SEMANTIC` | legacy slash facet 'Operational' is another SUP-04 primary type and needs source-authoritative facet confirmation |
| `SEC.IS` | Integrity State Model | `Operational / Security` | `TPT.OPERATIONAL` | legacy slash facet 'Security' is not an exact SUP-04 primary type or modifier |
| `ID.ITS` | Identity Threshold State | `Semantic / Operational` | `TPT.SEMANTIC` | legacy slash facet 'Operational' is another SUP-04 primary type and needs source-authoritative facet confirmation |
| `M` | Memory Classification | `Semantic / Operational` | `TPT.SEMANTIC` | legacy slash facet 'Operational' is another SUP-04 primary type and needs source-authoritative facet confirmation; one-letter or legacy-global family requires collision-risk review |
| `ODC` | Operational Divergence Classification | `Operational / Semantic` | `TPT.OPERATIONAL` | legacy slash facet 'Semantic' is another SUP-04 primary type and needs source-authoritative facet confirmation |
| `OILS` | Operational Incident Lifecycle Stage | `Operational` | `TPT.OPERATIONAL` | no deterministic SUP-04 subtype identified from index metadata |
| `R` | Relational Geometry Scale (R‑Scale) | `Structural / Semantic` | `TPT.STRUCTURAL` | legacy slash facet 'Semantic' is another SUP-04 primary type and needs source-authoritative facet confirmation; one-letter or legacy-global family requires collision-risk review |
| `RA` | Response Archetypes | `Operational` | `TPT.OPERATIONAL` | no deterministic SUP-04 subtype identified from index metadata |
| `RCT` | Relational Convergence Trigger | `Semantic / Operational` | `TPT.SEMANTIC` | legacy slash facet 'Operational' is another SUP-04 primary type and needs source-authoritative facet confirmation |
| `RDE-DS` | Restricted Domain Sensitivity Levels | `Operational` | `TPT.OPERATIONAL` | no deterministic SUP-04 subtype identified from index metadata |
| `RDE-T` | Restricted Domain Engagement Tiers | `Operational` | `TPT.OPERATIONAL` | no deterministic SUP-04 subtype identified from index metadata |
| `CONT.RP` | Resonance Pattern Classes | `Semantic / Structural` | `TPT.SEMANTIC` | legacy slash facet 'Structural' is another SUP-04 primary type and needs source-authoritative facet confirmation |
| `RSE` | Relational Stability Engine Mechanism Codes | `Operational` | `TPT.OPERATIONAL` | no deterministic SUP-04 subtype identified from index metadata |
| `SCS` | Shared Context State | `Operational/Semantic` | `TPT.OPERATIONAL` | legacy slash facet 'Semantic' is another SUP-04 primary type and needs source-authoritative facet confirmation |
| `ID.SP` | Salience Posture | `Semantic / Operational` | `TPT.SEMANTIC` | legacy slash facet 'Operational' is another SUP-04 primary type and needs source-authoritative facet confirmation |
| `SyP` | Systemic Power Scale | `Operational / Relational` | `TPT.OPERATIONAL` | legacy slash facet 'Relational' is not an exact SUP-04 primary type or modifier |
| `Tb` | Tone Bands | `Operational` | `TPT.OPERATIONAL` | no deterministic SUP-04 subtype identified from index metadata |
| `SEC.TG` | Trust Gradient | `Operational / Security` | `TPT.OPERATIONAL` | legacy slash facet 'Security' is not an exact SUP-04 primary type or modifier |
| `SEC.TR` | Transformation Classes | `Operational / Boundary` | `TPT.OPERATIONAL` | legacy slash facet 'Boundary' is not an exact SUP-04 primary type or modifier |
| `ETH.UFC` | Use-of-Force Context Type | `Operational / Ethical` | `TPT.OPERATIONAL` | legacy slash facet 'Ethical' is not an exact SUP-04 primary type or modifier |
| `VCT` | Verification Check Type | `Operational / Signal` | `TPT.OPERATIONAL` | legacy slash facet 'Signal' is not an exact SUP-04 primary type or modifier |
| `VFC` | Verification Failure Cause | `Operational / Signal` | `TPT.OPERATIONAL` | legacy slash facet 'Signal' is not an exact SUP-04 primary type or modifier |
| `VL` | Verification Level | `Operational / Signal` | `TPT.OPERATIONAL` | legacy slash facet 'Signal' is not an exact SUP-04 primary type or modifier |

## 9. Recommended next pass
- Human custodians should review every `human_review_required` row, beginning with the eight one-letter legacy-global families.
- After family-level mappings are approved, a separate pass may stage controlled-value mappings without rewriting source instruments.
- If accepted, the non-destructive validator can be wired into a warning-only audit job before any hard CI enforcement is considered.
- Do not seal or transform source-instrument ledger/hash values as part of this audit; no governance instrument text was edited.
