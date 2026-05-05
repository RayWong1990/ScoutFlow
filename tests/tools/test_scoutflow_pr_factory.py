from __future__ import annotations

import importlib.util
from pathlib import Path
from types import SimpleNamespace
import sys

import pytest


ROOT = Path(__file__).resolve().parents[2]
MODULE_PATH = ROOT / "tools" / "scoutflow_pr_factory.py"
SPEC = importlib.util.spec_from_file_location("scoutflow_pr_factory_for_tests", MODULE_PATH)
assert SPEC is not None
assert SPEC.loader is not None
pr_factory = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = pr_factory
SPEC.loader.exec_module(pr_factory)


@pytest.fixture
def repo_root(tmp_path: Path) -> Path:
    root = tmp_path / "ScoutFlow"
    (root / "docs").mkdir(parents=True)
    (root / "tools").mkdir()
    (root / ".gitignore").write_text("referencerepo/\n", encoding="utf-8")
    return root


def args(**overrides: str) -> SimpleNamespace:
    values = {
        "category": "xhs",
        "shoulder_id": "rednote-mcp",
        "upstream_url": "https://github.com/foo/bar.git",
        "github_user": "user",
        "default_branch": "main",
        "sync_cadence": "monthly",
        "shoulder_path": "referencerepo/xhs/rednote-mcp",
        "reason": "no-longer-needed",
    }
    values.update(overrides)
    return SimpleNamespace(**values)


def assert_runtime_error_mentions(label: str, value: str) -> None:
    with pytest.raises(RuntimeError) as excinfo:
        pr_factory.validate_path_segment(label, value)
    message = str(excinfo.value)
    assert label in message
    assert repr(value) in message


def test_segment_validation_accepts_single_segments() -> None:
    assert pr_factory.validate_path_segment("category", "xhs") == "xhs"
    assert pr_factory.validate_path_segment("shoulder_id", "rednote-mcp") == "rednote-mcp"


@pytest.mark.parametrize(
    "label,value",
    [
        ("category", ""),
        ("category", "."),
        ("category", ".."),
        ("category", "../docs"),
        ("category", "xhs/rednote"),
        ("category", "xhs\\rednote"),
        ("category", "/tmp/outside"),
        ("shoulder_id", "/tmp/outside"),
    ],
)
def test_segment_validation_rejects_escape_values(label: str, value: str) -> None:
    assert_runtime_error_mentions(label, value)


def test_fork_shoulder_normal_path_stays_under_referencerepo(repo_root: Path) -> None:
    steps = pr_factory.build_fork_steps(args(), repo_root)

    shoulder_dir = repo_root / "referencerepo" / "xhs" / "rednote-mcp"
    assert steps[0].command == ["mkdir", "-p", str((repo_root / "referencerepo" / "xhs").resolve())]
    assert steps[1].cwd == (repo_root / "referencerepo" / "xhs").resolve()
    assert steps[2].cwd == shoulder_dir.resolve()
    assert steps[-1].write_path == shoulder_dir.resolve() / "_SCOUTFLOW_FORK.local.md"


@pytest.mark.parametrize(
    "overrides",
    [
        {"category": "../docs"},
        {"category": "/tmp/scoutflow-outside"},
        {"shoulder_id": "../docs"},
        {"shoulder_id": "/tmp/scoutflow-outside"},
    ],
)
def test_fork_shoulder_rejects_segment_escapes(repo_root: Path, overrides: dict[str, str]) -> None:
    with pytest.raises(RuntimeError):
        pr_factory.build_fork_steps(args(**overrides), repo_root)


def test_sync_shoulder_accepts_existing_relative_path_under_referencerepo(repo_root: Path) -> None:
    shoulder_dir = repo_root / "referencerepo" / "xhs" / "rednote-mcp"
    shoulder_dir.mkdir(parents=True)

    steps = pr_factory.build_sync_steps(args(shoulder_path="referencerepo/xhs/rednote-mcp"), repo_root)

    assert all(step.cwd == shoulder_dir.resolve() for step in steps)


def test_sync_shoulder_accepts_existing_absolute_path_under_referencerepo(repo_root: Path) -> None:
    shoulder_dir = repo_root / "referencerepo" / "xhs" / "rednote-mcp"
    shoulder_dir.mkdir(parents=True)

    steps = pr_factory.build_sync_steps(args(shoulder_path=str(shoulder_dir)), repo_root)

    assert all(step.cwd == shoulder_dir.resolve() for step in steps)


@pytest.mark.parametrize(
    "shoulder_path",
    [
        "/tmp",
        "docs",
        "../docs",
        "{repo_docs}",
        "{repo_root}",
        "referencerepo",
    ],
)
def test_sync_shoulder_rejects_paths_outside_or_at_referencerepo_root(
    repo_root: Path, shoulder_path: str
) -> None:
    shoulder_path = shoulder_path.format(repo_docs=repo_root / "docs", repo_root=repo_root)

    with pytest.raises(RuntimeError):
        pr_factory.build_sync_steps(args(shoulder_path=shoulder_path), repo_root)


def test_archive_shoulder_normal_path_stays_under_referencerepo(repo_root: Path) -> None:
    source_dir = repo_root / "referencerepo" / "xhs" / "rednote-mcp"
    source_dir.mkdir(parents=True)

    steps = pr_factory.build_archive_steps(args(), repo_root)

    archive_dir = repo_root / "referencerepo" / "_archived" / "xhs" / "rednote-mcp"
    assert steps[1].command == ["mv", str(source_dir.resolve()), str(archive_dir.resolve())]
    assert steps[2].write_path == archive_dir.resolve() / "_SCOUTFLOW_ARCHIVE.local.md"


@pytest.mark.parametrize(
    "overrides",
    [
        {"category": "../docs"},
        {"shoulder_id": "../docs"},
        {"category": "/tmp/scoutflow-outside"},
        {"shoulder_id": "/tmp/scoutflow-outside"},
    ],
)
def test_archive_shoulder_rejects_segment_escapes(repo_root: Path, overrides: dict[str, str]) -> None:
    with pytest.raises(RuntimeError):
        pr_factory.build_archive_steps(args(**overrides), repo_root)


def test_parse_defaults_to_dry_run_and_execute_is_opt_in() -> None:
    default_args = pr_factory.parse_args(["sync-shoulder", "referencerepo/xhs/rednote-mcp"])
    execute_args = pr_factory.parse_args(["sync-shoulder", "--execute", "referencerepo/xhs/rednote-mcp"])
    dry_run_args = pr_factory.parse_args(
        ["fork-shoulder", "--dry-run", "rednote-mcp", "xhs", "https://github.com/foo/bar.git", "user"]
    )

    assert default_args.execute is False
    assert execute_args.execute is True
    assert dry_run_args.execute is False


def test_default_mode_does_not_execute_commands(
    repo_root: Path, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
) -> None:
    shoulder_dir = repo_root / "referencerepo" / "xhs" / "rednote-mcp"
    shoulder_dir.mkdir(parents=True)
    calls: list[list[str]] = []

    def fake_run(command: list[str], **_: object) -> object:
        calls.append(command)
        return object()

    monkeypatch.setattr(pr_factory.subprocess, "run", fake_run)

    result = pr_factory.main(["--workspace-root", str(repo_root), "sync-shoulder", str(shoulder_dir)])

    assert result == 0
    assert calls == []
    assert "[DRY RUN]" in capsys.readouterr().out


def test_execute_mode_runs_planned_commands(
    repo_root: Path, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
) -> None:
    shoulder_dir = repo_root / "referencerepo" / "xhs" / "rednote-mcp"
    shoulder_dir.mkdir(parents=True)
    calls: list[list[str]] = []

    def fake_run(command: list[str], **_: object) -> object:
        calls.append(command)
        return object()

    monkeypatch.setattr(pr_factory.subprocess, "run", fake_run)

    result = pr_factory.main(["--workspace-root", str(repo_root), "sync-shoulder", "--execute", str(shoulder_dir)])

    assert result == 0
    assert [command[:2] for command in calls] == [
        ["git", "fetch"],
        ["git", "checkout"],
        ["git", "log"],
        ["git", "log"],
        ["git", "diff"],
    ]
    assert "[EXECUTE]" in capsys.readouterr().out


def test_help_text_exposes_execute_flag(capsys: pytest.CaptureFixture[str]) -> None:
    with pytest.raises(SystemExit) as excinfo:
        pr_factory.parse_args(["sync-shoulder", "--help"])

    assert excinfo.value.code == 0
    help_text = capsys.readouterr().out
    assert "--execute" in help_text
    assert "--dry-run" in help_text
