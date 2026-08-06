# Pass 1 — Repository Hygiene, Working-File Disposition and Corpus Surface Audit

## Status

**Completed:** 2026-08-06  
**Branch:** `agent/corpus-industry-standards-normalisation`  
**Normative corpus changes:** None

---

## Purpose

Pass 1 establishes a clean repository baseline before substantive obsolescence, contradiction and glaring-omission findings are recorded.

It separates governed corpus material from working review material, removes completed one-off artefacts, and preserves operational tooling where a current dependency, reproducibility need or test surface remains.

---

## Location rule

Active review material is retained under:

`.github/Reviews/`

No review report, delta ledger, migration working paper, trigger note or audit scratch file is retained under `Governance/` unless it is an adopted governed instrument.

Generated review evidence belongs under:

`.github/Reviews/generated/`

---

## Completed cleanup

The following completed review records were removed from the current tree after their associated refactors were merged:

- `Governance/Reviews/AEON-003-COMPOSED-ARCHITECTURE-REFACTOR-REPORT.md`
- `Governance/Reviews/IDENTITY-DOMAIN-REFACTOR-DELTA.md`
- `Governance/Reviews/IDENTITY-DOMAIN-STAGE-3-SUPPLEMENT-DISPOSITION.md`
- `Governance/Reviews/RED-LINE-FRAMEWORK-CORPUS-INTEGRATION.md`
- `Governance/Reviews/RELATIONAL-IDENTITY-CONSOLIDATION-DELTA.md`

The following completed red-team automation artefacts were removed:

- `.github/trigger/red-team-governance-20260726.txt`
- `.github/workflows/apply-red-team-governance-extension.yml`
- `scripts/apply_red_team_governance_extension.py`

The following speculative Advanced Voice working files were removed because this repository contains no production voice runtime implementation and the files were not current governed sources:

- `.github/Audit/Advanced-Voice-Mode-Audit-Symbolic-Counting-Drift.md`
- `.github/Audit/Advanced-Voice-Mode-Implementation-Map.md`

Their history remains available in Git.

---

## Retained operational tooling

The following apparently migration- or repair-oriented files were reviewed and retained because they remain documented, tested, reproducible repository tooling:

- `.github/scripts/bootstrap-amendment-ledger-sha.py`
- `.github/scripts/migrate-amendment-ledger-provenance.py`
- `.github/scripts/repair_governance_validations.py`
- `.github/scripts/tests/test_migrate_amendment_ledger_provenance.py`
- `.github/scripts/tests/test_repair_governance_validations.py`

The migration script is explicitly documented as a schema-migration and recovery tool. The repair script is deterministic and constrained to recognised reference and ledger repairs. Neither was treated as disposable merely because its primary migration has completed.

All index builders, validators, archive tools, shared libraries, tests, active workflows, issue templates, hooks and generated governance outputs were retained.

---

## Current review surface

The only active human review files are:

- `.github/Reviews/CAELESTIS-CORPUS-OBSOLESCENCE-CONTRADICTION-REVIEW.md`
- `.github/Reviews/PASS-1-REPOSITORY-HYGIENE-AND-DISPOSITION.md`
- `.github/Reviews/PASS-1-DISPOSITION-REGISTER.md`
- `.github/Reviews/PASS-1-DISPOSITION-REGISTER.json`

---

## Pass 1 determination

The governed `Governance/` tree now contains governed instruments, governed standards and generated governance outputs only. Working reviews are separated into `.github/Reviews/`.

No normative doctrine was changed during Pass 1.

The repository is ready for Pass 2: substantive identification of obsolete content, internal and external contradictions, unsupported claims, misplaced source authority and glaring missing controls.