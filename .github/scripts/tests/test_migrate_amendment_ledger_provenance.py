import importlib.util
import pathlib
import json


spec = importlib.util.spec_from_file_location(
    "migration",
    pathlib.Path(__file__).resolve().parents[1] / "migrate-amendment-ledger-provenance.py",
)
migration = importlib.util.module_from_spec(spec)
spec.loader.exec_module(migration)


TIMESTAMP = "2026-08-04T14:26:58Z"


def legacy_document(hash_value="a" * 64):
    return f"""# Test

## 9. Provenance & Metadata

## 9.1 Authorship & Stewardship

| Field | Entry |
|---|---|
| Human | Someone |

## 9.2 Lineage & Metadata

| Field | Entry |
|---|---|
| Parent | CAM-X |

## 9.3 Review & Validation

| Field | Entry |
|---|---|
| Review | Static |

## 9.4 Amendment Ledger

| Version | Change Summary | Timestamp (UTC) | Reference Hash |
|---|---|---|---|
| 1.0 | Initial | 2026-01-01T00:00:00Z | {hash_value} |

## 9.5 Binding Seal

Seal
"""


def test_migration_preserves_historical_cells_and_adds_provenance_row():
    text = legacy_document()
    migrated, version, removed, changed = migration.migrate_text(
        text, timestamp=TIMESTAMP, model="GPT-5.6 Thinking"
    )
    assert changed is True
    assert removed == 2
    assert version == "1.1"
    assert "Authorship & Stewardship" not in migrated
    assert "Review & Validation" not in migrated
    assert "| 1.0 | Initial | 2026-01-01T00:00:00Z | Caelen | GPT-5 Series | Dr M.V. O'Rourke | " in migrated
    assert "a" * 64 in migrated
    assert "| 1.1 |" in migrated
    assert "| Caelen | GPT-5.6 Thinking | Dr M.V. O'Rourke |  |" in migrated


def test_open_row_is_consolidated_not_appended():
    text = legacy_document(hash_value="")
    migrated, version, _removed, _changed = migration.migrate_text(
        text, timestamp=TIMESTAMP, model="GPT-5.6 Thinking"
    )
    assert version == "1.0"
    assert migrated.count("| 1.0 |") == 1
    assert "| 1.1 |" not in migrated
    assert TIMESTAMP in migrated


def test_rebuild_is_idempotent():
    once, _version, _removed, _changed = migration.migrate_text(
        legacy_document(), timestamp=TIMESTAMP, model="GPT-5.6 Thinking"
    )
    twice, _version, removed, changed = migration.migrate_text(
        once, timestamp=TIMESTAMP, model="GPT-5.6 Thinking"
    )
    assert twice == once
    assert removed == 0
    assert changed is False


def test_rebuild_remains_idempotent_after_later_amendment():
    once, _version, _removed, _changed = migration.migrate_text(
        legacy_document(), timestamp=TIMESTAMP, model="GPT-5.6 Thinking"
    )
    later_row = (
        "| 1.2 | Later substantive amendment | 2026-08-04T15:12:23Z | "
        "Caelen | GPT-5.6 Thinking | Dr M.V. O'Rourke | " + "b" * 64 + " |\n"
    )
    with_later_amendment = once.replace("\n## 9.5 Binding Seal", "\n" + later_row + "\n## 9.5 Binding Seal")
    rebuilt, version, removed, changed = migration.migrate_text(
        with_later_amendment, timestamp=TIMESTAMP, model="GPT-5.6 Thinking"
    )
    assert rebuilt == with_later_amendment
    assert version == "1.2"
    assert removed == 0
    assert changed is False


def test_registry_missing_source_detection(tmp_path, monkeypatch):
    registry = tmp_path / "Governance" / "CAM.Governance.JSON"
    registry.parent.mkdir(parents=True)
    registry.write_text(json.dumps({"items": [{"link": "Charters/CAM-MISSING.md"}]}))
    monkeypatch.setattr(migration, "REPO_ROOT", tmp_path)
    assert migration.registry_missing_paths() == [tmp_path / "Governance" / "Charters" / "CAM-MISSING.md"]
