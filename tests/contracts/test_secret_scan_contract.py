from __future__ import annotations

import importlib.util
from pathlib import Path
import sys
from types import ModuleType


ROOT = Path(__file__).resolve().parents[2]


def load_secret_scan_module() -> ModuleType:
    module_path = ROOT / "tools" / "check-secrets-redlines.py"
    spec = importlib.util.spec_from_file_location("check_secrets_redlines", module_path)
    assert spec is not None
    assert spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def test_secret_scan_passes_definition_docs() -> None:
    scanner = load_secret_scan_module()

    findings = scanner.find_secret_redlines(
        ROOT,
        tracked_paths=[
            "docs/specs/raw-response-redaction.md",
            "tools/check-secrets-redlines.py",
        ],
    )

    assert findings == []


def test_secret_scan_fails_tracked_like_secret_file_without_printing_value(tmp_path: Path) -> None:
    scanner = load_secret_scan_module()
    fixture = tmp_path / "leak.log"
    secret_value = "fake-session-value"
    fixture.write_text(
        "Cookie" + ": " + "SESS" + "DATA=" + secret_value + "; " + "bili" + "_jct=fake-csrf\n",
        encoding="utf-8",
    )

    findings = scanner.find_secret_redlines(tmp_path, tracked_paths=["leak.log"])

    assert len(findings) == 1
    assert findings[0].path == "leak.log"
    assert findings[0].line_number == 1
    assert secret_value not in findings[0].redacted_excerpt
    assert "fake-csrf" not in findings[0].redacted_excerpt
    assert "[REDACTED]" in findings[0].redacted_excerpt
