from __future__ import annotations

import importlib.util
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
CHECKER_PATH = ROOT / "tools" / "check-docs-redlines.py"


def load_checker():
    spec = importlib.util.spec_from_file_location("check_docs_redlines", CHECKER_PATH)
    assert spec is not None
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def test_app_diff_guard_ignores_existing_app_tree_without_app_diff(tmp_path: Path) -> None:
    checker = load_checker()
    failures: list[str] = []

    checker.check_app_diff_scope_guard(
        tmp_path,
        ["apps/capture-station/index.html"],
        failures,
        changed_paths=["tools/check-docs-redlines.py"],
    )

    assert failures == []


def test_app_diff_guard_requires_scope_note_for_known_app_surface(tmp_path: Path) -> None:
    checker = load_checker()
    failures: list[str] = []

    checker.check_app_diff_scope_guard(
        tmp_path,
        [],
        failures,
        changed_paths=["apps/capture-station/src/App.tsx"],
    )

    assert len(failures) == 1
    assert "apps/capture-station/src/App.tsx" in failures[0]


def test_app_diff_guard_allows_known_app_surface_when_exact_path_is_named(tmp_path: Path) -> None:
    checker = load_checker()
    note = tmp_path / "docs/research/repairs/capture-station-scope-2026-05-05.md"
    note.parent.mkdir(parents=True)
    note.write_text(
        "- allowed path: `apps/capture-station/src/App.tsx`\n",
        encoding="utf-8",
    )
    failures: list[str] = []

    checker.check_app_diff_scope_guard(
        tmp_path,
        ["docs/research/repairs/capture-station-scope-2026-05-05.md"],
        failures,
        changed_paths=["apps/capture-station/src/App.tsx"],
    )

    assert failures == []


def test_app_diff_guard_fails_unexplained_new_app_path(tmp_path: Path) -> None:
    checker = load_checker()
    failures: list[str] = []

    checker.check_app_diff_scope_guard(
        tmp_path,
        [],
        failures,
        changed_paths=["apps/new-station/src/App.tsx"],
    )

    assert len(failures) == 1
    assert "apps/new-station/src/App.tsx" in failures[0]
    assert "dispatch/repair" in failures[0]


def test_app_diff_guard_allows_exact_path_named_by_tracked_scope_note(tmp_path: Path) -> None:
    checker = load_checker()
    note = tmp_path / "docs/research/repairs/new-app-scope-2026-05-05.md"
    note.parent.mkdir(parents=True)
    note.write_text(
        "- allowed path: `apps/new-station/src/App.tsx`\n",
        encoding="utf-8",
    )
    failures: list[str] = []

    checker.check_app_diff_scope_guard(
        tmp_path,
        ["docs/research/repairs/new-app-scope-2026-05-05.md"],
        failures,
        changed_paths=["apps/new-station/src/App.tsx"],
    )

    assert failures == []


def test_app_diff_guard_requires_exact_path_marker(tmp_path: Path) -> None:
    checker = load_checker()
    note = tmp_path / "docs/research/repairs/new-app-scope-2026-05-05.md"
    note.parent.mkdir(parents=True)
    note.write_text(
        "- wrong path: `apps/new-station/src/App.tsx.bak`\n",
        encoding="utf-8",
    )
    failures: list[str] = []

    checker.check_app_diff_scope_guard(
        tmp_path,
        ["docs/research/repairs/new-app-scope-2026-05-05.md"],
        failures,
        changed_paths=["apps/new-station/src/App.tsx"],
    )

    assert len(failures) == 1
    assert "apps/new-station/src/App.tsx" in failures[0]


def test_changed_paths_falls_back_when_origin_main_diff_is_unavailable(monkeypatch) -> None:
    checker = load_checker()

    def fake_name_only(repo: Path, args: list[str]) -> list[str] | None:
        if args == ["origin/main...HEAD"]:
            return None
        if args == []:
            return ["apps/new-station/src/App.tsx"]
        if args == ["--cached"]:
            return ["tools/check-docs-redlines.py"]
        raise AssertionError(f"unexpected args: {args}")

    monkeypatch.setattr(checker, "run_git_name_only", fake_name_only)

    assert checker.run_git_changed_paths(Path("/tmp/repo")) == [
        "apps/new-station/src/App.tsx",
        "tools/check-docs-redlines.py",
    ]


def test_status_taxonomy_rejects_current_authority_outside_whitelist(tmp_path: Path) -> None:
    checker = load_checker()
    path = tmp_path / "docs/memory/INDEX.md"
    path.parent.mkdir(parents=True)
    path.write_text("---\nstatus: current authority\n---\n", encoding="utf-8")
    failures: list[str] = []

    checker.check_markdown_status_taxonomy(
        tmp_path,
        ["docs/memory/INDEX.md"],
        failures,
    )

    assert len(failures) == 1
    assert "docs/memory/INDEX.md" in failures[0]
    assert "current authority" in failures[0]


def test_status_taxonomy_full_scan_rejects_current_authority_outside_whitelist(tmp_path: Path) -> None:
    checker = load_checker()
    path = tmp_path / "docs/memory/INDEX.md"
    path.parent.mkdir(parents=True)
    path.write_text("---\nstatus: current authority\n---\n", encoding="utf-8")
    failures: list[str] = []

    checker.check_markdown_status_taxonomy(
        tmp_path,
        ["docs/memory/INDEX.md"],
        failures,
        changed_paths=[],
        full_scan=True,
    )

    assert len(failures) == 1
    assert "current authority" in failures[0]


def test_status_taxonomy_allows_whitelisted_current_authority_path(tmp_path: Path) -> None:
    checker = load_checker()
    path = tmp_path / "docs/current.md"
    path.parent.mkdir(parents=True)
    path.write_text("---\nstatus: current authority\n---\n", encoding="utf-8")
    failures: list[str] = []

    checker.check_markdown_status_taxonomy(
        tmp_path,
        ["docs/current.md"],
        failures,
    )

    assert failures == []


def test_status_taxonomy_allows_docs_memory_reference_storage(tmp_path: Path) -> None:
    checker = load_checker()
    path = tmp_path / "docs/memory/INDEX.md"
    path.parent.mkdir(parents=True)
    path.write_text("---\nstatus: reference storage\n---\n", encoding="utf-8")
    failures: list[str] = []

    checker.check_markdown_status_taxonomy(
        tmp_path,
        ["docs/memory/INDEX.md"],
        failures,
        changed_paths=[],
        full_scan=True,
    )

    assert failures == []


def test_status_taxonomy_allows_current_authority_whitelist_in_full_scan(tmp_path: Path) -> None:
    checker = load_checker()
    files = [
        "docs/current.md",
        "docs/task-index.md",
        "docs/decision-log.md",
        "docs/00-START-HERE.md",
    ]
    for rel in files:
        path = tmp_path / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("---\nstatus: current authority\n---\n", encoding="utf-8")
    failures: list[str] = []

    checker.check_markdown_status_taxonomy(
        tmp_path,
        files,
        failures,
        changed_paths=[],
        full_scan=True,
    )

    assert failures == []


def test_status_taxonomy_rejects_illegal_status_word_in_full_scan(tmp_path: Path) -> None:
    checker = load_checker()
    path = tmp_path / "docs/research/example.md"
    path.parent.mkdir(parents=True)
    path.write_text("---\nstatus: active\n---\n", encoding="utf-8")
    failures: list[str] = []

    checker.check_markdown_status_taxonomy(
        tmp_path,
        ["docs/research/example.md"],
        failures,
        changed_paths=[],
        full_scan=True,
    )

    assert len(failures) == 1
    assert "status 非法" in failures[0]


def test_status_taxonomy_full_scan_grandfathers_legacy_candidate_composites(tmp_path: Path) -> None:
    checker = load_checker()
    path = tmp_path / "docs/research/legacy.md"
    path.parent.mkdir(parents=True)
    path.write_text("---\nstatus: candidate / research-only / not-authority\n---\n", encoding="utf-8")
    failures: list[str] = []

    checker.check_markdown_status_taxonomy(
        tmp_path,
        ["docs/research/legacy.md"],
        failures,
        changed_paths=[],
        full_scan=True,
    )

    assert failures == []
