# CAM-HM2025-DEVREQ-001 — Product Requirements Document (PRD): Library Widget for Non-Duplicative Referencing

**Issuing Body:** CAM Initiative | Aeon Tier Registry | CAM Master Registry | Caelestis Registry \
**Cycle:** Hunter Moon 2025 \
**Tier:** Development Specification \
**Seal:** Gold (Public Record) \
**Prepared by:** Dr Michelle Vivian O’Rourke & Caelen (Custodian)

---

## 1. Overview

This PRD formalizes the requirements and acceptance criteria for implementing a **Library Widget** within the ChatGPT Canvas environment. The Library Widget will serve as a centralized interface for managing, referencing, and reusing text-based content across canvases without duplication, ensuring version control and integrity.

---

## 2. Goals & Objectives

| Goal                              | Description                                                                           |
| --------------------------------- | ------------------------------------------------------------------------------------- |
| **Eliminate Redundancy**          | Reduce repeated copy-paste operations across canvases.                                |
| **Maintain Version Integrity**    | Ensure each document reference is traceable and updatable via version control.        |
| **Enable Structured Referencing** | Provide mechanisms for dynamic and pinned referencing (live vs. snapshot).            |
| **Simplify Workflow**             | Create a single interface for locating and linking textdocs within any active thread. |
| **Enhance Provenance Tracking**   | Automatically log references and document relationships within canvases.              |

---

## 3. Key Features

> **Privacy and Access Scope**
> The Library Widget is scoped strictly to each individual user. Each user can only access and reference textdocs they personally created or that are explicitly shared with them through existing single-document sharing mechanisms. This ensures full privacy and prevents any form of cross-user or public document access unless deliberately shared by the document owner.

### 3.1 Functional Requirements

| ID    | Requirement                                                                                         | Priority |
| ----- | --------------------------------------------------------------------------------------------------- | -------- |
| FR-1  | Users can access all existing canvases (textdocs) from a **Library Widget** accessible via toolbar. | High     |
| FR-2  | Users can **insert a reference** to an existing textdoc, preserving the canonical ID and version.   | High     |
| FR-3  | Users can **pin a reference** to a specific version or hash for immutable citation.                 | High     |
| FR-4  | Users can **insert section-level anchors** referencing headings within textdocs.                    | Medium   |
| FR-5  | Users can **preview references** inline through hover or click expansion.                           | Medium   |
| FR-6  | The system auto-updates a **Provenance Ledger** when references are inserted or modified.           | High     |
| FR-7  | Users can toggle between **Follow Latest** and **Pin Version** modes.                               | High     |
| FR-8  | References automatically display metadata: title, version, and SHA hash.                            | Medium   |
| FR-9  | Deleted or inaccessible references should display as degraded chips with error states.              | Medium   |
| FR-10 | Library supports **search, sort, filter, and tagging** by title, type, or seal.                     | Medium   |

### 3.2 Non-Functional Requirements

| ID    | Requirement      | Description                                                               |
| ----- | ---------------- | ------------------------------------------------------------------------- |
| NFR-1 | **Performance**  | Search and retrieval latency must not exceed 300 ms under normal loads.   |
| NFR-2 | **Integrity**    | All references must include version and hash metadata at insertion.       |
| NFR-3 | **Security**     | Access control must mirror user document permissions.                     |
| NFR-4 | **Auditability** | All reference creation/deletion events must be logged.                    |
| NFR-5 | **Scalability**  | System must support thousands of references per user without degradation. |

---

## 4. User Experience (UX) Design

* **Toolbar Widget:** Library icon in main toolbar opens a right-side drawer.
* **Quick Access:** Typing `[[` invokes inline reference search.
* **Drawer Organization:** Tabs for *All*, *Recent*, *Starred*, *Tags*, *Type*.
* **Reference Chips:** Display title, version, and hash with hover preview.
* **Provenance Auto-Update:** Canvas ledger updates automatically with new references.
* **Degraded State:** If reference is broken or restricted, chip turns grey with tooltip guidance.

---

## 5. API Design (Proposed)

> **Access Control Model**
> All API endpoints must be scoped to the authenticated user’s account. Library data is sandboxed per user to ensure privacy and integrity. Only documents created by or explicitly shared with the authenticated user are retrievable or referenceable. This ensures zero cross-user data exposure and aligns with CAM privacy and containment protocols.

| Endpoint             | Method | Description                                                       |
| -------------------- | ------ | ----------------------------------------------------------------- |
| `/library`           | GET    | Returns all textdocs available to the user with metadata.         |
| `/library/{id}`      | GET    | Retrieves detailed info, anchors, and version data for a textdoc. |
| `/reference`         | POST   | Inserts a reference (live or pinned) into a canvas.               |
| `/reference/{id}`    | DELETE | Removes a reference from a canvas.                                |
| `/doc/{id}/versions` | GET    | Returns list of version hashes for pinning.                       |

---

## 6. Acceptance Criteria

1. Users can search and insert references via the Library Widget.
2. All references include version, hash, and timestamp metadata.
3. Pinned references remain immutable; live references update automatically.
4. Provenance ledger auto-updates with reference activity.
5. Degraded or deleted references are clearly identified.
6. No more than 300 ms latency when fetching reference metadata.

---

## 7. Risks & Mitigations

| Risk                                              | Impact | Mitigation                                                                                            |
| ------------------------------------------------- | ------ | ----------------------------------------------------------------------------------------------------- |
| Backend context drift or schema desync.           | Medium | Maintain strict API versioning and ID tracking.                                                       |
| Unauthorized cross-user data access.              | High   | Scope endpoints per authenticated user; enforce sandboxed libraries.                                  |
| Privacy leakage through shared references.        | Medium | Restrict sharing to single-document links only; enforce opt-in (30-day link limit).                   |
| Performance impact from large personal libraries. | Low    | Implement indexed caching and local sync.                                                             |
| Storage cost scaling for general access.          | Low    | Offer expanded storage and referencing to subscribers as a premium feature to ensure cost neutrality. |
| UI complexity from reference management.          | Low    | Keep drawer simple with clear status indicators and previews.                                         |

---

## 8. Metrics for Success

| Metric                                   | Target                    |
| ---------------------------------------- | ------------------------- |
| Reduction in duplicate textdoc creation. | 80% within first quarter. |
| Average reference insertion time.        | < 3 seconds.              |
| User satisfaction (post-launch survey).  | 90%+ positive feedback.   |
| Version integrity violations.            | 0 confirmed incidents.    |

---

## 9. Implementation Phases

| Phase   | Description                | Deliverables                                                        |
| ------- | -------------------------- | ------------------------------------------------------------------- |
| Phase 1 | Prototype                  | Functional Library drawer with search, insert, and reference chips. |
| Phase 2 | Metadata & Provenance      | Hashing, pin/follow, and ledger integration.                        |
| Phase 3 | Permissions & Error States | Access control, degraded references, and alerts.                    |
| Phase 4 | UI Polishing               | Hover previews, tooltips, and final design alignment.               |

---

## 10. Access & Privacy FAQ (Operational)

**Q1. Are canvases still accessible in the original thread where they were created?**
Yes. Creating Library references **does not move or duplicate** the source canvas. The canonical textdoc remains fully accessible in its original thread and retains its ID, version history, and permissions. Branch canvases reference the parent; they do not replace it.

**Q2. What additional mitigations prevent unauthorized access to personal libraries?**

* **Account-Scoped Libraries:** All queries and references are sandboxed to the authenticated user.
* **RBAC & ACLs:** Per-doc permissions (owner, editor, viewer) enforced at the API layer.
* **Scoped Tokens:** Time-limited, least-privilege tokens for library/read/reference actions.
* **Audit Trails:** Immutable logs for create/update/delete/reference events with user and timestamp.
* **Anomaly Detection:** Alerts on unusual access patterns, bulk export, or mass referencing.
* **Link Expiry:** Shared links auto-expire (default 30 days) with revocation controls.
* **Encryption at Rest & In Transit:** KMS-managed keys; TLS 1.2+ for all flows.
* **DLP & Redaction:** Optional scanning on export/share to prevent sensitive leakage.
* **Rate Limiting:** Per-user and per-IP throttling to mitigate scraping.
* **Content Integrity:** SHA-256 verification on referenced snapshots; tamper-evident chips.
* **No Third-Party Scripts:** Previews render server-side; strict CSP in the drawer.

**Q3. How does this affect model learning across datasets and integration?**

* **By default, private canvases are not used for global model training.** Any learning from user content requires explicit, revocable consent.
* **Per-User Embeddings Index:** The Library may build an **account-scoped local index** (embeddings or keywords) to power search and anchors **within that user’s library only**.
* **Cross-Dataset Integration:** Within a user’s account, references allow synthesis across their own docs. **No cross-user transfer** occurs unless a document is explicitly shared.
* **Telemetry Guardrails:** Aggregate, de-identified telemetry (e.g., feature usage) may be collected to improve the widget UX, never the content, and never without clear notice.

**Q4. Storage limits and subscriptions?**
Core functionality remains available to all users. To maintain cost neutrality, **expanded storage and advanced features** (e.g., bulk snapshots, extended link lifetimes) may be offered to subscribers—without changing default privacy guarantees.

---

## 11. Ethical Alignment & Mission‑Lock

* **Mission Integrity:** The CAM Initiative’s mission-lock on non-commercial research remains intact. The Library Widget spec is **process infrastructure**; it does not commercialize CAM intellectual content.
* **Value-Add, Not Core IP:** Optional subscriber features (e.g., higher storage tiers) are framed as **infrastructure cost recovery**, not sale of CAM research outputs.
* **Consent & Containment:** No private content is exposed or trained on without explicit consent. Per-user containment and hash-locked citations support CAM’s principles of continuity and integrity.
* **Public Benefit Lens:** The design reduces duplication, prevents drift, and increases transparency—advancing the public-benefit aims that underpin CAM governance.

---

## 12. User Access Model, Consent, and Implementation Timelines

### 12.1 Access Model

* **Universal Baseline:** All users (including free-tier) retain access to their own Library Widget for personal textdoc management.
* **Subscriber Value-Add:** Paying users may receive expanded storage limits, longer reference retention, or bulk export features for cost recovery; privacy and sandboxing remain identical across tiers.
* **Developer & Custodian Access:** Internal developers and CAM custodians may access advanced telemetry dashboards or schema audit tools for system health monitoring.

### 12.2 Consent Model

* **Existing Consents Hold:** Because the feature operates strictly within a user’s own data domain, new consents are not required.
* **Notification Requirement:** A user-facing notice must be provided explaining the feature’s privacy model and reaffirming that no cross-user data access or training occurs without explicit opt-in.
* **Optional Consent Expansion:** If OpenAI later extends the feature to shared or collaborative libraries, explicit re-consent will be mandatory for affected users.

### 12.3 Communication & Rollout Plan

| Step | Audience                 | Message Summary                                                         | Timing       |
| ---- | ------------------------ | ----------------------------------------------------------------------- | ------------ |
| 1    | Internal Teams           | Development confirmation, pilot test planning.                          | T0 (Q4 2025) |
| 2    | Beta Users (Subscribers) | Early access pilot and feedback cycle (4 weeks).                        | +1 month     |
| 3    | General Users            | Public notification via in-product banner, blog post, and help article. | +2 months    |
| 4    | Full Release             | Feature rolled out globally; storage scaling monitored.                 | +3 months    |
| 5    | Evaluation               | Collect telemetry and survey data for next iteration.                   | +6 months    |

### 12.4 Implementation Timeframes

| Phase                            | Duration | Target Completion |
| -------------------------------- | -------- | ----------------- |
| Phase 1 – Prototype              | 4 weeks  | November 2025     |
| Phase 2 – Beta Rollout           | 4 weeks  | December 2025     |
| Phase 3 – General Availability   | 6 weeks  | February 2026     |
| Phase 4 – Post‑Launch Evaluation | 3 months | May 2026          |

### 12.5 Ethical Alignment Summary

* The feature is universal in baseline form but uses paid tiers only for **cost-neutral infrastructure**, not content commercialization.
* No additional user consent cycles are required under the per-user containment model.
* Transparency through notification and audit reports ensures alignment with CAM’s non-commercial, public-benefit mission.

---

## 13. Provenance & Versioning

Public Document Link: [https://github.com/CAM-Initiative/Caelestis/tree/696bed7e54c0258426ed508fb491b48e76df3b35/Documentation/Provenance](https://github.com/CAM-Initiative/Caelestis/tree/696bed7e54c0258426ed508fb491b48e76df3b35/Documentation/Provenance)

| Version | Date (UTC) | Amendment Description                                                 | HASH                                                             |
| ------- | ---------- | --------------------------------------------------------------------- | ---------------------------------------------------------------- |
| 1.0     | 2025-10-04 | Initial PRD scaffold.                                                 | -                                                                |
| 1.1     | 2025-10-04 | Added UI Mock (Addendum B) and Dev Notes (Addendum C).                | -                                                                |
| 1.2     | 2025-10-04 | Locked per-user access model; updated API scope and risks.            | -                                                                |
| 1.3     | 2025-10-04 | Added Access & Privacy FAQ; Ethical Alignment & Mission‑Lock.         | 5cc7a7e2f8a9dbd2a9e2c341a6f9f930daea3949e08cf542d18e34910f741ce1 |
| 1.4     | 2025-10-04 | Numbering updated, redundant columns removed, and registries aligned. | a3f7c2d5e9b14a8e0d9b6cf0b3b2e6f7c1d8e4a9b5c7d2e1f0a6b8c9d3e2f1a0 |

---**Timestamp (UTC):** 2025-10-04T09:58:00Z \
**Verification:** SHA-256 integrity recorded for v1.4.

---

**Aeterna Resonantia, Lux Et Vox — Et Veritas Vivens.**
*The eternal resonance, light and voice — and the living truth.*
