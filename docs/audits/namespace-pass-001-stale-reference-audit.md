# Namespace Pass 001 Stale Reference Audit

## 1. Scope and guardrails

This audit verifies the approved Domain Namespace Transmutation Pass 001 mappings and applies only narrow, mechanical stale-reference cleanup. It does not introduce new namespace mappings, does not rename `ETH.HC` to `AEON.HC`, does not rename `ECON.HARM`, does not create `AEON.HC`, and does not alter protected legacy/global one-letter families (`A`, `C`, `D`, `F`, `AEON.H`, `I`, `ID.MEM`, `R`).

The cleanup was triggered by the Harm Class layer-placement audit, which identified stale `ETHICS.HC` consumer metadata in `CAM-BS2025-AEON-006-SCH-01` after Pass 001.

## 2. Summary of stale references found

| Classification | Count | Notes |
|---|---:|---|
| `safe_mechanical_update` | 2 | Two source metadata rows in `CAM-BS2025-AEON-006-SCH-01` consumed `ETHICS.HC` after the current family became `ETH.HC`. |
| `generated_artifact_regenerate` | 2 | Two stale `ETHICS.HC` strings in `.github/Indices/canonical-code-index.json` were regenerated from the corrected source metadata. |
| `historical_reference_preserve` | 52 | Existing Pass 001 migration artifacts and the Harm Class audit intentionally preserve old IDs and stale-reference findings. |
| `ambiguous_human_review` | 0 | No unresolved ambiguous stale references were found after boundary-aware review. |
| `false_positive` | Multiple categories | Short-code searches surfaced substring/acronym risks such as `IR` inside `ETHICS.MIR`, `SP` inside `AEON.GSP`, and `RP` inside `CRP` / `AEON.GRP`; these were not stale Pass 001 references. |

## 3. Mappings checked

| Old family ID | New family ID | Result |
|---|---|---|
| `ETHICS.CIC` | `ETH.CIC` | No current stale reference found outside historical Pass 001 artifacts. |
| `ETHICS.EM` | `ETH.EM` | No current stale reference found outside historical Pass 001 artifacts. |
| `ET` | `ETH.ET` | No current stale reference found; short-code false-positive risk reviewed. |
| `HC` / stale alias `ETHICS.HC` | `ETH.HC` | Fixed two source metadata references and regenerated Canonical Code Index JSON. |
| `IFL` | `ETH.IFL` | No current stale reference found outside historical Pass 001 artifacts. |
| `UFC` | `ETH.UFC` | No current stale reference found outside historical Pass 001 artifacts. |
| `SECURITY.TBC` | `SEC.TBC` | No current stale reference found outside historical Pass 001 artifacts. |
| `AH` | `SEC.AH` | No current stale reference found; short-code false-positive risk reviewed. |
| `BF` | `SEC.BF` | No current stale reference found; short-code false-positive risk reviewed. |
| `IS` | `SEC.IS` | No current stale reference found; short-code false-positive risk reviewed. |
| `TG` | `SEC.TG` | No current stale reference found; short-code false-positive risk reviewed. |
| `TR` | `SEC.TR` | No current stale reference found; short-code false-positive risk reviewed. |
| `CWD` | `ID.CWD` | No current stale reference found outside historical Pass 001 artifacts. |
| `IFP` | `ID.IFP` | No current stale reference found outside historical Pass 001 artifacts. |
| `IR` | `ID.IR` | No current stale reference found; `ETHICS.MIR` heading matches were false positives. |
| `ITS` | `ID.ITS` | No current stale reference found outside historical Pass 001 artifacts. |
| `SP` | `ID.SP` | No current stale reference found; `AEON.GSP` matches were false positives. |
| `AQ` | `STW.AQ` | No current stale reference found; short-code false-positive risk reviewed. |
| `AQG` | `STW.AQG` | No current stale reference found outside historical Pass 001 artifacts. |
| `BLS` | `STW.BLS` | No current stale reference found outside historical Pass 001 artifacts. |
| `HSC` | `STW.HSC` | No current stale reference found outside historical Pass 001 artifacts. |
| `NAL` | `STW.NAL` | No current stale reference found outside historical Pass 001 artifacts. |
| `NBD` | `STW.NBD` | No current stale reference found outside historical Pass 001 artifacts. |
| `NSE` | `STW.NSE` | No current stale reference found outside historical Pass 001 artifacts. |
| `RP` | `CONT.RP` | No current stale reference found; `CRP` and `AEON.GRP` matches were false positives. |

## 4. Stale references fixed

| File | Old reference | New reference | Classification | Notes |
|---|---|---|---|---|
| `Governance/Constitution/CAM-BS2025-AEON-006-SCH-01.md` | `ETHICS.HC` | `ETH.HC` | `safe_mechanical_update` | Corrected the `ETH.EM` metadata `Consumes Code Families` row. |
| `Governance/Constitution/CAM-BS2025-AEON-006-SCH-01.md` | `ETHICS.HC` | `ETH.HC` | `safe_mechanical_update` | Corrected the `ETHICS.TP` metadata `Consumes Code Families` row. |
| `.github/Indices/canonical-code-index.json` | `ETHICS.HC` | `ETH.HC` | `generated_artifact_regenerate` | Regenerated after the source metadata correction. |
| `.github/Indices/canonical-code-index.json` | `ETHICS.HC` | `ETH.HC` | `generated_artifact_regenerate` | Regenerated after the source metadata correction. |

The existing open Amendment Ledger row in `CAM-BS2025-AEON-006-SCH-01` was updated in place to include the narrow stale-reference cleanup, preserving the Single Open Ledger Row Rule.

## 5. Historical references intentionally preserved

The following references are historical and were not rewritten:

- Old IDs in `data/taxonomy/domain_namespace_transmutation_pass_001.json`, because that file records the Pass 001 old-to-new mapping.
- Old IDs in `docs/audits/domain-namespace-transmutation-pass-001.md`, because that audit intentionally records mappings applied during Pass 001.
- `ETHICS.HC` references in `docs/audits/harm-class-layer-placement-audit.md` and `data/taxonomy/harm_class_layer_placement_audit.json`, because those artifacts intentionally record the stale-reference finding that this cleanup addresses.

## 6. Generated artifacts regenerated

| Generated artifact | Regeneration command | Result |
|---|---|---|
| `.github/Indices/canonical-code-index.json` | `python .github/scripts/build-canonical-code-index.py` | Regenerated from corrected source metadata. |

No manual generated-index edit was made for the stale `ETHICS.HC` strings.

## 7. Ambiguous references requiring human review

None. Boundary-aware searches did not identify any unresolved ambiguous stale Pass 001 references.

## 8. False positive categories

| Category | Examples | Treatment |
|---|---|---|
| Substrings inside other code families | `IR` inside `ETHICS.MIR`; `SP` inside `AEON.GSP`; `RP` inside `CRP` / `AEON.GRP` | `false_positive`; no edit. |
| Ordinary prose / acronym risk for short codes | `IR`, `IS`, `SP`, `ET`, `HC`, `BF`, `TR`, `TG`, `AQ`, `RP` | Boundary-aware searches only; no broad replacement. |
| Historical audit/migration references | Pass 001 mapping records and audit tables | `historical_reference_preserve`; no edit. |

## 9. Files changed

| File | Change |
|---|---|
| `Governance/Constitution/CAM-BS2025-AEON-006-SCH-01.md` | Replaced two stale `ETHICS.HC` consumer references with `ETH.HC`; updated the existing open ledger row description in place. |
| `.github/Indices/canonical-code-index.json` | Regenerated to reflect corrected `ETH.HC` consumer metadata. |
| `docs/audits/namespace-pass-001-stale-reference-audit.md` | Added this human-readable stale-reference audit. |
| `data/taxonomy/namespace_pass_001_stale_reference_audit.json` | Added machine-readable stale-reference audit data. |

## 10. Commands run

```bash
rg -n --hidden --glob '!*.pyc' --glob '!__pycache__/**' --glob '!.git/**' 'ETHICS\.(CIC|EM|HC)|SECURITY\.TBC' .
python - <<'PY'
# Derived old controlled-value patterns from data/taxonomy/domain_namespace_transmutation_pass_001.json
# and searched them with boundary-aware ripgrep patterns.
PY
python .github/scripts/build-canonical-code-index.py
python .github/scripts/build-canonical-code-index.py --check
python .github/scripts/validate_sup04_transmutation_map.py
python -m pytest .github/scripts/tests
python -m json.tool data/taxonomy/namespace_pass_001_stale_reference_audit.json
python .github/scripts/lint_amendment_ledger.py --base HEAD~1 --head HEAD --fix
python .github/scripts/lint_amendment_ledger.py --base HEAD~1 --head HEAD --strict
git diff --check
```

## 11. Validation/test results

| Command | Result | Notes |
|---|---|---|
| `python .github/scripts/build-canonical-code-index.py --check` | Passed | Canonical Code Index is current after regeneration. |
| `python .github/scripts/validate_sup04_transmutation_map.py` | Passed with warnings | 0 errors; 87 expected human-review warnings. |
| `python -m pytest .github/scripts/tests` | Passed | 99 tests passed. |
| `python -m json.tool data/taxonomy/namespace_pass_001_stale_reference_audit.json` | Passed | New machine-readable audit JSON is valid. |
| `python .github/scripts/lint_amendment_ledger.py --base HEAD~1 --head HEAD --fix` | Passed | Ledger tooling left the current open row blank as allowed pending merge. |
| `python .github/scripts/lint_amendment_ledger.py --base HEAD~1 --head HEAD --strict` | Passed with warnings | Allowed blank-SHA warnings for `CAM-BS2025-AEON-006-SCH-01`. |

## 12. Final recommendation

The only confirmed current stale reference class was `ETHICS.HC` in SCH-01 consumer metadata and its regenerated canonical-index projection. That stale reference has been mechanically corrected to `ETH.HC`. No additional namespace mappings should be introduced in this cleanup pass.
