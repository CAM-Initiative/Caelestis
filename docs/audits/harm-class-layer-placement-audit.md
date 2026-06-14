# Harm Class Layer-Placement Audit

## 1. Scope and guardrails

This audit reviews whether the current Harm Class namespace and source layer are architecturally correct after Domain Namespace Transmutation Pass 001. It is an audit-and-staging artifact only: no source doctrine was moved, no code family was renamed, and no instrument text was rewritten.

Primary question: whether the current `ETH.HC` Harm Class Scale is an Ethics-local family, a global harm-class family that should become `AEON.HC`, or a candidate for future parent/child architecture with domain-specific harm families.

## 2. Source files and generated artifacts inspected

### AEON / Constitution / Annex layer

| Source | Harm-related finding |
|---|---|
| `Governance/Constitution/CAM-BS2025-AEON-006-PLATINUM.md` | Contains continuity-impact and protection language, but no source-authoritative Harm Class Scale or `AEON.HC` declaration was found. |
| `Governance/Constitution/CAM-BS2025-AEON-006-SCH-01.md` | Consumes ETHICS-aligned harm classification and the `ETH.HC` scale; it expressly defers substantive harm classification to `CAM-EQ2026-ETHICS-003-PLATINUM`. |
| `Governance/Constitution/CAM-BS2025-AEON-006-SCH-02.md` | Contains relational signal / harm-classification routing language, but no Harm Class Scale declaration. |
| `Governance/Constitution/CAM-BS2025-AEON-006-SCH-03.md` | Contains threshold/risk calibration language, but no Harm Class Scale declaration. |
| `Governance/Constitution/CAM-BS2025-AEON-006-SCH-04.md` | No source-authoritative Harm Class Scale declaration found. |
| `Governance/Constitution/CAM-BS2025-AEON-006-SCH-07.md` | Contains restricted-domain harm-potential and operational-harm constraint doctrine, but no Harm Class Scale declaration. |
| Other `Governance/Constitution/CAM-BS*-AEON-*.md` matches | Harm-related references include economic-harm signals, continuity harm, governance harm, injury, and risk language; no `AEON.HC` source-authoritative declaration was found. |

### Domain charters and supplements

| Source area | Harm-related finding |
|---|---|
| `Governance/Charters/CAM-EQ2026-ETHICS-003-PLATINUM.md` | Source-authoritatively defines `ETH.HC` as the Harm Class Scale for ethical harm classification in criminal/violent harm routing and constraint posture. |
| Other `Governance/Charters/CAM-EQ2026-ETHICS-*` files | Contain ethical harm-floor references, but no competing `AEON.HC` declaration was found. |
| `Governance/Charters/CAM-EQ2026-ECONOMICS-003-PLATINUM.md` | Source-authoritatively defines `ECON.HARM` as Economic Harm Class with values for temporal extraction and metering divergence. |
| Other `Governance/Charters/CAM-EQ2026-ECONOMICS-*` files | Contain economic harm routing/failure references; no `ECON.HC` declaration was found. |
| `Governance/Charters/CAM-EQ2026-RELATION-*` | Consume `ETH.HC` in relation to risk escalation and harm-risk interaction, but do not define HC. |
| `Governance/Charters/CAM-EQ2026-OPERATIONS-*` | Operationally apply `ETH.HC` for escalation thresholds; do not redefine HC. |
| `Governance/Charters/CAM-EQ2026-IDENTITY-*` | Contains identity/relational harm and minimum-protectiveness language, but no domain HC declaration. |
| `Governance/Charters/CAM-EQ2026-SECURITY-*` | Contains ethical-harm coupling and harm-risk references, but no domain HC declaration. |
| `Governance/Charters/CAM-EQ2026-STEWARD-*` | No source-authoritative harm-class family declaration found in the required search scope. |
| `Governance/Charters/CAM-EQ2026-CONTINUITY-*` | No source-authoritative harm-class family declaration found in the required search scope. |

### Generated / staging artifacts

| Artifact | Finding |
|---|---|
| `Governance/canonical-code-index.json` | Contains `ETH.HC` and `ECON.HARM`; no `AEON.HC` family entry found. |
| `Governance/canonical-code-index.md` | Lists `ETH.HC` and `ECON.HARM`; no `AEON.HC` family entry found. |
| `data/taxonomy/sup04_transmutation_map.json` | Stages `ETH.HC` and `ECON.HARM`; no `AEON.HC` entry found. |
| `data/taxonomy/domain_namespace_transmutation_pass_001.json` | Records first-pass mapping `HC` -> `ETH.HC`. |
| `.github/analysis/metadata-declaration-gaps.md` | Still contains generated candidate rows that treat operational or relational applications of `ETH.HC` as candidate metadata gaps; these are generated-analysis artifacts, not source authority. |

## 3. Harm-related definitions found and classification

| Source | Reference | Material classification | Layer-match assessment | Notes |
|---|---:|---|---|---|
| `CAM-EQ2026-ETHICS-003-PLATINUM` | §3, §3.5, §8.1, §11.2, §12.3.1 | `domain_specific_harm_doctrine` | Current source layer matches declared ETHICS authority. | The source text repeatedly uses ethical harm-floor, criminal/violent harm, and ETHICS Domain language. |
| `CAM-BS2025-AEON-006-SCH-01` | §6.3, §7.5, metadata declarations | `domain_specific_extension_of_global_harm` / consumer of ETHICS harm doctrine | No AEON source declaration found. | The schedule defers harm-class severity and substantive harm classification to the Ethics Appendix. |
| `CAM-EQ2026-ECONOMICS-003-PLATINUM` | §4.6, §18.2, §20.3.2 | `domain_specific_harm_doctrine` | Current source layer matches Economics domain. | `ECON.HARM` is an economic harm-pattern family, not an ordinal clone of `ETH.HC`. |
| `CAM-EQ2026-OPERATIONS-004-PLATINUM` | §8.6, §15.3.3 | `domain_specific_extension_of_global_harm` / operational application | Layer matches operational-application role. | It applies `ETH.HC` for reporting, duty-of-care, evidence preservation, and escalation handling without redefining it. |
| `CAM-EQ2026-RELATION-001-PLATINUM` | Risk Escalation terminology and metadata | `domain_specific_extension_of_global_harm` / consumer | Layer matches consumer role. | It references `ETH.HC` for external risk-escalation terminology. |
| `CAM-EQ2026-RELATION-006-PLATINUM` | harm-risk interaction and metadata | `risk_or_failure_taxonomy_not_harm_class` plus consumer of `ETH.HC` | Layer matches relational crisis-response role. | It defines the `F` facilitation scale and consumes `ETH.HC`; it does not define HC. |
| Identity, Security, Steward, Continuity required source areas | search hits only | `risk_or_failure_taxonomy_not_harm_class` or absent | No domain-HC declaration found. | Harm references exist in prose, but no `ID.HC`, `SEC.HC`, `STW.HC`, or `CONT.HC` source family was found. |

## 4. Are Harm Classes already defined at the AEON / Annex level?

No source-authoritative AEON / Annex-level Harm Class Scale was found in the inspected AEON-006 instrument set or broader AEON source search. The strongest AEON-layer reference is `CAM-BS2025-AEON-006-SCH-01`, which states that harm type determination, lawful/non-lawful force classification, criminal or violent context classification, and harm-class severity defer to `CAM-EQ2026-ETHICS-003-PLATINUM`, and then names the `ETH.HC` scale as defined in that Ethics Appendix.

Therefore, this audit does **not** find an already-existing `AEON.HC` source family.

## 5. Is `ETH.HC` ethics-specific or global in substance?

Current source evidence supports treating `ETH.HC` as ethics-specific rather than already-global:

- The defining section states that the Harm Class (`ETH.HC`) scale is the authoritative **ethical** harm classification scale for criminal/violent harm routing and constraint posture.
- The canonical declaration states `Scope | Domain`, `Domain Namespace | ETH`, and an authority/protection level limited to source-authoritative ethical harm classification.
- The lineage metadata identifies Governance Authority as `ETHICS Domain — Harm Classification & Constraint Layer` and Ontological Scope as `Harm Classification Domain`.
- AEON and Operations sources consume or operationally apply `ETH.HC`; they do not currently source-authoritatively define a global Harm Class parent.

Conclusion: keep `ETH.HC` unchanged in this pass. Do not rename `ETH.HC` to `AEON.HC` without a later constitutional/source-authority amendment.

## 6. Should the global harm parent be `AEON.HC`?

`AEON.HC` is a plausible future architecture if maintainers want one global parent registry for harm-class severity. However, source evidence in the current repository does not yet establish `AEON.HC` as an existing family.

Recommended staging:

| Candidate family | Recommendation | Rationale |
|---|---|---|
| `AEON.HC` | Stage as a future constitutional/annex parent candidate, not as an applied rename. | Current source authority is ETHICS-local; creating a global parent would require source-doctrine amendment. |
| `ETH.HC` | Retain as active ETHICS-domain Harm Class Scale pending human/maintainer decision. | Source text explicitly declares ETHICS domain authority and domain scope. |
| Domain-specific `*.HC` families | Do not create in this pass. | No source-authoritative declarations were found for `ECON.HC`, `ID.HC`, `SEC.HC`, `RLN.HC`, `STW.HC`, `OPS.HC`, or `CONT.HC`. |

## 7. `ECON.HARM` / `ECON.HC` recommendation

Recommendation: **Option A — keep `ECON.HARM` unchanged and stage a relationship/crosswalk to any future global parent `AEON.HC`; do not rename to `ECON.HC` in this audit.**

Reasons:

- `ECON.HARM` is already source-authoritatively declared by the Economics Appendix as an economic-harm-class family.
- Its controlled values are named economic harm modes (`ECON.HARM.TEMPORAL-EXTRACTION`, `ECON.HARM.METERING-DIVERGENCE`) rather than ordinal class levels parallel to `ETH.HC-0` through `ETH.HC-4`.
- The economics declaration says it classifies economic harm patterns involving temporal extraction, hidden depletion, metering divergence, or misalignment between displayed and enforced economic conditions.
- No source text currently declares `ECON.HC`.

Staged relationship if `AEON.HC` is later created:

```json
{
  "family_id": "ECON.HARM",
  "related_code_families": ["AEON.HC"],
  "relationship_type": "domain_specific_harm_family",
  "rename_recommended": false,
  "notes": "Economic Harm Class remains an Economics-domain harm-pattern family and may crosswalk to a future global Harm Class parent."
}
```

## 8. Wrong-layer findings

| Finding | Status | Evidence | Recommended handling |
|---|---|---|---|
| Global `AEON.HC` source authority absent | Confirmed absent in inspected sources. | No AEON/Annex source declaration found; AEON schedule references consume ETHICS harm classification. | Do not create by index-only edit; require constitutional/source amendment if desired. |
| `ETH.HC` may be serving cross-domain consumers | Confirmed. | AEON schedule, Operations, and Relation instruments consume/apply `ETH.HC`. | Treat as a cross-domain-consumed ETHICS family for now; consider parent registry later. |
| Potential architectural desire for a global harm parent | Ambiguous / human review required. | Broad use makes global parent plausible, but source text expressly remains ETHICS-domain. | Human maintainer should decide whether to promote or parent the doctrine. |
| Stale `ETHICS.HC` references after short namespace pass | Confirmed in generated index/source metadata references. | `CAM-BS2025-AEON-006-SCH-01` metadata consumes `ETHICS.HC` in two rows while prose uses `ETH.HC`. | Separate narrow cleanup pass may update stale references to `ETH.HC`; this audit does not edit source instruments. |

## 9. Proposed migration pathway for a later Codex pass

1. **Maintainer decision checkpoint:** Decide whether CAM should have a constitutional/global harm-class parent family.
2. **If no global parent is desired:** retain `ETH.HC`; perform a narrow stale-reference cleanup for `ETHICS.HC` -> `ETH.HC` where source text is unambiguous; leave `ECON.HARM` unchanged.
3. **If global parent is desired:** draft a source-authoritative AEON/Annex amendment creating `AEON.HC`, preferably in an existing AEON runtime/arbitration/harm-classification instrument if maintainers confirm that layer. Candidate destination: an AEON-006 schedule or a new AEON schedule/supplement dedicated to harm-class registry and cross-domain harm-family architecture.
4. **After `AEON.HC` is source-authoritatively created:** decide whether `ETH.HC` becomes an ETHICS-domain extension, a cross-reference alias, or is superseded by `AEON.HC`.
5. **Crosswalk domain families:** relate `ECON.HARM` to `AEON.HC` as `domain_specific_harm_family` / `crosswalk` without renaming unless Economics source doctrine is amended to define `ECON.HC`.
6. **Only after source amendments:** regenerate `Governance/canonical-code-index.json`, `Governance/canonical-code-index.md`, SUP-04 staging maps, namespace-pass maps, analysis artifacts, and any catalogue metadata.

## 10. Recommended domain harm-family architecture

| Domain | Current family found | Recommended current state | Future architecture candidate |
|---|---|---|---|
| AEON / Constitutional | none | No applied `AEON.HC` yet. | `AEON.HC` parent registry only after source amendment. |
| Ethics | `ETH.HC` | Keep active. | Either remains domain-specific extension or is superseded/cross-referenced if `AEON.HC` is created. |
| Economics | `ECON.HARM` | Keep active; do not rename. | Crosswalk to future `AEON.HC`; consider `ECON.HC` only if source doctrine is amended. |
| Identity | none | No domain HC. | `ID.HC` only if Identity source doctrine defines identity harm classes. |
| Security | none | No domain HC. | `SEC.HC` only if Security source doctrine defines security harm classes. |
| Relation | none; consumes `ETH.HC`; defines separate `F` facilitation scale | Do not create `RLN.HC` now. | `RLN.HC` only if Relation source doctrine defines relational harm classes distinct from crisis/facilitation scales. |
| Steward | none | No domain HC. | `STW.HC` only if Steward source doctrine defines stewardship harm classes. |
| Operations | none; applies `ETH.HC` operationally | Do not create `OPS.HC` now. | `OPS.HC` only if Operations source doctrine defines operational harm classes rather than applications/escalation workflows. |
| Continuity | none | No domain HC. | `CONT.HC` only if Continuity source doctrine defines continuity harm classes. |

## 11. Commands run

```bash
find .. -name AGENTS.md -print
cat AGENTS.md
rg -n -i --glob 'CAM-BS2025-AEON-006*.md' 'harm class|harm category|harm|injury|risk|protection|continuity impact|ethical harm|economic harm|\bHC\b' Governance/Constitution
python - <<'PY'
import json
p='Governance/canonical-code-index.json'
data=json.load(open(p))
rows=data if isinstance(data,list) else data.get('families', data.get('code_families', []))
for fam in rows:
    fid=fam.get('family_id') or fam.get('code_family')
    if fid and ('HC' in fid or 'HARM' in fid):
        print(fid, fam.get('canonical_name'), fam.get('source_path'), fam.get('declaration_heading'), fam.get('parent_family'), fam.get('controlled_values_defined') or fam.get('controlled_values'))
PY
rg -n 'Harm Class|ETH\.HC|HC-|ECON\.HARM|Economic Harm|harm_class|Economic harm|domain-specific' Governance/Charters/CAM-EQ2026-ETHICS-003-PLATINUM.md Governance/Charters/CAM-EQ2026-ECONOMICS-003-PLATINUM.md Governance/Constitution/CAM-BS2025-AEON-006-PLATINUM.md Governance/Constitution/CAM-BS2025-AEON-006-SCH-*.md
rg -n -i --glob 'CAM-BS*-AEON-*.md' 'harm class|harm category|harm taxonomy|\bAEON\.HC\b|\bETH\.HC\b|ETHICS\.HC|economic harm|ethical harm|identity harm|security harm|relational harm|continuity harm|governance harm|operational harm|injury|continuity impact' Governance/Constitution
rg -n 'ETH\.HC|ETHICS\.HC|AEON\.HC|ECON\.HARM|Harm Class|Economic Harm' .github data docs Governance --glob '*.json' --glob '*.md'
python .github/scripts/build-canonical-code-index.py --check
python .github/scripts/validate_sup04_transmutation_map.py
python -m pytest .github/scripts/tests
python -m json.tool data/taxonomy/harm_class_layer_placement_audit.json
```

## 12. Validation results

| Command | Result | Notes |
|---|---|---|
| `python .github/scripts/build-canonical-code-index.py --check` | Passed | Canonical Code Index remains current. |
| `python .github/scripts/validate_sup04_transmutation_map.py` | Passed with warnings | Expected human-review warnings remain in SUP-04 staging map; no errors. |
| `python -m pytest .github/scripts/tests` | Passed | Full script test suite passed. |
| `python -m json.tool data/taxonomy/harm_class_layer_placement_audit.json` | Passed | Machine-readable audit JSON is valid. |

## 13. Unresolved questions

1. Should maintainers create an `AEON.HC` constitutional parent registry even though no current source instrument defines it?
2. If `AEON.HC` is created, should `ETH.HC` become a domain-specific extension, a deprecated alias/cross-reference, or be superseded?
3. Should `ECON.HARM` remain a harm-pattern family indefinitely, or should a separate `ECON.HC` ordinal economic harm-class scale be source-authored later?
4. Should the stale `ETHICS.HC` references in AEON schedule metadata be corrected to `ETH.HC` in a narrow cleanup pass?
5. Should generated analysis artifacts that classify operational `ETH.HC` applications as metadata-declaration gaps be regenerated or tuned after the namespace pass?

## 14. Final recommendation

Do **not** rename `ETH.HC` or `ECON.HARM` in this pass. The current source evidence supports `ETH.HC` as an ETHICS-domain Harm Class Scale that is consumed cross-domain, not as an already-source-authored `AEON.HC` family. `ECON.HARM` should remain unchanged and may be staged as a domain-specific harm family related to a future `AEON.HC` parent if maintainers choose to create that parent through source doctrine.
