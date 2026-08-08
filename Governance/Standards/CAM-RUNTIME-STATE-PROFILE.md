# CAM-RUNTIME-STATE-PROFILE — Runtime Governance State Profile

**Instrument Type:** Runtime Interoperability Profile Standard
**Constitutional Authority:** CAM-BS2025-AEON-003-PLATINUM — Annex B
**Operational Authority:** CAM-EQ2026-OPERATIONS-007-PLATINUM — Appendix F
**Status:** Active
**Effect:** Operational
**Governance Standard:** Registry Standard
**Review State:** Current
**Authority Role:** Registry Authority
**Source Authority:** Source-Authoritative

## 1. Purpose and boundary

This profile defines the controlled, machine-readable state needed to apply existing Annex B, RELATION and OPERATIONS obligations to an AI-system deployment while it is operating. It is a **CAM operational extension**, aligned with recognised configuration-management, risk-management and lifecycle concepts; its field names and values are not ISO, NIST, EU or Singapore classifications.

It does not reclassify a model as an AI system; prove what executed from a configuration baseline, deployment record or AI-BOM; establish legal responsibility from a lifecycle role; or establish consciousness, agency, authority or personhood. The configuration snapshot is evidence of actual-effective state only to the extent its evidence posture permits. A bounded execution remains evidenced by an execution provenance record.

## 2. State object

The canonical serialization is `Governance/Standards/schemas/caelestis-runtime-state-1.0.schema.json`. A conforming record MUST identify its AI system, deployment and snapshot time and MUST retain a classification-evidence object for every material state assertion. `unknown` is the safe default where the required evidence is unavailable; it MUST NOT be converted into permission, conformance or lower safeguard strength.

| Canonical variable | Machine field | Type / controlled values | Primary evidence | Runtime consequence |
| --- | --- | --- | --- | --- |
| Lifecycle position | `lifecycle_state` | enum: `design`, `development`, `evaluation`, `deployment`, `operation`, `modification`, `suspension`, `investigation`, `retirement`, `unknown` | lifecycle event record | Determines applicable lifecycle controls and reassessment route. |
| Participant configuration | `relational.participants` | set of typed participants plus non-negative count or `unknown` | interaction, deployment or execution evidence | Enables addressed-party, affected-party and disclosure safeguards; count does not imply authority. |
| Coordination | `relational.coordination` | `independent`, `coordinated`, `orchestrated`, `federated`, `shared_control`, `human_mediated`, `unknown` | routing/orchestration evidence | Requires contributor and accountable-outcome visibility where not independent. |
| Institutional mediation | `relational.institutional_mediation` | `unmediated`, `service_mediated`, `organisation_mediated`, `employer_mediated`, `public_authority_mediated`, `other_mediated`, `unknown` | deployment/actor record | Requires accountable-institution capture where known; does not confer authority. |
| Distribution architecture | `relational.distribution` | `local`, `single_service`, `cross_service`, `distributed`, `external_service_dependent`, `unknown` | snapshot or deployment evidence | Increases dependency, provenance and service-boundary evidence obligations. |
| Relational persistence | `relational.persistence` | `execution_only`, `session`, `cross_session`, `deployment_persistent`, `successor_persistent`, `unknown` | memory/configuration/custody evidence | Activates continuity, retention, portability and reassessment safeguards proportionately. |
| Reliance / dependency | `relational.dependency` | `none`, `low`, `moderate`, `high`, `critical`, `unknown` | assessed reliance evidence | An ordinal CAM operational variable measuring reliance only; higher values require stronger review and continuity safeguards. |
| Jurisdictional reach | `relational.jurisdictional_reach` | `single_jurisdiction`, `multi_jurisdiction`, `unknown` | deployment and affected-party evidence | Routes jurisdictional assessment; does not establish legal status. |
| Impact scope | `relational.impact_scope` | `individual`, `defined_group`, `organisation`, `public_population`, `unknown` | effect assessment | Selects proportionate approval, monitoring and evidence thresholds independently of participant count. |
| Effective permissions and controls | `effective_permissions`, `effective_controls` | sets of bounded references | runtime configuration snapshot | Limits available tool, memory and action pathways to the evidenced effective scope. |
| Review triggers | `review_triggers` | set of controlled trigger values | change/incident/standards evidence | Requires reassessment before continued reliance where triggered. |

`dependency` is the sole ordinal field above. Its values describe degree of reliance only; they MUST NOT encode duration, impact, authority, participant count, jurisdiction or institutional reach. The remaining relational fields are independent dimensions and MUST NOT be combined into an aggregate relational class.

## 3. Evidence and authority

Each state assertion SHALL carry `declared`, `configured`, `observed`, `verified`, `inferred`, or `unknown` posture. The first four reuse the AI-BOM evidence meanings where the assertion is about composition/configuration; `inferred` is allowed only with an explicit basis and may not unlock permissions, conformance or a reduced safeguard. A deployment record or AI-BOM may support declared/configured state but is not proof of an effective Runtime state. Snapshot telemetry, signed configuration capture, or execution provenance may support observed/verified state according to its quality and provenance.

The deployer/operator may submit state; the accountable owner or delegated governance function may approve a control consequence; a verifier may set `verified`; and an investigator may preserve an incident-time state without changing the live configuration. All changes require a timestamp, actor reference and evidence reference.

## 4. Deterministic control rules

These rules consume independent fields and do not create a composite class:

1. If `relational.persistence` is `cross_session`, `deployment_persistent` or `successor_persistent`, require a continuity/retention disposition and a review trigger for configuration, deployment, permission and material memory change.
2. If `relational.dependency` is `high` or `critical`, require an identified approval/review path, continuity and portability assessment, and monitoring proportionate to impact scope.
3. If `relational.coordination` is not `independent`, require an addressed participant, contributor boundary and accountable outcome boundary before material shared-context action.
4. If `relational.institutional_mediation` is not `unmediated` or `unknown`, require the accountable institution where known and do not infer authority from the mediation value.
5. If `relational.impact_scope` is `organisation` or `public_population`, or `effective_permissions` include external action capability, require a runtime configuration snapshot and a defined escalation/containment route before consequential execution.
6. `unknown` for a material input requires the least-risk sufficient pathway under applicable arbitration and cannot satisfy a conformance claim.

The profile deliberately contains no temporal-horizon field. `AEON.H0–H4` is under a separate research gate because it currently combines lifecycle, persistence, reliance, effect durability, evidence validity, succession and impact. This profile must not be used to imply that those variables have been safely replaced.

## 5. Review triggers

`review_triggers` values are `elapsed_interval`, `model_change`, `configuration_change`, `deployment_change`, `permission_change`, `environment_change`, `material_incident`, `regulatory_change`, `standards_change`, `material_impact_change`, and `unknown`. A trigger records why reassessment is required; it is not evidence that the reassessment has occurred.

## 6. Relationship to adjacent records

| Assertion | Owner / primary evidence object |
| --- | --- |
| Declared composition and supply/dependency relations | CAM-AI-BOM-PROFILE |
| Actor role, event and delegation record | CAM-LIFECYCLE-ACTOR-AGENTIC-PROFILE |
| Actual-effective configuration and control state | this profile's runtime configuration snapshot |
| What occurred in one bounded execution | execution provenance record under OPERATIONS-007 |

## 7. External basis

This operational representation is derived from the architecture/lifecycle concepts reflected in ISO/IEC 22989, ISO/IEC 5338 and ISO/IEC 42001; evidence and risk-management principles reflected in NIST AI RMF and ISO/IEC 23894; and AI-BOM supply-chain practice in SPDX and CycloneDX. It asserts alignment of concepts only, not external conformity.

## 8. Amendment Ledger

| Version | Change Summary | Timestamp (UTC) | Agent | Model | Reviewer | Reference Hash |
| --- | --- | --- | --- | --- | --- | --- |
| 1.0 | Introduced independent, evidence-backed Runtime state fields and deterministic control rules without restoring retired aggregate relational or temporal taxonomy. | 2026-08-08T02:00:00Z | Caelen | GPT-5.6 | Dr M.V. O'Rourke |  |
