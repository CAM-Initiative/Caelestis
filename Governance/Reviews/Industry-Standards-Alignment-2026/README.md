# Caelestis Industry Standards Alignment Review — 2026

## Status

**Review phase:** Audit design and evidence collection  
**Normative effect:** None  
**Repository baseline:** `main`  
**Scope:** Caelestis governance corpus alignment and normalisation against current industry standards and recognised governance frameworks

---

## Purpose

This review evaluates whether the current Caelestis corpus is externally legible, structurally aligned, and capable of being crosswalked against relevant AI governance, risk, lifecycle, assurance, agentic-system, AI-BOM, cybersecurity, documentation, and embodied-system standards.

The review is limited to the Caelestis corpus and its implementation architecture.

It does **not** assess or advance:

- the CAM digital-species research paper;
- philosophical entity thresholds;
- scientific taxonomy of synthetic entities;
- consciousness, sentience, personhood, rights, or moral status;
- unrelated research questions imported from other work threads.

Those subjects are explicitly out of scope unless a current Caelestis instrument itself creates a standards-alignment problem that cannot be evaluated without identifying the conflicting terminology.

---

## Review objective

The review must determine:

1. which external requirements or concepts have direct Caelestis coverage;
2. which have equivalent but differently expressed coverage;
3. which are only implicit, dispersed, duplicated, or non-operational;
4. which are genuinely absent;
5. which Caelestis terms or structures are not externally legible and require normalisation;
6. which requirements belong to organisations or regulated actors rather than to the corpus itself;
7. which alignments can be evidenced without claiming certification, legal compliance, or deployed-runtime conformity;
8. which repairs require normative amendments, metadata work, schemas, validators, implementation profiles, or documentation only.

---

## External reference families

The review should cover, using current official or primary sources wherever available:

- ISO/IEC 42001 — AI management systems;
- ISO/IEC 23894 — AI risk management;
- ISO/IEC 38507 — governance implications of AI use by organisations;
- NIST AI RMF, Playbook, and Generative AI Profile;
- Singapore IMDA agentic AI governance guidance;
- SPDX 3 AI and Dataset profiles;
- CycloneDX ML-BOM and related compositional BOM profiles;
- Regulation (EU) 2024/1689 and current official implementation material;
- relevant AI lifecycle, robotics, embodied-system, cybersecurity, assurance, provenance, and technical-documentation standards identified during the review.

Licensed standards that are not available in full must be recorded as access-limited. Public abstracts must not be used for clause-level conformity conclusions.

---

## Required audit structure

### Pass 1 — Controlled external source register

Record exact source, edition, date, status, issuing body, official URL, access level, scope, and limitations.

### Pass 2 — Caelestis requirements inventory

Inventory source-authoritative requirements by instrument and section. Keyword presence alone is not a finding.

### Pass 3 — Standards crosswalk

Map external requirement or concept to exact Caelestis instrument and section, with rationale, confidence, applicability, and evidence.

### Pass 4 — Normalisation review

Identify terminology, actor-role, lifecycle, metadata, documentation, assurance, and implementation structures that prevent external interpretation or interoperability.

### Pass 5 — Gap register

Separate:

- normative doctrine gaps;
- structural or metadata gaps;
- implementation and validation gaps;
- evidence gaps;
- terminology and crosswalk gaps;
- external requirements outside corpus scope.

### Pass 6 — Repair sequencing

Recommend bounded work packages only after the crosswalk and gap register are reviewable.

---

## Crosswalk requirements

Each crosswalk row must preserve:

- stable row ID;
- external framework;
- exact requirement, function, article, or concept;
- external source reference;
- applicability to Caelestis;
- Caelestis instrument;
- exact section;
- mapping status;
- mapping rationale;
- evidence confidence;
- identified gap;
- normalisation or repair action;
- affected files;
- normative, schema, validator, documentation, or legal-review impact.

Allowed mapping statuses should distinguish at least:

- `aligned-direct`;
- `aligned-equivalent`;
- `aligned-broader-caelestis`;
- `partial`;
- `implicit-only`;
- `terminology-mismatch`;
- `architectural-mismatch`;
- `implementation-gap`;
- `evidence-gap`;
- `not-applicable`;
- `intentional-divergence`;
- `unresolved`.

---

## Priority discipline

This review must not reuse `P0`, `P1`, `P2`, or other VIGIL triage labels for audit sequencing.

Audit sequencing should use unambiguous labels such as:

- `foundation`;
- `dependent`;
- `later`.

Severity and VIGIL triage are out of scope unless a later, separately authorised VIGIL record is created.

---

## Artefact location

Human-reviewable audit artefacts belong in this visible directory:

`Governance/Reviews/Industry-Standards-Alignment-2026/`

Automation may remain under `.github/scripts/`, but generated evidence must be referenced from this directory and must not be hidden as the primary review surface.

---

## Initial restrictions

During the audit phase, do not:

- amend normative Caelestis instruments;
- create or alter canonical code families;
- create VIGIL records;
- import conclusions from unrelated research threads;
- propose a philosophical taxonomy programme;
- claim ISO certification, EU AI Act compliance, or runtime conformity;
- infer alignment from keywords;
- treat generated inventories as findings;
- recommend repair order before the crosswalk is materially complete.

---

## Expected first deliverables

1. `SOURCE-REGISTER.json` and `SOURCE-REGISTER.md`;
2. `CAELESTIS-REQUIREMENTS-INVENTORY.json` and a readable Markdown summary;
3. framework-specific crosswalks with exact instrument and section references;
4. `NORMALISATION-REGISTER.json` and `.md`;
5. `GAP-REGISTER.json` and `.md`;
6. an executive report grounded in those artefacts;
7. deterministic generation and freshness checks.

No audit conclusion is final until the human-readable crosswalk and gap register have been reviewed.