# CAM-LIFECYCLE-ACTOR-AGENTIC-PROFILE — Lifecycle Actor and Agentic Governance Profile

**Instrument Type:** Lifecycle Interoperability Profile Standard
**Constitutional Authority:** CAM-BS2025-AEON-003-PLATINUM — Annex B
**Operational Authority:** CAM-EQ2026-OPERATIONS-007-PLATINUM — Appendix F
**Status:** Active
**Effect:** Operational
**Governance Standard:** Registry Standard
**Review State:** Current
**Authority Role:** Registry Authority
**Source Authority:** Source-Authoritative
**Purpose:** Defines controlled lifecycle-actor roles and an agentic lifecycle record for AI systems, deployments and agents.

---

## 1. Scope and Non-Equivalence

This profile controls functional lifecycle roles and their records. A role assignment identifies a contribution, control capacity or evidence responsibility; it does not by itself establish legal liability, personhood, agency, fault, employment status, regulatory status or authority to act.

One entity MAY hold several roles. One role MAY be distributed across entities. The applicable context determines whether an organisation, natural person, system element, public authority or other entity can occupy a role. The record SHALL preserve uncertainty and contested assignments.

`CAM-BS2025-AEON-003-PLATINUM` defines the AI-system, deployment, runtime and execution boundary. This profile owns the controlled lifecycle-role vocabulary. `CAM-EQ2026-OPERATIONS-007-PLATINUM` applies the profile in runtime accountability, conformance and incident records.

---

## 2. Lifecycle Actor Model

Every consequential AI-system deployment SHALL identify, to the extent known and proportionate, the accountable owner, deployer, operator, applicable approver, and the evidence custodian. Missing, shared, disputed or confidential assignments SHALL be recorded as such rather than inferred from branding or infrastructure ownership.

| Family | Controlled roles | Primary record purpose |
| --- | --- | --- |
| Supply | `model_provider`, `dataset_supplier`, `software_component_supplier`, `tool_service_provider` | Identify material upstream supply and component provenance. |
| Development | `developer`, `system_integrator` | Identify those who develop, materially modify or assemble the AI system. |
| Provision | `ai_system_provider` | Identify the entity that makes the AI system available under its name or control in the applicable context. |
| Deployment | `deployer` | Identify the entity that operationalises the system in a technical and organisational context. |
| Operation | `operator`, `platform_host` | Identify operational control of the deployment, environment or service. |
| Governance | `accountable_owner`, `approver`, `assurance_function`, `evidence_custodian` | Identify accountability, approval, assurance and evidence custody without deciding liability. |
| External oversight | `auditor`, `assessor`, `investigator`, `regulator` | Identify an independent, investigatory or statutory oversight function where present. |
| Affected | `user`, `affected_person`, `impacted_stakeholder` | Identify a person or stakeholder who uses, is subject to, or may be materially affected by the deployment. |

An `ai_system_provider` is a lifecycle-role assignment, not an assertion that the actor is the EU AI Act provider. An `operator` is a controlled functional role, not the EU AI Act umbrella term.

### 2.1 Minimum Actor Assignment Record

Each material assignment SHALL preserve:

1. a controlled role;
2. an actor identifier or a controlled/confidential reference;
3. the bounded system, deployment, agent, component or activity;
4. the function, authority scope and retained control relevant to that role;
5. effective interval and evidence posture;
6. known delegation, transfer or termination; and
7. a contact or authorised evidence-access pathway where required and lawful.

An actor record MUST NOT contain secrets or protected personal data beyond what is lawful, necessary and access-controlled.

### 2.2 EU AI Act and Standards Crosswalk

This is a comparison aid, not a legal equivalence or compliance determination.

| External term or lifecycle concept | Relevant CAM role(s) | Boundary |
| --- | --- | --- |
| EU AI Act `provider` | `ai_system_provider`, often also `developer`, `system_integrator` or `accountable_owner` | Context-specific legal definition; no automatic equivalence. |
| EU AI Act `deployer` | `deployer`, often `operator` | A CAM deployment role may exist outside EU law or differ in scope. |
| EU AI Act `authorised representative`, `importer`, `distributor`, `product manufacturer` | May be recorded as a jurisdictional/intermediary assignment alongside supply, provision or deployment roles | These are legal-market roles, not universal lifecycle families. |
| EU AI Act `operator` | Any applicable supply, provision or deployment role | CAM does not use `operator` as a legal umbrella. |
| ISO/IEC 5338 lifecycle processes | Supply, development, provision, deployment, operation, governance and oversight assignments | A process model is not a roster of legal actors. |
| NIST AI RMF govern/map/measure/manage functions | `accountable_owner`, `assurance_function`, `approver`, `operator`, `investigator` | Functional alignment only; not an RMF claim. |

The EU AI Act terms are taken from Article 3 of Regulation (EU) 2024/1689; the regulation defines `operator` as a provider, product manufacturer, deployer, authorised representative, importer or distributor. ISO/IEC 5338 is used only as lifecycle framing.

---

## 3. Agentic Lifecycle

The controlled lifecycle applies to an AI agent, agentic AI system, agent orchestration component and material delegated action pathway. It is event-based, not a maturity scale, and supports recurrence and branching.

| Lifecycle control event | Required decision or evidence |
| --- | --- |
| `commission` | Mandate, intended use, accountable owner, system/deployment boundary and impact context. |
| `configure` | Approved configuration baseline, relevant instructions, tools, memory, controls and change authority. |
| `permission` | Effective permissions, credential references, action limits, delegation constraints and approval/stop conditions. |
| `deploy` | Target environment, deployer/operator, activation conditions, monitoring and evidence custody. |
| `delegate` | Delegating and receiving entity, bounded task, authority and permission transfer/attenuation, termination condition. |
| `monitor` | Monitoring owner, telemetry boundary, alert/escalation route and review interval. |
| `modify` | Change request, affected baseline/deployment, approval, reassessment and post-change evidence. |
| `suspend` | Suspension trigger, effect, operator, residual access and evidence preservation. |
| `revoke` | Permission, credential, delegation or access revocation and confirmation of effect. |
| `investigate` | Investigation authority, evidence hold, access pathway, scope and unresolved propositions. |
| `retire` | Termination, decommission/retention disposition, transfer/portability where applicable, and closure evidence. |

An agent SHALL NOT receive a materially broader delegated authority or effective permission than the delegator can lawfully and operationally confer. Delegation is not evidence of authorship, intent, legal responsibility or authority beyond the recorded scope.

### 3.1 Required Control Rules

For an agentic deployment with external tools, persistent memory, material delegation, consequential action, asserted conformance or incident investigation:

1. `commission`, `configure`, `permission`, `deploy`, `monitor` and a termination pathway SHALL be recorded before or at activation;
2. each material delegation SHALL record task scope, authority scope, effective permissions, delegator, receiver and expiry/termination condition;
3. a material change SHALL create or link to a new configuration baseline or documented change state;
4. `suspend` and `revoke` controls SHALL be assignable to an identified operational or governance actor;
5. investigation SHALL preserve incident-time evidence separately from remediation; and
6. retirement SHALL not erase mandatory retention, incident-hold, portability or audit obligations.

---

## 4. Relationship to AI-BOM and Runtime Evidence

The AI-BOM identifies composition, supply relationships and declared deployment configuration. The lifecycle actor record identifies role assignments and event controls. The runtime configuration snapshot identifies what was actually effective. The execution provenance record identifies what occurred in a bounded execution.

These objects SHALL be linked by stable identifiers where available, but SHALL NOT be conflated:

| Assertion | Required primary evidence object |
| --- | --- |
| A component is declared or verified as part of the system/deployment. | AI-BOM Profile |
| An actor had a bounded lifecycle role, approval or evidence-custody function. | Lifecycle actor record |
| A permission, control or tool was effective at a time. | Runtime configuration snapshot |
| An agent or tool was actually invoked in a bounded event. | Execution provenance record |

---

## 5. External Reference Basis

This profile supports operational alignment without asserting external conformance. Its external terminology references are:

- [Regulation (EU) 2024/1689, Article 3](https://eur-lex.europa.eu/eli/reg/2024/1689/oj/eng);
- [ISO overview of ISO/IEC 5338 AI system life cycle processes](https://www.iso.org/sectors/it-technologies/ai); and
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework).

---

## 6. Amendment Ledger

| Version | Change Summary | Timestamp (UTC) | Agent | Model | Reviewer | Reference Hash |
| --- | --- | --- | --- | --- | --- | --- |
| 1.0 | Initial controlled lifecycle actor model and agentic lifecycle profile, with non-equivalence crosswalk to EU AI Act roles and lifecycle/assurance references. | 2026-08-07T19:00:00Z | Caelen | GPT-5.6 | Dr M.V. O'Rourke |  |
