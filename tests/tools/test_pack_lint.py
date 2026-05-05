from __future__ import annotations

import json
import subprocess
import sys
import textwrap
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
PACK_LINT = ROOT / "tools" / "pack_lint.py"


def run_pack_lint(*args: str, cwd: Path | None = None) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(PACK_LINT), *args],
        cwd=cwd or ROOT,
        check=False,
        capture_output=True,
        text=True,
    )


def write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(textwrap.dedent(content).lstrip(), encoding="utf-8")


def make_pack_files(pack_dir: Path, *, readme_line: str, self_audit_line: str, dispatch_name: str, dispatch_body: str) -> None:
    write_text(
        pack_dir / "README.md",
        f"""
        # Example Pack

        {readme_line}
        """,
    )
    write_text(
        pack_dir / "self-audit-report.md",
        f"""
        # Self Audit

        {self_audit_line}
        """,
    )
    write_text(
        pack_dir / "scoutflow-doc3-amend-pr76-pr125-worklist-2026-05-05.md",
        """
        # Amend Doc
        """,
    )
    write_text(pack_dir / dispatch_name, dispatch_body)


def test_pack_lint_reports_core_p1_findings(tmp_path: Path) -> None:
    pack_dir = tmp_path / "pack"
    make_pack_files(
        pack_dir,
        readme_line="This package contains 1 dispatch markdown file.",
        self_audit_line="- 1 dispatch markdown file.",
        dispatch_name="PR76-T-P1A-051-example.md",
        dispatch_body="""
        ---
        dispatch_id: T-P1A-051
        pr_number: 'PR #76'
        title: Example
        type: docs
        lane: research
        suggested_branch: task/T-P1A-051-example
        prior_pr_required: 'PR #75 / T-P1A-050 merged + PRD-v2.1 promoted'
        current_main_head_at_drafting_time: deadbeef
        ---

        ## allowed_paths

          - apps/capture-station/package.json

        ## forbidden_paths

          - apps/**
          - data/**

        ## 执行步骤

        ```bash
        test -f scoutflow-doc3-amend-pr76-pr125-worklist-2026-05-05.md
        ! git status --short --porcelain | grep -E "(^..[[:space:]]+| -> )(apps/|data/)"
        ```
        """,
    )

    result = run_pack_lint(str(pack_dir), "--origin-main-sha", "a5e65ef", "--output", "json", "--severity", "p1")

    assert result.returncode == 1, result.stdout
    payload = json.loads(result.stdout)
    rule_ids = {finding["rule_id"] for finding in payload["findings"]}
    assert "pack-lint/baseline-freshness" in rule_ids
    assert "pack-lint/amend-file-relative-path" in rule_ids
    assert "pack-lint/forbid-require-collision" in rule_ids
    assert "pack-lint/authority-gate-unreachable" in rule_ids


def test_pack_lint_accepts_patched_dispatch_for_p1(tmp_path: Path) -> None:
    pack_dir = tmp_path / "pack"
    amend_path = pack_dir / "scoutflow-doc3-amend-pr76-pr125-worklist-2026-05-05.md"
    make_pack_files(
        pack_dir,
        readme_line="This package contains 1 dispatch markdown file.",
        self_audit_line="- 1 dispatch markdown file.",
        dispatch_name="PR97-T-P1A-072-wave-4-ledger-open.md",
        dispatch_body=f"""
        ---
        dispatch_id: T-P1A-072
        pr_number: 'PR #97'
        title: Wave 4 Ledger Open
        type: docs
        lane: authority
        suggested_branch: task/T-P1A-072-wave-4-ledger-open
        prior_pr_required: 'PR #96 / T-P1A-071 merged'
        manual_gates_required:
          - PRD-v2.1 amendment promoted — manual gate
          - Verification command before stage: 'rg -n "PRD-v2.1|SRD-v3" docs/specs/contracts-index.md' must show entries
        current_main_head_at_drafting_time: deadbeef
          # actual_origin_main_at_audit_time: a5e65ef
        ---

        ## Audit-time drift note (2026-05-05)

        - Commander must use actual origin/main hash as EXPECTED_BASELINE.

        ## allowed_paths

          - docs/current.md

        ## forbidden_paths

          - apps/**
          - services/**

        ## 执行步骤

        ```bash
        test -f {amend_path}
        ! git status --short --porcelain | grep -E "(^..[[:space:]]+| -> )(apps/|services/)"
        ```
        """,
    )

    result = run_pack_lint(str(pack_dir), "--origin-main-sha", "a5e65ef", "--output", "json", "--severity", "p1")

    assert result.returncode == 0, result.stdout
    payload = json.loads(result.stdout)
    assert payload["summary"]["p1_findings"] == 0


def test_pack_lint_reports_duplicate_slot_and_inventory_mismatch(tmp_path: Path) -> None:
    pack_dir = tmp_path / "pack"
    base_dispatch = """
        ---
        dispatch_id: T-P1A-051
        pr_number: 'PR #76'
        title: Example
        type: docs
        lane: research
        suggested_branch: task/T-P1A-051-example
        prior_pr_required: 'PR #75 merged'
        current_main_head_at_drafting_time: a5e65ef
        ---

        ## allowed_paths

          - docs/example.md

        ## forbidden_paths

          - data/**
        """
    make_pack_files(
        pack_dir,
        readme_line="This package contains 1 dispatch markdown file.",
        self_audit_line="- 1 dispatch markdown file.",
        dispatch_name="PR76-T-P1A-051-example.md",
        dispatch_body=base_dispatch,
    )
    write_text(pack_dir / "PR76-T-P1A-051-example_副本.md", base_dispatch)

    result = run_pack_lint(str(pack_dir), "--origin-main-sha", "a5e65ef", "--output", "json", "--severity", "p2")

    assert result.returncode == 1, result.stdout
    payload = json.loads(result.stdout)
    rule_ids = {finding["rule_id"] for finding in payload["findings"]}
    assert "pack-lint/duplicate-dispatch-slot" in rule_ids
    assert "pack-lint/inventory-count-mismatch" in rule_ids


def test_pack_lint_severity_filter_ignores_p2_when_p1_requested(tmp_path: Path) -> None:
    pack_dir = tmp_path / "pack"
    make_pack_files(
        pack_dir,
        readme_line="This package contains 1 dispatch markdown file.",
        self_audit_line="- 1 dispatch markdown file.",
        dispatch_name="PR76-T-P1A-051-example.md",
        dispatch_body="""
        ---
        dispatch_id: T-P1A-051
        pr_number: 'PR #76'
        title: Example
        type: docs
        lane: research
        suggested_branch: task/T-P1A-051-example
        prior_pr_required: 'PR #75 merged'
        current_main_head_at_drafting_time: a5e65ef
        ---

        ## allowed_paths

          - docs/example.md

        ## forbidden_paths

          - apps/** (exception: docs/example.md is fine)
        """,
    )

    p1_result = run_pack_lint(str(pack_dir), "--origin-main-sha", "a5e65ef", "--output", "json", "--severity", "p1")
    p2_result = run_pack_lint(str(pack_dir), "--origin-main-sha", "a5e65ef", "--output", "json", "--severity", "p2")

    assert p1_result.returncode == 0, p1_result.stdout
    assert p2_result.returncode == 1, p2_result.stdout
    p2_payload = json.loads(p2_result.stdout)
    assert any(finding["rule_id"] == "pack-lint/inline-exception-in-forbidden" for finding in p2_payload["findings"])
