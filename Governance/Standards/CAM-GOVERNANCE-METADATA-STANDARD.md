# CAM-GOVERNANCE-METADATA-STANDARD — Governance Metadata and Source-Authority Standard

**Instrument Type:** Governance Metadata Standard  
**Status:** Active  
**Effect:** Operational  
**Governance Standard:** Registry Standard  
**Review State:** Current  
**Authority Role:** Metadata Authority  
**Source Authority:** Source-Authoritative  
**Purpose:** Defines the controlled metadata and source-authority contract for governed instruments.

---

## 1. Scope

This standard controls the top-level metadata used to determine an instrument's lifecycle position, normative effect, governance tier, review posture, authority function and operative source-authority state. It also defines the representation boundary between amendment-level provenance and the current document-level provenance state.

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

## 12. Amendment-level and document-level provenance

Amendment-level provenance and current document-level provenance are distinct records. An Amendment Ledger records who or what contributed to a particular amendment cycle. A document-level provenance record represents the current evidence concerning authorship, contribution, review, responsibility, authority, technical provenance and rights for the document as a whole.

Neither record may silently populate the other.

### 12.1 Amendment-level provenance

Governed instruments SHALL record drafting and review provenance for each amendment in the Amendment Ledger. A current document-level provenance block MUST NOT be used as a substitute for amendment history.

The canonical headers are:

1. `Version`
2. `Change Summary`
3. `Timestamp (UTC)`
4. `Agent`
5. `Model`
6. `Reviewer`
7. `Reference Hash`

Every amendment row SHALL contain seven cells. `Agent`, `Model`, and `Reviewer` SHALL be non-blank. `Agent` identifies the authoring agent or amendment contributor for that row; it does not establish authorship of the whole document. `Reviewer` records review of that amendment and does not establish authorship, editorial responsibility, adoption authority, publication authority or rights. GitHub approval, automation, CI validation, commit authorship and pull-request activity MUST NOT be represented as independent human or third-party review.

### 12.2 Current document-level provenance state

A governed document MAY declare a current document-level provenance block where authorship, contribution, review, responsibility, authority, technical provenance or rights attribution is material. The block is not an authority source and MUST NOT alter the instrument's six controlled governance metadata fields.

The canonical block uses the following fields:

| Field | Meaning | Requirement when a block is declared |
|---|---|---|
| `Authorship State` | Current evidence-based `AUTH` classification. | Required. |
| `Authoring Parties` | Identified parties to whom the authorship state applies. | Required unless `AUTH.UNDETERMINED`. |
| `Contribution Roles` | Actor-bound `CONTRIB` roles. | Required where material processing or contribution is declared. |
| `AI System / Provider` | Identifies a material AI system and provider without making the provider or model the author. | Optional. |
| `Human Reviewer` | Person or body that performed review. | Optional. |
| `Editorial Responsibility` | Person or body accountable for current editorial decisions. | Optional. |
| `Adoption Authority` | Person or body that adopted the document within the applicable governance process. | Optional. |
| `Publication Authority` | Person or body that authorised publication. | Optional. |
| `Technical Provenance Status` | Current `TPROV` state. | Required where technical provenance is material or asserted. |
| `Provenance Record` | Resolvable record containing the detailed current state and evidence anchors. | Required. |
| `Rights / Copyright` | Rights or copyright holder and applicable licence reference. | Optional and separate from authorship. |

The canonical machine-readable representation is `Governance/Standards/schemas/caelestis-document-provenance-1.0.schema.json`. A block MAY be represented inline or by reference to a conformant record. Omitted optional fields mean “not declared in this block”; they do not mean absent, none or inapplicable.

The following invariants are mandatory:

1. provenance is not authorship;
2. an AI-system processing or contribution role MUST NOT automatically establish AI-system authorship;
3. review, editorial responsibility, adoption authority, publication authority, custody, repository ownership and rights ownership MUST NOT automatically establish authorship;
4. technical provenance or a watermark MUST NOT automatically establish authorship, truth, ownership or authority;
5. absence, removal or failure of technical provenance MUST NOT establish human authorship or absence of AI participation;
6. an amendment author or authoring agent MUST NOT automatically become a whole-document author;
7. every declared party and contribution role MUST remain actor-bound and resolvable in the provenance record; and
8. rights and copyright declarations MUST remain separate from authorship and contribution records.

---

## 13. Constitutional Schedule Registry Contract

The constitutional Schedule registry is a deterministic projection of current operative instruments whose `Instrument Type` is a constitutional Schedule and whose authority chain resolves to the Constitution or a constitutional Annex.

The registry specification formerly contained in `CAM-BS2025-AEON-003-SCH-01` is continued here. Retirement of that Schedule does not retire the registry, its validation function, or its historical identifier.

The registry MUST be reconstructed from governed source instruments and MUST expose, at minimum:

- canonical instrument identifier and title;
- constitutional parent;
- lifecycle status and effect;
- Authority Role and Source Authority;
- constitutional Runtime function;
- activation posture;
- execution, non-execution, arbitration, registry or referral function, where applicable; and
- source path or other resolvable source locator.

Inclusion requires all of the following:

1. the instrument is operative;
2. the instrument uses the `SCH` form within the constitutional namespace;
3. its parent is the Constitution or an operative constitutional Annex;
4. its Schedule authority does not exceed that parent; and
5. its current source metadata passes strict metadata and source-authority validation.

Draft, proposed, retired, superseded, archival and domain instruments MUST NOT appear as current constitutional Schedules. Domain Charters, Appendices, Supplements, Standards and generated indexes may influence or support Runtime governance, but MUST NOT be assigned a constitutional Schedule position.

The registry MUST distinguish constitutional function from execution order. Registry presence does not make an instrument executable, callable, continuously active, or superior to its parent. A Schedule that performs no irreducible constitutional function MUST be decomposed or retired rather than preserved to maintain a registry row.

The registry output is generated evidence. It MUST NOT become the source authority for a Schedule, its function or its metadata. Divergence between the output and governed source instruments is a validation failure and MUST be corrected at the source or generator, as applicable.

Historical references to `CAM-BS2025-AEON-003-SCH-01` remain resolvable as references to the former constitutional registry instrument. New current references SHALL cite this section and the generated Constitution index.

---

## 14. Migration rule

Existing uncontrolled values remain evidence of historical corpus state and MUST be inventoried before correction. Migration MUST:

- preserve substantive doctrine unless a separate finding authorises amendment;
- map only semantically equivalent values automatically;
- route ambiguous values for human review;
- record the old value, new value and reason;
- update generators, parsers, validators and public projections together; and
- avoid treating metadata normalisation as proof that the underlying authority claim is valid.

---

## 15. Amendment Ledger

| Version | Change Summary | Timestamp (UTC) | Agent | Model | Reviewer | Reference Hash |
| --- | --- | --- | --- | --- | --- | --- |
| 1.0 | Initial governance metadata standard defining controlled Status, Effect and Governance Standard vocabulary; added canonical amendment-level provenance architecture. | 2026-08-04T14:26:58Z | Caelen | GPT-5.6 Thinking | Dr M.V. O'Rourke | - |
| 2.1 | Replaced the three-field metadata model with a six-field metadata and source-authority contract; controlled Review State and Authority Role; added Source Authority, combination invariants, conflict rules and migration requirements; clarified delegated subordinate declaration ownership; required resolvable, non-circular parent lineage for derived and applied authority; continued the constitutional Schedule registry contract from retired `CAM-BS2025-AEON-003-SCH-01`; completed S-03/O-03 authority-reference consolidation; and separated amendment-level provenance from a canonical current document-level provenance block and schema without treating metadata as substantive authority. | 2026-08-15T00:00:00Z | Caelen | GPT-5.6 Sol | Dr M.V. O'Rourke |  |
