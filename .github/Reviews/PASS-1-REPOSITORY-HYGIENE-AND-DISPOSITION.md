# Pass 1 — Repository Hygiene, Working-File Disposition and Corpus Surface Audit

## Purpose

Pass 1 establishes a clean assessment baseline before substantive corpus findings are recorded.

It must identify and remove completed, superseded or one-off working artefacts that remain in the repository after their implementation work has concluded. It must also separate working review material from the governed corpus so that repository support files are not mistaken for normative instruments.

---

## Location rule

All active and retained working review material belongs under:

`.github/Reviews/`

No review report, delta ledger, migration working paper, trigger note or audit scratch file belongs under `Governance/` unless it is itself an adopted governed instrument.

Generated review evidence belongs under:

`.github/Reviews/generated/`

---

## Immediate cleanup authorised in this pass

Remove the completed historical review artefacts that were retained after their associated refactors were merged:

- `AEON-003-COMPOSED-ARCHITECTURE-REFACTOR-REPORT.md`
- `IDENTITY-DOMAIN-REFACTOR-DELTA.md`
- `IDENTITY-DOMAIN-STAGE-3-SUPPLEMENT-DISPOSITION.md`
- `RED-LINE-FRAMEWORK-CORPUS-INTEGRATION.md`
- `RELATIONAL-IDENTITY-CONSOLIDATION-DELTA.md`

Their implementation history remains available in Git history and the relevant merged pull requests. They are not current corpus instruments and do not require permanent retention in the working tree.

Also remove completed one-off automation artefacts associated with the July red-team governance migration, including:

- `.github/trigger/red-team-governance-20260726.txt`
- `.github/workflows/apply-red-team-governance-extension.yml`

The underlying red-team governance doctrine remains in the adopted corpus. Removing the completed trigger and one-off workflow does not remove or alter that doctrine.

---

## Corpus-wide hygiene inventory

Pass 1 must inspect the full repository for:

- temporary trigger files;
- one-off workflows whose target work has completed;
- migration scripts retained after deterministic migration completion;
- patch helpers and temporary diagnostics;
- review deltas and implementation reports retained after merge;
- duplicate or superseded generated artefacts;
- abandoned draft instruments;
- obsolete compatibility or migration scaffolding;
- working notes embedded in normative instruments;
- hidden working files that should be deleted or retained only under `.github/Reviews/`;
- files whose names imply current authority but whose content is historical, superseded or non-operative.

---

## Disposition categories

Every candidate file must be assigned one of the following outcomes:

- `retain-operational` — required for current repository operation or validation;
- `retain-review` — current working evidence retained under `.github/Reviews/`;
- `retain-historical-source` — an intentional historical or migration source required in the current tree;
- `move-review` — working material located outside `.github/Reviews/`;
- `delete-completed-working-file` — completed review, trigger, helper or migration artefact;
- `delete-duplicate` — redundant copy or generated duplicate;
- `investigate` — purpose or dependency cannot yet be established safely.

---

## Safety rule

Do not delete a script, workflow or historical source solely because its name appears temporary.

Before deletion, determine whether it is:

- referenced by an active workflow;
- required by repository validation or deterministic rebuilds;
- the source of a generated artefact;
- linked from a current governed instrument;
- necessary to reproduce a still-current migration or release process.

Where dependency is uncertain, classify the file as `investigate` rather than deleting it.

---

## Pass 1 deliverables

1. A repository working-file inventory.
2. A disposition register with exact paths and reasons.
3. Removal of clearly completed and dependency-free working artefacts.
4. Relocation of active review material to `.github/Reviews/`.
5. Confirmation that `Governance/` contains only governed corpus material, generated governance outputs and intentionally retained corpus support files.
6. A clean baseline commit before the substantive obsolescence and contradiction audit proceeds.
