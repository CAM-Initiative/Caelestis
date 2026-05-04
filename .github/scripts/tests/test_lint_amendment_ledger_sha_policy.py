import pathlib
import importlib.util

spec = importlib.util.spec_from_file_location("ledger", pathlib.Path(__file__).resolve().parents[1] / "lint_amendment_ledger.py")
ledger = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ledger)


def mk(rows: list[str]) -> str:
    return "## 1. Amendment Ledger\n\n|Version|Desc|TS|SHA-256|\n|---|---|---|---|\n" + "\n".join(rows) + "\n\n## 2. X\n"


def test_latest_blank_allowed_default():
    text = mk(["|1.0|a|t|" + "a"*64 + "|", "|1.1|b|t|  |"])
    f=[]; w=[]; s={}
    ledger.evaluate_historical_and_latest_hashes("x.md", text, f, w, s)
    assert not f
    assert w


def test_historical_blank_fails():
    text = mk(["|1.0|a|t|  |", "|1.1|b|t|  |"])
    f=[]; w=[]; s={}
    ledger.evaluate_historical_and_latest_hashes("x.md", text, f, w, s)
    assert f


def test_historical_malformed_fails():
    text = mk(["|1.0|a|t|abc|", "|1.1|b|t|  |"])
    f=[]; w=[]; s={}
    ledger.evaluate_historical_and_latest_hashes("x.md", text, f, w, s)
    assert f


def test_latest_valid_passes():
    text = mk(["|1.0|a|t|" + "a"*64 + "|", "|1.1|b|t|" + "b"*64 + "|"])
    f=[]; w=[]; s={}
    ledger.evaluate_historical_and_latest_hashes("x.md", text, f, w, s)
    assert not f
    assert not w
