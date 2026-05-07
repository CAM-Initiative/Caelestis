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
    assert f.status == "ambiguous_named_instrument_reference"
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
    assert f.reference_class == "cross_document"
    assert f.status == "ignored_amendment_register_reference"


def test_non_amendment_section_failures_still_fail(tmp_path):
    src = tmp_path / "Governance" / "CAM-EQ2026-FOO-001.md"
    w(src, "## Core\nReference §99.9\n")
    findings = validator.run(tmp_path / "Governance")
    assert findings[0].status == "fail_local"
