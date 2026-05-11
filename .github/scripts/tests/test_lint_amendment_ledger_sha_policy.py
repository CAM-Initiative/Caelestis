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
