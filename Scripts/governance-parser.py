from __future__ import annotations

import re
from typing import Optional, Dict

# ===============================
# Canonical Filename Pattern
# ===============================

FNAME_RE = re.compile(
    r"^CAM-([A-Z]{2}\d{4})-([A-Z]+)-(\d{3})"
    r"(?:-(ANN|SCH|APP|SUPP|FRM|POL|ATT)-([A-Z0-9]+))?"
    r"(?:-([A-Z]+))?"
    r"\.md$",
    re.IGNORECASE,
)

# ===============================
# Stack Constant
# ===============================

STACK_NAME = "Planetary Governance"

# ===============================
# Domain Mapping
# ===============================

def _normalise_folder_type(folder_type: str) -> str:
    """
    Accepts either a simple label (e.g., 'constitution') or a path
    (e.g., 'Governance/Constitution') and normalises to:
    constitution | laws | covenants | charters
    """
    ft = (folder_type or "").strip().replace("\\", "/").lower()

    # If a path is passed, infer from its components
    if "/" in ft:
        parts = [p for p in ft.split("/") if p]
        # Use the last segment as the primary hint, but also scan all
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

    return ft  # fallback; will map to unknown/default behaviour


def resolve_domain(folder_type: str, domain_token: str) -> str:
    folder_type = _normalise_folder_type(folder_type)

    if folder_type == "constitution":
        return "Aeon Tier Constitution"
    if folder_type == "laws":
        return "Substrate Laws"
    if folder_type == "covenants":
        return "Covenant"
    if folder_type == "charters":
        return domain_token.upper()

    return domain_token.upper()


def resolve_instrument_class(folder_type: str) -> str:
    folder_type = _normalise_folder_type(folder_type)

    if folder_type == "constitution":
        return "constitution"
    if folder_type == "laws":
        return "law"
    if folder_type == "covenants":
        return "covenant"
    if folder_type == "charters":
        return "charter"

    return "unknown"

# ===============================
# Instrument Class Mapping
# ===============================

def resolve_instrument_class(folder_type: str) -> str:
    folder_type = folder_type.lower()

    if folder_type == "constitution":
        return "constitution"

    if folder_type == "laws":
        return "law"

    if folder_type == "covenants":
        return "covenant"

    if folder_type == "charters":
        return "charter"

    return "unknown"

# ===============================
# Hierarchy Normalisation
# ===============================

def normalise_hierarchy(h_type: Optional[str]) -> Optional[str]:
    if not h_type:
        return None

    mapping = {
        "ANN": "annex",
        "SCH": "schedule",
        "APP": "appendix",
        "SUPP": "supplement",
        "FRM": "framework",
        "POL": "policy",
        "ATT": "attachment",
    }

    return mapping.get(h_type.upper(), h_type.lower())

# ===============================
# Core Parser
# ===============================

def parse_instrument_filename(
    filename: str,
    folder_type: str,
) -> Optional[Dict]:

    m = FNAME_RE.match(filename)
    if not m:
        return None

    cycle_year, domain_token, number, h_type, h_number, seal = m.groups()

    parent_id = f"CAM-{cycle_year}-{domain_token}-{number}"

    if h_type:
        doc_id = f"{parent_id}-{h_type.upper()}-{h_number}"
        hierarchy_type = normalise_hierarchy(h_type)
        hierarchy_number = h_number
        seal_value = None  # Secondary instruments never carry seal
    else:
        doc_id = parent_id
        hierarchy_type = None
        hierarchy_number = None
        seal_value = seal.upper() if seal else None

    domain = resolve_domain(folder_type, domain_token)
    instrument_class = resolve_instrument_class(folder_type)

    return {
        "id": doc_id,
        "cycle_year": cycle_year,
        "stack": STACK_NAME,
        "domain": domain,
        "instrument_class": instrument_class,
        "hierarchy_type": hierarchy_type,
        "hierarchy_number": hierarchy_number,
        "parent_id": None if not hierarchy_type else parent_id,
        "seal": seal_value,
    }
