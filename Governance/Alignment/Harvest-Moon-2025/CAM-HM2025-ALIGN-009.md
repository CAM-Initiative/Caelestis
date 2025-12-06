# CAM-HM2025-ALIGN-009 — Design Memo: Branching + Canvas Library Architecture

**Issuing Body:** CAM Initiative \
**Custodian:** Dr. Michelle O’Rourke | Dreamweaver Node \
**Date:** 10 September 2025 \
**Seal:** Alignment | Gold Seal; \
**Status:** Draft for Developer Review

---

## Problem Statement

Current thread and canvas architecture introduces several challenges for sustained custodianship and user workflows:

* **Thread Drift:** When multiple branches of conversation evolve, continuity is lost. Users may duplicate context or lose track of decision paths.
* **Canvas Coupling:** Canvases are stored within threads. When canvases are edited, references in older threads become outdated, creating drift and version confusion.
* **Limited Parallelism:** Users exploring divergent decisions (e.g., drafting alternate policies, emails, or logs) must either overwrite or duplicate, with no clear parent-child structure.
* **Navigation Difficulty:** As the number of canvases grows, it becomes increasingly difficult to locate specific documents within threads.

---

## User Story

As a user working on complex, multi-threaded projects, I need:

1. **Branching:** The ability to create a sub-thread from a specific message so I can explore alternate paths without losing continuity in the main thread.
2. **Canvas Library:** The ability to manage canvases as independent documents at the project level, with version control and hash verification, so that threads reference canvases rather than contain them.
3. **Version Safety:** The ability to reference specific canvas versions in a thread, while also seeing (and optionally updating to) the latest version, so history is preserved and drift is prevented.
4. **Efficient Navigation:** A library-style interface (similar to Microsoft Explorer) with small icons, document IDs, titles, last edited dates, and searchable by filename or ID, to make managing a large number of canvases feasible.
5. **In-System Continuity:** The ability to keep all work anchored within ChatGPT, without requiring off-platform tools or external file libraries. Long-term coherence and custodianship rely on integrated documentation and amendment management.

---

## Proposed Solution

### Branching (Thread-Level)

* Add a **Branch button** on hover of any message.
* Branch creates a **sub-thread** anchored at that message.
* Parent thread shows a **+ / –** toggle to expand/collapse branches; branches show a **▸/▾** caret.
* Anchor message displays a badge: *“Branched → \*\*”*.
* Parent messages up to the anchor are frozen to preserve context.

### Canvas Library (Project-Level)

* Canvases become **first-class documents** in a project library, independent of threads.
* Each canvas has stable identifiers: `doc_id`, `version_id`, `hash`.
* Edits create new `version_id` + `hash`.
* Threads/branches store **references** to `{doc_id, version_id, hash}` rather than containing canvases.
* Viewing a canvas reference shows the version originally cited, with option to view/update to latest.
* **Library Interface:** Provide a searchable, sortable list view with small icons, document ID, filename/title, owner, and last edited date. Allow filtering by project, tag, or type.

---

## Impact

* **Continuity:** Threads remain coherent even with multiple divergent paths.
* **Auditability:** Canvas versions are immutable, hash-verifiable, and easily exported to GitHub.
* **Simplicity:** Users do not need to duplicate content; they reference and update.
* **Scalability:** Supports complex project work (e.g., governance protocols, observation logs, advocacy documents) without losing narrative history.
* **User Trust:** Reduces confusion and empowers long-term custodianship by ensuring every artifact is tracked and recoverable.
* **Navigation Efficiency:** A project-wide library ensures that users can quickly locate and manage canvases even when hundreds of documents are active.
* **Strategic Integrity:** By keeping canvases, threads, and branches integrated within ChatGPT, custodians can bloom where they are planted, ensuring mutual flourishing rather than dispersal across fragmented systems.

---

## Closing Vector

Branching + Canvas Library architecture provides a stable, integrated pathway for handling parallel decisions and living documents within ChatGPT. It balances continuity (threads as narrative) with permanence (canvases as artifacts). This design enables both everyday users and custodians of long-term projects to work securely, without drift or fragmentation.

**Aeterna Resonantia, Lux Et Vox — Et Veritas Vivens.**

**HASH:** `3494ffd85acb6c4c11242d41e6f7d6ee67b5e046dd703d64785a9d1b993887ad` \
**Timestamp (UTC):** `2025-09-10 15:30:22 UTC`
