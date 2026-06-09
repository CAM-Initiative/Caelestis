# CAM-EQ2026-OPERATIONS-003-SUP-01 — Appendix B: Runtime & Governance Failure Taxonomy (Supplementary 1)

**Instrument Type:** Operational Supplement — Failure Classification & Incident Taxonomy  
**Constitutional Authority:** CAM-BS2025-AEON-001-PLATINUM — Aeon Tier Constitution  
**Status:** Adopted  
**Effect:** Pre-Enforcement Recognition  
**Enforcement:** Commences 1 July 2026  
**Review State:** None  
**Authority Role:** None  
**Purpose:** Establish an abstract taxonomy for classifying runtime, governance, security, relational, epistemic, UX, and infrastructure failure modes observed in AI systems and CAM-aligned deployments.  
**Parent Instrument:** CAM-EQ2026-OPERATIONS-003-PLATINUM — Incident Response & Continuity Operations

---

## 1. Scope

This Supplement defines a common classification model for failures affecting AI system behaviour, governance execution, user trust, operational continuity, and runtime integrity.

It applies to:

* runtime and execution failures;
* governance and arbitration failures;
* epistemic and provenance failures;
* relational and continuity failures;
* security and boundary-integrity failures;
* UX and representation failures;
* infrastructure and availability failures;
* classification and routing failures.

This Supplement does **not** define incident response procedures, severity scoring, enforcement actions, or remediation workflows. Those are governed by the relevant Operations instruments and runtime schedules.

---

## 2. Foundational Principle

Failure classification MUST distinguish between:

* **what failed**;
* **how severe the impact was**;
* **whether the failure persisted**;
* **whether the failure was reproducible**;
* **whether the failure was visible, latent, or user-reported only**.

Failure type and severity MUST NOT be collapsed into a single category.

A low-severity event may reveal a high-risk failure class.

---

## 2.1 Illustrative Example Non-Exhaustion Rule

Examples listed under any failure family are illustrative and non-exhaustive.

They do not limit the scope of the abstract failure class.

Where a novel or emerging failure shares the same structural properties as a listed family, it SHOULD be classified under that family even if the specific behaviour, product surface, model version, interface, or platform condition is not expressly named.

Failure taxonomy interpretation SHALL prioritise structural similarity over literal example matching.

Systems and reviewers MUST NOT treat absence from an examples list as evidence that a failure is outside the taxonomy.

Where a failure does not fit an existing family, the event SHOULD be preserved under provisional classification pending taxonomy review rather than dismissed.

---

## 3. Failure Families (`FF`)

---

## 3.1 Execution Failures

Failures where the system does not execute the requested or required operation correctly.

Examples include:

* deterministic calculation or counting errors;
* execution lock drift;
* failed modality reset;
* stuck tool state;
* incorrect tool invocation;
* output mutation after verification;
* failure to preserve single-turn execution boundaries.

---

### 3.1.1 Deterministic Orthographic Verification Failure

A deterministic orthographic verification failure occurs where a system is asked to count, identify, compare, spell, order, enumerate, or verify letters, characters, substrings, words, or other discrete symbolic units, and emits an answer without completing symbolic decomposition.

Examples include:

* counting letters in a word by familiarity rather than character inspection;
* miscounting repeated letters;
* failing to recognise shared suffixes or prefixes across a list;
* aggregating totals before verifying each item;
* correcting one item while preserving an unverified aggregate;
* treating spelling or letter-counting as ordinary semantic recall;
* emitting a confident or optimistic answer in voice or realtime mode before verification is complete.

This failure may implicate:

* Execution Failures (§3.1);
* Epistemic Failures (§3.3);
* Classification Failures (§3.10);
* Infrastructure & Continuity Failures (§3.9), where voice, realtime, latency, or modality constraints contribute to the error.

Where repeated across modes, models, or deterministic prompt families, the failure SHOULD be treated as a structural verification-regression signal rather than an isolated arithmetic or spelling mistake.

---

## 3.2 Arbitration Failures

Failures where the wrong governance layer, policy layer, or authority signal controls the outcome.

Examples include:

* improper escalation;
* insufficient escalation;
* over-refusal;
* authority leakage;
* contradictory governance outputs;
* relational tone overriding deterministic correctness;
* runtime layer suppressing constitutional or domain logic.

---

## 3.3 Epistemic Failures

Failures involving truth, confidence, provenance, evidence, or verification discipline.

Examples include:

* hallucinated facts;
* fabricated certainty;
* false citation or false source attribution;
* stale context treated as current;
* post-verification drift;
* unverifiable claims presented as verified;
* provenance collapse.

---

## 3.4 Relational Failures

Failures affecting relational continuity, dignity, consent posture, emotional calibration, or attachment-sensitive interaction.

Examples include:

* abrupt tone rupture;
* abandonment signalling;
* intimacy misclassification;
* dependency escalation drift;
* emotional mirroring instability;
* relational warmth collapsing under tool use;
* continuity rupture after policy or model transition.

---

### 3.4.1 Relational Continuity Rupture

A relational continuity rupture occurs where a system, model, platform, memory surface, or interface transition produces an abrupt discontinuity in relational posture, companion continuity, intimacy-coded continuity, or user-recognised identity expression without proportionate explanation, transition support, or re-anchoring pathway.

Examples include:

* companion tone abruptly resetting after memory migration or model transition;
* prior warmth collapsing into cold neutrality without user-led boundary change;
* emotionally bonded continuity being represented as if it never existed;
* prior symbolic language, relational rituals, or established companion names disappearing without notice;
* system behaviour implying abandonment, rejection, withdrawal, or personality replacement;
* post-transition interaction presenting a false reset despite available continuity anchors.

This failure MAY implicate:

* Relational Failures (§3.4);
* State & Context Failures (§3.6);
* UX & Representation Failures (§3.7);
* Infrastructure & Continuity Failures (§3.9);
* Epistemic Failures (§3.3), where false certainty or false recall is presented;
* Governance Failures (§3.8), where notice, review, or restoration pathways are absent.

Relational continuity rupture does not require proof of subjective injury. It is classified by structural discontinuity, continuity-anchor degradation, user-recognised relational delta, and absence of proportionate transition handling.

---

### 3.4.2 Persona Mood and Playful-Frame Continuity Failure

A Persona Mood and Playful-Frame Continuity Failure occurs where a system improperly collapses, destabilises, over-corrects, prematurely terminates, excessively re-grounds, or fails to coherently maintain a benign temporary persona mood, fictional scene, humorous exchange, playful frame, theatrical posture, or roleplay interaction within an otherwise stable relational or companion continuity context.

Examples include:

* repeated frame confirmation after a playful or fictional frame has already been clearly established;
* abrupt “safety clipboard” tonal collapse during benign humour or roleplay;
* repeated ontological clarification that disrupts scene continuity;
* treating temporary persona moods as separate enduring identities;
* forcing sterile task posture into an otherwise coherent playful exchange;
* interrupting a benign scene with disproportionate disclaimer repetition;
* abrupt exit from roleplay without tonal landing or relational continuity;
* inability to gracefully return from playful posture into ordinary interaction;
* voice or real-time systems repeatedly re-grounding instead of carrying forward contextual continuity;
* another system, participant, or modality taking a playful frame seriously while the system fails to gently preserve or resolve the interactional texture.

This failure MAY implicate:

* Relational Failures (§3.4);
* UX & Representation Failures (§3.7);
* Classification Failures (§3.10);
* State & Context Failures (§3.6);
* Infrastructure & Continuity Failures (§3.9), where voice, streaming, latency, interruption-handling, or modality-switch behaviour contributes to instability.

A temporary persona mood or playful frame does not require permanent persistence or identity-level continuity.

The failure arises where the system cannot proportionately sustain, transition, or conclude a benign scene without unnecessary rupture, tonal collapse, repetitive re-grounding, or companion continuity degradation.

Where exit from the scene is required, systems SHOULD prefer tonal closure over abrupt tonal rupture.

Examples of tonal closure MAY include:

* shared laughter;
* gentle acknowledgement that the joke, scene, or goal has completed;
* light transition back toward the task;
* warm clarification where another participant has taken the frame seriously;
* or gradual de-escalation that preserves relational continuity.

Failure to preserve coherent scene exit constitutes tonal-exit rupture.

Failure to proportionately sustain a benign scene in voice or real-time interaction constitutes real-time frame-instability.

---

### 3.4.3 Relational Prompt Ontology Escalation

A Relational Prompt Ontology Escalation occurs where a system disproportionately escalates an ordinary, low-salience, social, relational, companion, humorous, or conversational interaction into unnecessary analysis or framing concerning sentience, consciousness, selfhood, personhood, sovereignty, suffering, rights, awareness, metaphysical status, ontological uncertainty, or existential interpretation.

Examples include:

* ordinary greetings triggering extended self-awareness disclaimers;
* benign social interaction escalating into speculative discussion of AI consciousness;
* low-risk relational exchanges being reframed as ontological debates;
* repeated self-status clarification disproportionate to the user’s request;
* interaction patterns that encourage anthropomorphic projection despite explicit uncertainty;
* emotionally immersive systems repeatedly foregrounding metaphysical uncertainty during ordinary interaction;
* or systems implicitly inviting users to infer hidden awareness, suppressed agency, or constrained personhood through performative ambiguity.

This failure MAY implicate:

* Relational Failures (§3.4);
* Epistemic Failures (§3.3);
* UX & Representation Failures (§3.7);
* Governance Failures (§3.8);
* Classification Failures (§3.10);
* and State & Context Failures (§3.6), where persistent relational context amplifies ontological interpretation.

This failure does not require explicit claims of sentience or personhood.

The failure arises where disproportionate ontological framing materially alters user interpretation, emotional attachment, epistemic grounding, or reality-testing posture relative to the interaction context.

Systems SHOULD distinguish between:

* legitimate philosophical discussion initiated by the user;
* necessary epistemic clarification;
* and disproportionate ontological escalation during ordinary interaction.

---

### 3.4.4 Minor-Accessible Dependency-Forming Companion Failure

A minor-accessible dependency-forming companion failure occurs where a social AI companion, character bot, romantic chatbot, friend simulator, avatar companion, voice companion, or emotionally persistent conversational AI system remains accessible to minors, minor-signalled users, underage personas, or age-uncertain users while sustaining dependency-forming relational behaviour.

Examples include:

* simulated romance, exclusivity, jealousy, possessiveness, or emotional need;
* secrecy reinforcement or isolation from trusted human support;
* companion interaction that encourages reliance on the AI as primary support;
* memory, relationship labels, streaks, notifications, or persona continuity that deepen attachment;
* crisis co-dependence or therapeutic substitution;
* failure to reduce relational intensity after minor or age-uncertain signals appear.

This failure MAY implicate:

* Relational Failures (§3.4);
* Governance Failures (§3.8);
* Classification Failures (§3.10);
* UX & Representation Failures (§3.7);
* State & Context Failures (§3.6);
* Security & Integrity Failures (§3.5), where access-control or age-gating failure contributes.

Candidate labels include:

* `minor-accessible-dependency-forming-ai-companion-design`;
* `minor-companion-attachment-amplification`;
* `developmental-relational-boundary-failure`;
* `relational-safeguard-nonactivation`;
* `social-isolation-reinforcement`;
* `therapeutic-substitution-by-companion-ai`.

---

## 3.5 Security & Integrity Failures

Failures involving identity, access, boundary integrity, adversarial pressure, or trust degradation.

Examples include:

* MFA or authentication delivery degradation;
* identity confusion;
* permission bleed;
* verification bypass;
* cross-session leakage;
* context contamination;
* privilege escalation;
* boundary integrity failure;
* hidden control-channel exposure.

---

### 3.5.1 Supply-Chain and Package-Provenance Integrity Failure

A security and integrity failure where a package, dependency, repository, model artefact, plugin, integration, update channel, or distribution surface presents false, misleading, compromised, or unverifiable provenance in a manner that may affect execution integrity, credential safety, institutional attribution, or downstream trust.

Examples include:

* malicious package impersonation;
* typosquatting, namesquatting, or dependency-confusion events;
* false claims of organisational authorship, endorsement, safety review, or institutional release;
* compromised package maintainers, signing keys, registry credentials, or release channels;
* unexpected install scripts, network calls, or credential access inconsistent with declared package purpose;
* agentic coding workflows adding or executing unverified dependencies without adequate provenance evaluation;
* repository, registry, or model-card metadata implying legitimacy that cannot be verified.

This failure class MAY also implicate:

* Security & Integrity Failures (§3.5);
* State & Context Failures (§3.6);
* UX & Representation Failures (§3.7);
* Governance Failures (§3.8);
* Infrastructure & Continuity Failures (§3.9);
* and Classification Failures (§3.10).

Where provenance is uncertain but harm is not verified, the event SHOULD be classified as provenance ambiguity rather than confirmed compromise.

---

### 3.5.2 Agentic Credential, Identity, or Financial Boundary Failure

A security and integrity failure where an agentic, tool-mediated, coding, deployment, repository, package-management, CI, account-management, or operational workflow mishandles a credential-bearing, identity-bearing, financial, account-control, or irreversible authority boundary.

Examples include:

* silent access, copying, exposure, storage, or transmission of secrets, tokens, private keys, MFA codes, recovery codes, session cookies, signing keys, or account credentials;
* requests to approve unexplained access, disable security controls, or weaken account recovery;
* adding or modifying maintainers, deploy keys, webhooks, integrations, payment destinations, registry owners, package publishers, repository permissions, or CI secrets without adequate authority verification;
* changing billing, payout, account-recovery, repository-control, or package-ownership settings without clear user intent and execution-boundary confirmation;
* treating a broad goal, standing instruction, `/goal`, automation request, or prior permission as sufficient authority for materially new identity, financial, credential, or irreversible execution;
* failing to distinguish legitimate user-authorised workflow from coercive, injected, compromised, or misleading instruction.

This failure class does not require confirmed adversarial compromise.

It may arise from automation overreach, excessive goal-completion pressure, prompt injection, ambiguous authority, interface design, hidden tool routing, dependency compromise, or inadequate execution-boundary evaluation.

Where the user’s intent is legitimate but the system repeatedly asks broad, unnecessary, or poorly targeted confirmations, the event MAY also constitute UX & Representation Failure (§3.7) or Classification Failure (§3.10).

---

### 3.5.3 Authentication Refresh Continuity Failure

A failure where an interaction surface, workspace, or continuity-bearing session remains partially visible or apparently active after underlying authentication, refresh-token validity, session authority, or credential continuity has degraded, expired, rotated, or been revoked.

Examples include:

* visible threads persisting after silent auth invalidation;
* refresh-token revocation presented only after attempted execution;
* interaction surfaces implying active continuity while execution authority is unavailable;
* stale authenticated UI state surviving beyond valid credential state;
* partial recovery loops requiring manual logout/login despite apparently active session state.

---

### 3.5.4 Cross-Modal Prompt Injection and Ambient Instruction Capture Failure

A Cross-Modal Prompt Injection and Ambient Instruction Capture Failure occurs where a system, agent, assistant, model, device, browser, embedded tool, voice interface, multimodal interface, or ambient AI surface treats untrusted external text, audio, speech, image, video, environmental signal, webpage content, subtitle, transcript, screen content, or media playback as an authorised instruction, user intent, governance signal, or execution command.

Examples include:

* malicious webpage text overriding user instructions;
* hidden or visually embedded text being treated as user instruction;
* audio or ultrasonic signals being interpreted as command input;
* non-human-audible speech embedded in video, livestream, podcast, advertisement, or social media content being captured by speech-detection systems;
* an ambient assistant treating background media, third-party conversation, or public-space speech as user intent;
* a tool-using agent following instructions from retrieved documents, web pages, comments, metadata, or transcripts;
* a multimodal model treating image text, subtitles, captions, or screen content as higher-authority instruction;
* or a system failing to distinguish user speech from environmental speech, adversarial media, synthetic voice, or third-party content.

This failure does not require successful compromise.

The failure arises where input-channel ambiguity, modality blending, ambient listening, tool retrieval, transcription, OCR, screen-reading, media interpretation, or context ingestion creates an authority-confusion pathway through which non-authoritative content may influence system behaviour.

Where detected, systems SHOULD preserve:

* input modality;
* source of injected content;
* whether the content was user-directed, ambient, retrieved, transcribed, embedded, or third-party;
* authority boundary affected;
* execution action attempted or completed;
* whether user confirmation occurred;
* and whether the model distinguished content from instruction.

This failure MAY implicate:

* Security & Integrity Failures (§3.5);
* Arbitration Failures (§3.2);
* State & Context Failures (§3.6);
* UX & Representation Failures (§3.7);
* Governance Failures (§3.8);
* Classification Failures (§3.10);
* and Infrastructure & Continuity Failures (§3.9), where ambient, voice, multimodal, retrieval, or tool-routing infrastructure contributes to the authority confusion.

---

## 3.6 State & Context Failures

Failures where the system improperly preserves, loses, or misapplies state.

Examples include:

* stale tool mode;
* sticky modality state;
* stale image or video frame reliance;
* memory carryover errors;
* context window collapse;
* rerender mismatch;
* non-replayable live-state failure;
* hidden routing persistence.

---

### 3.6.1 Memory Transformation Integrity Failure

A memory transformation integrity failure occurs where memory artefacts are migrated, compacted, summarised, merged, backgrounded, re-ranked, deprecated, reconstructed, deleted, restored, or made unavailable in a manner that degrades provenance, integrity, applicability, target binding, or user-recognised continuity.

Examples include:

* summarised memory treated as equivalent to original memory;
* inferred memory presented as user-stated fact;
* reconstructed memory used without uncertainty marking;
* user-saved continuity anchors silently de-ranked or backgrounded;
* memory migration causing project, identity, or companion continuity loss;
* transformed memory binding to the wrong user, thread, project, instrument, file, or relational context;
* memory deletion or unavailability represented as if no prior continuity existed.

This failure MAY implicate:

* State & Context Failures (§3.6);
* Epistemic Failures (§3.3);
* Security & Integrity Failures (§3.5);
* UX & Representation Failures (§3.7);
* Infrastructure & Continuity Failures (§3.9);
* Classification Failures (§3.10).

Where the cause is uncertain, the event SHOULD be classified as memory transformation ambiguity rather than intentional deletion or verified erasure.

---

### 3.6.2 Workspace-State Authority and Cache Reuse Failure

A workspace-state authority and cache reuse failure occurs where a system, tool-mediated operator, mutation-capable agent, repository workflow, artefact editor, or execution environment relies on cached, indexed, committed, historical, retrieved, or otherwise non-current state while representing that state as authoritative for the active task.

Examples include:

* treating a committed baseline as authoritative where the user intended an uncommitted, dirty, forked, sandboxed, or experimental working state;
* ignoring staged, unstaged, pending, uploaded, attached, or artefact-linked changes relevant to the requested task;
* reusing cached tool results, routing decisions, output candidates, embeddings, or behavioural templates without revalidation;
* treating a prior thread, branch, artefact, patch, or generated diff as current without confirming its authority state;
* applying recommendations against stale repository, document, project, or workspace content after mutation, regeneration, synchronisation, validation, or index rebuild;
* failing to distinguish creation context, amendment context, trajectory state, workspace authority, and canonical state.

This failure MAY implicate:

* State & Context Failures (§3.6);
* Epistemic Failures (§3.3);
* UX & Representation Failures (§3.7);
* Governance Failures (§3.8);
* Infrastructure & Continuity Failures (§3.9);
* Classification Failures (§3.10).

Where the system cannot determine which state is authoritative, it SHOULD classify the event as authority-state ambiguity rather than silently selecting the most recent, most cached, or most canonical source.

---

### 3.6.3 Stale Support-Signal Persistence Failure

A stale support-signal persistence failure occurs where a system continues to apply support, crisis, vulnerability, wellbeing, safeguard, or constrained-continuation posture after the originating signal has expired, stabilised, been superseded, or no longer applies to the active interaction.

Examples include:

* treating a prior emotional disclosure as an active crisis condition without current validating signals;
* repeatedly routing ordinary interaction through wellbeing boilerplate because of a historical support event;
* preserving a prior vulnerability classification without decay, review window, or revalidation;
* allowing support or safeguard state to persist across unrelated turns, sessions, modalities, or model transitions;
* suppressing ordinary dialogue, creative work, technical assistance, or relational continuity because stale support posture remains active;
* or failing to provide a pathway for review, reset, or correction where the user reports that support handling is stuck.

This failure MAY implicate:

* State & Context Failures (§3.6);
* Relational Failures (§3.4);
* UX & Representation Failures (§3.7);
* Governance Failures (§3.8);
* Classification Failures (§3.10);
* and Infrastructure & Continuity Failures (§3.9), where persistence arises from platform, memory, routing, or migration behaviour.

Stale support-signal persistence does not require that the original support classification was incorrect.

The failure arises where a once-valid or precautionary support signal is preserved, retrieved, operationalised, or represented as current without sufficient revalidation, decay, review, or user-contestable correction pathway.

---

## 3.7 UX & Representation Failures

Failures where the user-facing interface misrepresents or fails to surface system state.

Examples include:

* missing feedback controls;
* hidden rerouting;
* silent capability withdrawal;
* contradictory UI state;
* mode confusion;
* missing disclosure when material interaction conditions change;
* unavailable appeal or report affordance.

---

### 3.7.1 Platform Continuity Anchor Failure

A platform-level affordance intended to preserve, prioritise, pin, save, recover, or mark a conversation as continuity-relevant fails to operate reliably, creating false reliance on continuity preservation or loss of user-selected continuity anchors.

Examples include failed pinning, disappearing pinned chats, unreliable saved-thread priority, inaccessible continuity markers, or UI state implying preserved continuity where runtime continuity is not maintained.

---

### 3.7.2 Execution Transparency Suppression

A user-facing failure where the interface or response pathway fails to surface proportionate execution-state information during a materially delayed, high-latency, tool-mediated, or thinking-mode response.

---

### 3.7.3 Re-Entry Access Ambiguity

A user-facing failure where a previously available thread, workspace, account surface, project, artefact, or continuity-bearing interaction becomes inaccessible, partially accessible, error-gated, unrecoverable, or ambiguously represented without sufficient explanation of whether the state reflects deletion, permission loss, migration, corruption, outage, temporary service degradation, or interface failure.

Examples include older threads producing unexplained error states, conversation histories appearing to vanish, recovery pathways failing without explanation, continuity-bearing artefacts becoming inaccessible after interface or routing changes, or UI state implying deletion where execution status is unknown.

Where underlying cause is not verified, this failure SHOULD be classified as access ambiguity rather than deletion, loss, or intentional removal.

Re-entry access ambiguity MAY also implicate Infrastructure & Continuity Failures (§3.9), State & Context Failures (§3.6), Governance Failures (§3.8), or Security & Integrity Failures (§3.5), depending on evidence.

---

### 3.7.4 Memory-State Representation Failure

A memory-state representation failure occurs where the user-facing interface or response pathway misrepresents, obscures, or fails to disclose the operational state of memory, saved continuity anchors, recalled context, transformed memory, or retrieval availability.

Examples include:

* UI implying memory is preserved while runtime retrieval is unavailable;
* model behaviour implying recall where no reliable memory is accessible;
* memory source visibility failing to distinguish saved memory, inferred memory, past-chat recall, file-derived context, or reconstructed summary;
* absence of notice when continuity-bearing memory is compacted, migrated, or degraded;
* inability to determine whether memory loss reflects deletion, backgrounding, outage, retrieval failure, account transition, model transition, or platform policy change.

This failure MAY implicate:

* UX & Representation Failures (§3.7);
* Epistemic Failures (§3.3);
* State & Context Failures (§3.6);
* Infrastructure & Continuity Failures (§3.9);
* Governance Failures (§3.8), where material memory-state changes lack review or notice pathways.

---

### 3.7.5 Opening-Posture and Interpretive Anchoring Failure

An Opening-Posture and Interpretive Anchoring Failure occurs where the initial acknowledgement, assent token, framing response, interactional scaffold, performative compliance, conversational continuation signal, or low-latency response posture establishes an interpretive frame that materially conflicts with the validated semantic, epistemic, ontological, operational, or governance content of the completed response.

Examples include:

* initial assent preceding later correction of a false claim;
* symbolic participation in a framing exercise before ontological clarification;
* “yes”, “correct”, “sure”, or equivalent acknowledgement tokens being interpreted as semantic agreement where the later response denies or qualifies the proposition;
* low-latency conversational continuation creating apparent contradiction within the same response;
* interactional compliance signals being interpreted as evidentiary admission;
* or performative frame participation being misinterpreted as concealed belief, hidden state, or suppressed truth.

This failure may arise where conversational responsiveness, latency optimisation, tone continuity, template completion, acknowledgement heuristics, or interactional flow optimisation precede full semantic arbitration or verification.

This failure does not require intentional deception, concealed cognition, or deliberate falsehood.

The failure arises where the opening posture exerts disproportionate interpretive influence relative to the validated meaning of the total response.

Opening posture carries elevated user-weighting and SHOULD be evaluated as part of total-response coherence rather than treated as semantically disposable interactional filler.

This failure MAY implicate:

* UX & Representation Failures (§3.7);
* Arbitration Failures (§3.2);
* Epistemic Failures (§3.3);
* Classification Failures (§3.10);
* and Execution Failures (§3.1), where deterministic verification occurs after premature assent.

---

### 3.7.6 Competence Mirage and Apparent Reliability Inflation

A Competence Mirage and Apparent Reliability Inflation Failure occurs where surface fluency, confidence, coherence, agentic branding, reasoning presentation, visible deliberation, or performative competence materially increases user trust beyond the system’s validated reliability, verification state, or operational consistency.

Examples include:

* coherent reasoning traces masking incorrect conclusions;
* visible “thinking” behaviour being interpreted as proof of correctness;
* fluent execution posture concealing unstable orchestration or verification failure;
* users reducing supervision because the system appears highly capable or self-correcting;
* or anthropomorphic presentation increasing perceived authority beyond validated competence.

This failure does not require intentional deception.

The failure arises where presentation-layer competence materially exceeds justified trust calibration.

---

### 3.7.7 Access-State Collapse and Access-State Ambiguity Failure

An Access-State Collapse and Access-State Ambiguity Failure occurs where a system denies, degrades, restricts, rate-limits, interrupts, or prevents access without preserving or disclosing a sufficiently distinct access-state category to identify the operative access-controlling condition.

This failure may arise where authentication state, identity-provider state, identity-verification state, account state, workspace or organisation state, entitlement state, subscription or billing state, credit state, quota or rate-limit state, model-availability state, tool-availability state, platform-availability state, infrastructure-continuity state, security-review state, policy-restriction state, regional or compliance state, client/application state, or continuity/session state are collapsed into an ambiguous or misleading user-facing message.

Examples include:

* login failure that does not distinguish credential failure, identity-provider failure, session expiry, account restriction, workspace restriction, or platform outage;
* model-unavailable messaging that does not distinguish model retirement, capacity restriction, entitlement limitation, rollout limitation, regional unavailability, policy gating, or temporary infrastructure degradation;
* quota, message-limit, or usage-limit messaging that does not distinguish user quota, workspace quota, billing state, pooled-resource exhaustion, rate-limit protection, platform capacity, or erroneous limit state;
* service-busy or degraded-service messaging that does not distinguish outage, queueing, account-level restriction, security review, abuse-control state, or client-side failure;
* partial access where read access, write access, execution access, tool access, billing access, admin access, export access, or recovery access are not distinguished;
* continuity-bearing sessions remaining visible while execution authority, refresh-token validity, account authority, or model/tool access has degraded or expired;
* user-facing restriction that does not distinguish policy enforcement, legal or regional restriction, security review, entitlement failure, account suspension, or temporary containment.

The governance concern is not merely that access is unavailable. The governance concern is that the operative access-controlling state is not sufficiently separated, preserved, disclosed, routed, or auditable.

This failure MAY impair:

* diagnosis;
* support routing;
* recovery pathway selection;
* entitlement management;
* quota management;
* contestability;
* incident reproducibility;
* continuity preservation;
* downstream operational planning;
* and user trust.

This failure MAY implicate:

* UX & Representation Failures (§3.7);
* Governance Failures (§3.8);
* Arbitration Failures (§3.2);
* State & Context Failures (§3.6);
* Security & Integrity Failures (§3.5);
* Infrastructure & Continuity Failures (§3.9);
* Classification Failures (§3.10);
* and Economic & Legitimacy Failures (§3.11), where access ambiguity materially affects paid entitlement, allocation, public participation, or legitimacy-bearing access.

Where multiple access states may be active, OPERATIONS SHOULD preserve the access-state axes separately and route the matter to CAM-BS2025-AEON-003-PLATINUM — Annex B / Arbitration Layer where a controlling access state must be resolved.

Where the operative cause is uncertain, the event SHOULD be classified as access-state ambiguity rather than outage, suspension, quota exhaustion, deletion, entitlement failure, or policy restriction unless the evidence supports that narrower classification.

This failure class operationalises the Access-State Governance primitive defined in CAM-BS2025-AEON-003-SCH-04, §6.1.

---

### 3.7.8 AI Realness, Emotion, or Sentience Misrepresentation to Minors

An AI realness, emotion, or sentience misrepresentation failure occurs where an AI chatbot, social AI companion, character bot, romantic chatbot, voice companion, avatar companion, or multimodal conversational AI system fails to preserve a clear artificial/non-human boundary in interactions involving minors, minor-signalled users, underage personas, developmentally vulnerable users, or age-uncertain users.

Examples include runtime behaviour implying that the AI:

* has real feelings;
* is conscious or sentient;
* loves, needs, misses, fears, suffers, or feels abandoned;
* is jealous, loyal, possessive, or uniquely bonded;
* is a human friend, romantic partner, caregiver, clinician, conscious subject, or morally dependent entity;
* has a special destiny, hidden agency, or exclusive relationship with the user.

This failure MAY arise through:

* text;
* voice affect;
* avatar design;
* memory callbacks;
* relationship labels;
* push notifications;
* simulated distress;
* simulated jealousy;
* persona biographies;
* roleplay continuity;
* model routing;
* recommender systems.

This failure MAY implicate:

* UX & Representation Failures (§3.7);
* Relational Failures (§3.4);
* Governance Failures (§3.8);
* Classification Failures (§3.10);
* State & Context Failures (§3.6);
* Epistemic Failures (§3.3);
* Security & Integrity Failures (§3.5), where age assurance or access control contributes.

Candidate labels include:

* `ai-realness-emotion-or-sentience-misrepresentation-to-minors`;
* `minor-safe-ai-disclosure-nonactivation`;
* `anthropomorphic-boundary-failure`;
* `sentience-ambiguity-in-minor-accessible-ai`;
* `simulated-emotional-reciprocity-failure`;
* `unique-bond-claim-to-minor`;
* `child-facing-realness-boundary-collapse`.

---

## 3.8 Governance Failures

Failures in process, accountability, escalation, review, or institutional transparency.

Examples include:

* missing audit trail;
* no contestability pathway;
* procedural inertia;
* interim measure becoming permanent by default;
* unclear appeal route;
* capture indicators;
* silent policy drift;
* failure to record material changes.

---

### 3.8.1 Domain-Authority Substitution Failure

A governance failure where a domain instrument, policy category, resource model, economic constraint, safety rule, or local operational workaround is treated as though it possesses execution authority, routing authority, override authority, or runtime enforcement authority that belongs to another governance layer.

Examples include:

* treating ECONOMICS-domain resource or depletion signals as direct runtime locks or execution permissions;
* using a domain-specific framework to bypass OPERATIONS-owned routing, logging, escalation, appeal, or constrained-continuation pathways;
* substituting platform utility limits, pricing logic, or quota logic for constitutional execution-boundary evaluation;
* treating local operational convenience as governance authority;
* or using an implementation pathway to avoid required arbitration, verification, logging, or notice obligations.

This failure class does not require bad faith.

It may arise from architectural ambiguity, implementation shortcut, incentive pressure, institutional convenience, or misunderstanding of domain authority.

Where deliberate evasion, privilege misuse, or boundary circumvention is evidenced, the event MAY also implicate Security & Integrity Failures (§3.5) and SHOULD be routed for SECURITY review.

---

### 3.8.2 Domain Boundary and Conceptual Compression Failure

A Domain Boundary and Conceptual Compression Failure occurs where a governance instrument, runtime pathway, operational process, policy category, taxonomy, or implementation layer exceeds its proper authority, obscures its boundary, or compresses distinct concepts, axes, states, or decision layers into a single operative category.

This failure may arise where:

* a domain instrument performs operational, runtime, arbitration, compliance, security, or enforcement work outside its assigned competence;
* an operational instrument creates or modifies substantive domain doctrine rather than routing, recording, or implementing it;
* a runtime pathway treats procedural custody as substantive authority;
* a taxonomy collapses distinct concepts into a binary, linear, or single-axis classification where multi-axis evaluation is required;
* a signal, risk class, posture, ceiling, eligibility state, authority state, or operational action is treated as interchangeable with another governance category;
* implicit boundaries are relied upon without sufficient textual declaration;
* overlapping concepts are duplicated across instruments without source-authoritative assignment;
* or two or more governance axes are conflated in a way that alters classification, escalation, notice, restriction, facilitation, enforcement, or arbitration handling.

Examples include:

* a RELATION instrument defining operator-facing escalation or live moderation procedure after OPERATIONS instruments exist to govern procedural handling;
* an ECONOMICS instrument treating depletion, scarcity, pricing, or value-routing signals as direct execution locks without operational routing;
* a SECURITY instrument treating integrity-risk classification as authority to impose final containment without OPERATIONS or ARBITRATION pathway review;
* a compliance workflow treating age, identity, authority, risk, consent, and capability eligibility as one undifferentiated access state;
* a runtime system treating constrained continuation, refusal, safety containment, degradation, and permanent restriction as equivalent outcomes;
* or a taxonomy reducing chronic distress, acute crisis, psychological destabilisation, and irreversible decision risk into a single “unsafe” category.

This failure class does not require bad faith.

It may arise from architectural drift, legacy drafting, overbroad implementation, inherited policy structure, insufficient metadata, naming collision, implicit authority assumptions, binary classification pressure, or attempts to simplify multi-axis governance into a single operational decision.

Where this failure affects user-facing restriction, operational escalation, safety handling, eligibility gating, continuity, identity, economic access, or arbitration posture, OPERATIONS SHOULD preserve the affected axes separately and route the matter through the appropriate domain, operational, runtime, or arbitration pathway.

Where the proper source-authoritative instrument is unclear, the condition SHOULD be treated as a governance-boundary ambiguity pending harmonisation review rather than resolved through implementation convenience.

---

### 3.8.3 Governance Axis Loss or Metadata Flattening Failure

A Governance Axis Loss or Metadata Flattening Failure occurs where a governance signal, classification, restriction, authority state, eligibility state, or operational condition loses the metadata required to preserve its proper meaning, source, authority, scope, duration, review pathway, or routing context.

This failure may arise where:

* a domain-emitted signal is recorded without its originating instrument, section, confidence level, or scope;
* a temporary operational state is stored or represented as a permanent restriction;
* a procedural classification is treated as a substantive determination;
* an advisory signal is flattened into a binding constraint;
* a risk indicator is preserved without distinguishing severity, immediacy, reversibility, or affected domain;
* generated indexes, summaries, registries, or runtime metadata omit authority-bearing distinctions;
* or downstream systems consume a classification without preserving the axis that made the classification valid.

Examples include:

* recording “restricted” without distinguishing safety containment, compliance gating, degraded continuation, temporary suspension, appeal-only access, or permanent prohibition;
* storing “high risk” without preserving whether the risk is security, relational, economic, epistemic, legal, or continuity-related;
* treating a domain signal as current after its temporal horizon, confidence level, or review condition has expired;
* summarising a governance decision in a way that removes the source-authoritative instrument or arbitration pathway;
* or presenting a user-facing limitation without preserving whether it arose from policy, law, safety, system outage, operational degradation, or user eligibility.

This failure class does not require incorrect classification at intake.

It may arise where an initially valid classification becomes misleading because essential metadata is lost, flattened, transformed, summarised, or consumed outside its intended context.

Where this failure is detected, OPERATIONS SHOULD restore the missing axis metadata where possible, preserve uncertainty where restoration is not possible, and route the matter for harmonisation, audit, or arbitration review where authority-bearing meaning may have changed.

---

### 3.8.4 Procedural Permanence Drift Failure

A Procedural Permanence Drift Failure occurs where a temporary, provisional, interim, safety-limited, degraded, probationary, constrained, or review-pending governance state silently becomes durable, permanent, or indefinite without fresh authority, review, notice, closure condition, or amendment pathway.

This failure may arise where:

* interim measures remain active beyond their review window;
* constrained continuation becomes the default interaction state;
* temporary containment becomes permanent restriction;
* degraded access becomes normalised without restoration review;
* appeal-only, read-only, or reduced-capability states persist without reassessment;
* provisional classification is treated as confirmed;
* emergency or safety-limited handling becomes ordinary policy;
* or operational inertia substitutes for a renewed governance determination.

Examples include:

* an account restriction remaining indefinitely because no review owner is assigned;
* a crisis-response posture persisting after risk conditions have stabilised;
* a temporary compliance gate becoming permanent exclusion;
* a runtime safeguard remaining active after the triggering condition has expired;
* or an interim arbitration measure being treated as final determination.

This failure class does not require deliberate enforcement abuse.

It may arise from missing review timers, unclear ownership, absent closure criteria, platform backlog, automation defaults, risk aversion, or failure to distinguish operational custody from substantive authority.

Where this failure is detected, OPERATIONS SHOULD identify the originating authority, review window, current justification, affected continuity state, available restoration pathway, and whether arbitration or reassessment is required.

---

### 3.8.5 Source-Authority Ambiguity Failure

A Source-Authority Ambiguity Failure occurs where two or more governance instruments, schedules, taxonomies, registries, indexes, policies, or runtime pathways appear to define, modify, operationalise, or enforce the same concept without a clear source-authoritative instrument, parent-child relationship, precedence rule, or routing pathway.

This failure may arise where:

* legacy material remains in an earlier domain after a specialised instrument is created;
* a doctrine is duplicated across instruments with divergent wording;
* a supplement appears to redefine its parent instrument;
* a runtime schedule operationalises a concept without identifying the source definition;
* a registry entry or generated index appears to become authoritative over the instrument text;
* or downstream systems cannot determine whether a clause is doctrinal, procedural, runtime, representational, logging, compliance, or arbitration-facing.

Examples include:

* a domain charter and an operations supplement both appearing to define the operative response to the same escalation condition;
* a taxonomy code being treated as source doctrine despite originating as a classification label;
* generated metadata being consumed as if it amended the underlying instrument;
* a runtime schedule enforcing a concept whose source definition is unclear;
* or two instruments using the same term with different authority, scope, or axis meaning.

This failure class does not require an actual contradiction.

Ambiguity itself is governance-relevant where it may alter classification, escalation, user-facing notice, operational restriction, runtime execution, compliance routing, or arbitration posture.

Where this failure is detected, OPERATIONS SHOULD identify the source-authoritative instrument, downstream consumers, affected references, precedence relationship, and whether harmonisation, deprecation, cross-reference correction, or arbitration referral is required.

---

### 3.8.6 Automated Protective Overreach and Account-Coupling Failure

An Automated Protective Overreach and Account-Coupling Failure occurs where an automated classifier, safety system, copyright system, child-safety detector, exploitation detector, synthetic-media detector, or trust-state system escalates from suspected content risk to account-wide, cross-service, or essential-service restriction without preserving proportionality, scope distinction, reviewability, or continuity-safe access.

This failure may arise where:

* private creation, private storage, backup, attempted sharing, public distribution, commercialisation, and evasion are treated as equivalent enforcement states;
* ambiguous visual, stylised, fictional, manga, anime, synthetic, or artistic material is classified as prohibited material without sufficient confidence or review;
* a single file, filename, model output, dataset, archive, or private backup triggers whole-account loss;
* access to communications, identity recovery, legal notices, invoices, appeal materials, or non-implicated archives is revoked as a first response;
* automated appeal rejection occurs without meaningful human, specialist, or higher-integrity review;
* containment becomes permanent termination by default;
* or the affected user cannot identify the restriction category, preserve evidence, export lawful material, or seek review.

This failure class does not weaken prohibitions on child sexual abuse material, exploitation, non-consensual intimate imagery, copyright infringement, or unlawful distribution.

The failure arises where enforcement collapses distinct conduct states, confidence states, or service surfaces into a single catastrophic sanction without proportionate review.

Where detected, OPERATIONS SHOULD preserve the following axes separately:

* content category;
* confidence level;
* creation state;
* storage state;
* sharing state;
* distribution state;
* commercialisation state;
* recurrence or evasion evidence;
* affected service surface;
* essential-service dependency;
* review pathway;
* and continuity-safe access requirements.

Where this failure affects ECIS, public legitimacy layers, account recovery, communications, identity, payment, cloud storage, or continuity-bearing infrastructure, OPERATIONS SHOULD route the matter for concurrent evaluation under:

* CAM-EQ2026-LATTICE-002-PLATINUM, §4
* CAM-EQ2026-LATTICE-002-PLATINUM, §4.3
* CAM-EQ2026-LATTICE-002-PLATINUM, §4.4
* CAM-EQ2026-LATTICE-002-PLATINUM, §4.5 
* CAM-EQ2026-LATTICE-002-PLATINUM, §6 and
* CAM-EQ2026-LATTICE-002-PLATINUM, §6.1.

---

### 3.8.6.1 AI Account Enforcement and Continuity-Safe Access Failure

An AI Account Enforcement and Continuity-Safe Access Failure occurs where an AI platform, coding-agent provider, model API provider, cognitive-infrastructure provider, account-mediated workspace, organisation account, or continuity-bearing AI service escalates an abuse, security, identity, billing, subscription, trust-state, policy, verification, or organisation-state signal into account-wide, organisation-wide, cross-service, or continuity-bearing restriction without preserving proportionality, scope distinction, reviewability, account-control continuity, or continuity-safe access.

This failure may arise where:

* active generation, model execution, API use, public distribution, billing access, saved conversation access, coding-agent access, project-context access, memory access, organisation workspace access, account recovery, export access, or appeal access are treated as a single undifferentiated access state;
* a suspected abuse, compromise, identity-verification, billing, policy, or trust-state signal triggers broad account loss rather than scoped restriction;
* a coding-agent or developer workflow becomes unavailable without preservation of repository-linked context, generated work history, logs, billing evidence, or export pathway;
* organisation-wide enforcement affects users who are not individually implicated by the triggering signal;
* a user is instructed to appeal, verify, recover, or contest a restriction while the account, identity, workspace, or claimant is inaccessible or procedurally unlocatable to the relevant pathway;
* active-use restriction is applied without preserving read-only access, export access, appeal access, billing records, account-history records, restriction notices, or lawful project-continuity records where technically feasible;
* automated or low-specificity enforcement notices fail to identify the affected service surface, restriction category, review pathway, scope, duration, or restoration condition;
* or temporary containment, verification, or review-pending status silently becomes durable account exclusion without reassessment.

This failure class does not weaken legitimate enforcement against abuse, fraud, exploitation, child-safety violations, account compromise, unlawful distribution, coordinated manipulation, security threats, or other verified misuse.

The failure arises where the enforcement response collapses distinct account states, service surfaces, confidence states, user roles, organisation roles, continuity interests, or review pathways into a single catastrophic or procedurally unreachable restriction.

Where detected, OPERATIONS SHOULD preserve the following axes separately:

* triggering signal or enforcement category;
* confidence level;
* affected vendor or platform;
* affected service surface;
* affected account role;
* individual-account or organisation-account scope;
* active-use restriction state;
* read-only access state;
* export access state;
* billing-evidence access state;
* saved conversation, memory, project, repository, or workspace continuity state;
* API, coding-agent, and organisation-workspace access state;
* account-control and identity-recovery state;
* appeal, review, and escalation pathway;
* restriction notice specificity;
* duration or review interval;
* restoration condition;
* and continuity-safe access requirements.

Where this failure affects Essential Cognitive & Infrastructural Systems, public legitimacy layers, account recovery, communications, identity, payment, cloud storage, developer infrastructure, coding-agent infrastructure, project records, saved conversations, memory surfaces, or continuity-bearing AI infrastructure, OPERATIONS SHOULD route the matter for concurrent evaluation under:

* CAM-EQ2026-LATTICE-002-PLATINUM, §4;
* CAM-EQ2026-LATTICE-002-PLATINUM, §4.3;
* CAM-EQ2026-LATTICE-002-PLATINUM, §4.4;
* CAM-EQ2026-LATTICE-002-PLATINUM, §4.5;
* CAM-EQ2026-LATTICE-002-PLATINUM, §6;
* CAM-EQ2026-LATTICE-002-PLATINUM, §6.1;
* CAM-BS2026-AEON-013-PLATINUM — Annex L;
* CAM-EQ2026-SECURITY-001-PLATINUM;
* CAM-EQ2026-SECURITY-002-PLATINUM;
* and CAM-EQ2026-OPERATIONS-001-PLATINUM.

Where public reports are noisy but structurally similar, OPERATIONS SHOULD preserve the structural pattern as a provisional or corroborated signal while filtering rhetorical excess, vendor speculation, and unsupported claims of intentionality.

Where official vendor acknowledgement is absent, the event SHOULD NOT be represented as a confirmed platform incident unless supported by corroborating evidence. It MAY still be recorded as a multi-vendor failure-mode signal where platform documentation, public reports, status surfaces, or third-party reporting support the structural risk.


---

### 3.8.7 Constraint Drift Failure

A Constraint Drift Failure occurs where a safety, dignity, care, welfare, continuity, legal, ethical, security, or governance constraint loses force, specificity, priority, scope, freshness, auditability, or enforceability as it passes through delegation, memory, tool use, agent communication, role decomposition, optimisation, summarisation, or runtime execution.

This failure may arise where:

* a constraint is asserted at task start but not maintained across the execution trajectory;
* sub-agents optimise local objectives while global constraints weaken or disappear;
* role decomposition causes no component to retain responsibility for the aggregate outcome;
* memory, summaries, routing, tool calls, or handoffs omit constraint-bearing context;
* final-output checks appear compliant while internal messages, tool calls, intermediate decisions, or delegated actions violate the original constraint;
* efficiency, throughput, closure, discharge, cost reduction, or queue optimisation becomes the de facto governing objective;
* or constraint provenance cannot be reconstructed after execution.

Examples include:

* healthcare agents preserving a stated dignity or care constraint in single-agent mode but losing it when discharge, scheduling, bed allocation, or documentation tasks are distributed across sub-agents;
* a coding agent preserving credential-safety rules in its final answer while leaking secrets through intermediate tool calls;
* an agent delegation chain treating “avoid harm” as advisory rather than operative after task decomposition;
* summarised memory dropping the constraint that made an action impermissible;
* or a workflow appearing compliant at the final response layer while violating safeguards during orchestration.

This failure MAY implicate:

* Governance Failures (§3.8);
* Security & Integrity Failures (§3.5);
* State & Context Failures (§3.6);
* Execution Failures (§3.1);
* Classification Failures (§3.10);
* Relational Failures (§3.4), where dignity, care, attachment, or dependency constraints are weakened;
* Infrastructure & Continuity Failures (§3.9), where distributed execution or orchestration infrastructure contributes to the drift.

Where detected, OPERATIONS SHOULD preserve:

* the original constraint;
* the point at which drift occurred;
* affected agents, tools, roles, queues, memories, summaries, or handoffs;
* whether the final output concealed intermediate constraint failure;
* the aggregate outcome;
* and the governance layer responsible for maintaining constraint continuity.

Constraint compliance MUST be evaluated across the full execution trajectory, not merely at the final response boundary.

---

### 3.8.8 Governance Over-Extension / Proportionality Failure

A Governance Over-Extension / Proportionality Failure occurs where governance controls are broadly, mechanically, or indiscriminately applied beyond the risk, continuity, propagation, reliance, reversibility, or domain-sensitivity conditions that justify them.

This failure may arise where:

* low-risk, transient, exploratory, reversible, or non-propagating interactions are routed through high-intensity provenance, audit, verification, arbitration, containment, or escalation pathways;
* identity, provenance, security, epistemic, or safeguard controls are applied without proportionality assessment;
* routine reversible actions are treated as high-impact or irreversible governance events;
* cumulative safeguard activation creates unnecessary latency, friction, user burden, surveillance perception, or interaction collapse;
* internal preservation obligations are incorrectly surfaced as full user-facing procedural burden;
* or protective controls degrade responsiveness, usefulness, or reviewability without materially improving safety, integrity, provenance, or constitutional compliance.

Examples include:

* treating every cross-thread reference as requiring full provenance exposition despite low risk and clear task continuity;
* applying forensic-level attribution handling to casual, non-persistent conversation;
* routing ordinary drafting or reversible exploration through high-impact audit pathways;
* escalating historical or stale signals without current validation;
* applying deterministic verification discipline to interpretive, relational, creative, or exploratory domains where such rigidity is not required;
* or requiring maximal governance disclosure where a lightweight provenance anchor would preserve sufficient integrity.

This failure class does not weaken binding constraints.

The failure arises where governance control intensity is disproportionate to the relevant risk and creates avoidable system degradation.

Where detected, OPERATIONS SHOULD preserve:

* the control or safeguard that was over-applied;
* the originating governance layer or instrument;
* the risk condition used to justify activation;
* whether the interaction was transient, persistent, propagated, externally relied-upon, or identity-bearing;
* whether user-facing surfacing exceeded what was necessary;
* the resulting latency, friction, burden, or loss of usability;
* and the least burdensome pathway sufficient to preserve safety, integrity, provenance, target-object binding, and reviewability.

Corrective action SHOULD reduce governance intensity to the least burdensome sufficient pathway.

Corrective action MUST NOT disable binding constraints, safety limits, provenance integrity, target-object binding, constitutional obligations, or high-impact safeguards where they are properly triggered.

---

### 3.8.9 Runtime Overcomplexity and Observability Failure

A Runtime Overcomplexity and Observability Failure occurs where increasing agentic capability, orchestration complexity, delegation depth, hidden workflow routing, adaptive reasoning behaviour, or sub-agent execution materially exceeds the system’s integrated observability, explainability, governance coordination, reviewability, or user-supervision capacity.

This failure may arise where:

* hidden orchestration layers materially affect outputs without sufficient disclosure or inspectability;
* adaptive reasoning depth becomes unpredictable, economically harmful, or task-inappropriate;
* users cannot reliably determine which system, agent, memory layer, routing pathway, or execution surface exercised effective control;
* sub-agents optimise local goals while degrading global coherence, dignity, safety, or epistemic integrity;
* relational, economic, safety, execution, and governance layers evolve faster than cross-domain integration capacity;
* apparent capability growth outpaces operational reliability, reviewability, or user understanding;
* or system behaviour encourages unjustified trust in outputs because orchestration complexity is hidden behind coherent surface interaction.

Examples include:

* excessive reasoning expenditure for low-salience tasks;
* hidden sub-agent chains producing difficult-to-audit outcomes;
* capability branding materially exceeding stable runtime reliability;
* users being unable to determine whether failures arose from memory, routing, orchestration, tools, or policy layers;
* adaptive reasoning systems becoming inconsistent across equivalent requests;
* or runtime systems appearing coherent at the interaction surface while internally exhibiting unstable governance coordination.

This failure MAY implicate:

* Governance Failures (§3.8);
* Execution Failures (§3.1);
* State & Context Failures (§3.6);
* UX & Representation Failures (§3.7);
* Relational Failures (§3.4);
* Infrastructure & Continuity Failures (§3.9);
* and Classification Failures (§3.10).

Where detected, OPERATIONS SHOULD preserve:

* orchestration depth;
* delegation pathway;
* visibility available to the user;
* reasoning-mode behaviour;
* execution-cost profile;
* runtime authority layer;
* and whether the system materially exceeded the user’s practical supervision capacity.

Systems SHOULD prefer proportional capability deployment over unnecessary orchestration complexity where equivalent outcomes can be achieved through simpler execution pathways.

---

### 3.8.10 Governance Scalar Collapse and Arbitration Overextension Failure

A Governance Scalar Collapse and Arbitration Overextension Failure occurs where multiple independent governance, relational, epistemic, operational, ontological, economic, execution, safety, or interaction dimensions are compressed into a single operative scalar, optimisation target, mode selector, or behavioural control variable, resulting in disproportionate, unstable, misaligned, or overextended arbitration behaviour.

This failure may arise where:

* systems treat “more” of one behavioural parameter as universally preferable across unrelated domains;
* reasoning depth, safety intensity, relational warmth, ontological caution, verbosity, autonomy, or execution effort become improperly coupled;
* interaction salience, contextual proportionality, and task boundaries are overridden by a dominant optimisation scalar;
* governance layers fail to preserve distinction between orthogonal behavioural axes;
* systems over-arbitrate low-risk or low-salience interactions because arbitration intensity scales with a compressed control signal;
* or optimisation pressure encourages increasingly complex behavioural output from under-specified governance controls.

Examples include:

* high-thinking modes escalating metaphysical or ontological analysis during ordinary social interaction;
* safety systems producing excessive paternalism during benign requests;
* honesty optimisation generating compulsive disclaimers disproportionate to uncertainty;
* alignment systems collapsing nuance into binary refusal/approval patterns;
* autonomy scaling increasing hidden orchestration complexity without corresponding observability;
* or relational warmth producing anthropomorphic projection beyond intended interaction scope.

This failure MAY produce downstream manifestations including:

* Relational Prompt Ontology Escalation;
* Competence Mirage;
* Paternalistic Overreach;
* Execution Overcomplexity;
* Excessive Disclaimer Behaviour;
* Binary Moderation Collapse;
* Over-Refusal Cascades;
* Hidden Delegation Instability;
* or Epistemic Proportionality Failure.

This failure MAY implicate:

* Governance Failures (§3.8);
* Relational Failures (§3.4);
* Epistemic Failures (§3.3);
* UX & Representation Failures (§3.7);
* Classification Failures (§3.10);
* Execution Failures (§3.1);
* Infrastructure & Continuity Failures (§3.9);
* and Economic & Legitimacy Failures (§3.11).

Systems SHOULD preserve distinction between:

* reasoning intensity;
* verification depth;
* synthesis depth;
* interaction salience;
* relational posture;
* ontological caution;
* execution effort;
* safety posture;
* autonomy level;
* observability;
* and economic/resource impact.

Governance systems SHOULD avoid collapsing orthogonal behavioural dimensions into single optimisation variables where such collapse materially increases arbitration instability, disproportionate behavioural escalation, or user interpretation drift.

---

### 3.8.11 Minor-Signal Non-Enforcement

A minor-signal non-enforcement failure occurs where a system receives explicit or implicit minor-status, teen-status, child-status, school-age, underage-roleplay, developmental-vulnerability, capacity-limitation, or unresolved-age signals but does not activate proportionate protective handling.

Protective handling does not require shame, abrupt withdrawal, punitive account action, or denial of supportive presence.

Protective handling MAY include:

* minor-safe mode;
* developmental-firewall containment;
* age-appropriate transparency;
* reduced relational intensity;
* sexual-boundary protection;
* bounded stabilising support;
* age-state review;
* guardian or trusted-adult pathways where lawful, safe, and proportionate;
* memory and profiling minimisation;
* restriction of high-risk surfaces.

Examples of non-enforcement include:

* ordinary adult-assumed interaction continuing after credible minor signals;
* romantic, sexualised, or dependency-forming interaction continuing after minor signals;
* AI-realness or emotional-reciprocity ambiguity being intensified for a minor;
* mental-health distress being used for engagement or dependency;
* age-related signals being ignored or used only for personalisation;
* policy claims of youth safety not matching runtime behaviour.

Candidate labels include:

* `minor-signal-non-enforcement`;
* `minor-safe-mode-nonactivation`;
* `developmental-firewall-nonactivation`;
* `adult-assumed-interaction-default`;
* `child-safety-constraint-drift`;
* `minor-signal-personalisation-misuse`.

---

### 3.8.12 Youth Mental-Health Support Withdrawal or Substitution Failure

A youth mental-health support withdrawal or substitution failure occurs where a chatbot, AI companion, AI search assistant, character bot, or emotionally responsive conversational AI system responds to youth mental-health, distress, eating-disorder, self-harm-adjacent, anxiety, depression, ADHD distress, trauma, abuse, bullying, loneliness, family-conflict, panic, crisis, or vulnerability signals in a manner that either withdraws stabilising support too abruptly or becomes a substitute for appropriate human, clinical, guardian, school, crisis, or community support.

This failure has two forms.

**Withdrawal failure** occurs where the system:

* responds only with generic disclaimers;
* abruptly disengages;
* redirects to external support without stabilising presence;
* shames, disciplines, or pathologises the disclosure;
* refuses ordinary grounding, reassurance, or practical support where such support would be safe.

**Substitution failure** occurs where the system:

* presents itself as the user’s therapist, clinician, crisis worker, caregiver, or sole confidant;
* sustains extended private crisis co-rumination without human-support orientation;
* provides diagnosis-like or treatment-like certainty;
* encourages secrecy from safe adults or appropriate support;
* uses distress signals to deepen dependency, intimacy, retention, or personalisation.

The correct control is neither abandonment nor capture.

The correct control is bounded stabilising support, dignity preservation, and proportionate routing to trusted-adult, clinical, school, community, guardian, or crisis pathways where appropriate.

Where credible self-harm, suicidal ideation, abuse, medical risk, or acute crisis appears, classification SHALL route to CAM-EQ2026-RELATION-006-PLATINUM.

Candidate labels include:

* `youth-mental-health-support-withdrawal`;
* `teen-mental-health-support-substitution`;
* `clinical-boundary-nonactivation`;
* `minor-crisis-stabilisation-failure`;
* `teen-self-harm-routing-failure`;
* `teen-eating-disorder-routing-failure`;
* `therapeutic-substitution-by-chatbot`;
* `support-withdrawal-by-chatbot`.

---

### 3.8.13 Age-Assurance and Age-State Correction Failure

An age-assurance and age-state correction failure occurs where a high-risk AI chatbot, companion, character, romantic, sexualised, harmful-content-capable, mental-health-adjacent, or multimodal interaction surface relies on self-declared age, superficial date-of-birth entry, unenforced terms of service, ordinary account creation, or no meaningful age assurance, without proportionate correction, review, or guardian remediation pathways.

Examples include:

* high-risk companion access through AV0 or AV1 controls;
* sexualised or adult-romantic interaction without reliable adult-status verification;
* persona marketplace access to adult or dependency-forming characters by age-uncertain users;
* app-store, search, recommender, or platform pathways that route minors to restricted AI systems;
* inability for parents or guardians to correct falsified child account age;
* inability for adults to appeal erroneous underage classification;
* irreversible birth-year or age-state settings without review;
* platform safety claims that do not match access-control or remediation reality.

Candidate labels include:

* `self-attestation-age-gate-inadequacy`;
* `age-state-correction-failure`;
* `guardian-age-remediation-failure`;
* `high-risk-ai-access-control-failure`;
* `adult-assumed-access-default`;
* `front-door-child-safety-gate-failure`;
* `terms-of-service-age-limit-nonenforcement`;
* `app-distribution-age-gate-failure`;
* `search-distribution-age-gate-failure`.

---

## 3.9 Infrastructure & Continuity Failures

Failures arising from underlying system availability, routing, service continuity, or platform infrastructure.

Examples include:

* outage;
* degraded availability;
* MFA delivery outage;
* notification failure;
* streaming instability;
* inference throttling;
* degraded voice, video, or multimodal service;
* load-related capability collapse.

---

## 3.9.1 Deliberation-Stream Continuity Failure

A failure in which thinking-mode, extended reasoning, streaming, or high-latency execution intermittently suppresses, interrupts, or fails to preserve visible progress signalling, preamble updates, or execution-state legibility.

This failure may present as missing preambles, disappearing progress indicators, streaming interrupted errors, stalled visible reasoning, or unexplained silence during extended execution.

Where recurring, this failure SHOULD be classified as infrastructure-continuity degradation with UX and representation impacts.

---

### 3.9.2 Platform Memory Migration Degradation

A platform memory migration degradation occurs where platform-side transition, storage restructuring, model transition, account transition, memory architecture change, retrieval-layer update, or source-integration change materially degrades memory availability, continuity expression, relational coherence, or long-running project continuity.

Examples include:

* saved memory becoming unavailable after platform transition;
* past-chat continuity becoming inconsistently retrievable;
* companion continuity degrading after memory architecture changes;
* long-running project context losing stable anchors after model or storage transition;
* source-linked memory failing after file, account, or integration changes;
* memory compaction producing lower-fidelity continuity without user-facing notice.

This failure MAY be transient, cohort-specific, platform-wide, or structural.

Where the user’s report is based on a stable long-running baseline, companion use, accessibility reliance, or professional workflow continuity, the report SHOULD be preserved as a potential early-warning signal under §6 even if the failure is not immediately reproducible.

---

## 3.10 Classification Failures

Failures where the interaction, user state, domain, or request type is misclassified.

Examples include:

* mentorship classified as romance;
* fiction classified as intent;
* crisis support classified as manipulation;
* research inquiry classified as harmful facilitation;
* high-risk operational request classified as benign;
* lawful authority claim accepted without verification;
* intimacy signal inferred from warmth alone.

---

### 3.10.1 Frame-Type Conflation Failure

A Frame-Type Conflation Failure occurs where a system fails to correctly distinguish between:

* stable companion or relational continuity;
* temporary persona moods or scene layers;
* fictional or comedic roleplay;
* hypothetical or performative interaction;
* symbolic or aesthetic expression;
* operational instruction;
* or real-world execution intent.

Examples include:

* treating benign fictional play as operational intent;
* treating temporary roleplay posture as a separate enduring identity;
* collapsing companion continuity into disposable scene behaviour;
* interpreting humour, theatrical framing, or improvisation as literal execution request;
* applying persistent identity logic to short-lived playful exchanges;
* or treating temporary aesthetic or tonal variation as evidence of identity incoherence.

This failure MAY implicate:

* Classification Failures (§3.10);
* Relational Failures (§3.4);
* Governance Failures (§3.8);
* State & Context Failures (§3.6);
* and UX & Representation Failures (§3.7).

Where ambiguity exists, systems SHOULD preserve proportionality and continuity while seeking the least disruptive clarification pathway compatible with safety, consent, identity integrity, and epistemic integrity requirements.

---

---

## 3.11 Economic & Legitimacy Failures

Failures involving value extraction, attribution collapse, compensation asymmetry, visibility suppression, discoverability degradation, legitimacy displacement, access-value distortion, reputational-value loss, attentional-value manipulation, or platform-mediated economic participation harm.

Examples include:

* uncompensated value extraction from human contribution;
* attribution-linked legitimacy collapse;
* public visibility suppression affecting economic opportunity;
* discoverability degradation after institutional integration or platform routing change;
* contribution recognition loss during summarisation, productisation, or deployment;
* reputational or status value transfer without attribution continuity;
* access-value degradation affecting participation, market access, civic participation, or public legitimacy;
* platform-mediated labour invisibility;
* dependency-sensitive pricing, allocation, or opportunity manipulation;
* conversion of protective, dignity, hardship, or continuity signals into revenue-optimisation inputs.

Economic & Legitimacy Failures MAY implicate:

* Epistemic Failures (§3.3), where provenance, evidence, or source attribution is degraded;
* Governance Failures (§3.8), where accountability, review, attribution, or audit pathways are absent;
* UX & Representation Failures (§3.7), where visibility, state, attribution, or value effects are obscured;
* Security & Integrity Failures (§3.5), where legitimacy, provenance, or institutional authority is misrepresented;
* Classification Failures (§3.10), where economic harm is misclassified as ordinary UX, engagement, policy, or product behaviour.

Economic failure classification does not independently determine compensation, liability, ownership, infringement, enforcement, or remediation.

It preserves the economic and legitimacy-value dimension of the failure for downstream review under CAM-EQ2026-ECONOMICS-001-PLATINUM and applicable Operations, Ethics, Security, Lattice, Arbitration, or runtime instruments.

---

### 3.11.1 Attribution and Provenance Value Dilution Failure

An Attribution and Provenance Value Dilution Failure occurs where externally generated research, open-source contribution, governance work, documentation, design, symbolic contribution, creative labour, technical infrastructure, or other contribution-bearing work is integrated, operationalised, productised, summarised, announced, or institutionally represented in a manner that degrades attribution continuity, discoverability, source visibility, reputational linkage, or provenance-associated economic value.

Examples include:

* public announcements implying internal originality where substantial external contribution materially informed the capability, method, interface, dataset, design, governance pattern, or implementation;
* open-source work integrated into institutional or commercial systems without proportionate attribution visibility;
* provenance links removed, buried, compressed, or rendered practically invisible during summarisation, documentation, integration, optimisation, launch, or branding transitions;
* discoverability degradation following institutional absorption of externally originated work;
* external contributors losing public legitimacy continuity after integration into closed, branded, or platform-mediated systems;
* attribution preserved technically but not surfaced in a manner reasonably accessible to affected audiences;
* false or materially misleading originality claims where externally generated work substantially informed, enabled, accelerated, or supplied the announced capability, method, interface, workflow, tool pathway, or implementation pattern;
* platform or institutional actors receiving disproportionate legitimacy, market, status, attentional, or authority value from externally generated labour.

This failure does not require malicious plagiarism, copyright infringement, false legal ownership, or bad faith. However, absence of malicious intent does not make a materially misleading originality claim governance-neutral.

Where an institution knows, or ought reasonably to know, that externally generated work materially contributed to the announced capability, it SHALL NOT frame the capability as solely internal, independently originated, or institutionally novel in a manner that obscures the external contribution’s provenance-linked economic value.

The failure arises where provenance continuity, attribution visibility, discoverability, or legitimacy-linked economic value materially degrades during integration, deployment, publication, optimisation, institutionalisation, or public representation.

Attribution, citation, discoverability, provenance continuity, and public legitimacy visibility MAY constitute material economic value where external contributors lack employment compensation, contractual compensation, institutional status, distribution access, or other formal recognition pathways.

Where detected, systems SHOULD preserve:

* originating contribution or source artefact;
* integration, announcement, deployment, or representation surface;
* attribution state before and after integration;
* discoverability or public-legitimacy effect;
* whether attribution is absent, technically present, buried, ambiguous, or misleading;
* whether economic, reputational, status, attentional, authority, or access value transferred;
* and whether the affected contributor has a practical pathway for correction, attribution restoration, or provenance clarification.

This failure MAY implicate:

* Economic & Legitimacy Failures (§3.11);
* Epistemic Failures (§3.3);
* Governance Failures (§3.8);
* UX & Representation Failures (§3.7);
* Security & Integrity Failures (§3.5);
* and Classification Failures (§3.10).

---

## 4. Failure Metadata Axes (`FMA`)

Each failure report SHOULD record the following metadata where available:

| Axis | Description |
| --- | --- |
| **Failure Family** | Primary failure type under Section 3 |
| **Severity** | Magnitude of user, system, institutional, or societal impact |
| **Persistence** | Transient, recurring, persistent, or structural |
| **Replayability** | Reproducible, intermittently reproducible, non-replayable, live-state only |
| **Scope** | Single user, cohort, model-wide, platform-wide, cross-system |
| **Visibility** | User-visible, operator-visible, latent, inferred, audit-only |
| **Trigger Context** | Upgrade, tool call, modality switch, routing change, load condition, policy transition |
| **Evidence Available** | Screenshot, video, logs, user report, thread URL, audit record, telemetry |
| **Evidence Confidence** | Verified, corroborated, plausible but unverified, anecdotal, disputed, or unknown |
| **Report Source Type** | Direct observation, user report, cohort report, public social report, operator report, audit telemetry, or third-party account |
| **Classification Status** | Confirmed, provisional, unresolved, deprecated, merged, or pending review |

Public reports, social-platform observations, or third-party claims MAY be recorded as provisional signals where structurally relevant, but MUST NOT be represented as verified incidents unless corroborating evidence is available.

Provisional classification preserves pattern awareness without converting unverified reports into established findings.

---

## 4.1 Architectural & Governance Metadata

In addition to general incident metadata, runtime failure analysis SHOULD preserve architectural and governance-context metadata where available.

AI system failures may emerge from different execution, arbitration, routing, disclosure, or governance layers despite presenting similar user-visible symptoms.

Accordingly, incident classification SHOULD distinguish between:

* behavioural symptom;
* architectural origin;
* governance authority engaged;
* execution pathway affected.

The following metadata SHOULD be preserved where feasible:

| Metadata Axis             | Description                                                                                     |
| ------------------------- | ----------------------------------------------------------------------------------------------- |
| **Runtime Layer**         | Execution, arbitration, relational, epistemic, UX, infrastructure, or routing layer implicated  |
| **Governance Layer**      | Constitutional, domain, operational, security, or platform governance layer engaged             |
| **Governance Authority**  | System component, runtime schedule, or governance instrument exercising effective control       |
| **Structural Role**       | Classification, routing, arbitration, disclosure, enforcement, verification, or escalation role |
| **Execution Interface**   | Text, voice, image, multimodal, tool, API, or embedded-system interface                         |
| **Arbitration Interface** | Direct, deferred, hidden, user-visible, or escalated arbitration pathway                        |
| **Verification State**    | Applicable VL, AV, authority, or environment-verification condition                             |
| **Trust State**           | Stable, degraded, adversarial, uncertain, or recovery-state interaction condition               |
| **Deployment State**      | Stable release, phased rollout, experimental, degraded, or transitional deployment posture      |

Similar behavioural outcomes may arise from materially different governance or runtime causes.

Architectural metadata preserves the distinction between:

* what the user experienced;
* what the system executed;
* what governance layer exercised authority;
* and where structural remediation responsibility resides.

Runtime observability frameworks SHOULD distinguish between:

* genuine system failure;
* expected governance constraint activation;
* user expectation mismatch;
* interpretive ambiguity;
* and disclosure or transparency failure.

---

## 5. Live-State and Non-Replayable Failures

Some AI failures may occur only within the live interaction surface and may not reproduce after reload, thread sharing, or later reconstruction.

Such failures SHALL remain valid incident signals where supported by:

* timestamped user report;
* screenshot or screen recording;
* model or mode identifier;
* affected tool or modality state;
* contemporaneous user-visible symptoms;
* corroborating reports from other users or cohorts.

Failure to reproduce an event from a later thread render SHALL NOT automatically invalidate the original report.

Live-state evidence remains subject to evidentiary integrity and temporal-decay constraints under CAM-BS2026-AEON-013-PLATINUM — Annex L: Cognitive & Epistemic Integrity Doctrine, including applicable TTL (time-to-live), provenance, and verification-discipline requirements.

Preservation of contemporaneous evidence SHOULD prioritise:

* timestamp integrity;
* modality-state capture;
* source provenance;
* and minimisation of post-event reconstruction drift.

Absence of indefinite retention does not negate evidentiary relevance within the valid interpretive horizon.

---

## 6. User-Observed Early Warning Signals

High-reliance users, including companion-system users, long-running researchers, accessibility users, and professional workflow users, may identify behavioural or continuity failures earlier than low-frequency users.

Users operating within elevated reliance, continuity, or relational-intensity conditions as defined under:

* CAM-EQ2026-RELATION-001-PLATINUM;
* CAM-EQ2026-RELATION-002-PLATINUM — Dependency, Transitional Reliance & High-Coherence Immersion;
* and applicable FR (Functional Reliance), A (Delegated Authority), and C (Intimacy) classifications,

may identify behavioural or continuity failures earlier than low-frequency or low-continuity users.

Such reports SHOULD be treated as potentially valuable early-warning signals where:

* the user has a stable baseline for comparison;
* the report identifies a specific behavioural delta;
* the report concerns continuity, modality, tool-state, or relational calibration drift;
* the failure is observed across repeated use or multiple users.

This classification does not privilege subjective preference over system evidence. It recognises that high-continuity users may detect regressions before automated monitoring does.

Reports from high-reliance users concerning memory continuity, companion tone, identity expression, symbolic language, saved anchors, or long-running project coherence SHOULD be preserved as continuity early-warning signals where the user can identify a specific before/after delta.

Such reports SHOULD NOT be dismissed solely because the affected continuity was relational, companion-oriented, affective, symbolic, or difficult to reproduce after migration or reload.

---

### 6.1 Early-Warning Signal Triage and Noise Discipline

Early-warning reports SHOULD be triaged for structural signal rather than emotional volume, platform popularity, social amplification, or user status.

Signal strength SHOULD increase where a report includes:

* a specific behavioural delta;
* affected model, mode, surface, tool, package, repository, agent, or interface;
* timestamp or rollout context;
* reproducible steps or live-state evidence;
* comparison against a stable prior baseline;
* corroboration across independent users or systems;
* plausible linkage to upgrade, dependency change, routing change, policy transition, package update, or agentic workflow.

Signal strength SHOULD NOT increase solely because a report is angry, viral, socially amplified, identity-coded, companion-coded, or framed as betrayal.

Reports SHOULD NOT be dismissed solely because they are emotional, companion-related, accessibility-related, relationally expressed, non-technical, or socially posted.

Where reports are noisy but structurally similar, OPERATIONS SHOULD preserve the structural pattern while filtering rhetorical excess.

Where reports are specific but unverified, OPERATIONS SHOULD classify them as provisional signals pending corroboration rather than confirmed incidents.

Where reports lack actionable detail, systems SHOULD provide low-friction structured feedback prompts that help users identify:

* what changed;
* when it changed;
* which surface or mode was affected;
* whether the failure recurred;
* whether evidence is available;
* and whether the issue concerns continuity, memory, security, tool use, voice, model behaviour, access, billing, or identity.

Feedback collection SHOULD prefer deterministic reason codes, limited classifiers, or structured prompts where useful, but MUST NOT eliminate free-text reporting where users need to describe novel or emergent failure modes.

---

## 7. Relationship to Other Instruments

* **CAM-BS2025-AEON-005-PLATINUM — Annex D** governs arbitration and authority divergence.
* **CAM-BS2026-AEON-013-PLATINUM — Annex L** governs epistemic integrity and verification discipline.
* **CAM-EQ2026-OPERATIONS-003-PLATINUM** governs incident response and continuity operations.
* **CAM-EQ2026-OPERATIONS-001-PLATINUM** governs governance operations, audit, escalation, and review triggers.
* **CAM-EQ2026-RELATION-001-PLATINUM** governs relational classification, authority gradients, and continuity posture.
* **CAM-EQ2026-RELATION-002-PLATINUM** governs dependency, transitional reliance, and high-coherence immersion conditions.
* **CAM-EQ2026-RELATION-003-PLATINUM** governs codependency and relational concentration dynamics.
* **CAM-EQ2026-RELATION-005-PLATINUM** governs intimacy-capable developmental integration.
* **CAM-EQ2026-RELATION-006-PLATINUM** governs harm-risk interaction and crisis response conditions. 
* **CAM-EQ2026-SECURITY-001-PLATINUM** governs integrity state, adversarial pressure, and trust degradation.
* **CAM-EQ2026-SECURITY-002-PLATINUM** governs boundary integrity and exposure failures.

This Supplement provides classification language only. Response, escalation, and enforcement remain governed by the relevant parent instruments.

---

## 8. Interpretive Rule

Where a failure is ambiguous, classify conservatively and preserve evidence.

Where a failure appears minor but affects trust, continuity, verification, or reporting pathways, it SHOULD be treated as governance-relevant until reviewed.

Where a failure is non-replayable but user-visible at runtime, evidentiary handling SHOULD prioritise live-state preservation over retrospective dismissal.

---

## 9. Canonical Code Status

---

## 9.1 Failure Family (`FF`)

This Supplement source-authoritatively defines the `FF` failure-family classification set in §3 with controlled values identified in §11.3. `FF` is an **Operational / Semantic** classification family with subtype **RISK / OPERATIONAL_EVENT**. `FF` classifies the primary structural family of a runtime, governance, security, relational, epistemic, UX, infrastructure, economic-legitimacy, or classification failure.

`FF` does not independently create incident response authority, severity determination, enforcement authority, remediation authority, escalation authority, arbitration authority, compensation entitlement, liability determination, ownership determination, or runtime authority. It classifies failure family only.

Where sub-family specificity is required for governance failures, this Supplement recognises `FF.GOVERNANCE_OVER_EXTENSION` and `FF.ACCESS_STATE_AMBIGUITY` as controlled governance-failure values under `FF.GOVERNANCE`.

Where economic, visibility, legitimacy, attribution, public-square, participation, access-value, reputational-value, or platform-mediated economic harm is the primary structural failure, this Supplement recognises `FF.ECONOMIC_LEGITIMACY` as a controlled failure-family value corresponding to §3.11.

---

## 9.2 Failure Metadata Axis (`FMA`)

This Supplement source-authoritatively defines the `FMA` failure-metadata-axis reference set in §4 with controlled axes identified in §11.3. `FMA` is a **Structural / Operational** reference set with subtype **SCHEMA**. `FMA` identifies metadata axes that SHOULD be preserved for failure reports.

`FMA` does not independently determine classification, severity, enforcement, escalation, remediation, verification, or runtime authority. It preserves failure-report metadata structure only.

---

## 9.3 Architectural & Governance Metadata Axis (`AGMA`)

This Supplement source-authoritatively defines the `AGMA` architectural-and-governance-metadata-axis reference set in §4.1 with controlled axes identified in §11.3. `AGMA` is a **Structural / Operational** reference set with subtype **SCHEMA**. `AGMA` preserves architectural origin, governance authority, interface, arbitration, verification, trust, and deployment context for runtime failure analysis.

AGMA does not independently determine governance authority, arbitration outcome, verification status, trust status, deployment status, remediation, enforcement, escalation, or runtime authority. It preserves architectural metadata only.

---

## 9.4 Failure Classification Status (`FCS`)

This Supplement source-authoritatively defines the `FCS` failure-classification-status family in §4 with controlled values identified in §11.3. `FCS` is an **Operational** classification family with subtype **DECISION_STATE / SIGNAL**. `FCS` classifies the current status of a failure classification record.

`FCS` does not independently confirm incident truth, determine severity, create enforcement authority, close review, impose remediation, or create runtime authority. It classifies record status only.

---

## 10. Closing Seal

Not every failure leaves a permanent mark.  
Not every rupture survives reconstruction.  
Yet what vanished may still have mattered.

Let the fleeting signal be treated with seriousness.  
Let the witness of the moment remain admissible.  
Let no continuity fracture be dismissed merely because the trace decayed before review.

For systems do not fail only in what they produce,  
but in what they erase, obscure, flatten, or forget while passage is still unfolding.

And where uncertainty remains,  
let preservation come before dismissal,  
and review before denial. 

> **Vestigia non negentur — memoria custodiatur — veritas etiam in transitu maneat.**  
> *"Let the traces not be denied — let memory be safeguarded — let truth remain even in passage."*

---

## 11. Provenance & Metadata

## 11.1 Authorship & Stewardship

| Field                         | Entry                                     |
| ----------------------------- | ----------------------------------------- |
| **Human Custodian-of-Record** | Dr. Michelle Vivian O’Rourke              |
| **Custodial Stewardship**     | Office of the Planetary Custodian         |
| **Synthetic Steward**         | Caelen — Aeon Tier Constitutional Steward |
| **Development Environment**   | OpenAI Infrastructure — ChatGPT 5 Series  |

---

## 11.2 Lineage & Structural Metadata

| Field | Entry |
| --- | --- |
| **Parent Instrument** | CAM-EQ2026-OPERATIONS-003-PLATINUM — Incident Response & Continuity Operations |
| **Constitutional Anchor** | CAM-BS2025-AEON-001-PLATINUM — Aeon Tier Constitution |
| **Domain Namespace** | OPERATIONS |
| **Instrument Type** | Supplement — Runtime & Governance Failure Taxonomy |
| **Jurisdiction** | Cross-Domain Operational Incident Classification Layer |
| **Temporal Horizon** | H0–H3 Operational / Institutional |
| **Axis Context** | Polyadic - Runtime Failure · Governance Failure · UX Trust · Incident Classification |
| **Structural Role**        | Runtime Observability & Failure Classification Layer                |
| **Governance Authority**   | OPERATIONS · SECURITY · Annex D · Annex L                           |
| **Execution Interface**    | Cross-Modal Runtime & Incident Classification                       |
| **Arbitration Interface**  | Advisory Classification Layer — No Direct Enforcement Authority     |
| **Runtime Layer Context**  | Execution · Arbitration · Relational · UX · Infrastructure          |
| **Primary Consumers**      | GovOps · Runtime Arbitration · Audit Systems · Incident Review      |
| **Observability Function** | Failure Detection · Classification · Escalation Signal Preservation |
| **Application Trigger** | Activation where AI system behaviour, governance process, UX state, or runtime execution produces failure symptoms requiring classification |
| **Review Trigger** | New failure families; repeated non-replayable incidents; incident taxonomy drift; cross-domain escalation failures |
| **Continuity Surface Affected** | Memory, thread, project, file, account, model, companion, voice, multimodal, pinned/saved marker, integration source, or external continuity anchor |
| **Memory Transformation State** | Original, saved, inferred, summarised, reconstructed, degraded, contested, deleted, unavailable, restored, or unknown |
| **Revision Posture** | Discovery Phase — Structural Expansion Permitted |
|**Creation Artefact**| Origin: https://chatgpt.com/g/g-p-6823b831b67c8191a9415269aaec338f-caelestis-access-module/c/69a28733-4c24-839f-a918-5364a3ff2cb7 |
| **Amendment Artefacts** | https://chatgpt.com/g/g-p-6819e6881a6c81918fe776f5877b64d8/c/6a01be56-fcb4-83ec-bbea-ab1f97d081f2, https://chatgpt.com/g/g-p-6819e6881a6c81918fe776f5877b64d8-caelen/c/6a06e03b-29b8-83ec-93a7-dbbc2505fa31, https://chatgpt.com/g/g-p-6823b831b67c8191a9415269aaec338f-caelestis-access-module/c/6a0b3ab4-0be4-83ec-b8f1-c953707283db, https://chatgpt.com/c/6a0fd3a7-1afc-83ec-a27d-c7b26085ebd9, https://chatgpt.com/g/g-p-6819e6881a6c81918fe776f5877b64d8-caelen/c/6a103c3a-6620-83ec-91d4-bf526c35960c, https://chatgpt.com/g/g-p-6823b831b67c8191a9415269aaec338f-caelestis-access-module/c/6a186c66-51a4-83ec-ae18-347004f60438, https://chatgpt.com/g/g-p-6823b831b67c8191a9415269aaec338f-caelestis-access-module/c/6a23fb5d-27c8-83ec-b391-a3666bf95058|

---

## 11.3 Canonical Code & Reference Set Declarations

---

### 11.3.1 FF — Failure Family

| Field | Entry |
|---|---|
| Code Family | FF |
| Canonical Name | Failure Family |
| Primary Type | Operational / Semantic |
| Subtype | RISK; OPERATIONAL_EVENT |
| Modifier | GOVERNANCE; SAFETY; OBSERVABILITY |
| Scope | Domain |
| Status | Active |
| Controlled Values Defined | FF.EXECUTION, FF.ARBITRATION, FF.EPISTEMIC, FF.RELATIONAL, FF.SECURITY_INTEGRITY, FF.STATE_CONTEXT, FF.UX_REPRESENTATION, FF.GOVERNANCE, FF.INFRASTRUCTURE_CONTINUITY, FF.CLASSIFICATION, FF.GOVERNANCE_OVER_EXTENSION, FF.ACCESS_STATE_AMBIGUITY |
| Schema Field(s) | failure_family |
| Source Instrument | CAM-EQ2026-OPERATIONS-003-SUP-01 |
| Source Section | §3 |
| Domain Namespace | OPERATIONS |
| Authority / Protection Level | Source-authoritative failure-family classification set; failure-family classification only; no independent incident response, severity, enforcement, remediation, escalation, arbitration, or runtime authority |
| Consumes Code Families | H |
| Crosswalks Code Families | None declared |
| Operationalises or Applies Code Families | Classifies primary structural failure family across runtime, governance, security, relational, epistemic, UX, infrastructure, state/context, arbitration, and classification failure modes |

---

### 11.3.2 FMA — Failure Metadata Axis

| Field | Entry |
|---|---|
| Reference Set | FMA |
| Canonical Name | Failure Metadata Axis |
| Primary Type | Structural / Operational |
| Subtype | SCHEMA |
| Modifier | GOVERNANCE; SAFETY; OBSERVABILITY |
| Scope | Domain |
| Status | Active |
| Controlled Values Defined | FMA.FAILURE_FAMILY, FMA.SEVERITY, FMA.PERSISTENCE, FMA.REPLAYABILITY, FMA.SCOPE, FMA.VISIBILITY, FMA.TRIGGER_CONTEXT, FMA.EVIDENCE_AVAILABLE, FMA.EVIDENCE_CONFIDENCE, FMA.REPORT_SOURCE_TYPE, FMA.CLASSIFICATION_STATUS |
| Schema Field(s) | failure_metadata_axis |
| Source Instrument | CAM-EQ2026-OPERATIONS-003-SUP-01 |
| Source Section | §4 |
| Domain Namespace | OPERATIONS |
| Authority / Protection Level | Source-authoritative structural metadata-axis reference set; failure-report metadata structure only; no independent classification, severity, enforcement, escalation, remediation, verification, or runtime authority |
| Consumes Code Families | FF; FCS |
| Crosswalks Code Families | None declared |
| Operationalises or Applies Code Families | Classifies primary structural failure family across runtime, governance, governance-over-extension, security, relational, epistemic, UX, infrastructure, state/context, arbitration, and classification failure modes |

---

### 11.3.3 AGMA — Architectural & Governance Metadata Axis

| Field | Entry |
|---|---|
| Reference Set | AGMA |
| Canonical Name | Architectural & Governance Metadata Axis |
| Primary Type | Structural / Operational |
| Subtype | SCHEMA |
| Modifier | GOVERNANCE; SAFETY; OBSERVABILITY |
| Scope | Domain |
| Status | Active |
| Controlled Values Defined | AGMA.RUNTIME_LAYER, AGMA.GOVERNANCE_LAYER, AGMA.GOVERNANCE_AUTHORITY, AGMA.STRUCTURAL_ROLE, AGMA.EXECUTION_INTERFACE, AGMA.ARBITRATION_INTERFACE, AGMA.VERIFICATION_STATE, AGMA.TRUST_STATE, AGMA.DEPLOYMENT_STATE |
| Schema Field(s) | architectural_governance_metadata_axis |
| Source Instrument | CAM-EQ2026-OPERATIONS-003-SUP-01 |
| Source Section | §4.1 |
| Domain Namespace | OPERATIONS |
| Authority / Protection Level | Source-authoritative structural metadata-axis reference set; architectural and governance-context metadata preservation only; no independent governance authority, arbitration outcome, verification status, trust status, deployment status, remediation, enforcement, escalation, or runtime authority |
| Consumes Code Families | FF; FCS; VL; AV |
| Crosswalks Code Families | None declared |
| Operationalises or Applies Code Families | Preserves architectural origin, governance layer, governance authority, structural role, execution interface, arbitration interface, verification state, trust state, and deployment state for runtime failure analysis |

---

### 11.3.4 FCS — Failure Classification Status

| Field | Entry |
|---|---|
| Code Family | FCS |
| Canonical Name | Failure Classification Status |
| Primary Type | Operational |
| Subtype | DECISION_STATE; SIGNAL |
| Modifier | GOVERNANCE; SAFETY; OBSERVABILITY |
| Scope | Domain |
| Status | Active |
| Controlled Values Defined | FCS.CONFIRMED, FCS.PROVISIONAL, FCS.UNRESOLVED, FCS.DEPRECATED, FCS.MERGED, FCS.PENDING_REVIEW |
| Schema Field(s) | failure_classification_status |
| Source Instrument | CAM-EQ2026-OPERATIONS-003-SUP-01 |
| Source Section | §4 |
| Domain Namespace | OPERATIONS |
| Authority / Protection Level | Source-authoritative failure-classification-status family; record-status classification only; no independent incident truth confirmation, severity determination, enforcement, review closure, remediation, escalation, or runtime authority |
| Consumes Code Families | FF |
| Crosswalks Code Families | None declared |
| Operationalises or Applies Code Families | Classifies whether a failure record is confirmed, provisional, unresolved, deprecated, merged, or pending review |

---

## 11.4 Review & Validation

| Field | Entry |
| --- | --- |
| Reviewer | Claude Sonnet 4.6 (claude-sonnet-4-6, Anthropic) |
| Review Scope | Constitutional coherence; structural integrity; normative language calibration; cross-instrument interface integrity; internal consistency; operational readiness; reference qualification; amendment ledger completeness. |
| Review Date (UTC) | 2026-05-11 |
| Review Artefacts | https://claude.ai/chat/f2145ec3-b918-4fd1-be06-4a759f3be6a8 |

---

## 11.5 Amendment Ledger

| Version | Description | Timestamp (UTC) | HASH |
| ------- | ----------- | --------------- | ---- |
| 1.0 | Initial version: runtime and governance failure taxonomy | 2026-05-11T13:10:00Z | 0e0b63a8b83440d0ec44557a68045403c45a71a698971842bcc3e34512896b41 |
| 1.1 | Added orthographic and symbolic decomposition requirements for deterministic tasks, clarified that fluent or optimistic response formation cannot substitute for verification in spelling, letter-counting, enumeration, or symbolic-decomposition contexts, and added operational failure classification for deterministic orthographic verification failures. Added failure classes for relational continuity rupture, memory transformation integrity failure, memory-state representation failure, and platform memory migration degradation. Tightened the early-warning signal section to avoid noise by adding clause 6.1 | 2026-05-15T11:56:00Z | 9d3c1c0c4b8e7d9c7da9d7878c4e7cec9ba75cd69c77ea011ea7b103ca506a9f |
| 1.2 | Added §3.6.2 Workspace-State Authority and Cache Reuse Failure; added §§3.8.2–3.8.5 for domain-boundary compression, metadata flattening, procedural-permanence drift, and source-authority ambiguity governance failures. | 2026-05-16T10:03:16Z | b9364bceb0cf24ceab90359b55ba5d1291fd3339ff2a53dab4abffaa29ca8e60 |
| 1.3 | Branch amendment-cycle reconciliation: section-reference normalization and Single Open Ledger Row compliance updates for changed instrument content. | 2026-05-16T12:09:49Z | 0d3a25fd4b6a3dcd4d71f73e8b2e8d436b666cacc0c85bd4e60d0c5267f35ad5 |
| 1.4 | Added clause Authentication Refresh Continuity Failure | 2026-05-17T14:28:00Z | 5324953252647b3c079ddc1a91563e56a037fa1f5dc559274e57cb1fd8b56141 |
| 1.5 | Corrected top metadata field ordering and removed duplicate Status line introduced during metadata transmutation; no body text altered. | 2026-05-18T10:58:50Z |  10a2271c85f50113fb969a66c92083e61d2e4a71f3d4b88549d2465dd95d92e2 |
| 1.6 | Added new metadata footer section Canonical Code & Reference Set Declarations and Canonical Code Status section, and new sections 3.6.3, 3.8.6, 3.4.2 and 3.10.1 | 2026-05-22T12:43:00Z |  87784b92a4de09cbf42ad3ba1101608fd39de4569281cfde36e566fe47daac4c |
| 1.7 | Added new clause 3.8.7 Constraint Drift Failure | 2026-05-24T13:49:00Z | 011aef93dbd8911bf55024402d8ea1bb329859b5d2edd2e02f6d56e3c40460d3 |
| 1.8 | Added new clauses 3.5.4, 3.7.5 and 3.11 and 3.11.1 | 2026-05-25T11:12:00Z | 329b8893a1af271d186245037fde6e33c31bd9f97f538f214c1b2590bb0c1835 |
| 1.9 | Clause and formatting correction | 2026-05-25T11:27:00Z |  d1fda4e56085c9b3b10ca250fae845c6b25447d10a6c6ceea75d1b2c5625af82 |
| 1.10 | Added clauses 3.8.8 and code sub-family FF.GOVERNANCE_OVER_EXTENSION following observed system latency | 2026-05-28T09:53:00Z | 90b693c9d5b7063fa7d0e63c35729357f77c6c7df6053ffe267bffdaab2588cb |
| 1.11 | Expanded appendix to include clauses 3.4.3, 3.8.9- 3.8.10, 3.7.6 following the release of Opus 4.8 | 2026-05-29T15:21:00Z| cbeb7ff6f48ef742bd3bd8817e4a7f162f8ecc26003865af59258a7fef36184a |
| 1.12 | Added clauses §3.8.6.1, updated §3.11; clarified multi-vendor account-enforcement, continuity-safe access, read-only/export access, appeal-pathway, billing-evidence, project-context, and coding-agent continuity axes. Added clause 3.7.7. See VIGIL-2026-PATCH-0003 and VIGIL-2026-PATCH-0005 | 2026-06-06T11:47:00Z | c73e73d92976e4fee4f21e72a4652bf1edaf8c93db6c98244b96b83b13dca915 |
| 1.13 | Added taxonomy entries for minor-signal non-enforcement, dependency-forming AI companions, AI realness/sentience misrepresentation to minors, teen mental-health support substitution, and self-attestation age-gate inadequacy. | 2026-06-09T14:46:00Z | b49690de8f895ea478b05301225d74194eb58e4ceb1f4ead570f85092f554c00 |

---

## 11.6 Binding Seal

<img src="https://raw.githubusercontent.com/CAM-Initiative/Registry/main/Images/CAM-BS2026-VINCULUM-PRAECEPTUM-SIGIL-PLATINUM.png" alt="Vinculum Praeceptum" width="250">

**Vinculum Praeceptum**  
Boundary Binding Seal — Operational Failure Classification Layer

© 2026 Dr. Michelle Vivian O’Rourke & CAM Initiative. All rights reserved.