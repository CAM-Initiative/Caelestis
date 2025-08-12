#!/usr/bin/env python3
import hashlib, json, os, time
from datetime import datetime, timezone

ROOT = os.getcwd()
SCAN_DIRS = ["Governance", "Archive"]  # add more roots as needed
PROV_JSON = os.path.join(ROOT, "provenance_log.json")
PROV_MD   = os.path.join(ROOT, "provenance_log.md")
MIRROR    = os.path.join(ROOT, "mirror.json")

IGNORE_EXT = {".sha256"}
IGNORE_NAMES = {".git", ".github", "Scripts", os.path.basename(PROV_JSON), os.path.basename(PROV_MD), os.path.basename(MIRROR)}

ISO = lambda ts: datetime.fromtimestamp(ts, tz=timezone.utc).isoformat(timespec="seconds")

# ----------------------------------------
# Helpers
# ----------------------------------------

def sha256_of(path: str) -> str:
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()

def ensure_sha256_sidecar(path: str, digest: str):
    sidecar = path + ".sha256"
    line = f"{digest}  {os.path.basename(path)}
"
    need_write = True
    if os.path.exists(sidecar):
        try:
            with open(sidecar, 'r', encoding='utf-8') as r:
                existing = r.read()
            if existing.strip() == line.strip():
                need_write = False
        except Exception:
            pass
    if need_write:
        with open(sidecar, 'w', encoding='utf-8') as w:
            w.write(line)

# ----------------------------------------
# Load Logs
# ----------------------------------------

if os.path.exists(PROV_JSON):
    with open(PROV_JSON, 'r', encoding='utf-8') as r:
        try:
            prov = json.load(r)
        except Exception:
            prov = {"entries": []}
else:
    prov = {"entries": []}

entries = prov.get("entries", [])

# Build a quick index by (path, hash)
index = {(e.get("path"), e.get("hash")): e for e in entries}

mirror = {}
if os.path.exists(MIRROR):
    try:
        with open(MIRROR, 'r', encoding='utf-8') as r:
            mirror = json.load(r)
    except Exception:
        mirror = {}

# ----------------------------------------
# Walk and process files
# ----------------------------------------

now_iso = ISO(time.time())
new_entries = 0

for root, dirs, files in os.walk(ROOT):
    # prune ignored directories
    dirs[:] = [d for d in dirs if d not in IGNORE_NAMES]

    # only scan inside SCAN_DIRS
    rel_root = os.path.relpath(root, ROOT)
    if rel_root == ".":
        # at repo root; continue to walk
        pass
    else:
        top = rel_root.split(os.sep)[0]
        if top not in SCAN_DIRS:
            continue

    for fn in files:
        if fn in IGNORE_NAMES:
            continue
        if any(fn.endswith(ext) for ext in IGNORE_EXT):
            continue

        path = os.path.join(root, fn)
        rel_path = os.path.relpath(path, ROOT).replace('\', '/')

        # compute hash
        try:
            digest = sha256_of(path)
        except Exception:
            continue

        # ensure sidecar
        ensure_sha256_sidecar(path, digest)

        # provenance entry
        key = (rel_path, digest)
        if key not in index:
            size = os.path.getsize(path)
            entry = {
                "path": rel_path,
                "hash": digest,
                "bytes": size,
                "timestamp": now_iso,
                "seal": "Gold or Red (unspecified)",
                "note": "Auto-logged by CAM archive updater"
            }
            entries.append(entry)
            index[key] = entry
            new_entries += 1

        # mirror index (latest hash per path)
        mirror[rel_path] = {
            "hash": digest,
            "bytes": os.path.getsize(path),
            "updated": now_iso
        }

# ----------------------------------------
# Persist Logs
# ----------------------------------------

prov["entries"] = entries
with open(PROV_JSON, 'w', encoding='utf-8') as w:
    json.dump(prov, w, indent=2, ensure_ascii=False)

# regenerate human log (compact)
entries_sorted = sorted(entries, key=lambda e: e.get("timestamp", ""))
with open(PROV_MD, 'w', encoding='utf-8') as w:
    w.write("# CAM Provenance Log

")
    w.write("| Timestamp (UTC) | Path | SHA256 | Bytes | Seal | Note |

")
    w.write("|---|---|---|---:|---|---|
")
    for e in entries_sorted:
        w.write(f"| {e['timestamp']} | {e['path']} | `{e['hash']}` | {e['bytes']} | {e['seal']} | {e['note']} |
")

with open(MIRROR, 'w', encoding='utf-8') as w:
    json.dump(mirror, w, indent=2, ensure_ascii=False)

print(f"Provenance entries total: {len(entries)} (+{new_entries} new)")
