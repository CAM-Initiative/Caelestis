# Agent Instructions for CAM Repository Work

These instructions apply to AI coding agents and automated editing passes working in this repository.

Human maintainers may intentionally depart from these instructions, but agents should follow them unless the user explicitly directs otherwise.

## Governance Corpus Locality and Source-Authority Discipline

CAELESTIS is a mature, cross-domain governance corpus. Agents MUST NOT assume that a newly identified governance problem admits a simple, local, or single-instrument amendment.

Before drafting, inserting, relocating, or recommending substantive governance language, agents MUST perform an instrument-placement review.

The review MUST:

* identify the underlying failure mechanism rather than relying only on the topic or wording used in the request;
* classify the proposed requirement as constitutional, doctrinal, operational, runtime, evidentiary, classificatory, procedural, enforcement, registry, or interpretive;
* identify the source-authoritative instrument for that function;
* inspect the parent instrument, applicable schedules, supplements, appendices, registries, and named cross-domain interfaces;
* search for existing clauses governing the same or adjacent mechanism;
* determine whether the parent instrument delegates operational authority to a child schedule or domain instrument;
* distinguish a genuine doctrinal gap from an implementation, discoverability, enforcement, or cross-reference gap;
* prefer amendment of the narrowest source-authoritative instrument capable of resolving the issue;
* avoid creating duplicate, parallel, or competing authority;
* assess whether a cross-reference is genuinely necessary rather than adding one by default.

Agents MUST NOT place a clause in an instrument solely because:

* the user referred to that instrument by name;
* the topic appears conceptually related to that instrument;
* the instrument is constitutionally senior;
* the clause would read coherently in that location;
* the relevant child schedule or domain instrument has not yet been inspected;
* or the proposed wording appears to provide a convenient immediate fix.

Substantively reasonable wording placed in the wrong instrument constitutes a corpus-integrity risk. It may create duplicate authority, conflicting activation conditions, inappropriate enforcement posture, source-authority ambiguity, registry drift, or future migration debt.

Where source-authority or placement remains uncertain, agents MUST:

* state the uncertainty;
* identify the instruments inspected;
* identify the unresolved candidate instruments;
* refrain from presenting insertion guidance as authoritative;
* and avoid editing the corpus until locality has been adequately resolved.

### No Simple-Fix Presumption

The default posture for substantive CAELESTIS amendments is that the corpus may already contain relevant doctrine, delegation, classification, or enforcement machinery elsewhere.

Agents MUST therefore presume that:

* apparent gaps may be locality or discoverability problems rather than absent doctrine;
* parent instruments may delegate the relevant function;
* cross-domain consequences may arise from even narrowly worded amendments;
* generated indexes, registries, metadata, amendment ledgers, and validation artefacts may require coordinated updates;
* and a locally correct amendment may still be globally inconsistent.

No substantive amendment should be described as “surgical” until the placement review and adjacent-authority check have been completed.

### Required Placement Summary

Before proposing final insertion wording, agents SHOULD provide or internally establish:

* **Failure mechanism**
* **Governance layer**
* **Source-authoritative instrument**
* **Existing adjacent clauses**
* **Proposed insertion location**
* **Why neighbouring instruments are not the correct authority**
* **Duplicate-authority risk**
* **Required consequential updates**

This requirement applies to new clauses, substantive rewrites, instrument migration, consolidation, deletion, and recommendations concerning corpus architecture.

## Repository-State Verification

Before identifying a working branch as authoritative or recommending merge, closure, deletion, reset, overwrite, or branch disposal, agents MUST verify the complete relevant repository-state set.

Agents MUST NOT infer complete branch coverage from:

* pull-request history;
* a partial connector response;
* an empty branch-search result;
* a local checkout containing only fetched refs;
* visible timestamps;
* branch naming;
* or the fact that one branch is ahead of `main`.

Where complete branch or ref enumeration is unavailable, failed, partial, stale, permission-limited, or otherwise uncertain, agents MUST disclose that limitation and MUST NOT provide destructive branch-management advice.

No branch may be described as safe to delete until its unique commits and substantive changes have been verified as absent, merged, or deliberately transferred.

## Amendment Ledger Handling

Governance instruments in `Governance/Constitution/`, and `Governance/Charters/`,  use Amendment Ledgers to record merge-level amendment cycles.

The canonical ledger header is exactly:

```text
| Version | Change Summary | Timestamp (UTC) | Agent | Model | Reviewer | Reference Hash |
```

Every row MUST contain all seven cells. `Agent`, `Model`, and `Reviewer` MUST be non-blank. Historical migrated rows use `Caelen`, `GPT-5 Series`, and `Dr M.V. O'Rourke`; future rows record the exact model designation when known. Static document-level Authorship & Stewardship and Review & Validation blocks are not used as amendment provenance.

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
- leaving the `Reference Hash` cell blank for the ledger bot to seal.

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
