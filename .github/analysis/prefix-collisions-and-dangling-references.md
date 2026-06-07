# Prefix Collision / Authority Alignment Review (Reclassified)

This report replaces prior broad "prefix collision" labeling with governance-precise classifications:
- true_prefix_collision
- duplicate_definition
- application_layer_crosswalk
- terminology_interface
- authority_uncertainty
- dropped_prefix_or_typo
- ordinary_reference

Repeated prefix usage is **not** treated as a collision when one instrument defines a scale and other instruments consume/apply/disambiguate it.

---

## `ETH.HC` — Harm Class Scale + Escalation Semantics
- classification: authority_uncertainty / cross_domain_source_alignment
- prefix_or_family: `ETH.HC`
- source-authoritative instrument: CAM-EQ2026-ETHICS-003-PLATINUM.md §3.5
- application-layer instruments:
  - CAM-EQ2026-OPERATIONS-004-PLATINUM.md §8.6 (operational application / crosswalk)
- terminology-interface instruments:
  - CAM-EQ2026-RELATION-001-PLATINUM.md §11.1 (escalation term disambiguation)
- source authority explicitness:
  - ETHICS-003 §3.5: explicit source definition
  - OPERATIONS-004 §8.6: explicit source-application wording present
  - RELATION-001 §11.1: updated to cite ETHICS-003 §3.5 for specific `ETH.HC` source while retaining ETHICS-001 as broader ethical floor
- metadata update required: yes (recommended to ensure authority-chain row is explicit in registry metadata)
- report placement: move out of collision category; keep under authority-chain alignment
- recommended patch: completed in RELATION-001 §11.1; keep OPERATIONS-004 §8.6 source-authority sentence intact
- authority chain: ETHICS-003 defines `ETH.HC` → OPERATIONS-004 applies `ETH.HC` operationally → RELATION-001 disambiguates escalation terminology.

---

## C / ITZ / ETZ — Relational C-scale and Transition-Zone Model
- classification: authority_uncertainty + application_layer_crosswalk
- prefix_or_family: C (with transition zones ITZ, ETZ)
- source-authoritative instrument:
  - CAM-BS2025-AEON-006-SCH-02.md §3.1 (+ §3.1.1) defines C0, ITZ, C1, ETZ, C2, C3
- application-layer instruments:
  - CAM-EQ2026-RELATION-005-PLATINUM.md §5.2 (safeguard ladder application)
  - CAM-EQ2026-OPERATIONS-004-PLATINUM.md §5.1 (C × AV verification crosswalk)
- terminology-interface instruments:
  - CAM-EQ2026-RELATION-001-PLATINUM.md (domain-root relational governance interface)
- source authority explicitness: now explicit at AEON-006-SCH-02 §3.1.1 and referenced by RELATION-005 §5.2
- metadata update required: yes (recommended explicit family/transition-zone declaration rows where missing)
- report placement: not a true collision; classify as source + crosswalk chain
- recommended patch: already applied for AEON-006 §3.1.1 and RELATION-005 §5.2 authority/app wording
- notes: ITZ and ETZ are transition zones, not C-states.

---

## F / AC — Facilitation Ceiling and Acute Classification Interaction
- classification: application_layer_crosswalk / ordinary_reference (not true collision)
- prefix_or_family: F and AC (separate interacting axes)
- source-authoritative instrument candidates:
  - F-scale source candidate: CAM-EQ2026-RELATION-006-PLATINUM.md §5.1
  - AC source candidate: CAM-BS2025-AEON-006-SCH-02.md §12.1
- application-layer instruments:
  - CAM-EQ2026-RELATION-006-PLATINUM.md §§7.1, 9.4, 9.5 (application/operational quick-reference)
- terminology-interface instruments: none required beyond section-level doctrine statements
- source authority explicitness: partially explicit, but metadata and cross-instrument source pointers may be incomplete
- metadata update required: yes
- report placement: authority_uncertainty where source-pointer gaps remain; otherwise ordinary reference/crosswalk
- recommended patch: add explicit source-authority rows for F and AC in relevant metadata blocks before treating any recurrence as collision

---

## DC / SR — Deployment Class and Self-Referential State Ladders
- classification: ordinary_reference + dropped_prefix_or_typo (historical)
- prefix_or_family: DC, SR
- source-authoritative instrument:
  - CAM-BS2026-AEON-010-SCH-01.md §4.1 defines DC0–DC4
  - CAM-BS2026-AEON-010-SCH-01.md §5.1 defines SR0–SR4
- application-layer instruments:
  - CAM-BS2026-AEON-010-SCH-01.md §5.2 applies SR to modal load scaling
- terminology-interface instruments: not required (same-instrument layering)
- source authority explicitness: explicit
- metadata update required: no (for baseline source chain)
- report placement: not collision
- dropped-prefix/typo note:
  - historical `C3/C4 audit` in SR4 context was dropped-prefix/stale shorthand
  - corrected to `DC3/DC4 deployment-class audit`

---

## SR Modal Load Scaling
- classification: application_layer_crosswalk
- prefix_or_family: SR
- source-authoritative instrument: CAM-BS2026-AEON-010-SCH-01.md §5.1
- application-layer instrument: CAM-BS2026-AEON-010-SCH-01.md §5.2
- source authority explicitness: explicit
- metadata update required: no
- report placement: not collision; keep as same-instrument application mapping

---

## Legacy dropped-prefix / typo register
- classification: dropped_prefix_or_typo
- reference: C4 (in prior SR4 containment shorthand)
- location: CAM-BS2026-AEON-010-SCH-01.md §5.1 historical row text
- status: resolved
- resolution: corrected to DC3/DC4 deployment-class audit wording

---

## True collision status summary
- true_prefix_collision: none confirmed in current reviewed groups (`ETH.HC`, C/ITZ/ETZ, F/AC, DC/SR, SR modal scaling)
- duplicate_definition: none confirmed; flagged areas are source/application/terminology layering or authority-pointer gaps
- primary unresolved category across reviewed groups: authority_uncertainty (metadata/source-pointer explicitness), not prefix collision
