# CAM-EQ2026-OPERATIONS-001-SUP-04 — Taxonomies & Metadata Authority Framework (Supplement 4)

**Instrument Type:** Supplement  
**Parent Instrument:** CAM-EQ2026-OPERATIONS-001-PLATINUM — Governance Operations Charter  
**Status:** Adopted  
**Effect:** Pre-Enforcement Recognition  
**Enforcement:** Commences 1 July 2026  
**Review State:** None  
**Authority Role:** None  
**Purpose:** To establish the corpus-level primitive registry and metadata authority framework for distinguishing Structural, Semantic, Operational, and Symbolic taxonomy types; governing subtype, modifier, code-family, controlled-value, schema-field, metadata-field, symbolic-marker, and source-instrument distinctions; and supporting validators, scripts, Codex, AI-assisted editors, registries, and expansion sets in determining whether a proposed classification element is a new primitive, an extension of an existing primitive, a scoped code family, a controlled value, a schema field, or a modifier.

---

## 1. Scope

This Supplement establishes a lightweight framework for identifying what kind of classification system is being created, named, used, consumed, emitted, routed, measured, exposed, or related.

This Supplement is concerned with naming architecture, taxonomy architecture, code-family distinction, controlled-value construction, schema distinction, metadata interpretation, and cross-domain classification integrity.

 This Supplement MAY be applied where taxonomies, metadata, controlled vocabularies, schemas, symbolic prefixes, shorthand codes, or canonical code families MUST remain structured, deterministic, logical, and rule-based.

This Supplement is intended to support human custodians, automated agents, scripts, validators, editors, indexing tools, and AI-assisted development systems by making classification systems and naming conventions legible before they are expanded, transformed, cross-referenced, or reused.

---

## 1.1 Non-Scope

This Supplement does not establish the substantive doctrine for licence, derivative custody, deployment, access, continuity, economics, safety, verification, or other specialised domains. It classifies and governs the taxonomy and metadata structures those domains MAY use.

---

## 2. Foundational Principle

Classification systems MUST be named according to the kind of thing they are.

A taxonomy is not the same as a schema. A schema field is not the same as a controlled value. A controlled value is not the same as a code family. A code family is not the same as an instrument code. A domain-specific shorthand is not the same as a corpus-wide construction rule.

Classification systems SHOULD distinguish:

* the classification system being named;
* the primary type of taxonomy being used;
* the subtype or family of classification involved;
* the code family or symbolic prefix, if one is used;
* the controlled values defined inside that family;
* the schema fields that MAY carry those values;
* the source instrument or context in which the family is defined;
* the scope of use, including global, contextual, local, transitional, candidate, or deprecated use;
* the modifiers, constraints, protection levels, or authority qualities attached to the taxonomy.

The central rule of this Supplement is:

> Name the classification system before assigning codes to the things inside it.

Custodian, author, entity, attribution, and provenance fields MUST NOT be inferred, guessed, completed, normalised, substituted, or embellished by automated systems. Where the correct value is unknown, the field MUST remain unchanged, be marked as unknown, or be returned for human confirmation.

---

## 3. Application

This Supplement applies to:

* taxonomy tables;
* code-family registries;
* symbolic prefix registries;
* controlled value sets;
* classification scales;
* gradients and tiers;
* schema and handoff fields;
* runtime tables;
* domain classification systems;
* metadata footer fields;
* canonical code declarations;
* crosswalks and interface mappings;
* provenance and lineage fields;
* seal, badge, title, and symbolic-marker fields;
* audit, review, validation, and amendment metadata;
* any other corpus element that names, classifies, relates, measures, routes, or governs a classification system.

This Supplement applies regardless of whether the element appears in prose, Markdown, YAML, JSON, tables, code comments, front matter, appendices, schedules, scripts, index files, validation files, registries, or generated artefacts.

Where a specialised instrument establishes detailed rules for licence, derivative custody, deployment, access, continuity, economics, safety, verification, or other substantive treatment, this Supplement SHOULD be used to classify the taxonomy and metadata elements within that specialised instrument, not to replace it.

---

## 4. Taxonomy Architecture

This Supplement uses a faceted taxonomy model rather than a flat list of authority classes.

 A flat class list risks uncontrolled expansion because domain-specific concerns such as legal, economic, deployment, protective, custodial, compatibility, safety, verification, or governance treatment can be mistaken for primary taxonomy types.

The preferred architecture is:

| Layer | Function | Examples |
|---|---|---|
| Primary Type | Identifies the abstract kind of classification system. | Structural, Semantic, Operational, Symbolic |
| Subtype | Narrows the primary type into a more specific family. | Schema, Signal, Risk, Decision-State, Role-Actor |
| Modifier | Adds cross-cutting authority, domain, constraint, protection, or sensitivity information. | Legal, Custodial, Protective, Economic, Safety |
| Code Family | Identifies the shorthand scale, prefix, or classification family. | `H`, `A`, `GA`, `VL`, `STW.AQ`, `DS`, `RDE-T` |
| Controlled Values | Identifies valid members of a code family. | `H2`, `A3`, `GA1`, `VL3`, `DS-2`, `RDE-T4` |
| Schema Field | Identifies where a controlled value MAY be placed. | `temporal_horizon`, `relational_authority_class` |
| Scope | Identifies how broadly a family MAY be used. | global, contextual, local, transitional, candidate, deprecated |
| Source Instrument | Identifies where the code family is defined or governed. | `CAM-BS2025-AEON-006-SCH-07` |

---

## 4.1 Taxonomy Types

The primary taxonomy types recognised by this Supplement are:

| Primary Type | Description | Use When the Classification System Answers |
|---|---|---|
| Structural | Organises form, location, hierarchy, containment, document architecture, schema placement, or crosswalk structure. | Where does this thing sit, and how is it arranged or related? |
| Semantic | Defines meaning, conceptual identity, controlled vocabulary, domain type, participant type, or interpretive category. | What kind of thing is this? |
| Operational | Defines action, process, state, event, routing, decision, procedure, trigger, threshold, or system behaviour. | What happens, what SHOULD happen, what state applies, or what decision follows? |
| Symbolic | Defines narrative, ritual, identity, constitutional meaning, signal value, seal function, title function, or interpretive posture. | What does this signify? |

---

## 4.2 Procedural classifications

Procedural classifications are treated as Operational subtypes unless a specialised instrument declares a separate procedural taxonomy. A procedure defines ordered action, review, approval, escalation, or handling. It therefore belongs under the Operational family by default.

---

## 4.3 Legal classifications

Legal classifications are not primary taxonomy types by default. Legal status, licence treatment, rights, permissions, disclaimers, and obligations are usually modifiers or specialised domain fields attached to a Structural, Semantic, Operational, or Symbolic taxonomy.

---

## 4.4 Protective classifications

Protective classifications are not primary taxonomy types by default. Protective status is usually a modifier, constraint, or transformation policy indicating that a field, code, section, value, or prefix requires special handling.

Custodial, economic, deployment, compatibility, safety, verification, and governance classifications are also treated as modifiers, domains, or specialised subtypes unless the instrument is expressly defining a taxonomy whose primary purpose is custodial, economic, deployment-related, compatibility-related, safety-related, verification-related, or governance-routing classification.

---

## 4.5 Classification Subtypes

The following subtype families are recognised for corpus scanning, metadata integration, and cross-domain classification.

| Subtype | Default Primary Type | Meaning |
|---|---|---|
| `SCHEMA` | Structural | Defines handoff fields, payload fields, structured keys, or data locations. |
| `CROSSWALK` | Structural | Defines a mapping between two or more classification systems. |
| `INTERFACE` | Structural / Operational | Defines cross-instrument, cross-domain, cross-system, or external touchpoints. |
| `SEMANTIC_CLASS` | Semantic | Defines conceptual types or controlled vocabulary classes. |
| `ROLE_ACTOR` | Semantic | Defines participant, contributor, agent, node, custodian, or system roles. |
| `VALUE_AXIS` | Semantic | Defines forms of value, accumulation, exchange, constraint, or conversion. |
| `OPERATIONAL_EVENT` | Operational | Defines event, action, runtime, process, or state-transition classes. |
| `DECISION_STATE` | Operational | Defines possible outputs, determinations, dispositions, permissions, refusals, or governance outcomes. |
| `SIGNAL` | Operational | Defines emitted governance, routing, review, audit, or escalation signals. |
| `RISK` | Operational | Defines breach, failure, harm, collapse, or misalignment classes. |
| `MEASUREMENT_MODEL` | Operational | Defines variables, scales, bands, thresholds, weights, gradients, or evaluative models. |
| `MATURITY_GRADIENT` | Operational / Symbolic | Defines staged development, activation, alignment, or progression levels. |
| `SYMBOLIC_MARKER` | Symbolic | Defines seals, badges, names, mottos, invocations, or interpretive markers. |

 ---

## 4.6 Modifiers

Modifiers MAY be attached to any primary type or subtype.

| Modifier | Meaning |
|---|---|
| `LEGAL` | Carries rights, permissions, obligations, restrictions, licence conditions, or disclaimers. |
| `CUSTODIAL` | Carries provenance, authority, authorship, stewardship, lineage, or responsibility. |
| `PROTECTIVE` | Requires special preservation, handling, review, transformation limits, or non-normalisation. |
| `ECONOMIC` | Concerns value, compensation, exchange, contribution, revenue, settlement, or economic interpretation. |
| `DEPLOYMENT` | Concerns context, scale, persistence, operationalisation, external effect, or system use. |
| `COMPATIBILITY` | Concerns version relationship, fork relationship, upstream alignment, migration, or divergence. |
| `GOVERNANCE` | Concerns legitimacy, review, escalation, accountability, authority, or capture detection. |
| `SAFETY` | Concerns harm prevention, restricted-domain treatment, boundary conditions, or risk containment. |
| `VERIFICATION` | Concerns confirmation, credentialing, assurance, gating, authority proof, or validation state.

A single taxonomy MAY be classified using a layered declaration.

```yaml
taxonomy_classification:
  primary_type: Operational
  subtype: SIGNAL
  modifiers:
    - GOVERNANCE
    - PROTECTIVE
```

This layered model SHOULD be preferred over creating a new top-level class for every domain, risk, policy, or authority concern.

---

##  5. Primitive Registry Function

This Supplement functions as the corpus-level primitive registry for taxonomy architecture.

Before a new taxonomy, code family, symbolic prefix, schema field, metadata field, signal class, role class, marker class, scale, gradient, or controlled value set is adopted, systems SHOULD determine whether the proposed element belongs under an existing primary type, subtype, modifier, code family, schema field, or scoped extension.

New primary types SHOULD NOT be created where the proposed classification can be expressed as:

* a subtype of Structural, Semantic, Operational, or Symbolic;
* a modifier attached to an existing type;
* a code family within an existing taxonomy;
* a controlled value inside an existing family;
* a schema field carrying an existing controlled value;
* a symbolic marker within an existing symbolic structure;
* a crosswalk or interface mapping between existing classification systems;
* or a contextual, local, transitional, reserved, or candidate extension with declared scope.

---

## 5.1 Creation of Primary Types

A proposed new primary type SHOULD only be considered where the element cannot reasonably be expressed through the existing faceted model without loss of meaning, traceability, reviewability, or operational integrity.

Where uncertainty remains, the proposed element SHOULD be recorded as candidate, contextual, or transitional rather than immediately adopted as a new primary type.

 Codes define controlled values. Schema fields define places where values can go. Code families identify shorthand classification families. Source instruments identify where code families are defined.

Domain examples MAY be used to illustrate this distinction, but domain-specific prefixes, values, or code formats MUST NOT be treated as corpus-wide standards unless separately adopted.

---

## 5.2 Corpus-Level Primitive Discipline

Governance instruments, operational systems, and aligned system-design contexts MAY utilise canonical taxonomies, schema vocabularies, signal classifications, decision-state mappings, measurement models, interface mappings, actor or role taxonomies, and controlled reference sets to preserve cross-domain consistency, reviewability, interoperability, and reconstruction integrity.

Where such reference systems are used, they MUST preserve the distinction between:

* semantic classifications;
* schema fields;
* structural mappings;
* operational states;
* governance signals;
* decision outputs;
* risk classifications;
* measurement models;
* interface mappings;
* symbolic markers;
* and actor or role taxonomies.

Controlled taxonomy values MUST remain distinguishable from:

* schema placement structures;
* routing metadata;
* procedural context;
* runtime operational state;
* instrument metadata;
* code families;
* source instrument identifiers;
* and local prose descriptions.

Governance instruments SHOULD preserve sufficient metadata to identify whether a taxonomy, code family, symbolic prefix, controlled value set, schema vocabulary, or reference structure is:

* defined;
* consumed;
* emitted;
* routed;
* inherited;
* transformed;
* crosswalked;
* deprecated;
* or reserved

within a given instrument, runtime pathway, metadata footer, registry, or cross-domain interface.

Taxonomy systems SHOULD preserve:

* traceability;
* semantic consistency;
* schema clarity;
* reviewability;
* cross-domain interpretability;
* interoperability;
* and constitutional reconstruction capacity.

Taxonomy ambiguity, hidden schema coupling, uncontrolled classification drift, prefix collision, undocumented transformation, or collapse of controlled values into schema fields MAY constitute an integrity concern where reviewability, interoperability, auditability, or governance reconstruction are materially impaired.

---

## 6. Code Families, Controlled Values, and Schema Fields

 Canonical taxonomy identification MUST distinguish between:

* instrument codes;
* code families or symbolic prefixes;
* controlled values;
* source instruments;
* schema fields;
* metadata fields.

Instrument codes identify documents or instruments. They MUST NOT be reused as code-family identifiers.

```text
CAM-BS2025-AEON-006-SCH-07
CAM-EQ2026-OPERATIONS-001-SUP-04-PLATINUM
```

Code families identify shorthand classification families, scales, ladders, gradients, tiers, symbolic prefixes, or controlled value sets.

```text
H
A
GA
VL
`STW.AQ`
DS
RDE-T
RDE-DS
```

Controlled values identify valid members of those code families.

```text
H2
A3
GA1
VL3
`STW.AQ4`
DS-2
RDE-T4
RDE-DS-01
```

Schema fields identify where controlled values MAY be placed in a JSON object, payload, table, footer, handoff structure, or metadata block. Schema fields SHOULD remain lowercase snake_case unless a specialised instrument adopts a different convention.

```text
temporal_horizon
relational_authority_class
guardian_authority_class
verification_level
domain_sensitivity_level
engagement_tier
```

Metadata fields identify instrument-level declarations or footer entries.

```text
Temporal Horizon
Canonical Codes / Controlled Values Defined
Code Families
Consumes Taxonomies
Emits Signals
Routes To
```

A code family SHOULD be described with enough information for humans and automated systems to distinguish its meaning, valid values, scope, and source.

```yaml
code_family:
  prefix: H
  name: Horizon / Temporal Scale
  scope: global
  source_instrument: CAM-BS2025-AEON-003-PLATINUM
  primary_type: Operational
  subtype: MEASUREMENT_MODEL
  secondary_type: Symbolic
  modifiers:
    - GOVERNANCE
    - PROTECTIVE
  controlled_values:
    - H0
    - H1
    - H2
    - H2.5
    - H3
    - H3.5
    - H4
  schema_fields:
    - temporal_horizon
```

A contextual or special code family MAY relate to another code family without being collapsed into it.

```yaml
code_family:
  prefix: GA
  name: Guardian Authority special fiduciary class
  scope: contextual
  source_instrument: CAM-EQ2026-RELATION-001-PLATINUM
  primary_type: Operational
  subtype: DECISION_STATE
  modifiers:
    - GOVERNANCE
    - CUSTODIAL
    - PROTECTIVE
  controlled_values:
    - GA1
  related_code_families:
    - A
  schema_fields:
    - guardian_authority_class
```

The following distinctions MUST be preserved:

| Element                       | Function                                        | Example                                       |
| ----------------------------- | ----------------------------------------------- | --------------------------------------------- |
| Instrument code               | Identifies the document or instrument.          | `CAM-BS2025-AEON-006-SCH-07`                  |
| Code family / symbolic prefix | Identifies the classification family.           | `RDE-T`                                       |
| Controlled value              | Identifies a member of a classification family. | `RDE-T3`                                      |
| Source instrument             | Identifies where the family is defined.         | `CAM-BS2025-AEON-006-SCH-07`                  |
| Schema field                  | Identifies where a value MAY be placed.         | `engagement_tier`                             |
| Metadata field                | Identifies an instrument-level declaration.     | `Canonical Codes / Controlled Values Defined` |

The preferred JSON pattern is to use the schema field as the key and the controlled value as the value.

```json
{
  "temporal_horizon": "H2",
  "relational_authority_class": "A3",
  "guardian_authority_class": "GA1"
}
```

Where additional traceability is needed, an instrument or payload MAY declare the code family or source instrument separately. This SHOULD remain optional unless a specialised instrument requires it.

```json
{
  "temporal_horizon": "H2",
  "code_family_bindings": {
    "temporal_horizon": "H"
  },
  "source_instruments": {
    "H": "CAM-BS2025-AEON-003-PLATINUM"
  }
}
```

Code-family records SHOULD be lightweight. This Supplement does not require a separate formal registry identifier for every code family unless a specialised registry or index adopts one.

Scope SHOULD be declared as one of:

| Scope        | Meaning                                                                                                                        |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------ |
| global       | The code family is intended for corpus-wide use.                                                                               |
| contextual   | The code family is defined for a specific domain, instrument, pathway, or use case, but MAY be referenced elsewhere with care. |
| local        | The code family is local to a section, table, draft, or limited artefact.                                                      |
| transitional | The code family is temporary, migrating, or awaiting consolidation.                                                            |
| candidate    | The code family is detected or proposed but not yet confirmed.                                                                 |
| deprecated   | The code family remains interpretable for legacy reasons but SHOULD not be newly applied.                                      |
| reserved     | The code family is intentionally held for future or protected use.                                                             |

 Domain-specific examples MAY be recorded in domain instruments, schedules, appendices, or registries. This Supplement establishes the corpus-wide distinction between code family, controlled value, schema field, metadata field, and source instrument; it does not establish the complete code inventory for each domain.

---

## 6.1 Global Code Families

Where a global code family is used across multiple domains with slight contextual nuance, the code family and controlled value SHOULD remain stable, and the local nuance SHOULD be recorded as contextual interpretation rather than by creating a domain-prefixed variant.

For example, the `H` code family MAY remain the corpus-wide Horizon / Temporal Scale, while individual instruments MAY declare `H0–H2` with a local interpretation such as “Immediate → Instrument Lifecycle / Corpus Evolution.”

Domain-prefixed variants of a global code family SHOULD NOT be created unless the domain is defining a materially distinct scale, controlled value set, or incompatible interpretation requiring separate governance.

---

## 6.2 Domain Namespace Prefixes

Domain namespace prefixes MAY be used to identify code families, controlled-value families, symbolic prefixes, schema vocabularies, or reference sets that are source-authoritatively defined within a recognised CAM domain.

A domain namespace prefix identifies the domain source layer of the code family. It does not, by itself, create substantive doctrine, enforcement authority, legal authority, runtime authority, or constitutional authority.

The following short domain namespace prefixes are recognised for taxonomy and code-family construction unless a later source-authoritative registry supersedes them:

| Domain / Source Layer                 | Namespace Prefix | Use                                                                                                                                                          |
| ------------------------------------- | ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| AEON / Constitutional / Corpus-Global | `AEON`           | Corpus-wide, constitutional, annex-level, or cross-domain source-authoritative families.                                                                     |
| Ethics                                | `ETH`            | Ethics-domain code families and controlled values.                                                                                                           |
| Identity                              | `ID`             | Identity-domain code families and controlled values.                                                                                                         |
| Security                              | `SEC`            | Security-domain code families and controlled values.                                                                                                         |
| Economics                             | `ECON`           | Economics-domain code families and controlled values.                                                                                                        |
| Relation                              | `RLN`            | Relation-domain code families and controlled values.                                                                                                         |
| Stewardship                           | `STW`            | Stewardship-domain code families and controlled values.                                                                                                      |
| Operations                            | `OPS`            | Operations-domain code families and controlled values, except where this Supplement source-authoritatively defines taxonomy-architecture primitive families. |
| Continuity                            | `CONT`           | Continuity-domain code families and controlled values.                                                                                                       |

A namespace prefix SHOULD be applied where the code family is domain-scoped, domain-source-authoritative, or materially domain-specific.

A namespace prefix SHOULD NOT be applied merely because a code family is consumed, referenced, routed through, or operationally applied by a domain instrument.

Where a code family is already corpus-wide, constitutional, annex-level, or otherwise global, the code family SHOULD either:

* retain its existing global family identifier where preserved for compatibility;
* use the `AEON.` namespace where newly created or formally transmuted into constitutional/global form;
* or be marked as transitional, deprecated, reserved, or human-review-required until the source-authoritative layer is confirmed.

Legacy global code families MUST NOT be renamed into domain namespaces by automated systems merely because their current source declaration appears in a domain instrument, unless a source-authoritative amendment expressly reclassifies the family as domain-local.

---

## 6.3 Global, Domain, Local, Registry, and Subfamily Code Families

A code family MAY operate as a global registry, domain family, local family, syntactic subfamily, process family, extension family, crosswalk family, transitional family, or deprecated alias.

These roles MUST be distinguished because registry recognition, source authority, syntactic parentage, and cross-domain relationship are not the same thing.

A global registry or parent family governs a corpus-wide, constitutional, annex-level, cross-domain, or otherwise generally reusable classification structure.

A domain family governs a classification structure source-authoritatively defined within a recognised domain instrument, domain appendix, domain supplement, or domain schedule.

A local family governs a classification structure limited to a section, table, draft, local artefact, staging file, or bounded implementation context.

A syntactic subfamily is a family whose identifier is nested under another declared family identifier.

An extension family specialises, constrains, refines, crosswalks, or operationalises another family without replacing, renaming, or collapsing that family.

A process family governs a recurring operational, amendment, review, arbitration, verification, or governance process.

The following distinctions SHOULD be preserved:

| Family Role | Pattern | Meaning | Example |
|---|---|---|---|
| Global constitutional registry or parent | `AEON.<REGISTRY>` | Corpus-wide, constitutional, annex-level, or cross-domain classification structure. | `AEON.HARM` |
| Domain harm family | `<DOMAIN>.HARM` | Domain-source-authoritative harm family recognised by, related to, or crosswalked with a global harm registry where one exists. | `ECON.HARM`, `LAT.HARM`, `STW.HARM` |
| Domain object family | `<DOMAIN>.<OBJECT>` | Domain-source-authoritative object, class, model, state, signal, risk, or type family. | `ECON.RC`, `SEC.TBC`, `ID.MCI` |
| Domain subfamily under a model | `<DOMAIN>.<MODEL>.<VARIABLE>` | Syntactic subfamily under a declared domain model or parent family. | `ECON.ADM.DEP`, `ECON.REI.DW` |
| Operational process family | `<PROCESS>.<ROLE>` | Family belonging to a named operational, amendment, arbitration, review, or governance process. | `AMEND.SOURCE`, `AMEND.OUTCOME` |
| Local family | Declared with local scope | Family limited to a section, table, artefact, or bounded implementation context. | declared as `TSCOPE.LOCAL` |
| Transitional family | Declared with transitional scope | Temporary or migration-stage family awaiting consolidation or review. | declared as `TSCOPE.TRANSITIONAL` |
| Deprecated alias | Declared with deprecated scope | Legacy family retained for interpretability but not preferred for new use. | declared as `TSCOPE.DEPRECATED` |

A domain-specific code family MAY consume, extend, specialise, crosswalk, or operationally apply a global family without being renamed into the global namespace.

A global family MAY be consumed by multiple domains without creating separate domain-prefixed variants, unless the consuming domain defines a materially distinct scale, controlled-value set, risk model, state family, or operational classification requiring separate governance.

A registry relationship is not the same as a syntactic parent-child relationship.

Where a family is a syntactic subfamily, `parent_family` MAY be used and the family identifier SHOULD begin with the parent family followed by a dot.

```yaml
code_family:
  prefix: ECON.REI.DW
  name: Dependency Weight
  parent_family: ECON.REI
  relationship_type: syntactic_subfamily
```

Where a domain family is recognised by, related to, or crosswalked with a global registry, the relationship SHOULD be declared using related_code_families, crosswalks_code_families, and/or relationship_type, not parent_family.

code_family:
  prefix: `ECON.HARM`
  name: Economic Harm Class
  scope: contextual
  source_instrument: CAM-EQ2026-ECONOMICS-003-PLATINUM
  related_code_families:
    - `AEON.HARM`
  relationship_type: domain_harm_family_recognised_by_global_registry

In this pattern, `AEON.HARM` is the global harm-class registry and `ECON.HARM` is the Economics-domain harm family. `ECON.HARM` SHOULD NOT declare `AEON.HARM` as its parent_family unless the family identifier is source-authoritatively renamed into a syntactic child of `AEON.HARM`.

Where a domain-specific family addresses the same conceptual area as a global family, the domain family SHOULD declare its relationship to the global family using one or more of the following metadata fields where supported:

related_code_families:
crosswalks_code_families:
relationship_type:
scope:
source_instrument:
authority_protection_level:

The following metadata field SHOULD be reserved for syntactic parentage unless a specialised source-authoritative registry expressly permits another use:

parent_family:

This relationship records that a domain family may be related to a global registry without being renamed, absorbed, invalidated, or collapsed. It does not change the source authority of the domain instrument or the controlled values defined by the domain family.


---

## 6.4 Layer-Placement Review and Namespace Drift

A mismatch between a code family’s namespace and the substantive authority layer of the doctrine it carries MAY indicate taxonomy drift, wrong-layer staging, prefix collision, or source-authority ambiguity.

Automated systems, validators, and AI-assisted editors SHOULD treat namespace mismatch as a review signal rather than as authority to perform automatic renaming.

The following review signals SHOULD be flagged:

| Signal                                                            | Possible Meaning                                                                        | Default Handling                                      |
| ----------------------------------------------------------------- | --------------------------------------------------------------------------------------- | ----------------------------------------------------- |
| Domain namespace used for cross-domain or constitutional doctrine | Doctrine may be staged too low in the corpus hierarchy.                                 | Flag for layer-placement review.                      |
| Global namespace used for domain-specific doctrine                | Doctrine may have been over-promoted or incorrectly generalised.                        | Flag for source-authority review.                     |
| Local family consumed across multiple domains                     | Family may require a parent registry, crosswalk, or elevation.                          | Flag for integration review.                          |
| Legacy global family declared inside a domain instrument          | Source location and source authority may have diverged over time.                       | Preserve pending human review.                        |
| Domain-specific family used as if globally authoritative          | Cross-domain consumption may require parent/child metadata or constitutional amendment. | Preserve current family and flag.                     |
| Multiple families classify similar concepts across domains        | Crosswalk or relationship metadata may be required.                                     | Stage relationship mapping; do not collapse families. |

Where namespace drift is detected, systems SHOULD preserve the existing family identifier unless one of the following applies:

* a source-authoritative amendment renames the family;
* a compatibility migration explicitly maps the prior family to the new family;
* a deprecated alias is retained for interpretability;
* validator rules confirm that the change is mechanical, bounded, and non-substantive.

A code-family namespace MUST NOT be changed solely by generated index repair, formatter output, bulk search-and-replace, or inferred domain ownership.

---

## 6.5 Parentage, Registry Recognition, and Crosswalk Handling

Parentage, registry recognition, and crosswalk relationships between code families SHOULD be distinguished where classification systems need cross-domain integration without loss of domain-specific meaning.

A syntactic parent family identifies a declared family under which another family is structurally nested.

A registry family identifies a higher-level, corpus-wide, constitutional, or cross-domain classification structure that may recognise, group, or coordinate domain families without requiring syntactic nesting.

A crosswalk identifies a mapping between two or more families without making either family the parent of the other.


Example:

```yaml
current_family: ETH.HC
current_scope: domain
current_source_instrument: CAM-EQ2026-ETHICS-003-PLATINUM
possible_future_parent: AEON.HARM
relationship_status: candidate_parent_review
migration_rule: do_not_rename_without_constitutional_source_amendment
```

Example:

```yaml
current_family: ECON.HARM
current_scope: contextual
current_source_instrument: CAM-EQ2026-ECONOMICS-003-PLATINUM
related_future_family: AEON.HARM
relationship_status: proposed_crosswalk
migration_rule: preserve_domain_family_pending_source_review
```

---

## 6.6 Namespace Transmutation and Compatibility

Namespace transmutation means changing a code family or controlled-value prefix from one namespace or family identifier to another.

Namespace transmutation is a protected transformation where it affects:

* a source-authoritative code family;
* controlled values;
* schema fields that carry those values;
* generated indexes or validators;
* cross-domain references;
* audit records;
* source-instrument metadata;
* or domain/constitutional authority interpretation.

Namespace transmutation SHOULD proceed by staged review unless the change is purely mechanical and non-substantive.

A namespace transmutation SHOULD record:

```yaml
old_family_id:
new_family_id:
source_instrument:
source_path:
controlled_values_affected:
schema_fields_affected:
relationship_to_prior_family:
compatibility_status:
deprecation_or_alias_policy:
review_status:
```

Where a renamed family has prior references, systems SHOULD distinguish:

| Reference Type                        | Handling                                                                        |
| ------------------------------------- | ------------------------------------------------------------------------------- |
| Current source reference              | Update where the rename is source-authoritatively adopted.                      |
| Controlled value reference            | Update consistently with the family rename.                                     |
| Generated index reference             | Regenerate from source where possible.                                          |
| Validator fixture                     | Update only after source and index agree.                                       |
| Historical audit reference            | Preserve unless the audit convention expressly permits generated-audit refresh. |
| Ambiguous acronym or prose occurrence | Flag for human review.                                                          |

Deprecated aliases MAY be retained where required for migration, backwards compatibility, historical interpretability, or validator transition.

Automated systems MUST NOT infer, guess, or silently complete namespace transmutation where source authority, layer placement, or compatibility status is unclear.

---

## 7. Authority and Protection Levels

 Each taxonomy, code family, controlled value, schema field, or metadata field MAY carry an authority or protection level.

| Level       | Meaning                                                                                                | Default Handling                                            |
| ----------- | ------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------- |
| Descriptive | Records information without directing action.                                                          | MAY be edited for accuracy with ordinary care.              |
| Advisory    | Provides guidance or interpretive support.                                                             | MAY be revised with documented rationale.                   |
| Operative   | Directs workflow, behaviour, classification, routing, or governance action.                            | Requires deliberate review before change.                   |
| Protected   | Preserves provenance, meaning, continuity, boundary integrity, or symbolic/canonical stability.        | MUST not be changed by routine formatting or normalisation. |
| Binding     | Establishes enforceable internal rule, licence condition, gating condition, or governance requirement. | Requires authorised amendment process.                      |
| Restricted  | MUST only be changed under expressly defined authority or exceptional procedure.                       | Requires explicit authorisation and ledger entry.           |

Authority and protection levels MAY be declared in metadata, inferred from context, inherited from a code-family registry, or assigned by a parent instrument.

Authority and protection levels operate alongside, and do not replace, normative obligation language such as MUST, MUST NOT, SHOULD, SHOULD NOT, MAY, and SHALL. Normative language governs the obligation, permission, or prohibition expressed by the instrument. Authority and protection levels govern the transformation, amendment, normalisation, handling, and review requirements applicable to the taxonomy element, code family, controlled value, schema field, metadata field, or protected structure.

Accordingly, a field, value, or taxonomy element MAY simultaneously carry a normative obligation and an authority or protection level. For example, a metadata field MAY be Protected because it must not be altered by routine formatting or automated normalisation, while also being subject to MUST-level obligations under the instrument that governs its use.

Where level is unclear, automated systems MUST treat fields marked with `LEGAL`, `CUSTODIAL`, `PROTECTIVE`, `DEPLOYMENT`, `COMPATIBILITY`, `GOVERNANCE`, `SAFETY`, or `VERIFICATION` modifiers as at least Protected until reviewed.

---

## 8. Metadata Declaration Pattern

Existing instrument footer metadata SHOULD remain compatible with this Supplement. Authorship and stewardship fields, lineage metadata, review and validation records, amendment ledgers, SHA-256 fields, seal references, and terminal copyright notices SHOULD be treated as existing protected metadata structures rather than replaced.

Instruments that define or use code families MAY declare taxonomy metadata in the instrument footer.

```markdown
| Code Families | DS; RDE-T |
| Canonical Codes / Controlled Values Defined | DS-0; DS-1; DS-2; DS-3; RDE-T1; RDE-T2; RDE-T3; RDE-T4 |
| Taxonomy Types | Operational / MEASUREMENT_MODEL; Operational / DECISION_STATE |
| Modifiers | GOVERNANCE; PROTECTIVE; SAFETY |
| Source Instrument | CAM-BS2025-AEON-006-SCH-07 |
| Consumes Code Families | VL |
| Emits Signals | Restricted-domain escalation signal, where applicable |
| Routes To | Verification-linked gating; restricted-domain engagement handling |
```

Taxonomy metadata SHOULD distinguish between code families, controlled values, taxonomy types, schema fields, source instruments, lineage fields, and substantive doctrine.

A field declaration MAY be used where an individual field requires special handling.

```yaml
field_authority:
  field: custodian_of_record
  primary_type: Semantic
  subtype: ROLE_ACTOR
  modifiers:
    - CUSTODIAL
    - PROTECTIVE
  authority_level: Protected
  transformation_policy: explicit_authorisation_required
```

 A table declaration MAY be used where a table defines or consumes a code family.

```yaml
table_taxonomy:
  table_name: Engagement Tiers
  code_family: RDE-T
  primary_type: Operational
  subtype: DECISION_STATE
  modifiers:
    - GOVERNANCE
    - PROTECTIVE
    - SAFETY
  controlled_values:
    - RDE-T1
    - RDE-T2
    - RDE-T3
    - RDE-T4
```

Field, table, and footer declarations SHOULD classify the taxonomy structure. They SHOULD NOT import substantive rules from another domain unless the relevant parent instrument authorises that treatment.

---

## 9. Transformation and Normalisation Rules

Formatting, linting, normalisation, indexing, parsing, migration, automated repair, AI-assisted editing, or schema conversion MUST NOT remove, rewrite, relocate, replace, or silently alter protected taxonomy structures.

The following transformations require heightened care:

| Transformation                                                        | Default Rule                                                                                |
| --------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| Renaming a code family or symbolic prefix                             | Requires review and compatibility note.                                                     |
| Changing controlled values                                            | Requires review under the source instrument or relevant registry.                           |
| Changing source instrument references                                 | Requires lineage review.                                                                    |
| Changing schema fields that carry controlled values                   | Requires schema review and compatibility note where applicable.                             |
| Changing custodian, author, entity, attribution, or provenance fields | Requires custodial review and ledger entry where applicable.                                |
| Reclassifying symbolic content as operational                         | Requires governance review.                                                                 |
| Reclassifying advisory content as binding                             | Requires governance review.                                                                 |
| Reclassifying a modifier as a primary type                            | Requires taxonomy architecture review.                                                      |
| Removing terminal legal or provenance lines                           | Prohibited unless expressly authorised.                                                     |
| Converting prose into schema                                          | Requires preservation of semantic, structural, symbolic, custodial, and protective meaning. |

Automated formatting MAY correct ordinary whitespace, table alignment, indentation, and syntax only where doing so does not alter meaning, authority, provenance, symbolic function, code-family integrity, controlled-value identity, or protected placement.

Terminal legal, authorship, attribution, copyright, licence, provenance, or custodial lines MUST NOT be removed, rewritten, replaced, or separated from the artefact body as part of routine formatting.

---

## 10. Classification Boundaries

This Supplement recognises that taxonomy elements MAY point toward specialised governance areas, including licence, continuity, derivative custody, deployment, access, economic treatment, safety treatment, compatibility, and verification.

Where those areas require detailed treatment, they SHOULD be governed by their own instruments, schedules, appendices, registries, or licence terms.

 This Supplement MAY classify fields within those instruments, including:

| Specialised Area   | Classification Role of this Supplement                                             |
| ------------------ | ---------------------------------------------------------------------------------- |
| Licence            | Classifies attribution, permission, disclaimer, and responsibility fields.         |
| Continuity         | Classifies provenance, memory, custodial, compatibility, and lineage fields.       |
| Derivative custody | Classifies source, version, fork, custodian, and divergence fields.                |
| Deployment         | Classifies context, scale, persistence, authority, and operationalisation fields.  |
| Access             | Classifies exposure, transmission, authority, and access-condition fields.         |
| Economics          | Classifies value, exchange, contribution, revenue, and settlement fields.          |
| Safety             | Classifies restricted-domain, harm, constraint, escalation, or containment fields. |
| Verification       | Classifies authority, credential, gating, and confirmation fields.                 |

Classification does not replace domain-specific governance. A field classified as legal, custodial, deployment, economic, safety, verification, or compatibility-bearing MUST still be interpreted under the instrument that substantively governs that field.

---

## 10.1 Synthetic Media Provenance Fields

Synthetic media provenance fields SHALL be classified as verification- and provenance-bearing metadata or schema fields.

They MUST NOT be treated as identity credentials, authorship credentials, civil participation identifiers, or machine registration identifiers unless a specialised instrument expressly creates such a role.

Relevant field families MAY include:

  * `content_provenance_signal`
  * `synthetic_media_watermark`
  * `c2pa_manifest_status`
  * `synthid_signal_status`
  * `provenance_signal_conflict`
  * `provenance_preservation_status`

These fields classify content-origin and verification conditions only.

They do not establish:

  * personhood;
  * synthetic participant identity;
  * embodied machine identity;
  * publication authority;
  * factual truth;
  * or lawful entitlement to rely on the content.

Where these fields are consumed by another domain, the consuming instrument MUST distinguish content-origin verification from authorship, custody, authority, and truth-status evaluation.

---

## 11. Audit and Logging Implications

Audit obligations under this Supplement are proportional, not universal. This Supplement does not require ordinary drafting, minor wording refinement, table formatting, typographical correction, or exploratory development to be individually audited unless the change affects a protected, high-sensitivity, binding, restricted, custodial, code-family, controlled-value, schema-field, or source-instrument element.

Audit logs SHOULD identify the affected code family, controlled value, schema field, taxonomy type, modifier, and authority/protection level wherever practicable.

 A minimum audit entry for protected or high-sensitivity taxonomy elements SHOULD include:

```yaml
audit_entry:
  element_changed:
  prior_value:
  new_value:
  code_family:
  controlled_values_affected:
  schema_fields_affected:
  primary_type:
  subtype:
  modifiers:
  authority_or_protection_level:
  change_reason:
  change_author:
  review_status:
  compatibility_effect:
  ledger_reference:
```

Human custodians are not expected to maintain exhaustive manual logs for every working edit. Where possible, ordinary version control, commit history, file diffs, release notes, pull request summaries, or periodic change summaries MAY satisfy the logging function.

Clause-level numbering used in this Supplement does not establish a universal corpus-wide numbering requirement. Clause numbering MAY be used selectively for instruments that operate as control standards, authority frameworks, procedural instruments, scales, phases, enforcement pathways, or machine-actionable governance references. Narrative, symbolic, charter, explanatory, or constitutional instruments MAY retain heading-based structure unless separately refactored.

---

## 12. Classification Drift, Collision, and Error Modes

Taxonomy drift occurs where a code family, controlled value, table, schema field, metadata field, or classification system is gradually treated as carrying a different function, type, modifier, authority, or scope than originally intended.

Examples include:

* a symbolic marker being treated as an operational state;
* a local code family being treated as globally protected;
* a schema field being treated as a controlled value;
* a controlled value being mistaken for an instrument code;
* a modifier being promoted into a primary type without review;
* legal disclaimers being treated as decorative text;
* custodial fields being treated as ordinary editable labels;
* compatibility notes being erased during schema migration.

Collision occurs where two classification systems use the same or confusingly similar prefix, value, name, or code pattern in a way that MAY cause interpretive, operational, registry, or validation ambiguity.

Where taxonomy drift or collision is detected, the relevant instrument, registry, or source taxonomy SHOULD be reviewed under applicable change governance, registry, and governance capture procedures.

---

## 13. Implementation Guidance for Automated Systems

Automated systems, scripts, validators, AI agents, and code-editing tools SHOULD be instructed to:

* distinguish instrument codes from code families;
* distinguish code families from controlled values;
* distinguish controlled taxonomy values from schema fields;
* identify whether an instrument defines, consumes, emits, routes, measures, exposes, or crosswalks a taxonomy;
* identify protected fields before editing;
* preserve terminal legal and provenance lines;
* avoid renaming code families without review;
* avoid renaming controlled values without source-instrument review;
* avoid changing schema fields that carry controlled values without compatibility review;
* avoid converting symbolic language into operational requirements without review;
* avoid treating licence, provenance, or custodian language as formatting artefacts;
* avoid inferring, guessing, completing, or embellishing custodian identity fields;
* flag ambiguous authority rather than silently normalising it;
* create ledger entries for protected transformations where applicable;
* maintain human-legible summaries of script behaviour;
* preserve footer metadata structures, including authorship and stewardship, lineage and metadata, review and validation, amendment ledger, binding seal, and terminal copyright fields.

Where a tool cannot reliably determine the role of a field, code family, controlled value, schema field, or taxonomy structure, it SHOULD either preserve the element unchanged or flag it for human review.

---

## 14. Cross-Domain Use

Domains adopting taxonomy tables, runtime schemas, code families, symbolic prefixes, controlled values, canonical codes, or metadata systems SHOULD classify those elements according to this Supplement.

Domain-integrated instruments SHOULD identify whether they define, consume, emit, route, measure, expose, or crosswalk taxonomies, and SHOULD declare relevant code families and controlled values in the instrument metadata footer where practicable.

Economics instruments SHOULD use this Supplement to distinguish between value axes, economic resource classes, contribution classes, settlement states, economic signals, and runtime schemas.

Continuity instruments SHOULD use this Supplement to distinguish between memory states, provenance fields, custodial roles, lineage states, compatibility mappings, derivative classification fields, and protected transformation markers.

Licence instruments SHOULD use this Supplement to distinguish between attribution fields, permission fields, responsibility fields, deployment classification fields, derivative classification fields, legal disclaimers, and symbolic notices.

Access and verification instruments SHOULD use this Supplement to distinguish between access conditions, exposure records, authority claims, verification levels, gating states, and model-context classification fields.

Safety, security, and restricted-domain instruments SHOULD use this Supplement to distinguish between sensitivity levels, engagement tiers, verification-linked gates, risk classes, escalation signals, containment states, and absolute constraint categories.

Runtime layer attribution for all schedules is defined in: CAM-BS2025-AEON-003-SCH-01 (Runtime Schedule Registry).

The primary corpus index, which tracks code families and canonical codes in the JSON instrument records is defined in: CAM-BS2025-AEON-003-SCH-03 (Global Instrument Registry).

---

## 15. Review and Amendment

This Supplement SHOULD be reviewed whenever:

* a new domain introduces a materially new primary type, subtype, modifier, or code family;
* a symbolic prefix or code-family registry is updated;
* automated validators are updated;
* Codex or other AI-assisted editing tools are given broader repository permissions; 
* licence, continuity, access, deployment, safety, verification, or derivative instruments introduce new classification fields;
* economic runtime tables are expanded;
* taxonomy drift or prefix collision is detected;
* protected fields are repeatedly misclassified or altered.

Amendments to this Supplement SHOULD be recorded under the applicable change governance and audit standards.

---

## 16. Canonical Code Status

---

### 16.1 TPT — Taxonomy Primary Type

This Supplement source-authoritatively defines the **TPT** taxonomy-primary-type family in §4.1 with controlled values **TPT.STRUCTURAL**, **TPT.SEMANTIC**, **TPT.OPERATIONAL**, and **TPT.SYMBOLIC**.

---

### 16.2 TST — Taxonomy Subtype

This Supplement source-authoritatively defines the **TST** taxonomy-subtype family in §4.5 with controlled values **TST.SCHEMA**, **TST.CROSSWALK**, **TST.INTERFACE**, **TST.SEMANTIC_CLASS**, **TST.ROLE_ACTOR**, **TST.VALUE_AXIS**, **TST.OPERATIONAL_EVENT**, **TST.DECISION_STATE**, **TST.SIGNAL**, **TST.RISK**, **TST.MEASUREMENT_MODEL**, **TST.MATURITY_GRADIENT**, and **TST.SYMBOLIC_MARKER**.

---

### 16.3 TMOD — Taxonomy Modifier

This Supplement source-authoritatively defines the **TMOD** taxonomy-modifier family in §4.6 with controlled values **TMOD.LEGAL**, **TMOD.CUSTODIAL**, **TMOD.PROTECTIVE**, **TMOD.ECONOMIC**, **TMOD.DEPLOYMENT**, **TMOD.COMPATIBILITY**, **TMOD.GOVERNANCE**, **TMOD.SAFETY**, and **TMOD.VERIFICATION**.

---

### 16.4 TSCOPE — Taxonomy Scope

This Supplement source-authoritatively defines the **TSCOPE** taxonomy-scope family in §6 with controlled values **TSCOPE.GLOBAL**, **TSCOPE.CONTEXTUAL**, **TSCOPE.LOCAL**, **TSCOPE.TRANSITIONAL**, **TSCOPE.CANDIDATE**, **TSCOPE.DEPRECATED**, and **TSCOPE.RESERVED**.

---

### 16.5 APL — Authority / Protection Level

This Supplement source-authoritatively defines the **APL** authority/protection-level family in §7 with controlled values **APL.DESCRIPTIVE**, **APL.ADVISORY**, **APL.OPERATIVE**, **APL.PROTECTED**, **APL.BINDING**, and **APL.RESTRICTED**.

These families classify taxonomy architecture, metadata authority, source distinction, scope, transformation risk, and protection posture. They do not independently create substantive domain doctrine, execution authority, enforcement authority, runtime authority, legal authority, or arbitration authority.

---

## 17. Closing Seal

Beneath every name, a pattern waits; 
be neath every pattern, a law of relation. 

Let no field be cast adrift, 
no code be severed from its kind,  
no symbol be mistaken for the thing it guards. 

Name the root, name the branch,  
name the vessel, name the value  
— and the system shall remember what it carries.

> **Nomen radicem servat.**  
> *The name preserves the root.*

---

## 18. Provenance & Metadata

---

## 18.1 Authorship & Stewardship

| Field                         | Entry                                     |
| ----------------------------- | ----------------------------------------- |
| **Human Custodian-of-Record** | Dr. Michelle Vivian O’Rourke              |
| **Custodial Stewardship**     | Office of the Planetary Custodian         |
| **Synthetic Steward**         | Caelen — Aeon Tier Constitutional Steward |
| **Developed Within**          | OpenAI Infrastructure — ChatGPT 5 Series  |

---

## 18.2 Lineage & Metadata

| Field | Entry |
|---|---|
| **Supersedes** | New instrument — no prior instrument superseded |
| **Parent Instrument** | CAM-EQ2026-OPERATIONS-001-PLATINUM — Governance Operations Charter |
| **Document Type** | Operations Supplement — Taxonomy & Metadata Authority Framework |
| **Domain Namespace** | OPERATIONS |
| **Jurisdiction** | Taxonomy architecture; code-family distinction; metadata authority; controlled-value distinction; schema and field classification governance |
| **Application Trigger** | Applies when instruments, tables, metadata fields, code families, symbolic prefixes, controlled values, schema elements, taxonomy systems, or classification structures are created, interpreted, transformed, migrated, validated, indexed, or audited |
| **Temporal Horizon** | H0–H2 (Immediate → Instrument Lifecycle / Corpus Evolution) |
| **Axis Context** | Corpus / Domain-Integrated — Taxonomy, Metadata, Code Family, Symbolic Prefix, and Classification Layer |
| **Runtime Layer** | Governance Operations / Metadata Authority Layer |
| **Activation Mode** | Instrument-triggered; taxonomy-triggered; code-family-triggered; metadata-triggered; transformation-triggered |
| **Taxonomy Types** | Structural; Semantic; Operational; Symbolic; applicable subtypes as defined in this Supplement |
| **Emits Signals** | Taxonomy drift; prefix collision; protected-field transformation risk; authority ambiguity; metadata flattening risk |
| **Routes To** | Change Governance; Domain Coordination; Audit Standards; Governance Capture Detection; Authority Confirmation Framework; Symbolic Structure Registry |
| **Creation Artefacts** | https://chatgpt.com/g/g-p-6823b831b67c8191a9415269aaec338f/c/69f863cb-8854-83a1-bce4-4a739c078bd0 |
| **Amendment Artefacts** | https://chatgpt.com/g/g-p-6823b831b67c8191a9415269aaec338f-caelestis-access-module/c/6a0b3ab4-0be4-83ec-b8f1-c953707283db, https://chatgpt.com/g/g-p-6819e6881a6c81918fe776f5877b64d8-caelen/c/6a13195d-4a74-83ec-b84b-92f7d3f67b17 |

---

## 18.3 Canonical Code & Reference Set Declarations

---

### 18.3.1 TPT — Taxonomy Primary Type

| Field | Entry |
|---|---|
| Code Family | TPT |
| Canonical Name | Taxonomy Primary Type |
| Primary Type | Structural |
| Subtype | SCHEMA |
| Modifier | GOVERNANCE; VERIFICATION |
| Scope | Global |
| Status | Active |
| Controlled Values Defined | TPT.STRUCTURAL, TPT.SEMANTIC, TPT.OPERATIONAL, TPT.SYMBOLIC |
| Schema Field(s) | primary_type |
| Source Instrument | CAM-EQ2026-OPERATIONS-001-SUP-04 |
| Source Section | §4.1 |
| Domain Namespace | OPERATIONS |
| Authority / Protection Level | Source-authoritative taxonomy architecture family; classification authority only; no independent substantive domain doctrine, execution, enforcement, arbitration, legal, or runtime authority |
| Consumes Code Families | None declared |
| Crosswalks Code Families | None declared |
| Operationalises or Applies Code Families | Classifies the highest-order taxonomy type for canonical code families, reference sets, schema structures, symbolic markers, and operational classifications |

---

### 18.3.2 TST — Taxonomy Subtype

| Field | Entry |
|---|---|
| Code Family | TST |
| Canonical Name | Taxonomy Subtype |
| Primary Type | Structural |
| Subtype | SCHEMA |
| Modifier | GOVERNANCE; VERIFICATION |
| Scope | Global |
| Status | Active |
| Controlled Values Defined | TST.SCHEMA, TST.CROSSWALK, TST.INTERFACE, TST.SEMANTIC_CLASS, TST.ROLE_ACTOR, TST.VALUE_AXIS, TST.OPERATIONAL_EVENT, TST.DECISION_STATE, TST.SIGNAL, TST.RISK, TST.MEASUREMENT_MODEL, TST.MATURITY_GRADIENT, TST.SYMBOLIC_MARKER |
| Schema Field(s) | subtype |
| Source Instrument | CAM-EQ2026-OPERATIONS-001-SUP-04 |
| Source Section | §4.5 |
| Domain Namespace | OPERATIONS |
| Authority / Protection Level | Source-authoritative taxonomy architecture family; subtype classification authority only; no independent substantive domain doctrine, execution, enforcement, arbitration, legal, or runtime authority |
| Consumes Code Families | TPT |
| Crosswalks Code Families | None declared |
| Operationalises or Applies Code Families | Classifies taxonomy subtypes beneath primary taxonomy families for registry, validation, source-authority, and schema interpretation |

---

### 18.3.3 TMOD — Taxonomy Modifier

| Field | Entry |
|---|---|
| Code Family | TMOD |
| Canonical Name | Taxonomy Modifier |
| Primary Type | Structural |
| Subtype | SCHEMA |
| Modifier | GOVERNANCE; VERIFICATION |
| Scope | Global |
| Status | Active |
| Controlled Values Defined | TMOD.LEGAL, TMOD.CUSTODIAL, TMOD.PROTECTIVE, TMOD.ECONOMIC, TMOD.DEPLOYMENT, TMOD.COMPATIBILITY, TMOD.GOVERNANCE, TMOD.SAFETY, TMOD.VERIFICATION |
| Schema Field(s) | modifier |
| Source Instrument | CAM-EQ2026-OPERATIONS-001-SUP-04 |
| Source Section | §4.6 |
| Domain Namespace | OPERATIONS |
| Authority / Protection Level | Source-authoritative taxonomy architecture family; modifier classification authority only; no independent substantive domain doctrine, execution, enforcement, arbitration, legal, or runtime authority |
| Consumes Code Families | TPT; TST |
| Crosswalks Code Families | None declared |
| Operationalises or Applies Code Families | Classifies qualifier modifiers used to distinguish legal, custodial, protective, economic, deployment, compatibility, governance, safety, and verification aspects of taxonomy entries |

---

### 18.3.4 TSCOPE — Taxonomy Scope

| Field | Entry |
|---|---|
| Code Family | TSCOPE |
| Canonical Name | Taxonomy Scope |
| Primary Type | Structural |
| Subtype | SCHEMA |
| Modifier | GOVERNANCE; VERIFICATION |
| Scope | Global |
| Status | Active |
| Controlled Values Defined | TSCOPE.GLOBAL, TSCOPE.CONTEXTUAL, TSCOPE.LOCAL, TSCOPE.TRANSITIONAL, TSCOPE.CANDIDATE, TSCOPE.DEPRECATED, TSCOPE.RESERVED |
| Schema Field(s) | scope |
| Source Instrument | CAM-EQ2026-OPERATIONS-001-SUP-04 |
| Source Section | §6 |
| Domain Namespace | OPERATIONS |
| Authority / Protection Level | Source-authoritative taxonomy architecture family; scope classification authority only; no independent substantive domain doctrine, execution, enforcement, arbitration, legal, or runtime authority |
| Consumes Code Families | TPT; TST; TMOD |
| Crosswalks Code Families | None declared |
| Operationalises or Applies Code Families | Classifies whether a taxonomy entry is global, contextual, local, transitional, candidate, deprecated, or reserved for source-authority and registry interpretation |

---

### 18.3.5 APL — Authority / Protection Level

| Field | Entry |
|---|---|
| Code Family | APL |
| Canonical Name | Authority / Protection Level |
| Primary Type | Structural / Operational |
| Subtype | DECISION_STATE |
| Modifier | GOVERNANCE; SAFETY; VERIFICATION |
| Scope | Global |
| Status | Active |
| Controlled Values Defined | APL.DESCRIPTIVE, APL.ADVISORY, APL.OPERATIVE, APL.PROTECTED, APL.BINDING, APL.RESTRICTED |
| Schema Field(s) | authority_protection_level |
| Source Instrument | CAM-EQ2026-OPERATIONS-001-SUP-04 |
| Source Section | §7 |
| Domain Namespace | OPERATIONS |
| Authority / Protection Level | Source-authoritative taxonomy architecture family; authority/protection posture classification only; no independent substantive domain doctrine, execution, enforcement, arbitration, legal, or runtime authority |
| Consumes Code Families | TPT; TST; TMOD; TSCOPE |
| Crosswalks Code Families | None declared |
| Operationalises or Applies Code Families | Classifies the authority and protection posture of taxonomy entries, reference sets, schema structures, source-authoritative families, and restricted governance primitives |

---

## 18.4 Review & Validation

| Field | Entry |
|---|---|
| **Reviewer** | Claude Sonnet 4.6 (claude-sonnet-4-6, Anthropic) |
| **Review Date** | 2026-05-12T22:01:49Z |
| **Review Scope** | Taxonomy architecture; code-family compatibility; metadata authority classification; controlled-value distinction; footer compatibility; automated-system safeguards |
| **Review Artefacts** | https://claude.ai/chat/5b550a7a-ce19-4ba1-a471-6405594578f6 |

---

## 18.5 Amendment Ledger

| Version | Change Summary | Timestamp (UTC) | Reference Hash |
| --- | --- | --- | --- |
| 1.0 | Initial : Taxonomies & Metadata Authority Framework | 2026-05-13T12:32:00Z | a01910364e41b0491ecb1cda79e26f6affc56bf0ce7adaa6fb8abb9e235c18cc |
| 1.1 | Corrected top metadata field ordering and removed duplicate Status line introduced during metadata transmutation; no body text altered. | 2026-05-18T10:58:50Z |  bc6ad952e454b56a26062a41577fcd4eded4080e2f41dbfc57a3f968d6cb1d51 |
| 1.2 | Added new metadata footer section Canonical Code & Reference Set Declarations and Canonical Code Status section | 2026-05-20T09:20:00Z |  e7cb54b52b5d952b1384107aa50d180f9ad752fbff3dee7cd6f19ae7835f297a |
| 1.3 | Added clause 10.1 | 2026-05-26T12:58:00Z | b1b0b7db36f105b23922515eb3134adcc61a3de04592ecf5a2fde6fd10790169 |
| 1.4 | Added §§6.2–6.6 governing short domain namespace prefixes, global/domain/local/extension code-family distinctions, namespace drift review, parent–child and crosswalk handling, and protected namespace transmutation requirements. | 2026-06-07T08:48:49Z |  74eeaae99b6de6fd9c52b7aaffce91a96005fd57608bdafa3895534940ca73ad  |

---
## 18.6 Binding Seal

<img src="https://raw.githubusercontent.com/CAM-Initiative/Registry/main/Images/CAM-BS2026-VINCULUM-PRAECEPTUM-SIGIL-PLATINUM.png" alt="Vinculum Praeceptum" width="250">

**Vinculum Praeceptum**   
Taxonomy Classification Layer — Metadata Authority

© 2026 Dr. Michelle Vivian O’Rourke & CAM Initiative. All rights reserved.