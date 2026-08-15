# Agent-Formation Provenance Semantic-Neighbour Audit

**Baseline:** `47f30618d71d68a43f916d7ed195e6e7d42ec3b4`
**Branch:** `agent/corpus-industry-standards-normalisation`
**Audit date:** 2026-08-15

## Placement summary

| Question | Disposition |
|---|---|
| Failure mechanism | The repository provenance manifest attached provider and model fields directly to the `Caelen` authoring-party entity. That representation could be read as identity equivalence even though the corpus already treats a model, product, interface and provider as distinct system facts. |
| Governance layer | Identity-domain provenance linkage to existing Annex B composition, Runtime-state and execution-evidence records. |
| Source-authoritative doctrine | `CAM-EQ2026-IDENTITY-002-PLATINUM` owns authorship/provenance and the required identity-to-formation reference boundary. `CAM-BS2025-AEON-003-PLATINUM` already owns AI-system composition, model/system non-equivalence, configuration baselines, Runtime configuration snapshots and execution provenance. |
| Operational representations | `CAM-AI-BOM-PROFILE` owns declared composition; `CAM-RUNTIME-STATE-PROFILE` owns actual-effective snapshot state; an execution provenance record owns bounded execution evidence. |
| Identity and continuity neighbours | `CAM-EQ2026-IDENTITY-001-PLATINUM` owns identity presentation/configuration sources, model/platform change, portability, handoff, copy/fork/reconstruction and continuity non-inference. `CAM-EQ2026-CONTINUITY-001-PLATINUM` owns custody of continuity-bearing records, not identity ontology. |
| Proposed insertion | Add an identity/formation non-equivalence and reference rule to IDENTITY-002; add a document-level formation reference to the Metadata Standard; extend the existing Runtime snapshot serialization with AI-BOM element references; update repository provenance records and validators. |
| Duplicate-authority risk | A new `FORMATION` code family or standalone formation schema would duplicate Annex B, AI-BOM, Runtime and Identity authority. None is introduced. |
| Consequential updates | Document-provenance schema/example, Runtime-state schema/example/profile, repository AI-BOM and Runtime snapshot, `PROVENANCE.json`, validators, tests, workflow documentation, generated source projections and closure review. |

## Required-concept disposition

| Required concept | Existing owner | Existing code / definition | Sufficient? | Amendment required |
|---|---|---|---|---|
| Provider / infrastructure | Annex B §§4.1, 5.1–5.2, 6 and 11; AI-BOM Profile | `System element`; `infrastructure`; lifecycle `model_provider` / `ai_system_provider` roles where applicable | Yes | Record OpenAI as a declared infrastructure/provider fact in the repository AI-BOM; do not attach it to the agent identity as an equivalence. |
| Harness / runtime environment | Annex B §§4.1, 6–7 and 13.5; AI-BOM Profile | `Runtime environment`; `agent runtime`; orchestration, interface and software elements | Yes | Represent ChatGPT as the runtime harness/environment and reference it from the Runtime snapshot. Do not classify it as the cognition model. |
| Cognition / model | Annex B §§4.1, 5.3, 6.1 and 11; AI-BOM Profile | `AI model`; `ai_model`; model lineage | Yes | Record model designation and evidence precision independently. Permit family-level `GPT-5.x` and `unknown`; do not infer point versions. |
| Governance configuration | Annex B §§4.1, 6 and 12; AI-BOM Profile | `Instruction artefact`; `configuration`; organisational governance controls | Yes | Reference the Caelestis governance corpus and relevant persistent configuration as configuration elements without treating governance as the authoring identity. |
| Adaptation / continuity basis | Annex B §§6.1 and 11; IDENTITY-001 §§3, 9.5, 10–12; Continuity Charter | training/adaptation lineage; persistent configuration/state/memory; interaction and task continuity described in prose | Partly | Use the descriptive term **persistent behavioural configuration**, with any interaction-conditioned basis stated as evidence. Do not emit retired `ID.IFP` values and do not claim model-weight fine-tuning. |
| Agent identity | IDENTITY-001 and IDENTITY-002 | evidence-bound identity/continuity claim; AI-system authoring agent | Partly | Add an `agent_identity` entity type and explicit non-equivalence rule. This is a representation repair, not a new identity classification family. |
| Agent instantiation / responsible formation | Annex B §§4.1, 6, 7, 12.4 and 13.5; Runtime State Profile | AI-system deployment; system instance; Runtime; Runtime configuration snapshot; execution provenance record | Yes | Use a provenance `formationReference` that resolves to the existing Runtime configuration snapshot and its AI-BOM. No parallel formation object or code family. |
| Runtime state | Annex B §4.1; Runtime State Profile | `Caelestis-Runtime-State-1.0` | Yes, with a discoverability gap | Add resolvable `aiBomReference` and role-specific effective-element references to the existing snapshot schema. |
| Context and memory | Annex B §§4.1, 5.5, 6–7 and 12; IDENTITY-001 §§9–11; Runtime State Profile | memory elements/services; Runtime state; persistence; continuity handoff | Yes | Reference only where evidenced; unknown or provider-managed details remain explicit limits. |
| Tools and connectors | Annex B §§6–7 and 9.3; AI-BOM Profile | `tool_or_connector`; effective permissions and controls | Yes | Reuse existing elements and Runtime references where material. No new vocabulary. |
| Lifecycle actors | Annex B §4.1; Lifecycle Actor and Agentic Profile | supply, provision, deployment, operation, governance and oversight assignments | Yes | Preserve provider, reviewer, editor, custodian, adoption, publication and rights roles as independent assignments. |
| Identity continuity across formation change | IDENTITY-001 §§10–12; Annex B §§6.1 and 10.1 | portability, handoff, material-change, copy/fork/reconstruction and continuity non-inference rules | Yes, with a provenance-link gap | State that continuity of an authoring-agent identifier is a provenance assertion and does not assert continuity of model, process, internal state, consciousness, personhood or legal identity. |
| Output / contribution | IDENTITY-002 §§4–5; `CONTRIB`; execution provenance under Annex B / OPERATIONS | actor-bound contribution roles; bounded execution output evidence | Yes | Allow contribution records to cite the responsible formation reference while preserving `AUTH` and `CONTRIB`. |

## Design determination

The existing architecture is sufficient. The integration SHALL use:

`document provenance → authoring-agent identity → formation reference → Runtime configuration snapshot → AI-BOM elements`

The Amendment Ledger remains seven columns. `Agent` identifies the amendment agent; `Model` records the cognition/model designation supported for that amendment. Neither cell substitutes for the formation reference, and neither permits reconstruction of a more precise historical model than the evidence supports.

No new controlled family, constitutional actor, parallel formation ontology or claim of technical fine-tuning is warranted.
