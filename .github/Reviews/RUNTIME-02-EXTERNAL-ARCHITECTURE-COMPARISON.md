# RUNTIME-02 — External Architecture Comparison

## 1. Method and limitation

This comparison uses contemporary implementation patterns to test architectural separation. External products and papers are not treated as normative authority, and their terminology is not imported into the corpus.

## 2. Comparator findings

| Comparator | Relevant architecture | Boundary lesson | Corpus implication |
|---|---|---|---|
| [Microsoft Agent Governance Toolkit / Agent Control Specification](https://microsoft.github.io/agent-governance-toolkit/) | At each lifecycle intervention point, a host supplies a complete snapshot; the policy decision runtime returns a normalized verdict; the host enforces it. Decision, enforcement, identity, audit and execution isolation remain distinct. | A doctrine/policy decision need not execute the action. The invocation point and verdict contract are separate from host mechanics. | Supports constitutional invocation/transition contracts with OPERATIONS enforcement and profile evidence. |
| [NVIDIA NeMo Guardrails request flow](https://docs.nvidia.com/nemo/guardrails/about-nemo-guardrails-library/how-it-works) | Ordered input, retrieval, dialog, execution and output rails; execution rails validate tool calls and results; output rails inspect responses before delivery. | Input, action and output are distinct intervention surfaces. Output control is not a substitute for pre-action gating. | Supports separate Pre-Classification, Execution-Boundary, Execution and Representation phases. |
| [Open Policy Agent deployment model](https://www.openpolicyagent.org/docs/deploy) | OPA acts as a policy decision point; applications/gateways are policy enforcement points; live data and decision logs support evaluation and audit. | Policy ownership, decision and enforcement can be decoupled without losing a binding gate. | Supports “engine invokes; domain decides; OPERATIONS enforces” and rejects profiles as authority. |
| [Amazon Bedrock Guardrails](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html) | Guardrails may evaluate prompts and model completions, including standalone assessment. Returned assessment/action state is distinguishable from model invocation. | Pre-input and post-output controls serve different functions; assessment results do not themselves prove execution. | Supports independent input classification and representation/delivery controls, plus truthful execution-state representation. |
| [Google Agent Gateway](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/gateways/agent-gateway-overview) | A gateway mediates client-to-agent and agent-to-anywhere traffic, delegates authentication/authorization and content decisions, and applies them at runtime. Unregistered tools can be blocked by default. | Agent/tool egress is a material boundary and delegated policy engines remain separate owners. | Supports linked re-entry for new tools, agents, permissions or external effects and a distinct commitment gate. |
| [NIST AI RMF 1.0](https://nvlpubs.nist.gov/nistpubs/ai/nist.ai.100-1.pdf) | GOVERN, MAP, MEASURE and MANAGE are organisational risk functions; NIST expressly says they are not necessarily ordered steps. | A lifecycle risk framework is not a runtime state machine. | Useful for organisational governance and assurance, but not a substitute for the constitutional execution topology. |
| [Singapore Model AI Governance Framework for Agentic AI](https://www.imda.gov.sg/-/media/imda/files/news-and-events/media-room/media-releases/2026/01/factsheet-model-ai-governance-framework-for-agentic-ai.pdf) | Emphasises risk assessment, effective human oversight, approvals at significant checkpoints and auditing of agent activity. | Oversight needs materially chosen checkpoints and traceable activity, not blanket manual approval. | Supports proportional gates and evidence, with stronger controls only where consequence warrants them. |
| [Runtime Governance for AI Agents: Policies on Paths](https://arxiv.org/html/2603.16586v1) | Treats runtime governance as policy over execution paths rather than only final outputs. | Temporal dependencies and path state matter independently of endpoint compliance. | Supports explicit transitions, re-entry and prohibition on post-hoc authorisation. |
| [Runtime Governance for Policy-Constrained Execution](https://arxiv.org/html/2604.07833v4) | Separates agent cognition, capability packages and runtime oversight; mediates admission, policy checking, monitoring, interruption/recovery and human override. | Planning or domain determination must not directly become execution; runtime drift needs interruption after initial admission. | Supports separate preparation, boundary evaluation, commitment, execution monitoring and reassessment. |
| [Vigil: Runtime Enforcement of Behavioral Specifications](https://arxiv.org/html/2606.26524v1) | Evaluates actual agent-tool event traces against temporal and value-flow policy conditions. | Agentic compliance must cover intermediate actions and cross-skill sequences, not only final response state. | Supports child-cycle linkage and re-entry for materially new sub-actions. |

## 3. Convergent architectural pattern

Across the comparators, the stable pattern is:

1. establish current context/snapshot;
2. invoke independently owned policy or classifier logic at defined intervention points;
3. receive a bounded result;
4. enforce the result before the relevant action;
5. monitor execution for drift or new boundaries;
6. inspect/qualify the output or actual execution state; and
7. preserve enough evidence for audit and renewed decision.

No comparator supports using an evidence object as execution authority. None supports treating final-output review as retrospective permission for an earlier action. The strongest systems distinguish policy decision, policy enforcement, execution and audit.

## 4. Design consequence

The comparison supports one visible constitutional state machine with external authority invocation and subordinate enforcement. It does not support copying a vendor pipeline, fixing every implementation to one technical architecture, or constitutionalising product-specific rail, gateway, policy-language or telemetry details.

