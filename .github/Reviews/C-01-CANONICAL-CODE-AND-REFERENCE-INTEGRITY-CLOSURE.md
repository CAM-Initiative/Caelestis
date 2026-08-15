# C-01 — Canonical Code and Reference Integrity Closure

## 1. Scope and repository state

Work began from remote branch head `7ad8a77f03d4db7bd058edd2df78d8f8f3922767` on `agent/corpus-industry-standards-normalisation`. The remote head matched the handoff and no later commits were present. The branch remained intentionally one commit behind and 71 commits ahead of `origin/main`; no merge, rebase, reset, cherry-pick or other divergence reconciliation was performed.

Four other Caelestis checkouts were inspected without modification. Their unique commits, detached state and untracked validation output were not reconciled into this worktree. The starting checkout was clean.

The Governance Rebuild, Metadata/Source-Authority Audit, Runtime-processing architecture guard, document provenance checks and canonical header/terminology checks were green at baseline apart from the known non-blocking canonical declaration diagnostics.

## 2. Validator defect confirmed

The prior “Symbolic/index validation” did not prove current canonical-reference integrity:

* the canonical index was a JSON array while the linter's legacy checks only operated on a JSON object;
* the configured legacy symbolic registry was absent;
* absence of that registry explicitly skipped the canonical-code cross-check; and
* the index generator printed declaration defects as warnings and returned success.

The result was a misleading green check. In particular, operative `ID.ISTATE.SYSTEM_PROPOSED` survived while the source declaration still listed retired `ID.ISTATE.RI_PROPOSED`.

## 3. Declaration-set disposition

| Measure | Starting state | Final state |
|---|---:|---:|
| Source-derived declaration records | 172 | 189 |
| Declaration diagnostics | 24 | 0 |
| Missing-supported-identifier diagnostics | 17 | 0 |
| Nonstandard-heading diagnostics | 1 | 0 |
| Incomplete-declaration diagnostics | 6 | 0 |
| Duplicate active source authorities | 0 | 0 |
| Invalid or undeclared subfamily parents | 4 parser artefacts | 0 |

The 17 starting missing-identifier diagnostics were non-declaration application, overview, schema or lineage tables and are now structurally excluded. The valid canonical-constraint heading is now recognised. The six incomplete declarations received only mechanically determinable fields.

Explicit field-entry declarations are now discoverable even where migrated declarations are same-level siblings of their canonical heading. This recovered current ARBITRATION, MENTIS and Annex K declarations without relocating authority. Annex B's existing `AEON.H`, `AEON.OL` and `AEON.SR` source declarations were made machine-complete in its canonical footer. `ARB.APO`, `ARB.AMB` and `ARB.AMP` were recorded as reference sets, consistently with their existing source-authoritative descriptions.

Dots no longer infer parentage. A code family is a subfamily only where `Family Kind` and `Parent Family` expressly establish it, and the parent must independently resolve.

## 4. Current-reference inventory

The deterministic inventory is recorded in `C-01-CANONICAL-REFERENCE-INVENTORY.json` beside this review.

| Resolution | Occurrences |
|---|---:|
| valid-family-reference | 2,108 |
| valid-controlled-value | 3,314 |
| valid-subfamily-reference | 25 |
| valid-reference-set | 338 |
| permitted-historical-use | 26 |
| ambiguous-token | 12 |
| unresolved current-use error | 0 |
| **Total** | **5,823** |

The 12 ambiguous tokens are narrow and explicit: `ECON.ADM.DEP` is a construction-pattern example; `AEON.HARM.ECONOMIC` is an example of a duplicate value that must not be created; and ten Annex B identifiers are expressly non-canonical migration proposals. They are not admitted as declarations.

The 26 historical occurrences are confined to amendment ledgers, explicit retired-family declarations or express historical-compatibility statements. They include retired `CONT.RP`, Identity families, `AUTH.RI_AUTHORED`, `PCLASS.SYNTHETIC`, `ETH.HC`, former Economics identifiers and other version-fidelity records. No historical row was rewritten for presentational consistency.

## 5. Genuine current defects repaired

The source authority was clear for each repair; no new family or governance power was created.

* `ID.ISTATE.RI_PROPOSED` was replaced by `ID.ISTATE.SYSTEM_PROPOSED` in the source declaration.
* Retired `ID.IFP.*` labels were removed from current presentation-source headings while the explicit retirement record was preserved.
* `CBR.RES` was aligned to the operative `CBR.PAT` record class.
* `ECON.DEP.INCIDENTAL`, `.MATERIAL` and `.CRITICAL` consumer labels were aligned to the source family's unprefixed controlled values.
* `ECON.DW` and `ECON.DW.HIGH` were aligned to the expressly declared `ECON.REI.DW` subfamily; `ECON.FIC.IE.MOD` was aligned to operative `ECON.FIC.IE.MODERATE`.
* `SEC.BF-DR` was aligned to the source-declared `SEC.BF-D` value.
* Current `ETH.HC` consumers were aligned to `ETH.RISK`; an obsolete `RLN.R` crosswalk was removed while ledger history was retained.
* `AEON.HCD.D1_HUMAN_COGNITIVE_LABOUR` and `AEON.HCD.D2_JOINT_EMERGENT_CREATION` were aligned to declared `AEON.HCD.D1` and `AEON.HCD.D2`.
* `AEON.AEON.H3/AEON.H4` was corrected to `AEON.H3`–`AEON.H4`.
* `OPS.CGRD`, `OPS.CGRS`, `OPS.RTC` and `OPS.RGRF` declaration status was aligned from `Proposed` to `Active`. The source instrument already defined and used all four families and current consumers already treated `OPS.RGRF` as source-authoritative; this corrected stale declaration metadata and did not introduce a family.

Seventeen amended Constitution/Charter instruments each received one C-01 Amendment Ledger entry. The repository ledger tool sealed those entries; no instrument has multiple open C-01 rows.

## 6. Validation architecture

`build-canonical-code-index.py` now:

* extracts bounded and recognised sibling declarations from the same source corpus;
* parses comma- and semicolon-delimited controlled values;
* normalises explicit none-values without creating parentage;
* validates source-instrument ownership, declaration shape, collision state and explicit subfamily parent resolution; and
* exits non-zero for declaration defects.

`lint-symbolic-structures.py` now validates the current JSON-array projection and current Governance Markdown directly from source-derived declarations. It fails for unknown families, unknown values, retired current use, invalid parentage, duplicate authority, wrong source ownership and generated-index/source disagreement. Missing legacy registry data no longer disables current validation.

The Governance Rebuild now separates “Canonical declaration and index generation” from blocking “Canonical reference integrity”, and uploads the machine-readable occurrence inventory as its own validation artefact.

Regression coverage includes a stale Identity-class value, unknown family, unknown value under a valid family, non-inference of dotted subfamilies, a dotted controlled value, an expressly declared subfamily, historical retired use, current retired use, consumer/source separation, generated-index disagreement and the missing-legacy-registry condition.

## 7. Final validation

| Check | Result |
|---|---|
| Script tests | 181 passed |
| Canonical declaration/index generation | 189 declarations; 0 diagnostics |
| Canonical reference integrity | 5,823 references; 0 errors |
| Amendment Ledger / SHA coverage | 80 instruments; 1,538 valid historical hashes; 49 recognised historical-null rows; 80 valid latest hashes; 0 invalid or blank latest hashes |
| Canonical headers | 84 files; 0 issues |
| Architecture terminology | 108 operative artefacts; 4 sealed-Law exceptions; 0 warnings |
| Runtime-processing architecture | 10 phases; authority, transition, re-entry and representation boundaries intact |
| Document provenance / citation | 0 issues |
| AI-BOM / Runtime State | all canonical examples and repository manifests passed |
| Markdown section references | 1,114 references; 916 passed; 198 historical-ledger references ignored; 0 hard failures; 0 manual review |
| Metadata / source authority | 88 operative instruments; 0 issues |
| Idempotency rerun | Identical tracked working-diff SHA-256 before and after: `5fcb17b31a678e77e26b4724cc5a44978e68614bc3ec6a62123562ba3ef2622f`; the untracked closure and inventory artefacts were unchanged by the rerun |

## 8. Closure disposition

V-05 is closed with zero unexplained declaration diagnostics. No active aliases were retained. Historical identifiers remain only where version fidelity or explicit retirement explanation requires them. No source-authority collision, ambiguous ownership, compatibility choice or semantic decision remains for maintainer adjudication.

The constitutional ten-phase Runtime engine was not amended. VIGIL was not modified. The branch's intentional divergence from `main` remains untouched.
