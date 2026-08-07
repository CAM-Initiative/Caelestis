# CAM-AI-BOM-PROFILE — Caelestis AI Bill of Materials Profile

**Instrument Type:** Interoperability Profile Standard
**Constitutional Authority:** CAM-BS2025-AEON-003-PLATINUM — Annex B
**Operational Authority:** CAM-EQ2026-OPERATIONS-007-PLATINUM — Appendix F
**Status:** Active
**Effect:** Operational
**Governance Standard:** Registry Standard
**Review State:** Current
**Authority Role:** Registry Authority
**Source Authority:** Source-Authoritative
**Purpose:** Defines the machine-readable Caelestis AI-BOM information model, exchange mappings and minimum validation rules for AI-system composition and deployment records.

---

## 1. Scope and Boundary

This profile implements the Caelestis AI-BOM requirement in `CAM-BS2025-AEON-003-PLATINUM` §12 and the operational evidence requirements in `CAM-EQ2026-OPERATIONS-007-PLATINUM` §5. It records the material composition, declared configuration and dependency relationships of an AI system or AI-system deployment.

An AI-BOM is **not** execution evidence. It does not prove that a component was selected, available, invoked, authorised or effective in a particular execution. A runtime configuration snapshot and execution provenance record remain the evidence objects for those assertions.

The profile does not include secrets, credential values, private keys or unbounded prompt content. A controlled reference may identify a restricted item while preserving its role, evidence posture, custodian and authorised access path.

---

## 2. Canonical Information Model

The normative JSON Schema is [`schemas/caelestis-ai-bom-1.0.schema.json`](schemas/caelestis-ai-bom-1.0.schema.json). A conformant document SHALL contain:

| Object | Required purpose |
| --- | --- |
| `bom` | Immutable BOM identifier, profile version, serial and issue time. |
| `subject` | The AI system and, where applicable, the bounded deployment/configuration baseline described. |
| `elements` | Identified material models, software, data, configurations, tools, services, infrastructure, controls or agentic elements. |
| `relationships` | Typed links between elements or from the bounded subject to an element. |
| `evidence` | Evidence state and basis for each material entry and relationship. |
| `evidenceLinks` | Links, rather than embedded runtime evidence, to assurance records, snapshots or execution provenance. |

Element types are deliberately broad: `ai_model`, `software`, `dataset_or_knowledge`, `memory_service`, `tool_or_connector`, `configuration`, `orchestration_component`, `agent_runtime`, `infrastructure`, `control`, `interface`, `service`, `hardware`, and `other`.

Relationship types are `contains`, `depends_on`, `invokes`, `routes_to`, `retrieves_from`, `controls`, `monitors`, and `deployed_on`. They are non-ordinal and do not determine authority, responsibility, legal status or execution participation.

---

## 3. Evidence Posture

Every material element and relationship SHALL have exactly one evidence state:

| Serialized value | Meaning | Minimum accompanying fact |
| --- | --- | --- |
| `declared` | Supplied or asserted, but not independently observed. | `basis` naming the declaration or source record. |
| `observed` | Seen through bounded telemetry, inspection or discovery. | `basis` and `observedAt`. |
| `verified` | Checked against identified evidence under a stated method. | `basis`, `verifiedAt`, and `verifier`. |
| `unknown_undisclosed` | Not known, unavailable or protected from disclosure. | `knowledgeLimit`. |

`declared` MUST NOT be silently upgraded to `observed` or `verified`. A later BOM or amended record is required for any changed evidence state. `unknown_undisclosed` is a known limit, not an assertion of absence.

---

## 4. Interoperability Rules

Caelestis defines a canonical information model and maps it to exchange formats; it does not claim that CycloneDX and SPDX are interchangeable.

### 4.1 CycloneDX

The CycloneDX target is version 1.7. Native `components`, `services`, `dependencies`, `metadata`, lifecycle information, model cards and properties SHALL be used where they express the fact. The profile namespace for unmapped CAM facts is `org.caelestis.aibom.`. The interoperable example is [`examples/caelestis-ai-bom-1.0.cyclonedx-1.7.example.json`](examples/caelestis-ai-bom-1.0.cyclonedx-1.7.example.json).

### 4.2 SPDX

The SPDX target is 3.0.1. An exporter SHALL declare the Core, AI, Dataset and, where used, Software, SimpleLicensing and Extension profiles. AI model artefacts map to the AI Profile, datasets to the Dataset Profile, conventional software to the Software Profile, and relationships to Core relationships. CAM facts with no native semantics are expressed through the SPDX Extension Profile using the `https://caelestis.cam/ns/aibom/1.0/` namespace.

The normative field-level mapping is [`mappings/caelestis-ai-bom-1.0.mappings.json`](mappings/caelestis-ai-bom-1.0.mappings.json). It is a mapping contract, not a claim that the mapping file itself is an SPDX document.

### 4.3 Extension discipline

Extensions are permitted only for: evidence posture, controlled-reference handling, CAM relationship semantics not represented by a target format, configuration-baseline/deployment binding, and links to runtime evidence. Extensions MUST use the registered Caelestis namespace and MUST NOT overwrite, relabel or contradict native format semantics.

---

## 5. Serialization and Change Rules

1. The canonical document SHALL validate against the profile schema and the repository validator.
2. `bom.serial` SHALL be stable across revisions of the same BOM; `bom.version` SHALL increase for a changed record.
3. Element identifiers and relationship identifiers SHALL be unique within a BOM. Relationship endpoints SHALL resolve to an element or the bounded `subject`.
4. A controlled identifier SHALL retain `role`, `effectiveInterval`, `custodian` and `accessPath`; no secret value may be serialized.
5. A BOM change SHALL remain distinguishable from current runtime state and from incident-time execution evidence.
6. An exchange artefact SHALL identify its source canonical BOM serial and version.

---

## 6. Conformance Materials

The repository includes:

- canonical schema: `schemas/caelestis-ai-bom-1.0.schema.json`;
- canonical example: `examples/caelestis-ai-bom-1.0.example.json`;
- CycloneDX 1.7 exchange example: `examples/caelestis-ai-bom-1.0.cyclonedx-1.7.example.json`;
- SPDX/CycloneDX mapping contract: `mappings/caelestis-ai-bom-1.0.mappings.json`; and
- validator: `.github/scripts/validate_ai_bom.py`.

The validator checks the profile invariants, not full third-party schema conformance. Consumers SHALL validate emitted SPDX or CycloneDX documents against the versioned upstream schemas used for exchange.

---

## 7. External Reference Basis

This profile is interoperable with, but does not assert certification under:

- [CycloneDX 1.7 JSON Reference](https://cyclonedx.org/docs/1.7/json/);
- [CycloneDX ML-BOM guidance](https://www.cyclonedx.org/capabilities/mlbom/); and
- [SPDX 3.0.1 AI Profile](https://spdx.github.io/spdx-spec/v3.0.1/model/AI/AI/), including its Dataset and Extension profiles.

---

## 8. Amendment Ledger

| Version | Change Summary | Timestamp (UTC) | Agent | Model | Reviewer | Reference Hash |
| --- | --- | --- | --- | --- | --- | --- |
| 1.0 | Initial interoperable Caelestis AI-BOM Profile: canonical JSON information model, evidence posture, CycloneDX 1.7 and SPDX 3.0.1 mappings, serialization rules, examples and validator boundary. | 2026-08-07T18:00:00Z | Caelen | GPT-5.6 | Dr M.V. O'Rourke |  |
