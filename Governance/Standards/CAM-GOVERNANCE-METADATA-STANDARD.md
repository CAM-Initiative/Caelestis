# CAM-GOVERNANCE-METADATA-STANDARD — Governance Metadata Standard

**Instrument Type:** Governance Metadata Standard
**Status:** Active
**Effect:** Interpretive
**Governance Standard:** Registry Standard
**Review State:** Active Metadata Harmonisation
**Authority Role:** Source-authoritative controlled vocabulary for governance metadata fields; no independent doctrinal, runtime, or enforcement authority.
**Purpose:** Defines the minimal controlled metadata vocabulary for lifecycle state, authority type, and governance expectation.

---

## 1. Scope

This standard controls top-level metadata vocabulary for Governance instruments.

The metadata system answers only three questions:

* `Status` — what lifecycle state is the instrument in?
* `Effect` — what type of authority does the instrument exercise?
* `Governance Standard` — what level of governance expectation does the instrument create?

The metadata layer does not encode instrument scope, governance surface, activation conditions, qualification criteria, runtime triggers, risk surfaces, or stakeholder categories. Those concepts remain governed by the source-authoritative instruments that define them.

`Governance Standard` replaces the previous combined use of `Enforcement` and `Applicability Class` introduced during the metadata harmonisation pass. This replacement is a metadata-schema simplification only; it does not alter substantive doctrine, declared scope, activation rules, runtime triggers, qualification pathways, or binding obligations established elsewhere in the corpus.

Architectum qualification remains governed by CAM-EQ2026-STEWARD-003-PLATINUM, including `STW.AQ`, `STW.NAL`, and `STW.AQG`. This metadata field does not determine qualification status and does not classify any real-world entity, company, laboratory, model, cloud provider, institution, or deployment as Architectum-Class.

---

## 2. Status

Allowed values:

* `Draft`
* `Proposed`
* `Adopted`
* `Active`
* `Deprecated`
* `Superseded`
* `Retired`

Interpretation:

* `Draft` — working text; not source-authoritative.
* `Proposed` — reviewable candidate; not binding.
* `Adopted` — accepted into corpus as source-authoritative text, but may require activation context before operational enforcement.
* `Active` — currently operative source-authoritative instrument.
* `Deprecated` — retained for history but discouraged for current use.
* `Superseded` — replaced by later source-authoritative instrument.
* `Retired` — no longer operative except for archival/historical interpretation.

---

## 3. Effect

Allowed values:

* `Interpretive`
* `Operational`
* `Binding`
* `Transitional`
* `Archival`

Interpretation:

* `Interpretive` — guides interpretation, classification, review, repair, ambiguity handling, or audit; does not independently impose execution/enforcement.
* `Operational` — governs runtime, validation, routing, registry, procedural handling, or execution sequencing where activated by applicable instruments.
* `Binding` — imposes mandatory obligations within declared scope.
* `Transitional` — bridges prior and new doctrine during harmonisation or migration.
* `Archival` — retained as record only.

---

## 4. Governance Standard

Allowed values:

* `Not Enforceable`
* `Registry Standard`
* `CAM Standard`
* `CAM Enhanced Standard`
* `Architectum Standard`
* `Archival`

Interpretation:

### 4.1 Not Enforceable

Creates no mandatory obligations.

Used for drafts, exploratory instruments, conceptual research, candidate doctrine, and non-operative materials.

### 4.2 Registry Standard

Applies to metadata, registries, schemas, canonical code systems, classification frameworks, stewardship registries, catalogues, and related governance infrastructure.

### 4.3 CAM Standard

Represents the baseline governance expectation for systems operating within the instrument's declared scope.

Examples include:

* relational protections;
* child-safe safeguards;
* consent protections;
* likeness protections;
* refusal narration integrity;
* proportional runtime governance.

### 4.4 CAM Enhanced Standard

Represents enhanced governance expectations for systems whose capability, scale, dependency footprint, user reliance, societal impact, or governance significance exceeds ordinary deployment expectations but does not yet require Architectum qualification.

Examples may include:

* large-scale companion systems;
* substantial memory-enabled systems;
* high-impact recommender systems;
* major synthetic media platforms;
* large multi-agent environments;
* high-capability deployments below Architectum qualification thresholds.

### 4.5 Architectum Standard

Represents governance obligations intended for systems meeting the Architectum or Architectum-Eligible qualification pathway.

Architectum qualification remains governed by:

* `STW.AQ`
* `STW.NAL`
* `STW.AQG`
* CAM-EQ2026-STEWARD-003-PLATINUM

This metadata field does not determine qualification status. It only indicates that the instrument belongs to the Architectum governance tier.

### 4.6 Archival

Historical or traceability-only material.

---

## 5. Transitional Interpretation

Instruments previously marked `Pre-Enforcement Recognition`, `Immediate Effect`, `Active on Commit`, `Commences 1 July 2026`, or `Pending Adoption` SHALL be interpreted according to the controlled `Status`, `Effect`, and `Governance Standard` model introduced by this harmonisation pass.

Where an instrument is source-authoritative and already consumed by an Active or Binding instrument, it may possess interpretive, operational, or binding authority through that source-authoritative relationship even if the metadata field does not independently create enforcement power.

Binding obligations for Architectum-Eligible, Architectum-Class, frontier-backbone, enhanced, platform-level, or baseline CAM systems SHALL remain binding within their declared scope unless expressly deprecated, superseded, or retired.

`Governance Standard` identifies the level of governance expectation expressed by the instrument. It does not reduce source authority, does not determine qualification status, does not encode activation conditions, and does not convert binding obligations into advisory guidance where the declared risk surface is present.

---

## 6. Amendment Ledger

| Version | Change Summary | Timestamp (UTC) | Reference Hash |
| --- | --- | --- | --- |
| 1.0 | Initial governance metadata standard defining controlled Status, Effect, and Governance Standard vocabulary. | 2026-06-21T14:33:04Z |  |
