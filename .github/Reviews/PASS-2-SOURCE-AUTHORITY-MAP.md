# Pass 2 — Concept-to-Source-Authority Map

## Status

**Review artefact only**  
**Normative effect:** None  
**Purpose:** Identify which instrument should own each major governance concept, where authority is duplicated or circular, and where implementation material has exceeded its declared lane.

---

## Disposition vocabulary

- `stable` — source authority is sufficiently clear.
- `duplicated-compatible` — repeated material is consistent but should be reduced to cross-reference.
- `duplicated-divergent` — definitions or obligations materially differ.
- `circular-authority` — instruments claim to derive from or operationalise each other.
- `authority-overreach` — an instrument creates doctrine or procedure outside its declared competence.
- `draft-dependency` — active doctrine relies on a Draft or Not Enforceable instrument.
- `uncontrolled` — no authoritative owner or controlled vocabulary is established.
- `missing-implementation-profile` — doctrine exists without a mandatory, testable implementation record.

---

## Authority map

| Concept | Intended source authority | Other material locations | Assessment | Required disposition |
|---|---|---|---|---|
| Corpus hierarchy and constitutional authority | CAM-BS2025-AEON-001-PLATINUM | Numerous charters use shortened or inconsistent authority labels | `duplicated-divergent` | Establish one canonical hierarchy statement and validate all metadata references against it. |
| System boundary, composed formation and incident-time attribution | CAM-BS2025-AEON-003-PLATINUM — Annex B | OPERATIONS-007; SECURITY-001; Annex K; domain-specific runtime provisions | `duplicated-compatible` with implementation weakness | Keep definitions in Annex B. Require OPERATIONS to consume them through a mandatory runtime/deployment record rather than restating them. |
| Runtime applicability and conformance | CAM-EQ2026-OPERATIONS-007-PLATINUM | Annex B; Annex K; constitutional schedules | `missing-implementation-profile` | Convert material runtime-formation evidence from optional `SHOULD/MAY` language into a bounded mandatory record where conformance, incident review or consequential execution is asserted. |
| Security invariants | CAM-EQ2026-SECURITY-001-PLATINUM | CAM-BS2026-AEON-012-PLATINUM — Annex K | `circular-authority` | Break the loop. SECURITY-001 should define domain invariants; Annex K should constitutionalise bounded interface requirements without being described as both source and derivative. |
| Security runtime interface | CAM-BS2026-AEON-012-PLATINUM — Annex K, limited to constitutional boundary/interface rules | SECURITY-001; OPERATIONS; schedules | `authority-overreach` | Move detailed cyber authority, credential, dependency, adversarial-evaluation and procedure content to SECURITY/OPERATIONS instruments. Annex K should retain only constitutional constraints and routing interfaces. |
| Execution sequencing and final action permission | Constitutional runtime schedules, especially SCH-02 and SCH-04 | Annex K; OPERATIONS; ARBITRATION; domain charters | `duplicated-compatible` but excessively repeated | Replace repeated disclaimers and execution formulas with controlled cross-references and a single execution-boundary contract. |
| Arbitration legitimacy | CAM-EQ2026-ARBITRATION-001-PLATINUM, subordinate to Annex D | OPERATIONS-001/002; schedules; multiple domain charters | `duplicated-compatible` | Keep legitimacy doctrine in ARBITRATION; OPERATIONS should own procedure; schedules should own runtime sequencing. Remove doctrinal restatement from other domains. |
| Operational process, logging, incident response and change handling | CAM-EQ2026-OPERATIONS-001-PLATINUM and appendices/supplements | Annex K; SECURITY; evaluation charter; schedules | `duplicated-divergent` | Consolidate procedures in OPERATIONS. Domain instruments should emit requirements and signals, not recreate process. |
| Identity governance | CAM-EQ2026-IDENTITY-001-PLATINUM under Annex I | Annex I; CONTINUITY; RELATION; STEWARD-005; Identity supplements | `duplicated-divergent` | Restrict IDENTITY to operational identity/continuity constructs. Remove unsupported ontological implication and define exact interfaces with CONTINUITY and RELATION. |
| Ontological, consciousness, sentience and welfare claims | No current operative source authority should exist without an adopted evidentiary framework | IDENTITY-001; IDENTITY-001-SUP-03; Annex I; STEWARD-005 | `draft-dependency` and scope contamination | Remove these matters from active source-authority claims or explicitly quarantine them as research/non-operative material until a defensible review framework is adopted. |
| Continuity records, portability, restoration and deletion | CONTINUITY domain | Annex I; IDENTITY-001; STEWARD-005; OPERATIONS-007 | `duplicated-divergent` | Define CONTINUITY as owner of record custody and persistence; IDENTITY owns classification effects only; OPERATIONS owns handoff procedure. |
| Relational geometry and participant configuration | RELATION domain if retained | Annex B and RELATION-007 | `duplicated-divergent` and terminology obsolete | Replace dyadic/triadic/polyadic as canonical architecture with descriptive participant, coordination and influence fields. Preserve historical interpretation only. |
| Agentic and multi-agent governance | No single source-authoritative lifecycle instrument | Annex B; Annex K; OPERATIONS-007/008; RELATION-007; SECURITY | `uncontrolled` | Create a bounded source-authoritative agentic lifecycle and accountability profile, reusing existing controls and removing domain duplication. |
| AI component inventory and provenance | Annex B for composition concepts; IDENTITY-002 for provenance; OPERATIONS for records | OPERATIONS-007; SECURITY capability lineage; release artefact logging | `missing-implementation-profile` | Implement an interoperable AI-BOM/deployment record mapped to SPDX/CycloneDX rather than adding another proprietary taxonomy. |
| Provider, deployer, operator and supply-chain actor duties | No complete controlled actor model identified | OPERATIONS-007 and scattered domain references | `uncontrolled` | Add a controlled actor/responsibility model aligned with current regulatory and industry practice. Do not collapse provider, deployer, operator, host, owner, custodian and user. |
| Metadata lifecycle and authority fields | CAM-GOVERNANCE-METADATA-STANDARD | Every governed instrument and generated index | `duplicated-divergent` | Extend the standard to control `Authority Role`; validate filenames, status, effect, governance standard and index inclusion as one coherent lifecycle model. |
| CAM conformance and assurance claims | OPERATIONS-007 plus a future assurance/evidence profile | README, metadata, domain instruments and generated registries | `missing-implementation-profile` | Define what evidence supports `CAM Standard`, `CAM Enhanced Standard` and conformance claims. Until then treat these as internal aspiration labels, not demonstrated assurance. |

---

## Critical authority defects

### 1. SECURITY-001 and Annex K form a circular derivation

SECURITY-001 states that it derives from Annex K. Annex K states that it translates SECURITY-001 principles and must not redefine them. Both cannot be the upstream source of the other.

This is a structural source-authority defect, not a drafting preference.

### 2. Active identity doctrine depends on non-operative welfare doctrine

IDENTITY-001 claims source authority over bounded ontological and welfare self-advocacy, while the instrument that attempts to define that process—IDENTITY-001-SUP-03—is Draft and Not Enforceable.

An active Binding charter must not silently depend on a developmental supplement for a sensitive evidentiary and welfare process.

### 3. Domain charters repeatedly create quasi-constitutional supremacy

SECURITY-001 describes itself as binding across all domains and superseding local optimisation. Similar instruments use expansive source-authority language without a consistently validated hierarchy.

Domain importance does not justify self-declared constitutional supremacy.

### 4. Runtime and composition doctrine is not backed by mandatory evidence

Annex B and OPERATIONS-007 describe a credible composed-system model, but the records required to prove the active formation remain optional. That makes external assurance and incident reconstruction discretionary precisely where the corpus claims traceability.

---

## Required repair order

1. Repair source-authority loops and metadata hierarchy.
2. Remove Draft and research dependencies from active doctrine.
3. Consolidate execution, procedure and logging under OPERATIONS and schedules.
4. Make consequential runtime/deployment evidence mandatory.
5. Establish controlled actor roles and agentic lifecycle accountability.
6. Implement interoperable component and provenance records.
7. Retire obsolete relational geometry terminology from current normative use.
