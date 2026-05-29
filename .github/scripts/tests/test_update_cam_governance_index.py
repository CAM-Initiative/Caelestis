import importlib.util
import json
import pathlib

spec = importlib.util.spec_from_file_location(
    "governance_index",
    pathlib.Path(__file__).resolve().parents[1] / "update-CAM-Governance-Index.py",
)
governance_index = importlib.util.module_from_spec(spec)
spec.loader.exec_module(governance_index)


def test_github_url_for_link_uses_main_blob_url():
    assert governance_index.github_url_for_link("Constitution/CAM-BS2025-AEON-001-PLATINUM.md") == (
        "https://github.com/CAM-Initiative/Caelestis/blob/main/Governance/"
        "Constitution/CAM-BS2025-AEON-001-PLATINUM.md"
    )


def test_github_url_for_link_quotes_path_segments():
    assert governance_index.github_url_for_link("Charters/File With Space.md").endswith(
        "/Governance/Charters/File%20With%20Space.md"
    )


def test_write_json_preserves_generated_urls(tmp_path, monkeypatch):
    out_json = tmp_path / "CAM.Governance.JSON"
    monkeypatch.setattr(governance_index, "OUT_JSON", out_json)

    governance_index.write_json(
        [
            {
                "id": "CAM-TEST-001",
                "link": "Laws/CAM-TEST-001.md",
                "url": governance_index.github_url_for_link("Laws/CAM-TEST-001.md"),
                "summary": "Summary",
            }
        ]
    )

    payload = json.loads(out_json.read_text(encoding="utf-8"))
    assert payload["items"][0]["url"] == (
        "https://github.com/CAM-Initiative/Caelestis/blob/main/Governance/Laws/CAM-TEST-001.md"
    )
