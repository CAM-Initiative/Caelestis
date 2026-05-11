import pathlib
import importlib.util

spec = importlib.util.spec_from_file_location("ledger", pathlib.Path(__file__).resolve().parents[1] / "lint_amendment_ledger.py")
ledger = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ledger)


def mk(rows: list[str]) -> str:
    return "## 1. Amendment Ledger\n\n|Version|Desc|TS|SHA-256|\n|---|---|---|---|\n" + "\n".join(rows) + "\n\n## 2. X\n"


def eval_rows(rows, strict=False):
    f=[]; w=[]; s={}
    ledger.evaluate_historical_and_latest_hashes("x.md", mk(rows), f, w, s, strict_latest=strict)
    return f,w,s


def test_historical_dash_passes():
    f,w,s = eval_rows(["|1.0|a|t|-|", "|1.1|b|t|  |"])
    assert not f
    assert s.get("historical_known_null_shas",0) == 1


def test_historical_blank_fails():
    f,_,_ = eval_rows(["|1.0|a|t|  |", "|1.1|b|t|  |"])
    assert f


def test_historical_malformed_fails():
    f,_,_ = eval_rows(["|1.0|a|t|abc|", "|1.1|b|t|  |"])
    assert f


def test_latest_blank_passes_default_and_warns():
    f,w,s = eval_rows([f"|1.0|a|t|{'a'*64}|", "|1.1|b|t|  |"], strict=False)
    assert not f
    assert w
    assert s.get("blank_latest_sha_allowed",0) == 1


def test_latest_blank_fails_strict():
    f,w,s = eval_rows([f"|1.0|a|t|{'a'*64}|", "|1.1|b|t|  |"], strict=True)
    assert f
    assert s.get("blank_latest_sha_rejected",0) == 1


def test_multiple_files_simulated_summary_behavior():
    f=[]; w=[]; s={}
    ledger.evaluate_historical_and_latest_hashes("a.md", mk([f"|1.0|a|t|{'a'*64}|","|1.1|b|t|  |"]), f,w,s, strict_latest=False)
    ledger.evaluate_historical_and_latest_hashes("b.md", mk([f"|1.0|a|t|{'b'*64}|","|1.1|b|t|-|"]), f,w,s, strict_latest=False)
    assert not f
    assert s.get("valid_historical_sha",0) == 2


def test_allowlisted_latest_blank_passes_in_strict_mode():
    f=[]; w=[]; s={}
    ledger.evaluate_historical_and_latest_hashes(
        "Governance/Charters/CAM-BS2025-AEON-006-SCH-01.md",
        mk([f"|1.0|a|t|{'a'*64}|", "|1.1|b|t|  |"]),
        f,
        w,
        s,
        strict_latest=True,
    )
    assert not f
    assert any("Allowed blank SHA: CAM-BS2025-AEON-006-SCH-01" in msg for msg in w)


def test_latest_open_row_prevents_append():
    text = mk([f"|1.0|a|t|{'a'*64}|", "|1.1|b|t|  |"])
    assert ledger.latest_ledger_row_is_open(text) is True
    updated, added = ledger.append_amendment_ledger_entry(
        text,
        description="auto",
        timestamp_utc="2026-05-11T00:00:00Z",
    )
    # low-level append function still appends; guard is enforced in lint() via latest_ledger_row_is_open
    assert added is True
    assert "| 1.2 |" in updated


def test_new_row_appended_when_latest_is_sealed():
    text = mk([f"|1.0|a|t|{'a'*64}|"])
    assert ledger.latest_ledger_row_is_open(text) is False
    updated, added = ledger.append_amendment_ledger_entry(
        text,
        description="auto",
        timestamp_utc="2026-05-11T00:00:00Z",
    )
    assert added is True
    assert "| 1.1 | auto | 2026-05-11T00:00:00Z |  |" in updated


def test_fix_seals_existing_open_latest_row_without_appending():
    text = mk([f"|1.0|a|t|{'a'*64}|", "|1.1|b|t|  |"])
    sealed_text, stored_hash, changed, _ = ledger.update_last_ledger_hash_cell(text, fix=True)
    assert changed is True
    row_info = ledger.get_last_ledger_row_info(sealed_text)
    assert row_info is not None
    cols = ledger.split_markdown_table_row(row_info[1].strip())
    assert cols[-1].strip()
    assert "|1.1|b|t|  |" not in sealed_text


def test_sch02_not_in_blank_sha_allowlist():
    assert ledger.allows_blank_sha("CAM-BS2025-AEON-003-SCH-02") is False
