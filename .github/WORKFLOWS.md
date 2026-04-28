# CAM Workflow System — Human Readable Guide

## 1. Overview

This repository uses GitHub Actions workflows to keep governance documents consistent and up to date.

At a high level, workflows do three connected jobs:

1. **Build or refresh registry/state outputs** (indexes, derived documents, structured artifacts).
2. **Validate quality and consistency** (linting, structure checks, strict ledger checks).
3. **Seal amendment ledger hashes** so amendment rows are populated and traceable.

These jobs are intentionally ordered. The hash step depends on earlier steps finishing successfully.

- If builders fail, validation and hash steps do not complete.
- If validation fails, hash/commit steps may be blocked.
- If hashing fails, commits should not proceed silently.

---

## 2. Trigger Events

Below is what starts each workflow and where it runs.

### `lint-amendment-ledger.yml`
- **Triggers:** `pull_request`, `push`
- **Branch scope:** push events on `main`; PR events against repo paths
- **Purpose:** pre-merge and post-push quality checks for ledger and symbolic structures.

### `update-ledgers.yml`
- **Triggers:** `push`
- **Branch scope:** `main`
- **Purpose:** auto-seal amendment ledgers after changes land.

### `update-CAM-Laws-Index.yml`
- **Triggers:** `push` with relevant path changes
- **Branch scope:** `main`
- **Purpose:** regenerate laws index artifacts, validate, hash ledgers, and write updates.

### `update-CAM-Constitution-Index.yml`
- **Triggers:** `push` with relevant path changes
- **Branch scope:** `main`
- **Purpose:** regenerate constitution index artifacts, validate, hash ledgers, and write updates.

### `update-CAM-Charters-Index.yml`
- **Triggers:** `push` with relevant path changes
- **Branch scope:** `main`
- **Purpose:** regenerate charters index artifacts, validate, hash ledgers, and write updates.

### `update-CAM-Governance-Index.yml`
- **Triggers:** `push` (governance update flow)
- **Branch scope:** `main`
- **Purpose:** run broader governance artifact refresh (including schedules/symbolic outputs), then validate + hash + write.

### `update-CAM-BS2025-AEON-003-SCH-03.yml`
- **Triggers:** `pull_request`, `workflow_dispatch`
- **Branch scope:** PR paths + manual run
- **Purpose:** determinism check for schedule generation (validation-oriented, no normal write-back step).

---

## 3. Execution Pipeline (Step-by-Step)

Most write workflows follow this pipeline:

1. **Environment setup**  
   Checkout repo and set up runtime tools (for example Python).

2. **Dependency installation**  
   Install basic tooling so scripts run consistently.

3. **Registry / index generation**  
   Run builder scripts that create/update derived governance files.

4. **Validation / lint checks**  
   Verify generated and source content passes required checks.

5. **Ledger hash computation**  
   Run the ledger hash step to populate/seal amendment hash values.

6. **Commit / push (if applicable)**  
   Stage changes, commit only if there are changes, then push.

Important behavior: this is a chain. A failure in any earlier stage blocks later stages.

---

## 4. Ledger Hashing — Explained Simply

The ledger hash step computes/fills amendment ledger hash fields using the repository’s ledger rules.

It runs **after** generation and validation, and **before** final commit/push in write workflows.

Why it might not run:
- An earlier step failed (builder, validation, setup).
- The workflow never triggered.
- The job was skipped by conditions.

What **`files updated: N`** means:
- `N` is the number of files newly changed by the ledger hash step during that run.
- `N = 0` means hash step ran but did not need to modify files.

---

## 5. Failure Modes (Critical Section)

### A) Registry step fails → ledger never runs
- **Symptoms:** workflow stops at generation step; no ledger start/completion logs.
- **How to check:** open failed job logs and find the first non-zero exit in builder steps.

### B) Script path incorrect → script not found
- **Symptoms:** error like “No such file or directory” or cannot open script.
- **How to check:** inspect the exact script path printed in the failing step logs.

### C) Permissions issue → cannot write hashes
- **Symptoms:** commit/push errors, permission denied, or write failure.
- **How to check:** confirm workflow/job permissions include `contents: write` and inspect push logs.

### D) Node/Python version mismatch
- **Symptoms:** action runtime warnings/failures, setup failures, dependency execution errors.
- **How to check:** read setup steps and action version logs for compatibility messages.

### E) No changes detected → no commit
- **Symptoms:** workflow reports “No changes to commit” and exits normally.
- **How to check:** review commit stage logs; this is usually expected, not an error.

---

## 6. How to Debug (Step-by-Step)

1. Open the **Actions** tab in GitHub.
2. Click the failed workflow run.
3. Open the failed job.
4. Identify the first failed step.
5. Read that step’s logs fully.
6. Look specifically for:
   - `Ledger hash step started`
   - `Ledger hash step completed`
   - any `ERROR` messages
7. If hash logs are missing, move upward to find earlier failure.
8. If hash started but failed, fix the script/input issue shown in that log.
9. Re-run workflow after fix.

---

## 7. Observability Signals (NEW)

Ledger hashing now emits explicit operational signals:

- **Start log:** `Ledger hash step started`
- **Completion log:** `Ledger hash step completed (files updated: N)`
- **File-count signal:** `N` shows how many files hash processing changed
- **Explicit failure output:** `ERROR: ...` with non-zero exit behavior

These signals make it easier to separate:
- “hash step never ran” vs
- “hash step ran but failed” vs
- “hash step ran and made no changes”.

---

## 8. Mental Model (Simple Summary)

Think of this system as a single pipeline:

> **Build → Validate → Hash → Write**

If an early stage fails, later stages do not run.  
So if ledger hashes are missing, always check whether the workflow failed earlier in the chain.
