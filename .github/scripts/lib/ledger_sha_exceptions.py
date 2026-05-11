"""Governance exceptions for intentionally blank ledger/index SHA values.

These identifiers represent instruments whose hash state is intentionally
deferred, externally anchored, or excluded from registry-level SHA
enforcement. Blank SHA/HASH values are therefore expected and must not be
treated as data-quality failures.
"""

ALLOWED_BLANK_SHA_IDS = {
    "CAM-BS2025-AEON-006-SCH-01",
    "CAM-BS2025-AEON-006-SCH-03",
}


def allows_blank_sha(doc_id: str) -> bool:
    return (doc_id or "").strip() in ALLOWED_BLANK_SHA_IDS
