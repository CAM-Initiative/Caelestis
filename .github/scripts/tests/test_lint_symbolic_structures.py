import json
import pathlib
import subprocess
import sys


REPO_ROOT = pathlib.Path(__file__).resolve().parents[3]
SCRIPT = REPO_ROOT / ".github" / "scripts" / "lint-symbolic-structures.py"
BUILDER = REPO_ROOT / ".github" / "scripts" / "build-canonical-code-index.py"


def declaration(identifier, values, *, status="Active", kind="", parent=""):
    hierarchy = ""
    if kind:
        hierarchy += f"| Family Kind | {kind} |\n"
    if parent:
        hierarchy += f"| Parent Family | {parent} |\n"
    return f"""### `{identifier}` — Test declaration
| Field | Entry |
|---|---|
| Code Family | {identifier} |
{hierarchy}| Canonical Name | Test {identifier} |
| Primary Type | Semantic |
| Subtype | TEST |
| Modifier | GOVERNANCE |
| Scope | Test |
| Status | {status} |
| Controlled Values Defined | {values} |
| Schema Field(s) | test_field |
| Source Instrument | Source |
| Source Section | §1 |
| Domain Namespace | TEST |
| Authority / Protection Level | Test classification only |
| Consumes Code Families | None declared |
| Crosswalks Code Families | None declared |
| Operationalises or Applies Code Families | Test classification |
"""


def prepare(tmp_path, consumer_text):
    governance = tmp_path / "Governance"
    governance.mkdir()
    source = "## Canonical Code & Reference Set Declarations\n" + "\n".join([
        declaration("BASE", "BASE.ACTIVE, BASE.DOTTED.VALUE"),
        declaration("BASE.SUB", "BASE.SUB.ACTIVE", kind="subfamily", parent="BASE"),
        declaration("ID.ISTATE", "ID.ISTATE.SYSTEM_PROPOSED"),
        declaration("OLD", "OLD.VALUE", status="Retired"),
    ])
    (governance / "Source.md").write_text(source, encoding="utf-8")
    (governance / "Consumer.md").write_text(consumer_text, encoding="utf-8")
    index = tmp_path / "index.json"
    md_index = tmp_path / "index.md"
    built = subprocess.run(
        [sys.executable, str(BUILDER), "--root", str(governance), "--json-out", str(index), "--md-out", str(md_index)],
        cwd=REPO_ROOT, text=True, capture_output=True, check=False,
    )
    assert built.returncode == 0, built.stdout + built.stderr
    return governance, index


def run_lint(governance, index, *extra):
    return subprocess.run(
        [
            sys.executable, str(SCRIPT), "--root", str(governance),
            "--index", str(index), "--registry", str(governance / "missing-legacy-registry.json"),
            *extra,
        ],
        cwd=REPO_ROOT, text=True, capture_output=True, check=False,
    )


def test_valid_family_value_dotted_value_and_explicit_subfamily_pass(tmp_path):
    governance, index = prepare(
        tmp_path,
        "Uses `BASE`, `BASE.ACTIVE`, `BASE.DOTTED.VALUE`, `BASE.SUB`, and `BASE.SUB.ACTIVE`.\n",
    )
    result = run_lint(governance, index)
    assert result.returncode == 0, result.stdout


def test_stale_identity_value_fails_general_unknown_value_invariant(tmp_path):
    governance, index = prepare(tmp_path, "Current state: `ID.ISTATE.RI_PROPOSED`.\n")
    result = run_lint(governance, index)
    assert result.returncode == 1
    assert "unknown-value: ID.ISTATE.RI_PROPOSED" in result.stdout


def test_unknown_family_fails(tmp_path):
    governance, index = prepare(tmp_path, "Uses `GHOST.FAMILY`.\n")
    result = run_lint(governance, index)
    assert result.returncode == 1
    assert "unknown-family: GHOST.FAMILY" in result.stdout


def test_unknown_value_under_valid_family_fails(tmp_path):
    governance, index = prepare(tmp_path, "Uses `BASE.MISSING`.\n")
    result = run_lint(governance, index)
    assert result.returncode == 1
    assert "unknown-value: BASE.MISSING" in result.stdout


def test_dotted_controlled_value_is_not_inferred_as_subfamily(tmp_path):
    governance, index = prepare(tmp_path, "Uses `BASE.DOTTED.VALUE`.\n")
    inventory = tmp_path / "inventory.json"
    result = run_lint(governance, index, "--inventory-out", str(inventory))
    assert result.returncode == 0, result.stdout
    report = json.loads(inventory.read_text(encoding="utf-8"))
    item = next(row for row in report["references"] if row["sourceFile"].endswith("Consumer.md"))
    assert item["resolution"] == "valid-controlled-value"


def test_retired_value_permitted_in_historical_section(tmp_path):
    governance, index = prepare(tmp_path, "## Historical compatibility\nEarlier records used `OLD.VALUE`.\n")
    result = run_lint(governance, index)
    assert result.returncode == 0, result.stdout


def test_retired_value_fails_in_current_prose(tmp_path):
    governance, index = prepare(tmp_path, "Current systems emit `OLD.VALUE`.\n")
    result = run_lint(governance, index)
    assert result.returncode == 1
    assert "stale-or-retired-current-use: OLD.VALUE" in result.stdout


def test_consumer_does_not_become_source_owner(tmp_path):
    governance, index = prepare(tmp_path, "Uses `BASE.ACTIVE`.\n")
    inventory = tmp_path / "inventory.json"
    result = run_lint(governance, index, "--inventory-out", str(inventory))
    assert result.returncode == 0, result.stdout
    report = json.loads(inventory.read_text(encoding="utf-8"))
    item = next(row for row in report["references"] if row["sourceFile"].endswith("Consumer.md"))
    assert item["semanticRole"] == "consumption"
    assert item["expectedSourceAuthority"].endswith("Source.md")


def test_missing_legacy_registry_does_not_disable_current_validation(tmp_path):
    governance, index = prepare(tmp_path, "Uses `BASE.MISSING`.\n")
    result = run_lint(governance, index)
    assert result.returncode == 1
    assert "legacy symbolic registry absent; current source-derived reference validation remains active" in result.stdout
    assert "unknown-value: BASE.MISSING" in result.stdout


def test_generated_index_source_disagreement_fails(tmp_path):
    governance, index = prepare(tmp_path, "Uses `BASE.ACTIVE`.\n")
    data = json.loads(index.read_text(encoding="utf-8"))
    data[0]["canonical_name"] = "tampered"
    index.write_text(json.dumps(data), encoding="utf-8")
    result = run_lint(governance, index)
    assert result.returncode == 1
    assert "Generated canonical index disagrees" in result.stdout
