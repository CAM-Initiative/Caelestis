# AI-BOM Readiness Assessment

## Determination

Caelestis is **conceptually ready but not implementation-ready** for an externally inspectable AI-BOM.

Annex B already requires an AI Architecture Bill of Materials (`AI-ABOM`) at a defined time and requires materially richer information than a conventional component list. It covers the deployed formation: model and provider, lineage, configuration, routing, harness, memory, tools, permissions, credentials, environment, interfaces, classifiers, controls, monitoring, human gates, actor roles, jurisdiction, dependencies, changes and unresolved architecture.

That is a strong governance model. It is not yet a portable data product.

---

## Readiness matrix

| Capability | Current position | Assessment | Required before an external claim |
| --- | --- | --- |
| Governance scope | Annex B §§12–12.4 | Strong | Retain the broader deployed-formation scope. |
| Evidence status | declared / observed / inferred / unresolved | Strong | Define per-field provenance mechanics and confidence handling. |
| Incident-time reconstruction | Required in Annex B; runtime identity strengthened in OPERATIONS-007 | Strong conceptually | Define snapshot identity, effective-time semantics and retention/disposition profile. |
| Model and dataset description | Required where applicable | Partial | Map fields to SPDX AI/dataset profiles and CycloneDX ML-BOM model/dataset components. |
| Dependencies and composition | Required conceptually | Partial | Model graph relationships, nested BOMs and external references using established exchange primitives. |
| Runtime, tooling and credentials | Required conceptually | Partial | Define safe identifier handling, redaction, protected references and verifier access pathways. |
| Embodiment and hardware | Addressed in draft STEWARD-005 and identity instruments | Partial | Decide adopted stewardship posture and map to hardware/operations BOM material where relevant. |
| Serialisation and exchange | None | Gap | Select JSON-LD / SPDX / CycloneDX profile architecture and publish schemas. |
| Validation and test fixtures | Corpus validators only | Gap | Publish schema validation, reference validation, test fixtures and version-compatibility checks. |
| Conformance and assurance | No deployment assessment profile | Gap | Define evidence requirements without asserting provider or runtime conformance. |

---

## Recommended architecture

The future AI-ABOM should be a **CAM governance extension and profile**, not a competing universal BOM format.

1. Use SPDX 3 AI and dataset profiles for portable component, dataset and relationship description.
2. Use CycloneDX ML-BOM, SaaSBOM, HBOM or OBOM structures where the deployment requires their respective lifecycle information.
3. Add a clearly namespaced CAM extension only for governance-specific fields that the external specifications do not carry: authority boundary, evidence posture, constraint/continuation state, custody, incident-time governance snapshot, and protected-reference access pathway.
4. Preserve separate identifiers for a model, model instance, deployed formation, agent process, physical substrate and continuity-bearing layer. Never treat an AI-BOM identifier as an entity-identity determination.
5. Require a versioned profile, sample records, protected-record pattern, schema validator and compatibility policy before representing AI-ABOM as interoperable.

---

## Non-claims

This assessment does not claim that CAM emits SPDX or CycloneDX, that any AI deployment conforms to CAM, or that an AI-BOM establishes legal status, safe deployment, authority, or identity continuity.
