# Pass 4 — Zero-Current-Use Exception Register

**Date:** 2026-08-07  
**Branch:** `agent/corpus-industry-standards-normalisation`  
**Normative effect:** None. This register records the Category A completion
state; it does not create a new technical taxonomy or reopen the canonical
architecture.

## Verification boundary

The zero-use result applies to mutable, operative Caelestis source and emitted
Governance artefacts: `Governance/**/*.md`, `json`, `yaml`, and `yml`, excluding
`Governance/Drafts/**`, the four SHA-sensitive Laws, and historical text after
an instrument's Amendment Ledger heading. The checked current corpus includes
the generated Constitution, Charter, global-Governance, and canonical-code
outputs.

Verification command:

```bash
python .github/scripts/validate_canonical_architecture_terminology.py
```

The validator has zero findings at this completion point. It fails on the
unambiguous retired names below in current governed source or generated output;
it does not use a regex to adjudicate ambiguous uses of `model`, `system`,
`agent`, `Runtime`, or `formation`.

## Zero-current-use register

| Retired family | Current mutable operative use | Permitted exception | Enforcement |
| --- | --- | --- | --- |
| `AEON.CCS`; `Cognitive Cycle Stage`; known `AEON.CC` cognitive aliases | **0** | Historical amendment-ledger and migration/disposition wording only | Corpus-wide retired-terminology guard, including aliases and readable class label |
| Responding Intelligence / Component / Formation; bare `RI` as the prior entity label | **0** | Historical amendment-ledger and migration/disposition wording only | Corpus-wide retired-terminology guard |
| Cognitive-system / cognitive-formation system taxonomy; composed-system, agentic-harness, governance-stack, and runtime-formation taxonomy | **0** | Historical amendment-ledger and migration/disposition wording only | Corpus-wide retired-terminology guard |
| Dyadic, triadic, polyadic; `RLN.R0`–`RLN.R4`; relational geometry; R-Scale | **0** | Historical amendment-ledger and migration/disposition wording only | Corpus-wide retired-terminology guard |
| Instrumenta, Collectiva, Cognitiva | **0** | Historical amendment-ledger and migration/disposition wording only | Corpus-wide retired-terminology guard |

## Out-of-scope locations

These locations are explicitly not evidence of current mutable use in this
Category A completion state:

| Location | Reason | Disposition |
| --- | --- | --- |
| `Governance/Drafts/**` | Non-operative development material | Not migrated in this batch; it cannot be emitted through operative registries. |
| `Governance/Laws/**` | Four SHA-sensitive Laws | No change in this batch. Their separate migration remains required before making any all-repository zero-use claim. |
| Amendment-ledger history | Immutable provenance of prior wording and decisions | Preserved verbatim; validators exclude only text after the ledger heading. |
| `.github/Reviews/**` and validator tests | Review evidence and regression controls may name retired terms in order to record and prevent them | Non-operative; not emitted by Governance indexes or canonical-code outputs. |

## Remaining limitations

This is a zero-current-use result for the unambiguous Category A terminology
families above. It does not resolve Category B terminology decisions, alter
CAM-defined extensions, or substitute a mechanical test for passage-level
standards-alignment review.
