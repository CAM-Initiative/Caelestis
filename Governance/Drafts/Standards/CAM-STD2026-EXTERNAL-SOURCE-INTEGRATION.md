# CAM-STD2026-EXTERNAL-SOURCE-INTEGRATION — External Source Integration and Operationalisation Standard

> **DRAFT — NON-OPERATIVE**
> This instrument is retained for developmental review only. It is not source-authoritative, does not carry a Platinum designation or binding seal, and must not be used to establish current CAM conformance, duties, definitions, procedures or authority.

**Instrument Type:** Governance Standard
**Constitutional Authority:** CAM-BS2025-AEON-001-PLATINUM §13.10 — External Source Integration and Operationalisation Principle
**Status:** Draft
**Effect:** Interpretive
**Governance Standard:** Not Enforceable
**Review State:** Under Review
**Authority Role:** No Independent Authority
**Source Authority:** Non-Operative Draft
**Purpose:** Proposes a controlled, evidence-backed method for classifying external sources, mapping their concepts into canonical CAM doctrine, and recording CAM operational extensions without overstating external authority or reproducing external instruments.

---

## 1. Draft Purpose and Boundary

This draft develops the subordinate implementation contemplated by CAM-BS2025-AEON-001-PLATINUM §13.10. It proposes a single external-source integration process:

> external source → source posture → concept extraction → CAM semantic mapping → operational representation → evidence determination → governance consequence

It does not itself adopt source classifications, mappings, code families, schemas, implementation requirements, or conformance claims. Until reviewed adoption, operative source authority remains with the relevant constitutional, annex, charter, standard, schedule, or profile instrument.

This draft does not reproduce legislation, standards, frameworks, guidance, or research as an alternative corpus. It defines the information CAM needs to explain its own handling of those sources.

---

## 2. Proposed Source-Posture Model

The model separates independent characteristics that must not be collapsed into one authority label.

| Proposed field | Type | Purpose | Illustrative values |
|---|---|---|---|
| `external_source_id` | identifier | Stable record identity | locally assigned identifier |
| `source_class` | enum | What kind of source it is | legislation; regulation; regulatory guidance; international standard; draft standard; technical specification; government framework; industry framework; engineering guidance; research; other |
| `source_status` | set/enum | Publication and lifecycle posture | binding; published; adopted; current; draft; committee draft; FDIS; superseded; withdrawn; historical |
| `authority_scope` | set/enum | Nature of the source's authority | jurisdictional; contractual; standards conformance; advisory; informative; research |
| `jurisdiction_or_scope` | text/relationship | Legal, organisational, or technical applicability boundary | stated jurisdiction or scope |
| `issuer` | relationship | Originating authority or publisher | identified issuer |
| `source_version` | identifier | Exact edition, release, or amendment relied upon | edition/version/date |
| `official_locator` | URI | Authoritative publication location | official locator |
| `supersession_state` | enum | Current relationship to successor material | current; superseded; withdrawn; unknown |
| `review_due` | timestamp/trigger | Reassessment point | review date or source-change trigger |

`source_class`, `source_status`, and `authority_scope` are independent. For example, a published international standard is not legislation; a committee draft is not a published standard; and advisory guidance does not become binding because it is cited by CAM.

The adopted standard should determine final controlled values, including whether `source_status` and `authority_scope` are sets rather than exclusive enums. It must preserve an explicit `unknown` or `unavailable` posture where the evidence does not establish the value.

---

## 3. Proposed Semantic-Mapping Record

Each material use of an external concept should be traceable to a mapping record rather than embedded as unstructured prose across multiple instruments.

| Proposed field | Purpose |
|---|---|
| `external_source_id` | Links to the source-posture record. |
| `external_concept` | Narrow concept, provision, or recognised engineering concern being relied upon. |
| `external_locator` | Clause, section, page, or durable semantic anchor where available. |
| `cam_canonical_concept` | Canonical CAM concept used to represent it. |
| `cam_owner` | Source-authoritative CAM instrument and semantic anchor. |
| `mapping_type` | Proposed relationship such as adoption, adaptation, compatibility, informative reference, or divergence. |
| `governed_object` | AI system, deployment, Runtime state, execution, actor, record, control, or other defined object. |
| `cam_operational_field` | Controlled field, state, identifier, or relationship used where operationally material. |
| `cam_code_family` | CAM family, if an adopted code family is used. |
| `evidence_requirement` | Evidence required to assign, verify, or rely on the mapped state. |
| `runtime_consumer` | Rule, schedule, profile, control, or workflow that consumes the state. |
| `runtime_consequence` | Resulting routing, safeguard, approval, monitoring, logging, reassessment, or constraint consequence. |
| `review_trigger` | Source change, implementation change, incident, elapsed interval, or other reassessment condition. |
| `supersession_state` | Whether the mapping remains current, requires review, or has been superseded. |

The record must distinguish a declared or configured condition from observed, verified, inferred, unknown, or unavailable evidence. A source record, provider statement, model card, AI-BOM, lifecycle record, or configuration baseline does not by itself prove that an effective Runtime state or execution occurred.

---

## 4. Proposed Operationalisation Test

Before an external concept is represented as a CAM operational field, code, or rule, the adopting instrument should answer:

1. What single governance variable does the representation measure or state?
2. Are its values controlled, independently assessable, and dimensionally distinct?
3. What evidence supports assignment, verification, change, uncertainty, or invalidation?
4. Which actor or process may assign or transition the state?
5. What governance, assurance, routing, monitoring, constraint, or Runtime consequence follows?
6. What review trigger applies when the source, deployment, configuration, evidence, or impact changes?

If no material control consequence exists, the concept should be explicitly classified as assessment metadata, provenance, reporting, assurance evidence, or interpretive material rather than presented as a Runtime control variable.

CAM may define a controlled operational representation where an external source supplies a concept or obligation but no executable form. The record must mark that representation as a **CAM operational extension derived from or aligned with the named external concept**. It must not imply that the external source issued the CAM field, code, threshold, or rule.

---

## 5. Proposed Conformance-Language Discipline

The adopted standard should constrain conformance language so that a CAM instrument cannot claim more than the supporting mapping and evidence establish.

At minimum, it should distinguish:

* reference to an external source;
* conceptual alignment;
* mapped compatibility;
* partial implementation;
* adopted CAM obligation; and
* independently evidenced external conformance or certification, where such a status is factually established.

Neither a mapping record nor use of similar terminology should be treated as proof of external conformity, legal compliance, certification, approval, authorship, intent, culpability, or an effective Runtime state.

---

## 6. Proposed Adoption Work

Before this draft is promoted, the adoption work should:

* validate the final vocabulary against accessible primary sources without inventing requirements from licensed or draft material;
* assign one source-authoritative owner for the register, mappings, schema, and validation workflow;
* decide the relationship between source-posture evidence and the Runtime State Profile’s declared/configured/observed/verified/inferred/unknown posture;
* define proportionate minimum evidence by mapping type and governance consequence;
* provide a schema, examples, migration rules, supersession process, and deterministic guards for unambiguous regressions; and
* cross-reference, rather than duplicate, the constitutional principle, Annex B architecture, AI-BOM evidence posture, lifecycle-actor model, Runtime State Profile, and applicable conformance instruments.

---

## 7. Draft Review Questions

1. Should `source_status` and `authority_scope` be multi-valued sets, or should each record use a primary value plus qualifiers?
2. Which mappings require a machine-readable record, and which may remain a cited interpretive note under a proportionality rule?
3. Should a mapping be separately versioned from its source record, or should each source-version change require a new immutable mapping revision?
4. Which adopted instrument should own the source register and schema: a cross-domain governance standard, an Annex B supplementary standard, or another established registry authority?

---

## 8. Non-Operative Closing Note

This draft is a design and review artefact. It does not create a new authority branch, alter the authority of any external source, or require a Runtime implementation until an explicit adoption amendment establishes the relevant source-authoritative standard.
