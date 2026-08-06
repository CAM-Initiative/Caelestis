# Pass 4 — Operative Authority Assignment Register

## Purpose

This register defines the proposed hierarchy-derived metadata assignments for operative instruments other than the four constitutional-adjacent Laws. It is a review record, not an automatic amendment instruction.

The four Laws are excluded pending a dedicated SHA-aware migration because their content hashes are consumed by the Law manifest and integrity controls.

## Assignment classes

| Instrument class | Proposed Review State | Proposed Authority Role | Proposed Source Authority | Required confirmation |
|---|---|---|---|---|
| Root constitutional instrument | `Current` unless a bounded review is active | `Constitutional Authority` | `Source-Authoritative` | Confirm the bounded constitutional subject and conflict rule |
| Constitutional schedule | `Current` unless a bounded review is active | `Constitutional Schedule Authority` | `Derived Authority` | Confirm the parent instrument and that the schedule does not exceed it |
| Root domain charter | `Current` unless a bounded review is active | `Domain Authority` | `Source-Authoritative` | Confirm the domain owned by the charter |
| Binding domain appendix | `Current` unless a bounded review is active | `Supplementary Authority` | `Derived Authority` | Confirm the parent and remove any competing source-authority claim |
| Operational supplement | `Current` unless a bounded review is active | `Operational Authority` | `Derived Authority` | Confirm the parent delegation and procedural boundary |
| Interpretive supplement | `Current` unless a bounded review is active | `Interpretive Authority` or `Supplementary Authority` | `Derived Authority` or `Applied Authority` | Confirm that it interprets rather than executes or redefines |
| Metadata or registry instrument | `Current` | `Metadata Authority` or `Registry Authority` | `Source-Authoritative` | Identify the exact vocabulary, schema or projection owned |
| Proposed instrument in an operative namespace | `Review Required` | `No Independent Authority` | `Non-Operative Draft` | Move to `Governance/Drafts/**` or complete formal adoption before migration |

## Review-state mappings

The following presentation mappings are safe because they do not alter substantive authority:

- `None` → `Current`;
- `Formal Review Completed — Pre-Enforcement Alignment` → `Current`;
- `Developmental Review` → `Under Review`;
- named active alignment reviews → `Under Review`;
- missing review state → `Review Required` unless the instrument's current status and review record establish `Current`.

Project names, dates and review descriptions belong in review records or amendment ledgers, not in the controlled `Review State` field.

## Authority values that must not be mechanically preserved

The following observed values are free-text claims and require conversion to the controlled class supported by hierarchy:

- `None`;
- `Transitional` when used as an authority role;
- `Binding Authority`;
- `Constitutional Spine`;
- `Domain Source Authority` and extended variants;
- `Reference-Only`;
- prose descriptions beginning with `Source-authoritative`, `Binding constitutional`, or similar claims;
- runtime, telemetry or symbolic-role descriptions embedded directly in `Authority Role`.

Their descriptive content may be retained in scope prose, but not in the controlled field.

## Source-authority rule

- A root owner of a bounded constitutional subject, governance domain, controlled vocabulary or registry may be `Source-Authoritative`.
- A schedule, appendix or supplement is presumptively `Derived Authority` unless it merely applies doctrine without elaboration, in which case `Applied Authority` may be appropriate.
- Child instruments must identify their parent and must not claim independent supremacy.
- Circular derivation and competing source-authoritative claims remain blocked for instrument-level adjudication.

## Migration constraint

No bulk operative migration should be committed until each proposed root owner and parent-child relationship has been checked against the Pass 2 source-authority map. The migration must add an amendment-ledger row and reseal each governed instrument through the existing deterministic workflow.
