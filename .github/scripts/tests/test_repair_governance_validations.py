import pathlib
import importlib.util

spec = importlib.util.spec_from_file_location("repair", pathlib.Path(__file__).resolve().parents[1] / "repair_governance_validations.py")
repair = importlib.util.module_from_spec(spec)
spec.loader.exec_module(repair)


def test_fix_row_requires_valid_version():
    row, changed = repair.fix_row("| X | summary | 2026-05-20T00:00:00Z | |\n")
    assert changed is False
    assert row.startswith("| X |")


def test_fix_row_normalizes_valid_row():
    row, changed = repair.fix_row("|1.2|summary|2026-05-20T00:00:00Z| |\n")
    assert changed is True
    assert row == "| 1.2 | summary | 2026-05-20T00:00:00Z |  |\n"


def test_fix_short_ref_unique_candidate():
    line, changed, todo = repair.fix_short_ref(
        "See RELATION-001 §5.4\n",
        {"CAM-EQ2026-RELATION-001-PLATINUM": pathlib.Path("x")},
    )
    assert changed is True
    assert "CAM-EQ2026-RELATION-001-PLATINUM, §5.4" in line
    assert todo == ""


def test_fix_short_ref_ambiguous_is_todo():
    line, changed, todo = repair.fix_short_ref(
        "See RELATION-001 §5.4\n",
        {
            "CAM-EQ2026-RELATION-001-PLATINUM": pathlib.Path("x"),
            "CAM-EQ2026-RELATION-001-SUP-01": pathlib.Path("y"),
        },
    )
    assert changed is False
    assert "TODO ambiguous short ref" in todo
    assert line == "See RELATION-001 §5.4\n"


def test_fix_row_accepts_three_part_version():
    row, changed = repair.fix_row("|2.4.1|summary|2026-05-20T00:00:00Z| |\n")
    assert changed is True
    assert row == "| 2.4.1 | summary | 2026-05-20T00:00:00Z |  |\n"
