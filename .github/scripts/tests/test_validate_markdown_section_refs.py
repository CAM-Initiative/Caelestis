import pathlib
import importlib.util

spec = importlib.util.spec_from_file_location("validator", pathlib.Path(__file__).resolve().parents[1] / "validate_markdown_section_refs.py")
validator = importlib.util.module_from_spec(spec)
spec.loader.exec_module(validator)


def w(p, text):
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(text)


def test_local_pass(tmp_path):
    f = tmp_path / "Governance" / "A.md"
    w(f, "## 5. Scope\nSee §5\n")
    findings = validator.run(tmp_path / "Governance")
    assert findings[0].status == "pass_local"


def test_local_fail_closest(tmp_path):
    f = tmp_path / "Governance" / "A.md"
    w(f, "## 5.4 Scope\nSee §5.9\n")
    findings = validator.run(tmp_path / "Governance")
    assert findings[0].status == "fail_local"
    assert findings[0].closest_section.startswith("5.4")


def test_cross_document_pass(tmp_path):
    src = tmp_path / "Governance" / "SRC.md"
    tgt = tmp_path / "Governance" / "CAM-BS2025-AEON-003-PLATINUM.md"
    w(src, "See §3 CAM-BS2025-AEON-003-PLATINUM\n")
    w(tgt, "## 3. Temporal Attribution Framework\n")
    findings = validator.run(tmp_path / "Governance")
    f = [x for x in findings if x.file_path.endswith("SRC.md")][0]
    assert f.status == "pass_cross_document"


def test_cross_document_target_missing(tmp_path):
    src = tmp_path / "Governance" / "SRC.md"
    w(src, "See §3 CAM-UNKNOWN-999\n")
    findings = validator.run(tmp_path / "Governance")
    assert findings[0].status == "fail_cross_document_target_missing"


def test_cross_document_section_missing(tmp_path):
    src = tmp_path / "Governance" / "SRC.md"
    tgt = tmp_path / "Governance" / "CAM-BS2025-AEON-003-PLATINUM.md"
    w(src, "See §3 CAM-BS2025-AEON-003-PLATINUM\n")
    w(tgt, "## 4. Other\n")
    findings = validator.run(tmp_path / "Governance")
    f = [x for x in findings if x.file_path.endswith("SRC.md")][0]
    assert f.status == "fail_cross_document_section_missing"


def test_cross_document_doc_before_section_binds_correctly(tmp_path):
    src = tmp_path / "Governance" / "SRC.md"
    tgt = tmp_path / "Governance" / "CAM-BS2025-AEON-003-SCH-02.md"
    other = tmp_path / "Governance" / "CAM-BS2025-AEON-001-SCH-01.md"
    w(src, "as defined in CAM-BS2025-AEON-003-SCH-02 §13.1, subject to CAM-BS2025-AEON-001-SCH-01\n")
    w(tgt, "## 13.1 Execution Boundary Evaluation\n")
    w(other, "## 3.1 Something Else\n")
    findings = validator.run(tmp_path / "Governance")
    f = [x for x in findings if x.file_path.endswith("SRC.md")][0]
    assert f.status == "pass_cross_document"
    assert f.target_document == "CAM-BS2025-AEON-003-SCH-02"


def test_ambiguous_named_instrument_reference_appendix(tmp_path):
    src = tmp_path / "Governance" / "CAM-EQ2026-FOO-001.md"
    w(src, "Systems MAY utilise interpretive heuristic frameworks (Appendix F §5.9).\n")
    findings = validator.run(tmp_path / "Governance")
    f = findings[0]
    assert f.status == "fail_short_document_reference"
    assert f.target_document.endswith(":Appendix F")


def test_named_instrument_with_explicit_doc_is_cross_document(tmp_path):
    src = tmp_path / "Governance" / "SRC.md"
    tgt = tmp_path / "Governance" / "CAM-EQ2026-ECONOMICS-007-PLATINUM.md"
    w(src, "(CAM-EQ2026-ECONOMICS-007-PLATINUM §5.9 — Appendix F)\n")
    w(tgt, "## 5.9 Reciprocity Sufficiency Test\n")
    findings = validator.run(tmp_path / "Governance")
    f = [x for x in findings if x.file_path.endswith("SRC.md")][0]
    assert f.status == "pass_cross_document"


def test_cross_doc_direct_doc_before_section(tmp_path):
    src = tmp_path / "Governance" / "SRC.md"
    tgt = tmp_path / "Governance" / "CAM-EQ2026-IDENTITY-001-PLATINUM.md"
    w(src, "CAM-EQ2026-IDENTITY-001-PLATINUM §6.3\n")
    w(tgt, "## 6.3 Identity Gradient Input Constraint\n")
    findings = validator.run(tmp_path / "Governance")
    f = [x for x in findings if x.file_path.endswith("SRC.md")][0]
    assert f.reference_class == "cross_document"
    assert f.target_document == "CAM-EQ2026-IDENTITY-001-PLATINUM"
    assert f.reference == "§6.3"
    assert f.status == "pass_cross_document"


def test_cross_doc_full_title_doc_before_section(tmp_path):
    src = tmp_path / "Governance" / "SRC.md"
    tgt = tmp_path / "Governance" / "CAM-EQ2026-IDENTITY-001-PLATINUM.md"
    w(src, "CAM-EQ2026-IDENTITY-001-PLATINUM — Identity Domain Charter §6.3\n")
    w(tgt, "## 6.3 Identity Gradient Input Constraint\n")
    findings = validator.run(tmp_path / "Governance")
    f = [x for x in findings if x.file_path.endswith("SRC.md")][0]
    assert f.reference_class == "cross_document"
    assert f.target_document == "CAM-EQ2026-IDENTITY-001-PLATINUM"
    assert f.reference == "§6.3"
    assert f.status == "pass_cross_document"


def test_cross_doc_appendix_title_form(tmp_path):
    src = tmp_path / "Governance" / "SRC.md"
    tgt = tmp_path / "Governance" / "CAM-EQ2026-ECONOMICS-007-PLATINUM.md"
    w(src, "CAM-EQ2026-ECONOMICS-007-PLATINUM — Appendix F §5.9\n")
    w(tgt, "## 5.9 Reciprocity Sufficiency Test\n")
    findings = validator.run(tmp_path / "Governance")
    f = [x for x in findings if x.file_path.endswith("SRC.md")][0]
    assert f.reference_class == "cross_document"
    assert f.target_document == "CAM-EQ2026-ECONOMICS-007-PLATINUM"
    assert f.status == "pass_cross_document"


def test_cross_doc_schedule_title_form(tmp_path):
    src = tmp_path / "Governance" / "SRC.md"
    tgt = tmp_path / "Governance" / "CAM-BS2025-AEON-003-SCH-02.md"
    w(src, "CAM-BS2025-AEON-003-SCH-02 — Annex B: Runtime Governance Execution Model §13.1\n")
    w(tgt, "## 13.1 Execution Boundary Evaluation\n")
    findings = validator.run(tmp_path / "Governance")
    f = [x for x in findings if x.file_path.endswith("SRC.md")][0]
    assert f.reference_class == "cross_document"
    assert f.target_document == "CAM-BS2025-AEON-003-SCH-02"
    assert f.status == "pass_cross_document"


def test_cross_doc_does_not_overbind_across_another_doc_id(tmp_path):
    src = tmp_path / "Governance" / "SRC.md"
    cam_a = tmp_path / "Governance" / "CAM-A-001.md"
    cam_b = tmp_path / "Governance" / "CAM-B-001.md"
    w(src, "CAM-A-001 — Title CAM-B-001 — Other Title §3.1\n")
    w(cam_a, "## 9.9 Not Targeted\n")
    w(cam_b, "## 3.1 Correct Target\n")
    findings = validator.run(tmp_path / "Governance")
    f = [x for x in findings if x.file_path.endswith("SRC.md")][0]
    assert f.reference_class == "cross_document"
    assert f.target_document == "CAM-B-001"
    assert f.status == "pass_cross_document"


def test_amendment_register_local_failure_is_ignored(tmp_path):
    src = tmp_path / "Governance" / "CAM-EQ2026-FOO-001.md"
    w(src, "## 1. Main\nSee §1\n## Amendment Register\nHistorical reference §99.9\n")
    findings = validator.run(tmp_path / "Governance")
    ignored = [x for x in findings if x.reference == "§99.9"][0]
    assert ignored.status == "ignored_amendment_register_reference"


def test_amendment_history_cross_document_failure_is_ignored(tmp_path):
    src = tmp_path / "Governance" / "SRC.md"
    w(src, "## Amendment History\nLegacy mapping §3 CAM-UNKNOWN-999\n")
    findings = validator.run(tmp_path / "Governance")
    f = findings[0]
    assert f.reference_class == "ignored"
    assert f.status == "ignored_amendment_register_reference"


def test_non_amendment_section_failures_still_fail(tmp_path):
    src = tmp_path / "Governance" / "CAM-EQ2026-FOO-001.md"
    w(src, "## Core\nReference §99.9\n")
    findings = validator.run(tmp_path / "Governance")
    assert findings[0].status == "fail_local"


def test_amendment_ledger_heading_marks_region_as_ignored(tmp_path):
    src = tmp_path / "Governance" / "CAM-EQ2026-ECONOMICS-004-PLATINUM.md"
    w(src, "## 18.4 Amendment Ledger\n| Version | Description |\n| --- | --- |\n| 1.2 | Canonicalized (§5.9). |\n## 18.5 Binding Seal\n")
    findings = validator.run(tmp_path / "Governance")
    f = [x for x in findings if x.reference == "§5.9"][0]
    assert f.status == "ignored_amendment_register_reference"


def test_manual_review_statuses_are_non_blocking_sets():
    assert "manual_review_required" in validator.MANUAL_REVIEW_STATUSES
    assert "manual_review_required" not in validator.BLOCKING_STATUSES


def _run_main(monkeypatch, capsys, tmp_path, content, *args):
    root = tmp_path / "Governance"
    for rel, text in content.items():
        w(root / rel, text)
    monkeypatch.setattr("sys.argv", ["validate_markdown_section_refs.py", "--root", str(root), *args])
    code = validator.main()
    out = capsys.readouterr().out
    return code, out


def test_default_output_hides_pass_local(monkeypatch, capsys, tmp_path):
    code, out = _run_main(monkeypatch, capsys, tmp_path, {"A.md": "## 5. Scope\nSee §5\n"})
    assert code == 0
    assert "pass_local" not in out


def test_default_output_hides_pass_cross_document(monkeypatch, capsys, tmp_path):
    code, out = _run_main(monkeypatch, capsys, tmp_path, {
        "SRC.md": "See §3 CAM-BS2025-AEON-003-PLATINUM\n",
        "CAM-BS2025-AEON-003-PLATINUM.md": "## 3. Temporal Attribution Framework\n",
    })
    assert code == 0
    assert "pass_cross_document" not in out


def test_default_output_shows_fail_statuses(monkeypatch, capsys, tmp_path):
    code, out = _run_main(monkeypatch, capsys, tmp_path, {"A.md": "## 1. Scope\nSee §9\n"})
    assert code == 1
    assert "fail_local" in out


def test_default_output_shows_manual_review_statuses(monkeypatch, capsys, tmp_path):
    code, out = _run_main(monkeypatch, capsys, tmp_path, {"A.md": "See Appendix F §5.9\n"})
    assert code == 1
    assert "fail_short_document_reference" in out


def test_default_output_hides_ignored_amendment_register_statuses(monkeypatch, capsys, tmp_path):
    code, out = _run_main(monkeypatch, capsys, tmp_path, {"A.md": "## Amendment Register\nLegacy reference §9.9\n"})
    assert code == 0
    assert "ignored_amendment_register_reference" not in out
    assert "SUPPRESSED_IGNORED_ROWS=1" in out


def test_show_passes_flag_restores_full_output(monkeypatch, capsys, tmp_path):
    code, out = _run_main(monkeypatch, capsys, tmp_path, {"A.md": "## 5. Scope\nSee §5\n"}, "--show-passes")
    assert code == 0
    assert "pass_local" in out


def test_exit_code_zero_when_only_manual_and_ignored(monkeypatch, capsys, tmp_path):
    code, out = _run_main(monkeypatch, capsys, tmp_path, {
        "A.md": "See Appendix F §5.9\n## Amendment Register\nLegacy reference §9.9\n",
    })
    assert "fail_short_document_reference" in out
    assert "SUPPRESSED_IGNORED_ROWS=1" in out
    assert code == 1


def test_exit_code_one_when_fail_exists(monkeypatch, capsys, tmp_path):
    code, out = _run_main(monkeypatch, capsys, tmp_path, {
        "A.md": "## Amendment Register\nLegacy reference §9.9\n## Core\nSee §9\n",
    })
    assert "fail_local" in out
    assert code == 1


def test_cross_doc_cam_direct_variants(tmp_path):
    src = tmp_path / "Governance" / "SRC.md"
    tgt = tmp_path / "Governance" / "CAM-EQ2026-OPERATIONS-004-PLATINUM.md"
    w(tgt, "## 8.6 Harm Escalation Thresholds — Operational Application of HC Scale\n")
    for line in [
        "CAM-EQ2026-OPERATIONS-004-PLATINUM §8.6",
        "CAM-EQ2026-OPERATIONS-004-PLATINUM: §8.6",
        "CAM-EQ2026-OPERATIONS-004-PLATINUM, §8.6",
        "CAM-EQ2026-OPERATIONS-004-PLATINUM.md §8.6",
    ]:
        w(src, line+"\n")
        f = validator.run(tmp_path / "Governance")[0]
        assert f.status == "pass_cross_document"


def test_annex_forms_and_placeholder(tmp_path):
    src = tmp_path / "Governance" / "SRC.md"
    tgt = tmp_path / "Governance" / "CAM-BS2025-AEON-004-PLATINUM.md"
    w(tgt, "## 1.2 Any\n")
    w(src, "CAM-BS2025-AEON-004-PLATINUM - Annex A §1.2\n")
    assert validator.run(tmp_path / "Governance")[0].status == "pass_cross_document"
    w(src, "CAM-BS2025-AEON-004-PLATINUM: Annex A\n")
    assert validator.run(tmp_path / "Governance") == []
    w(src, "CAM-BS2025-AEON-004-PLATINUM: Annex [x] §1.2\n")
    assert validator.run(tmp_path / "Governance")[0].status == "manual_review_required"


def test_short_named_references_are_blocking(tmp_path):
    src = tmp_path / "Governance" / "SRC.md"
    for text in ["Annex B §14.3.1", "Appendix Y §6.2", "Schedule 2 §13.8", "RELATION-001 §5.4", "AEON-003 §14.3.1"]:
        w(src, text + "\n")
        finding = validator.run(tmp_path / "Governance")[0]
        assert finding.status == "fail_short_document_reference"


def test_full_cam_references_with_variants_are_accepted(tmp_path):
    src = tmp_path / "Governance" / "SRC.md"
    tgt = tmp_path / "Governance" / "CAM-EQ2026-RELATION-001-PLATINUM.md"
    w(tgt, "## 5.4 X\n")
    for text in [
        "CAM-EQ2026-RELATION-001-PLATINUM §5.4",
        "CAM-EQ2026-RELATION-001-PLATINUM, §5.4",
        "CAM-EQ2026-RELATION-001-PLATINUM — Annex/Title, §5.4",
    ]:
        w(src, text + "\n")
        assert validator.run(tmp_path / "Governance")[0].status == "pass_cross_document"


def test_default_output_hides_ignored(monkeypatch, capsys, tmp_path):
    code, out = _run_main(monkeypatch, capsys, tmp_path, {"A.md": "## Amendment Register\nLegacy reference §9.9\n"})
    assert code == 0
    assert "ignored_amendment_register_reference" not in out
    assert "SUPPRESSED_IGNORED_ROWS=1" in out
