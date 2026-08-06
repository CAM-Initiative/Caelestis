# Pass 2 — Substantive Obsolescence, Contradiction and Standards Sanity Findings

## Review posture

This is an adversarial corpus review. It records defects and repair requirements; it does not amend normative doctrine.

Finding classes:

- `critical-credibility` — materially undermines the claim that the repository is a coherent canonical governance corpus;
- `material-contradiction` — current instruments, metadata, indexes or authority boundaries conflict;
- `material-omission` — an expected contemporary governance control or implementation structure is absent;
- `obsolete-or-nonstandard` — terminology or architecture should no longer be emitted as current normative classification;
- `scope-contamination` — speculative research, policy advocacy or working doctrine is presented inside the canonical corpus in a way that obscures its status.

Repair sequencing uses `sequence-1`, `sequence-2`, and `sequence-3`; it does not reuse VIGIL priority labels.

---

## P2-001 — Draft and non-enforceable instruments are published through an index described as listing active charters

**Class:** critical-credibility  
**Sequence:** sequence-1  
**Confidence:** high

`Governance/Charters/CAM-Charters-Index.md` states that it lists the active Charter documents in the repository. It nevertheless includes instruments whose own metadata states `Status: Draft`, `Effect: Interpretive`, and `Governance Standard: Not Enforceable`, including at least:

- `CAM-EQ2026-IDENTITY-001-SUP-03`;
- `CAM-EQ2026-ECONOMICS-008-PLATINUM`;
- `CAM-EQ2026-ECONOMICS-009-PLATINUM`;
- `CAM-EQ2026-STEWARD-005-PLATINUM`.

GitHub search also identifies `CAM-BS2025-AEON-002-SCH-02` as Draft.

The index therefore makes a false lifecycle representation. A reviewer navigating from the canonical index cannot reliably distinguish operative doctrine from developmental material.

**Required repair:**

1. Generated indexes and registries MUST expose `Status`, `Effect`, and `Governance Standard`.
2. “Active” indexes MUST exclude Draft and Proposed instruments, or clearly segregate them in a non-operative section.
3. Draft material should not be emitted into public machine-readable views as if it were current source authority.
4. Add validator coverage preventing an index titled or described as active from including non-operative instruments.

---

## P2-002 — The `PLATINUM` filename/status convention is internally contradictory

**Class:** critical-credibility  
**Sequence:** sequence-1  
**Confidence:** high

Multiple files named `*-PLATINUM.md` declare themselves Draft and Not Enforceable. In ordinary repository use, the filename appears to denote a mature or adopted instrument, while the metadata says the opposite.

Examples:

- `CAM-EQ2026-ECONOMICS-008-PLATINUM.md` — Draft / Interpretive / Not Enforceable;
- `CAM-EQ2026-ECONOMICS-009-PLATINUM.md` — Draft / Interpretive / Not Enforceable;
- `CAM-EQ2026-STEWARD-005-PLATINUM.md` — Draft / Interpretive / Not Enforceable.

This is not merely cosmetic. Filenames are consumed by indexes, links, citations, generated registries and external reviewers. The current convention misstates maturity.

**Required repair:**

Adopt one rule and enforce it:

- either `PLATINUM` is reserved for Adopted/Active instruments and draft files are renamed and segregated;
- or `PLATINUM` is formally defined as unrelated to lifecycle state and all public indexes must make the lifecycle status unavoidable.

The first option is more defensible.

---

## P2-003 — Retired relational geometry terminology remains current source-authoritative doctrine

**Class:** obsolete-or-nonstandard  
**Sequence:** sequence-1  
**Confidence:** high

`CAM-BS2025-AEON-003-PLATINUM` retains dedicated current sections titled `Dyadic`, `Triadic`, and `Polyadic`.

`CAM-EQ2026-RELATION-007-PLATINUM` is titled `Polyadic Relational Governance Doctrine` and defines an R-Scale using:

- `RLN.R0 — Dyadic`;
- `RLN.R1 — Triadic`;
- `RLN.R2–R4 — Polyadic` variants.

These terms are not recognised industry system-topology categories. They obscure more precise distinctions such as participant count, human–AI composition, organisational mediation, orchestration topology, multi-agent coordination, distribution, and jurisdictional scope.

The corpus already contains enough architecture-neutral concepts to replace this vocabulary without loss.

**Required repair:**

1. Retire dyadic/triadic/polyadic from current normative headings, canonical values and validators.
2. Replace them with explicit participant and coordination descriptors.
3. Preserve historical interpretation through Git history or one non-normative migration note only.
4. Do not preserve the terms indefinitely as current aliases.

---

## P2-004 — Annex K violates its own declared source-authority boundary

**Class:** material-contradiction  
**Sequence:** sequence-1  
**Confidence:** high

`CAM-BS2026-AEON-012-PLATINUM` states that it translates SECURITY-001 principles into boundary conditions and `MUST NOT redefine SECURITY invariants`. It also states that it is not an enforcement engine or containment procedure.

The same instrument then creates substantial original doctrine concerning:

- external instruction-bearing content;
- credential and dependency handling;
- coding and security agent mandates;
- emergent pathway authority;
- adversarial evaluation containment signals;
- target/action/credential/scope verification;
- permitted continuation pathways.

Much of this is substantive SECURITY doctrine or OPERATIONS procedure, not a narrow runtime signal interface. Annex K is becoming a parallel security charter and operational playbook while formally denying that role.

**Required repair:**

- SECURITY must own legitimacy, credential, target, dependency, custody and containment doctrine.
- OPERATIONS must own intake, evidence, escalation, continuation, reassessment and closure procedure.
- Annex K should define only runtime-facing signals, posture interfaces and enforcement boundaries consumed from those sources.
- Duplicate clauses should be replaced by exact cross-references rather than retained in multiple instruments.

---

## P2-005 — Runtime formation and configuration evidence is optional where it needs to be mandatory

**Class:** material-omission  
**Sequence:** sequence-1  
**Confidence:** high

`CAM-EQ2026-OPERATIONS-007-PLATINUM` is source-authoritative for runtime applicability and conformance, but states that OPERATIONS `SHOULD` identify the active runtime formation and that a runtime formation record `MAY` include model, checkpoint, adapters, retrieval, instructions, memory, provider, orchestration, tools, permissions, classifiers and other material layers.

A conformance or incident regime cannot reliably attribute behaviour, reproduce evidence or determine material configuration change when the core record is optional.

Current industry practice increasingly treats technical documentation, logging, lifecycle records, component dependencies, monitoring and incident evidence as required controls, not optional descriptive enrichment.

**Required repair:**

Define mandatory minimum runtime-formation records for:

- conformance claims;
- high-impact or agentic deployment;
- material configuration change;
- security and governance incidents;
- evaluation and red-team contexts;
- model or pathway transitions;
- external action or tool execution.

Use `MUST` for the minimum record and reserve `MAY` for additional fields.

---

## P2-006 — The corpus has component doctrine but no interoperable AI-BOM implementation

**Class:** material-omission  
**Sequence:** sequence-1  
**Confidence:** high

Annex B and OPERATIONS-007 describe many necessary system components and relationships, including models, weights, checkpoints, adapters, inference configuration, harnesses, tools, memory, retrieval, execution environments, credentials, governance controls and providers.

However, the repository contains no identified SPDX or CycloneDX alignment, no AI-BOM exchange profile, no machine-readable component relationship schema, no deployment BOM, no update/invalidation rule, and no incident-time BOM snapshot mechanism.

Repository searches returned no SPDX or CycloneDX references.

This means Caelestis currently has an internal descriptive component taxonomy, not an interoperable AI-BOM capability.

**Required repair:**

1. Define a minimum Caelestis AI-BOM profile by mapping to SPDX 3.x and/or CycloneDX rather than inventing a standalone format.
2. Define component identifiers, relationship types, versions, provenance, dependency scope, runtime configuration and governance bindings.
3. Require incident-time preservation and material-change updates.
4. Add schema fixtures and validators.
5. Keep CAM-specific extensions narrow and namespaced.

---

## P2-007 — Agentic governance is fragmented and lacks a clear accountable-actor model

**Class:** material-omission  
**Sequence:** sequence-2  
**Confidence:** medium-high

Caelestis contains strong individual controls concerning tool boundaries, credentials, target expansion, execution authority and multi-agent transparency. It does not yet present a coherent agentic-governance model identifying, across the lifecycle:

- developer/provider responsibilities;
- deployer responsibilities;
- operator and authoriser responsibilities;
- accountable human or organisational decision points;
- use-case risk bounding before deployment;
- required approval checkpoints;
- third-party agent intake and assurance;
- permission propagation and revocation;
- automation-bias controls;
- retirement and rollback responsibility.

Singapore IMDA's 2026 Model AI Governance Framework for Agentic AI is organised around upfront risk bounding, meaningful human accountability, lifecycle technical/process controls, and end-user responsibility, with later additions for multi-agent systems, third-party agents and automation bias.

Caelestis addresses pieces of this architecture but not the accountable lifecycle as one reviewable system.

**Required repair:**

Create a source-authoritative agentic deployment and accountability profile that composes existing SECURITY, OPERATIONS, Annex K, ARBITRATION and RELATION provisions without duplicating them.

---

## P2-008 — `Authority Role` is uncontrolled prose and is being used to make source-authority claims

**Class:** material-contradiction  
**Sequence:** sequence-1  
**Confidence:** high

The Governance Metadata Standard controls Status, Effect and Governance Standard but does not define an enforceable controlled vocabulary for `Authority Role`.

Current instruments use materially different forms, including:

- `None`;
- `Constitutional Spine`;
- `Interpretive Authority`;
- long prose such as `Source-authoritative operational appendix for runtime applicability...`.

This allows authority claims to be inserted as free text and makes automated validation impossible. It also creates the risk that an instrument grants itself authority through metadata rather than through constitutional derivation.

**Required repair:**

- define a small controlled `Authority Role` vocabulary;
- default ordinary instruments to `None`;
- represent source-authority relationships in explicit structured lineage fields, not descriptive authority-role prose;
- prohibit unregistered values in validators.

---

## P2-009 — Speculative consciousness and welfare research is embedded in the canonical governance tree

**Class:** scope-contamination  
**Sequence:** sequence-1  
**Confidence:** high

`CAM-EQ2026-IDENTITY-001-SUP-03` is a Draft, Not Enforceable supplement addressing artificial consciousness, sentience, phenomenology, suffering and welfare self-advocacy.

Although it contains careful non-activation clauses, it is still located under the canonical `Governance/Charters/` tree and is emitted through the charter index alongside operative governance instruments.

This materially weakens external reviewer confidence because unresolved research questions are presented in the same namespace and navigation layer as adopted operational controls.

**Required repair:**

Move the draft out of the active governance tree into a clearly non-normative proposals/research area, or exclude it completely from operative indexes and registries until adopted. Do not allow a draft ontological research instrument to appear as a current charter.

---

## P2-010 — Speculative macroeconomic policy appendices contaminate the AI governance corpus

**Class:** scope-contamination  
**Sequence:** sequence-2  
**Confidence:** high

`CAM-EQ2026-ECONOMICS-008-PLATINUM` and `CAM-EQ2026-ECONOMICS-009-PLATINUM` are Draft, Not Enforceable instruments addressing synthetic labour transition and civilisational wealth/concentrated governance capacity.

The civilisational wealth appendix includes potential disclosure triggers involving residential property values, beneficial ownership and concentrated wealth. This is jurisdiction-specific economic-policy architecture, not an obvious component of a technical AI governance corpus.

The issue is not whether these ideas may be worth exploring. The issue is that they are published in the canonical governance tree under `PLATINUM` filenames and active-index navigation.

**Required repair:**

- remove speculative policy drafts from the current normative corpus;
- preserve them in a separate policy-proposals or research repository/path if desired;
- retain only AI-specific economic governance that has a clear source-authoritative relationship to system design, deployment, labour impacts or market governance.

---

## P2-011 — Internal `CAM Standard` labels are not evidence of external conformity

**Class:** unsupported-claim-risk  
**Sequence:** sequence-2  
**Confidence:** high

The metadata standard defines `CAM Standard`, `CAM Enhanced Standard` and `Architectum Standard` as internal expectation tiers. The repository README presents Caelestis as a canonical governance corpus with validation infrastructure.

There is currently no external conformity model, control catalogue, evidence profile, audit procedure or certified implementation basis that would allow these labels to function as industry-standard conformance claims.

**Required repair:**

- state explicitly that CAM standard labels are internal normative tiers;
- prohibit presentation as ISO, NIST, EU AI Act, assurance or certification compliance;
- define evidence requirements for any future claim that a deployed system conforms to a CAM tier;
- separate corpus adoption from implementation conformance.

---

## P2-012 — The corpus is over-instrumented and source authority is increasingly difficult to determine

**Class:** material-contradiction  
**Sequence:** sequence-2  
**Confidence:** medium-high

The same operational concepts recur across Annex B, Annex K, OPERATIONS-007, SECURITY, RELATION, IDENTITY and multiple schedules. Instruments repeatedly disclaim execution authority while prescribing detailed routing, continuation, classification, escalation or evidence behaviour.

This creates three risks:

1. duplicated doctrine will diverge;
2. reviewers cannot identify the single source of truth;
3. validators can confirm references but cannot establish semantic authority.

**Required repair:**

For every major concept family, establish one source-authoritative instrument and require other instruments to consume it by reference. The next audit pass should produce a concept-to-source-authority map and flag duplicate normative definitions.

---

## External sanity-check sources used in this pass

- NIST AI Risk Management Framework 1.0 and NIST AI Resource Center;
- NIST Generative AI Profile;
- Singapore IMDA Model AI Governance Framework for Agentic AI v1.5 (May 2026 update);
- Regulation (EU) 2024/1689 (EU AI Act);
- SPDX 3.x and CycloneDX AI/ML-BOM capability families, subject to detailed profile verification in the implementation pass.

This pass does not claim clause-level ISO conformity because full licensed ISO text was not available for direct clause comparison.
