#!/usr/bin/env python3
"""Refresh and verify ScoutFlow START-HERE live anchors."""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def _resolve_env_path(env_var: str, default: Path) -> Path:
    """Allow env var override for hardcoded paths (M-1 mitigation)."""
    override = os.environ.get(env_var)
    if override:
        return Path(override).expanduser().resolve()
    return default


START_HERE_PATH = ROOT / "docs/00-START-HERE.md"
SUMMARY_PATH = _resolve_env_path(
    "SCOUTFLOW_SUMMARY_PATH",
    ROOT / "docs/research/strategic-upgrade/2026-05-07/audit/PHASE-A-B-SUMMARY.md",
)
RUNS_DIR = _resolve_env_path(
    "SCOUTFLOW_RUNS_DIR",
    ROOT / "docs/research/post-frozen/runs",
)
REMOTE = os.environ.get("SCOUTFLOW_REMOTE", "origin")

AUTO_BEGIN = "<!-- START_HERE_AUTO_ANCHORS_BEGIN -->"
AUTO_END = "<!-- START_HERE_AUTO_ANCHORS_END -->"

DEFAULT_REFRESH_INTERVAL = 50
DEFAULT_NEXT_FORCED_REFRESH_PR = 300

PR_NUMBER_RE = re.compile(r"\(#(?P<pr>\d+)\)")
MERGE_PR_NUMBER_RE = re.compile(r"\bpull request #(?P<pr>\d+)\b", re.IGNORECASE)
INT_FIELD_TEMPLATE = r"^{field}:\s+.*$"
SHA_FIELD_RE = re.compile(r"^last_refreshed_from_main_sha:\s+.*$", re.MULTILINE)
MARKDOWN_COUNT_RE = re.compile(r"\*\*(?P<count>[\d,]+)\s+markdown\*\*")
WORD_COUNT_RE = re.compile(r"\*\*(?P<count>[\d,]+)\s+字\*\*")
PR_NUMBER_BY_SHORT_SHA = {
    # PR #261 landed as a local closeout commit without a "(#261)" subject suffix.
    "5902ecf": 261,
}


@dataclass(frozen=True)
class GitCommit:
    sha: str
    subject: str
    pr_number: int | None


@dataclass(frozen=True)
class RefreshContext:
    target_ref: str
    commits: list[GitCommit]
    current_pr_number: int | None
    checkpoint_dispatch_total: int
    strategic_markdown_count: str
    strategic_word_count: str
    refresh_interval_pr: int
    next_forced_refresh_pr: int
    last_updated: str


def default_main_ref() -> str:
    return f"{REMOTE}/main"


def run_git(repo: Path, *args: str) -> str:
    result = subprocess.run(
        ["git", *args],
        cwd=repo,
        check=False,
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        raise RuntimeError(f"git {' '.join(args)} failed: {result.stderr.strip()}")
    return result.stdout.strip()


def parse_pr_number(subject: str) -> int | None:
    match = PR_NUMBER_RE.search(subject)
    if match:
        return int(match.group("pr"))
    merge_match = MERGE_PR_NUMBER_RE.search(subject)
    if merge_match:
        return int(merge_match.group("pr"))
    return None


def pr_number_for_commit(sha: str, subject: str) -> int | None:
    return parse_pr_number(subject) or PR_NUMBER_BY_SHORT_SHA.get(sha)


def current_branch_name(repo: Path) -> str:
    branch_name = run_git(repo, "rev-parse", "--abbrev-ref", "HEAD")
    return branch_name.strip()


def resolve_target_ref(
    explicit_ref: str | None,
    branch_name: str,
    check_mode: bool,
    check_anchor_mode: str = "main",
) -> str:
    del branch_name
    if check_mode and check_anchor_mode == "main":
        return default_main_ref()
    if explicit_ref:
        return explicit_ref
    if check_mode and check_anchor_mode == "head":
        return "HEAD"
    return default_main_ref()


def is_main_ref(target_ref: str) -> bool:
    return target_ref == "main" or target_ref.endswith("/main")


def ensure_ref_is_available(repo: Path, target_ref: str) -> None:
    if not target_ref.startswith(f"{REMOTE}/"):
        return
    remote_check = subprocess.run(
        ["git", "remote", "get-url", REMOTE],
        cwd=repo,
        check=False,
        capture_output=True,
        text=True,
    )
    if remote_check.returncode != 0:
        raise RuntimeError(
            f"git remote {REMOTE!r} not found "
            f"(set SCOUTFLOW_REMOTE to a valid remote name; default 'origin')"
        )


def read_git_commits(repo: Path, target_ref: str, limit: int = 3) -> list[GitCommit]:
    ensure_ref_is_available(repo, target_ref)
    output = run_git(repo, "log", "--no-merges", target_ref, f"-{limit}", "--pretty=%h%x09%s%x09%cs")
    commits: list[GitCommit] = []
    for line in output.splitlines():
        sha, subject, _date = line.split("\t", 2)
        commits.append(GitCommit(sha=sha, subject=subject, pr_number=pr_number_for_commit(sha, subject)))
    if not commits:
        raise RuntimeError(f"{target_ref} has no commits")
    return commits


def read_current_pr_number(repo: Path, target_ref: str, limit: int = 20) -> int | None:
    ensure_ref_is_available(repo, target_ref)
    output = run_git(repo, "log", target_ref, f"-{limit}", "--pretty=%h%x09%s")
    for line in output.splitlines():
        sha, subject = line.split("\t", 1)
        pr_number = pr_number_for_commit(sha, subject)
        if pr_number is not None:
            return pr_number
    return None


def sum_checkpoint_dispatches(runs_dir: Path) -> int:
    if not runs_dir.exists() or not runs_dir.is_dir():
        raise RuntimeError(
            f"checkpoint runs directory not found: {runs_dir} "
            f"(set SCOUTFLOW_RUNS_DIR to override default path)"
        )
    total = 0
    for path in sorted(runs_dir.glob("CHECKPOINT-Run*-final.json")):
        payload = json.loads(path.read_text(encoding="utf-8"))
        total += int(payload.get("dispatches_total", 0))
    return total


def parse_strategic_summary(path: Path) -> tuple[str, str]:
    text = path.read_text(encoding="utf-8")
    markdown_match = MARKDOWN_COUNT_RE.search(text)
    word_match = WORD_COUNT_RE.search(text)
    if markdown_match is None or word_match is None:
        raise RuntimeError("Failed to parse markdown/word counts from PHASE-A-B-SUMMARY.md")
    return markdown_match.group("count"), word_match.group("count")


def frontmatter_int(text: str, field: str, default: int) -> int:
    pattern = re.compile(INT_FIELD_TEMPLATE.format(field=re.escape(field)), re.MULTILINE)
    match = pattern.search(text)
    if not match:
        return default
    _, value = match.group(0).split(":", 1)
    return int(value.strip())


def replace_or_insert_frontmatter_value(text: str, field: str, value: str) -> str:
    pattern = re.compile(INT_FIELD_TEMPLATE.format(field=re.escape(field)), re.MULTILINE)
    replacement = f"{field}: {value}"
    if pattern.search(text):
        return pattern.sub(replacement, text, count=1)
    frontmatter_end = text.find("---", 4)
    if frontmatter_end == -1:
        raise RuntimeError("START-HERE frontmatter not found")
    return text[:frontmatter_end] + replacement + "\n" + text[frontmatter_end:]


def compute_next_forced_refresh(current_pr: int | None, configured_next: int, interval: int) -> int:
    next_refresh = configured_next
    if current_pr is None:
        return next_refresh
    while current_pr >= next_refresh:
        next_refresh += interval
    return next_refresh


def render_main_head(commits: list[GitCommit]) -> str:
    rendered: list[str] = []
    for commit in commits:
        if commit.pr_number is not None:
            rendered.append(f"`{commit.sha}` (PR #{commit.pr_number})")
        else:
            rendered.append(f"`{commit.sha}`")
    return " ← ".join(rendered)


def render_ref_label(target_ref: str) -> str:
    if target_ref == "HEAD":
        return "checked-out content anchor"
    if target_ref.endswith("/main"):
        return "main content anchor"
    return f"{target_ref} content anchor"


def render_anchor_block(context: RefreshContext) -> str:
    lines = [
        AUTO_BEGIN,
        "| 维度 | 值 |",
        "|---|---|",
        "| repo | `/Users/wanglei/workspace/ScoutFlow` |",
        f"| {render_ref_label(context.target_ref)} | {render_main_head(context.commits)} |",
        "| capture-station stack | React 18.3.1 + Vite 5.4.10 + CSS Modules + tokens.css 三层 overlay + 自写 SVG sprite |",
        (
            "| checkpoint dispatch 累计 | "
            f"`{context.checkpoint_dispatch_total}`"
            "（`docs/research/post-frozen/runs/CHECKPOINT-Run*-final.json` 当前求和；"
            "不含 Amendment / PF-C4-01 / governance lane） |"
        ),
        "| PRD canonical | PRD-v2 + PRD-v2.1 amend (promoted, PR #58) |",
        "| SRD canonical | SRD-v2 + SRD-v3 h5-bridge amend (promoted, PR #64) |",
        (
            "| 16 ZIP 储能层 | "
            "`docs/research/strategic-upgrade/2026-05-07/audit/PHASE-A-B-SUMMARY.md` "
            f"当前摘要 = `{context.strategic_markdown_count} markdown / {context.strategic_word_count} 字` |"
        ),
        AUTO_END,
    ]
    return "\n".join(lines)


def refresh_text(text: str, context: RefreshContext, update_main_frontmatter: bool | None = None) -> str:
    refreshed = text
    current_pr = context.current_pr_number or context.commits[0].pr_number
    next_forced_refresh = compute_next_forced_refresh(
        current_pr=current_pr,
        configured_next=context.next_forced_refresh_pr,
        interval=context.refresh_interval_pr,
    )

    refreshed = replace_or_insert_frontmatter_value(refreshed, "last_updated", context.last_updated)
    if update_main_frontmatter is None:
        update_main_frontmatter = is_main_ref(context.target_ref)

    if update_main_frontmatter:
        refreshed = replace_or_insert_frontmatter_value(
            refreshed,
            "last_refreshed_from_main_pr",
            str(current_pr if current_pr is not None else "unknown"),
        )
        refreshed = SHA_FIELD_RE.sub(
            f"last_refreshed_from_main_sha: {context.commits[0].sha}",
            refreshed,
            count=1,
        )
    refreshed = replace_or_insert_frontmatter_value(
        refreshed, "refresh_interval_pr", str(context.refresh_interval_pr)
    )
    refreshed = replace_or_insert_frontmatter_value(
        refreshed, "next_forced_refresh_pr", str(next_forced_refresh)
    )

    anchor_pattern = re.compile(
        rf"{re.escape(AUTO_BEGIN)}.*?{re.escape(AUTO_END)}",
        re.DOTALL,
    )
    if not anchor_pattern.search(refreshed):
        raise RuntimeError("START-HERE auto anchor markers not found")
    return anchor_pattern.sub(render_anchor_block(context), refreshed, count=1)


def build_context(start_here_text: str, target_ref: str) -> RefreshContext:
    commits = read_git_commits(ROOT, target_ref)
    current_pr_number = read_current_pr_number(ROOT, target_ref)
    strategic_markdown_count, strategic_word_count = parse_strategic_summary(SUMMARY_PATH)
    refresh_interval_pr = frontmatter_int(
        start_here_text, "refresh_interval_pr", DEFAULT_REFRESH_INTERVAL
    )
    next_forced_refresh_pr = frontmatter_int(
        start_here_text, "next_forced_refresh_pr", DEFAULT_NEXT_FORCED_REFRESH_PR
    )
    last_updated = run_git(ROOT, "log", target_ref, "-1", "--pretty=%cs")
    return RefreshContext(
        target_ref=target_ref,
        commits=commits,
        current_pr_number=current_pr_number,
        checkpoint_dispatch_total=sum_checkpoint_dispatches(RUNS_DIR),
        strategic_markdown_count=strategic_markdown_count,
        strategic_word_count=strategic_word_count,
        refresh_interval_pr=refresh_interval_pr,
        next_forced_refresh_pr=next_forced_refresh_pr,
        last_updated=last_updated,
    )


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="fail if START-HERE needs refresh")
    parser.add_argument(
        "--ref",
        dest="target_ref",
        default=None,
        help=(
            "git ref to render for non-check refresh or --check-mode=head. "
            "Default is ${SCOUTFLOW_REMOTE:-origin}/main. In --check-mode=main, "
            "an explicit --ref is only resolved as a probe and does not rewrite the START-HERE authority content anchor."
        ),
    )
    parser.add_argument(
        "--check-mode",
        choices=("main", "head"),
        default="main",
        help=(
            "main checks START-HERE against the remote main authority content anchor; "
            "head checks against the selected ref without updating main frontmatter fields."
        ),
    )
    args = parser.parse_args(argv)

    original = START_HERE_PATH.read_text(encoding="utf-8")
    if args.check and args.target_ref and args.check_mode == "main":
        read_git_commits(ROOT, args.target_ref, limit=1)

    target_ref = resolve_target_ref(
        explicit_ref=args.target_ref,
        branch_name=current_branch_name(ROOT),
        check_mode=args.check,
        check_anchor_mode=args.check_mode,
    )
    if not args.check and not is_main_ref(target_ref):
        raise RuntimeError(
            "START-HERE refresh writes long-lived authority anchors and only accepts a main ref. "
            "Use `--check --check-mode head --ref <ref>` to inspect PR or synthetic refs."
        )
    context = build_context(original, target_ref)
    refreshed = refresh_text(
        original,
        context,
        update_main_frontmatter=is_main_ref(target_ref) and args.check_mode == "main",
    )

    if args.check:
        if refreshed != original:
            sys.stderr.write(
                "docs/00-START-HERE.md needs refresh: run `python tools/refresh-start-here.py`\n"
            )
            return 1
        return 0

    if refreshed != original:
        START_HERE_PATH.write_text(refreshed, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
