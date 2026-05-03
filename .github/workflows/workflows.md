# CAM Repository Workflows

Last updated: 2026-04-29 (UTC)

## Index generation workflow

Use these scripts to regenerate governance indexes:

- `python .github/scripts/update-CAM-Constitution-Index.py`
- `python .github/scripts/update-CAM-Charters-Index.py`
- `python .github/scripts/update-CAM-Laws-Index.py`

Each script now emits debug telemetry:

- number of markdown files detected
- number of entries written
- list of skipped files (if any)

## Hash source of truth

- Constitution and Charters JSON `HASH` values are sourced from each document's Amendment Ledger (latest valid SHA-256 row).
- Laws JSON `HASH` values are sourced from `MANIFEST.json`.

## Verification workflow

- Coverage/integrity check:
  - `python .github/scripts/verify-ledger-sha-coverage.py`
- Law manifest integrity check:
  - `python .github/scripts/verify-law-manifest-integrity.py`

## Typical maintenance sequence

1. Update governance instruments.
2. Regenerate indexes with the three update scripts above.
3. Run verification scripts.
4. Commit generated JSON changes together with script changes.
