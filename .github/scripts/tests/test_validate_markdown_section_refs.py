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
