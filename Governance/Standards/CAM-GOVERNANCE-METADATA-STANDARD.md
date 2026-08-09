# CAM-GOVERNANCE-METADATA-STANDARD — Governance Metadata and Source-Authority Standard

**Instrument Type:** Governance Metadata Standard  
**Status:** Active  
**Effect:** Operational  
**Governance Standard:** Registry Standard  
**Review State:** Current  
**Authority Role:** Metadata Authority  
**Source Authority:** Source-Authoritative  
**Purpose:** Defines the controlled metadata and source-authority contract for governed Caelestis instruments.

---

## 1. Scope

This standard controls the top-level metadata used to determine an instrument's lifecycle position, normative effect, governance tier, review posture, authority function and operative source-authority state.

Metadata describes authority. It does not create authority that the instrument does not otherwise possess through the constitutional hierarchy, its parent instrument and its declared scope.

An instrument MUST NOT:

- declare authority exceeding its parent or constitutional source;
- use metadata to convert a draft, proposal or archival record into operative doctrine;
- use a governance tier as evidence of external certification, regulatory compliance or independent assurance;
- combine lifecycle, effect, review and authority concepts in one free-text field; or
- redefine controlled metadata values locally.

---

## 2. Required controlled fields

Every governed instrument in the operative Constitution, Charter, Law and Standards namespaces MUST declare:

1. `Status`
2. `Effect`
3. `Governance Standard`
4. `Review State`
5. `Authority Role`
6. `Source Authority`

Draft instruments MUST declare the same six fields, but are always non-operative and are excluded from operative registries.

---

## 3. Status — lifecycle state

Allowed values:

- `Draft`
- `Proposed`
- `Adopted`
- `Active`
- `Deprecated`
- `Superseded`
- `Retired`

Interpretation:

- `Draft` — developmental working text; not source-authoritative and not operative.
- `Proposed` — reviewable candidate; not adopted and not operative.
- `Adopted` — accepted into the corpus and source-authoritative within declared scope, but not necessarily activated for continuous operation.
- `Active` — currently operative source-authoritative instrument.
- `Deprecated` — still resolvable but prohibited for new classifications, designs or assertions unless expressly authorised for migration.
- `Superseded` — replaced by an identified later instrument; retained only for historical interpretation.
- `Retired` — no longer operative and not a current source of doctrine.

`Status` MUST NOT encode urgency, enforcement intensity, review activity, commencement wording or conformance level.

---

## 4. Effect — normative function

Allowed values:

- `Interpretive`
- `Operational`
- `Binding`
- `Transitional`
- `Archival`

Interpretation:

- `Interpretive` — controls meaning, classification, ambiguity resolution, audit or review; does not independently authorise execution.
- `Operational` — controls procedures, validation, routing, registries, runtime sequencing or implementation mechanics within authority granted elsewhere.
- `Binding` — imposes mandatory obligations within declared scope.
- `Transitional` — temporarily controls migration between identified prior and successor states.
- `Archival` — retained solely as evidence or historical record.

`Effect` MUST NOT encode lifecycle state, governance tier, source-authority position or review posture.

---

## 5. Governance Standard — internal governance tier

Allowed values:

- `Not Enforceable`
- `Registry Standard`
- `CAM Standard`
- `CAM Enhanced Standard`
- `Architectum Standard`
- `Archival`

These are internal Caelestis governance tiers. They are not certifications, legal conclusions, regulatory approvals, conformity assessments or representations of compliance with ISO, IEC, IEEE, NIST, EU, national or sectoral requirements.

- `Not Enforceable` — creates no mandatory obligation.
- `Registry Standard` — governs metadata, schemas, controlled vocabularies, registries, validation and related governance infrastructure.
- `CAM Standard` — baseline internal governance expectation within declared scope.
- `CAM Enhanced Standard` — heightened internal governance expectation for elevated capability, dependency, scale, impact or reliance.
- `Architectum Standard` — internal tier for systems qualifying under the source-authoritative Architectum pathway.
- `Archival` — historical or traceability-only material.

A governance tier MUST NOT determine whether a real-world system qualifies for that tier. Qualification remains controlled by its source-authoritative instrument and required evidence.

---

## 6. Review State — current review posture

Allowed values:

- `Current`
- `Review Required`
- `Under Review`
- `Verification Required`
- `Migration Review`
- `No Further Review Scheduled`
- `Historical Record`

Interpretation:

- `Current` — no unresolved review action is recorded.
- `Review Required` — a defined review is required but has not commenced.
- `Under Review` — a bounded review is active.
- `Verification Required` — implementation or evidence verification remains outstanding.
- `Migration Review` — retained temporarily while a controlled migration is completed.
- `No Further Review Scheduled` — operative review activity is closed without implying immutability.
- `Historical Record` — review posture applies only to archived, superseded or retired material.

`Review State` MUST NOT be used as a substitute for Status or Effect.

---

## 7. Authority Role — function within the hierarchy

Allowed values:

- `Constitutional Authority`
- `Constitutional Schedule Authority`
- `Domain Authority`
- `Supplementary Authority`
- `Operational Authority`
- `Metadata Authority`
- `Registry Authority`
- `Interpretive Authority`
- `Assurance Authority`
- `No Independent Authority`

Interpretation:

- `Constitutional Authority` — establishes constitutional principles and conflict rules.
- `Constitutional Schedule Authority` — operationalises a defined constitutional parent without exceeding it.
- `Domain Authority` — owns doctrine for a declared governance domain.
- `Supplementary Authority` — supplements an identified parent and cannot exceed or contradict it.
- `Operational Authority` — owns procedures, execution sequencing or runtime controls authorised by a parent.
- `Metadata Authority` — owns controlled metadata vocabulary and combination rules.
- `Registry Authority` — owns registry structures, identifiers or canonical projections.
- `Interpretive Authority` — owns bounded interpretation or classification without independent execution power.
- `Assurance Authority` — owns an internal evidence, verification or conformance method; does not imply independent certification.
- `No Independent Authority` — provides guidance, evidence or context only.

Free-text authority descriptions are prohibited in the controlled field. Scope qualifications belong in prose and source-authority declarations.

---

## 8. Source Authority — operative authority state

Allowed values:

- `Source-Authoritative`
- `Derived Authority`
- `Applied Authority`
- `Informative Only`
- `Non-Operative Draft`
- `Historical Only`

Interpretation:

- `Source-Authoritative` — canonical owner of the doctrine, definition, controlled vocabulary or procedure within declared scope.
- `Derived Authority` — derives authority from an identified parent and may elaborate only within that delegation.
- `Applied Authority` — applies source-authoritative doctrine to a bounded operational or domain context without redefining it.
- `Informative Only` — provides explanation, examples or context and creates no authority.
- `Non-Operative Draft` — developmental text excluded from operative authority and registries.
- `Historical Only` — retained solely to interpret prior versions or decisions.

Each `Derived Authority` or `Applied Authority` instrument MUST identify its source instrument or parent. Circular derivation is prohibited.

A derived instrument MAY be the canonical declaration location for a subordinate code family, reference set, schema or procedure only where that ownership is expressly within the parent delegation. Such bounded declaration ownership does not convert the instrument-level `Source Authority` from `Derived Authority` to `Source-Authoritative` or permit the child to exceed its parent.

---

## 9. Valid combination rules

The following invariants are mandatory:

1. `Draft` or `Proposed` requires `Not Enforceable`, `Non-Operative Draft`, and `No Independent Authority` unless a proposal is explicitly classified as informative only.
2. `Active` or `Adopted` MUST NOT use `Non-Operative Draft` or `Historical Only`.
3. `Deprecated`, `Superseded` or `Retired` MUST NOT be `Active` in any generated registry.
4. `Superseded` or `Retired` requires `Archival` effect or a documented transitional exception.
5. `Archival` effect requires `Archival` governance standard and `Historical Only` source authority.
6. `Binding` effect requires `Adopted` or `Active` status and a source-authority state other than `Informative Only`.
7. `Registry Standard` requires `Metadata Authority`, `Registry Authority`, `Operational Authority` or `Assurance Authority`.
8. `No Independent Authority` MUST NOT be paired with `Source-Authoritative`.
9. `Source-Authoritative` MUST identify a bounded concept, domain, vocabulary or procedure owned by the instrument; it does not confer hierarchy-wide supremacy.
10. A child, appendix, supplement or schedule MUST NOT claim authority exceeding its parent.
11. A domain instrument MUST NOT declare constitutional supremacy or unilaterally override another domain.
12. Review wording such as `Active Metadata Harmonisation`, `Developmental Review`, `Pending Review`, dates or prose sentences is invalid in `Review State`.
13. `Derived Authority` and `Applied Authority` require an explicit, resolvable `Parent Instrument` in top-level metadata.
14. A declared parent MUST identify an operative governed instrument, MUST NOT identify the child itself, and MUST NOT create a circular authority chain.
15. `Constitutional Schedule Authority` requires a constitutional instrument and an explicit constitutional parent.
16. `Domain Authority` is reserved for a bounded root domain instrument and MUST NOT be used by a constitutional schedule, appendix, supplement, profile or standard.
17. `Informative Only` requires `No Independent Authority` and MUST NOT be paired with `Binding` effect.

Exceptions require an explicit transition record, expiry condition and amendment-ledger entry.

---

## 10. Source-authority conflict rules

Where multiple instruments address the same concept:

1. the designated source-authoritative instrument owns the definition or rule;
2. derived and applied instruments MUST cross-reference rather than redefine;
3. later text does not silently supersede earlier source authority;
4. conflicts MUST be resolved through an explicit amendment, deprecation or supersession decision;
5. circular source-authority declarations are invalid; and
6. an instrument's statement that it is binding, constitutional, source-authoritative or supreme is ineffective unless supported by the corpus hierarchy and metadata contract.

---

## 11. Adoption, activation, deprecation and retirement

- Adoption requires an amendment-ledger entry and valid controlled metadata.
- Activation requires the activation conditions defined by the applicable source instrument; metadata alone does not activate runtime duties.
- Deprecation requires a migration destination or a statement that no replacement exists.
- Supersession requires identification of the successor instrument.
- Retirement removes the instrument from current operative registries while preserving historical resolution.
- Draft promotion requires movement from `Governance/Drafts/**` into the appropriate operative namespace and replacement of draft metadata through reviewed amendment.

---

## 12. Amendment-level provenance

Governed instruments SHALL record drafting and review provenance in each Amendment Ledger row rather than static document-level authorship or review blocks.

The canonical headers are:

1. `Version`
2. `Change Summary`
3. `Timestamp (UTC)`
4. `Agent`
5. `Model`
6. `Reviewer`
7. `Reference Hash`

Every amendment row SHALL contain seven cells. `Agent`, `Model`, and `Reviewer` SHALL be non-blank. GitHub approval, automation, CI validation, commit authorship and pull-request activity MUST NOT be represented as independent human or third-party review.

---

## 13. Migration rule

Existing uncontrolled values remain evidence of historical corpus state and MUST be inventoried before correction. Migration MUST:

- preserve substantive doctrine unless a separate finding authorises amendment;
- map only semantically equivalent values automatically;
- route ambiguous values for human review;
- record the old value, new value and reason;
- update generators, parsers, validators and public projections together; and
- avoid treating metadata normalisation as proof that the underlying authority claim is valid.

---

## 14. Amendment Ledger

| Version | Change Summary | Timestamp (UTC) | Agent | Model | Reviewer | Reference Hash |
| --- | --- | --- | --- | --- | --- | --- |
| 1.0 | Initial governance metadata standard defining controlled Status, Effect and Governance Standard vocabulary; added canonical amendment-level provenance architecture. | 2026-08-04T14:26:58Z | Caelen | GPT-5.6 Thinking | Dr M.V. O'Rourke |  |
| 2.0 | Replaced the three-field metadata model with a six-field metadata and source-authority contract; controlled Review State and Authority Role; added Source Authority, combination invariants, conflict rules and migration requirements; clarified delegated subordinate declaration ownership; and required resolvable, non-circular parent lineage for derived and applied authority. | 2026-08-09T01:25:00Z | Caelen | GPT-5.6 Sol | Dr M.V. O'Rourke |  |
