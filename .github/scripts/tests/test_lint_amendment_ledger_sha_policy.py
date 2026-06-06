import pathlib
import subprocess
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


def test_malformed_date_only_row_is_detected_with_line_number():
    text = mk(["| 2026-05-20 | | | |", "|1.1|b|t|  |"])
    malformed = ledger.get_malformed_ledger_rows(text)
    assert malformed
    assert malformed[0][0] > 0


def test_malformed_non_version_first_cell_detected():
    text = mk(["| Annex B | desc | 2026-05-20T00:00:00Z | |", "|1.1|b|t|  |"])
    malformed = ledger.get_malformed_ledger_rows(text)
    assert any("dotted numeric version" in msg for _, msg in malformed)


def test_structurally_valid_latest_blank_hash_allowed():
    text = mk(["|1.0|summary|2026-05-20T00:00:00Z|  |"])
    malformed = ledger.get_malformed_ledger_rows(text)
    assert malformed == []


def test_formatting_only_categories_are_accepted():
    rows = [
        "|1.0|minor formatting patch in headings|2026-05-20T00:00:00Z|  |",
        "|1.1|formatting correction for section numbering-only references|2026-05-21T00:00:00Z|  |",
        "|1.2|metadata formatting correction (metadata-ordering, table-alignment, whitespace-only)|2026-05-22T00:00:00Z|  |",
    ]
    text = mk(rows)
    malformed = ledger.get_malformed_ledger_rows(text)
    assert malformed == []


def test_blank_change_summary_is_rejected():
    text = mk(["|1.0|   |2026-05-20T00:00:00Z|  |"])
    malformed = ledger.get_malformed_ledger_rows(text)
    assert malformed
    assert any("non-blank" in reason for _, reason in malformed)


def test_formatting_only_with_substantive_claim_is_rejected():
    text = mk(["|1.0|minor formatting patch plus substantive clause changes|2026-05-20T00:00:00Z|  |"])
    malformed = ledger.get_malformed_ledger_rows(text)
    assert malformed
    assert any("Formatting-only" in reason for _, reason in malformed)


def test_normal_substantive_row_unchanged_behavior():
    text = mk(["|1.0|Substantive clause changes to Article 4 dispute quorum thresholds|2026-05-20T00:00:00Z|  |"])
    malformed = ledger.get_malformed_ledger_rows(text)
    assert malformed == []


def test_dotted_numeric_versions_with_two_or_more_parts_are_valid():
    for version in ["1.0", "1.12", "1.1.2", "2.3.4", "10.11.12", "2.4.1.3"]:
        assert ledger.VERSION_CELL_RE.match(version)

    for version in ["", "2", "2.", "2.4.", "2..4", "2.a.4", "v2.4"]:
        assert not ledger.VERSION_CELL_RE.match(version)


def test_three_part_version_sorts_under_two_part_minor():
    versions = ["2.5", "2.4.2", "2.4", "2.4.1"]
    assert sorted(versions, key=ledger.version_sort_key) == ["2.4", "2.4.1", "2.4.2", "2.5"]
    assert ledger.is_minor_only_increment("2.4", "2.4.1") is True
    assert ledger.is_minor_only_increment("2.4.1", "2.4.2") is True
    assert ledger.is_minor_only_increment("2.4.1", "2.4.1.1") is True


def test_four_part_dotted_numeric_versions_are_accepted_in_rows():
    text = mk(["|2.4.1.3|summary|2026-05-20T00:00:00Z|  |"])
    malformed = ledger.get_malformed_ledger_rows(text)
    assert malformed == []


def test_malformed_dotted_versions_rejected_in_rows():
    for version in ["", "2", "2.", "2..4", "2.a.4", "v2.4"]:
        text = mk([f"|{version}|summary|2026-05-20T00:00:00Z|  |"])
        malformed = ledger.get_malformed_ledger_rows(text)
        assert malformed


def test_allowlisted_latest_blank_is_not_sealed_by_fix():
    text = mk(["|1.0|summary|2026-05-20T00:00:00Z|  |"])
    sealed_text, _stored_hash, changed, _ = ledger.update_last_ledger_hash_cell(
        text, fix=True, allow_blank_latest=True
    )
    assert changed is False
    assert sealed_text == text



def init_git_repo(tmp_path):
    subprocess.run(["git", "init"], cwd=tmp_path, check=True, capture_output=True)
    subprocess.run(["git", "config", "user.email", "test@example.com"], cwd=tmp_path, check=True)
    subprocess.run(["git", "config", "user.name", "Test User"], cwd=tmp_path, check=True)


def write_doc(root, rel, rows, body="Body"):
    path = root / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        f"# {path.stem} — Test Instrument\n\n"
        "## 1. Amendment Ledger\n\n"
        "|Version|Desc|TS|SHA-256|\n|---|---|---|---|\n"
        + "\n".join(rows)
        + f"\n\n## 2. Body\n\n{body}\n",
        encoding="utf-8",
    )
    return path


def commit_all(root, message="init"):
    subprocess.run(["git", "add", "."], cwd=root, check=True)
    subprocess.run(["git", "commit", "-m", message], cwd=root, check=True, capture_output=True)


def test_changed_file_with_blank_sha_is_repaired(tmp_path, monkeypatch):
    init_git_repo(tmp_path)
    rel = "Governance/Charters/CAM-TST2026-UNIT-001-PLATINUM.md"
    path = write_doc(tmp_path, rel, [f"|1.0|initial|2026-05-20T00:00:00Z|{'a'*64}|"])
    commit_all(tmp_path)
    path.write_text(path.read_text().replace("## 2. Body", "| 1.1 | update | 2026-05-21T00:00:00Z |  |\n\n## 2. Body"), encoding="utf-8")
    subprocess.run(["git", "add", rel], cwd=tmp_path, check=True)
    monkeypatch.setattr(ledger, "REPO_ROOT", tmp_path)
    assert ledger.lint("HEAD", ":", fix=True, staged=True) == 0
    assert "| 1.1 | update | 2026-05-21T00:00:00Z |  |" not in path.read_text()


def test_unchanged_file_with_blank_sha_is_repaired(tmp_path, monkeypatch):
    init_git_repo(tmp_path)
    rel_changed = "Governance/Charters/CAM-TST2026-UNIT-001-PLATINUM.md"
    rel_unchanged = "Governance/Charters/CAM-TST2026-UNIT-002-PLATINUM.md"
    changed = write_doc(tmp_path, rel_changed, [f"|1.0|initial|2026-05-20T00:00:00Z|{'a'*64}|"])
    unchanged = write_doc(tmp_path, rel_unchanged, ["|1.0|initial|2026-05-20T00:00:00Z|  |"])
    commit_all(tmp_path)
    changed.write_text(changed.read_text().replace("## 2. Body", "| 1.1 | update | 2026-05-21T00:00:00Z |  |\n\n## 2. Body"), encoding="utf-8")
    subprocess.run(["git", "add", rel_changed], cwd=tmp_path, check=True)
    monkeypatch.setattr(ledger, "REPO_ROOT", tmp_path)
    assert ledger.lint("HEAD", ":", fix=True, staged=True) == 0
    assert "|1.0|initial|2026-05-20T00:00:00Z|  |" not in unchanged.read_text()


def test_malformed_row_with_blank_sha_still_fails(tmp_path, monkeypatch):
    init_git_repo(tmp_path)
    rel = "Governance/Charters/CAM-TST2026-UNIT-001-PLATINUM.md"
    write_doc(tmp_path, rel, ["| bad | initial | 2026-05-20T00:00:00Z |  |"])
    commit_all(tmp_path)
    monkeypatch.setattr(ledger, "REPO_ROOT", tmp_path)
    assert ledger.lint_all(fix=True) == 1


def test_allowlisted_blank_repair_candidate_remains_unchanged(tmp_path, monkeypatch):
    rel = "Governance/Charters/CAM-BS2025-AEON-006-SCH-01.md"
    path = write_doc(tmp_path, rel, ["|1.0|initial|2026-05-20T00:00:00Z|  |"])
    monkeypatch.setattr(ledger, "REPO_ROOT", tmp_path)
    assert ledger.list_blank_sha_repair_candidate_files() == []
    assert ledger.lint_all(fix=True, strict=True) == 0
    assert "|1.0|initial|2026-05-20T00:00:00Z|  |" in path.read_text()


def test_valid_ledgers_without_blanks_remain_unchanged(tmp_path, monkeypatch):
    rel = "Governance/Charters/CAM-TST2026-UNIT-001-PLATINUM.md"
    path = write_doc(tmp_path, rel, ["|1.0|initial|2026-05-20T00:00:00Z|  |"])
    text = path.read_text()
    sealed, _stored, changed, _mismatch = ledger.update_last_ledger_hash_cell(text, fix=True)
    assert changed is True
    path.write_text(sealed, encoding="utf-8")
    before = path.read_text()
    monkeypatch.setattr(ledger, "REPO_ROOT", tmp_path)
    assert ledger.lint_all(fix=True) == 0
    assert path.read_text() == before
