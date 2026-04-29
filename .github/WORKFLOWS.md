# CAM Governance Automation — Deterministic Rebuild Guide

## Overview

The repository now uses a **single canonical writer workflow** to avoid race conditions and overlapping writes:

- **Canonical workflow:** `.github/workflows/governance-rebuild.yml`
- **Manual emergency workflow:** `.github/workflows/refresh-ledger-hashes.yml`
- Legacy workflows remain in place but are **manual-only** and no longer auto-write on push.

This design enforces one ordered pipeline and one commit point.

---

## Canonical Pipeline (`governance-rebuild.yml`)

### Trigger
- `push` to `main` when files change under:
  - `Governance/Constitution/**`
  - `Governance/Charters/**`
  - `Governance/Laws/**`
  - `.github/scripts/**`
- `workflow_dispatch`

### Execution Order

1. Rebuild folder-level Constitution index + JSON.
2. Rebuild folder-level Charters index + JSON.
3. Rebuild folder-level Laws index + JSON.
4. Populate latest amendment-ledger SHA values (`--fix`).
5. Run strict amendment-ledger validation.
6. Rebuild Constitution, Charters, and Laws indexes/JSON again (to carry latest hashes into JSON).
7. Verify ledger SHA coverage and JSON consistency:
   - latest row SHA is non-empty (for docs with amendment ledgers)
   - folder JSON `HASH` is non-empty
   - folder JSON `HASH` equals document latest ledger SHA
   - `SCH-01` and `SCH-03` are excluded from SHA-ledger requirements
8. Build global Governance registry.
9. Mutate SCH-01 and SCH-03 from validated registry state.
10. Build global Governance registry again.
11. Final strict ledger validation.
12. Run symbolic/index lint.
13. Commit once.

---

## Manual Emergency Workflow (`refresh-ledger-hashes.yml`)

Use this when latest-row amendment hashes are missing or placeholder values exist.

### What it does
1. Runs ledger hash fill/strict validation across Constitution, Charters, and Laws.
2. Rebuilds folder-level indexes/JSON.
3. Verifies folder JSON hash consistency.
4. Rebuilds global Governance registry.
5. Commits once.

### What it does NOT do
- Does not rewrite historical rows.
- Does not change hash semantics.
- Does not require SCH-01 or SCH-03 amendment ledgers.

---

## Script Responsibilities

### Folder builders
- `.github/scripts/update-CAM-Constitution-Index.py`
- `.github/scripts/update-CAM-Charters-Index.py`
- `.github/scripts/update-CAM-Laws-Index.py`

Each updates its own folder index + JSON.

### Ledger hash and validation
- `.github/scripts/lint_amendment_ledger.py`
  - scope includes Constitution and Charters (Laws are manifest-validated)
  - fix mode only fills latest-row missing/placeholder/mismatch states under existing semantics
  - explicit exclusions apply only to derived registries SCH-01 and SCH-03; SCH-02 remains ledger-enforced

### SHA coverage verification
- `.github/scripts/verify-ledger-sha-coverage.py`
  - ensures ledger SHA completeness + JSON SHA matching
  - fails loudly with file and instrument context

---

## Legacy Workflows

Legacy auto-writer workflows were removed to keep the repository lean and avoid accidental multi-writer drift.

---

## Troubleshooting Guide

### 1) Ledger strict validation fails
**Symptoms**
- strict step exits non-zero
- logs show amendment ledger errors

**Likely causes**
- latest ledger row SHA still blank/placeholder
- malformed amendment ledger table

**Actions**
1. Run manual `refresh-ledger-hashes.yml`.
2. Inspect files reported in failure logs.
3. Confirm the latest amendment row has a valid SHA.

---

### 2) SHA coverage verifier fails (`verify-ledger-sha-coverage.py`)
**Symptoms**
- errors like JSON HASH blank/mismatch or missing instrument

**Likely causes**
- folder JSON stale relative to amended markdown
- instrument ID mismatch between markdown and JSON
- unexpected exclusion behavior

**Actions**
1. Re-run folder builders in order (Constitution → Charters → Laws).
2. Re-run ledger fix and strict.
3. Re-run folder builders again.
4. Re-run SHA coverage verifier.

---

### 3) Global Governance registry looks stale
**Symptoms**
- CAM governance registry missing updated hash/status/version data

**Likely causes**
- folder-level JSON not refreshed after ledger fix
- global build run too early

**Actions**
1. Confirm pipeline order was followed.
2. Re-run canonical workflow end-to-end.

---

### 4) No commit produced
**Symptoms**
- workflow exits with “No changes to commit.”

**Meaning**
- no generated outputs changed; this is expected when repo is already consistent.

---

### 5) Push/rebase conflict in commit step
**Symptoms**
- rebase/push fails during final commit

**Likely causes**
- concurrent pushes to `main`

**Actions**
1. Re-run canonical workflow.
2. Avoid parallel manual pushes while rebuild is running.

---

## Recommended Operational Runbook

1. **Normal operation:** rely on `governance-rebuild.yml`.
2. **If hashes are missing:** run `refresh-ledger-hashes.yml` once.
3. **If failures persist:** inspect first failed step, fix root cause, re-run canonical workflow.

This keeps the system deterministic: **one ordered pipeline, one writer, one commit**.
