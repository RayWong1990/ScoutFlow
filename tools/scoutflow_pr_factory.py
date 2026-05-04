#!/usr/bin/env python3
"""Local PR Factory helper for ScoutFlow shoulder operations."""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
import shlex
import shutil
import subprocess
import sys


DEFAULT_BRANCH = "main"
LOCAL_ONLY_ENTRY = "referencerepo/"


@dataclass(frozen=True)
class Step:
    description: str
    command: list[str] | None = None
    cwd: Path | None = None
    write_path: Path | None = None
    write_body: str | None = None


def utc_now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def repo_root(explicit_root: str | None) -> Path:
    if explicit_root:
        return Path(explicit_root).expanduser().resolve()
    return Path(__file__).resolve().parents[1]


def ensure_repo_layout(root: Path) -> None:
    if not (root / ".gitignore").is_file():
        raise RuntimeError(f"missing .gitignore at repo root: {root}")
    if not (root / "docs").is_dir() or not (root / "tools").is_dir():
        raise RuntimeError(f"unexpected ScoutFlow root layout: {root}")
    gitignore = (root / ".gitignore").read_text(encoding="utf-8")
    if LOCAL_ONLY_ENTRY not in gitignore.splitlines():
        raise RuntimeError("referencerepo/ is not declared as local-only in .gitignore")


def normalize_upstream_url(url: str) -> str:
    return url.rstrip("/").removesuffix(".git")


def repo_name_from_url(url: str) -> str:
    normalized = normalize_upstream_url(url)
    name = normalized.rsplit("/", 1)[-1]
    if ":" in name:
        name = name.rsplit(":", 1)[-1]
    if not name:
        raise RuntimeError(f"cannot derive repository name from URL: {url}")
    return name


def quote_command(command: list[str]) -> str:
    return shlex.join(command)


def print_steps(steps: list[Step], dry_run: bool) -> None:
    mode = "DRY RUN" if dry_run else "EXECUTE"
    print(f"[{mode}] planned steps:")
    for index, step in enumerate(steps, start=1):
        print(f"{index}. {step.description}")
        if step.command is not None:
            prefix = f"(cd {step.cwd} && " if step.cwd else ""
            suffix = ")" if step.cwd else ""
            print(f"   {prefix}{quote_command(step.command)}{suffix}")
        if step.write_path is not None:
            print(f"   write -> {step.write_path}")


def run_steps(steps: list[Step], dry_run: bool) -> None:
    print_steps(steps, dry_run=dry_run)
    if dry_run:
        return
    for step in steps:
        if step.command is not None:
            subprocess.run(step.command, cwd=step.cwd, check=True, text=True)
        if step.write_path is not None and step.write_body is not None:
            step.write_path.parent.mkdir(parents=True, exist_ok=True)
            step.write_path.write_text(step.write_body, encoding="utf-8")


def build_fork_steps(args: argparse.Namespace, root: Path) -> list[Step]:
    normalized_url = normalize_upstream_url(args.upstream_url)
    repo_name = repo_name_from_url(normalized_url)
    reference_dir = root / "referencerepo" / args.category
    shoulder_dir = reference_dir / args.shoulder_id
    fork_url = f"git@github.com:{args.github_user}/{repo_name}.git"

    if shoulder_dir.exists():
        raise RuntimeError(f"target shoulder path already exists: {shoulder_dir}")

    timestamp = utc_now()
    meta_body = (
        "---\n"
        f"shoulder_id: {args.shoulder_id}\n"
        f"category: {args.category}\n"
        f"upstream_url: {normalized_url}\n"
        f"fork_url: {fork_url}\n"
        f"forked_at: {timestamp}\n"
        f"sync_cadence: {args.sync_cadence}\n"
        "---\n"
    )
    fork_body = (
        f"# {args.shoulder_id} Fork Patch List\n\n"
        "## ScoutFlow local patches\n"
        "- TODO: record branch-local commits and why they exist.\n\n"
        "## Upstream sync history\n"
        f"- {timestamp}: initialized from `{normalized_url}`\n\n"
        "## Known conflict points\n"
        "- TODO: list files or modules that are likely to drift.\n"
    )

    return [
        Step("create reference category directory", command=["mkdir", "-p", str(reference_dir)]),
        Step(
            "clone upstream into local-only referencerepo",
            command=["git", "clone", "--depth", "1", normalized_url, args.shoulder_id],
            cwd=reference_dir,
        ),
        Step("rename origin to upstream", command=["git", "remote", "rename", "origin", "upstream"], cwd=shoulder_dir),
        Step("prepare GitHub fork without cloning again", command=["gh", "repo", "fork", normalized_url, "--clone=false"]),
        Step("add personal fork remote", command=["git", "remote", "add", "origin", fork_url], cwd=shoulder_dir),
        Step("fetch upstream branches", command=["git", "fetch", "upstream"], cwd=shoulder_dir),
        Step(
            "create scoutflow-fork branch from upstream default branch",
            command=["git", "checkout", "-b", "scoutflow-fork", f"upstream/{args.default_branch}"],
            cwd=shoulder_dir,
        ),
        Step("push scoutflow-fork branch", command=["git", "push", "-u", "origin", "scoutflow-fork"], cwd=shoulder_dir),
        Step("write local metadata file", write_path=shoulder_dir / "_SCOUTFLOW_META.local.md", write_body=meta_body),
        Step("write local fork ledger template", write_path=shoulder_dir / "_SCOUTFLOW_FORK.local.md", write_body=fork_body),
    ]


def build_sync_steps(args: argparse.Namespace, root: Path) -> list[Step]:
    shoulder_dir = Path(args.shoulder_path).expanduser()
    if not shoulder_dir.is_absolute():
        shoulder_dir = root / shoulder_dir
    shoulder_dir = shoulder_dir.resolve()
    if not shoulder_dir.exists():
        raise RuntimeError(f"shoulder path does not exist: {shoulder_dir}")
    return [
        Step("fetch upstream", command=["git", "fetch", "upstream"], cwd=shoulder_dir),
        Step("checkout scoutflow-fork", command=["git", "checkout", "scoutflow-fork"], cwd=shoulder_dir),
        Step("show local patch count", command=["git", "log", "--oneline", "upstream/main..HEAD"], cwd=shoulder_dir),
        Step("show upstream delta count", command=["git", "log", "--oneline", "HEAD..upstream/main"], cwd=shoulder_dir),
        Step("show upstream diff files", command=["git", "diff", "--name-only", "HEAD..upstream/main"], cwd=shoulder_dir),
    ]


def build_archive_steps(args: argparse.Namespace, root: Path) -> list[Step]:
    source_dir = root / "referencerepo" / args.category / args.shoulder_id
    archive_dir = root / "referencerepo" / "_archived" / args.category / args.shoulder_id
    if not source_dir.exists():
        raise RuntimeError(f"shoulder path does not exist: {source_dir}")
    timestamp = utc_now()
    archive_body = (
        "---\n"
        f"shoulder_id: {args.shoulder_id}\n"
        f"category: {args.category}\n"
        f"archived_at: {timestamp}\n"
        f"reason: {args.reason}\n"
        "---\n"
    )
    return [
        Step("create archive parent directory", command=["mkdir", "-p", str(archive_dir.parent)]),
        Step("move shoulder to local archive", command=["mv", str(source_dir), str(archive_dir)]),
        Step("write local archive note", write_path=archive_dir / "_SCOUTFLOW_ARCHIVE.local.md", write_body=archive_body),
    ]


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--workspace-root", help="Override the ScoutFlow repository root.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    fork = subparsers.add_parser("fork-shoulder", help="Prepare a local-only shoulder clone/fork workflow.")
    fork.add_argument("--dry-run", action="store_true", help="Print planned steps without executing them.")
    fork.add_argument("--default-branch", default=DEFAULT_BRANCH, help="Upstream default branch name.")
    fork.add_argument("--sync-cadence", default="monthly", help="Metadata sync cadence label.")
    fork.add_argument("shoulder_id")
    fork.add_argument("category")
    fork.add_argument("upstream_url")
    fork.add_argument("github_user")

    sync = subparsers.add_parser("sync-shoulder", help="Show upstream drift for a local-only shoulder clone.")
    sync.add_argument("--dry-run", action="store_true", help="Print planned steps without executing them.")
    sync.add_argument("shoulder_path")

    archive = subparsers.add_parser("archive-shoulder", help="Archive a local-only shoulder clone.")
    archive.add_argument("--dry-run", action="store_true", help="Print planned steps without executing them.")
    archive.add_argument("shoulder_id")
    archive.add_argument("category")
    archive.add_argument("reason")

    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv or sys.argv[1:])
    root = repo_root(args.workspace_root)
    ensure_repo_layout(root)

    if args.command == "fork-shoulder":
        steps = build_fork_steps(args, root)
    elif args.command == "sync-shoulder":
        steps = build_sync_steps(args, root)
    elif args.command == "archive-shoulder":
        steps = build_archive_steps(args, root)
    else:
        raise RuntimeError(f"unsupported command: {args.command}")

    try:
        run_steps(steps, dry_run=getattr(args, "dry_run", False))
    except subprocess.CalledProcessError as exc:
        print(f"command failed with exit code {exc.returncode}: {quote_command(exc.cmd)}", file=sys.stderr)
        return exc.returncode or 1
    except RuntimeError as exc:
        print(str(exc), file=sys.stderr)
        return 1
    except OSError as exc:
        print(str(exc), file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
