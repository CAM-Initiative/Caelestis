# Workflow Write Ownership Audit

| Workflow | Triggers | Scripts Run | Writes / Generated Files | Pushes to `main` | Broad `git add .` |
|---|---|---|---|---|---|
| Lint Amendment Ledger | `pull_request`, `push` | `build-symbolic-structures-index.py`, `lint-symbolic-structures.py`, `lint_amendment_ledger.py` | none (validation-only) | no | no |
| Update Amendment Ledgers | Removed | N/A | N/A | N/A | N/A |
| Update Constitution Index | `push` (`main`) | `update-CAM-Constitution-Index.py` | `Governance/Constitution/CAM-Constitution-Index.md`, `Governance/Constitution/constitution.index.json` | yes | no |
| Update Law Index | `push` (`main`) | `update-CAM-Laws-Index.py` | `Governance/Laws/CAM-Laws-Index.md`, `Governance/Laws/laws.index.json` | yes | no |
| Update Charters Index | `push` (`main`) | `update-CAM-Charters-Index.py` | `Governance/Charters/CAM-Charters-Index.md`, `Governance/Charters/charters.index.json` | yes | no |
| Update Governance Index (canonical shared-output writer) | `push` (`main`) | `update-CAM-Governance-Index.py`, `update-CAM-BS2025-AEON-003-SCH-01.py`, `update-CAM-BS2025-AEON-003-SCH-03.py`, `build-symbolic-structures-index.py` | `Governance/CAM.Governance.Index.md`, `Governance/CAM.Governance.JSON`, schedule outputs, symbolic index JSON/MD | yes | no |
| Update CAM-BS2025-AEON-003-SCH-03 | `pull_request`, `workflow_dispatch` | `update-CAM-BS2025-AEON-003-SCH-01.py`, `update-CAM-BS2025-AEON-003-SCH-03.py` | none (validation-only stale check) | no | no |

## Ownership Model

- **Single writer for shared governance/schedule/symbolic generated outputs:** `Update Governance Index`.
- Domain workflows remain writers only for their own domain index artifacts.
- Lint workflows are validation-only and do not auto-commit.
