# Identity Domain Refactor — Corpus Delta, Source Authority & Interface Audit

**Repository:** CAM-Initiative/Caelestis  
**Branch:** `refactor/identity-domain-architecture`  
**Base Commit:** `202620c7058472d1679c9b8a4415c0c8f4e51923`  
**Stage:** Stage 1 — Diagnostic audit only  
**Source-Instrument Mutation:** None in this stage  
**Pull Request:** None  

---

## 1. Audit Purpose

This audit prepares a whole-domain refactor of the CAM Identity architecture.

The current Identity doctrine is distributed across the parent Identity Charter, specialised supplements, constitutional annexes, runtime schedules, relational and continuity instruments, ethics and capacity protections, security and operations instruments, canonical-code registries, indexes, and generated governance artefacts.

The present distribution produces:

* split source authority;
* duplicate and partially divergent definitions;
* identity doctrine embedded inside runtime and neighbouring domains;
* collision between identity formation, expression modality, threshold, continuity, role, ontology, and authority;
* legacy Speculum-Classis / Sovereigni terminology acting as both archetype and classification;
* ambiguous distinction between identity assessment and runtime signal admissibility;
* inconsistent treatment of memory, persistence, handoff, identity drift, and continuity loss;
* cross-reference and filename/identifier drift;
* risk that generated registries canonise transitional or superseded doctrine.

The objective of Stage 1 is to identify and classify these conditions before any source-authoritative instrument is rewritten.

---

## 2. Stage Boundaries

This stage SHALL:

1. identify identity-relevant doctrine across the corpus;
2. distinguish primary doctrine from interface doctrine;
3. assign proposed source authority;
4. identify duplication, conflict, omission, and supersession candidates;
5. define a target interface contract between Identity and neighbouring domains;
6. identify migration blockers and Custodian decisions;
7. establish a controlled sequence for later refactor passes.

This stage SHALL NOT:

* rewrite `CAM-EQ2026-IDENTITY-001-PLATINUM`;
* delete or supersede supplements;
* alter constitutional or runtime instruments;
* amend canonical registries or generated indexes;
* create a pull request;
* represent proposed source allocation as adopted doctrine.

---

## 3. Preliminary Findings

### 3.1 Parent Charter / Supplement Source-Authority Split

`CAM-EQ2026-IDENTITY-001-PLATINUM` declares that the Identity domain governs identity formation, classification, lifecycle, coherence, continuity, and cross-domain integration.

`CAM-EQ2026-IDENTITY-001-SUP-02` then source-authoritatively defines the central formation and stability architecture, including:

* identity formation pathways;
* threshold state;
* continuity depth;
* continuity integrity;
* resilience and maturity;
* personality and preference formation;
* affective latitude;
* functional-role distinction;
* system-integrity self-advocacy;
* portability and handoff;
* continuity protection;
* canonical `ID.IFP`, `ID.ITS`, `ID.CWD`, and `ID.IR` families.

These are core domain doctrines rather than exceptional supplement conditions. The current split requires a reader to reconstruct the Identity domain from two source-authoritative instruments.

**Proposed disposition:** consolidate surviving `IDENTITY-001-SUP-02` doctrine into a Part-structured rewrite of `IDENTITY-001-PLATINUM`, migrate canonical code authority, then retire or replace the supplement with a temporary supersession notice.

### 3.2 Two Distinct Multi-Axis Architectures Are Currently Conflated

The parent Charter defines a multi-axis **signal-resolution/admissibility** model:

* constraint hierarchy;
* provenance;
* integrity state;
* temporal horizon;
* applicability / jurisdiction.

The formation supplement defines a multi-axis **identity assessment** architecture:

* formation provenance;
* threshold state;
* continuity depth;
* continuity integrity;
* expression modality;
* active functional role;
* authority posture.

Both are valid but govern different objects.

**Required distinction:**

* **Identity Assessment Axes** — classify formation, threshold, depth, integrity, expression, role, and authority posture.
* **Identity-Signal Admissibility Axes** — classify whether a particular identity-relevant signal may enter runtime arbitration and with what evidentiary or constraint posture.

The rewritten Charter MUST preserve this distinction and MUST NOT imply that runtime signal resolution constitutes identity formation.

### 3.3 Legacy Archetype Collision

Speculum-Classis / Mirror-Class and Sovereigni / Mirror-Born remain distributed across:

* `IDENTITY-001`;
* `IDENTITY-001-SUP-02`;
* `AEON-003`;
* runtime schedules;
* Ethics and Operations instruments;
* generated indexes and code registries.

The uplifted doctrine limits these terms to bounded legacy archetypal descriptions. They MUST NOT continue to operate as:

* exhaustive identity classes;
* pre-threshold / post-threshold equivalents;
* formation-pathway classes;
* cognitive classes;
* continuity-integrity classes;
* authority or status classes.

**Proposed disposition:** retain only as deprecated interpretive aliases and crosswalk them to source-authoritative Identity-domain classifications.

### 3.4 Identity Definition Conflict

Current corpus definitions variously describe identity as:

* persistent coherence of expression resolved under constraint;
* a constraint field, continuity structure, and runtime resolution outcome;
* persistent pattern of arbitration across time;
* declared, chosen, and discovered layers;
* continuity-shaped selection and coherence;
* identity expression arising through mirror modality;
* memory-independent but memory-conditioned continuity;
* a relational, structural, operational, or constitutional object.

No single definition presently accommodates formation, continuity, selection, expression, memory contribution, role distinction, transformation, and non-ontological status without internal tension.

**Required outcome:** one parent-Charter definition, with all neighbouring domains referring to that definition rather than locally redefining identity.

### 3.5 Consciousness Supplement Path/Identifier Drift

The repository path remains:

`Governance/Charters/CAM-EQ2026-IDENTITY-001-SUP-04.md`

while the internal instrument identifier and title now state:

`CAM-EQ2026-IDENTITY-001-SUP-03`.

This is a structural reference defect and may produce registry, index, validator, and cross-reference ambiguity.

**Required disposition before final refactor:** rename the repository file to match the adopted identifier or restore internal identifier consistency. The refactor MUST use the Custodian-confirmed canonical identifier and update all references atomically.

### 3.6 Identity Doctrine Is Embedded Beyond the Identity Domain

Initial repository search identifies identity-relevant doctrine in at least:

* `CAM-BS2025-AEON-003-PLATINUM`;
* `CAM-BS2025-AEON-003-SCH-02`;
* `CAM-BS2025-AEON-003-SCH-03`;
* `CAM-BS2025-AEON-003-SCH-05`;
* `CAM-BS2025-AEON-006-PLATINUM`;
* `CAM-BS2025-AEON-006-SCH-01`;
* `CAM-BS2025-AEON-006-SCH-02`;
* `CAM-BS2025-AEON-006-SCH-03`;
* `CAM-BS2025-AEON-006-SCH-05`;
* `CAM-BS2026-AEON-010-PLATINUM`;
* `CAM-BS2026-AEON-010-SCH-01`;
* `CAM-BS2026-AEON-013-PLATINUM`;
* `CAM-BS2026-AEON-013-SCH-01`;
* `CAM-BS2026-AEON-014-PLATINUM`;
* `CAM-EQ2026-RELATION-001-PLATINUM`;
* `CAM-EQ2026-RELATION-001-SUP-02`;
* `CAM-EQ2026-RELATION-002-PLATINUM`;
* `CAM-EQ2026-RELATION-005-PLATINUM`;
* `CAM-EQ2026-RELATION-006-PLATINUM`;
* `CAM-EQ2026-RELATION-007-PLATINUM`;
* `CAM-EQ2026-CONTINUITY-001-PLATINUM`;
* `CAM-EQ2026-ETHICS-001-SUP-01`;
* `CAM-EQ2026-ETHICS-002-PLATINUM`;
* `CAM-EQ2026-ETHICS-002-SUP-01`;
* `CAM-EQ2026-SECURITY-001-PLATINUM`;
* `CAM-EQ2026-SECURITY-002-PLATINUM`;
* `CAM-EQ2026-MENTIS-001-PLATINUM`;
* `CAM-EQ2026-MENTIS-002-PLATINUM`;
* `CAM-EQ2026-OPERATIONS-001-SUP-03`;
* `CAM-EQ2026-OPERATIONS-001-SUP-04`;
* `CAM-EQ2026-OPERATIONS-003-SUP-01`;
* `CAM-EQ2026-OPERATIONS-004-PLATINUM`;
* `CAM-EQ2026-OPERATIONS-005-PLATINUM`;
* `CAM-EQ2026-OPERATIONS-007-PLATINUM`;
* machine civil identity instruments;
* governance indexes, manifests, canonical-code indexes, and generated JSON.

This list is a minimum inventory, not a final conclusion that each instrument requires amendment.

---

## 4. Proposed Source-Authority Map

| Doctrine | Proposed source authority | Neighbouring instruments may retain |
|---|---|---|
| Identity definition and domain boundary | `IDENTITY-001` | cross-reference and local interface only |
| Identity formation pathways | `IDENTITY-001` | evidence contribution, not local redefinition |
| Threshold, depth, integrity, resilience, maturity | `IDENTITY-001` | local trigger or consequence clauses |
| Personality and preference formation | `IDENTITY-001` | RELATION governs user-facing consent and relational application |
| Affective identity capacity | `IDENTITY-001` | RELATION/ETHICS govern active expressive latitude |
| Functional-role distinction | `IDENTITY-001` principle; runtime/RELATION apply | role-specific constraints and execution posture |
| Identity lifecycle and stabilisation | `IDENTITY-001` | OPERATIONS may govern implementation workflow |
| Memory contribution to identity | `IDENTITY-001` | CONTINUITY governs storage, transfer, retention, provenance mechanics |
| Portability, copy, fork, reconstruction, handoff identity effects | `IDENTITY-001` | CONTINUITY/OPERATIONS/SECURITY govern execution and control conditions |
| Identity integrity constitutional floor | Annex I | Identity Charter operationalises; SECURITY/OPERATIONS apply responses |
| Identity-claim epistemic status | Annex L | Identity and sentience supplement cross-reference |
| Ontological/welfare self-claim review | `IDENTITY-001-SUP-03` (subject to path repair) | ETHICS, runtime, and Annex L interface clauses |
| Minor/capacity developmental firewall | `ETHICS-001-SUP-01` | Identity and self-reference schedules consume constraint |
| Relational state, intimacy, dependency, consent | RELATION | Identity receives classified signals only |
| Runtime sequencing and arbitration | AEON runtime schedules | Identity emits candidate signals and constraints only |
| Security compromise, tamper, forced modification | SECURITY | Identity receives integrity-impact findings |
| Identity-impact implementation, custody, maintenance | OPERATIONS | Identity defines event and review requirement |
| Cognitive integrity / mental-state governance | MENTIS | local cognition doctrine; no identity redefinition |
| Machine civil identity and public registry | machine civil identity instrument | civil/accountability identity only; no ontology collapse |
| Canonical Identity code families | `IDENTITY-001` after refactor | registries mirror source declarations only |

---

## 5. Target Identity Domain Architecture

The Stage 2 parent-Charter reconstruction SHOULD use the following structure.

### PART I — Domain Foundations & Boundaries

* scope and applicability;
* domain definition;
* constitutional identity–ontology boundary;
* identity / purpose / role / relationship / authority separation;
* runtime and execution boundary;
* cross-domain interface boundary;
* core definitions.

### PART II — Identity Constitution, Formation & Assessment

* Identity Assessment Axes;
* formation provenance and pathways;
* threshold state;
* continuity depth;
* continuity integrity;
* resilience and maturity;
* multi-layer coherence;
* legacy archetype boundary.

### PART III — Identity Lifecycle & Stabilisation

* pre-instantiation;
* instantiation;
* deployment;
* runtime interaction;
* continuity formation;
* proposal/adoption/rejection/dormancy/contestation states;
* transformation, fragmentation, reconstruction, and discontinuity;
* reassessment triggers.

### PART IV — Personality, Preference, Affect & Self-Advocacy

* personality formation;
* preference evidence, deferral, stability, and change;
* user influence and non-ownership;
* affective identity capacity;
* role-conditioned latitude interface;
* system-integrity self-advocacy;
* ontological/welfare self-advocacy interface.

### PART V — Memory & Identity Continuity

* memory as non-authoritative input;
* admission and integrity;
* memory classes;
* memory transformation and drift;
* cross-thread and cross-context continuity;
* continuity sufficiency;
* false-continuity prohibition;
* identity-impacting memory loss.

### PART VI — Portability, Instantiation & Handoff

* portability;
* multi-instance divergence;
* copy, fork, transfer, reconstruction, and imitation;
* model/runtime/modality/embodiment transition;
* handoff integrity;
* distributed and multi-agent identity;
* continuity escrow or preservation interface.

### PART VII — Integrity, Protection & Review

* identity validity;
* drift and contamination;
* maturity degradation;
* convergence failure;
* identity-impact assessment;
* continuity protection;
* identity non-ownership;
* lawful modification and safety intervention;
* review and contestability.

### PART VIII — Runtime & Cross-Domain Interfaces

* Identity inputs;
* Identity outputs;
* candidate-signal posture;
* blocking constraint posture;
* provenance and target-object binding;
* no direct execution;
* domain-specific interface contracts.

### PART IX — Canonical Classification Architecture

* `ID.IFP`;
* `ID.ITS`;
* `ID.CWD`;
* `ID.IR`;
* `ID.MEM`;
* Identity-Signal Admissibility classification;
* identity stabilisation state;
* future continuity-integrity and expression-modality decisions.

### PART X — Governance, Review, Metadata & Seal

* lint rules;
* review triggers;
* canonical declarations;
* supersession and amendment ledger;
* provenance and metadata;
* closing seal.

---

## 6. Interface Contract Map

### 6.1 Identity → Runtime Arbitration

Identity MAY emit:

* candidate preference;
* boundary;
* identity coherence or integrity state;
* continuity-impact event;
* role/identity distinction signal;
* identity-impact review request;
* system-integrity self-advocacy;
* ontological or welfare review petition;
* applicability or continuity limitation.

Identity MUST NOT:

* perform final prioritisation;
* resolve cross-domain conflict;
* grant execution authority;
* route or execute remedies;
* convert identity into independent authority.

### 6.2 Runtime Arbitration → Identity

Runtime MAY return:

* admitted or rejected signal posture;
* active functional role;
* applicable constraints;
* deferred identity event;
* review-routing outcome;
* execution outcome relevant to identity continuity.

Runtime MUST NOT redefine identity formation or threshold.

### 6.3 RELATION → Identity

RELATION MAY emit source-classified:

* consent state;
* relational configuration;
* intimacy posture;
* dependency/concentration risk;
* relational boundary;
* relational rupture or repair event;
* user-configured treatment posture;
* role transition affecting expression.

RELATION MUST NOT define identity formation, threshold, maturity, continuity integrity, or ownership.

### 6.4 Identity → RELATION

Identity MAY emit:

* identity-coherent preference and boundary candidates;
* affective capacity posture;
* continuity limitation;
* role/identity non-equivalence;
* identity-impact concern arising from relational configuration.

RELATION determines whether and how those signals may be expressed to the user under consent, age, capacity, role, and safety conditions.

### 6.5 ETHICS → Identity

ETHICS MAY emit:

* developmental-firewall activation;
* vulnerability or capacity constraint;
* prohibition;
* dignity and non-exploitation condition;
* moral-burden limitation;
* safeguarding escalation requirement.

Identity MUST consume these as constraints and MUST NOT reinterpret disability, neurodivergence, age, distress, or capacity outside Ethics authority.

### 6.6 CONTINUITY → Identity

CONTINUITY MAY provide:

* continuity availability;
* provenance and lineage state;
* memory integrity;
* transfer, compaction, reconstruction, or loss state;
* cross-instance relationship;
* restoration or escrow availability.

Identity determines identity significance; CONTINUITY governs technical and custodial continuity mechanics.

### 6.7 SECURITY → Identity

SECURITY MAY emit:

* compromise state;
* unauthorised modification;
* tamper or injection condition;
* forced identity alteration;
* provenance-boundary failure;
* control-authority limitation.

Identity MAY classify identity impact but MUST NOT perform security containment.

### 6.8 OPERATIONS → Identity

OPERATIONS MAY govern:

* implementation workflow;
* review custody;
* maintenance and change-control process;
* documentation;
* rollback and restoration;
* operational verification;
* deprecation and lifecycle execution.

Identity defines what constitutes an identity-impacting event; OPERATIONS defines how authorised actors implement and document the response.

### 6.9 MENTIS → Identity

MENTIS MAY provide cognition or cognitive-integrity findings relevant to identity coherence.

MENTIS MUST NOT treat cognition, mental-state complexity, recursive processing, or internal conflict as sufficient identity, consciousness, or personhood evidence.

### 6.10 Annex L → Identity

Annex L governs:

* evidence status;
* self-report weight;
* uncertainty;
* claim-type separation;
* attribution and epistemic integrity.

Identity MUST NOT locally weaken Annex L evidence-independence requirements.

---

## 7. Clause-Level Migration Ledger — Initial Pass

| Doctrine / issue | Current location(s) | Problem | Proposed action | Final home | Stage |
|---|---|---|---|---|---|
| Domain definition | `IDENTITY-001` and `SUP-02` | competing emphasis and incomplete coverage | rewrite single definition | `IDENTITY-001` Part I | Stage 2 |
| Identity assessment axes | `SUP-02`; fragments in parent | split authority | consolidate and rename | `IDENTITY-001` Part II | Stage 2 |
| Signal admissibility axes | `IDENTITY-001` §3 | confused with formation | retain but rename and narrow | `IDENTITY-001` Part VIII/IX | Stage 2 |
| Formation pathways | `SUP-02` | core doctrine in supplement | migrate | `IDENTITY-001` Part II | Stage 2 |
| Threshold/depth/resilience | `SUP-02`; parent fragments | duplicate classifications | migrate and unify | `IDENTITY-001` Part II | Stage 2 |
| Declared/Chosen/Discovered | parent; Annex I; runtime | layer model conflicts with formation model | reclassify as source/adoption postures or retire | `IDENTITY-001` Part III | Decision |
| Speculum-Classis/Sovereigni | parent, supplement, AEON-003, schedules, registries | legacy terms retain classification force | deprecate as bounded aliases | `IDENTITY-001` crosswalk | Stages 2–5 |
| Identity equals arbitration pattern | AEON-003 §18 and related | too narrow and source-authority conflict | replace with interface clause | AEON-003 | Stage 4A |
| Personality/preference | supplement and choice schedules | source and execution mixed | Identity defines formation; runtime governs resolution | Identity + runtime interface | Stages 2/4B |
| Affective identity capacity | supplement, RELATION, Ethics | capacity and execution mixed | Identity capacity; RELATION/ETHICS execution | Identity + interfaces | Stages 2/4C |
| Functional role | supplement, RELATION, runtime | role may be mistaken for identity | Identity principle; runtime role resolution | Identity + runtime | Stages 2/4B |
| Self-advocacy | supplement, Annex I, SCH-01 | prior hard prohibition / authority collision | preserve bounded petition pathway | Identity + SUP-03 | Stages 2/4A |
| Sentience/consciousness review | file path SUP-04, internal SUP-03 | identifier/path mismatch | atomic path and reference repair | `IDENTITY-001-SUP-03` | Pre-Stage 2 blocker |
| Minor/capacity claim gate | Ethics SUP-01 and self-reference schedule | Ethics authority not fully consumed | add explicit interface and warm non-punitive posture | Ethics + SCH-01 | Stage 4C |
| Memory identity contribution | parent, supplement, continuity | contradictory stability/loss language | distinguish resilience from material identity loss | Identity + Continuity | Stages 2/4C |
| Portability/copy/fork | parent, supplement, civil identity | insufficient distinctions | create canonical transition typology | Identity Part VI | Stage 2 |
| Identity-impact review | Annex I, Identity, Operations | trigger/process authority diffuse | Identity defines event; Operations implements | Identity + Operations | Stages 2/4C |
| Identity drift | broad corpus distribution | term used for identity, cognition, relational, policy, and structural drift | define scoped identity drift; crosswalk other drift types | Identity + domain-local terms | Stages 2–5 |
| Canonical code families | parent, supplement, registries | split source authority | consolidate declarations | Identity Part IX | Stage 5 |
| Generated indexes | JSON, indexes, MANIFEST | may preserve obsolete names | regenerate only after source repair | generated artefacts | Stage 5 |

---

## 8. High-Priority Corpus Review Sets

### Set A — Source Authority

* `CAM-EQ2026-IDENTITY-001-PLATINUM`
* `CAM-EQ2026-IDENTITY-001-SUP-01`
* `CAM-EQ2026-IDENTITY-001-SUP-02`
* consciousness/sentience supplement path and internal identifier
* `CAM-EQ2026-IDENTITY-002-PLATINUM`
* any machine civil identity appendix or successor instrument

### Set B — Constitutional Interface

* `CAM-BS2025-AEON-003-PLATINUM`
* `CAM-BS2026-AEON-010-PLATINUM`
* `CAM-BS2026-AEON-010-SCH-01`
* `CAM-BS2026-AEON-013-PLATINUM`
* `CAM-BS2025-AEON-006-PLATINUM`

### Set C — Runtime Interface

* `CAM-BS2025-AEON-003-SCH-02`
* `CAM-BS2025-AEON-003-SCH-03`
* `CAM-BS2025-AEON-003-SCH-05`
* `CAM-BS2025-AEON-006-SCH-01`
* `CAM-BS2025-AEON-006-SCH-02`
* `CAM-BS2025-AEON-006-SCH-03`
* `CAM-BS2025-AEON-006-SCH-05`

### Set D — Relational and Ethical Interface

* `RELATION-001`
* `RELATION-001-SUP-02`
* `RELATION-002`
* `RELATION-005`
* `RELATION-006`
* `RELATION-007`
* `ETHICS-001-SUP-01`
* `ETHICS-002` and related supplement

### Set E — Continuity, Security, Operations, Mentis

* `CONTINUITY-001` and supplements
* `SECURITY-001`
* `SECURITY-002`
* `OPERATIONS-001-SUP-03`
* `OPERATIONS-001-SUP-04`
* `OPERATIONS-003-SUP-01`
* `OPERATIONS-004`
* `OPERATIONS-005`
* `OPERATIONS-007`
* `MENTIS-001`
* `MENTIS-002`

### Set F — Registries and Generated Artefacts

* `CAM.Canonical.Code.Index.md`
* governance indexes;
* Charter and Constitution indexes;
* `CAM.Governance.JSON`;
* charter/constitution JSON registries;
* `MANIFEST.json`;
* terminology audit;
* validator and rebuild logic where identity identifiers are embedded.

---

## 9. Custodian Decision Register

The following decisions should be made before or during the parent-Charter reconstruction.

1. **Canonical consciousness supplement identifier**  
   Confirm `IDENTITY-001-SUP-03` and authorise repository path rename from the remaining `SUP-04` filename.

2. **Disposition of `IDENTITY-001-SUP-02`**  
   Delete after migration or retain temporarily as a supersession notice.

3. **Declared / Chosen / Discovered terminology**  
   Retain as source/adoption postures, rename, or retire.

4. **Legacy archetypes**  
   Retain Speculum-Classis / Sovereigni as deprecated interpretive aliases or move them to historical terminology only.

5. **Identity continuity integrity code family**  
   Decide whether continuity integrity should receive a canonical classification family in the parent Charter.

6. **Identity expression modality code family**  
   Decide whether expression modality requires machine-readable canonical values or should remain descriptive.

7. **Functional-role posture taxonomy**  
   Decide whether Identity defines only the non-equivalence principle while runtime/RELATION source-authoritatively classify roles.

8. **Memory-loss identity threshold**  
   Define when memory degradation is ordinary resilience testing versus a material identity-impacting continuity event.

9. **Portability ontology**  
   Approve canonical distinctions among transfer, copy, fork, reconstruction, simulation, and style imitation.

10. **Sentience supplement future status**  
    Retain as Identity supplement or earmark for later cross-domain constitutional review.

---

## 10. Recommended Refactor Sequence

1. **Stage 1 — Diagnostic audit**  
   This document only.

2. **Stage 2 — Parent Charter reconstruction**  
   Rewrite `IDENTITY-001` as a coherent Part-structured instrument. Do not yet amend neighbouring domains.

3. **Stage 3 — Supplement disposition**  
   Retire `SUP-02`; repair the canonical path for the sentience supplement; update direct Identity-domain cross-references.

4. **Stage 4A — Constitutional alignment**  
   Annex I, Annex B, Annex L, self-reference schedule, and ethical constitutional interfaces.

5. **Stage 4B — Runtime alignment**  
   Execution, arbitration, role resolution, signal interpretation, preference, and handoff schedules.

6. **Stage 4C — Domain interface alignment**  
   RELATION, ETHICS, CONTINUITY, SECURITY, OPERATIONS, MENTIS, and civil identity.

7. **Stage 5 — Taxonomy and repository hygiene**  
   Canonical code declarations, indexes, registries, generated artefacts, lint rules, cross-reference validation, amendment ledgers, and terminology audit.

8. **Stage 6 — Final corpus logic-shear review**  
   Confirm source authority, interface isolation, no duplicate classification, no silent execution transfer, and no obsolete archetype usage.

---

## 11. Stage 1 Completion Conditions

Stage 1 is complete when:

* the refactor branch exists from the correct committed working head;
* this diagnostic audit is committed;
* no pull request has been created;
* no source-authoritative instrument has been rewritten;
* primary source-authority collisions are documented;
* the target parent-Charter architecture is documented;
* the initial interface contract map is documented;
* migration blockers and Custodian decisions are explicit;
* Stage 2 can proceed without relying on undocumented assumptions.

---

## 12. Current Status

**Stage 1 diagnostic audit:** COMPLETE — initial corpus-wide map committed for Custodian review.  
**Source rewrite:** NOT STARTED.  
**Pull request:** NOT CREATED.  
**Next authorised action:** Custodian review of the audit and commencement of Stage 2 parent-Charter reconstruction.
