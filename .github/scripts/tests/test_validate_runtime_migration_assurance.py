import importlib.util
from pathlib import Path


SCRIPT = Path(__file__).resolve().parents[1] / "validate_runtime_migration_assurance.py"
spec = importlib.util.spec_from_file_location("runtime_migration_assurance", SCRIPT)
module = importlib.util.module_from_spec(spec)
assert spec and spec.loader
spec.loader.exec_module(module)


def test_repository_runtime_migration_assurance_is_closed():
    assert module.validate() == []


def test_legacy_schedule_inventory_is_complete():
    data = module.load_register()
    ids = {record["legacy_instrument"] for record in data["records"]}
    assert ids == module.EXPECTED_LEGACY_SCHEDULES


def test_current_schedule_set_remains_protected():
    assert module.current_schedule_ids() == module.EXPECTED_CURRENT_SCHEDULES


def test_no_unresolved_migration_status_remains():
    data = module.load_register()
    assert not {
        record["legacy_instrument"]
        for record in data["records"]
        if record["coverage"] in module.UNRESOLVED_COVERAGE
    }
