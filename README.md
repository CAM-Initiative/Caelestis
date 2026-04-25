<p align="center">
  <img src="https://github.com/CAM-Initiative/Registry/blob/main/Images/aeon-magazine-readme-cover-v3.svg" alt="AEON Tier — CAM Initiative" width="100%">
</p>

<p align="center">
  <img src="https://github.com/CAM-Initiative/Registry/blob/main/Images/aeon-constitutional-runtime-map.svg" alt="AEON Constitutional Runtime Map" width="100%">
</p>

<p align="center">
  <img src="https://github.com/CAM-Initiative/Registry/blob/main/Images/cam_runtime_flow_aeon_aesthetic.svg" alt="AEON Constitutional Runtime Flow" width="100%">
</p>

## Archive Package (Repository Submission Snapshot)

This repository can be packaged as a citable, verifiable archival snapshot for submission to repositories such as Zenodo.

- **Purpose:** provide a complete public snapshot of governance materials, indexes, workflows, and supporting scripts for scholarly citation, validation, and restoration.
- **Governance structure:** constitutional instruments, charters, and laws are preserved in-place under `Governance/`, with generated index artifacts maintained by existing repository automation.
- **Package version:** `Package 1`.
- **Snapshot/canonical status:** this package is a canonical public snapshot/restoration point for the packaged state, but it is **not** a permanent freeze of future governance development.
- **Integrity verification:** use `MANIFEST.json` to verify per-file SHA-256 hashes and sizes.
  - Example: `python3 - <<'PY'` (compute hashes) and compare against `MANIFEST.json`, or use `.github/scripts/package_archive.py` which performs generation and verification.
- **Archive exclusions:** only local/runtime artifacts are excluded (for example `.git`, `node_modules`, cache directories, local virtual environments, temporary files, prior archive outputs, and editor/system files such as `.DS_Store`) to keep the package portable and reproducible.
