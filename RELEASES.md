# Repository-Level Release Notes

This file records repository-level release and publication notes only. It does not replace per-instrument amendment ledgers, governance metadata, generated registries, VIGIL records, or archive/DOI records.

Canonical governance amendments are recorded at the instrument level through the relevant amendment ledger and associated metadata. VIGIL records may record observations, failure modes, proposals, and patches where appropriate.

These notes are for repository-facing publication context: reviewer-readiness changes, documentation and contribution-process changes, local validation reproducibility, release/archive metadata reminders, generated-registry publication notes, and public-interface-impacting summaries where applicable. They are not the authoritative history of the CAM corpus.

## Unreleased

### Added

- Added front-door contributor guidance for governance-corpus contribution boundaries.
- Added pull request and issue templates for broken references, metadata/index issues, validator failures, governance amendment proposals, documentation/navigation issues, and sensitive disclosure warnings.
- Added repository-level release notes to summarize publication, archive, validation, documentation, or interface-impacting changes without replacing canonical amendment records.
- Added local validation reproducibility files: `.python-version`, `requirements-dev.txt`, and `scripts/run-governance-checks.sh`.

### Changed

- Expanded and refined the root README to describe the CAM corpus, canonical source-of-truth boundary, reviewer quick start, local validation path, generated indices, validation pipeline, navigation paths, CAM Governance Interface relationship, VIGIL boundary, licence posture, citation metadata, and contribution boundaries.
- Repaired `CITATION.cff` metadata so citation tooling can parse it as valid YAML.
