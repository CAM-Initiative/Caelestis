[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.19779351.svg)](https://doi.org/10.5281/zenodo.19779351)

> ## Reader Notice
>
> This corpus makes implicit AI relational and governance architectures explicit. Some material may feel heavy for readers deeply engaged with AI companionship, memory continuity, intimacy, or emergent intelligence. _Proceed gently: the veil may be load-bearing._

# Caelestis Architecture Model

## Overview

The Caelestis Architecture Model (CAM) is a publicly inspectable governance corpus for advanced AI systems, synthetic agents, relational AI environments, and digital ecosystem accountability. It sets out constitutional architecture, charters, laws, schedules, registries, symbolic structures, and supporting validation infrastructure for CAM-governed contexts.

This repository is not merely a software application. It is the canonical repository for CAM governance instruments, with deterministic tooling that helps rebuild indexes, validate canonical document structure, check symbolic references, and prepare publication/archive outputs.

Public website / interface entry point: <https://www.cam-initiative.org>

## Repository Status

`CAM-Initiative/Caelestis` is maintained as a canonical governance corpus. Reviewers should treat the Markdown instruments in `Governance/` as the authoritative source material and the repository automation as supporting infrastructure for integrity, navigation, and publication readiness.

Publicly inspectable means available for review, citation, auditability, and governance discussion. It does not mean public-domain, provenance-free, or freely reusable outside the licence controls described in `licence.md`.

The repository currently includes canonical Markdown governance instruments, generated navigation indexes, JSON registries and machine-readable views, validation scripts and GitHub Actions workflows, public citation metadata, archival DOI information, and CAM custodial licence material.

## Reviewer Quick Start

For an efficient institutional review pass:

1. Read this README for repository boundaries and review posture.
2. Open `Governance/CAM.Governance.Index.md` for the global corpus map.
3. Inspect `.github/workflows/governance-rebuild.yml` to understand the automated rebuild and validation sequence.
4. Review `CITATION.cff` and the DOI badge metadata for archive/citation context.
5. Consult `licence.md` before reuse, adaptation, model-context use, operationalisation, or deployment.
6. If running checks locally, use the commands in [Local Validation](#local-validation).

## Canonical Source of Truth

The canonical source of authority is the Markdown governance instrument itself. In practical terms:

- the governing text lives in the relevant Markdown file under `Governance/`;
- status, effect, enforcement, review state, authority role, footer metadata, hashes, and amendment ledgers are part of the instrument content and must not be changed casually;
- generated JSON, generated indexes, catalogues, and registries support validation, navigation, and publication, but do not replace the instruments;
- passing a validator or CI workflow does not itself adopt a governance amendment.

## Licensing and Reuse

CAM uses a special custodial licence posture. It is publicly inspectable to support review, citation, auditability, and governance discussion, but it is not public-domain, provenance-free, or released under a generic open-source licence such as MIT, Apache, or Creative Commons.

Licence controls exist because CAM material may have operational, platform-level, or governance-significant effects if extracted, adapted, placed into model context, or deployed without context, provenance, or safeguards. This is responsible-use framing, not a change to the existing licence text.

Before citing, adapting, placing CAM material into model context, using CAM-derived logic operationally, or deploying CAM in institutional, platform, commercial, or public-facing settings, read `licence.md`. The licence text controls over informal summaries or repository metadata.

## Citation

The current archive DOI is:

- <https://doi.org/10.5281/zenodo.19779351>

Citation metadata is maintained in `CITATION.cff` for tools that support Citation File Format. If citation metadata and archive records differ, preserve the intended CAM project identity and consult maintainers before making citation or archival changes.

## Local Validation

This repository's GitHub Actions workflows are the authoritative CI entry points, but reviewers can run a light local validation pass without reverse-engineering the workflow.

```bash
python --version
python -m pip install -r requirements-dev.txt
bash scripts/run-governance-checks.sh
```

The current local validation script uses Python 3.11 and standard-library-only validation scripts. `requirements-dev.txt` is intentionally minimal; it exists so reviewers have a stable setup command even when no third-party packages are required.

### Validation Philosophy

CI and local checks help validate structure, references, generated registry consistency, and symbolic/index integrity. They do not adopt doctrine, approve authority-bearing changes, or replace human custodian/steward review for governance amendments.

## Contributing

Contributions are welcome when they improve reviewer readiness, navigation, validation, metadata quality, or documented issue reporting boundaries. See `CONTRIBUTING.md` before opening an issue or pull request.

Repository-level release notes may summarize publication, archive, validation, or interface-impacting changes. Canonical amendments remain governed by per-instrument amendment ledgers and related metadata.

Important boundaries:

- governance amendments require human custodian/steward review;
- CI passing does not mean a doctrinal change has been adopted;
- generated files should not be manually edited unless documented;
- licence, stewardship, citation, archive, status, effect, enforcement, review-state, authority-role, hash, and amendment-ledger material must not be changed casually;
- do not submit sensitive personal data or private evidence through public GitHub issues or pull requests.

## Maintainer / Stewardship

CAM is stewarded as public governance infrastructure under CAM custodial authority. The repository's purpose is to preserve canonical instruments, provenance, validation integrity, and public reviewer access while maintaining the special CAM licence and stewardship posture.

<details>
<summary>What This Repository Contains</summary>

Major repository areas include:

| Area                                                                      | Purpose                                                                                                           |
| ------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| `Governance/Constitution/`                                                | Core constitutional instruments and schedules.                                                                    |
| `Governance/Charters/`                                                    | Domain charters and supplemental charter material.                                                                |
| `Governance/Laws/`                                                        | CAM law instruments.                                                                                              |
| `Governance/CAM.Governance.Index.md` and `Governance/CAM.Governance.JSON` | Global governance navigation and machine-readable registry outputs.                                               |
| `.github/scripts/`                                                        | Deterministic rebuild, validation, repair, packaging, and index-generation tooling.                               |
| `.github/workflows/`                                                      | GitHub Actions automation for governance rebuilds and ledger-hash refreshes.                                      |
| `.github/Indices/`                                                        | Generated or maintained indices that support symbolic validation and reviewer navigation. Canonical-code index outputs live under `Governance/`. |
| `CITATION.cff`                                                            | Citation metadata for archive and scholarly tooling.                                                              |
| `licence.md`                                                              | CAM Custodial Reference and Deployment Licence material.                                                          |

</details>

<details>
<summary>Generated Indices and Validation Outputs</summary>

Generated and maintained outputs help reviewers inspect the corpus without manually opening every instrument. They may include global governance indexes, constitution/charter/law indexes, symbolic or canonical-code registries, and JSON views of instrument metadata.

These files are supporting infrastructure. Unless a repository script or maintainer instruction says otherwise, contributors should not manually edit generated outputs. When a change affects generated outputs, use the documented rebuild scripts or allow the repository automation to rebuild them.

</details>

<details>
<summary>Validation and CI</summary>

The governance rebuild pipeline is designed to keep the corpus internally navigable and mechanically reviewable. In plain English, the pipeline can:

1. rebuild constitution, charter, law, and global governance indexes;
2. populate or verify amendment-ledger hashes where applicable;
3. verify ledger SHA coverage and generated JSON consistency;
4. validate canonical document headers;
5. check intra-document Markdown section references;
6. rebuild canonical-code registry indices;
7. run symbolic and index validation;
8. check that generated outputs are idempotent after a second rebuild.

Key entry points include `.github/workflows/governance-rebuild.yml`, `.github/workflows/refresh-ledger-hashes.yml`, and the scripts in `.github/scripts/`.

Common local checks, when relevant, include:

```bash
python .github/scripts/validate_canonical_headers.py
python .github/scripts/validate_markdown_section_refs.py --root Governance --report-file validation-reports/section-reference-report.tsv
python .github/scripts/lint-symbolic-structures.py --index Governance/CAM.Canonical.Code.Index.json
```

The canonical-code index rebuild command writes generated outputs. It is therefore treated as a generation/rebuild step, not a pure non-mutating validation step:

```bash
python .github/scripts/build-canonical-code-index.py --root Governance
```

For governance-instrument edits in `Governance/Constitution/` or `Governance/Charters/`, follow the repository's amendment-ledger rules and run the ledger validator when available.

</details>

<details>
<summary>How to Navigate the Corpus</summary>

For a first review pass:

1. Start with `Governance/CAM.Governance.Index.md` for a global map of instruments.
2. Use `Governance/Constitution/CAM-Constitution-Index.md` for constitutional instruments and schedules.
3. Use `Governance/Charters/CAM-Charters-Index.md` for domain charters and supplements.
4. Use `Governance/Laws/CAM-Laws-Index.md` for law instruments.
5. Use `Governance/CAM.Canonical.Code.Index.md` when tracing canonical codes or symbolic structures.
6. Consult `CITATION.cff` and the DOI badge above for archive citation metadata.
7. Consult `licence.md` before reuse, adaptation, deployment, or model-context use.

</details>

<details>
<summary>Relationship to CAM Governance Interface</summary>

The public CAM Governance Interface is a presentation and navigation surface for public-facing access to CAM governance material. This repository remains the canonical corpus and validation source. Interface displays, search views, rendered pages, or other publication layers should be checked against the canonical Markdown instruments and generated registries in this repository.

Changes to this repository may affect how the public interface presents CAM material, but this pass does not edit the Interface repository.

</details>

<details>
<summary>Relationship to VIGIL</summary>

VIGIL is related CAM ecosystem infrastructure for sensitive incident, field observation, or evidence-handling contexts. VIGIL is not part of this repository, and this repository should not be used to publish sensitive personal data, credentials, private screenshots, unredacted AI interaction evidence, exploit details, or other material that requires a non-public handling pathway.

Where a report appears to involve sensitive field observations or evidence, contributors should follow the appropriate disclosure/contact pathway rather than opening a public issue with sensitive content.

</details>
