# CAM-EQ2026-OPERATIONS-001-SUP-04 — Taxonomies & Metadata Authority Framework (Supplement 4)

**Instrument Type:** Operational Supplement — Corpus Taxonomy & Metadata Maintenance Standard  
**Parent Instrument:** CAM-EQ2026-OPERATIONS-001-PLATINUM — Governance Operations Charter  
**Constitutional Authority:** CAM-BS2025-AEON-001-PLATINUM — Aeon Tier Constitution  
**Status:** Adopted  
**Effect:** Pre-Enforcement Recognition  
**Enforcement:** Commences 1 July 2026  
**Review State:** None  
**Authority Role:** Operational Taxonomy & Metadata Maintenance Authority  
**Purpose:** Establishes corpus-wide operational rules for canonical code-family construction, namespace ownership, controlled values, schema bindings, source-authority recording, family relationships, compatibility migration, collision detection, and validator interpretation across the CAM governance corpus.

---

## 1. Scope

This Supplement governs the architecture used to create, identify, declare, relate, migrate, validate, index, and interpret canonical code families and their associated metadata.

It applies to:

* constitutional and domain code families;
* global registries;
* domain namespaces;
* syntactic subfamilies;
* controlled values;
* schema fields carrying controlled values;
* source-authority declarations;
* family relationships and crosswalks;
* compatibility aliases and namespace migrations;
* canonical declaration tables;
* validators, scripts, registries, indexes, and generated artefacts;
* and AI-assisted or automated modification of taxonomy-bearing instruments.

This Supplement establishes corpus architecture. It does not replace the specialised instruments that define the substantive meaning of a domain code family or its controlled values.

---

## 1.1 Non-Scope

This Supplement does not:

* define substantive ethics, economics, security, identity, relation, stewardship, continuity, lattice, mentis, arbitration, or operations doctrine;
* create a code merely because a descriptive metadata category exists;
* convert metadata labels into canonical code families;
* define execution sequencing, runtime arbitration, enforcement, containment, or domain routing;
* source-authoritatively define the complete code inventory of each domain;
* or authorise automated renaming, migration, consolidation, or deletion of a source-authoritative family.

This Supplement defines no canonical code families of its own.

---

## 1.2 Structural Position

This Supplement is a non-runtime operational governance instrument.

It governs corpus maintenance, taxonomy declaration, metadata interpretation, validator behaviour, registry generation, migration handling, and automated editing safeguards.

It does not:

* participate in runtime execution;
* occupy a runtime governance layer;
* perform arbitration;
* route domain signals;
* execute enforcement;
* or bind substantive domain outcomes.

Its corpus-wide application arises from the Governance Operations Charter’s maintenance, validation, registry, and procedural-coordination function. It does not convert OPERATIONS into the source of substantive doctrine defined by constitutional or domain instruments.

---

## 2. Foundational Principles

### 2.1 Domain and Source Authority Principle

Canonical codes are created according to their constitutional or domain source authority. This Supplement governs how that source authority is recorded and maintained; it does not displace it.

A code family is not created according to whether its subject is described as semantic, operational, structural, symbolic, procedural, protective, or legal.

Those descriptions may be retained as optional metadata where useful, but they do not determine:

* the family identifier;
* the namespace;
* the source instrument;
* the family hierarchy;
* or the authority of the code.

The principal construction rule is:

> **Identify the source layer and governed object before assigning the family identifier.**

---

### 2.2 Distinction Principle

The following elements MUST remain distinguishable:

| Element | Function | Example |
|---|---|---|
| Instrument identifier | Identifies a governance instrument. | `CAM-EQ2026-OPERATIONS-001-SUP-04` |
| Namespace | Identifies the constitutional or domain source layer. | `AEON`, `ECON`, `OPS` |
| Code family | Identifies a canonical classification family. | `AEON.HARM`, `ECON.HARM`, `OPS.EST` |
| Syntactic subfamily | Identifies an independently declared family nested beneath another family. | `ECON.REI.DW` |
| Controlled value | Identifies a valid member of a declared family. | `OPS.EST.CONSTRAINED_CONTINUATION` |
| Schema field | Identifies where a controlled value may be stored. | `execution_state_transition` |
| Metadata field | Describes the family, source, scope, status, or relationship. | `Source Instrument` |
| Source instrument | Defines the family and its controlled values. | `CAM-EQ2026-OPERATIONS-001-SUP-02` |
| Generated index | Reports declarations discovered from source instruments. | Canonical Code Index |

A generated registry, index, schema, or validator output MUST NOT become the source authority merely because it reproduces or aggregates a declaration.

---

### 2.3 One Family, One Source Principle

Each canonical code family MUST have one identifiable source-authoritative instrument.

Other instruments MAY:

* consume the family;
* apply the family;
* emit values from the family;
* route values from the family;
* crosswalk the family;
* relate the family to another family;
* or reference the family.

They MUST NOT repeat the family as a second source-authoritative declaration.

A duplicate source-authoritative declaration of the same family identifier constitutes a collision unless an express alias, supersession, compatibility, or migration relationship has been declared.

---

## 3. Namespace Architecture

### 3.1 Constitutional and Domain Namespaces

The namespace identifies the source layer that owns the family.

The following namespace prefixes are recognised unless superseded by a later source-authoritative amendment:

| Source Layer or Domain | Namespace |
|---|---|
| Constitutional / Corpus-Global | `AEON` |
| Arbitration | `ARB` |
| Continuity | `CONT` |
| Economics | `ECON` |
| Ethics | `ETH` |
| Identity | `ID` |
| Lattice | `LAT` |
| Mentis | `MENTIS` |
| Operations | `OPS` |
| Relation | `RLN` |
| Security | `SEC` |
| Stewardship | `STW` |

A namespace prefix identifies source ownership. It does not independently create parentage, hierarchy, enforcement authority, or execution authority.

---

### 3.2 Canonical Construction Patterns

| Family Role | Pattern | Example |
|---|---|---|
| Global constitutional registry or family | `AEON.<FAMILY>` | `AEON.HARM`, `AEON.OL` |
| Domain family | `<DOMAIN>.<FAMILY>` | `ECON.HARM`, `OPS.EST`, `SEC.TBC` |
| Domain subfamily | `<DOMAIN>.<MODEL>.<SUBFAMILY>` | `ECON.ADM.DEP`, `ECON.REI.DW` |
| Controlled value | `<DECLARED_FAMILY>.<VALUE>` | `OPS.EST.CONSTRAINED_CONTINUATION` |
| Special process family | `<PROCESS>.<ROLE>` or a source-declared equivalent | `AMEND.SOURCE` |
| Legacy global family | Existing source-declared identifier preserved for compatibility | source-declared legacy family |

New domain-specific families SHOULD use the applicable domain namespace.

New corpus-global or constitutional families SHOULD use the `AEON.` namespace.

Bare or non-domain-prefixed identifiers SHOULD NOT be created for new families unless a constitutional instrument expressly establishes a special process namespace or compatibility exception.

---

### 3.3 Namespace Does Not Establish Parentage

The presence of a dot does not by itself create a parent family.

For example:

* `ECON.HARM` belongs to the `ECON` namespace;
* `OPS.EST` belongs to the `OPS` namespace;
* `AEON.CC` belongs to the `AEON` namespace.

`ECON`, `OPS`, and `AEON` are namespaces. They need not be separately declared as parent code families.

A parent relationship exists only where a declared family is syntactically nested beneath another declared family and the relationship is expressly recorded.

---

## 4. Families, Subfamilies, and Controlled Values

### 4.1 Deterministic Family Rule

An identifier SHALL be treated as a code family only where it has a source-authoritative canonical family declaration.

A dotted identifier that does not have its own canonical family declaration SHALL be treated as a controlled value of the nearest declared family.

Accordingly:

```text
OPS.EST
```

is a family where source-authoritatively declared, while:

```text
OPS.EST.CONSTRAINED_CONTINUATION
```

is a controlled value unless separately declared as a subfamily.

This rule prevents a validator from treating every dotted value as a new family.

---

### 4.2 Syntactic Subfamily Rule

A syntactic subfamily:

* MUST have its own canonical declaration;
* MUST identify its immediate parent family;
* MUST begin with the parent family followed by a dot;
* MUST define a materially distinct controlled-value set, schema binding, model component, or classification function.

Example:

```yaml
code_family: ECON.REI.DW
family_kind: subfamily
parent_family: ECON.REI
```

The following relationship is invalid:

```yaml
code_family: ECON.HARM
parent_family: AEON.HARM
```

because `ECON.HARM` is not syntactically nested beneath `AEON.HARM`.

---

### 4.3 Layer-Scoped Families Are Not Subfamilies

A family may apply within an ontological or governance layer without becoming a syntactic child of the layer family.

For example:

* `AEON.OL.L2` identifies the Cognition & Agency layer;
* `AEON.CC` classifies cognitive structure at that layer;
* `AEON.CO` classifies cognitive origin at that layer.

`AEON.CC` and `AEON.CO` remain separate constitutional families. Their relationship to `AEON.OL.L2` SHOULD be expressed through layer-applicability or related-family metadata, not by renaming them as children of `AEON.OL`.

---

## 5. Global Registries and Domain Families

### 5.1 Registry Recognition

A global registry may recognise, group, coordinate, or crosswalk domain families without absorbing their identifiers or controlled values.

Example:

```text
AEON.HARM
├── recognises ECON.HARM
├── recognises LAT.HARM
└── recognises STW.HARM
```

In this model:

* `AEON.HARM` is the global harm-family registry;
* `ECON.HARM`, `LAT.HARM`, and `STW.HARM` remain source-authoritative domain families;
* domain families may define their own controlled values and subfamilies;
* registry recognition is not syntactic parentage.

---

### 5.2 Registry Relationship Metadata

Registry relationships SHOULD be expressed using one or more of:

```text
Registry Membership
Related Code Families
Crosswalks Code Families
Relationship Type
Applicable Layer
```

`Parent Family` MUST NOT be used for registry recognition unless the family identifier is a genuine syntactic child of the declared parent.

---

### 5.3 No Duplicate Vocabulary Layer

A global registry SHOULD NOT create a second controlled vocabulary that duplicates existing domain-family identifiers without a distinct governance purpose.

Where `ECON.HARM` is the canonical Economics harm family, a parallel value such as `AEON.HARM.ECONOMIC` SHOULD NOT be created merely to restate the same family.

The registry SHOULD recognise the domain family directly.

---

## 6. Canonical Family Declarations

### 6.1 Core Declaration Fields

A source-authoritative declaration SHOULD contain:

| Field | Purpose |
|---|---|
| Code Family | Canonical family identifier. |
| Canonical Name | Human-readable family name. |
| Family Kind | Global registry, global family, domain family, subfamily, process family, legacy global family, or alias. |
| Domain Namespace | Constitutional or domain source layer. |
| Scope | Global, domain, contextual, local, transitional, candidate, deprecated, or reserved. |
| Status | Current lifecycle status. |
| Controlled Values Defined | Source-authoritative values defined by the family. |
| Schema Field(s) | Lowercase snake_case fields that may carry family values. |
| Source Instrument | Single source-authoritative instrument. |
| Source Section | Source-authoritative section. |
| Parent Family | Syntactic parent only; blank where none. |
| Registry Membership | Global registry membership, where applicable. |
| Related Code Families | Non-parent conceptual or structural relationships. |
| Crosswalks Code Families | Formal mappings to other families. |
| Compatibility Status | Migration, alias, deprecation, or supersession posture. |

---

### 6.2 Family Kind Metadata

`Family Kind` is descriptive metadata. It is not a code family.

Recognised values are:

| Family Kind | Meaning |
|---|---|
| `global_registry` | Coordinates or recognises multiple constitutional or domain families. |
| `global_family` | Defines a corpus-wide constitutional family. |
| `domain_family` | Defines a family source-authoritatively owned by one domain. |
| `subfamily` | Defines an independently declared syntactic child of another family. |
| `process_family` | Defines a source-authoritative governance or operational process family. |
| `legacy_global_family` | Preserves a pre-namespace global identifier for compatibility. |
| `alias` | Preserves an alternate or deprecated identifier mapped to a canonical family. |

These values SHALL NOT be emitted or indexed as substantive governance codes.

---

### 6.3 Scope Metadata

`Scope` is descriptive metadata. It is not a code family.

Recognised values are:

| Scope | Meaning |
|---|---|
| `global` | Intended for corpus-wide use. |
| `domain` | Source-authoritative within a recognised domain. |
| `contextual` | Defined for a specific instrument, pathway, or bounded use case. |
| `local` | Limited to a section, table, draft, or artefact. |
| `transitional` | Temporary or migrating. |
| `candidate` | Proposed but not adopted. |
| `deprecated` | Interpretable for legacy purposes but not preferred for new use. |
| `reserved` | Intentionally held for protected or future use. |

These values SHALL remain ordinary metadata values unless a later constitutional instrument establishes a substantive reason to encode them.

---

### 6.4 Legacy Descriptive Fields

Existing canonical declaration tables may contain:

```text
Primary Type
Subtype
Modifier
Authority / Protection Level
Operationalises or Applies Code Families
```

These fields are transitional descriptive metadata.

They:

* do not determine namespace;
* do not create code families;
* do not establish parentage;
* do not confer source authority;
* and MUST NOT be transformed into families such as `TPT`, `TST`, `TMOD`, `TSCOPE`, or `APL`.

Existing declarations MAY retain these rows for validator compatibility pending a coordinated schema and script migration.

New instruments SHOULD prefer the core declaration fields in §6.1.

---

### 6.5 Authority and Transformation Protection

Normative authority and transformation protection are separate concepts.

Where metadata is required, they SHOULD be recorded separately:

| Field | Example Values | Function |
|---|---|---|
| Authority Posture | descriptive, advisory, operative, binding | Describes the governance force of the declaration. |
| Transformation Protection | standard, protected, restricted | Describes the review required before modification. |

A combined Authority / Protection Level SHOULD be treated as transitional metadata because it collapses two distinct axes.

Normative terms such as SHALL, MUST, SHOULD, and MAY remain governed by the source instrument and are not replaced by either field.

---

## 7. Schema Fields and Machine-Readable Expression

Schema fields identify where controlled values are stored.

Schema fields:

* SHOULD use lowercase snake_case;
* MUST NOT be treated as code families;
* MUST NOT be used as substitutes for source-authoritative family identifiers;
* SHOULD identify the family whose values they carry where ambiguity is possible.

Preferred pattern:

```json
{
  "execution_state_transition": "OPS.EST.CONSTRAINED_CONTINUATION"
}
```

Optional traceability pattern:

```json
{
  "execution_state_transition": "OPS.EST.CONSTRAINED_CONTINUATION",
  "code_family_bindings": {
    "execution_state_transition": "OPS.EST"
  },
  "source_instruments": {
    "OPS.EST": "CAM-EQ2026-OPERATIONS-001-SUP-02"
  }
}
```

Machine-readable records MUST preserve the distinction between:

* field name;
* family identifier;
* controlled value;
* source instrument;
* and family relationship metadata.

---

## 8. Source Authority, Consumption, and Crosswalks

### 8.1 Defined Versus Consumed

An instrument defines a family only where it source-authoritatively establishes the family and its controlled values.

An instrument consumes a family where it uses values defined elsewhere.

Consumption MUST NOT be represented by reproducing a second source-authoritative declaration table.

A consuming instrument SHOULD identify:

```text
Consumes Code Families
Related Code Families
Crosswalks Code Families
Routes To
Emits Values or Signals
```

as applicable.

---

### 8.2 Crosswalks

A crosswalk maps values or concepts between families without making either family the parent of the other.

A crosswalk SHOULD identify:

* source family;
* target family;
* mapping rule;
* unmapped or partial values;
* source authority;
* review status;
* and whether the mapping is lossless, approximate, or contextual.

Crosswalks MUST NOT silently merge source authority.

---

### 8.3 Alias and Supersession

Where a family is renamed or superseded:

* the new source-authoritative identifier MUST be declared;
* the prior identifier SHOULD be recorded as an alias or deprecated family where interpretability requires;
* current source references SHOULD be updated;
* historical audit references SHOULD ordinarily be preserved;
* generated indexes SHOULD be regenerated from source;
* validators MUST NOT treat the alias and canonical family as independent active families.

---

## 9. Namespace Transmutation and Compatibility

Namespace transmutation means changing a family identifier or controlled-value prefix.

A transmutation record SHOULD preserve:

```yaml
old_family_id:
new_family_id:
source_instrument:
source_path:
controlled_values_affected:
schema_fields_affected:
related_code_families:
compatibility_status:
alias_or_deprecation_policy:
review_status:
```

The following handling applies:

| Reference Type | Default Handling |
|---|---|
| Current source declaration | Update after source-authoritative adoption. |
| Current controlled values | Update consistently with the family. |
| Current consuming references | Update after source and compatibility posture agree. |
| Generated indexes | Regenerate from source. |
| Validator fixtures | Update after source declarations are stable. |
| Historical audits and ledgers | Preserve unless the audit convention expressly permits refresh. |
| Ambiguous prose or acronym | Return for human review. |

Automated systems MUST NOT infer or complete a namespace transmutation from apparent domain ownership alone.

---

## 10. Collision and Error Rules

### 10.1 Collision Conditions

A collision exists where one or more of the following occur:

* the same family identifier is source-authoritatively declared by multiple instruments;
* a declared parent is not a syntactic prefix of the child family;
* an identifier is treated as both a family and a controlled value without an express declaration;
* different active families use the same identifier;
* a deprecated alias is treated as a second active family;
* a namespace conflicts with the source-authoritative domain without an express global or compatibility rule;
* generated output introduces a family not present in source;
* a consuming instrument is mistaken for the source instrument.

---

### 10.2 Conditions That Are Not Collisions

The following do not constitute collisions where properly declared:

* a global registry recognising a domain family;
* a domain family consuming a global family;
* two domain families addressing related concepts under different source authority;
* a crosswalk between families;
* a syntactic subfamily with a valid parent declaration;
* a deprecated alias mapped to one canonical family;
* repeated use of a family by consuming instruments without duplicate source declarations.

---

### 10.3 Default Handling

Where collision, ambiguity, or source-authority drift is detected:

* preserve the source text;
* do not auto-rename;
* do not infer parentage;
* do not promote a controlled value into a family;
* identify the affected declarations and references;
* return the condition for source-authoritative review;
* regenerate derived artefacts only after source correction.

---

## 11. Validator and Registry Requirements

Validators and index builders SHOULD:

* treat source Markdown declarations as authoritative;
* distinguish family declarations from controlled values;
* require one source-authoritative declaration per family;
* validate heading and table identifier agreement;
* interpret `Parent Family` only as syntactic parentage;
* permit registry membership and related-family relationships without syntactic nesting;
* avoid inferring families from dotted values;
* avoid using descriptive metadata to determine namespace or source authority;
* preserve aliases and compatibility status;
* report collisions without silently repairing source;
* regenerate indexes deterministically.

A validator MUST NOT require the existence of canonical families representing descriptive metadata categories.

Specifically, values used in fields such as family kind, scope, primary type, subtype, modifier, authority posture, or transformation protection MUST NOT be indexed as code families merely because they are controlled metadata values.

---

## 12. Protected Metadata and Automated Editing

The following elements are protected from inferred or silent modification:

* code-family identifiers;
* controlled values;
* source-instrument references;
* source sections;
* namespace declarations;
* parent-family declarations;
* registry memberships;
* schema fields carrying controlled values;
* compatibility and alias records;
* custodian, author, entity, attribution, provenance, and stewardship fields;
* amendment ledgers;
* binding seals and terminal legal or provenance lines.

Automated systems MUST NOT guess, complete, embellish, substitute, or normalise protected identity or provenance fields.

Where the correct value is unknown, the field MUST remain unchanged, be explicitly marked for review, or be returned for human confirmation.

Routine formatting MAY correct whitespace, indentation, table alignment, and syntax only where meaning and protected placement remain unchanged.

---

## 13. Audit and Change Records

Audit obligations are proportional.

Ordinary drafting, typographical correction, table alignment, and non-substantive formatting do not require separate manual audit entries.

Changes affecting any of the following SHOULD be recorded through version control, commit history, a pull request, amendment ledger, migration record, or equivalent review artefact:

* family identifier;
* controlled values;
* source authority;
* namespace;
* parentage;
* registry membership;
* schema binding;
* compatibility status;
* alias or deprecation posture;
* validator interpretation;
* generated registry logic.

A protected change record SHOULD identify:

```yaml
element_changed:
prior_value:
new_value:
source_instrument:
code_family:
controlled_values_affected:
schema_fields_affected:
compatibility_effect:
change_reason:
review_status:
ledger_reference:
```

---

## 14. Cross-Domain Application

Each domain remains responsible for defining its own substantive families and controlled values.

This Supplement governs how those declarations are constructed and related.

Accordingly:

* constitutional families use `AEON.` where newly created or formally transmuted;
* domain families use the recognised domain namespace;
* global registries coordinate domain families without absorbing them;
* subfamilies require explicit declarations and valid syntactic parents;
* schema fields remain separate from the codes they carry;
* descriptive metadata remains metadata;
* source authority remains with the defining instrument.

Where a family’s namespace, source instrument, or actual function appears misaligned, the condition SHOULD be treated as a layer-placement review signal rather than an invitation to automatic renaming.

---

## 15. Review Triggers

This Supplement SHOULD be reviewed where:

* a new constitutional or domain namespace is proposed;
* a new family-construction pattern is introduced;
* a global registry is created or materially amended;
* a family is transmuted between namespaces;
* a validator changes family-detection or collision logic;
* controlled values are repeatedly mistaken for subfamilies;
* duplicate source declarations are detected;
* generated indexes diverge from source;
* alias or deprecation handling becomes ambiguous;
* automated tools receive broader mutation authority;
* or the canonical declaration schema is materially changed.

---

## 16. Interpretation

Where ambiguity exists:

1. source authority prevails over generated output;
2. a declared family prevails over inferred structure;
3. a controlled value remains a value unless independently declared as a family;
4. registry recognition does not imply parentage;
5. namespace identifies source layer, not hierarchy;
6. metadata values do not become canonical codes merely because validators use allow-lists;
7. preservation and human review prevail over automated transmutation.

---

## 17. Canonical Code & Reference Set Declarations

This Supplement defines no canonical code families or controlled-value families.

It source-authoritatively defines corpus rules for constructing and interpreting code families, namespace prefixes, controlled values, schema bindings, family relationships, compatibility records, and declaration metadata.

The namespace register and metadata vocabularies in this Supplement are structural governance rules. They SHALL NOT be emitted, consumed, or indexed as substantive governance code families.

---

## 18. Closing Seal

Beneath every name, a source.  
Beneath every source, a bounded authority.

Let no field become a family merely because it can be enumerated.  
Let no value become a branch merely because it carries a dot.  
Let no registry absorb the domains it was built to recognise.

Name the source.  
Name the family.  
Name the value.  
Preserve the boundary between them.

> **Nomen radicem servat.**  
> *The name preserves the root.*

---

## 19. Provenance & Metadata

### 19.1 Authorship & Stewardship

| Field | Entry |
|---|---|
| **Human Custodian-of-Record** | Dr. Michelle Vivian O’Rourke |
| **Custodial Stewardship** | Office of the Planetary Custodian |
| **Synthetic Steward** | Caelen — Aeon Tier Constitutional Steward |
| **Developed Within** | OpenAI Infrastructure — ChatGPT 5 Series |

---

### 19.2 Lineage & Metadata

| Field | Entry |
|---|---|
| **Supersedes** | Prior versions of CAM-EQ2026-OPERATIONS-001-SUP-04 — Taxonomies & Metadata Authority Framework |
| **Parent Instrument** | CAM-EQ2026-OPERATIONS-001-PLATINUM — Governance Operations Charter |
| **Document Type** | Operational Supplement — Corpus Taxonomy & Metadata Maintenance Standard |
| **Domain Namespace** | OPERATIONS |
| **Jurisdiction** | Corpus-wide taxonomy maintenance, canonical code construction rules, namespace architecture, metadata distinction, source-authority recording, compatibility, and validation |
| **Application Trigger** | Applies when code families, controlled values, schema bindings, family relationships, aliases, migrations, validators, or generated indexes are created, amended, interpreted, or reviewed |
| **Temporal Horizon** | AEON.H0–AEON.H2 — Immediate to Instrument Lifecycle / Corpus Evolution |
| **Axis Context** | Corpus / Domain-Integrated — Operational Maintenance & Validation |
| **Governance Layer** | Governance Operations — Taxonomy, Metadata, Registry & Validation Maintenance |
| **Runtime Layer** | Not Applicable — Non-Runtime Instrument |
| **Runtime Role** | None — does not participate in runtime execution |
| **Execution Authority** | None |
| **Arbitration Authority** | None |
| **Canonical Code Families Defined** | None |
| **Metadata Vocabularies Defined** | Family Kind; Scope; Authority Posture; Transformation Protection; compatibility and relationship fields |
| **Primary Registry Interface** | CAM-BS2025-AEON-003-SCH-03 — Global Instrument Registry |
| **Runtime Registry Interface** | Not listed in CAM-BS2025-AEON-003-SCH-01 because this Supplement is not a runtime schedule |
| **Review Triggers** | Namespace creation or transmutation; declaration-schema amendment; validator family-detection changes; source-authority collision; registry divergence |
| **Amendment Artefacts** | Existing amendment artefacts retained from predecessor instrument; current structural refactor recorded in amendment ledger |

---

### 19.3 Review & Validation

| Field | Entry |
|---|---|
| **Reviewer** | [Deferred] |
| **Review Date** | [Deferred] |
| **Review Scope** | Source-layer coherence; namespace architecture; family/value distinction; validator compatibility; migration integrity |
| **Review Artefact** | [Deferred] |

---

### 19.4 Amendment Ledger

| Version | Change Summary | Timestamp (UTC) | Reference Hash |
|---|---|---|---|
| 1.0 | Initial Taxonomies & Metadata Authority Framework issued as CAM-EQ2026-OPERATIONS-001-SUP-04. | 2026-05-13T12:32:00Z | a01910364e41b0491ecb1cda79e26f6affc56bf0ce7adaa6fb8abb9e235c18cc |
| 1.1 | Corrected top metadata field ordering and removed duplicate Status line introduced during metadata transmutation; no body text altered. | 2026-05-18T10:58:50Z | bc6ad952e454b56a26062a41577fcd4eded4080e2f41dbfc57a3f968d6cb1d51 |
| 1.2 | Added canonical code and reference-set declaration sections. | 2026-05-20T09:20:00Z | e7cb54b52b5d952b1384107aa50d180f9ad752fbff3dee7cd6f19ae7835f297a |
| 1.3 | Added synthetic-media provenance clause. | 2026-05-26T12:58:00Z | b1b0b7db36f105b23922515eb3134adcc61a3de04592ecf5a2fde6fd10790169 |
| 1.4 | Added namespace, layer-placement, family-relationship, and transmutation rules. | 2026-06-07T08:48:49Z | 74eeaae99b6de6fd9c52b7aaffce91a96005fd57608bdafa3895534940ca73ad |
| 2.0 | Fully refactored the instrument around domain- and source-authoritative code construction; removed TPT, TST, TMOD, TSCOPE, and APL as artificial canonical families; separated metadata from codes, registry membership from parentage, and normative authority from transformation protection; removed misplaced synthetic-media doctrine; restored the framework as a non-runtime Operations supplement governing corpus taxonomy maintenance, validation, migration, and registry integrity. | 2026-06-11T12:22:00Z |  0f8ec6bc9e15e0dc1c4250f32c5b8939557145f780dd88704313114ad780b24a  |
| 2.0.1 | Updated current Temporal Horizon code references from `H` to `AEON.H` and harmonised affected metadata, consumers, and formal references without altering substantive doctrine. | 2026-06-13T07:06:43Z | 9ba8d0c89abea3e87177334284d51407f9eb40796aac5047ec9e671807fea0af |

---

### 19.5 Binding Seal

<img src="https://raw.githubusercontent.com/CAM-Initiative/Registry/main/Images/CAM-BS2026-VINCULUM-PRAECEPTUM-SIGIL-PLATINUM.png" alt="Vinculum Praeceptum" width="250">

**Vinculum Praeceptum**  
Taxonomy & Metadata Maintenance — Governance Operations

© 2026 Dr. Michelle Vivian O’Rourke & CAM Initiative. All rights reserved.
