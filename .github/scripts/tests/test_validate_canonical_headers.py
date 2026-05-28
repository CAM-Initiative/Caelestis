import importlib.util
import pathlib

spec = importlib.util.spec_from_file_location(
    "headers", pathlib.Path(__file__).resolve().parents[1] / "validate_canonical_headers.py"
)
headers = importlib.util.module_from_spec(spec)
spec.loader.exec_module(headers)


def issues(text, path="Governance/Constitution/CAM-BS2025-AEON-001-PLATINUM.md"):
    return headers.validate_text(path, text, expected_id=pathlib.Path(path).stem)


def codes(found):
    return {issue.code for issue in found}


def test_valid_canonical_h1():
    found = issues(
        "# CAM-BS2025-AEON-001-PLATINUM — Aeon Tier Constitution\n\n"
        "**Instrument Type:** Constitution\n"
        "**Status:** Adopted\n\n---\n\n## 1. Purpose\n"
    )
    assert found == []


def test_missing_h1():
    found = issues("**Instrument Type:** Constitution\n\n## 1. Purpose\n")
    assert "missing_h1" in codes(found)


def test_duplicated_h1_in_header_block():
    found = issues(
        "# CAM-BS2025-AEON-001-PLATINUM — Aeon Tier Constitution\n"
        "# CAM-BS2025-AEON-001-PLATINUM — Aeon Tier Constitution\n"
        "**Instrument Type:** Constitution\n"
        "**Status:** Adopted\n"
    )
    assert "duplicated_h1" in codes(found)


def test_metadata_block_duplicated_but_would_previously_pass():
    found = issues(
        "# CAM-BS2025-AEON-001-PLATINUM — Aeon Tier Constitution\n\n"
        "**Instrument Type:** Constitution\n"
        "**Status:** Adopted\n\n"
        "**Instrument Type:** Constitution\n"
        "**Status:** Adopted\n\n"
        "---\n"
    )
    assert "duplicated_metadata_block" in codes(found)


def test_h1_missing_title_after_emdash():
    found = issues("# CAM-BS2025-AEON-001-PLATINUM —   \n")
    assert "h1_missing_full_title" in codes(found)


def test_h1_with_only_instrument_id():
    found = issues("# CAM-BS2025-AEON-001-PLATINUM\n")
    assert "h1_only_instrument_id" in codes(found)


def test_h1_not_first_non_empty_line():
    found = issues("\n# CAM-BS2025-AEON-001-PLATINUM — Aeon Tier Constitution\n")
    assert "h1_not_first_non_empty" in codes(found)


def test_annex_g_specific_regression_case_mismatched_id():
    found = issues(
        "# CAM-BS2025-AEON-008-PLATINUM — Annex G: Human Creative & Cognitive Contribution Recognition, Boundaries, and Valuation Preconditions\n",
        path="Governance/Constitution/CAM-BS2026-AEON-008-PLATINUM.md",
    )
    assert "instrument_id_mismatch" in codes(found)
