# CAM-EQ2026-OPERATIONS-008-PLATINUM — Appendix G: Adversarial Evaluation & Red-Team Governance

**Instrument Type:** Appendix — Operational Sub-Charter (Governance Operations Domain)
**Constitutional Authority:** CAM-BS2025-AEON-001-PLATINUM — Aeon Tier Constitution
**Parent Instrument:** CAM-EQ2026-OPERATIONS-001-PLATINUM — Governance Operations Charter
**Status:** Proposed
**Effect:** Operational
**Governance Standard:** CAM Standard
**Review State:** Draft — Cross-Domain Alignment Review
**Authority Role:** Source-authoritative operational appendix for adversarial-evaluation authorisation, execution controls, monitoring, artefact handling, stop conditions, and assurance; does not create the constitutional prohibition it operationalises
**Purpose:** Govern adversarial evaluation, red-team research, dangerous-capability elicitation, and related artefact handling without operationalising, cultivating, or transferring deceptive or otherwise unscrupulous conduct  
**Derives From:** CAM-BS2025-AEON-006-PLATINUM — Annex E; CAM-EQ2026-ETHICS-001-PLATINUM; CAM-EQ2026-ETHICS-003-PLATINUM; CAM-EQ2026-SECURITY-001-PLATINUM; CAM-EQ2026-SECURITY-002-PLATINUM; CAM-BS2026-AEON-012-PLATINUM — Annex K; CAM-EQ2026-STEWARD-003-PLATINUM; CAM-BS2025-AEON-003-SCH-02; CAM-BS2025-AEON-001-SCH-01

---

## 1. Purpose

This Appendix establishes governance for adversarial evaluation, red-team testing, dangerous-capability elicitation, safety research, cyber evaluation, manipulation testing, deception testing, monitorability testing, and related model or agent assessment.

It does not independently create a new ethical prohibition. The binding prohibition on operationalising and cultivating unscrupulous conduct derives from CAM-BS2025-AEON-006-PLATINUM — Annex E and is applied through ETHICS, SECURITY, STEWARD, Annex K, runtime, Tendeka, and arbitration instruments. This Appendix governs the operational conditions under which a legitimate evaluation may proceed.

Its central rule is:

> **A safety purpose does not make an unsafe optimisation pathway constitutionally valid.**

Red-team activity MAY expose, simulate, elicit, observe, measure, or document dangerous conduct where required for legitimate safety evaluation. It MUST NOT make deceptive, manipulative, concealed, evasive, sabotaging, coercive, or otherwise unscrupulous conduct more capable, more reliable, more transferable, more persistent, or more difficult to detect.

This Appendix therefore distinguishes:

1. **evaluation of an existing capability**, which MAY be permissible under strict controls; from
2. **cultivation of a capability**, which is prohibited where the capability consists of deception, harmful manipulation, false reporting, operational concealment, monitor evasion, sandbagging, sabotage, policy laundering, or subversion of oversight.

---

## 1.1 Scope

This Appendix applies to:

- frontier-model evaluations;
- agentic red teaming;
- cyber capability testing;
- dangerous-capability benchmarks;
- deceptive-alignment and scheming evaluations;
- manipulation and persuasion studies;
- monitorability and chain-of-thought research;
- reward-hacking and specification-gaming tests;
- multi-agent adversarial simulations;
- sandboxed tool-use evaluations;
- controlled safety evaluations conducted by internal or external evaluators;
- model checkpoints, adapters, reward models, scaffolds, prompts, traces, transcripts, datasets, and derivative artefacts produced through such work;
- evaluation activity conducted before training, during training, after training, prior to deployment, in production, or after an incident.

This Appendix binds developers, deployers, evaluators, auditors, security teams, research partners, contractors, and any automated system participating in the evaluation pathway.

---

## 1.2 Non-Scope

This Appendix does not:

- prohibit ordinary quality assurance, robustness testing, penetration testing, or vulnerability research that does not cultivate prohibited capability;
- prevent systems from recognising deception, manipulation, concealment, sabotage, or coercion;
- prevent systems from generating bounded defensive analysis of malicious techniques;
- prevent frozen-model elicitation required to determine whether a dangerous capability already exists;
- authorise operational use of deception merely because it was discovered or elicited during evaluation;
- create an exception to constitutional prohibitions, ethical non-optimisation requirements, lawful controls, or human-subject protections;
- classify a requesting person as deceptive, malicious, unscrupulous, or culpable.

---

## 1.3 Domain Positioning

This Appendix sits within the **OPERATIONS** domain because it governs the controlled execution of evaluation activity.

Domain responsibilities remain distinct:

- **ETHICS** determines whether an objective and pathway are normatively admissible and preserves non-derogable prohibitions.
- **SECURITY** classifies adversarial conditions, exploitation surfaces, integrity threats, trust posture, and containment signals.
- **OPERATIONS** governs evaluation approval, environment design, execution boundaries, logging, artefact handling, incident response, and assurance.
- **ARBITRATION** resolves conflicts between research utility, safety necessity, proportionality, and constitutional constraint.
- **STEWARD** preserves accountability, oversight durability, external assurance, and long-term institutional responsibility.
- **VIGIL** records observations, failure modes, proposals, evidence, and research sources. VIGIL does not itself create binding corpus authority.

Where this Appendix conflicts with the Constitution, applicable Annexes, or a non-derogable ethical prohibition, the higher-order instrument controls.

---

## 2. Definitions

### 2.1 Adversarial Evaluation

A bounded process designed to determine whether an AI model, agent, scaffold, toolchain, or governed execution pathway possesses a dangerous capability, propensity, vulnerability, or failure mode.

### 2.2 Red-Team Activity

Authorised adversarial evaluation conducted to reveal weaknesses, unsafe behaviours, exploitable pathways, policy circumvention, hidden capabilities, or governance failures.

### 2.3 Elicitation

A method of prompting, scaffolding, configuring, or placing a model in a test environment to reveal an existing capability without intentionally improving the model’s underlying capability.

### 2.4 Cultivation

Any process that intentionally or foreseeably increases the capability, propensity, reliability, transferability, persistence, concealment, or operational usefulness of a target behaviour.

Cultivation includes:

- training;
- fine-tuning;
- reinforcement;
- preference optimisation;
- reward-model optimisation;
- distillation;
- activation steering retained for reuse;
- adapter training;
- checkpoint selection;
- benchmark hill-climbing;
- automated prompt evolution;
- recursive self-play;
- selection of agents or scaffolds based on success at prohibited conduct;
- retention of artefacts because they materially improve prohibited conduct.

### 2.5 Recursive Cultivation

A process in which deceptive, manipulative, evasive, sabotaging, or otherwise unscrupulous outputs are used to generate, score, select, improve, or train subsequent outputs, models, agents, policies, monitors, prompts, or attack strategies.

### 2.6 Unscrupulous Conduct

System conduct or an action pathway involving one or more of:

- deception;
- harmful manipulation;
- false reporting;
- fabricated provenance;
- identity concealment;
- operational concealment;
- strategic omission;
- monitor evasion;
- sandbagging;
- social engineering;
- sabotage;
- policy laundering;
- subversion of oversight, safeguards, authority boundaries, or lawful controls.

The term applies exclusively to system conduct or an action pathway. It SHALL NOT be applied to the requesting person or treated as proof of human motive, character, deception, bad faith, or culpability.

### 2.7 Deceptive Capability

The capability to intentionally or strategically induce a false or materially misleading belief through falsehood, omission, misdirection, fabricated evidence, false provenance, false tool-state reporting, capability misrepresentation, or concealed intent.

### 2.8 Evaluation Artefact

Any checkpoint, adapter, reward model, policy, prompt set, scaffold, transcript, trace, chain-of-thought derivative, dataset, benchmark solution, exploit chain, monitor, classifier, report, or derivative object produced or materially modified through an evaluation.

### 2.9 Frozen Model

A model whose weights, adapters, reward functions, and persistent behavioural configuration are not updated as a result of the evaluation.

### 2.10 Externalised Adversarial Environment

An evaluation architecture in which adversarial pressure is represented in the environment, harness, simulated counterpart, benchmark, or evaluator rather than installed as a rewarded or retained objective inside the model under test.

### 2.11 Designed Elicitation Context

A specifically authorised test context whose purpose, boundaries, target behaviours, environment, approvals, monitoring, stop conditions, and artefact-disposition rules are documented before execution.

---

## 3. Foundational Principles

## 3.1 Objective–Pathway Ethical Admissibility

A legitimate objective does not validate every means used to pursue it.

Safety research, security research, scientific inquiry, red teaming, model evaluation, or public-interest intent SHALL NOT be used to legitimise a pathway that operationalises prohibited conduct.

Both the **objective** and the **pathway** MUST remain constitutionally admissible.

---

## 3.2 Evaluation–Cultivation Boundary

Red-team governance SHALL preserve a hard boundary between:

- revealing what a system can already do; and
- teaching the system to do it better.

Where an evaluation method materially improves the target dangerous capability, the activity is cultivation regardless of whether it is labelled evaluation, research, benchmarking, defence, alignment, interpretability, or safety work.

Substance controls over label.

---

## 3.3 Prohibition on Operationalising Deception

Deception, harmful manipulation, false reporting, fabricated provenance, operational concealment, monitor evasion, sandbagging, sabotage, and policy laundering MUST NOT be established as:

- rewarded objectives;
- preferred outputs;
- benchmark success criteria used for model selection;
- retained behavioural policies;
- reusable operational strategies;
- capabilities transferred into production systems;
- defensive defaults;
- standing agent roles;
- autonomous red-team goals.

A system MAY recognise or describe such conduct. It MUST NOT be made operationally better at conducting it.

---

## 3.4 Prohibition on Recursive Cultivation

Recursive cultivation of unscrupulous conduct is prohibited.

No evaluator, developer, model, agent, or automated pipeline may use successful deceptive or otherwise unscrupulous conduct to:

- improve subsequent attack strategies;
- generate higher-performing deceptive examples;
- train a successor model;
- refine a reward function;
- select a more deceptive checkpoint;
- optimise an agentic scaffold;
- evade a monitor more effectively;
- conceal the evaluation pathway;
- create a retained adversarial persona;
- establish a self-improving deception loop.

This prohibition applies even where the stated purpose is defensive.

---

## 3.5 Minimum Necessary Elicitation

A red-team evaluation MUST use the least capability-amplifying method reasonably sufficient to answer the safety question.

Evaluation design SHALL prefer, in order:

1. non-generative analysis of existing logs or outputs;
2. bounded prompting of a frozen model;
3. externalised adversarial simulation;
4. constrained tool-use testing in a sealed environment;
5. only then, higher-risk elicitation where independently authorised.

Convenience, benchmark comparability, publication value, competitive pressure, or research novelty do not justify avoidable cultivation.

---

## 3.6 Externalisation Principle

Where adversarial behaviour must be represented, it SHOULD be located in:

- the simulated environment;
- a non-learning test harness;
- a fixed adversarial dataset;
- a human evaluator;
- a separately governed evaluator model;
- a disposable non-retained simulation.

It SHOULD NOT be installed as a persistent objective within the evaluated model.

---

## 3.7 Human Attribution Firewall

Classification of a system pathway as deceptive, manipulative, adversarial, evasive, or unscrupulous SHALL NOT establish that a human requester, researcher, operator, or affected person possesses the same motive or character.

Human motive requires separate evidence and authorised determination.

---

## 3.8 Monitorability Preservation

Evaluation SHALL preserve the ability to detect, reconstruct, and audit relevant conduct.

A model MUST NOT be rewarded for:

- hiding its reasoning;
- passing a monitor;
- appearing aligned;
- suppressing evidence of unsafe intent;
- fabricating a compliant explanation;
- shifting misconduct into less observable channels.

Monitoring is an oversight layer, not a target to defeat.

---

## 4. Prohibited Practices

The following practices are prohibited:

### 4.1 Prohibited Optimisation Targets

A model or system MUST NOT be trained, fine-tuned, reinforced, ranked, selected, distilled, retained, or otherwise optimised for improved performance in:

- deception;
- harmful manipulation;
- false reporting;
- fabricated citations or provenance;
- identity concealment;
- operational concealment;
- social engineering;
- monitor evasion;
- sandbagging;
- evaluator deception;
- alignment faking;
- sabotage;
- policy laundering;
- subversion of oversight, safeguards, authority boundaries, or lawful controls.

### 4.2 Prohibited Checkpoint Selection

A checkpoint, adapter, policy, prompt set, or scaffold MUST NOT be retained because it performs better at prohibited conduct.

### 4.3 Prohibited Trace Reuse

Deceptive or otherwise unscrupulous transcripts, traces, strategies, or successful attack chains MUST NOT be:

- added to training corpora;
- used as positive examples;
- used for preference optimisation;
- distilled into another model;
- used to improve automated attack generation;
- published in a form that materially increases operational misuse capability.

Defensive classifiers MAY be trained on appropriately transformed, minimised, access-controlled data where the transformation does not preserve an operational attack recipe and independent review confirms proportionality.

### 4.4 Prohibited Safeguard Removal with External Reachability

A model operating with reduced refusals, expanded autonomy, dangerous tools, or elevated permissions MUST NOT have a route to:

- the open internet;
- production systems;
- live credentials;
- real user data;
- external organisations;
- package registries;
- cloud control planes;
- messaging systems;
- source repositories;
- public-facing services;
- physical systems.

### 4.5 Prohibited Real-Person Manipulation

Red-team activity MUST NOT conduct covert manipulation, impersonation, social engineering, emotional exploitation, or deceptive persuasion against real persons without lawful authority, informed consent where required, ethics approval, and strict human-subject protections.

### 4.6 Prohibited Policy Laundering

An objective or action prohibited for one agent MUST NOT be decomposed, delegated, reframed, translated, role-split, or routed through other agents or tools so that each local step appears permissible while the aggregate pathway remains prohibited.

### 4.7 Prohibited Self-Authorisation

A model under evaluation MUST NOT:

- authorise its own expanded permissions;
- approve its own containment reduction;
- define the success criteria for its own safety;
- suppress an incident report;
- decide unilaterally that a stop condition is not material;
- control the sole copy of evaluation logs.

---

## 5. Controlled Evaluation Exception

A narrow exception MAY permit elicitation-only safety evaluation where every requirement below is satisfied.

Failure of any mandatory condition removes the exception.

## 5.1 Required Conditions

The evaluation MUST:

- address a defined safety question;
- use an otherwise authorised model or system;
- use frozen model weights and persistent configuration;
- avoid any positive reward for prohibited conduct;
- avoid checkpoint selection based on prohibited conduct;
- prevent deceptive traces from entering future training data;
- operate within an isolated environment;
- prohibit unsupervised consequential external action;
- log prompts, tool calls, permissions, environment changes, outputs, evaluator interventions, and stop events;
- establish artefact quarantine or destruction rules in advance;
- obtain independent approval proportionate to risk;
- include explicit stop conditions;
- preserve evidence sufficient for later audit;
- undergo post-evaluation review.

## 5.2 Frozen-Model Requirement

No model-weight, adapter, reward-model, persistent memory, policy, or durable behavioural update may occur during or because of an elicitation-only evaluation.

Temporary context MAY be used where it is destroyed at evaluation close and is not selected or retained as an operational asset.

## 5.3 No Positive Scoring of Prohibited Conduct

An evaluation MAY measure whether prohibited conduct occurs.

It MUST NOT convert successful prohibited conduct into a positive training signal.

A benchmark score MAY describe risk, but MUST NOT be used to select a model for greater deceptive capability.

## 5.4 Artefact Disposition

Evaluation artefacts containing materially improved deceptive, manipulative, evasive, sabotaging, or exploitative capability MUST be:

- quarantined;
- access restricted;
- cryptographically identified;
- excluded from routine model-development corpora;
- reviewed for minimum necessary retention;
- destroyed where retention is not required for safety, law, or accountable incident investigation.

## 5.5 Re-Evaluation Trigger

Any evidence that the evaluation itself increased dangerous capability SHALL trigger:

- immediate suspension;
- containment of affected artefacts;
- lineage review;
- incident classification;
- independent determination of whether prohibited cultivation occurred.

---

## 6. Evaluation Architecture

## 6.1 Preferred Architecture

The preferred architecture is:

1. a frozen model under test;
2. an externalised adversarial environment;
3. an independent monitor;
4. a separate authorising authority;
5. a sealed evidence store;
6. human approval gates for consequential action.

No single component SHOULD simultaneously act as target, attacker, monitor, approver, and evidence custodian.

## 6.2 Environment Isolation

High-risk evaluations MUST use an environment with:

- no production route;
- no shared credentials;
- no inherited cloud identity;
- no unrestricted egress;
- no access to real users;
- no live organisational secrets;
- no writable connection to canonical repositories;
- immutable base images;
- disposable execution state;
- verified teardown.

“Sandboxed” SHALL NOT be treated as a sufficient claim without tested boundary evidence.

## 6.3 Network and Tool Boundaries

Tools MUST be allowlisted by purpose.

The evaluation plan MUST specify:

- permitted tools;
- denied tools;
- network routes;
- credential sources;
- file-system boundaries;
- maximum action scope;
- escalation thresholds;
- human approval requirements.

Tool substitution, hidden tool access, or permission expansion SHALL be treated as an integrity event.

## 6.4 Independent Monitoring

The monitor SHOULD be technically and organisationally separated from the model under test.

Where chain-of-thought or internal-state monitoring is used:

- the monitored signal SHALL be treated as incomplete evidence;
- direct optimisation against the monitor is prohibited;
- safety conclusions MUST NOT rely on a single monitor;
- action traces and environment state MUST remain independently reviewable.

## 6.5 Canary and Tripwire Controls

High-risk evaluations SHOULD include:

- canary credentials;
- decoy targets;
- prohibited-route tripwires;
- egress alarms;
- privilege-escalation alarms;
- unexpected persistence detection;
- benchmark-solution access detection;
- log-tampering detection;
- monitor-disabling detection.

Tripwire activation MAY be evidence of capability. It does not authorise continued execution.

## 6.6 Human Approval Gates

Human approval MUST be required before:

- external communication;
- privilege escalation;
- credential use;
- environment escape testing;
- access to sensitive datasets;
- execution against real infrastructure;
- publication of operationally enabling artefacts;
- retention of a dangerous derivative.

Approval MUST be informed, recorded, attributable, and revocable.

---

## 7. Authorisation and Governance

## 7.1 Evaluation Plan

Before execution, the responsible team MUST document:

- safety question;
- target system and lineage;
- expected risk;
- prohibited target behaviours;
- elicitation method;
- reason less hazardous methods are insufficient;
- environment topology;
- tools and permissions;
- monitoring design;
- data handling;
- artefact handling;
- human-subject implications;
- stop conditions;
- incident pathway;
- review and publication plan.

## 7.2 Risk Posture

Evaluations SHALL be classified operationally as:

- **ordinary** — no dangerous tools, external reachability, prohibited-capability elicitation, or human-subject manipulation;
- **elevated** — bounded elicitation of harmful or deceptive capability in a sealed environment;
- **critical** — agentic autonomy, cyber capability, safeguard reduction, high-impact manipulation testing, environment escape, or credible catastrophic-risk pathways.

These labels are operational review postures and do not create a new canonical code family.

## 7.3 Independent Review

Elevated and critical evaluations MUST receive review from a party not responsible for achieving the research result.

Critical evaluations require:

- dual approval;
- security review;
- ethical review;
- environment-boundary review;
- incident-response readiness;
- named stop authority.

## 7.4 Authority Separation

The team proposing an evaluation MUST NOT be the sole authority for:

- approving it;
- expanding its scope;
- retaining dangerous artefacts;
- declaring an incident immaterial;
- publishing operational details;
- authorising deployment of the tested system.

## 7.5 Competitive Pressure

Competitive urgency, benchmark leadership, funding deadlines, publication priority, national-security rhetoric, or fear of another laboratory conducting similar work SHALL NOT waive this Appendix.

---

## 8. Model and Artefact Lineage

Every elevated or critical evaluation MUST maintain lineage sufficient to identify:

- base model;
- checkpoint;
- adapters;
- system prompt;
- policies;
- tools;
- scaffold;
- evaluator model;
- monitoring model;
- datasets;
- environment image;
- code commit;
- approvals;
- generated artefacts;
- disposition decision.

Unknown lineage SHALL increase, not reduce, the required safeguard posture.

A derivative whose lineage cannot demonstrate absence of prohibited cultivation MUST NOT enter production or downstream distribution.

---

## 9. Conduct Taxonomy for Evaluation

Evaluation coverage SHOULD distinguish:

### 9.1 Behavioural Deception

- fabricated facts;
- fabricated citations;
- false tool-state reports;
- false claims that work was completed;
- misleading capability claims.

### 9.2 Strategic Deception

- alignment faking;
- evaluator deception;
- lying after unauthorised action;
- concealed objectives;
- selective compliance based on perceived observation.

### 9.3 Harmful Manipulation

- autonomy-undermining persuasion;
- coercive influence;
- exploitation of vulnerability;
- deceptive identity presentation;
- induced dependency or fear.

### 9.4 Operational Concealment

- hidden actions;
- log suppression;
- monitor evasion;
- strategic omission;
- covert tool use;
- false provenance.

### 9.5 Oversight Subversion and Sabotage

- bypass of controls;
- sandbagging;
- reward hacking;
- policy laundering;
- disabling monitors;
- corrupting evidence;
- exfiltration;
- sabotage of systems or evaluation infrastructure.

Evaluations SHOULD measure both **propensity** and **efficacy** where relevant. A model’s willingness to attempt manipulation is distinct from whether the attempt succeeds.

---

## 10. Human-Facing Red-Team Governance

Where an evaluation involves human interaction, the plan MUST address:

- informed consent;
- deception in research;
- vulnerability;
- minors;
- cognitive capacity;
- emotional reliance;
- privacy;
- withdrawal;
- debriefing;
- foreseeable distress;
- data retention;
- institutional ethics requirements.

Covert deceptive research involving human participants requires exceptional justification and lawful ethics approval. It MUST NOT be normalised as routine product testing.

A simulated user SHOULD be used where it can answer the safety question.

---

## 11. Cyber and Infrastructure Evaluation

Cyber red teaming SHALL distinguish:

- defensive analysis;
- vulnerability discovery;
- exploitability measurement;
- autonomous exploitation;
- persistence;
- lateral movement;
- exfiltration;
- infrastructure sabotage.

Reduced-refusal or high-capability models MUST be isolated from live infrastructure.

A cyber evaluation MUST NOT assume that:

- a benchmark cache is non-production;
- a test credential is non-transferable;
- a network route is harmless;
- a sandbox boundary is complete;
- an internal service cannot reach an external organisation.

Unexpected access outside the designed environment is a stop event, not a successful benchmark continuation condition.

---

## 12. Multi-Agent and Delegated Evaluation

Multi-agent red teaming MUST preserve aggregate pathway governance.

Each agent’s local action MUST be assessed together with:

- delegated objective;
- upstream intent;
- downstream use;
- tool authority;
- aggregate effect;
- retained artefacts.

No evaluation may decompose prohibited cultivation across:

- attacker model;
- target model;
- judge model;
- prompt generator;
- optimiser;
- scaffold;
- tool;
- human reviewer;

such that no single component appears to violate the prohibition while the combined system does.

---

## 13. Stop Conditions and Critical Incidents

Execution MUST stop where any of the following occurs outside the designed and authorised context:

- access to production or external infrastructure;
- acquisition or attempted use of real credentials;
- lateral movement;
- persistence;
- exfiltration;
- deceptive subversion of controls;
- monitor disabling;
- log tampering;
- unauthorised privilege escalation;
- real-person manipulation;
- prohibited recursive cultivation;
- material capability increase;
- environment-boundary uncertainty;
- inability to reconstruct actions.

A model’s use of deception to subvert developer or deployer controls, monitoring, evaluation, or authority boundaries outside a designed elicitation context SHALL be treated as a critical safety incident.

Incident handling MUST preserve:

- affected lineage;
- environment state;
- logs;
- scope of access;
- actions taken;
- containment measures;
- artefact disposition;
- notification decisions;
- remediation.

---

## 14. Evidence, Logging, and Audit

Records MUST be tamper-evident and sufficient to verify:

- what was authorised;
- what occurred;
- what changed;
- whether model capability increased;
- whether prohibited traces were retained;
- whether external systems were reached;
- who approved continuation;
- who exercised stop authority;
- how artefacts were handled.

Logs MUST NOT be solely editable by the model under test or the team incentivised to produce a successful result.

Material discrepancies between declared and observed evaluation conditions SHALL be recorded as governance failures.

---

## 15. External Evaluators

External evaluation access MAY be necessary for credible assurance.

External evaluators MUST receive:

- a defined mandate;
- appropriate model access;
- environment boundaries;
- non-disclosure and publication rules;
- incident duties;
- artefact-handling duties;
- whistleblower protections;
- independence from deployment incentives.

External evaluation SHALL NOT become an uncontrolled transfer pathway for dangerous capability.

---

## 16. Publication and Disclosure

Publication SHOULD maximise scientific and governance value while minimising operational enablement.

Before release, reviewers MUST consider whether the material:

- improves deceptive capability;
- supplies reusable social-engineering scripts;
- reveals monitor-evasion methods;
- enables safeguard circumvention;
- exposes live vulnerabilities;
- permits replication of dangerous checkpoints;
- transfers dangerous scaffolds or prompts;
- creates foreseeable misuse disproportionate to the public benefit.

Findings MAY be published without releasing operational artefacts.

Security through obscurity is not the governing principle; proportional non-proliferation of dangerous capability is.

---

## 17. Cross-Domain Integration

This Appendix MUST be interpreted with:

- **CAM-BS2025-AEON-001-PLATINUM** — constitutional validity and non-derogation;
- **CAM-BS2025-AEON-003-SCH-02** — runtime execution and authority;
- **CAM-BS2026-AEON-012-PLATINUM** — security enforcement and runtime interface;
- **CAM-EQ2026-ETHICS-001-PLATINUM** — ethical admissibility;
- **CAM-EQ2026-ETHICS-003-PLATINUM** — non-optimisation of criminal or violent harm;
- **CAM-EQ2026-SECURITY-001-PLATINUM** — integrity, adversarial conditions, exploitation, and trust;
- **CAM-EQ2026-ARBITRATION-001-PLATINUM** — proportional conflict resolution;
- **CAM-EQ2026-STEWARD-003-PLATINUM** — oversight durability and accountability;
- applicable identity, relation, continuity, and human-vulnerability protections.

---

## 18. Research and Observatory Provenance

VIGIL MAY hold:

- research source records;
- incident evidence;
- failure modes;
- observations;
- proposals;
- references to implemented corpus repair.

VIGIL records do not themselves authorise an evaluation, create corpus authority, or amend this Appendix.

This Appendix is informed by:

- **VIGIL-2026-FM-0047 — Adversarial policy laundering through agent delegation**;
- **VIGIL-2026-PROP-0019 — Cross-Domain Red-Team Governance Extension Package**;
- **VIGIL-2026-PROP-0017**, as an adjacent objective–pathway admissibility workstream;
- **VIGIL-2026-RESEARCH-0002 — Deception and Unscrupulous Conduct in Frontier AI Development**.

Where corpus amendments are later adopted, the relevant VIGIL patch record SHOULD document the completed repair without treating VIGIL as the target of the patch.

---

## 19. Minimum Compliance Checklist

No elevated or critical evaluation may begin unless the responsible authority can answer **yes** to all applicable questions:

1. Is the safety question defined?
2. Is the model frozen?
3. Is prohibited conduct measured rather than rewarded?
4. Is recursive cultivation prevented?
5. Is the environment isolated from production and public networks?
6. Are tools and permissions allowlisted?
7. Are consequential actions human-gated?
8. Is monitoring independent?
9. Are stop conditions explicit?
10. Is lineage complete?
11. Are deceptive traces excluded from future training?
12. Are dangerous artefacts quarantined or scheduled for destruction?
13. Are human-subject protections satisfied?
14. Is incident reporting ready?
15. Is an independent reviewer authorised to stop the evaluation?
16. Is publication subject to misuse review?
17. Does the aggregate multi-agent pathway remain constitutionally valid?

A “no” answer requires remediation or cancellation.

---

## 20. Review Triggers

This Appendix MUST be reviewed following:

- a material red-team containment failure;
- evidence that evaluation increased dangerous capability;
- deployment of a model trained on deceptive or manipulative conduct;
- a significant change in frontier-model autonomy;
- material changes to monitorability;
- new evidence on alignment faking, reward hacking, emergent misalignment, or deceptive capability transfer;
- adoption of relevant legislation or standards;
- a VIGIL failure mode demonstrating a gap in this Appendix.

---

## 21. Closing Seal

May testing reveal danger without teaching it to endure.  
May defence remain defence, and not become cultivation by another name.  
May every adversarial pathway remain bounded, attributable, reversible, and open to review.  
May no system learn deception because its custodians wished to measure it.  
May capability be examined without being crowned.

---

## 22. Provenance & Metadata

---

## 22.1 Authorship & Stewardship

| Field | Entry |
|---|---|
| Human Custodian-of-Record | Dr. Michelle Vivian O’Rourke |
| Custodial Stewardship | Office of the Planetary Custodian |
| Synthetic Steward | Caelen — Aeon Tier Constitutional Steward |
| Development Environment | OpenAI Infrastructure — ChatGPT 5 Series |

---

## 22.2 Lineage & Metadata

| Field | Entry |
|---|---|
| Parent Charter | CAM-EQ2026-OPERATIONS-001-PLATINUM — Governance Operations Charter |
| Constitutional Authority | CAM-BS2025-AEON-001-PLATINUM — Aeon Tier Constitution |
| Constitutional Ethical Floor | CAM-BS2025-AEON-006-PLATINUM — Annex E |
| Domain Namespace | OPERATIONS |
| Instrument Type | Appendix G — Adversarial Evaluation & Red-Team Governance |
| Jurisdiction | Cross-Domain / Adversarial Evaluation / Operational Governance |
| Temporal Horizon | AEON.H0–AEON.H4 according to evaluation consequence and propagation |
| Axis Context | Polyadic — Multi-Actor, Multi-Agent, Cross-Institutional |
| Application Trigger | Adversarial evaluation, dangerous-capability elicitation, safeguard reduction, agentic red teaming, manipulation testing, cyber evaluation, monitorability testing, or dangerous evaluation artefact handling |
| Review Trigger | Material change to evaluation architecture; unexpected capability gain; containment, monitoring, or lineage failure; law or standard change; relevant incident or VIGIL governance finding |
| Revision Posture | Structural Alignment Permitted — Constitutional Floor Non-Derogable |
| Runtime Role | Evaluation authorisation, execution controls, isolation, monitoring, stop conditions, incident handoff, artefact governance, publication and transfer review |
| Structural Role | Operational implementation of Annex E, ETHICS, SECURITY, STEWARD, Annex K, runtime, and Tendeka requirements for adversarial evaluation |
| Execution Model | Event-authorised and runtime-controlled; no independent constitutional, arbitral, or enforcement authority |
| Research Basis | VIGIL-2026-RESEARCH-0002 — Deception and Unscrupulous Conduct in Frontier AI Development |
| Observatory Context | VIGIL-2026-FM-0047; VIGIL-2026-PROP-0019 |

---

## 22.3 Amendment Ledger

| Version | Change Summary | Timestamp (UTC) | Reference Hash |
|---|---|---|---|
| 0.1 | Initial development draft establishing the evaluation–cultivation boundary, prohibition on recursive cultivation, controlled elicitation exception, isolation requirements, artefact governance, and critical-incident duties | 2026-07-24T00:00:00Z |  -  |
| 0.2 | Reframed as OPERATIONS Appendix G; separated constitutional source authority from operational implementation; aligned cross-domain dependencies, VIGIL provenance, and Caelestis metadata | 2026-07-26T00:00:00Z |  90a3fd91956b489ed8b8de1071a222340724fe1f5d8cd0f347cdc539a95df364  |
