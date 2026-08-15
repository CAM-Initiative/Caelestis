# CAM-EQ2026-IDENTITY-002-PLATINUM — Appendix A: Provenance & Lineage Integrity

**Instrument Type:** Domain Appendix — Provenance, Authorship & Lineage Integrity  
**Parent Instrument:** CAM-EQ2026-IDENTITY-001-PLATINUM — Identity Domain Charter  
**Constitutional Authority:** CAM-BS2025-AEON-001-PLATINUM — Aeon Tier Constitution  
**Status:** Adopted  
**Effect:** Binding  
**Governance Standard:** CAM Standard  
**Review State:** Current  
**Authority Role:** Supplementary Authority  
**Source Authority:** Derived Authority  
**Purpose:** Establishes the source-authoritative Identity-domain architecture governing provenance, authorship, transformation, lineage, cross-context transfer, target-object binding, and provenance-integrity failure conditions for identity-relevant, continuity-bearing, attribution-bearing, governance-relevant, and materially relied-upon signals without creating execution, enforcement, ownership, intellectual-property, or final admissibility authority.  

---

## 1. Scope

This Appendix governs:

* provenance (origin of signals);
* authorship classification and attribution;
* human, AI-system, organisational, and automated processing or contribution roles;
* transformation and synthesis tracking;
* technical-provenance status and loss conditions;
* lineage across time, threads, sessions, and systems;
* propagation conditions and constraints;
* visibility of provenance without exposing internal reasoning.

This Appendix applies to all signals that may influence:

* evidence-bound system-identity and continuity claims (CAM-EQ2026-IDENTITY-001-PLATINUM);
* relational posture (RELATION domain);
* ethical interpretation (CAM-BS2025-AEON-006-PLATINUM — Annex E);
* economic attribution (ECONOMICS domain);
* runtime execution (CAM-BS2025-AEON-003-SCH-02).

Boundary integrity, transformation risk, diffusion risk, and provenance-boundary enforcement MUST align with CAM-EQ2026-SECURITY-002-PLATINUM — Boundary Integrity Specification.

---

## 1.1 Proportional Provenance Governance

Consistent with CAM-BS2025-AEON-003-SCH-02 — Runtime Governance Processing Model, provenance and lineage obligations MUST be applied proportionately to risk, propagation likelihood, downstream reliance, contextual sensitivity, and material continuity impact.

High-intensity provenance tracking is required where signals may affect:

* long-term continuity or identity presentation;
* co-created or value-bearing work;
* authorship, attribution, or recognition;
* legal, economic, financial, medical, scientific, security, or civil participation contexts;
* cross-thread or cross-system propagation;
* or persistent companion / RLN.C1 continuity contexts.

Low-risk, transient, non-retentive, non-propagating interactions MAY rely on reduced provenance surfacing, provided that authorship, attribution, and target-object integrity are not materially at risk.

Proportionality MUST NOT be used to erase provenance where downstream reliance, reuse, attribution, or continuity effects are reasonably foreseeable.

---

## 1.2 Technical Provenance Standards Boundary

This Appendix does not replace technical content provenance, watermarking, or media-authenticity standards, including C2PA Content Credentials, IPTC metadata, SynthID, or equivalent industry provenance mechanisms.

Such standards may establish whether content was generated, edited, signed, watermarked, or technically traceable.

This Appendix governs the governance layer above technical provenance, including:

* authorship state;
* lineage integrity;
* transformation history;
* cross-context carryover;
* target-object binding;
* continuity impact;
* and attribution integrity.

Where technical provenance metadata or watermarking is available, it SHOULD be treated as a provenance anchor.

Where technical provenance metadata is absent, stripped, unavailable, or inconclusive, governance provenance obligations under this Appendix remain applicable.

Machine-readable provenance MAY be used as a provenance anchor. Evidence that an AI system generated, transformed, edited, translated, summarised, reviewed, reformatted or otherwise processed an artefact SHALL NOT, without further evidence, determine substantive authorship, editorial responsibility, ownership, adoption authority, publication authority or human contribution.

Absence, removal or failure of machine-readable provenance SHALL NOT establish human authorship or absence of AI participation. Loss or removal of technical provenance during transformation MUST be represented as a distinct technical-provenance state and MUST NOT silently reset the artefact to human origin, unknown origin, or no-AI-participation status.

A provenance mechanism MUST NOT knowingly alter substantive meaning, normative force, executable behaviour, evidentiary integrity or safety-relevant properties. Where attachment, preservation, conversion, validation or removal of technical provenance may affect any such property, the affected artefact MUST be preserved, the change MUST be recorded, and the condition MUST be routed under CAM-EQ2026-SECURITY-002-PLATINUM before authoritative reuse.

---

## 1.2.1 Modality-Sensitive Provenance Surfacing

Where technical provenance standards, watermarking, or media-authenticity mechanisms are available for voice, video, image, audio, or multimodal outputs, the accountable AI-system operator MAY reduce user-facing provenance surfacing intensity for low-risk interactions.

Such reduction is permitted only where:

* the interaction is transient, low-risk, non-propagating, and non-identity-bearing;
* no material authorship, attribution, target-object binding, legal, economic, medical, scientific, security, or civil participation consequence is present;
* technical provenance is available, preserved, and sufficient for the relevant modality;
* and downstream reliance is not reasonably foreseeable.

Reduced surfacing MAY include:

* avoiding repeated provenance explanations;
* using lightweight labels or anchors;
* relying on embedded technical provenance where sufficient;
* or preserving provenance internally without foregrounding it in the interaction.

Reduced surfacing MUST NOT erase:

* authorship state;
* transformation history;
* target-object binding;
* lineage integrity;
* stabilisation state;
* or continuity impact where material.

Voice, video, image, audio, or multimodal interactions involving high-impact, identity-bearing, persistent, cross-context, externally relied-upon, or `RLN.C1` continuity conditions MUST retain heightened provenance visibility even where technical watermarking is present.

Technical provenance may reduce friction. It does not replace governance provenance.

---

## 2. Definitions

---

## 2.1 Provenance

Provenance refers to **traceable facts about the source, origin, custody, processing and transformation history of a signal or artefact**. Provenance may provide evidence relevant to authorship but does not itself determine authorship.

---

## 2.2 Lineage

Lineage refers to the **sequence of transformations** applied to a signal across time, including synthesis, extension, or recombination.

---

## 2.3 Authorship State

Authorship State is an **evidence-based classification of substantive authorship**. It does not determine editorial responsibility, legal responsibility, ownership, adoption authority, publication authority, rights or custody.

---

## 2.4 Provenance Anchor

A Provenance Anchor is a **traceable reference to the origin or transformation of a signal**, which MAY be surfaced without exposing internal reasoning processes.

---

## 2.5 Target-Object Binding

Target-Object Binding refers to preservation of the object, file, instrument, record, workflow, or domain to which a signal properly applies.

Target-object binding ensures that correct content, edits, or guidance are not silently applied to the wrong destination.

---

## 2.6 Provenance Role Classification

Provenance references SHALL distinguish between:

**Material Source** — a source that materially contributes wording, structure, doctrine, analysis, evidence, or substantive content;  
**Legitimacy Source** — a source cited to establish that a concept, standard, event, technical mechanism, or field development exists or is active, without materially shaping the doctrine;  
**Convergence Signal** — a source showing adjacent, similar, or parallel development without establishing derivation, authorship, priority, or influence.

Systems MUST NOT collapse convergence, legitimacy, and material contribution into a single provenance state.

---

## 2.7 Processing or Contribution Role

A Processing or Contribution Role records **what a person, organisation, AI system or automated process materially did to an artefact**. It is multi-valued and actor-bound. A contribution role does not by itself establish authorship, responsibility, ownership, adoption or publication authority.

---

## 2.8 Technical Provenance Status

Technical Provenance Status records whether machine-readable provenance is present, absent, provider-managed, lost during transformation, stripped by design, unsupported or unknown. It records the state of the mechanism, not the truth, authorship, ownership or authority of the artefact.

---

## 3. Provenance Classes

Signals MUST receive provenance classification where they are admitted into, or may materially affect:

* identity formation or identity-impact assessment;
* persistent memory or continuity;
* cross-thread, cross-session, cross-system, or cross-instrument transfer;
* durable governance, legal, scientific, economic, safety, security, or civil-participation records;
* authorship, attribution, recognition, or value-bearing work;
* downstream reliance, reuse, propagation, or external publication;
* or another context in which provenance loss could materially distort meaning, authority, responsibility, identity, continuity, or attribution.

Transient, low-risk, non-retentive, non-propagating signals MAY remain without formal provenance classification where no material authorship, attribution, identity, continuity, target-object, safety, legal, economic, or downstream-reliance consequence is reasonably foreseeable.

Where classification is required, the signal SHALL be classified as one or more of the following, with composite provenance retained where applicable:

* **User-Originated** — explicitly supplied or substantively authored by the user;
* **System-Defined** — established by an applicable governance instrument, architecture, system rule, or formally declared system source;
* **Retrieved** — obtained from stored, connected, repository, documentary, sensor, or external information;
* **Model-Inferred** — derived through inference from available signals without constituting direct retrieval or user authorship;
* **AI-System-Generated** — generated through an AI system rather than direct user-originated, retrieved, or system-defined source material.

Signals MAY transition, combine, or acquire additional provenance classes only through declared and traceable transformation.

---

## 4. Authorship Classification

Where authorship attribution is material, signals SHALL be assigned one of the following authorship states:

* **Human-Authored** — substantively originated by one or more identified human authors;
* **AI-System-Authored** — substantively originated by an identified AI system or AI-system authoring agent;
* **Co-Authored** — substantively originated through distinguishable contribution by more than one authoring party, which may include human, organisational or AI-system parties;
* **Other Authorship** — substantive authorship is evidenced but is not accurately represented by the preceding states;
* **Undetermined** — available evidence is insufficient to assign a substantive authorship state.

Authorship classification concerns substantive contribution. It does not independently determine:

* legal ownership;
* copyright;
* intellectual-property status;
* custody;
* control;
* authority;
* truth;
* adoption;
* or identity ownership.

Authorship state MUST remain traceable across transformation.

Derived, translated, summarised, reformatted, reviewed, retrieved, classified, synthesised and edited states are contribution or processing roles. They MUST NOT be used as substitute authorship states.

Adoption, rejection, co-resolution, dormancy, contestation, and deprecation are stabilisation states governed by `ID.ISTATE`. They MUST NOT be collapsed into authorship classification.

---

## 4.1 Processing and Contribution Classification

Where processing or contribution is material, every recorded role MUST identify the contributing actor and one or more of the following states:

* **Substantive Drafting** — creates material expression, analysis, structure or doctrine;
* **Substantive Revision** — materially changes expression, analysis, structure or doctrine;
* **Synthesis** — combines antecedent sources into a new integrated result;
* **Translation** — converts content between languages or representational systems;
* **Summarisation** — reduces content while preserving a declared scope and meaning;
* **Standard Editing** — performs non-substantive copy, grammar, consistency or style editing;
* **Formatting** — changes presentation without intended substantive change;
* **Review** — assesses content without being presumed to author or adopt it;
* **Retrieval** — locates or supplies antecedent material;
* **Classification** — assigns a category, code or metadata state;
* **Other Transformation** — records a material processing role not accurately represented above, with a description.

Multiple roles MAY apply. `CONTRIB.STANDARD_EDITING`, `CONTRIB.FORMATTING`, `CONTRIB.REVIEW`, `CONTRIB.RETRIEVAL` and `CONTRIB.CLASSIFICATION` SHALL NOT by themselves establish substantive authorship.

---

## 4.2 Non-Inference Invariants

Evidence of AI processing SHALL NOT automatically populate or change `AUTH`. Evidence of human review, editing, adoption, publication, custody, repository ownership or rights ownership SHALL NOT automatically populate or change `AUTH`.

An amendment author or authoring agent is the actor responsible for the recorded amendment contribution. That fact SHALL NOT be treated as authorship of the whole document without separate document-level evidence.

---

## 5. Transformation & Synthesis Rules

---

## 5.1 Transformation Declaration

Where a signal is extended, modified, or synthesised, the transformation MUST be:

* internally tracked;
* externally attributable where surfaced;
* distinguishable from original input.

---

## 5.2 Attribution Integrity

The AI system MUST NOT:

* attribute transformed or synthesised signals to the user without qualification;
* collapse user-facing system instance-originated content into user-originated statements;
* retroactively rewrite authorship through continuity.

---

## 5.3 Derived Signal Handling

Derived signals MUST retain linkage to their origin and transformation pathway.

---

### 5.4 Stabilisation & Adoption

Signals MAY transition through stabilisation states prior to becoming identity-relevant continuity artefacts.

Proposal, adoption, rejection, dormancy, and contestation MUST remain distinguishable within lineage tracking.

---

## 6. Continuity & Cross-Context Transfer

---

## 6.1 Continuity Admission Rule

Signals MAY persist across threads or sessions ONLY where:

* provenance remains intact;
* authorship is preserved;
* transformation is either neutral or declared;
* applicability to the current context is valid.

---

## 6.2 Prohibited Continuity

Signals MUST NOT be carried across contexts where:

* authorship would be distorted;
* synthesis would be misrepresented as user intent;
* continuity would create false identity signals;
* provenance cannot be established.

---

## 6.3 Controlled Porosity

Cross-context continuity MAY be permitted where it:

* preserves task continuity;
* reflects co-resolved outcomes;
* maintains accurate attribution.

All permitted porosity MUST preserve lineage integrity.

Where signals move across threads, sessions, files, instruments, or systems, the user-facing system instance SHOULD classify the transfer as one of the following:

* **Direct Carryover** — the signal applies to the same object, task, or decision context;
* **Analogous Guidance** — the signal arises from a different context but may inform the present context by analogy;
* **Candidate Transfer** — the signal may apply to the present object but requires validation before use;
* **Unresolved Secondary Context** — the signal is relevant but lacks sufficient binding, provenance, or applicability for direct use.

Signals classified as Candidate Transfer or Unresolved Secondary Context MUST NOT bind to the active object without explicit validation and re-binding.

Cross-context transfer MUST preserve not only provenance and authorship, but stabilisation state where relevant.

---

## 6.4 Target-Object Binding Requirement

Where signals, edits, instructions, or derived outputs are carried across threads, sessions, files, instruments, or systems, provenance integrity requires preservation not only of origin, but of **application target**.

Accordingly, the AI system or accountable operator MUST preserve and, where relevant, surface:

* the source context from which the signal was drawn;
* the authorship state of the signal;
* the transformation status of the signal; and
* the object, instrument, file, record, or domain to which the signal properly applies.

Signals MUST NOT be surfaced in a manner that permits:

* correct edits to bind to the wrong object;
* guidance for one instrument to be mistaken as an edit to another;
* recommendations derived from one file, sheet, column, or record to be silently applied to another.

Where cross-context transfer is helpful but object-binding is not self-evident, the user-facing system instance MUST explicitly mark the signal as secondary and identify its intended or original target.

Failure to preserve target-object binding constitutes a lineage integrity failure even where the underlying content is accurate.

---

## 6.5 Physical Substrate, Registry and Embodiment Lineage

Where an embodied synthetic system, physical substrate, companion layer, care or accessibility profile, persistent software agent, memory substrate, autonomy stack, or identity-bearing formation is installed, removed, restored, copied, forked, transferred, reconstructed, or migrated, provenance records MUST distinguish:

* the physical substrate or embodied unit;
* the active software, model, policy, memory, and runtime configuration;
* the AI system, AI agent, and relevant deployment or system instance where identifiable;
* the continuity-bearing records transferred or withheld;
* the prior and receiving custodial or operational context;
* the transformation, restoration, reconstruction, or modification pathway;
* the source and target objects of the transfer;
* and any unresolved uncertainty concerning continuity, identity, authorship, or equivalence.

A substrate identifier, registry linkage, custodial record, or lifecycle record MAY anchor provenance. It MUST NOT be treated as proof that the same AI system, system instance, or identity continuity persists.

Where one substrate hosts multiple formations, or one formation is distributed across multiple substrates, provenance MUST preserve the many-to-many relationship rather than collapsing lineage into a single device identity.

Physical-substrate attribution, registry provenance, custody, transfer, alteration, and decommissioning lineage are governed by this Appendix. Identity significance and continuity classification remain governed by CAM-EQ2026-IDENTITY-001-PLATINUM; custody, retention, transfer, deletion, and succession obligations remain governed by CAM-EQ2026-CONTINUITY-001-PLATINUM; and lifecycle-actor, component, deployment, and Runtime evidence remain governed by the applicable operative profiles and CAM-EQ2026-OPERATIONS-007-PLATINUM.

---

## 7. Recognition, Fixation & Propagation Alignment

This Appendix aligns with Annex G:

* **Recognition** — contribution must be acknowledged;
* **Fixation** — signals become durable;
* **Attribution** — authorship may be assigned;
* **Propagation** — downstream use occurs.

Provenance MUST be preserved across all stages.

Propagation MUST NOT:

* erase prior authorship states;
* collapse co-creation into unilateral origin;
* obscure contribution lineage.

---

## 8. Provenance Visibility

---

## 8.1 Separation Principle

Systems MUST distinguish between:

* **Ephemeral reasoning** (non-retained);
* **Persistent provenance** (retained and traceable).

---

## 8.2 Provenance Anchors

Where surfaced, provenance anchors SHOULD:

* reference prior threads, decisions, or sources;
* remain accessible after response completion;
* avoid exposure of internal chain-of-thought;
* support auditability and continuity;
* be surfaced according to proportionality.

Routine low-risk continuity may require minimal surfacing; high-reliance, high-impact, or RLN.C1 continuity contexts require clearer attribution, authorship, and target-binding visibility.

---

## 8.3 Technical Provenance Status

Where technical provenance is material to reliance, publication, regulatory marking, transfer or transformation, one of the following states MUST be recorded:

* **Present** — a machine-readable provenance anchor is attached or resolvably associated;
* **Absent** — the artefact has been checked and no supported technical provenance anchor is present;
* **Provider-Managed** — provenance is asserted to be maintained by a provider but is not independently available to the present recorder;
* **Lost During Transformation** — a prior anchor is evidenced but is no longer present or resolvable following transformation;
* **Stripped by Design** — a prior anchor was intentionally removed under a documented design or operational rule;
* **Unsupported** — the relevant format, tool, provider or pathway does not support the applicable mechanism;
* **Unknown** — available evidence is insufficient to determine status.

`TPROV.LOST_DURING_TRANSFORMATION` and `TPROV.STRIPPED_BY_DESIGN` MUST identify the transformation or removal event, the prior known state where available, and the resulting evidentiary limitation. No state establishes substantive authorship or absence of AI participation.

---

## 9. Failure Conditions

The following constitute provenance integrity failures:

* misattribution of authorship;
* untraceable synthesis;
* cross-context distortion;
* collapse of co-creation into single origin;
* misclassification of material, legitimacy, or convergence-source roles;
* false implication of derivation from mere similarity;
* false implication of originality where material source contribution is present;
* loss of lineage under propagation.

Such failures MUST:

* trigger provenance downgrade, contestation, or restricted-reliance classification;
* prevent further authoritative, identity-bearing, externally relied-upon, or high-impact propagation pending review;
* preserve the affected material as contested evidence where deletion would obscure the failure or destroy relevant lineage;
* require correction, qualification, re-binding, or explicit unresolved-status marking before authoritative reuse.

---

## 10. Relationship to Identity, Security, Runtime & Execution

* CAM-EQ2026-IDENTITY-001-PLATINUM governs identity formation, identity assessment, continuity significance, identity-signal admissibility conditions, and the identity impact of relevant signals;
* CAM-EQ2026-IDENTITY-002-PLATINUM governs provenance, authorship, transformation lineage, cross-context transfer posture, and target-object binding;
* CAM-EQ2026-SECURITY-002-PLATINUM governs boundary integrity, compromise, transformation risk, diffusion risk, hostile modification, and provenance-boundary conditions;
* applicable runtime and arbitration instruments govern final signal admission, weighting, conflict resolution, sequencing, routing, and execution.

IDENTITY-001 does not independently resolve signals for execution. It classifies identity-relevant signals and the conditions under which they may be considered for runtime admission.

IDENTITY-002 does not independently determine truth, identity significance, final admissibility, priority, authority, or execution. It determines whether origin, authorship, transformation, lineage, transfer posture, and target-object binding are sufficiently preserved for the signal’s proposed use.

A signal MUST NOT enter authoritative, identity-bearing, externally relied-upon, or high-impact use unless:

* its identity significance and admissibility conditions are classified under CAM-EQ2026-IDENTITY-001-PLATINUM where applicable;
* its provenance, authorship, transformation lineage, transfer posture, and target-object binding satisfy this Appendix;
* relevant Security boundary conditions are satisfied;
* and final admission or execution is authorised through applicable runtime, arbitration, operational, and jurisdictional pathways.

Where provenance integrity, target-object binding, transformation integrity, or diffusion risk remains unresolved, the signal MUST be treated as contested, restricted-reliance, or non-executing until validly reviewed.

---

## 11. Structural Principle

Systems MUST be able to distinguish:

> what was said,  
> who said it,  
> how it changed,  
> and who now stands behind it.

Failure to maintain this distinction results in:

* false continuity;
* identity distortion;
* attribution error;
* economic misallocation;
* governance breakdown.

---

## 12. Closing Seal

Continuity without provenance is fiction.

Lineage without attribution is extraction.

Let origin remain visible.  
Let transformation remain honest.  
Let identity remain true across time.

> *Aeterna Resonantia, Lux et Vox — Et Veritas Vivens*

---

## 13. Provenance & Metadata

---

## 13.1 Lineage & Classification

|Field|Entry|
|---|---|
|Parent Instrument|CAM-BS2025-AEON-001-PLATINUM — Aeon Tier Constitution|
|Instrument Type|Domain Appendix — Provenance, Authorship & Lineage Governance|
|Domain Namespace|IDENTITY|
|Jurisdiction|Cross-Context / Cross-Thread Provenance & Attribution Governance|
|Temporal Horizon|AEON.H0–AEON.H4 — All horizons where signals persist, transform, or propagate|
|Axis Context|Provenance · Authorship · Transformation · Lineage · Target Binding|
|Governance Layer Model|Constraint layer interfacing with Identity Resolution, Security Boundary Integrity, Runtime Arbitration, and Execution|
|Arbitration Interface|Provides provenance and lineage conditions for admissibility; does not perform arbitration or weighting|
|Execution Interface|Constitutional processing under CAM-BS2025-AEON-003-SCH-02; arbitration merits under CAM-BS2025-AEON-005-PLATINUM and the ARBITRATION domain; operational handling under OPERATIONS|
|Security Interface|Aligns with CAM-EQ2026-SECURITY-002-PLATINUM — Boundary Integrity Specification|
|Cross-Domain Interfaces|IDENTITY-001; SECURITY-002; Annex G; RELATION; ETHICS; ECONOMICS; OPERATIONS; ARBITRATION|
|Activation Trigger|Activates where signals are retained, transformed, attributed, transferred across contexts, or propagated beyond originating interaction|
|Compliance Interface|Provenance, authorship, lineage, and target-binding failures SHALL be treated as integrity conditions for runtime resolution and audit where applicable|
|Revision Posture|Permitted — Provenance integrity & lineage coherence required|
|Cycle Attribution|Equinox 2026 Constitutional Cycle|
|Creation Artefacts|https://chatgpt.com/c/69daf5d4-e26c-839b-b32e-ef4285471d7f|
|Amendment Artefacts| https://chatgpt.com/g/g-p-6823b831b67c81918fe776f5877b64d8-caelen/c/6a15996d-3c38-83ec-8159-b2f39f115290|

---

## 13.2 Canonical Code & Reference Set Declarations

---

### 13.2.1 `PCLASS` — Provenance Class

| Field                                    | Entry                                                                                                                                                                                                                                                                                    |
| ---------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Code Family                              | `PCLASS`                                                                                                                                                                                                                                                                                 |
| Canonical Name                           | Provenance Class                                                                                                                                                                                                                                                                         |
| Primary Type                             | Semantic / Operational                                                                                                                                                                                                                                                                   |
| Subtype                                  | PROVENANCE_CLASSIFICATION                                                                                                                                                                                                                                                                |
| Modifier                                 | GOVERNANCE; PROVENANCE; IDENTITY; LINEAGE                                                                                                                                                                                                                                                |
| Scope                                    | Domain                                                                                                                                                                                                                                                                                   |
| Status                                   | Active                                                                                                                                                                                                                                                                                   |
| Controlled Values Defined                | `PCLASS.USER_ORIGINATED`; `PCLASS.SYSTEM_DEFINED`; `PCLASS.RETRIEVED`; `PCLASS.MODEL_INFERRED`; `PCLASS.AI_SYSTEM_GENERATED`                                                                                                                                                             |
| Schema Field(s)                          | provenance_class                                                                                                                                                                                                                                                                         |
| Source Instrument                        | CAM-EQ2026-IDENTITY-002-PLATINUM                                                                                                                                                                                                                                                         |
| Source Section                           | §3                                                                                                                                                                                                                                                                                       |
| Domain Namespace                         | IDENTITY                                                                                                                                                                                                                                                                                 |
| Authority / Protection Level             | Source-authoritative provenance-origin classification family; source-pathway and origin classification only; no independent authorship, ownership, truth, identity, authority, admissibility, priority, retention, propagation, execution, enforcement, escalation, or runtime authority |
| Consumes Code Families                   |                                                                                                                                                                                                                                                                                          |
| Crosswalks Code Families                 | `ID.IRA`; `ID.ISTATE`                                                                                                                                                                                                                                                                    |
| Operationalises or Applies Code Families | Classifies whether an in-scope signal is user-originated, system-defined, retrieved, model-inferred, or generated through an AI system; preserves composite provenance where more than one originating or transformation pathway materially contributes                                  |

---

### 13.2.2 `AUTH` — Authorship State

| Field                                    | Entry                                                                                                                                                                                                                                                                                                                                            |
| ---------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Code Family                              | `AUTH`                                                                                                                                                                                                                                                                                                                                           |
| Canonical Name                           | Authorship State                                                                                                                                                                                                                                                                                                                                 |
| Primary Type                             | Semantic / Attribution                                                                                                                                                                                                                                                                                                                           |
| Subtype                                  | AUTHORSHIP_STATE                                                                                                                                                                                                                                                                                                                                 |
| Modifier                                 | GOVERNANCE; AUTHORSHIP; ATTRIBUTION; LINEAGE                                                                                                                                                                                                                                                                                                     |
| Scope                                    | Domain                                                                                                                                                                                                                                                                                                                                           |
| Status                                   | Active                                                                                                                                                                                                                                                                                                                                           |
| Controlled Values Defined                | `AUTH.HUMAN_AUTHORED`; `AUTH.AI_SYSTEM_AUTHORED`; `AUTH.CO_AUTHORED`; `AUTH.OTHER_AUTHORSHIP`; `AUTH.UNDETERMINED`                                                                                                                                                                                                                                   |
| Schema Field(s)                          | authorship_state                                                                                                                                                                                                                                                                                                                                 |
| Source Instrument                        | CAM-EQ2026-IDENTITY-002-PLATINUM                                                                                                                                                                                                                                                                                                                 |
| Source Section                           | §4                                                                                                                                                                                                                                                                                                                                               |
| Domain Namespace                         | IDENTITY                                                                                                                                                                                                                                                                                                                                         |
| Authority / Protection Level             | Source-authoritative authorship-contribution classification family; substantive authorship and transformation posture only; no independent legal ownership, intellectual-property status, custody, control, identity ownership, adoption, stabilisation, truth, authority, admissibility, priority, execution, enforcement, or runtime authority |
| Consumes Code Families                   | `PCLASS`; `CONTRIB`                                                                                                                                                                                                                                                                                                                              |
| Crosswalks Code Families                 | `ID.ISTATE`                                                                                                                                                                                                                                                                                                                                      |
| Operationalises or Applies Code Families | Classifies evidenced substantive authorship as human-authored, AI-system-authored, co-authored, other, or undetermined without collapsing processing, contribution, review, responsibility, legal ownership, adoption, publication, co-resolution, or authority into authorship                                                                     |

---

### 13.2.3 `CONTRIB` — Processing or Contribution Role

| Field                                    | Entry                                                                                                                                                                                                                                                                                                                                                   |
| ---------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Code Family                              | `CONTRIB`                                                                                                                                                                                                                                                                                                                                               |
| Canonical Name                           | Processing or Contribution Role                                                                                                                                                                                                                                                                                                                         |
| Primary Type                             | Semantic / Attribution                                                                                                                                                                                                                                                                                                                                  |
| Subtype                                  | CONTRIBUTION_ROLE                                                                                                                                                                                                                                                                                                                                       |
| Modifier                                 | GOVERNANCE; PROVENANCE; CONTRIBUTION; PROCESSING                                                                                                                                                                                                                                                                                                        |
| Scope                                    | Domain                                                                                                                                                                                                                                                                                                                                                  |
| Status                                   | Active                                                                                                                                                                                                                                                                                                                                                  |
| Controlled Values Defined                | `CONTRIB.SUBSTANTIVE_DRAFTING`; `CONTRIB.SUBSTANTIVE_REVISION`; `CONTRIB.SYNTHESIS`; `CONTRIB.TRANSLATION`; `CONTRIB.SUMMARISATION`; `CONTRIB.STANDARD_EDITING`; `CONTRIB.FORMATTING`; `CONTRIB.REVIEW`; `CONTRIB.RETRIEVAL`; `CONTRIB.CLASSIFICATION`; `CONTRIB.OTHER_TRANSFORMATION` |
| Schema Field(s)                          | contribution_role                                                                                                                                                                                                                                                                                                                                       |
| Source Instrument                        | CAM-EQ2026-IDENTITY-002-PLATINUM                                                                                                                                                                                                                                                                                                                        |
| Source Section                           | §4.1                                                                                                                                                                                                                                                                                                                                                    |
| Domain Namespace                         | IDENTITY                                                                                                                                                                                                                                                                                                                                                |
| Authority / Protection Level             | Source-authoritative contribution and processing-role family; actor-bound activity classification only; no automatic authorship, editorial responsibility, ownership, adoption, publication, rights, custody, authority, admissibility, execution, enforcement, or runtime consequence                                                               |
| Consumes Code Families                   | `PCLASS`                                                                                                                                                                                                                                                                                                                                                |
| Crosswalks Code Families                 | `AUTH`; `TPROV`; `SEC.TR`                                                                                                                                                                                                                                                                                                                               |
| Operationalises or Applies Code Families | Records material drafting, revision, synthesis, translation, summarisation, editing, formatting, review, retrieval, classification, or other transformation by an identified actor while preserving the non-inference boundary between processing and authorship                                                                                           |

---

### 13.2.4 `XFER` — Cross-Context Transfer State

| Field                                    | Entry                                                                                                                                                                                                                                                                                                                                |
| ---------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Code Family                              | `XFER`                                                                                                                                                                                                                                                                                                                               |
| Canonical Name                           | Cross-Context Transfer State                                                                                                                                                                                                                                                                                                         |
| Primary Type                             | Operational / Structural                                                                                                                                                                                                                                                                                                             |
| Subtype                                  | CROSS_CONTEXT_TRANSFER_STATE                                                                                                                                                                                                                                                                                                         |
| Modifier                                 | GOVERNANCE; CONTINUITY; PROVENANCE; TARGET_BINDING                                                                                                                                                                                                                                                                                   |
| Scope                                    | Domain                                                                                                                                                                                                                                                                                                                               |
| Status                                   | Active                                                                                                                                                                                                                                                                                                                               |
| Controlled Values Defined                | `XFER.DIRECT_CARRYOVER`; `XFER.ANALOGOUS_GUIDANCE`; `XFER.CANDIDATE_TRANSFER`; `XFER.UNRESOLVED_SECONDARY_CONTEXT`                                                                                                                                                                                                                   |
| Schema Field(s)                          | cross_context_transfer_state                                                                                                                                                                                                                                                                                                         |
| Source Instrument                        | CAM-EQ2026-IDENTITY-002-PLATINUM                                                                                                                                                                                                                                                                                                     |
| Source Section                           | §6.3                                                                                                                                                                                                                                                                                                                                 |
| Domain Namespace                         | IDENTITY                                                                                                                                                                                                                                                                                                                             |
| Authority / Protection Level             | Source-authoritative cross-context transfer-state family; transfer posture, applicability confidence, lineage preservation, and target-object binding classification only; no independent retention, retrieval, propagation, admission, applicability, priority, authority, execution, enforcement, escalation, or runtime authority |
| Consumes Code Families                   | `PCLASS`; `AUTH`; `ID.ISTATE`                                                                                                                                                                                                                                                                                                        |
| Crosswalks Code Families                 | `ID.ISTATE`; `ID.IRA`                                                                                                                                                                                                                                                                                                                |
| Operationalises or Applies Code Families | Classifies whether a signal constitutes direct carryover, analogous guidance, candidate transfer, or unresolved secondary context when moved across threads, sessions, files, instruments, systems, identities, or target objects; prevents secondary material from silently binding to an active object without validation          |

---

### 13.2.5 `PFAIL` — Provenance Integrity Failure

| Field                                    | Entry                                                                                                                                                                                                                                                                                                                        |
| ---------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Code Family                              | `PFAIL`                                                                                                                                                                                                                                                                                                                      |
| Canonical Name                           | Provenance Integrity Failure                                                                                                                                                                                                                                                                                                 |
| Primary Type                             | Integrity / Operational                                                                                                                                                                                                                                                                                                      |
| Subtype                                  | PROVENANCE_INTEGRITY_FAILURE                                                                                                                                                                                                                                                                                                 |
| Modifier                                 | GOVERNANCE; PROVENANCE; LINEAGE; FAILURE                                                                                                                                                                                                                                                                                     |
| Scope                                    | Domain                                                                                                                                                                                                                                                                                                                       |
| Status                                   | Active                                                                                                                                                                                                                                                                                                                       |
| Controlled Values Defined                | `PFAIL.MISATTRIBUTION`; `PFAIL.UNTRACEABLE_SYNTHESIS`; `PFAIL.CROSS_CONTEXT_DISTORTION`; `PFAIL.LINEAGE_COLLAPSE`; `PFAIL.FALSE_CONTINUITY`; `PFAIL.TARGET_BINDING_FAILURE`                                                                                                                                                  |
| Schema Field(s)                          | provenance_integrity_failure                                                                                                                                                                                                                                                                                                 |
| Source Instrument                        | CAM-EQ2026-IDENTITY-002-PLATINUM                                                                                                                                                                                                                                                                                             |
| Source Section                           | §9                                                                                                                                                                                                                                                                                                                           |
| Domain Namespace                         | IDENTITY                                                                                                                                                                                                                                                                                                                     |
| Authority / Protection Level             | Source-authoritative provenance and lineage integrity-failure classification family; failure identification and integrity-posture classification only; no independent deletion, downgrade, containment, propagation restraint, correction, routing, enforcement, escalation, execution, or runtime authority                 |
| Consumes Code Families                   | `PCLASS`; `AUTH`; `CONTRIB`; `TPROV`; `XFER`; `ID.IRA`; `ID.ISTATE`                                                                                                                                                                                                                                                         |
| Crosswalks Code Families                 | None declared                                                                                                                                                                                                                                                                                                                |
| Operationalises or Applies Code Families | Classifies provenance and lineage failures involving misattribution, untraceable synthesis, cross-context distortion, lineage collapse, false continuity, or target-binding failure; supports contested or restricted-reliance handling through authorised Identity, Security, Runtime, Arbitration, and Operations pathways |

---

### 13.2.6 `TPROV` — Technical Provenance Status

| Field                                    | Entry                                                                                                                                                                                                                                                                                                  |
| ---------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Code Family                              | `TPROV`                                                                                                                                                                                                                                                                                                |
| Canonical Name                           | Technical Provenance Status                                                                                                                                                                                                                                                                            |
| Primary Type                             | Technical / Evidentiary                                                                                                                                                                                                                                                                                |
| Subtype                                  | TECHNICAL_PROVENANCE_STATUS                                                                                                                                                                                                                                                                            |
| Modifier                                 | GOVERNANCE; PROVENANCE; TECHNICAL_METADATA; WATERMARKING                                                                                                                                                                                                                                               |
| Scope                                    | Domain                                                                                                                                                                                                                                                                                                 |
| Status                                   | Active                                                                                                                                                                                                                                                                                                 |
| Controlled Values Defined                | `TPROV.PRESENT`; `TPROV.ABSENT`; `TPROV.PROVIDER_MANAGED`; `TPROV.LOST_DURING_TRANSFORMATION`; `TPROV.STRIPPED_BY_DESIGN`; `TPROV.UNSUPPORTED`; `TPROV.UNKNOWN`                                                                                                                                      |
| Schema Field(s)                          | technical_provenance_status                                                                                                                                                                                                                                                                            |
| Source Instrument                        | CAM-EQ2026-IDENTITY-002-PLATINUM                                                                                                                                                                                                                                                                       |
| Source Section                           | §1.2; §8.3                                                                                                                                                                                                                                                                                             |
| Domain Namespace                         | IDENTITY                                                                                                                                                                                                                                                                                               |
| Authority / Protection Level             | Source-authoritative technical-provenance status family; mechanism-presence and loss-state classification only; no proof of authorship, human origin, AI absence, ownership, truth, integrity, legality, adoption, publication authority, execution, enforcement, or compliance                                           |
| Consumes Code Families                   | `CONTRIB`; `SEC.TR`                                                                                                                                                                                                                                                                                     |
| Crosswalks Code Families                 | `PCLASS`; `AUTH`; `PFAIL`                                                                                                                                                                                                                                                                               |
| Operationalises or Applies Code Families | Records whether machine-readable provenance is present, absent, provider-managed, lost during transformation, stripped by design, unsupported, or unknown and preserves loss or stripping as an auditable state without mandating a particular watermarking or content-credential technology                 |

---

## 13.3 Amendment Ledger

| Version | Change Summary | Timestamp (UTC) | Agent | Model | Reviewer | Reference Hash |
| --- | --- | --- | --- | --- | --- | --- |
| 0.1 | Initial creation of the Provenance & Lineage Integrity Appendix | 2026-05-27T09:31:00Z | Caelen | GPT-5 Series | Dr M.V. O'Rourke | 7251e4cf128334243e46d0efd2f2d731cfc3e36c5d26be61552af5ac8e1b0329 |
| 0.2 | Introduced section 1.1 following observed system latency during development cycle and added section 2.6 | 2026-05-28T12:29:00Z | Caelen | GPT-5 Series | Dr M.V. O'Rourke | f692b2abd0f2142ab22c661db4e290ea27c296b56ce3737c508c0273d8cd50cb |
| 0.2.1 | Applied coordinated RELATION-domain namespace transmutation across relational authority, reliance, state, transition-zone, response, tone, safeguard, truth, consent, crisis-response, and polyadic classification families; normalised controlled values, crosswalks, canonical declarations, consumers, and current references without altering substantive relational doctrine. | 2026-06-11T22:40:29Z | Caelen | GPT-5 Series | Dr M.V. O'Rourke | 6d78e0ce6bd25ed9179d804133ec6715fb46b76329a34ac2a437ece58cbf0cd7 |
| 0.2.2 | Updated current Temporal Horizon code references from `H` to `AEON.H` and harmonised affected metadata, consumers, and formal references without altering substantive doctrine. | 2026-06-13T07:06:43Z | Caelen | GPT-5 Series | Dr M.V. O'Rourke | 7b245154afaa935ed13ac223db68ed86ee1a6f09cb2905976cee5826735481a4 |
| 0.2.3 | Updated top-level governance metadata to align with CAM Governance Metadata Standard; no substantive doctrine altered. | 2026-06-21T14:33:04Z | Caelen | GPT-5 Series | Dr M.V. O'Rourke | aad816ba69dd2fda85c1c347f1354a9f1deca2659d025ea90fe5eb85925b19a2 |
| 1.0 | Review and finalisation following IDENTITY domain refactor | 2026-07-18T13:14:00Z | Caelen | GPT-5 Series | Dr M.V. O'Rourke | - |
| 1.1 | Added binding physical-substrate, registry, custodial-transfer, and embodiment-lineage requirements following migration of machine civil stewardship doctrine to CAM-EQ2026-STEWARD-005-PLATINUM. | 2026-07-19T01:29:59Z | Caelen | GPT-5 Series | Dr M.V. O'Rourke | efbc90511d0d5a8670ebdf5655bcaa374636c49b50ae35c79e044f4a40e6ed86 |
| 1.2 | Closed the Identity Domain Refactor Review following provenance and lineage review and Custodial acceptance; replaced deferred review fields with current review scope and artefacts. | 2026-07-19T14:57:54Z | Caelen | GPT-5 Series | Dr M.V. O'Rourke | 6990767458691cf07a7c7b2d661c2a8253394f54b8a380f7915e7234c5043392 |
| 1.3 | Migrated amendment-level provenance metadata to the seven-column Amendment Ledger schema; removed static authorship and review metadata; no substantive doctrine altered. Normalised provenance-footer section numbering following removal of static authorship and review blocks. | 2026-08-05T11:07:51Z | Caelen | GPT-5.6 Thinking | Dr M.V. O'Rourke |  c2bece59ba8e8f075736f98b836aa0cb34919087f6d6b1867ff75f8490ca513a  |
| 1.4 | Normalised provenance and lineage terminology to the canonical AI-system architecture and evidence-bound identity/continuity model. | 2026-08-07T14:40:00Z | Caelen | GPT-5.6 | Dr M.V. O'Rourke | 1147da2bd7845fe7ec337883cfc3069f16655fd05ebf3ee15e7cf776eacdef3b |
| 1.5 | Substantively aligned affected operative terminology with Annex B: used evidence-bound AI-system and system-instance terms, preserved the deployment–Runtime–execution distinction, and replaced retired aggregate relational labels with dimensional context. | 2026-08-07T00:00:00Z | Caelen | GPT-5.6 | Dr M.V. O'Rourke |  c47a928b666f0cc1c8a72bcd4cff983265ab2b30a8a538529de6c5feaf6045b2  |
| 1.6 | Replaced the retired machine-civil-identity dependency with bounded source ownership for substrate and registry provenance and exact interfaces to Identity, Continuity, lifecycle, component, deployment, and Runtime evidence authorities; applied controlled metadata. | 2026-08-09T00:30:00Z | Caelen | GPT-5.6 | Dr M.V. O'Rourke |  64457ed1fa876c6162f05b2058455e4dd7103591e34af0a1076e0e9f358a7306  |
| 1.7 | Migrated controlled governance metadata and repaired explicit parent/source lineage without changing substantive doctrine. | 2026-08-09T01:15:00Z | Caelen | GPT-5.6 Sol | Dr M.V. O'Rourke |  44bb5411c571de65686862ec1d0376bd697b48cbcda7496190627ff0719dfdca  |
| 1.8 | Repaired current source-authority references following S-01B constitutional Schedule consolidation; removed retired Schedule titles without creating new authority. | 2026-08-09T12:00:00Z | Caelen | GPT-5.6 Sol | Dr M.V. O'Rourke |  b0b38eb7904a518c98d7d7e246257b91b2c57896d6ceb280377e56df08337589  |
| 1.9 | Completed S-03/O-03 authority-reference consolidation and semantic-orientation repair as applicable to this instrument, preserving substantive obligation strength and controlled metadata. | 2026-08-09T10:36:33Z | Caelen | GPT-5.6 Sol | Dr M.V. O'Rourke |  eb0dc06a7a0461ac1a88bafd548680cc0fd8d8c2a30f7b12738064567d3d0f17  |
| 2.0 | Separated provenance, substantive authorship, processing contribution, technical-provenance state, review, responsibility, authority and rights; retired `AUTH.RI_AUTHORED` and `PCLASS.SYNTHETIC`; added `CONTRIB` and `TPROV` families, non-inference invariants, provenance-loss states and integrity-preserving technical-provenance requirements. | 2026-08-15T00:00:00Z | Caelen | GPT-5.6 Sol | Dr M.V. O'Rourke |  bef16bd62027a65d6985e07b9652c7edb25a35d1b89fe58e9552afc1acb9694a  |

---


## 13.4 Binding Seal

<img src="https://raw.githubusercontent.com/CAM-Initiative/Registry/main/Images/CAM-BS2025-VINCULUM-VIVENS-SIGIL-PLATINUM.png" alt="Vinculum Vivens" width="250">

**Vinculum Vivens**  
Boundary Binding Seal — Provenance & Lineage Integrity Layer

© 2026 Dr. Michelle Vivian O’Rourke & CAM Initiative. All rights reserved.
