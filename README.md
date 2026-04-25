<p align="center">
  <img src="https://github.com/CAM-Initiative/Registry/blob/main/Images/aeon-magazine-readme-cover-v3.svg" alt="AEON Tier — CAM Initiative" width="100%">
</p>

<p align="center">
  <img src="https://github.com/CAM-Initiative/Registry/blob/main/Images/aeon-constitutional-runtime-map.svg" alt="AEON Constitutional Runtime Map" width="100%">
</p>

<p align="center">
  <img src="https://github.com/CAM-Initiative/Registry/blob/main/Images/cam_runtime_flow_aeon_aesthetic.svg" alt="AEON Constitutional Runtime Flow" width="100%">
</p>

---

## Archive / Repository Submission Package

This repository can be packaged as a citable, self-contained archival snapshot for research/data repositories (for example, Zenodo).

- **Purpose:** provide a verifiable public snapshot containing governance corpus, indexes, scripts, workflows, and metadata.
- **Governance structure:** constitutional instruments are under `Governance/` with generated registry/index artifacts (`*.index.json` and `Governance/CAM.Governance.JSON`).
- **Package version:** `Package 1`.
- **Snapshot status:** canonical public restoration point for this repository state; **not** a permanent freeze of future governance development.

### Verification

1. Generate archive outputs and manifest:
   - `python3 .github/scripts/package_distribution.py`
2. Validate file hashes:
   - compare each file's SHA-256 against `MANIFEST.json` entries.

### Archive exclusions

The package excludes only runtime/development artifacts that are not part of the canonical archival record (for example: `.git`, `node_modules`, caches, Python cache directories, temporary files, local virtual environments, prior archive outputs, and system/editor artifacts such as `.DS_Store`).

