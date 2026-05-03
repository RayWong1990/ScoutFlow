#!/usr/bin/env python3
"""ScoutFlow authority and redline checks."""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path


REQUIRED_DOCS = [
    "README.md",
    "AGENTS.md",
    "CLAUDE.md",
    "docs/current.md",
    "docs/task-index.md",
    "docs/specs/contracts-index.md",
    "docs/specs/locked-principles.md",
    "docs/specs/parallel-execution-protocol.md",
]

FORBIDDEN_ROOT_DIRS = [
    "apps",
    "workers",
    "packages",
    "candidates",
    "dispatches",
    "audits",
]

LOCAL_ONLY_ROOTS = ("data/", "referencerepo/")
ALLOWED_BANNED_WORD_FILES = {
    "docs/specs/locked-principles.md",
    "tools/check-docs-redlines.py",
}
BANNED_WORD_RE = re.compile(r"\b(crawl|spider|scrape_all|auto_capture|harvest)\b", re.IGNORECASE)
STATE_RE = re.compile(r"`?(backlog|in_progress|review|done|blocked)`?")
TASK_RE = re.compile(r"T-P(?:0|1A)-\d{3}")
OLD_RUNNING_STATUS = " ".join(("T-P0-001", "执行中"))
TASK_INDEX_SECTIONS = {"Review", "Backlog", "Blocked", "Done"}
HEADING_RE = re.compile(r"^##\s+(.+?)\s*$")


def run_git_ls_files(repo: Path) -> list[str]:
    result = subprocess.run(
        ["git", "ls-files"],
        cwd=repo,
        check=False,
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        raise RuntimeError(f"git ls-files 执行失败：{result.stderr.strip()}")
    return [line.strip() for line in result.stdout.splitlines() if line.strip()]


def read_text_if_text(path: Path) -> str | None:
    data = path.read_bytes()
    if b"\0" in data:
        return None
    try:
        return data.decode("utf-8")
    except UnicodeDecodeError:
        return data.decode("utf-8", errors="ignore")


def extract_line_value(text: str, label: str) -> str | None:
    for line in text.splitlines():
        if label in line:
            return line
    return None


def extract_task_id(line: str | None) -> str | None:
    if not line:
        return None
    match = TASK_RE.search(line)
    return match.group(0) if match else None


def extract_state(line: str | None) -> str | None:
    if not line:
        return None
    match = STATE_RE.search(line)
    return match.group(1) if match else None


def parse_task_index_states(task_index: str) -> tuple[dict[str, str], list[str]]:
    states: dict[str, str] = {}
    sections: dict[str, str] = {}
    errors: list[str] = []
    current_section: str | None = None

    for line_number, line in enumerate(task_index.splitlines(), start=1):
        heading = HEADING_RE.match(line)
        if heading:
            section = heading.group(1).strip()
            current_section = section if section in TASK_INDEX_SECTIONS else None
            continue

        if current_section is None or not line.lstrip().startswith("|"):
            continue

        cells = [cell.strip().strip("`") for cell in line.strip().strip("|").split("|")]
        if not cells:
            continue
        task_match = TASK_RE.fullmatch(cells[0])
        if not task_match:
            continue

        task_id = task_match.group(0)
        if task_id in states:
            errors.append(
                f"docs/task-index.md 中任务 {task_id} 重复出现："
                f"{sections[task_id]} 与 {current_section}（第 {line_number} 行）"
            )
            continue

        if current_section in {"Review", "Backlog"}:
            if len(cells) < 3 or not cells[2]:
                errors.append(f"docs/task-index.md 中任务 {task_id} 缺少状态列：第 {line_number} 行")
                continue
            state = cells[2]
        elif current_section == "Done":
            state = "done"
        elif current_section == "Blocked":
            state = "blocked"
        else:
            continue

        states[task_id] = state
        sections[task_id] = current_section

    return states, errors


def task_index_state(task_index: str, task_id: str, failures: list[str]) -> str | None:
    states, errors = parse_task_index_states(task_index)
    failures.extend(errors)
    return states.get(task_id)


def check_task_index_parser_self_check(failures: list[str]) -> None:
    review_fixture = """
## Review

| 任务 ID | 标题 | 状态 |
|---|---|---|
| `T-P0-003` | sample | `review` |
"""
    done_fixture = """
## Done

| 任务 ID | 标题 | 完成时间 | 备注 |
|---|---|---|---|
| `T-P0-003` | sample | `2026-05-03` | closed |
"""
    duplicate_fixture = review_fixture + done_fixture

    review_states, review_errors = parse_task_index_states(review_fixture)
    done_states, done_errors = parse_task_index_states(done_fixture)
    _, duplicate_errors = parse_task_index_states(duplicate_fixture)

    if review_errors or review_states.get("T-P0-003") != "review":
        failures.append("task-index 解析自检失败：Review 表未解析为 review")
    if done_errors or done_states.get("T-P0-003") != "done":
        failures.append("task-index 解析自检失败：Done 表未解析为 done")
    if not duplicate_errors:
        failures.append("task-index 解析自检失败：重复任务未报错")


def is_banned_word_definition(lines: list[str], index: int) -> bool:
    context = "\n".join(lines[max(0, index - 16) : min(len(lines), index + 17)])
    markers = [
        "禁用词",
        "禁用命名",
        "命名禁区",
        "禁止使用",
        "不要使用",
        "设计红线",
        "不借",
        "Avoid words",
        "banned words",
        "banned word",
        "banned naming",
    ]
    return any(marker.lower() in context.lower() for marker in markers)


def check_required_docs(repo: Path, failures: list[str]) -> None:
    for rel in REQUIRED_DOCS:
        if not (repo / rel).is_file():
            failures.append(f"缺少 required doc：{rel}")


def check_forbidden_dirs(repo: Path, failures: list[str]) -> None:
    for name in FORBIDDEN_ROOT_DIRS:
        if (repo / name).exists():
            failures.append(f"根目录禁止存在：{name}/")


def check_local_only_tracking(tracked: list[str], failures: list[str]) -> None:
    tracked_local = [
        path
        for path in tracked
        if any(path == root.rstrip("/") or path.startswith(root) for root in LOCAL_ONLY_ROOTS)
    ]
    if tracked_local:
        failures.append("data/ 或 referencerepo/ 不得被 git 跟踪：" + ", ".join(tracked_local[:20]))


def check_banned_words(repo: Path, tracked: list[str], failures: list[str]) -> None:
    for rel in tracked:
        if rel in ALLOWED_BANNED_WORD_FILES:
            continue
        path = repo / rel
        if not path.is_file():
            continue
        text = read_text_if_text(path)
        if text is None:
            continue
        lines = text.splitlines()
        for index, line in enumerate(lines):
            if not BANNED_WORD_RE.search(line):
                continue
            if is_banned_word_definition(lines, index):
                continue
            failures.append(f"禁用命名残留：{rel}:{index + 1}: {line.strip()}")


def check_old_status(repo: Path, tracked: list[str], failures: list[str]) -> None:
    for rel in tracked:
        path = repo / rel
        if not path.is_file():
            continue
        text = read_text_if_text(path)
        if text is not None and OLD_RUNNING_STATUS in text:
            failures.append(f"旧状态残留：{rel} 包含旧执行中状态")


def check_task_state_consistency(repo: Path, failures: list[str]) -> None:
    agents = (repo / "AGENTS.md").read_text(encoding="utf-8")
    current = (repo / "docs/current.md").read_text(encoding="utf-8")
    task_index = (repo / "docs/task-index.md").read_text(encoding="utf-8")

    agents_task = extract_task_id(extract_line_value(agents, "当前活动任务"))
    current_task = extract_task_id(extract_line_value(current, "主任务"))
    current_state = extract_state(extract_line_value(current, "当前任务状态"))

    if not agents_task:
        failures.append("AGENTS.md 未声明当前活动任务")
    if not current_task:
        failures.append("docs/current.md 未声明主任务")
    if agents_task and current_task and agents_task != current_task:
        failures.append(f"当前任务冲突：AGENTS.md={agents_task}，docs/current.md={current_task}")

    if current_task:
        index_state = task_index_state(task_index, current_task, failures)
        if not index_state:
            failures.append(f"docs/task-index.md 未找到当前任务：{current_task}")
        elif current_state and index_state != current_state:
            failures.append(
                f"当前任务状态冲突：docs/current.md={current_state}，docs/task-index.md={index_state}"
            )

    agents_status = extract_line_value(agents, "当前状态")
    agents_status_state = extract_state(agents_status)
    if agents_status_state and current_state and agents_status_state != current_state:
        failures.append(f"当前任务状态冲突：AGENTS.md={agents_status_state}，docs/current.md={current_state}")


def main() -> int:
    repo = Path.cwd()
    failures: list[str] = []

    if not (repo / ".git").exists():
        failures.append("请从 ScoutFlow 仓库根目录运行本脚本。")

    check_required_docs(repo, failures)
    check_forbidden_dirs(repo, failures)

    try:
        tracked = run_git_ls_files(repo)
    except RuntimeError as exc:
        failures.append(str(exc))
        tracked = []

    check_local_only_tracking(tracked, failures)
    check_banned_words(repo, tracked, failures)
    check_old_status(repo, tracked, failures)
    check_task_index_parser_self_check(failures)

    if all((repo / rel).is_file() for rel in ("AGENTS.md", "docs/current.md", "docs/task-index.md")):
        check_task_state_consistency(repo, failures)

    if failures:
        print("文档红线检查失败：")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("文档红线检查通过：required docs、禁止目录、local-only 跟踪、禁用命名、任务状态一致性均符合当前任务边界。")
    return 0


if __name__ == "__main__":
    sys.exit(main())
