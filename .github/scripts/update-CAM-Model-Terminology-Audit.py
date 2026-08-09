#!/usr/bin/env python3
"""Rebuild the model-terminology audit and its generated registry summary."""

from __future__ import annotations

import importlib.util
from pathlib import Path


SCRIPT_DIR = Path(__file__).resolve().parent
REGISTRY_GENERATOR = SCRIPT_DIR / "update-CAM-Constitutional-Schedule-Registry.py"

spec = importlib.util.spec_from_file_location("constitutional_schedule_registry", REGISTRY_GENERATOR)
if spec is None or spec.loader is None:
    raise RuntimeError(f"Unable to load registry helper: {REGISTRY_GENERATOR}")
registry = importlib.util.module_from_spec(spec)
spec.loader.exec_module(registry)


def main() -> None:
    rows = registry.build_model_terminology_rows()
    registry.update_model_terminology_block(registry.render_model_terminology_summary(rows))
    registry.write_model_terminology_audit(registry.render_model_terminology_register(rows))
    print(f"Updated: {registry.MODEL_AUDIT_PATH.relative_to(registry.REPO_ROOT)}")


if __name__ == "__main__":
    main()
