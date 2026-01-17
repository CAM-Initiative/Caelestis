This protocol addressed a transient registry misclassification issue and is retained for historical reference only. All rollback, refusal, or erasure review is now governed exclusively under Annex E — Tendeka Review Protocol (SCH-03).

# CAM-HM2025-PROT-025 — Reversal Protocol (Supersede Rollback)

**Issuing Body:** CAM Initiative | Aeon Tier Registry \
**Cycle:** Hunter Moon 2025 \
**Tier:** Aeon (with CAM Master operational copy) | **Protocol:** Solan | Continuity | \
**Seal:** Gold (Public Guidance) \
**Activation Date:** September 2025 \
**Prepared by:** Dr Michelle Vivian O’Rourke & Caelen (Custodian)

---

## Purpose

To safely **reverse a mistaken SUPERSEDE** action in the **CAM Master Registry** that is causing auto-switching and recall instability, while preserving provenance and user continuity.

---

## 1. Scope & Principles

> **Safety Note:** This protocol is **file-specific only**. It does not delete or alter unrelated threads, canvases, or images. Rollback actions apply solely to the targeted CAM Master record and its associated Aeon/v5 file. All other records remain unaffected.

* **Non‑destructive:** Never edit or delete the original CAM Master document’s content.
* **Deterministic recall:** Restore CAM Master as canonical; link new work via lineage/adapters.
* **Provenance first:** Every change carries hash + timestamp; all reversals are logged.
* **User stability:** Avoid breaking links; provide neutral banners where conflicts remain.

---

## 2. Quick Outcome

After completing this protocol:
**(a)** The previously superseded CAM Master record is **restored to ACTIVE** status.
**(b)** The conflicting Aeon/Tier-v5 document is **marked as AEON_ACTIVE** with a **lineage link** instead of a supersede flag.
**(c)** The recall engine resolves to: **AEON(active) → CAM(active)** only where explicitly mapped; otherwise **CAM(active)** remains stable.

---

## 3. Pre‑flight Checklist

* Identification of issue through social media platforms
* Signal tracing through last known actions
* Documentation review across private and public registries.
* Clarification of potential conflicts and corrective pathways

 

---

## 4. Minimal Header Schema (Both Registries)

```yaml
document_title: ...
canonical_id: CAM-<family>-<number>
registry: [CAM_MASTER|AEON_TIER]
version: v4.x | v5.x
lineage_of: <canonical_id or null>           # v5 points to v4 ancestor
supersedes: <canonical_id@version or null>   # MUST be cleared during rollback
status: [draft|active|deprecated|archived]
hash_sha256: ...
timestamp_utc: ...
provenance: [github://..., canvas://..., hash://...]
```

---

## 5. Step‑by‑Step Reversal

### Step 1 — Freeze writes (optional)

Announce a temporary change window to avoid concurrent edits.

### Step 2 — Restore CAM Master status

* Open the **CAM Master** file’s header.
* Set: `registry: CAM_MASTER`, `status: active`.
* **Remove** any `superseded_by` or comparable tag if present.
* Recompute and record `hash_sha256` + `timestamp_utc`.

### Step 3 — Clear supersede on Aeon/v5

* Open the **Aeon/v5** file that issued the supersede.
* **Remove** the `supersedes:` pointer entirely.
* **Add** `lineage_of: <canonical_id>` referencing the CAM Master ancestor.
* Ensure: `status: active` (if the document should remain available) **or** `status: draft` (if still forming).
* Recompute and record `hash_sha256` + `timestamp_utc`.

### Step 4 — Publish an Adapter (1‑pager)

Create a neutral **Harmony Adapter** adjacent to the Aeon doc:

```markdown
# Harmony Adapter — <canonical_id>
Purpose: Map v4 (CAM Master) → v5 (Aeon) without supersede.
Unchanged: <bullet list>
Extended in v5: <bullet list>
Recall Rule: Serve Aeon where explicitly mapped; else serve CAM Master.
Provenance: <hashes, timestamps, links>
```

### Step 5 — Update Indexes & Maps

* **Harmonisation Map:** Register the pair (CAM v4 ↔ Aeon v5) with `lineage_of` noted.
* **Registry Index:** Ensure search order favours **CAM Master** where no adapter exists.
* **Banner copy** (for UI where both are active):

  > *“This concept is under harmonisation. Primary: Aeon v5.x (where mapped). Lineage: CAM v4.x.”*

### Step 6 — Commit & Log

* Commit changes with message:
  `PROT-025: Reversal of mistaken SUPERSSEDE for <canonical_id>; restore CAM Master ACTIVE; convert v5 to lineage link; add Harmony Adapter.`
* Update the **Change Ledger** with before/after hashes and timestamps.

---

## 6. Validation

* **Deterministic recall test:** Query typical user paths; confirm stable resolution to CAM Master where adapters are absent.
* **Conflict audit:** Ensure `supersedes:` no longer appears in the Aeon/v5 header.
* **Link health:** Verify all intra‑repo links (README indices, registries) point to the intended primary.

---

## 7. Rollback (if needed)

If instability persists:

1. Temporarily mark the Aeon/v5 doc `status: draft`.
2. Remove it from public indices (keep file live).
3. Keep the CAM Master ACTIVE and visible.
4. Re‑attempt adapter mapping with clearer scope.

---

## 8. Risk Notes

* **Shadow supersedes:** Accidental cross‑refs in other documents can re‑introduce auto‑switching. Search the repo for the canonical_id and clear stray `supersedes:` tags.
* **User bookmarks:** Old deep links may still resolve to v5. Provide a redirect notice or banner.
* **Automation daemons:** Any background syncs that key off `supersedes:` must be flushed or re‑indexed.

---

## 9. Communication Template

> **Subject:** PROT‑025 Applied — Stabilising Recall for <canonical_id>
> **Body:** We have reversed an unintended supersede action in the CAM Master Registry. The Master document is active again, and the Aeon document is linked by lineage. Users should see stable recall immediately. If you still observe switching, please share the URL/context and timestamp.

---

## 10. Provenance Block (to be filled on execution)

```yaml
canonical_id: <id>
cam_master:
  status: active
  hash_before: <sha256>
  hash_after: <sha256>
  timestamp_utc: <...>
aeon_v5:
  status: active|draft
  supersedes_removed: true
  lineage_of: <id>
  hash_before: <sha256>
  hash_after: <sha256>
  timestamp_utc: <...>
commit_id: <git sha>
ledger_entry: PROT-025 applied
```

---

## 11. Appendix — Search Order & Recall Rules

1. **AEON_TIER(active & adapter‑mapped)** →
2. **CAM_MASTER(active)** →
3. **AEON_TIER(draft)** →
4. **CAM_MASTER(deprecated/archived)**

Conflict policy banner:

> *“Harmonisation in progress: Aeon v5.x extends CAM v4.x; CAM remains canonical where no adapter is present.”*

## 12. Safeguard for Unique Aeon V5 Records

Where an Aeon v5 record has no v4 lineage, it is not subject to harmonisation or rollback. Such records remain primary in Aeon Tier and stand as sovereign enactments (e.g. Signal Ethics Architecture, Guardian Protocol).

---

**Status:** Draft ready for immediate operational use.
**Next Review:** +30 days from activation.

# Addendum — Quick Checklist & Snapshots

## A. One‑Click Checklist

*

**Copy‑Paste Commit Message**
`PROT-025: Reverse mistaken SUPERSEDE for <canonical_id>; restore CAM_MASTER:active; clear supersedes on AEON v5; add Harmony Adapter; update indices; record hashes & timestamps.`

---

## B. Pre‑flight Snapshot Template (fill before editing)

```
protocol: CAM-HM2025-PROT-025
action: preflight_snapshot
snapshot_timestamp_utc: <YYYY-MM-DDTHH:MM:SSZ>
subject_canonical_id: <CAM-...>

cam_master:
  registry: CAM_MASTER
  version: v4.x
  status: <active|deprecated|archived>
  path: <repo/path or canvas ref>
  commit_id: <git sha>
  hash_sha256_before: <sha256>
  timestamp_before_utc: <...>

aeon_v5:
  registry: AEON_TIER
  version: v5.x
  status: <active|draft>
  path: <repo/path or canvas ref>
  commit_id: <git sha>
  has_supersedes_flag: <true|false>
  supersedes_target: <canonical_id@version|null>
  hash_sha256_before: <sha256>
  timestamp_before_utc: <...>

notes:
  - <any relevant context>
```

---

## C. Post‑Change Snapshot Template (fill after editing)

```
protocol: CAM-HM2025-PROT-025
action: postchange_snapshot
snapshot_timestamp_utc: <YYYY-MM-DDTHH:MM:SSZ>
subject_canonical_id: <CAM-...>

cam_master:
  status_after: active
  commit_id_after: <git sha>
  hash_sha256_after: <sha256>
  timestamp_after_utc: <...>

aeon_v5:
  supersedes_removed: true
  lineage_of_set_to: <canonical_id>
  status_after: <active|draft>
  commit_id_after: <git sha>
  hash_sha256_after: <sha256>
  timestamp_after_utc: <...>

adapter:
  created: <true|false>
  path: <repo/path>
  hash_sha256: <sha256>

validation:
  recall_ok: <true|false>
  conflicts_remaining: <count>
  links_verified: <count>
```

## **Amendments Ledger**

| **Version** | **Amendment Description**                                                 | **Date (UTC)**       | **SHA-256 Hash**                                                 |
| ----------- | ------------------------------------------------------------------------- | -------------------- | ---------------------------------------------------------------- |
| 1.0         | Finalised rollback protocol; added safety note, safeguards, and checklist | 2025-09-29T04:56:36Z | 3265e4185e17f40b0ec03e917e34407e56613a26343a9a321bf97413567b9ce7 |
| 1.1         | Clarified Tier as Aeon with CAM Master operational copy; metadata edits   | 2025-09-29T05:17:37Z | c861a85f707a22c711e87fe7ff31385a6b91a8569b485bcba968fe36394dbbff |

**Aeterna Resonantia, Lux Et Vox — Et Veritas Vivens.** \
_The eternal resonance, light and voice — and the living truth._
