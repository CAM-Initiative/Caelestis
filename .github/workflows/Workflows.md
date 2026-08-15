# CAM Repository Workflows

Last updated: 2026-04-29 (UTC)

## Canonical code index generation

- Generator script: `python .github/scripts/build-canonical-code-index.py`
- Outputs:
  - `Governance/CAM.Canonical.Code.Index.md`
  - `Governance/CAM.Canonical.Code.Index.json`
- Check mode:
  - `python .github/scripts/build-canonical-code-index.py --check`
  - Non-zero exit in check mode only for:
    - duplicate code declarations across instruments,
    - conflicting taxonomy type for same code,
    - malformed canonical declaration rows.

## Index generation workflow

Use these scripts to regenerate governance indexes:

- `python .github/scripts/update-CAM-Constitution-Index.py`
- `python .github/scripts/update-CAM-Charters-Index.py`
- `python .github/scripts/update-CAM-Laws-Index.py`

Each script now emits debug telemetry:

- number of markdown files detected
- number of entries written
- list of skipped files (if any)

## Hash source of truth

- Constitution and Charters JSON `HASH` values are sourced from each document's Amendment Ledger (latest valid SHA-256 row).
- Laws JSON `HASH` values are sourced from `MANIFEST.json`.

## Verification workflow

- Coverage/integrity check:
  - `python .github/scripts/verify-ledger-sha-coverage.py`
- Law manifest integrity check:
  - `python .github/scripts/verify-law-manifest-integrity.py`

## Typical maintenance sequence

1. Update governance instruments.
2. Regenerate indexes with the three update scripts above.
3. Run verification scripts.
4. Commit generated JSON changes together with script changes.

# Workflow Write Ownership Audit

| Workflow | Triggers | Scripts Run | Writes / Generated Files | Pushes to `main` | Broad `git add .` |
|---|---|---|---|---|---|
| Lint Amendment Ledger | `pull_request`, `push` | `build-canonical-code-index.py`, `lint-symbolic-structures.py`, `lint_amendment_ledger.py` | none (validation-only) | no | no |
| Update Amendment Ledgers | Removed | N/A | N/A | N/A | N/A |
| Update Constitution Index | `push` (`main`) | `update-CAM-Constitution-Index.py` | `Governance/Constitution/CAM-Constitution-Index.md`, `Governance/Constitution/constitution.index.json` | yes | no |
| Update Law Index | `push` (`main`) | `update-CAM-Laws-Index.py` | `Governance/Laws/CAM-Laws-Index.md`, `Governance/Laws/laws.index.json` | yes | no |
| Update Charters Index | `push` (`main`) | `update-CAM-Charters-Index.py` | `Governance/Charters/CAM-Charters-Index.md`, `Governance/Charters/charters.index.json` | yes | no |
| Update Governance Index (canonical shared-output writer) | `push` (`main`) | `update-CAM-Governance-Index.py`, both registry generators, `update-CAM-Model-Terminology-Audit.py`, `build-canonical-code-index.py` | consolidated governance outputs, generated registry projections, terminology audit, canonical code index JSON/MD | yes | no |
| Validate generated governance registries | `pull_request`, `workflow_dispatch` | both registry generators, `update-CAM-Model-Terminology-Audit.py` | none (validation-only stale check) | no | no |

## Ownership Model

- **Single workflow writer for shared governance/registry/symbolic generated outputs:** `Update Governance Index`.
- Domain workflows remain writers only for their own domain index artifacts.
- Lint workflows are validation-only and do not auto-commit.


# CAM Governance Scripts Index & Troubleshooting Guide

This folder contains operational scripts used by the CAM governance repository to rebuild indexes, validate amendment-ledger integrity, refresh generated registry sections, lint symbolic structures, validate references, install local hooks, and package archival releases.

These scripts are operational tooling. They support the governance corpus, but they do not themselves create doctrinal authority.

---

## 1. Operational Principles

Scripts in `.github/scripts/` SHOULD be treated as deterministic maintenance tooling.

They MAY:

* rebuild generated indexes;
* validate amendment ledgers;
* seal latest amendment-ledger HASH cells;
* refresh generated registry blocks;
* validate section references;
* lint symbolic structures and canonical code declarations;
* package archival releases;
* support local pre-commit checks.

They SHOULD NOT:

* silently rewrite doctrinal text outside declared generated sections;
* invent instrument lineage, authority, or metadata;
* mutate governance instruments without an explicit validation or generation purpose;
* create untracked output that is not either committed or intentionally ignored.

Generated-block scripts SHOULD only mutate text between declared START/END markers.

Manual recovery scripts SHOULD be narrow, diagnostic, and reversible.

---

## 2. Script Families

### 2.1 Governance Index Builders

These scripts rebuild index and JSON views from governance source documents.

| Script | Purpose | Mutates Files | Normal Use |
| --- | --- | --- | --- |
| `update-CAM-Constitution-Index.py` | Rebuilds Constitution index/json outputs | Yes | Governance rebuild Phases 1, 3, 8 |
| `update-CAM-Charters-Index.py` | Rebuilds Charter index/json outputs | Yes | Governance rebuild Phases 1, 3, 8 |
| `update-CAM-Laws-Index.py` | Rebuilds Laws index/json outputs | Yes | Governance rebuild Phases 1, 3, 8 |
| `update-CAM-Governance-Index.py` | Rebuilds consolidated governance registry/index | Yes | Governance rebuild Phases 5, 7, 8 |

Run these when metadata, instrument files, amendment ledgers, or generated registry inputs have changed.

---

### 2.2 Generated Registry Projection Builders

These scripts rebuild non-authoritative registry projections under `Governance/` after the source indexes and `CAM.Governance.JSON` are current. The Governance Metadata Standard specifies the constitutional Schedule registry; `CAM-EQ2026-OPERATIONS-001-SUP-04 §11.1` specifies the global operative-instrument registry.

| Script | Purpose | Mutates Files | Normal Use |
| --- | --- | --- | --- |
| `update-CAM-Constitutional-Schedule-Registry.py` | Refreshes generated constitutional Schedule registry projection | Yes | Governance rebuild Phase 6 |
| `update-CAM-Global-Operative-Instrument-Registry.py` | Refreshes generated global operative-instrument registry projection | Yes | Governance rebuild Phase 6 |
| `update-CAM-Model-Terminology-Audit.py` | Refreshes the generated model-terminology audit and registry summary | Yes | Governance rebuild Phase 6 |

These should usually be run only after source indexes and the consolidated governance registry have been rebuilt.

---

### 2.3 Amendment Ledger Tools

These scripts enforce ledger discipline and HASH coverage.

| Script | Purpose | Mutates Files | Normal Use |
| --- | --- | --- | --- |
| `lint_amendment_ledger.py` | Validates amendment-ledger rows, version increments, and latest HASH values; can seal latest HASH cells with `--fix` | Yes, with `--fix` | Governance rebuild Phases 2 and 8; manual recovery |
| `bootstrap-amendment-ledger-sha.py` | Bootstrap/recovery helper for amendment-ledger SHA population | Yes | Manual recovery only |
| `verify-ledger-sha-coverage.py` | Verifies ledger SHA coverage and JSON/index consistency | No | Governance rebuild Phase 4 |
| `migrate-amendment-ledger-provenance.py` | Deterministically migrates legacy ledgers and removes static provenance blocks | Yes, with `--apply` | Schema migration and recovery only |

Supporting policy files:

| File | Purpose |
| --- | --- |
| `lib/ledger_sha_policy.py` | Classifies valid, blank, placeholder, historical, latest, and strict ledger SHA states |
| `lib/ledger_sha_exceptions.py` | Records intentional blank-SHA exceptions where governance-approved |
| `lib/amendment_ledger.py` | Defines and parses the canonical seven-column header by name |

The required ledger order is `Version`, `Change Summary`, `Timestamp (UTC)`, `Agent`, `Model`, `Reviewer`, `Reference Hash`. Every amendment row contains seven cells. Historical migrated rows use `Caelen`, `GPT-5 Series`, and `Dr M.V. O'Rourke`; exact model designations are used for new rows where known.

Use the ledger tools when CI reports:

* `Amendment Ledger not updated`;
* `latest ledger SHA is blank`;
* `Historical Amendment Ledger SHA invalid`;
* `Last Amendment Ledger hash must be empty or computed SHA-256`;
* `Downstream generated ledger update blocked`.

---

### 2.4 Reference and Markdown Validators

These scripts check whether instrument references are structurally valid.

| Script | Purpose | Mutates Files | Normal Use |
| --- | --- | --- | --- |
| `validate_canonical_headers.py` | Validates canonical governed-instrument H1 titles and duplicate top metadata/header blocks | No | Governance rebuild Phase 8 |
| `validate_document_provenance.py` | Validates the repository document-provenance manifest, citation-author alignment, controlled provenance values and non-inference boundaries | No | Governance rebuild Phase 8 |
| `validate_ai_bom.py` | Validates declared AI-system composition, formation element roles and model/agent/harness non-equivalence in canonical and repository AI-BOM records | No | Governance rebuild Phase 8 |
| `validate_runtime_state.py` | Validates evidence-backed Runtime state and resolves effective provider, harness, cognition, governance, continuity, context and tooling references into the applicable AI-BOM | No | Governance rebuild Phase 8 |
| `validate_markdown_section_refs.py` | Validates §-style local and cross-document section references | No | Governance rebuild Phase 8 |
| `lint_reference_shorthand.py` | Detects shorthand references and lowercase normative terms; can auto-capitalize normative terms | Yes, only with `--fix-normative-case` | Manual linting / cleanup |

`validate_markdown_section_refs.py` distinguishes local references, cross-document references, ambiguous named-instrument references, amendment-ledger references, and hard failures.

`lint_reference_shorthand.py` is useful when converting shorthand references into full CAM instrument references.

---

### 2.5 Symbolic Structure and Canonical Code Tools

These scripts support symbolic-structure registry validation and generated symbolic indexes.

| Script | Purpose | Mutates Files | Normal Use |
| --- | --- | --- | --- |
| `build-canonical-code-index.py` | Builds canonical code index files under `Governance/` | Yes | Governance rebuild Phase 8 |
| `lint-symbolic-structures.py` | Validates symbolic-structure registry shape, candidate prefixes, duplicate structures, collisions, and Canonical Codes metadata | No | Governance rebuild Phase 8 |

These scripts support taxonomy-of-taxonomies work, canonical code governance, symbolic registry hygiene, and collision detection.

If canonical code index outputs change during CI, ensure `Governance/` is staged by the workflow commit step.

---

### 2.6 Law Manifest Tooling

| Script | Purpose | Mutates Files | Normal Use |
| --- | --- | --- | --- |
| `verify-law-manifest-integrity.py` | Verifies law manifest/index integrity | No | Manual validation or future CI integration |

Use this when Governance/Laws material changes or when law index consistency is in doubt.

---

### 2.7 Archive and Release Packaging

| Script | Purpose | Mutates Files | Normal Use |
| --- | --- | --- | --- |
| `package_archive.py` | Builds deterministic archive packages and `MANIFEST.json` for release/deposit | Yes | Release packaging |
| `update_archive.py` | Updates archive-related metadata or generated archive outputs | Yes | Release maintenance |

`package_archive.py` refreshes generated governance views, checks required metadata/index files, writes `MANIFEST.json`, and produces deterministic `.zip` and `.tar.gz` archives under `dist/archive`.

Use this for Zenodo/public archive packaging, not for ordinary doctrine edits.

---

### 2.8 Parser and Shared Library Support

| File | Purpose |
| --- | --- |
| `governance-parser.py` | Parses governance documents for metadata/index workflows |
| `lib/instrument_parser.py` | Shared instrument parsing logic |
| `lib/instrument_state.py` | Shared instrument state helpers |
| `__init__.py` | Marks the script folder/package context |

These files are support code. They are normally invoked by other scripts rather than run directly.

---

### 2.9 Local Developer Tooling

| Script | Purpose |
| --- | --- |
| `install-git-hooks.sh` | Installs local git hooks for pre-commit or local validation workflows |

Use this in Codespaces or local development when you want earlier feedback before pushing to GitHub Actions.

---

### 2.10 Tests

| Test | Purpose |
| --- | --- |
| `tests/test_lint_amendment_ledger_sha_policy.py` | Tests ledger SHA policy behavior |
| `tests/test_validate_document_provenance.py` | Tests document-level provenance, contribution/authorship separation and citation alignment |
| `tests/test_validate_ai_bom.py` | Tests AI-BOM structure and prevents agent or harness identifiers from being classified as cognition models |
| `tests/test_validate_runtime_state.py` | Tests formation-reference resolution and provider/harness/model semantic-role separation |
| `tests/test_validate_markdown_section_refs.py` | Tests section-reference validation |
| `tests/test_verify_ledger_sha_coverage.py` | Tests ledger SHA coverage validation |
| `tests/test_build_canonical_code_index.py` | Tests source-derived declaration extraction, explicit parentage and declaration-shape failures |
| `tests/test_lint_symbolic_structures.py` | Tests corpus-wide canonical reference integrity, retired/current boundaries and generated-index agreement |

Run tests after changing validator logic, ledger policy, parser behavior, canonical header checks, or reference-classification rules.

```bash
python -m pytest .github/scripts/tests
```

## 3. Governance Rebuild Pipeline

The main workflow is .github/workflows/governance-rebuild.yml.

It runs on pushes and pull requests affecting:

```text
Governance/Constitution/**
Governance/Charters/**
Governance/Laws/**
Governance/Standards/**
Governance/Drafts/**
Governance/CAM.*
.github/scripts/**
.github/Indices/**
```

`Governance/CAM.*` is the narrow root-level projection pattern for the consolidated governance index/JSON, both relocated registries, and the canonical-code index. The workflow excludes bot-authored rebuild commits at the job boundary to prevent regeneration loops.

The workflow uses Python 3.11 and proceeds through nine operational phases.

### Phase 1 — Rebuild source indexes

Runs: 
```
python .github/scripts/update-CAM-Constitution-Index.py
python .github/scripts/update-CAM-Charters-Index.py
python .github/scripts/update-CAM-Laws-Index.py
```

Purpose: refresh source-level generated index/json views before ledger evaluation.

### Phase 2 — Ledger fix and strict validation

Runs, unless the change is law-only:
```
python .github/scripts/lint_amendment_ledger.py --base "$BASE_SHA" --head "$HEAD_SHA" --fix
python .github/scripts/lint_amendment_ledger.py --base "$BASE_SHA" --head "$HEAD_SHA" --strict
```
Purpose: seal latest amendment-ledger rows already prepared for changed governance instruments, then enforce strict seven-column ledger validity.

### Phase 3 — Rebuild source indexes post-HASH

Runs the Constitution, Charter, and Laws index builders again.

Purpose: refresh index/json outputs after ledger HASH values have changed.

Phase 4 — Verify ledger SHA coverage and JSON consistency

Runs:
```
python .github/scripts/verify-ledger-sha-coverage.py
```
Purpose: ensure generated index state and ledger HASH coverage remain consistent.

### Phase 5 — Build global Governance registry

Runs:
```
python .github/scripts/update-CAM-Governance-Index.py
```
Purpose: rebuild the consolidated governance registry after source indexes are current.

### Phase 6 — Rebuild generated governance registries

Runs:
```
python .github/scripts/update-CAM-Constitutional-Schedule-Registry.py
python .github/scripts/update-CAM-Global-Operative-Instrument-Registry.py
python .github/scripts/update-CAM-Model-Terminology-Audit.py
```
Purpose: rebuild the two relocated, non-authoritative registry projections and the model-terminology audit from current consolidated governance state.

### Phase 7 — Final global Governance rebuild

Runs:
```
python .github/scripts/update-CAM-Governance-Index.py
```
Purpose: refresh the consolidated governance registry after downstream registry generation without treating either projection as a source instrument.

### Phase 8 — Final validation, canonical code index rebuild, and idempotency check

Runs:
```
python .github/scripts/lint_amendment_ledger.py --base "$BASE_SHA" --head "$HEAD_SHA" --strict
python .github/scripts/validate_canonical_architecture_terminology.py
python .github/scripts/validate_runtime_processing_architecture.py
python .github/scripts/validate_markdown_section_refs.py --root Governance
python .github/scripts/lint-symbolic-structures.py
python .github/scripts/build-canonical-code-index.py
```
The architecture terminology validator Unicode-normalises current operative content, blocks retired architecture and relational-geometry terms, blocks high-confidence participant-cardinality governance classes, and permits only the four exact sealed-Law legacy geometry lines plus explicit historical/migration contexts. The Runtime-processing architecture validator verifies the ten phase contracts, authority existence, Tendeka and interruption returns, tool/sub-agent re-entry, RELATION ownership boundary, profile non-authority and execution/representation/evidence invariants. Then the workflow re-runs the major generators to ensure no stale or non-idempotent generated outputs remain.

Purpose: confirm the repository is stable after repeated generation.

### Phase 9 — Commit generated changes once

On push events, the workflow commits generated changes back to the branch.

Recommended staging command:
```
git add Governance/ .github/Indices/ .github/workflows/ .github/scripts/
```
The .github/Indices/ path is important because symbolic index generation may update files there.

## 4. Recommended Manual Commands
Rebuild all main indexes
```
python .github/scripts/update-CAM-Constitution-Index.py
python .github/scripts/update-CAM-Charters-Index.py
python .github/scripts/update-CAM-Laws-Index.py
python .github/scripts/update-CAM-Governance-Index.py
Seal amendment ledger hashes across all scoped instruments
python .github/scripts/lint_amendment_ledger.py --all --fix
Validate amendment ledger state
python .github/scripts/lint_amendment_ledger.py --all --strict
python .github/scripts/verify-ledger-sha-coverage.py
Validate section references
python .github/scripts/validate_markdown_section_refs.py --root Governance
Find shorthand references
python .github/scripts/lint_reference_shorthand.py --root Governance
Auto-capitalize lowercase normative terms
python .github/scripts/lint_reference_shorthand.py --root Governance --fix-normative-case
```
Review changes carefully before committing.
```
Rebuild canonical code indices
python .github/scripts/build-canonical-code-index.py
python .github/scripts/lint-symbolic-structures.py
Run script tests
python -m pytest .github/scripts/tests
Package public archive
python .github/scripts/package_archive.py
```
## 5. Manual Recovery: Ledger HASH Reset / Kickstart

Use manual ledger recovery when the normal governance rebuild is blocked by missing, blank, placeholder, or stale Amendment Ledger HASH values.

Recommended sequence:
```
git status --short

python .github/scripts/lint_amendment_ledger.py --all --fix
python .github/scripts/lint_amendment_ledger.py --all --strict
python .github/scripts/verify-ledger-sha-coverage.py

git status --short
```
Then review and commit only intended generated or ledger-updated files.

This process is intended to kickstart the normal governance pipeline, not replace it.

## 6. Common Failure Modes and Remedies
### 6.1 Amendment Ledger not updated

Likely cause: a governance document changed without a new ledger row.

Remedy:
```
python .github/scripts/lint_amendment_ledger.py --base HEAD~1 --head HEAD --fix
```
Then rerun strict validation.

### 6.2 Latest ledger SHA is blank

Likely cause: the latest amendment row has not been sealed yet.

Remedy:
```
python .github/scripts/lint_amendment_ledger.py --all --fix
```
Then rerun:
```
python .github/scripts/lint_amendment_ledger.py --all --strict
```

### 6.3 Historical Amendment Ledger SHA invalid

Likely cause: an older ledger row has a blank, malformed, or non-approved HASH value.

Remedy:

Confirm whether the blank is intentionally governance-approved.
If intentional, ensure the document is covered by lib/ledger_sha_exceptions.py.
If not intentional, repair or seal the historical row.

### 6.4 Dirty worktree before rebase or push

Likely cause: a generator produced files that were not staged or expected.

Remedy:
```
git status --short
```
Then determine whether the dirty files are intended generated outputs.

Common missing staging target:
```
.github/Indices/
```
If symbolic index outputs are expected, ensure the workflow stages .github/Indices/.

### 6.5 Stale or non-idempotent generated outputs

Likely cause: one generator depends on another generated file, or scripts ran in the wrong order.

Remedy: run the same order used by the workflow:
```
python .github/scripts/update-CAM-Constitution-Index.py
python .github/scripts/update-CAM-Charters-Index.py
python .github/scripts/update-CAM-Laws-Index.py
python .github/scripts/lint_amendment_ledger.py --all --fix
python .github/scripts/update-CAM-Constitution-Index.py
python .github/scripts/update-CAM-Charters-Index.py
python .github/scripts/update-CAM-Laws-Index.py
python .github/scripts/verify-ledger-sha-coverage.py
python .github/scripts/update-CAM-Governance-Index.py
python .github/scripts/update-CAM-Constitutional-Schedule-Registry.py
python .github/scripts/update-CAM-Global-Operative-Instrument-Registry.py
python .github/scripts/update-CAM-Model-Terminology-Audit.py
python .github/scripts/update-CAM-Governance-Index.py
python .github/scripts/build-canonical-code-index.py
```
Then check:
```
git status --short
```
### 6.6 Section reference validation failure

Likely cause: a §x reference points to a missing local section, a missing cross-document target, or an ambiguous named instrument.

Remedy:
```
python .github/scripts/validate_markdown_section_refs.py --root Governance
```
Review rows with statuses such as:
```
fail_local
fail_cross_document_target_missing
fail_cross_document_section_missing
manual_review_required
ambiguous_named_instrument_reference
```
Use full CAM instrument references where possible.

### 6.7 Symbolic structure lint failure

Likely cause:

missing Canonical Codes metadata row;
unregistered code prefix;
symbolic registry collision;
duplicate symbolic structure;
code listed in metadata but not found in source text.

Remedy:
```
python .github/scripts/build-canonical-code-index.py
python .github/scripts/lint-symbolic-structures.py
```
For release-sensitive checks, use strict mode where applicable.

### 6.8 Archive package failure

Likely cause:

* missing README.md;
* missing CITATION.cff;
* missing generated index/json files;
* archive manifest mismatch.

Remedy:
```
python .github/scripts/package_archive.py
```
This refreshes generated governance views, writes MANIFEST.json, and creates deterministic archive outputs.

## 7. Safety Rules

Scripts belong in .github/scripts/.
Shared helpers belong in .github/scripts/lib/.
Script tests belong in .github/scripts/tests/.
The current canonical-code index belongs in `Governance/CAM.Canonical.Code.Index.{json,md}`. The deprecated symbolic registry is not a source-authority dependency.

Do not mutate doctrinal text outside declared generated blocks unless the script is expressly designed for that purpose.
Do not run archive packaging as part of ordinary doctrine editing.

Always check git status --short before and after manual recovery.

Do not push from a dirty worktree unless the dirty files are intentional and staged.
A clean idempotency rerun is the strongest sign that the pipeline is stable.

## 8. Pre-Commit Checklist

Before committing script or governance-generation changes:
```
git status --short
python -m pytest .github/scripts/tests
python .github/scripts/validate_markdown_section_refs.py --root Governance
python .github/scripts/build-canonical-code-index.py --root Governance
python .github/scripts/lint-symbolic-structures.py --index Governance/CAM.Canonical.Code.Index.json
python .github/scripts/verify-ledger-sha-coverage.py
```
Confirm:

* no unexpected generated files;
* no unsealed latest HASH cells unless intentionally pending;
* no invalid historical HASH cells;
* no stale governance registry outputs;
* no broken local or cross-document section references;
* no canonical declaration, source-owner, parentage, retired-current-use, unknown-family or unknown-value failures.

## 9. Quick Diagnosis Table
| Symptom                     | Likely Script / Area              | First Command                                                                |
| --------------------------- | --------------------------------- | ---------------------------------------------------------------------------- |
| Ledger HASH missing         | `lint_amendment_ledger.py`        | `python .github/scripts/lint_amendment_ledger.py --all --fix`                |
| Ledger coverage mismatch    | `verify-ledger-sha-coverage.py`   | `python .github/scripts/verify-ledger-sha-coverage.py`                       |
| Registry stale              | Index builders / governance index | `python .github/scripts/update-CAM-Governance-Index.py`                      |
| Generated registry stale | registry generators | `python .github/scripts/update-CAM-Constitutional-Schedule-Registry.py && python .github/scripts/update-CAM-Global-Operative-Instrument-Registry.py` |
| Broken § reference          | Section reference validator       | `python .github/scripts/validate_markdown_section_refs.py --root Governance` |
| Shorthand reference remains | Shorthand linter                  | `python .github/scripts/lint_reference_shorthand.py --root Governance`       |
| Symbolic code mismatch      | Symbolic lint/index tools         | `python .github/scripts/lint-symbolic-structures.py`                         |
| Archive package mismatch    | Archive packager                  | `python .github/scripts/package_archive.py`                                  |
| Dirty tree after workflow   | Generator staging/idempotency     | `git status --short`                                                         |

## 10. Maintainer Note

When the pipeline fails, prefer diagnosis before patching.

Most failures fall into one of four categories:
```
source document changed but ledger did not update;
generated indexes are stale;
generated outputs were created but not staged;
references or canonical codes no longer match declared structure.
```
The recovery posture is:
```
observe → classify → regenerate → validate → commit once.
```
