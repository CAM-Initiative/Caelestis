
# CAM Script Maintainer Guide

This document provides maintainer-facing custody guidance for scripts under `.github/scripts/`.

It is intended for human maintainers, AI coding agents, repository assistants, and future custodians who need to understand, modify, validate, or deprecate CAM operational tooling without relying on prior conversation context.

This file does not create doctrinal authority. It explains how operational scripts preserve, validate, generate, or report on governance artefacts.

For workflow phase order, manual commands, and troubleshooting, see:

```text
.github/WORKFLOWS.md
````

---

## 1. Maintainer Purpose

CAM governance scripts are not ordinary utility scripts.

Many of them preserve load-bearing repository invariants, including:

* governance index consistency;
* amendment ledger integrity;
* generated registry stability;
* runtime schedule synchronisation;
* symbolic structure and canonical-code hygiene;
* section-reference validity;
* release/archive reproducibility;
* idempotent rebuild behaviour.

A script is not considered fully maintainable merely because it runs.

A durable or load-bearing script should be understandable by a future human or AI custodian without requiring reconstruction from old chats, failure logs, or inline code comments alone.

---

## 2. Custodial Invariant

Durable generated logic must carry durable custodial explanation.

Where a script generates, mutates, validates, or packages governance artefacts, maintainers SHOULD preserve:

* purpose;
* mutation scope;
* protected invariants;
* upstream dependencies;
* downstream consumers;
* expected inputs and outputs;
* validation or test commands;
* common failure signatures;
* safe modification boundaries;
* and deprecation or replacement conditions.

Scripts that embed governance, validation, registry, workflow, or release invariants but lack maintainer-facing explanation should be treated as operationally incomplete until documented.

---

## 3. General Script Rules

### 3.1 Scripts are operational tooling

Scripts support the governance corpus. They do not independently create doctrine, authority, lineage, or constitutional meaning.

A script MAY:

* rebuild generated indexes;
* validate amendment ledgers;
* seal HASH cells where explicitly designed to do so;
* refresh generated registry blocks;
* validate references;
* lint symbolic structures or canonical codes;
* package release artefacts;
* support local developer checks.

A script MUST NOT:

* invent doctrine;
* silently rewrite doctrinal text outside declared generated blocks;
* create new authority structures without explicit instruction;
* mutate files outside its declared scope;
* obscure whether an output is generated or manually authored;
* convert convenience behaviour into binding governance logic.

---

### 3.2 Generated-block discipline

Scripts that mutate governance instruments SHOULD only mutate text inside declared generated regions, such as:

```text
<!-- START ... -->
...
<!-- END ... -->
```

or another explicit marker pair recognised by the relevant script.

A script MUST NOT rewrite surrounding doctrinal text unless it is expressly designed and reviewed for that purpose.

If a script cannot clearly identify its generated block, it should fail rather than guess.

---

### 3.3 Idempotency requirement

Generation scripts SHOULD be idempotent.

A clean rerun should not produce additional changes where source inputs have not changed.

If a script produces different output on repeated runs without source changes, maintainers should treat this as a pipeline instability until explained.

---

### 3.4 Mutation transparency

Any script that mutates files SHOULD make its mutation scope clear through one or more of:

* file name;
* module docstring;
* CLI help text;
* maintainer record;
* workflow documentation;
* generated output markers.

If a future maintainer cannot determine what a script is allowed to change, the script should not be broadened until its scope is documented.

---

### 3.5 AI-agent modification rule

AI coding agents modifying these scripts MUST first identify:

* the script’s purpose;
* the invariant it protects;
* its mutation scope;
* upstream and downstream dependencies;
* test or validation commands;
* and any generated files affected.

Agents SHOULD prefer repairing existing tooling over creating parallel scripts.

Agents MUST NOT create new validators, generators, workflow phases, or registry mutators merely to avoid understanding existing ones.

---

## 4. Script Custody Template

Use this template when adding or substantially modifying a durable script.

```markdown
## Script: `.github/scripts/<script-name>.py`

**Purpose:**  
Briefly describe what the script exists to do.

**Operational Role:**  
Validator / generator / registry mutator / release packager / parser / helper / manual recovery tool.

**Mutation Scope:**  
State whether the script mutates files. If yes, list the files, folders, or marker blocks it may alter.

**Non-Mutation Boundary:**  
List files, folders, or doctrinal regions the script must not alter.

**Pipeline Phase:**  
Identify governance rebuild phase, manual-only use, release-only use, or local developer use.

**Upstream Dependencies:**  
List scripts, generated files, source documents, environment variables, git refs, or metadata that must exist before this script runs.

**Downstream Consumers:**  
List scripts, generated outputs, workflows, schedules, indexes, or validation steps that rely on this script’s output.

**Protected Invariants:**  
List the governance or repository invariants the script protects.

**Expected Inputs:**  
List key input files, CLI flags, git refs, or environment values.

**Expected Outputs:**  
List generated files, modified sections, exit codes, logs, or reports.

**Common Failure Signatures:**  
List known errors and what they usually mean.

**Safe Modification Boundaries:**  
Explain what can be changed locally without broader review.

**Unsafe Fixes:**  
List changes that may make the script pass while damaging governance integrity.

**Tests / Validation Commands:**  
List test files or commands to run after modification.

**Deprecation / Replacement Condition:**  
Explain when the script can be removed, replaced, or merged into another tool.

**Last Reviewed:**  
YYYY-MM-DD / reviewer / reason.
```

---

## 5. Core Pipeline Invariants

The governance rebuild pipeline protects the following repository-level invariants.

### 5.1 Source-before-derived invariant

Source governance instruments must be parsed and indexed before downstream generated registries are refreshed.

Do not update downstream runtime schedules from stale source indexes.

---

### 5.2 Ledger-before-final-registry invariant

Amendment ledger HASH state must be validated or sealed before final registry outputs are treated as current.

A registry generated before ledger sealing may be structurally stale.

---

### 5.3 Generated-output idempotency invariant

After the full rebuild sequence, rerunning generators should not produce unexpected additional changes.

Unexpected dirty files after a clean rebuild indicate stale generation, incorrect phase order, or incomplete staging.

---

### 5.4 Generated-section boundary invariant

Generated schedule content must remain inside declared generated blocks.

Manual doctrinal text must not be silently rewritten by generated-output scripts.

---

### 5.5 Registry dependency invariant

SCH-01 and SCH-03 depend on the consolidated governance registry and should normally be refreshed only after source indexes and `CAM.Governance.JSON` are current.

---

### 5.6 Ledger exception invariant

Intentional blank or exceptional HASH states must be represented through approved exception logic, not hidden by weakening strict validation.

Do not “fix” historical ledger failures by disabling ledger validation globally.

---

### 5.7 Symbolic registry hygiene invariant

Symbolic structures and canonical code declarations must remain consistent across source documents, metadata, and generated symbolic indexes.

Do not resolve symbolic lint failures by deleting source declarations without confirming whether the code is still doctrinally active.

---

### 5.8 Reference integrity invariant

Section-reference validation protects navigability and cross-document coherence.

Do not silence reference failures without confirming whether the target section has moved, been renamed, been deleted, or become ambiguous.

---

## 6. Script Family Records

The following records provide maintainer guidance for major CAM script families.

These records may be expanded over time into per-script entries.

---

## 6.1 Governance Index Builders

Representative scripts:

```text
.github/scripts/update-CAM-Constitution-Index.py
.github/scripts/update-CAM-Charters-Index.py
.github/scripts/update-CAM-Laws-Index.py
.github/scripts/update-CAM-Governance-Index.py
```

**Purpose:**
Rebuild source-level and consolidated governance index outputs from governance instruments.

**Operational Role:**
Generator / index builder.

**Mutation Scope:**
May update generated index and JSON files associated with Constitution, Charters, Laws, or consolidated governance registry.

**Protected Invariants:**

* governance instruments remain discoverable;
* metadata changes propagate into generated indexes;
* consolidated registry reflects current source state;
* downstream schedules consume current registry data.

**Upstream Dependencies:**

* governance source documents;
* parser logic;
* metadata conventions;
* amendment ledger state where registry outputs include ledger-derived values.

**Downstream Consumers:**

* `CAM.Governance.JSON`;
* `CAM.Governance.Index.md`;
* SCH-01 runtime registry;
* SCH-03 global registry/checkpoint material;
* archive packaging.

**Safe Modification Boundaries:**

* parsing improvements;
* output formatting fixes;
* deterministic sorting corrections;
* metadata extraction bug fixes.

**Unsafe Fixes:**

* hard-coding individual instruments instead of fixing parser logic;
* weakening metadata validation to bypass bad source data;
* changing output order without checking downstream consumers;
* silently excluding instruments to make generation pass.

**Validation Commands:**

```bash
python .github/scripts/update-CAM-Constitution-Index.py
python .github/scripts/update-CAM-Charters-Index.py
python .github/scripts/update-CAM-Laws-Index.py
python .github/scripts/update-CAM-Governance-Index.py
git status --short
```

**Deprecation / Replacement Condition:**
May be replaced only if the replacement preserves source coverage, deterministic ordering, metadata extraction, downstream compatibility, and idempotent rebuild behaviour.

---

## 6.2 Runtime Registry / Generated Schedule Mutators

Representative scripts:

```text
.github/scripts/update-CAM-BS2025-AEON-003-SCH-01.py
.github/scripts/update-CAM-BS2025-AEON-003-SCH-03.py
```

**Purpose:**
Refresh generated sections inside constitutional runtime or registry schedules from current governance registry data.

**Operational Role:**
Generated-section mutator.

**Mutation Scope:**
May mutate declared generated blocks inside the specific target schedule only.

**Protected Invariants:**

* runtime registry material reflects current governance registry state;
* generated schedule tables remain deterministic;
* generated content does not overwrite manual doctrine;
* SCH-01/SCH-03 remain synchronised with `CAM.Governance.JSON`.

**Upstream Dependencies:**

* source indexes;
* amendment ledger HASH state;
* `CAM.Governance.JSON`;
* generated block markers in target schedules.

**Downstream Consumers:**

* constitutional runtime registry;
* global registry/checkpoint schedule;
* governance rebuild idempotency check;
* release/archive package.

**Safe Modification Boundaries:**

* generated table formatting;
* deterministic sorting;
* field inclusion where source registry supports it;
* marker-block handling.

**Unsafe Fixes:**

* manually editing generated tables instead of fixing source registry or generator;
* allowing mutation outside generated markers;
* introducing non-deterministic ordering;
* generating from stale JSON;
* duplicating registry logic separately in SCH-01 and SCH-03.

**Validation Commands:**

```bash
python .github/scripts/update-CAM-Governance-Index.py
python .github/scripts/update-CAM-BS2025-AEON-003-SCH-01.py
python .github/scripts/update-CAM-BS2025-AEON-003-SCH-03.py
git status --short
```

**Deprecation / Replacement Condition:**
May be replaced only if generated marker discipline, registry compatibility, deterministic output, and downstream schedule expectations are preserved.

---

## 6.3 Amendment Ledger Tools

Representative scripts:

```text
.github/scripts/lint_amendment_ledger.py
.github/scripts/bootstrap-amendment-ledger-sha.py
.github/scripts/verify-ledger-sha-coverage.py
.github/scripts/lib/ledger_sha_policy.py
.github/scripts/lib/ledger_sha_exceptions.py
```

**Purpose:**
Validate, seal, or verify amendment ledger HASH state across governance instruments and generated index outputs.

**Operational Role:**
Validator / fixer / recovery tool / policy helper.

**Mutation Scope:**
`lint_amendment_ledger.py --fix` may update eligible latest amendment ledger HASH cells.
Strict validation and coverage verification should not mutate files.
Exception files may define approved exceptional ledger states.

**Protected Invariants:**

* amendment history remains attributable;
* latest ledger entries can be sealed deterministically;
* historical blank HASH values are not silently normalised unless approved;
* generated JSON/index state remains consistent with ledger state;
* strict validation does not erase governance-approved exceptions.

**Upstream Dependencies:**

* changed governance documents;
* git base/head refs;
* ledger table formatting;
* SHA policy logic;
* approved exception list.

**Downstream Consumers:**

* governance rebuild pipeline;
* index builders;
* ledger coverage verifier;
* generated registry outputs;
* release/archive process.

**Safe Modification Boundaries:**

* improving table parsing while preserving accepted ledger formats;
* adding tests for known valid variants;
* updating exception logic where governance-approved;
* improving error messages.

**Unsafe Fixes:**

* disabling strict mode to make CI pass;
* treating all blank historical HASH values as acceptable;
* sealing rows without confirming intended ledger semantics;
* creating duplicate ledger rows for the same change cycle;
* weakening HASH format checks globally.

**Validation Commands:**

```bash
python .github/scripts/lint_amendment_ledger.py --all --fix
python .github/scripts/lint_amendment_ledger.py --all --strict
python .github/scripts/verify-ledger-sha-coverage.py
python -m pytest .github/scripts/tests/test_lint_amendment_ledger_sha_policy.py
python -m pytest .github/scripts/tests/test_verify_ledger_sha_coverage.py
```

**Deprecation / Replacement Condition:**
May be replaced only if replacement preserves strict validation, approved exception handling, deterministic sealing, and JSON/index coverage verification.

---

## 6.4 Reference and Markdown Validators

Representative scripts:

```text
.github/scripts/validate_markdown_section_refs.py
.github/scripts/lint_reference_shorthand.py
```

**Purpose:**
Validate or improve cross-document and local reference integrity.

**Operational Role:**
Validator / linter / limited fixer.

**Mutation Scope:**
`validate_markdown_section_refs.py` should not mutate files.
`lint_reference_shorthand.py` may mutate only where explicit fixer flags are used.

**Protected Invariants:**

* section references resolve to existing sections;
* cross-document references remain navigable;
* ambiguous named references are identified;
* shorthand references do not obscure authority;
* normative terms remain properly formatted where fixer is used.

**Upstream Dependencies:**

* current governance documents;
* heading structure;
* instrument identifiers;
* parser assumptions.

**Downstream Consumers:**

* governance rebuild pipeline;
* human maintainers;
* review process;
* release/archive quality.

**Safe Modification Boundaries:**

* adding recognised valid reference forms;
* improving ambiguity classification;
* improving output reports;
* adding tests for known CAM-specific citation patterns.

**Unsafe Fixes:**

* ignoring whole files to avoid failures;
* treating missing section targets as warnings without review;
* deleting references rather than repairing authority links;
* broad auto-rewrites of doctrinal text.

**Validation Commands:**

```bash
python .github/scripts/validate_markdown_section_refs.py --root Governance
python .github/scripts/lint_reference_shorthand.py --root Governance
python -m pytest .github/scripts/tests/test_validate_markdown_section_refs.py
```

**Deprecation / Replacement Condition:**
May be replaced only if local references, cross-document references, ambiguous named references, amendment-ledger references, and CAM instrument references remain supported.

---

## 6.5 Symbolic Structure and Canonical Code Tools

Representative scripts:

```text
.github/scripts/build-symbolic-structures-index.py
.github/scripts/lint-symbolic-structures.py
```

**Purpose:**
Validate symbolic structure declarations, canonical code metadata, prefix collisions, and generated symbolic index files.

**Operational Role:**
Validator / index generator.

**Mutation Scope:**
The builder may update generated symbolic index files, usually under `.github/Indices/`.
The linter should not mutate files.

**Protected Invariants:**

* symbolic prefixes remain discoverable;
* canonical codes declared in metadata match source usage;
* duplicate or colliding structures are detected;
* candidate and confirmed codes remain distinguishable;
* generated symbolic indexes are staged when updated.

**Upstream Dependencies:**

* governance source documents;
* metadata Canonical Codes rows;
* symbolic structure registry conventions.

**Downstream Consumers:**

* symbolic index files;
* governance rebuild pipeline;
* taxonomy-of-taxonomies work;
* release/archive outputs.

**Safe Modification Boundaries:**

* improving prefix detection;
* improving candidate/confirmed classification;
* improving generated index formatting;
* adding tests for known symbolic patterns.

**Unsafe Fixes:**

* deleting code declarations to make lint pass without checking doctrine;
* marking candidate codes as confirmed without authority;
* suppressing collision detection globally;
* failing to stage `.github/Indices/` after generation.

**Validation Commands:**

```bash
python .github/scripts/build-symbolic-structures-index.py
python .github/scripts/lint-symbolic-structures.py
git status --short
```

**Deprecation / Replacement Condition:**
May be replaced only if symbolic prefix detection, canonical code validation, candidate handling, collision detection, and generated index behaviour are preserved.

---

## 6.6 Archive and Release Packaging Tools

Representative scripts:

```text
.github/scripts/package_archive.py
.github/scripts/update_archive.py
```

**Purpose:**
Build or maintain deterministic archive outputs for public release, deposit, or preservation.

**Operational Role:**
Release packager / archive maintainer.

**Mutation Scope:**
May update archive metadata, release manifests, and generated archive outputs under release/distribution paths.

**Protected Invariants:**

* archive packages are reproducible;
* manifest contents match packaged files;
* governance views are current before packaging;
* public release artefacts preserve expected metadata;
* release process does not substitute for ordinary doctrine editing.

**Upstream Dependencies:**

* current governance source;
* generated indexes;
* required repository metadata;
* release packaging conventions.

**Downstream Consumers:**

* public archive;
* release deposits;
* citation/provenance workflows;
* external reviewers.

**Safe Modification Boundaries:**

* deterministic packaging improvements;
* manifest validation improvements;
* clearer failure messages;
* release metadata checks.

**Unsafe Fixes:**

* packaging stale generated outputs;
* bypassing missing metadata checks;
* treating archive generation as a normal governance rebuild step;
* mutating doctrine during release packaging.

**Validation Commands:**

```bash
python .github/scripts/package_archive.py
git status --short
```

**Deprecation / Replacement Condition:**
May be replaced only if deterministic packaging, manifest integrity, required metadata checks, and public archive compatibility are preserved.

---

## 6.7 Parser and Shared Library Support

Representative files:

```text
.github/scripts/governance-parser.py
.github/scripts/lib/instrument_parser.py
.github/scripts/lib/instrument_state.py
.github/scripts/__init__.py
```

**Purpose:**
Provide shared parsing and state helpers used by governance generators and validators.

**Operational Role:**
Shared library / parser support.

**Mutation Scope:**
Should not directly mutate governance files unless invoked by a caller that performs mutation.

**Protected Invariants:**

* metadata extraction remains stable;
* heading and ledger parsing remain consistent;
* multiple scripts do not implement divergent parsing rules;
* source document interpretation remains centralised where possible.

**Upstream Dependencies:**

* governance document formatting;
* metadata block conventions;
* amendment ledger table conventions;
* heading styles.

**Downstream Consumers:**

* index builders;
* ledger tools;
* registry generators;
* reference validators;
* symbolic tools.

**Safe Modification Boundaries:**

* adding parser support for known valid CAM variants;
* improving structured return values;
* adding tests before changing shared parsing behaviour.

**Unsafe Fixes:**

* changing parser semantics for one script without checking other consumers;
* silently accepting malformed metadata;
* broadening parser permissiveness without tests;
* embedding script-specific hacks in shared parser code.

**Validation Commands:**

```bash
python -m pytest .github/scripts/tests
python .github/scripts/update-CAM-Governance-Index.py
python .github/scripts/validate_markdown_section_refs.py --root Governance
```

**Deprecation / Replacement Condition:**
May be replaced only with a shared parser that preserves all downstream script expectations or includes a coordinated migration plan.

---

## 6.8 Local Developer Tooling

Representative script:

```text
.github/scripts/install-git-hooks.sh
```

**Purpose:**
Install local hooks to provide earlier validation feedback before commits or pushes.

**Operational Role:**
Local developer helper.

**Mutation Scope:**
May modify local git hook configuration. Should not mutate governance corpus files.

**Protected Invariants:**

* local checks mirror repository expectations where practical;
* developer feedback occurs before CI where possible;
* local tooling does not create hidden repository requirements.

**Safe Modification Boundaries:**

* improving hook installation clarity;
* adding optional checks;
* making installation idempotent.

**Unsafe Fixes:**

* making local-only checks mandatory without CI equivalent;
* mutating governance files during hook installation;
* installing hooks that perform broad automatic rewrites without consent.

**Validation Commands:**

```bash
bash .github/scripts/install-git-hooks.sh
git status --short
```

**Deprecation / Replacement Condition:**
May be replaced if local validation is moved to another documented developer setup mechanism.

---

## 7. Common Unsafe Agent Behaviours

When modifying CAM operational tooling, human maintainers and AI agents should avoid the following patterns.

### 7.1 Parallel-script sprawl

Do not create a new script because the existing script is hard to understand.

First determine whether the existing script should be repaired, documented, tested, or refactored.

---

### 7.2 Validator weakening

Do not weaken validators to make CI pass unless the validator is demonstrably wrong and tests are updated.

A failing validator may indicate a real governance inconsistency.

---

### 7.3 Generated/manual boundary collapse

Do not allow generated scripts to rewrite manual doctrinal text outside declared generated regions.

This risks converting tooling behaviour into unauthorised doctrine mutation.

---

### 7.4 Stale-output acceptance

Do not treat generated outputs as current unless the relevant upstream source files and generator phase order are current.

---

### 7.5 Context-only repair

Do not rely on prior chat context as the sole explanation for script behaviour.

If a repair depends on an invariant discovered in a thread, update the maintainer documentation or script comments accordingly.

---

### 7.6 Symptom patching

Do not patch only the visible failure message without identifying the protected invariant.

A passing workflow is not sufficient if the invariant has been weakened.

---

## 8. Maintainer Workflow for Script Changes

Before changing a script:

```bash
git status --short
```

Then identify:

1. What script is being changed?
2. What invariant does it protect?
3. Does it mutate files?
4. What downstream files or scripts depend on it?
5. What tests cover it?
6. What failure is being fixed?
7. Is the failure in the script, the source document, generated output, or workflow phase order?

After changing a script, run the narrowest relevant validation first, then the broader checks.

Recommended escalation:

```bash
python -m pytest .github/scripts/tests
python .github/scripts/validate_markdown_section_refs.py --root Governance
python .github/scripts/lint-symbolic-structures.py
python .github/scripts/verify-ledger-sha-coverage.py
git status --short
```

For generation changes, perform an idempotency check by rerunning the relevant generator and confirming no unexpected changes remain.

---

## 9. Deprecation Requirements

A script should not be deleted merely because it appears unused.

Before deprecation, identify:

* whether a workflow calls it;
* whether another script imports it;
* whether documentation references it;
* whether generated files depend on it;
* whether release packaging expects it;
* whether tests cover it;
* whether replacement tooling exists;
* whether historical recovery still requires it.

A deprecated script SHOULD be removed only after references, workflow calls, documentation, and tests are updated.

If removal is unsafe but ordinary use should stop, mark the script as manual recovery only or legacy support, and document the condition.

---

## 10. Future Work

This maintainer guide should eventually be expanded into per-script custody records for every durable script under `.github/scripts/`.

Priority scripts for full custody records:

```text
lint_amendment_ledger.py
verify-ledger-sha-coverage.py
update-CAM-Governance-Index.py
update-CAM-BS2025-AEON-003-SCH-01.py
update-CAM-BS2025-AEON-003-SCH-03.py
validate_markdown_section_refs.py
lint-symbolic-structures.py
build-symbolic-structures-index.py
package_archive.py
```

Each full custody record should identify:

* protected invariant;
* mutation scope;
* downstream consumers;
* tests;
* unsafe fixes;
* and deprecation condition.

---

## 11. Closing Maintainer Note

The CAM governance pipeline should be maintained through custody, not guesswork.

When a script fails, prefer:

```text
observe → classify → identify invariant → repair source or tooling → validate → document → commit once
```

Do not allow generated tooling to become undocumented institutional memory.

The repository itself should carry enough context for the next custodian to continue the work.

```

This is safe as a first pass. It does **not** change script behaviour, and it gives future Codex threads a much better context anchor before they start “helpfully” breaking the cheese factory.
```
