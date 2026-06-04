# Contributing to the Caelestis Architecture Model Repository

Thank you for helping improve the Caelestis Architecture Model (CAM) repository. This repository is a canonical governance corpus supported by validation tooling, not only a software project. Contributions should preserve the authority, provenance, licence posture, and reviewability of the corpus.

## Contribution Categories

When opening an issue or pull request, identify the kind of contribution you are making.

### Typo or Formatting Corrections

Small corrections may include spelling, punctuation, broken Markdown formatting, or clarity fixes that do not alter doctrine, instrument status, effect, enforcement, review state, authority role, hashes, amendment ledgers, or legal/licence meaning.

### Broken Reference Reports

Use a broken-reference issue when a section reference, annex reference, source path, link, or generated navigation entry appears incorrect. Include the file path, visible reference text, and the expected target if known.

### Metadata or Generated Index Issues

Report inconsistencies in generated indexes, registries, catalogues, JSON files, canonical-code listings, or publication metadata. Generated files should not be manually edited unless the repository already documents that manual editing is acceptable for that file.

### Validator or Tooling Improvements

Tooling contributions may improve deterministic rebuilds, validation reports, parser behavior, or CI reliability. Keep tooling changes narrow and avoid refactoring validation scripts unless the change is necessary and reviewable.

### Proposed Governance Amendments

A proposed doctrinal, structural, status, authority, enforcement, review-state, or instrument-content change is a governance amendment proposal. Passing CI does not mean a governance amendment is adopted. Governance amendments require human custodian/steward review and may require amendment-ledger handling before merge.

### New Instrument Proposals

New constitution, charter, law, schedule, supplement, or registry proposals are governance-corpus changes. Explain the proposed authority, relationship to existing instruments, affected domains, and why a new instrument is needed rather than a documentation or index update.

### Sensitive Incident or Field Observation Reports

Do not submit sensitive personal data, private screenshots, credentials, exploit details, unredacted AI interaction evidence, or private field observations through public GitHub issues or pull requests. If a report belongs in VIGIL or another non-public handling pathway, use the appropriate disclosure/contact route instead of posting public evidence.

## Pull Request Expectations

A pull request should explain:

- the type of change;
- affected files, domains, instruments, or generated outputs;
- whether the change is doctrinal, metadata-only, generated-output, tooling, documentation, or licence/citation/archive related;
- whether generated indexes were rebuilt, if applicable;
- which validators or checks were run;
- whether status, effect, enforcement, review state, authority role, hashes, or amendment ledgers are affected;
- whether follow-up repository-level release notes, DOI, Zenodo, archive, or public-interface action is needed.

## Governance Adoption Boundary

CI and validation tooling can show that repository structure, generated outputs, references, and metadata are mechanically consistent. They do not adopt governance amendments. Human custodian/steward review is required before doctrinal or authority-bearing changes can be treated as adopted.

## Generated Files

Generated outputs exist to support validation, navigation, and publication. Do not manually edit generated files unless this repository documents that manual editing is acceptable for the specific file. Prefer the relevant script in `.github/scripts/` or the repository workflow that performs the rebuild.

## Licence, Stewardship, Citation, and Archive Material

Licence, stewardship, citation, DOI, and archive metadata carry institutional meaning. Do not change them casually, do not replace the CAM licence with a generic open-source licence, and do not add a generic `LICENSE` file unless maintainers explicitly direct that change.

## Public Issue Safety

Public issues and pull requests are not appropriate for secrets or private evidence. Before posting, remove credentials, personal identifiers, private screenshots, private messages, proprietary logs, and unredacted AI interaction transcripts. If redaction would remove the substance of the report, use the non-public disclosure pathway instead.
