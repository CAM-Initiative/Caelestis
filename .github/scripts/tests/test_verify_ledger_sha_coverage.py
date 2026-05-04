import json
import pathlib
import importlib.util

spec = importlib.util.spec_from_file_location("v", pathlib.Path(__file__).resolve().parents[1] / "verify-ledger-sha-coverage.py")
v = importlib.util.module_from_spec(spec)
spec.loader.exec_module(v)


def write(p, t):
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(t)


def mk_md(rows):
    return "## 1. Amendment Ledger\n\n|Version|Desc|TS|SHA|\n|---|---|---|---|\n" + "\n".join(rows) + "\n"


def run_with(tmp_path, rows, strict=False):
    folder = tmp_path / "Governance" / "Charters"
    md = folder / "CAM-T-001.md"
    write(md, mk_md(rows))
    write(folder / "charters.index.json", json.dumps({"items": [{"id": "CAM-T-001", "HASH": "a"*64}]}))
    v.SCOPES = {"Charters": (folder, folder / "charters.index.json")}
    v.verify_law_manifest = lambda: 0
    import sys
    sys.argv = ["x"] + (["--strict-latest"] if strict else [])
    return v.main()


def test_single_latest_blank_default_pass_strict_fail(tmp_path):
    rows = ["|1.0|d|t|  |"]
    assert run_with(tmp_path, rows, strict=False) == 0
    assert run_with(tmp_path, rows, strict=True) == 1


def test_historical_valid_latest_blank(tmp_path):
    rows = [f"|1.0|d|t|{'a'*64}|", "|1.1|d|t|  |"]
    assert run_with(tmp_path, rows, strict=False) == 0
    assert run_with(tmp_path, rows, strict=True) == 1


def test_historical_blank_fails(tmp_path):
    rows = ["|1.0|d|t|  |", f"|1.1|d|t|{'a'*64}|"]
    assert run_with(tmp_path, rows, strict=False) == 1
    assert run_with(tmp_path, rows, strict=True) == 1


def test_historical_malformed_fails(tmp_path):
    rows = ["|1.0|d|t|abc|", f"|1.1|d|t|{'a'*64}|"]
    assert run_with(tmp_path, rows, strict=False) == 1
    assert run_with(tmp_path, rows, strict=True) == 1


def test_latest_valid_passes(tmp_path):
    rows = [f"|1.0|d|t|{'a'*64}|"]
    assert run_with(tmp_path, rows, strict=False) == 0
    assert run_with(tmp_path, rows, strict=True) == 0
