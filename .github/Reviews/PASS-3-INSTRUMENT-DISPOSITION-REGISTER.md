# Pass 3 — Instrument Disposition Register

**Date:** 2026-08-06  
**Branch:** `agent/corpus-industry-standards-normalisation`  
**Normative effect:** None. This is a review and repair-design record.

## Decision rules

Each instrument is assigned one of: retain unchanged; retain with bounded amendment; consolidate; move to drafts; deprecate; retire; replace; or investigate.

Draft instruments are not part of the operative corpus and must not appear in operative indexes, registries, canonical-code outputs or conformance claims.

## Approved structural dispositions

| Instrument | Current defect | Disposition | Destination / repair |
|---|---|---|---|
| `CAM-EQ2026-ECONOMICS-008-PLATINUM` | Draft, Not Enforceable, but presented in operative Charter namespace with `PLATINUM` designation | Move to drafts | `Governance/Drafts/Charters/CAM-EQ2026-ECONOMICS-008.md`; remove from operative registries; retain as policy-development material |
| `CAM-EQ2026-ECONOMICS-009-PLATINUM` | Draft macroeconomic policy proposal presented as an operative Charter appendix | Move to drafts | `Governance/Drafts/Charters/CAM-EQ2026-ECONOMICS-009.md`; remove from operative registries |
| `CAM-EQ2026-STEWARD-005-PLATINUM` | Draft machine civil-identity doctrine presented in operative namespace | Move to drafts | `Governance/Drafts/Charters/CAM-EQ2026-STEWARD-005.md`; retain only as developmental lifecycle-policy material |
| `CAM-EQ2026-IDENTITY-001-SUP-03` | Draft consciousness, sentience and welfare process contaminates normal Charter navigation | Move to drafts | `Governance/Drafts/Charters/CAM-EQ2026-IDENTITY-001-SUP-03.md`; remove active-domain dependencies |
| `CAM-BS2025-AEON-002-SCH-02` | Draft civilisational-wealth runtime schedule placed in Constitution namespace | Move to drafts | `Governance/Drafts/Constitution/CAM-BS2025-AEON-002-SCH-02.md`; no runtime or constitutional effect |

## Foundational instruments requiring repair

| Instrument / surface | Disposition | Required repair |
|---|---|---|
| `CAM-GOVERNANCE-METADATA-STANDARD` | Retain with major amendment | Control `Authority Role`; define valid metadata combinations; prohibit Draft + operative designation; define registry inclusion rules |
| `CAM-BS2025-AEON-003-PLATINUM` — Annex B | Retain with bounded amendment | Become canonical structural-definition source; retire cardinality labels; define system/component/runtime terms once; bind AI-BOM and incident-time evidence requirements |
| `CAM-EQ2026-OPERATIONS-007-PLATINUM` | Retain with major amendment | Make runtime-formation evidence mandatory where conformance, incidents or responsibility are asserted; link to interoperable AI-BOM profile |
| `CAM-EQ2026-SECURITY-001-PLATINUM` | Retain with major amendment | Remove self-declared cross-domain supremacy; become source authority for security invariants; correct derivation relationship |
| `CAM-BS2026-AEON-012-PLATINUM` — Annex K | Retain with major amendment | Reduce to constitutional boundary conditions and interfaces; move procedures and detailed security controls to SECURITY or OPERATIONS |
| `CAM-EQ2026-RELATION-007-PLATINUM` | Replace taxonomy while retaining safeguards | Retire `RLN.R0–R4`; separate participant topology, coordination, institutional mediation, distribution and impact scope |
| `CAM-EQ2026-IDENTITY-001-PLATINUM` | Retain with bounded amendment | Remove operative dependency on draft welfare doctrine; distinguish governance identity records from unvalidated identity-threshold claims |
| `CAM-BS2026-AEON-010-PLATINUM` — Annex I | Retain with bounded amendment | Narrow evidentiary claims; remove or qualify constructs lacking measurable criteria; preserve identity–ontology firewall |
| Charter/Constitution/global index generators | Replace inclusion rule | Index only adopted or active governed instruments; expose status/effect; exclude `Governance/Drafts/**` |
| Canonical-code and terminology generators | Amend | Exclude draft declarations from current canonical outputs; optionally emit a separately labelled draft inventory |

## Canonical definition decisions

The following definitions require a single source of truth, with consumers using cross-references rather than redefinition:

- component;
- model architecture, weights/checkpoint and model instance;
- foundation model or generative core;
- inference configuration;
- operational or agentic harness;
- execution environment;
- governance and assurance stack;
- deployed AI system formation;
- incident-time formation;
- runtime configuration;
- provider, developer, deployer, operator, host, platform, owner, custodian and affected person;
- agent and multi-agent system;
- conformance and assurance claim;
- identity and continuity.

Annex B should own technical system-boundary definitions. The metadata standard should own metadata vocabulary. Domain instruments should own only domain-specific terms.
