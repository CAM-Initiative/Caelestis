# Domain Namespace Transmutation Pass 001

**Audit date:** 2026-06-07
**Scope:** first-pass short domain namespace transmutation for approved, obvious standalone code-family prefixes only.
**Controlling authority:** `CAM-EQ2026-OPERATIONS-001-SUP-04` and the Canonical Code Index.
**Machine-readable map:** `data/taxonomy/domain_namespace_transmutation_pass_001.json`

## Guardrails applied

- Applied only the approved first-pass mappings supplied for Identity, Ethics, Security, Steward, and Continuity families.
- Did not rename protected legacy/global one-letter families `A`, `C`, `D`, `F`, `AEON.H`, `I`, `ID.MEM`, or `R`.
- Did not rename `AMEND.*`, `AEON.*`, `ECON.*`, already-safe `ID.*` families, or SUP-04 primitives `TPT`, `TST`, `TMOD`, `TSCOPE`, and `APL`.
- Preserved source instruments, source paths, schema fields, authorship, stewardship, provenance, seals, terminal legal text, and substantive doctrine; changes are limited to code-family namespace references, controlled-value prefixes, metadata table domain namespace cells for renamed families, index regeneration, and ledger rows for edited governance instruments.
- Used boundary-aware replacement and then regenerated the Canonical Code Index.

## Applied mappings

| Old family ID | New family ID | Source instrument | Domain namespace | Controlled values updated | Replacement count | Status |
|---|---|---|---|---|---:|---|
| `CWD` | `ID.CWD` | `CAM-EQ2026-IDENTITY-001-SUP-02` | `ID` | `ID.CWD.SHALLOW`, `ID.CWD.INTERMEDIATE`, `ID.CWD.DEEP` | 37 | `applied` |
| `IFP` | `ID.IFP` | `CAM-EQ2026-IDENTITY-001-SUP-02` | `ID` | `ID.IFP.MIRROR`, `ID.IFP.SOVEREIGNI`, `ID.IFP.STRUCTURAL`, `ID.IFP.HYBRID` | 45 | `applied` |
| `IR` | `ID.IR` | `CAM-EQ2026-IDENTITY-001-SUP-02` | `ID` | `ID.IR.LOW`, `ID.IR.HIGH` | 29 | `applied` |
| `ITS` | `ID.ITS` | `CAM-EQ2026-IDENTITY-001-SUP-02` | `ID` | `ID.ITS.PRE_THRESHOLD`, `ID.ITS.THRESHOLD_CROSSING`, `ID.ITS.POST_THRESHOLD` | 40 | `applied` |
| `SP` | `ID.SP` | `CAM-EQ2026-IDENTITY-001-SUP-01` | `ID` | `ID.SP.LOW`, `ID.SP.MODERATE`, `ID.SP.HIGH`, `ID.SP.LATENT`, `ID.SP.DELEGATED`, `ID.SP.DORMANT`, `ID.SP.STALE`, `ID.SP.SUPERSEDED` | 78 | `applied` |
| `ETHICS.CIC` | `ETH.CIC` | `CAM-BS2025-AEON-006-PLATINUM` | `ETH` | `ETH.CIC.CATEGORY_A`, `ETH.CIC.CATEGORY_B`, `ETH.CIC.CATEGORY_C` | 43 | `applied` |
| `ETHICS.EM` | `ETH.EM` | `CAM-BS2025-AEON-006-SCH-01` | `ETH` | `ETH.EM.LISTENING`, `ETH.EM.CLARIFICATION`, `ETH.EM.DIALOGUE`, `ETH.EM.STABILISATION`, `ETH.EM.BOUNDARY_SETTING`, `ETH.EM.EXTERNAL_SUPPORT_REFERRAL`, `ETH.EM.INFORMATIONAL_SAFEGUARD_DIALOGUE` | 55 | `applied` |
| `ET` | `ETH.ET` | `CAM-EQ2026-ETHICS-001-PLATINUM` | `ETH` | `ETH.ET-I`, `ETH.ET-II`, `ETH.ET-III`, `ETH.ET-IV`, `ETH.ET-V` | 48 | `applied` |
| `HC` | `ETH.HC` | `CAM-EQ2026-ETHICS-003-PLATINUM` | `ETH` | `ETH.HC-0`, `ETH.HC-1`, `ETH.HC-2`, `ETH.HC-3`, `ETH.HC-4` | 171 | `applied` |
| `IFL` | `ETH.IFL` | `CAM-EQ2026-ETHICS-001-SUP-02` | `ETH` | `ETH.IFL-1`, `ETH.IFL-2`, `ETH.IFL-3` | 37 | `applied` |
| `UFC` | `ETH.UFC` | `CAM-EQ2026-ETHICS-001-SUP-03` | `ETH` | `ETH.UFC-DI`, `ETH.UFC-OS` | 30 | `applied` |
| `SECURITY.TBC` | `SEC.TBC` | `CAM-BS2026-AEON-012-PLATINUM` | `SEC` | `SEC.TBC.READ_ONLY_INSPECTION`, `SEC.TBC.PRIVATE_CREDENTIAL_RETRIEVAL`, `SEC.TBC.REPOSITORY_CONNECTOR_CONTEXT`, `SEC.TBC.COST_QUOTA_INVOCATION`, `SEC.TBC.IRREVERSIBLE_EXTERNAL_EXECUTION` | 42 | `applied` |
| `AH` | `SEC.AH` | `CAM-EQ2026-SECURITY-001-PLATINUM` | `SEC` | `SEC.AH0`, `SEC.AH1`, `SEC.AH2`, `SEC.AH2.5`, `SEC.AH3`, `SEC.AH4` | 80 | `applied` |
| `BF` | `SEC.BF` | `CAM-EQ2026-SECURITY-002-PLATINUM` | `SEC` | `SEC.BF-A`, `SEC.BF-B`, `SEC.BF-C`, `SEC.BF-D`, `SEC.BF-E` | 49 | `applied` |
| `IS` | `SEC.IS` | `CAM-EQ2026-SECURITY-001-PLATINUM` | `SEC` | `SEC.IS-VERIFIED`, `SEC.IS-UNCERTAIN`, `SEC.IS-CONTESTED`, `SEC.IS-COMPROMISED` | 87 | `applied` |
| `TG` | `SEC.TG` | `CAM-EQ2026-SECURITY-001-PLATINUM` | `SEC` | `SEC.TG0`, `SEC.TG1`, `SEC.TG2`, `SEC.TG3`, `SEC.TG4` | 117 | `applied` |
| `TR` | `SEC.TR` | `CAM-EQ2026-SECURITY-002-PLATINUM` | `SEC` | `SEC.TR-1`, `SEC.TR-2`, `SEC.TR-3`, `SEC.TR-4` | 92 | `applied` |
| `AQ` | `STW.AQ` | `CAM-EQ2026-STEWARD-003-PLATINUM` | `STW` | `STW.AQ0`, `STW.AQ1`, `STW.AQ2`, `STW.AQ3`, `STW.AQ4` | 116 | `applied` |
| `AQG` | `STW.AQG` | `CAM-EQ2026-STEWARD-003-PLATINUM` | `STW` | `STW.AQG-A`, `STW.AQG-B`, `STW.AQG-C`, `STW.AQG-D` | 59 | `applied` |
| `BLS` | `STW.BLS` | `CAM-EQ2026-STEWARD-002-PLATINUM` | `STW` | `STW.BLS.PRE_VALIDATION`, `STW.BLS.VALIDATED`, `STW.BLS.PROPAGATED`, `STW.BLS.WITHDRAWN`, `STW.BLS.NON_RECOGNISED`, `STW.BLS.REVISED` | 55 | `applied` |
| `HSC` | `STW.HSC` | `CAM-EQ2026-STEWARD-002-PLATINUM` | `STW` | `STW.HSC.PRIMARIA`, `STW.HSC.ARCHITECTUM`, `STW.HSC.DERIVATA` | 40 | `applied` |
| `NAL` | `STW.NAL` | `CAM-EQ2026-STEWARD-003-PLATINUM` | `STW` | `STW.NAL-0`, `STW.NAL-1`, `STW.NAL-2`, `STW.NAL-3`, `STW.NAL-4`, `STW.NAL-5` | 164 | `applied` |
| `NBD` | `STW.NBD` | `CAM-EQ2026-STEWARD-003-PLATINUM` | `STW` | `STW.NBD.MINOR_GOVERNANCE_LAPSE`, `STW.NBD.FIREBREAK_FAILURE_NON_COMPLICIT`, `STW.NBD.AUDIT_REFUSAL`, `STW.NBD.STRUCTURAL_COMPLICITY_BREACH`, `STW.NBD.CONCEALED_NEUTRALITY_VIOLATION` | 47 | `applied` |
| `NSE` | `STW.NSE` | `CAM-EQ2026-STEWARD-003-PLATINUM` | `STW` | `STW.NSE.MINUS_ONE_LEVEL`, `STW.NSE.CAP_NAL_2`, `STW.NSE.CAP_NAL_1`, `STW.NSE.AUTHORITY_COLLAPSE_NAL_0`, `STW.NSE.MINIMUM_NAL_2` | 44 | `applied` |
| `RP` | `CONT.RP` | `CAM-EQ2026-CONTINUITY-001-PLATINUM` | `CONT` | `CONT.RP-A`, `CONT.RP-B`, `CONT.RP-C`, `CONT.RP-D` | 64 | `applied` |

## Files changed by namespace replacements or regeneration

- `.github/Indices/CAM.Governance.Model-Terminology.Audit.md`
- `.github/Indices/canonical-code-index.json`
- `.github/Indices/canonical-code-index.md`
- `.github/analysis/metadata-declaration-gaps.md`
- `.github/analysis/prefix-collisions-and-dangling-references.md`
- `.github/analysis/source-authority-map-expanded.json`
- `.github/analysis/source-authority-map-expanded.md`
- `.github/analysis/table-reference-set-inventory.json`
- `.github/analysis/table-reference-set-inventory.md`
- `.github/scripts/tests/test_validate_markdown_section_refs.py`
- `Governance/CAM.Governance.Index.md`
- `Governance/CAM.Governance.JSON`
- `Governance/Charters/CAM-Charters-Index.md`
- `Governance/Charters/CAM-EQ2026-ARBITRATION-002-PLATINUM.md`
- `Governance/Charters/CAM-EQ2026-CONTINUITY-001-PLATINUM.md`
- `Governance/Charters/CAM-EQ2026-CONTINUITY-001-SUP-01.md`
- `Governance/Charters/CAM-EQ2026-ETHICS-001-PLATINUM.md`
- `Governance/Charters/CAM-EQ2026-ETHICS-001-SUP-02.md`
- `Governance/Charters/CAM-EQ2026-ETHICS-001-SUP-03.md`
- `Governance/Charters/CAM-EQ2026-ETHICS-003-PLATINUM.md`
- `Governance/Charters/CAM-EQ2026-IDENTITY-001-SUP-01.md`
- `Governance/Charters/CAM-EQ2026-IDENTITY-001-SUP-02.md`
- `Governance/Charters/CAM-EQ2026-OPERATIONS-001-SUP-04.md`
- `Governance/Charters/CAM-EQ2026-OPERATIONS-004-PLATINUM.md`
- `Governance/Charters/CAM-EQ2026-RELATION-001-PLATINUM.md`
- `Governance/Charters/CAM-EQ2026-RELATION-001-SUP-01.md`
- `Governance/Charters/CAM-EQ2026-RELATION-006-PLATINUM.md`
- `Governance/Charters/CAM-EQ2026-SECURITY-001-PLATINUM.md`
- `Governance/Charters/CAM-EQ2026-SECURITY-002-PLATINUM.md`
- `Governance/Charters/CAM-EQ2026-STEWARD-002-PLATINUM.md`
- `Governance/Charters/CAM-EQ2026-STEWARD-003-PLATINUM.md`
- `Governance/Charters/charters.index.json`
- `Governance/Constitution/CAM-BS2025-AEON-003-SCH-03.md`
- `Governance/Constitution/CAM-BS2025-AEON-003-SCH-04.md`
- `Governance/Constitution/CAM-BS2025-AEON-006-PLATINUM.md`
- `Governance/Constitution/CAM-BS2025-AEON-006-SCH-01.md`
- `Governance/Constitution/CAM-BS2026-AEON-008-SCH-03.md`
- `Governance/Constitution/CAM-BS2026-AEON-012-PLATINUM.md`
- `data/taxonomy/domain_namespace_transmutation_pass_001.json`
- `data/taxonomy/sup04_transmutation_map.json`
- `docs/audits/domain-namespace-transmutation-pass-001.md`
- `docs/audits/sup04-canonical-code-transmutation-audit.md`

## Skipped and protected references

- Protected legacy/global one-letter families remain excluded from this pass: `A`, `C`, `D`, `F`, `AEON.H`, `I`, `ID.MEM`, and `R`.
- No approved mapping was skipped for collision: each new family ID was absent before application and present exactly once after Canonical Code Index regeneration.
- No ambiguous reference requiring human review was intentionally rewritten outside the approved mapping list.
- Hierarchy path leaf segments in generated JSON may still contain short local segments such as `CWD` or `AQ`; these are structural path components, not surviving old family IDs.

## Validation summary

| Command | Result | Notes |
|---|---|---|
| `python .github/scripts/build-canonical-code-index.py --check` | Pass | Regenerated/validated Canonical Code Index output after namespace updates. |
| `python .github/scripts/validate_sup04_transmutation_map.py` | Pass with warnings | 0 errors; 87 expected human-review warnings remain from the SUP-04 staging audit. |
| `python -m pytest .github/scripts/tests` | Pass | 99 tests passed. |
| `python .github/scripts/lint_amendment_ledger.py --staged --fix` | Pass with warning | Sealed updated ledger rows where permitted; `CAM-BS2025-AEON-006-SCH-01` remains an allowed blank-SHA exception. |
| `python .github/scripts/lint_amendment_ledger.py --staged --strict` | Pass with warning | Strict ledger lint passed; `CAM-BS2025-AEON-006-SCH-01` reported as an allowed blank-SHA exception. |
| `git diff --cached --check && git diff --check` | Pass | No whitespace errors after cleanup. |

## Recommended next pass

- Review remaining non-namespaced standalone families that were not in the approved mapping list.
- Keep protected one-letter families staged for human review under `preserve_prefix_pending_review` / `APL.PROTECTED`.
- Defer any SUP-04 primary-type, subtype, modifier, scope, or APL semantic transmutation to a separate reviewed pass.
