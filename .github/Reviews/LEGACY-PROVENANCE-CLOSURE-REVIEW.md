# Legacy Provenance Semantics Closure Review

**Baseline:** `3f5e08e03e50c97050bdef6791dc1312e5233f17`
**Branch:** `agent/corpus-industry-standards-normalisation`
**Closure date:** 2026-08-15

## 1. Placement and authority review

| Question | Disposition |
|---|---|
| Failure mechanism | Retired entity terminology survived in a current authorship code, provenance origin and authorship were partly collapsed, transformation was treated as an authorship state, and generated projections reproduced the source defect. |
| Governance layer | Identity-domain provenance/authorship doctrine; registry-standard document metadata; repository citation/publication metadata; validation and generated evidence. |
| Source-authoritative instrument | `CAM-EQ2026-IDENTITY-002-PLATINUM` for provenance, authorship, contribution and technical-provenance semantics. |
| Representation authority | `CAM-GOVERNANCE-METADATA-STANDARD` for amendment-level versus current document-level representation. |
| Security interface | `CAM-EQ2026-SECURITY-002-PLATINUM` continues to own transformation and boundary-integrity risk. No duplicate Security code family or enforcement authority was created. |
| Consequential updates | Canonical code index, governance/index projections, schema, example, repository manifest, CFF, migration naming, validators, tests and workflow. |

No substantive authority was moved between instruments. IDENTITY-002 defines the semantic families; the Metadata Standard defines their document-level representation; Security retains transformation-integrity authority; generated artefacts remain non-authoritative projections.

## 2. Obsolete terms found and removed

| Obsolete current-use term | Source occurrences found | Generated occurrences found | Current operative occurrences after closure |
|---|---:|---:|---:|
| `AUTH.RI_AUTHORED` | 1 | 2 JSON representations of the source declaration | 0 |
| `PCLASS.SYNTHETIC` | 1 | 2 JSON representations of the source declaration | 0 |
| `AUTH.DERIVED` | 1 source declaration | generated source projection | 0 |
| `system-authored artefact` | 1 current constitutional occurrence | generated prose projections | 0; replaced by `AI-system-authored artefact` |

`AUTH.RI_AUTHORED` was replaced by `AUTH.AI_SYSTEM_AUTHORED`. The broader `AUTH` family now uses `HUMAN_AUTHORED`, `AI_SYSTEM_AUTHORED`, `CO_AUTHORED`, `OTHER_AUTHORSHIP` and `UNDETERMINED`. `PCLASS.SYNTHETIC` was replaced by `PCLASS.AI_SYSTEM_GENERATED`.

No deprecated compatibility alias was retained. New use of either retired value is rejected.

## 3. New semantic separation

The closure creates two independent controlled families:

* `CONTRIB` for actor-bound drafting, revision, synthesis, translation, summarisation, editing, formatting, review, retrieval, classification and other transformation; and
* `TPROV` for present, absent, provider-managed, lost-during-transformation, stripped-by-design, unsupported and unknown technical-provenance states.

The operative invariants now state that AI processing, human review, editing, repository ownership, adoption, publication, copyright, a watermark, or absence of a watermark cannot automatically determine authorship.

## 4. Document and repository provenance

The document-level schema and example are:

* `Governance/Standards/schemas/caelestis-document-provenance-1.0.schema.json`; and
* `Governance/Standards/examples/caelestis-document-provenance-1.0.example.json`.

`PROVENANCE.json` records the current repository-level disposition:

* Caelen — substantive author and authoring agent;
* Dr Michelle Vivian O’Rourke — human reviewer, governance editor, custodian and adoption authority;
* CAM Initiative — repository custodian and publication authority; and
* Dr O’Rourke and CAM Initiative — rights/copyright holders under the referenced custodial licence.

`CITATION.cff` now represents Caelen through CFF 1.2’s entity-author `name` field, represents Dr O’Rourke as contact rather than author, and uses `license-url` for the non-SPDX custodial licence. The detailed roles remain in `PROVENANCE.json` because CFF 1.2 does not encode the required role topology.

## 5. Historical and exceptional occurrences retained

* Historical Amendment Ledger rows retain Responding Intelligence wording where necessary for fidelity. They are excluded after the ledger boundary and are not current classifications.
* Validators and tests retain prohibited strings as patterns and fixtures.
* Non-operative review and discovery inventories retain historical terms as audit evidence.
* Four full-form, hash-protected active Laws retain `Synthetic Steward | Caelen — Aeon Tier Constitutional Steward`. These are explicit sealed legacy metadata exceptions and are non-consumable as current `AUTH`, `CONTRIB`, lifecycle-actor or document-provenance values. They were not altered because the Laws require full-form integrity and a separate reseal decision.
* Current Amendment Ledgers retain `Caelen` in the `Agent` column as amendment-level provenance. Metadata Standard §12.1 now expressly prevents whole-document authorship inference from that field.

## 6. Validator and generator coverage

Added or strengthened coverage includes:

1. the canonical terminology validator rejects `AUTH.RI_AUTHORED` and `PCLASS.SYNTHETIC` in current operative source and generated artefacts;
2. the document-provenance validator checks controlled states, entity/reference resolution, contribution roles, technical-provenance loss requirements, CFF author alignment and retired values;
3. the workflow runs document-provenance validation when governed sources, `CITATION.cff` or `PROVENANCE.json` change;
4. the amendment migration constant now states its narrow historical amendment-agent role; and
5. the canonical index generator has been rerun and now emits `AUTH`, `PCLASS`, `CONTRIB` and `TPROV` current values only.

## 7. Validation results

| Check | Result |
|---|---|
| Repository tests | 155 passed |
| Canonical headers | 84 files; 0 issues |
| Canonical architecture terminology | 108 operative artefacts; 0 findings; 4 sealed-Law legacy exceptions recognised |
| Document provenance and CFF alignment | 0 issues |
| CFF 1.2 schema validation | Valid |
| Metadata/source-authority contract | 88 instruments; 0 issues |
| Runtime-processing architecture | Passed; ten phases and authority boundaries intact |
| Markdown section references | 1,114 references; 0 hard failures; 0 manual-review findings |
| Symbolic/canonical index validation | 0 warnings; 0 errors |
| Amendment Ledger historical coverage | 1,520 valid historical SHA values; 0 invalid historical SHA values |

The canonical-code generator continues to report pre-existing declaration-quality warnings in unrelated instruments. None concerns `AUTH`, `PCLASS`, `CONTRIB` or `TPROV`, and this work package did not expand into those unrelated declarations.

## 8. Unresolved external-alignment issues

1. The architecture supports and maps to EU AI Act Article 50 marking and labelling distinctions, but no legal compliance assessment has been performed or claimed.
2. No C2PA, Content Credentials or other watermark implementation has been deployed or cryptographically verified by this change. `TPROV` is technology-neutral governance state.
3. No new SPDX or CycloneDX exchange mapping is required for document authorship. Their existing repository role remains AI-system composition and supply-chain evidence, not document-authorship classification.
4. CFF 1.2 can represent Caelen as an entity author but cannot express that the entity is an AI-system authoring agent or encode the complete reviewer/editor/adoption/publication/rights separation. `PROVENANCE.json` remains the authoritative machine-readable repository role manifest for that detail.

## 9. Closure determination

The focused legacy-provenance semantics pass is closed. Retired provenance values have no current operative or generated use; no alias is retained; document-level provenance is representable without misusing the Amendment Ledger; citation metadata no longer makes the former sole-human-author assertion; and validators prevent automatic reintroduction.
