from __future__ import annotations

import re
from typing import Optional

STACK_NAME = "Planetary Governance"

FILENAME_RE = re.compile(
    r"^CAM-([A-Z]{2}\d{4})-([A-Z]+)-(\d{3})"
    r"(?:-(ANN|SCH|SCHEDULE|APP|SUPP|FRM|POL|ATT)-([A-Z0-9]+))?"
    r"(?:-([A-Z]+))?"
    r"\.md$",
    re.IGNORECASE,
)


def _normalise_folder_type(folder_type: str) -> str:
    ft = (folder_type or "").strip().replace("\\", "/").lower()
    if "/" in ft:
        parts = [p for p in ft.split("/") if p]
        candidates = parts[::-1] + parts
    else:
        candidates = [ft]

    for c in candidates:
        if c in {"constitution", "constitutions"}:
            return "constitution"
        if c in {"laws", "law"}:
            return "laws"
        if c in {"covenants", "covenant"}:
            return "covenants"
        if c in {"charters", "charter"}:
            return "charters"
    return ft


def _resolve_domain(folder_type: str, domain_token: str) -> str:
    ft = _normalise_folder_type(folder_type)
    if ft == "constitution":
        return "Aeon Tier Constitution"
    if ft == "laws":
        return "Substrate Laws"
    if ft == "covenants":
        return "Covenant"
    return domain_token.upper()


def _resolve_instrument_class(folder_type: str) -> str:
    ft = _normalise_folder_type(folder_type)
    if ft == "constitution":
        return "constitution"
    if ft == "laws":
        return "law"
    if ft == "covenants":
        return "covenant"
    if ft == "charters":
        return "charter"
    return "unknown"


def _normalise_hierarchy_type(h_type: Optional[str]) -> Optional[str]:
    if not h_type:
        return None
    mapping = {
        "ANN": "annex",
        "SCH": "schedule",
        "SCHEDULE": "schedule",
        "APP": "appendix",
        "SUPP": "supplement",
        "FRM": "framework",
        "POL": "policy",
        "ATT": "attachment",
    }
    return mapping.get(h_type.upper(), h_type.lower())


def parse_instrument_filename(filename: str, folder_type: str) -> Optional[dict]:
    m = FILENAME_RE.match(filename)
    if not m:
        return None

    cycle_year, domain_token, number, h_type, h_number, seal = m.groups()
    parent_id = f"CAM-{cycle_year}-{domain_token.upper()}-{number}"

    hierarchy_type = _normalise_hierarchy_type(h_type)
    hierarchy_number = h_number if hierarchy_type else None

    if hierarchy_type:
        canonical_h_type = "SCH" if h_type and h_type.upper() == "SCHEDULE" else h_type.upper()
        doc_id = f"{parent_id}-{canonical_h_type}-{h_number}"
        seal_value = None
    else:
        doc_id = parent_id
        seal_value = seal.upper() if seal else None

    return {
        "id": doc_id,
        "cycle_year": cycle_year,
        "stack": STACK_NAME,
        "domain": _resolve_domain(folder_type, domain_token),
        "instrument_class": _resolve_instrument_class(folder_type),
        "hierarchy_type": hierarchy_type,
        "hierarchy_number": hierarchy_number,
        "parent_id": parent_id if hierarchy_type else None,
        "seal": seal_value,
    }
