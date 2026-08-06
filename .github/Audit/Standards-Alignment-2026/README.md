# Caelestis Standards-Alignment Audit — 2026-08-06

## Executive determination

Caelestis contains substantial, often sophisticated governance doctrine for composed AI systems, runtime identity, authority separation, incident reconstruction, multi-agent control, identity/continuity distinctions and embodied lifecycle stewardship. The corpus is not ready to claim external standard conformance, certification, legal compliance or deployed-runtime assurance.

The critical gap is now clear: CAM has a strong **AI-ABOM governance requirement** but no versioned, portable, validated implementation profile. The next priority is therefore a controlled AI-ABOM design pass, not another broad ontology rewrite.

The second material gap is a reviewable **entity threshold**. The corpus now separates models, components, harnesses, formations, instances, substrates and continuity layers much better than its retired ontology did. It still does not determine when such a formation is sufficiently individuated to be classed as an entity for scientific or architectural purposes. That question must be researched before new “digital species” or rights-adjacent taxonomy is proposed.

---

## Audit baseline

| Baseline item | Treatment |
| --- | --- |
| PR #104 — AEON-003 composed-architecture refactor | Merged and treated as the adopted corpus baseline. |
| PR #105 — FM-0048 defensive cyber incident assistance | Active stacked branch, inspected as a pending baseline only; not represented as adopted corpus fact. |
| Scope | ISO/IEC 42001, 23894, 38507 and SC 42 orientation; NIST AI RMF/Playbook/GenAI Profile; SPDX and CycloneDX AI-BOM; Singapore agentic governance; bounded EU AI Act themes; embodied lifecycle identity; current Caelestis taxonomy. |
| Exclusions | No normative Caelestis amendments; no new VIGIL records; no automatic VIGIL update; no certification, legal-compliance or provider-runtime-conformance claim. |

---

## Findings at a glance

| Finding | Determination | Repair sequence |
| --- | --- | --- |
| AI-ABOM | Strong concept; no interoperable implementation profile | P0 — implementation profile and validation design |
| Entity taxonomy | Useful distinctions; no entity threshold | P0 — dedicated research before taxonomy drafting |
| Agentic governance | Strong conceptual correspondence | Use Singapore framework as a practical review lens; preserve CAM authority axes |
| Embodied lifecycle | Careful model exists, but STEWARD-005 is Draft | P1 — adoption/locality review, then neutral record profile |
| Retired AEON.CC family | No current exact residual | Maintain prohibition on reintroduction |
| Dyadic/triadic/polyadic language | 231 current textual matches; mechanism valid, terms not externally crosswalkable | P1 — contextual terminology migration |
| ISO treatment | Public abstracts reviewed; full texts not available | Do not make clause-level ISO claims without authorised access |

---

## Artefact map

| File | Role |
| --- | --- |
| `SOURCE-REGISTER.json` | Versioned primary-source register with access-status discipline. |
| `STANDARDS-CROSSWALK.json` | Human and machine-readable concept comparison with explicit non-claim language. |
| `GAP-REGISTER.json` | Repair sequencing; not a VIGIL record or severity register. |
| `CORPUS-CONCEPT-INVENTORY.json` | Deterministic textual evidence inventory generated from current Governance instruments. |
| `TERMINOLOGY-RESIDUAL-SCAN.json` | Deterministic scan for retired families, cardinality vocabulary and singular-arbitration assumptions. |
| `TERMINOLOGY-DISPOSITION.md` | Human review of retained mechanisms and vocabulary disposition. |
| `AI-BOM-READINESS.md` | Readiness assessment and recommended compositional implementation approach. |
| `STAGED-REPAIR-PROGRAMME.md` | Ordered, gated programme for subsequent work packages. |

---

## Rebuilding the deterministic evidence inventories

```bash
python .github/scripts/build_standards_alignment_audit.py
python .github/scripts/build_standards_alignment_audit.py --check
```

The script deliberately records text evidence only. It does not determine alignment, adoption, implementation, legal applicability, conformity or deployed-runtime behaviour; those are human-review determinations in the crosswalk and gap register.

---

## Recommended next work package

Begin **Stage 1: Entity-Threshold Research and Taxonomy Boundary** in a separate research work package, then use its result to constrain—not pre-authorise—any future taxonomy drafting. In parallel, a narrowly technical **AI-ABOM Implementation Profile discovery** can assess SPDX 3 and CycloneDX mappings without amending the corpus.

The terminology migration must follow those two decisions, not precede them: it should preserve the underlying safeguards while replacing terms that cannot bear external scrutiny.
