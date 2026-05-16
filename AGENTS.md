# Agent Instructions for CAM Repository Work

These instructions apply to AI coding agents and automated editing passes working in this repository.

Human maintainers may intentionally depart from these instructions, but agents should follow them unless the user explicitly directs otherwise.

## Amendment Ledger Handling

Governance instruments in `Governance/Constitution/`, and `Governance/Charters/`,  use Amendment Ledgers to record merge-level amendment cycles.

Agents MUST apply the Single Open Ledger Row Rule.

### Single Open Ledger Row Rule

Each instrument may have only one open Amendment Ledger row at a time.

An open row is the latest Amendment Ledger row with a blank SHA-256 cell.

If the latest ledger row is blank and the instrument receives additional edits before merge, agents MUST update that existing open row instead of appending a new row.

Updating the open row may include:

- expanding the description to cover additional changes;
- replacing a narrow description with a consolidated amendment summary;
- updating the timestamp to the latest relevant edit time;
- preserving the same version number;
- leaving the SHA-256 cell blank for the ledger bot to seal.

Agents MUST NOT append a new Amendment Ledger row while the current latest row remains blank.

A new Amendment Ledger row may be appended only when the previous latest row already contains a valid SHA-256 hash.

The Amendment Ledger records the instrument-level amendment prepared for merge. It does not record every intermediate branch commit, Codex pass, formatting edit, validation repair, or drafting revision.

### Open Amendment Cycle Fragmentation

Open Amendment Cycle Fragmentation occurs when an instrument contains more than one unsealed Amendment Ledger row.

If this occurs, agents SHOULD consolidate the unsealed rows into one latest row, preserving the substance of all descriptions, using the latest relevant timestamp, and leaving only the final SHA-256 cell blank.

Agents SHOULD NOT invent, manually fabricate, or guess SHA-256 ledger values.

Use the repository ledger tooling to seal amendment rows.

## Validation

After editing governance instruments, agents SHOULD run the relevant validation commands when available, including:

```bash
python .github/scripts/lint_amendment_ledger.py --base "${BASE_SHA:-HEAD~1}" --head "${HEAD_SHA:-HEAD}" --fix
python .github/scripts/lint_amendment_ledger.py --base "${BASE_SHA:-HEAD~1}" --head "${HEAD_SHA:-HEAD}" --strict
```
