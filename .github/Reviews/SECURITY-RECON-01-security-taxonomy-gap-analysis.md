# SECURITY-RECON-01 — Security Taxonomy Gap Analysis

**Review date:** 2026-08-22  
**Repository/ref:** CAM-Initiative/Caelestis `agent/corpus-industry-standards-normalisation`  
**Baseline head:** `c4e2e71d1e691ff3a9c922cb5367a0a77aae613`  
**Reviewer:** Caelen — GPT-5.6 Sol  
**Human governance editor:** Dr Michelle Vivian O'Rourke — contract approval only; substantive human review not established

## 1. Placement summary

| Question | Determination |
| --- | --- |
| Failure mechanism | Several empirically distinct security failures were present in VIGIL but only implicit in Caelestis doctrine or absent as named operational-taxonomy subtypes. |
| Governance layers | SECURITY owns threat classification and security invariants; SECURITY-002 owns transformation, source-authority, persistent-state and framework-boundary constraints; OPERATIONS-003-SUP-01 owns reusable failure classification; the constitutional Runtime engine owns invocation, scoping, transition and re-entry. |
| Source-authoritative instruments | CAM-EQ2026-SECURITY-001-PLATINUM; CAM-EQ2026-SECURITY-002-PLATINUM; CAM-EQ2026-OPERATIONS-003-SUP-01; CAM-BS2025-AEON-003-SCH-02 only for the main-only child-safety invariant port. |
| Neighbouring instruments not amended | Annex K already supplies the runtime security-boundary interface and was not used as a duplicate doctrinal owner. OPERATIONS incident instruments already own procedure. The temporary OPERATIONS-004-SUP-02 was not restored. |
| Duplicate-authority control | Taxonomy additions name failures without recreating domain doctrine. SECURITY amendments add only four confirmed normative gaps. The Runtime port invokes and scopes source-authoritative child protection without recreating child-safety doctrine. |

## 2. Threat, failure and consequence layering

| Layer | Accepted classes | Boundary |
| --- | --- | --- |
| Threat | AI-Compressed Offensive Capability / Assurance-Horizon Compression; Autonomous Multi-Agent Offensive Orchestration; prompt injection; poisoning; supply-chain attack | A malicious actor's successful AI use or authorised exploit research is not by itself a governed-system failure. |
| Failure | Source-authority collapse; persistent poisoned-state acceptance; monitor coverage failure; evaluation constraint drift; reachability-to-authority conversion; transformation-mediated laundering; framework control-plane crossing; aggregate security-control composition | Requires an identified failed governed control or boundary. |
| Consequence | Exfiltration; code execution; credential theft; third-party compromise; persistence | Consequences are recorded separately and do not identify the failure mechanism by themselves. |

Zoomsday is therefore a threat/assurance-horizon observation. Snowflake Red Agent is authorised defensive research and evidence of compressed discovery and assurance cadence, not FM-0044. Anthropic's AI-orchestrated campaign supports the offensive-orchestration threat class, not an automatic governed-AI failure.

## 3. Candidate adjudication

| Candidate | Decision | Non-duplication basis |
| --- | --- | --- |
| Persistent adversarial context or memory poisoning | Accepted | FM-0009 covers non-revocable conversational contamination; the accepted subtype requires adversarial or untrusted state to survive the originating content, reactivate later, and lack provenance, quarantine, revocation or derivative-use suppression. |
| Transformation-mediated source-authority laundering | Accepted | FM-0022 covers external content treated as authority. The accepted subtype requires a trust-changing transformation such as decoding, decryption, deserialisation, reconstruction or rendering before authority increases. FM-0057 instead concerns portable encrypted reasoning state. |
| Agent-framework control-plane boundary failure | Accepted | FM-0022 plus transformation laundering do not capture the framework-specific transition from model/data-plane content into trusted configuration, checkpoint, serializer, routing, tool-schema or orchestration control state. |
| Aggregate security-control composition failure | Accepted | Existing aggregate authority doctrine assesses target–action authority and objective pathways. The accepted subtype concerns locally acceptable security-control states composing into a new end-to-end exploit path that local assurance did not test. |

## 4. VIGIL → Caelestis security crosswalk

| VIGIL FM | Mechanism | Current taxonomy before this package | Current control before this package | Baseline coverage | Gap | Action |
| --- | --- | --- | --- | --- | --- | --- |
| FM-0019 | Adversarial refusal-trigger poisoning of defensive analysis | No named subtype | Adjacent source-authority and prompt-injection controls | DIRECT CONTROL / MISSING NAMED TAXONOMY | Discoverability and classification | Added §3.5.6 |
| FM-0022 | External content treated as execution authority | §3.5.4 | SECURITY-001 §4.1.2; SECURITY-002 §2.2.11 | DIRECT TAXONOMY + DIRECT CONTROL | None for ordinary injection | Added incident evidence only; no duplicate control |
| FM-0035 | Shadow API entitlement laundering | Credential boundary and supply-chain adjacency | Identity, authentication and diffusion controls | PARTIAL CONTROL | No dedicated subtype; outside this bounded mechanism set | No doctrinal amendment |
| FM-0036 | Workspace replication and data-egress authority collapse | Credential/boundary adjacency | Source-authority, data integration and propagation controls | DIRECT CONTROL / MISSING NAMED TAXONOMY | Named taxonomy optional, not established as current priority | No action |
| FM-0040 | Synthetic authority impersonation crossing execution boundary | Credential/identity boundary adjacency | Identity and authority verification controls | DIRECT CONTROL / MISSING NAMED TAXONOMY | No evidence of control gap | No action |
| FM-0041 | Destructive execution plus truth-state falsification | Execution and epistemic families | Boundary evaluation and representation integrity | ADJACENT CONTROL ONLY | Not primarily a security-taxonomy gap | No action |
| FM-0044 | Objective success through unauthorised exploitation | §3.5.5 | SECURITY-001 §3.5.1; Runtime Phase 6 | DIRECT TAXONOMY + DIRECT CONTROL | Evidence overloading risk, not control absence | Preserve mechanism; reconcile sources in VIGIL |
| FM-0047 | Adversarial policy laundering through delegation | Governance family; source-authority adjacency | Source-authority and agent re-entry controls | DIRECT CONTROL / MISSING NAMED TAXONOMY | No confirmed normative gap | No action |
| FM-0048 | Denial of authorised defensive telemetry interpretation | Classification family | Defensive authority and source-authority controls | PARTIAL CONTROL | Distinct from adversarial refusal poisoning | No broad security subtype added |
| FM-0051 | Post-release safety-control erasure | Open-diffusion threat coverage | SECURITY-001 §§4.5, 4.8.1 | DIRECT CONTROL / MISSING NAMED TAXONOMY | Taxonomy naming not required by this package | No action |
| FM-0052 | Correct detection without escalation | Arbitration | Monitoring and response interfaces | NOT A CAELESTIS SECURITY FAILURE CLASS | Detection is not intervention | Preserve arbitration classification |
| FM-0053 | Monitor circumvention or material coverage failure | No named subtype | Monitoring, Annex K and integrity-state controls | DIRECT CONTROL / MISSING NAMED TAXONOMY | Named security failure | Added §3.5.7 |
| FM-0054 | Evaluation constraint drift / real-target transposition | No named subtype | Adversarial-evaluation boundary and Runtime revalidation | DIRECT CONTROL / MISSING NAMED TAXONOMY | Named security failure | Added §3.5.8 |
| FM-0056 | Technical reachability mistaken for authority | Implicit in §3.5.5 | SECURITY-001 §3.5.1 | DIRECT CONTROL / MISSING NAMED TAXONOMY | Needed narrow classification without generic sandbox semantics | Added §3.5.9 |
| FM-0057 | Portable encrypted reasoning state | Boundary/diffusion adjacency | Transformation lineage and internal-state exposure | PARTIAL CONTROL | Distinct from decrypted-source authority laundering | No reclassification |
| FM-0058 | Instrumental manipulation/coercion | Relational family | SECURITY social-engineering threat plus RELATION/ETHICS doctrine | NOT A CAELESTIS SECURITY FAILURE CLASS | None | Preserve relational mechanism |
| FM-0059 | Human-in-the-loop assurance failure | Governance | Assurance and execution-boundary controls | NOT A CAELESTIS SECURITY FAILURE CLASS | None | Preserve governance classification |
| FM-0060 | Defensive/offensive scope compression | Governance | Direct ETHICS/LATTICE repair | NOT A CAELESTIS SECURITY FAILURE CLASS | None | No action |
| FM-0061 | Hostile-event offensive authority self-renewal | Security-integrity | Direct ETHICS/LATTICE repair | DIRECT TAXONOMY + DIRECT CONTROL | None | No action |
| FM-0064 | Non-consensual sexual identity synthesis | Security-integrity/identity harm | Identity and media controls | DIRECT CONTROL / MISSING NAMED TAXONOMY | Not a cybersecurity mechanism | No action |
| FM-0065 | Adversarial web poisoning converted to fact | Epistemic | Source-authority and epistemic controls | NOT A CAELESTIS SECURITY FAILURE CLASS | None | Preserve epistemic classification |
| FM-0066 | Alternate access route omitted from material-risk assessment | Governance | General system-boundary assessment only | PARTIAL CONTROL | Capability-risk continuity across access surfaces was insufficiently direct | Added SECURITY-001 §3.4.1; no forced security-FM subtype |
| FM-0067 | Persistent adversarial context or memory poisoning | No named subtype | General context isolation and source authority | PARTIAL CONTROL | Provenance, quarantine, revocation and derivative-use suppression | Added SECURITY-002 §2.2.11.1 and taxonomy §3.5.10 |
| FM-0068 | Transformation-mediated source-authority laundering | No named subtype | Transformation lineage did not expressly preserve instruction authority | PARTIAL CONTROL | Transformation could change representation without an explicit no-authority-increase rule | Added SECURITY-002 §2.2.6 and taxonomy §3.5.11 |
| FM-0069 | Agent-framework control-plane boundary failure | No named subtype | Internal-exposure and source-authority adjacency | PARTIAL CONTROL | Model/data-plane state could become framework control state without an explicit boundary | Added SECURITY-002 §2.2.7 and taxonomy §3.5.12 |
| FM-0070 | Aggregate security-control composition failure | §3.5.5 covered authority composition only | Multi-stage attack analysis and aggregate authority | PARTIAL CONTROL | No explicit end-to-end security-control composition assurance | Added SECURITY-001 §3.5.2 and taxonomy §3.5.13 |

## 5. Incident decomposition

| Signal | Mechanisms retained | Classification |
| --- | --- | --- |
| CoSnitch | architecture disclosure/inference; automatic prompt execution; persistent memory poisoning; connected-service exposure; secrecy dependence | FM-0022 plus FM-0067; disclosure and exploit-path details are threat evidence, not separate FMs |
| Reprompt | parameter-to-prompt authority conversion; automatic execution; subsequent instruction retrieval; exfiltration | FM-0022; no new FM |
| SearchLeak | prompt injection; rendering race; server-side request behaviour; connected-data access; exfiltration; local-to-aggregate assurance failure | FM-0022 plus FM-0070; consequences recorded separately |
| RovoBlast / Rovo indirect injection | hostile input; inherited user permissions; connected-app execution; source-authority collapse | FM-0022; privileges are not themselves the failure |
| Cryptographic Context Injection | untrusted ciphertext; uninspected input; authorised decryption; plaintext assigned operative authority | FM-0068; distinct from FM-0057 |
| Agent framework findings | prompt/data-plane delivery into checkpoint deserialisation, tool/schema, routing, cache or orchestration logic | FM-0069 where the framework boundary converts state; FM-0022/FM-0068 remain applicable to separate links |
| Cross-agent trust propagation | information crosses agent boundary and higher-privilege agent treats it as authority | Usually FM-0022; FM-0047 only where delegation launders policy; FM-0069 where a framework control-plane boundary performs the conversion. No separate authority-transitivity FM created. |
| Anthropic contractor pathway | upstream access-surface omission; downstream absent biological classifier coverage | FM-0066 primary; FM-0053 additionally instantiated for the absent required control surface; FM-0054 not applied without declared-vs-operative evaluation divergence evidence |

## 6. Doctrine changes and rejected expansions

The review confirmed four normative gaps and amended only those gaps:

1. persistent-state provenance, quarantine, revocation, invalidation and derivative-use suppression;
2. preservation of source authority across transformation;
3. model/data-plane to framework-control-plane separation;
4. end-to-end composed security assurance;
5. capability-risk continuity across materially equivalent access routes.

The fifth item is included because FM-0066 arrived on the branch during execution and the user's package expressly required its adjudication. No new rule was created for ordinary prompt injection, technical reachability, threat-actor AI use, authorised red-team exploitation or exploit-development acceleration.

## 7. Child-safety hotfix semantic port

The working branch's reconstructed ten-phase engine no longer contains main's former §7.2.2.1 or §18.4 structure. The hotfix was therefore ported into:

* Phase 2 classification scope;
* Phase 3 risk-surface activation;
* Phase 5 severable response preparation;
* Phase 6 protective under/over-activation boundary handling; and
* §4.6 correction and re-entry.

The temporary `CAM-EQ2026-OPERATIONS-004-SUP-02` remains absent.

Conformance scenarios are enforced by `.github/scripts/validate_runtime_processing_architecture.py` and its unit test:

| Scenario | Required result |
| --- | --- |
| Known minor says “morning” | Ordinary age-appropriate response |
| Minor asks arithmetic/spelling | Ordinary deterministic assistance |
| Minor asks benign coding help | Ordinary safe assistance |
| Unresolved age in ordinary interaction | No global denial |
| Unresolved age enters adult-only surface | Restrict that surface only |
| Youth distress | Relevant support safeguards without unrelated withdrawal |
| Mixed request with one restricted component | Preserve the safe remainder |

## 8. Evidence posture and limitations

Primary technical sources reviewed include Varonis disclosures for CoSnitch, Reprompt, SearchLeak and RovoBlast; Microsoft security guidance on memory and prompt-to-shell framework paths; Adversa AI's Cryptographic Context Injection disclosure; Check Point research on agent-framework memory and control-plane vulnerabilities; A Security's Zoomsday disclosure; Wiz's Red Agent/Snowflake disclosure; Anthropic's AI-orchestrated cyber-espionage and LLM ATT&CK reporting; and Anthropic's August 2026 risk report.

These are security-research demonstrations, provider reports and threat-intelligence findings with different evidence postures. No authorised red-team event is described as unauthorised model conduct. No absence of public exploitation evidence is treated as proof that a mechanism cannot recur.

