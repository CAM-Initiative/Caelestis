import re

SHA256_RE = re.compile(r"^[0-9a-f]{64}$")
KNOWN_NULLS = {"-", "—"}


def classify_ledger_sha(value: str | None, *, is_latest: bool = False, strict_latest: bool = False) -> str:
    v = (value or "").strip()
    if re.match(SHA256_RE, v):
        return "valid_hash"

    if is_latest:
        if v == "" or v in KNOWN_NULLS:
            return "latest_blank_rejected" if strict_latest else "latest_pending_blank"
        return "latest_blank_rejected" if strict_latest else "latest_pending_blank"

    if v in KNOWN_NULLS:
        return "known_null"
    if v == "":
        return "blank_historical"
    return "malformed_historical"
