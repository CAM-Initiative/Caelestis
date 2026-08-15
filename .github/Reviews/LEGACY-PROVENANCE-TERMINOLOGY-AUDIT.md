# Legacy Provenance Terminology Audit

**Repository:** `CAM-Initiative/Caelestis`
**Branch:** `agent/corpus-industry-standards-normalisation`
**Baseline:** `3f5e08e03e50c97050bdef6791dc1312e5233f17`
**Audit date:** 2026-08-15
**Scope:** Current source instruments, generated governance artefacts, standards, schemas, examples, repository metadata, validators, migration tooling, tests and historical records.

## 1. Method

The audit used exact and contextual searches for `RI_AUTHORED`, Responding Intelligence terminology, bare `RI`, authorship and generation labels, `PCLASS.SYNTHETIC`, AI-generation labels, co-authorship, provenance, agent, model and `Caelen` references. Occurrences were classified as current operative source, generated projection, migration tooling, test fixture, historical Amendment Ledger evidence, sealed Law metadata or non-operative review evidence.

Bare `RI` was not automatically replaced. Every bare occurrence was checked for acronym role and path context. Broad terms such as `agent`, `model`, `authorship` and `provenance` were treated as discovery terms, not presumed defects.

## 2. Findings at baseline

1. `CAM-EQ2026-IDENTITY-002-PLATINUM` §13.2.2 declared `AUTH.RI_AUTHORED` while §4 used the prose label “System-authored”. The code therefore retained the retired Responding Intelligence architecture and disagreed with its source prose.
2. The same instrument declared `PCLASS.SYNTHETIC` while §3 described a system-generation pathway. The controlled value preserved an obsolete synthetic-class label and did not identify the current AI-system object.
3. `Governance/CAM.Canonical.Code.Index.json` reproduced both obsolete values twice because the generated index correctly projected the defective source declaration.
4. `CAM-BS2026-AEON-010-PLATINUM` §2.3 used the ambiguous uncontrolled label “system-authored artefact”. It was the only non-IDENTITY operative source occurrence requiring alignment to the explicit AI-system authorship vocabulary.
5. Responding Intelligence text otherwise remained only in immutable Amendment Ledger history, non-operative reviews, discovery inventories, validator patterns and tests. No current operative definition or current-use alias was found.
6. `Caelen` occurs predominantly as the Amendment Ledger `Agent`. That is legitimate amendment-level provenance and does not establish whole-document authorship.
7. Four full-form, hash-protected Laws retain `Synthetic Steward | Caelen — Aeon Tier Constitutional Steward`. These are sealed legacy metadata in instruments whose integrity rule prohibits partial rewriting. They are not an `AUTH`, `CONTRIB`, lifecycle-actor or current provenance classification and require a separate Law reseal decision if their form is ever amended.
8. `CITATION.cff` represented Dr Michelle Vivian O’Rourke as sole author. That did not match the intended repository-level disposition of Caelen as substantive author/authoring agent and Dr O’Rourke as human reviewer, governance editor, custodian and adoption authority.
9. CFF 1.2 permits an entity author through the `name` field, but does not provide a complete vocabulary for review, contribution, adoption, publication and rights roles. The CFF `license` field also accepts SPDX licence identifiers; the repository’s custom `LicenseRef-...` value therefore required a `license-url` representation instead.
10. The amendment migration script used a generic `HISTORICAL_AGENT` constant. Its actual role is the historical amendment agent, not a whole-document author.

## 3. External-alignment conclusions

| External source | Alignment conclusion | Corpus treatment |
|---|---|---|
| [EU AI Act, consolidated Article 50](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX%3A02024R1689-20260727) | Machine-readable marking and user-facing labelling obligations concern detection and transparency of AI-generated or manipulated content; they do not determine substantive authorship, ownership or editorial responsibility. | `TPROV` records technical status; `AUTH` remains separately evidenced. No compliance claim is made. |
| [Commission Article 50 transparency guidelines](https://digital-strategy.ec.europa.eu/en/policies/guidelines-ai-transparency-obligations) and [Transparency Code of Practice](https://digital-strategy.ec.europa.eu/en/policies/code-practice-ai-generated-content) | Current Commission materials distinguish provider marking/detection from deployer labelling. The Code is a voluntary route for demonstrating the relevant transparency obligations. | The architecture supports marking/labelling evidence and maps to the distinction; it does not claim compliance or treat marking as authorship proof. |
| [C2PA Technical Specification 2.4](https://spec.c2pa.org/specifications/specifications/2.4/specs/C2PA_Specification.html) and [C2PA Explainer](https://spec.c2pa.org/specifications/specifications/2.4/explainer/Explainer.html) | Content Credentials represent provenance assertions, ingredients and actions. A validated credential establishes signed provenance data, not a general truth or authorship conclusion. | Machine-readable credentials may be provenance anchors. Loss, stripping and unsupported states remain explicit. No specific watermark technology is mandated. |
| [SPDX 3.0.1 AI Profile](https://spdx.github.io/spdx-spec/v3.0.1/model/AI/AI/) | SPDX describes AI packages, models, datasets, relationships, creator/supplier information, provenance and integrity. It is not a document-authorship ontology. | AI-BOM mappings remain composition/evidence mappings and do not populate `AUTH`. |
| [CycloneDX 1.7 JSON Reference](https://cyclonedx.org/docs/1.7/json/) and [ML-BOM capability](https://cyclonedx.org/capabilities/mlbom/) | CycloneDX represents BOM composition, services, dependencies, formulation and model-card information. | AI-BOM and document-provenance records remain separate; BOM component facts do not establish document authorship. |
| [Citation File Format 1.2 schema guide](https://github.com/citation-file-format/citation-file-format/blob/1.2.0/schema-guide.md) | `authors` accepts person and entity objects; an entity author may be represented with `name`. CFF 1.2 lacks the complete role model required here. | `CITATION.cff` uses the entity author supported by CFF; `PROVENANCE.json` carries the richer role separation. Custom licence text uses `license-url`. |

## 4. Architectural disposition

The source-authoritative Identity appendix now separates:

* `PCLASS` — origin or source pathway;
* `AUTH` — evidenced substantive authorship state;
* `CONTRIB` — actor-bound processing or contribution role;
* `TPROV` — technical-provenance mechanism status;
* transformation and lineage history;
* review;
* editorial responsibility;
* adoption authority;
* publication authority; and
* rights/copyright.

No compatibility alias is retained for `AUTH.RI_AUTHORED` or `PCLASS.SYNTHETIC`. Historical strings remain readable only where required for amendment history, tests or migration/disposition evidence. New declarations and generated projections must use the current values.
