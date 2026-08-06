# Pass 4 — Metadata and Source-Authority Migration Plan

## Governing rule

Only semantically exact mappings may be automated. Authority ownership, constitutional priority, source-authoritative scope and cross-domain precedence require instrument-level review.

Metadata normalisation MUST NOT be used to validate an otherwise unsupported authority claim.

## Migration classes

### Class A — deterministic field additions

These changes are safe where the instrument's existing lifecycle and namespace are unambiguous:

- add `Review State: Current` where the existing value is `None` and no open review is recorded;
- add `Review State: Under Review` to the five current drafts;
- add `Authority Role: No Independent Authority` to the five drafts;
- add `Source Authority: Non-Operative Draft` to the five drafts;
- replace `Review State: Developmental Review` in drafts with `Under Review`;
- replace `Reference-Only` with `No Independent Authority` where the instrument is explicitly a reference catalogue and creates no rule.

Class A mappings require a generated before-and-after register and amendment-ledger entry where the file is governed.

### Class B — hierarchy-derived candidates

These mappings may be proposed mechanically but require review before commit:

- root Constitution instrument → candidate `Constitutional Authority`;
- Constitution schedule → candidate `Constitutional Schedule Authority` and `Derived Authority`;
- root domain Charter → candidate `Domain Authority` and `Source-Authoritative` for its bounded domain;
- appendix or supplement → candidate `Supplementary Authority`, `Operational Authority`, `Interpretive Authority`, or `Applied Authority` depending on function;
- registry or metadata standard → candidate `Metadata Authority` or `Registry Authority`;
- operational procedure → candidate `Operational Authority` and `Derived Authority` or `Applied Authority`.

Filename hierarchy alone is insufficient. Each candidate must be checked against the parent declaration and actual content.

### Class C — authority adjudication required

The following values cannot be safely mapped without substantive review:

- `Constitutional Spine`;
- `Binding Authority`;
- `Annex-Level, Substrate-Binding`;
- `Transitional` used as Authority Role;
- `Domain Source Authority — ...`;
- long source-authority or execution-scope sentences;
- any claim of corpus-wide supremacy;
- any source-authoritative claim shared by multiple instruments;
- any circular derivation, including the SECURITY-001 and Annex K relationship.

Class C records must be resolved through the Pass 2 source-authority map and the Pass 3 disposition decisions.

### Class D — lifecycle disposition required

The following require an explicit lifecycle decision rather than metadata substitution:

- the Proposed instrument remaining in an operative namespace;
- Laws using `Canonical — Inviolable Constraint` as Status;
- any instrument whose actual adoption or activation state cannot be established from the ledger and hierarchy;
- deprecated, superseded or retired instruments that remain in operative indexes;
- instruments whose title, seal or directory conflicts with lifecycle state.

## Law migration

The four Laws require a dedicated constitutional mapping. Recommended candidate metadata is:

- `Status: Active`
- `Effect: Binding`
- `Governance Standard: CAM Standard`
- `Review State: Current`
- `Authority Role: Constitutional Authority`
- `Source Authority: Source-Authoritative`

This candidate does not by itself establish that every Law is legally or philosophically "inviolable". Their priority must be grounded in the Aeon Tier hierarchy and explicit conflict rules. The term `Inviolable Constraint` may remain descriptive doctrine only if the Constitution supports it.

## Review-state migration

| Existing value | Proposed controlled value | Treatment |
|---|---|---|
| `None` | `Current` | deterministic only where no review is open |
| blank | `Review Required` or `Current` | inspect instrument state |
| `Developmental Review` | `Under Review` | drafts only |
| `MENTIS Domain Alignment Review` | `Under Review` | preserve workstream in prose or review record |
| `Active Runtime Alignment Review` | `Under Review` | preserve workstream in prose or review record |
| `Formal Review Completed — Pre-Enforcement Alignment` | `Verification Required` or `Current` | inspect whether implementation remains outstanding |
| `Draft` | invalid | use Status for lifecycle; assign controlled review state separately |

## Authority-role migration

| Existing pattern | Candidate controlled value | Treatment |
|---|---|---|
| `None` | depends on hierarchy and function | no bulk default for operative instruments |
| `Transitional` | move to Effect if accurate | authority role still requires adjudication |
| `Domain Source Authority ...` | `Domain Authority` | source scope moves to `Source Authority` and prose |
| `Reference-Only` | `No Independent Authority` | deterministic if no rule is created |
| operational appendix sentence | `Operational Authority` | verify parent delegation |
| source-authoritative classification sentence | `Interpretive Authority` or `Registry Authority` | verify canonical ownership |
| constitutional runtime schedule sentence | `Constitutional Schedule Authority` | verify parent and no overreach |

## Source-authority migration

Every instrument must receive one of:

- `Source-Authoritative`
- `Derived Authority`
- `Applied Authority`
- `Informative Only`
- `Non-Operative Draft`
- `Historical Only`

For `Derived Authority` and `Applied Authority`, the migration must also ensure the parent or source instrument is identified in existing metadata or top-level prose.

## Enforcement sequence

1. Migrate the five drafts and add strict draft metadata validation.
2. Resolve the four Laws.
3. Resolve the metadata standard and registry/validator instruments.
4. Resolve root Constitution instruments.
5. Resolve Constitution schedules.
6. Resolve root domain Charters.
7. Resolve appendices and supplements by functional class.
8. Resolve known source-authority conflicts and circular dependencies.
9. Regenerate all indexes and public projections.
10. Enable `--strict` metadata-authority validation in CI only after the exception register reaches zero.

## Required evidence for closure

Pass 4 closes only when:

- every governed instrument has all six fields;
- all values are controlled;
- every binding instrument has an authority chain;
- no draft or proposal is represented as operative;
- no child claims authority exceeding its parent;
- all derived/applied instruments identify their source;
- Laws use controlled lifecycle metadata;
- the deterministic audit reports zero exceptions; and
- governance rebuild and idempotency checks pass.
