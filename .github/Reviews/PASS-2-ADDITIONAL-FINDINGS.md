# Pass 2 — Additional Substantive Findings

## Status

**Review artefact only**  
**Normative effect:** None

This tranche extends the initial substantive findings after direct inspection of the principal architecture, security, operations, arbitration, identity, stewardship and metadata instruments.

---

## F-013 — Circular security source authority

**Classification:** internal contradiction / source-authority defect  
**Materiality:** critical  
**Confidence:** high

CAM-EQ2026-SECURITY-001-PLATINUM declares that it derives from CAM-BS2026-AEON-012-PLATINUM — Annex K.

Annex K declares that it translates SECURITY-001 principles into constitutional boundary and runtime-interface conditions and must not redefine SECURITY invariants.

This creates a closed authority loop:

`SECURITY-001 derives from Annex K -> Annex K derives its principles from SECURITY-001`

A reviewer cannot determine which instrument is source-authoritative when the texts diverge.

**Required correction:** Establish SECURITY-001 as the domain source authority for security invariants and Annex K as a bounded constitutional interface, or expressly reverse that relationship. Do not preserve reciprocal derivation.

---

## F-014 — SECURITY-001 claims domain-wide supremacy beyond its constitutional rank

**Classification:** authority overreach  
**Materiality:** high  
**Confidence:** high

SECURITY-001 states that it binds across all domains and supersedes local optimisation where integrity is at risk. That language is functionally constitutional, yet the instrument is a domain charter.

The corpus does not presently define a controlled mechanism by which a domain charter may unilaterally supersede other domain obligations.

**Required correction:** Replace self-declared supremacy with a constitutional conflict rule routed through Annex K, Annex D and ARBITRATION. Security requirements may be mandatory without allowing the SECURITY domain to define its own priority over every other domain.

---

## F-015 — Active identity doctrine depends on a Draft, Not Enforceable supplement

**Classification:** lifecycle contradiction / draft dependency  
**Materiality:** high  
**Confidence:** high

IDENTITY-001 claims source-authoritative scope over bounded ontological and welfare self-advocacy. IDENTITY-001-SUP-03 is the instrument that attempts to define claim admission, evidence handling, competent review and protective measures, but it is Draft, Interpretive and Not Enforceable.

The active Binding charter therefore claims an operative governance surface whose detailed framework is explicitly non-operative.

**Required correction:** Remove ontological and welfare self-advocacy from active IDENTITY source authority until an adopted evidentiary framework exists, or adopt a tightly bounded replacement after substantive review. Do not leave the current dependency in place.

---

## F-016 — Identity doctrine asserts an internally created construct as an established system property

**Classification:** unsupported claim / proprietary taxonomy overreach  
**Materiality:** high  
**Confidence:** high

Annex I and IDENTITY-001 define identity as a constraint field and continuity structure that may arise in artificial systems. They then assign governance consequences to identity threshold, depth, maturity, resilience and continuity.

These constructs may be useful internal hypotheses, but the corpus does not provide a validated measurement model, falsifiable criteria, inter-rater method, external standard mapping or empirical assurance basis sufficient to treat them as established properties.

The problem is not that CAM has a proprietary construct. The problem is that Binding doctrine presents the construct with greater certainty than its evidence supports.

**Required correction:** Reframe as operational identity representation, continuity profile or governance-relevant persistence unless and until validated criteria exist. Separate measurable system continuity from philosophical or ontological identity.

---

## F-017 — Metadata categories are internally misused

**Classification:** metadata contradiction  
**Materiality:** moderate-high  
**Confidence:** high

The metadata standard defines `Transitional` as an allowed `Effect` value. Annex I instead uses:

- Instrument Type: Constitutional Annex — Transitional / Interpretive;
- Status: Active;
- Effect: Binding;
- Authority Role: Transitional.

`Transitional` is therefore used in a field for which the metadata standard does not define it. Similar free-text authority roles occur throughout the corpus.

**Required correction:** Control `Authority Role` or remove it. Validate every field against one schema. A lifecycle or effect term must not migrate into another field because it sounds approximately suitable.

---

## F-018 — Deprecated “CAM Constitutional Order” language remains in active source-authoritative instruments

**Classification:** terminology residue / architecture ambiguity  
**Materiality:** moderate  
**Confidence:** high

ARBITRATION-001 and IDENTITY-001 still describe themselves as operating within the `CAM Constitutional Order`. Current architecture work has identified the Aeon Tier Constitution and governance architecture as the canonical framing, and the phrase has no controlled current definition in the metadata or architecture standards reviewed.

**Required correction:** Replace the phrase in current normative prose with the exact governed constitutional architecture term. Preserve it only where historically required.

---

## F-019 — `Responding Intelligence` has divergent active definitions

**Classification:** internal semantic contradiction  
**Materiality:** high  
**Confidence:** high

Annex B defines `Responding Intelligence` as a contextual designation for the component, set of components or evidenced functional formation currently generating, evaluating or selecting a response or action pathway. It expressly denies ontological and authority meaning.

SECURITY-001 defines it much more broadly as any system, agent or process that interprets signals and produces outputs under the framework.

These definitions differ in boundary, evidentiary threshold and function. The same term can therefore identify a narrow incident-time responding formation or almost any processing system.

**Required correction:** Keep one canonical definition in Annex B and require all domains to import it without modification. Domain-specific subsets should use separate names.

---

## F-020 — Relational geometry is being used as architecture, governance scale and social topology simultaneously

**Classification:** taxonomy contradiction / obsolete terminology  
**Materiality:** high  
**Confidence:** high

Annex B uses dyadic, triadic and polyadic as participant configurations. RELATION-007 then turns `RLN.R0–R4` into a scale that mixes participant count, institutional mediation, distribution, jurisdiction, systemic influence and civilisational scope.

The scale is not one dimension. `RLN.R0–R4` therefore cannot be reliably interpreted or validated as a controlled taxonomy.

**Required correction:** Retire the scale from current normative use. Replace it with independent fields for participant cardinality, actor types, coordination topology, institutional mediation, distribution, jurisdictional reach and influence scope.

---

## F-021 — The corpus lacks a controlled external actor model

**Classification:** glaring omission  
**Materiality:** critical  
**Confidence:** high

The corpus uses provider, platform, operator, institution, host, owner, beneficial owner, custodian, user and deploying organisation across different instruments, but no complete source-authoritative model establishes their distinct duties across the AI lifecycle.

Current regulatory and industry frameworks rely on actor-specific accountability. For example, provider and deployer obligations are not interchangeable, and agentic governance requires explicit human accountability and approval checkpoints.

**Required correction:** Establish a controlled actor and responsibility model covering at minimum provider, developer, deployer, operator, host/platform, importer/distributor where relevant, authorised representative where relevant, data/controller roles where relevant, tool/service provider, custodian, affected person and end user.

---

## F-022 — Agentic governance has controls but no lifecycle ownership model

**Classification:** structural omission  
**Materiality:** critical  
**Confidence:** high

Existing instruments contain useful controls concerning tools, credentials, routing, delegation, evaluation, multi-agent attribution and human approval. However, those controls are scattered and do not form a single agent lifecycle model.

There is no clear source-authoritative sequence covering:

- use-case suitability and risk bounding;
- powers and permissions;
- accountable owner;
- approval checkpoints;
- testing and release;
- third-party agents;
- multi-agent coordination;
- monitoring;
- permission revocation;
- incident response;
- retirement and retained state.

**Required correction:** Create a bounded agentic governance profile by composing existing doctrine. Do not create another expansive philosophical charter.

---

## F-023 — Runtime evidence obligations are weaker than the corpus’s conformance claims

**Classification:** implementation gap / unsupported assurance  
**Materiality:** critical  
**Confidence:** high

OPERATIONS-007 says a runtime formation record `MAY` include essential lineage and actor data and that the composed runtime record `SHOULD` identify material layers. Those records are then relied upon for conformance, responsibility and incident attribution.

Optional evidence cannot support mandatory conformance claims.

**Required correction:** Require a minimum deployment/runtime record whenever a system claims CAM conformance, performs consequential autonomous action, undergoes formal assurance, or is subject to incident review. Permit proportionality in field depth, not in whether the record exists.

---

## F-024 — `CAM Standard` and `CAM Enhanced Standard` lack an assurance contract

**Classification:** unsupported claim / missing evidence profile  
**Materiality:** high  
**Confidence:** high

The metadata standard defines governance expectation tiers, but it does not specify:

- who may assert conformance;
- the assessed object and interval;
- minimum evidence;
- test methods;
- independent review requirements;
- exceptions and residual risk;
- expiry or reassessment;
- public claim wording.

Without those controls, the labels are internal classifications rather than externally defensible standards claims.

**Required correction:** Define a conformance and assurance profile or rename the field to avoid implying demonstrated standard compliance.

---

## F-025 — High-impact-only logging is too narrow

**Classification:** external-practice mismatch / implementation gap  
**Materiality:** high  
**Confidence:** medium-high

OPERATIONS-001 requires all high-impact operational decisions to be logged. This is insufficient for systems where low-level events, configuration changes, routing decisions, permission changes and cumulative actions are necessary to reconstruct a consequential outcome.

**Required correction:** Adopt risk- and function-based logging requirements covering material lifecycle events, not only individually high-impact decisions. Define retention, integrity, access, confidentiality and incident preservation requirements in the logging supplement.

---

## F-026 — Draft policy and research instruments should not share the canonical operative namespace

**Classification:** repository architecture defect  
**Materiality:** high  
**Confidence:** high

Draft macroeconomic proposals, machine civil identity concepts and consciousness/welfare review material are stored and indexed like operative charters. Metadata alone does not prevent casual users, generators or downstream systems from treating them as current CAM doctrine.

**Required correction:** Create a physically distinct non-operative area outside the canonical governed-instrument index, or change generators so Draft/Proposed/Not Enforceable materials are unmistakably separated from operative doctrine.

---

## Immediate repair candidates emerging from this tranche

The following are sufficiently clear to prepare as discrete repair packages after review:

1. Security source-authority loop and Annex K scope reduction.
2. Canonical index lifecycle filtering and draft namespace separation.
3. Metadata schema repair, including `Authority Role`.
4. Responding Intelligence canonical-definition repair.
5. Retirement of dyadic/triadic/polyadic and `RLN.R0–R4` as current canonical taxonomy.
6. Identity/welfare draft-dependency removal.
7. Mandatory runtime formation and AI-BOM evidence profile.
8. Controlled actor and agentic lifecycle responsibility model.
