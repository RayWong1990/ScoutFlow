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
    "workers",
    "packages",
    "candidates",
    "dispatches",
    "audits",
]

LOCAL_ONLY_ROOTS = ("data/", "referencerepo/")
ALLOWED_STATUS = {
    "current authority",
    "promoted addendum",
    "candidate north-star",
    "reference storage",
}
CURRENT_AUTHORITY_PATHS = {
    "docs/current.md",
    "docs/task-index.md",
    "docs/decision-log.md",
    "docs/00-START-HERE.md",
}
ALLOWED_BANNED_WORD_FILES = {
    "docs/specs/locked-principles.md",
    "tools/check-docs-redlines.py",
}
# reference storage (16 ZIP 储能层 + archive) 是历史 / grep-able reference, 不是 active 文档,
# 内含工具名 (firecrawl crawl depth) / 反例 narrative (no auto_capture) 等 mention 合法.
# 状态词体系 4 类: current authority / promoted addendum / candidate north-star / reference storage.
# 本豁免对应 reference storage 类, 跟 docs/00-START-HERE.md §2 一致.
ALLOWED_BANNED_WORD_PREFIXES = (
    "docs/research/strategic-upgrade/",
    "docs/archive/",
)
BANNED_WORD_RE = re.compile(r"\b(crawl|spider|scrape_all|auto_capture|harvest)\b", re.IGNORECASE)
STATE_RE = re.compile(r"`?(active|backlog|in_progress|review|done|blocked)`?")
TASK_RE = re.compile(r"T-P(?:0|1A)-\d{3}[A-Z]?")
INLINE_TASK_STATE_RE = re.compile(
    r"(?P<task>T-P(?:0|1A)-\d{3}[A-Z]?)\s*=\s*(?P<state>active|backlog|in_progress|review|done|blocked)"
)
DETAIL_TASK_STATE_RE = re.compile(
    r"^\s*-\s+`?(?P<task>T-P(?:0|1A)-\d{3}[A-Z]?)`?.*?状态\s+`?(?P<state>active|backlog|in_progress|review|done|blocked)`?"
)
FRONTMATTER_STATUS_RE = re.compile(r"^status:\s*(.+?)\s*$", re.MULTILINE)
ACTIVE_COUNT_RE = re.compile(r"Active count=`?(\d+)/(\d+)`?")
OLD_RUNNING_STATUS = " ".join(("T-P0-001", "执行中"))
TASK_INDEX_SECTIONS = {"Active", "Review", "Backlog", "Blocked", "Done"}
HEADING_RE = re.compile(r"^##\s+(.+?)\s*$")
SCOPE_NOTE_ROOTS = (
    "docs/research/repairs/",
    "docs/plans/",
)
SCOPE_NOTE_NAME_TOKENS = ("dispatch", "fixup", "repair", "worklist")


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


def run_git_name_only(repo: Path, args: list[str]) -> list[str] | None:
    result = subprocess.run(
        ["git", "diff", "--name-only", *args],
        cwd=repo,
        check=False,
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        return None
    return [line.strip() for line in result.stdout.splitlines() if line.strip()]


def run_git_changed_paths(repo: Path) -> list[str]:
    base_paths = run_git_name_only(repo, ["origin/main...HEAD"])
    if base_paths is None:
        fallback_paths = run_git_name_only(repo, []) or []
        staged_paths = run_git_name_only(repo, ["--cached"]) or []
        return sorted(set(fallback_paths + staged_paths))

    unstaged_paths = run_git_name_only(repo, []) or []
    staged_paths = run_git_name_only(repo, ["--cached"]) or []
    return sorted(set(base_paths + unstaged_paths + staged_paths))


def read_text_if_text(path: Path) -> str | None:
    data = path.read_bytes()
    if b"\0" in data:
        return None
    try:
        return data.decode("utf-8")
    except UnicodeDecodeError:
        return data.decode("utf-8", errors="ignore")


def extract_frontmatter_status(text: str) -> str | None:
    if not text.startswith("---\n"):
        return None
    frontmatter_end = text.find("\n---", 4)
    if frontmatter_end == -1:
        return None
    frontmatter = text[: frontmatter_end + 1]
    match = FRONTMATTER_STATUS_RE.search(frontmatter)
    if match is None:
        return None
    return match.group(1).strip()


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

        if current_section in {"Active", "Review", "Backlog"}:
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
    done_fixture = """
## Done

| 任务 ID | 标题 | 完成时间 | 备注 |
|---|---|---|---|
| `T-P1A-013A` | sample | `2026-05-04` | closed |
| `T-P1A-012R` | sample | `2026-05-04` | closed |
"""
    duplicate_fixture = """
## Active

| 任务 ID | 标题 | 状态 |
|---|---|---|
| `T-P1A-013A` | sample | `active` |

## Done

| 任务 ID | 标题 | 完成时间 | 备注 |
|---|---|---|---|
| `T-P1A-013A` | sample | `2026-05-04` | closed |
"""
    current_fixture = """
# Current

## 当前状态

- Active count=`0/3`

## 当前任务

- `T-P1A-013A`：sample；状态 `active`
"""

    done_states, done_errors = parse_task_index_states(done_fixture)
    _, duplicate_errors = parse_task_index_states(duplicate_fixture)
    current_errors = current_doc_state_failures(current_fixture)

    if done_errors or done_states.get("T-P1A-013A") != "done":
        failures.append("task-index 解析自检失败：Done 表未解析带后缀任务 T-P1A-013A")
    if done_errors or done_states.get("T-P1A-012R") != "done":
        failures.append("task-index 解析自检失败：Done 表未解析带后缀任务 T-P1A-012R")
    if not duplicate_errors:
        failures.append("task-index 解析自检失败：带后缀重复任务未报错")
    if not current_errors:
        failures.append("docs/current 自检失败：Active count=0 但仍有 active 任务时未报错")


def current_doc_state_mentions(current: str) -> list[tuple[str, str, int]]:
    mentions: list[tuple[str, str, int]] = []
    for line_number, line in enumerate(current.splitlines(), start=1):
        for match in INLINE_TASK_STATE_RE.finditer(line):
            mentions.append((match.group("task"), match.group("state"), line_number))
        detail_match = DETAIL_TASK_STATE_RE.search(line)
        if detail_match:
            mentions.append((detail_match.group("task"), detail_match.group("state"), line_number))
    return mentions


def current_doc_state_failures(current: str) -> list[str]:
    failures: list[str] = []
    mentions = current_doc_state_mentions(current)
    task_states: dict[str, list[tuple[str, int]]] = {}

    for task_id, state, line_number in mentions:
        task_states.setdefault(task_id, []).append((state, line_number))

    for task_id, entries in task_states.items():
        unique_states = {state for state, _ in entries}
        if len(unique_states) > 1:
            details = ", ".join(f"{state}@{line_number}" for state, line_number in entries)
            failures.append(f"docs/current.md 中任务 {task_id} 状态冲突：{details}")

    active_count_line = extract_line_value(current, "Active count=")
    active_count_match = ACTIVE_COUNT_RE.search(active_count_line or "")
    if active_count_match and active_count_match.group(1) == "0":
        active_mentions = [(task_id, line_number) for task_id, state, line_number in mentions if state == "active"]
        if active_mentions:
            details = ", ".join(f"{task_id}@{line_number}" for task_id, line_number in active_mentions)
            failures.append(f"docs/current.md 声明 Active count=0/3，但仍存在状态 active 任务：{details}")

    return failures


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
    apps_dispatch_only_enabled = False
    authority_files = [repo / "AGENTS.md", repo / "docs/current.md"]
    apps_markers = (
        "apps/**`、`services/**` 只有当前 dispatch 明确授权路径时可动",
        "apps/**`、`services/**` 仅当前 dispatch 明确授权路径时可动",
        "apps/services remain explicit-dispatch-only",
    )

    for path in authority_files:
        if not path.is_file():
            continue
        text = path.read_text(encoding="utf-8")
        if any(marker in text for marker in apps_markers):
            apps_dispatch_only_enabled = True
            break

    if (repo / "apps").exists() and not apps_dispatch_only_enabled:
        failures.append("根目录禁止存在：apps/")

    for name in FORBIDDEN_ROOT_DIRS:
        if (repo / name).exists():
            failures.append(f"根目录禁止存在：{name}/")


def is_scope_note_path(rel: str) -> bool:
    if not rel.endswith(".md"):
        return False
    if any(rel.startswith(root) for root in SCOPE_NOTE_ROOTS):
        return True
    lowered_name = Path(rel).name.lower()
    return any(token in lowered_name for token in SCOPE_NOTE_NAME_TOKENS)


def app_path_is_named_in_scope_note(repo: Path, tracked: list[str], app_path: str) -> bool:
    exact_path_re = re.compile(r"(?<![A-Za-z0-9_./-])" + re.escape(app_path) + r"(?![A-Za-z0-9_./-])")
    for rel in tracked:
        if not is_scope_note_path(rel):
            continue
        path = repo / rel
        if not path.is_file():
            continue
        text = read_text_if_text(path)
        if text is not None and exact_path_re.search(text):
            return True
    return False


def check_app_diff_scope_guard(
    repo: Path,
    tracked: list[str],
    failures: list[str],
    changed_paths: list[str] | None = None,
) -> None:
    if changed_paths is None:
        changed_paths = run_git_changed_paths(repo)

    changed_app_paths = sorted(
        {
            path.replace("\\", "/")
            for path in changed_paths
            if path.replace("\\", "/").startswith("apps/")
        }
    )
    if not changed_app_paths:
        return

    unexplained_paths = [path for path in changed_app_paths if not app_path_is_named_in_scope_note(repo, tracked, path)]
    if unexplained_paths:
        failures.append(
            "apps/** diff 缺少显式 dispatch/repair scope 说明："
            + ", ".join(unexplained_paths[:20])
            + "；历史 tracked app surface 不构成当前 PR 授权，请在 tracked dispatch/repair note 中逐路径点名。"
        )


def check_local_only_tracking(tracked: list[str], failures: list[str]) -> None:
    tracked_local = [
        path
        for path in tracked
        if any(path == root.rstrip("/") or path.startswith(root) for root in LOCAL_ONLY_ROOTS)
    ]
    if tracked_local:
        failures.append("data/ 或 referencerepo/ 不得被 git 跟踪：" + ", ".join(tracked_local[:20]))


def check_markdown_status_taxonomy(
    repo: Path,
    tracked: list[str],
    failures: list[str],
    changed_paths: list[str] | None = None,
) -> None:
    candidate_paths = tracked
    if changed_paths is not None:
        changed_set = {path.replace("\\", "/") for path in changed_paths}
        candidate_paths = [rel for rel in tracked if rel in changed_set]

    for rel in candidate_paths:
        if not rel.endswith(".md"):
            continue
        path = repo / rel
        if not path.is_file():
            continue
        text = read_text_if_text(path)
        if text is None:
            continue
        status = extract_frontmatter_status(text)
        if status is None:
            continue
        if status not in ALLOWED_STATUS:
            failures.append(
                f"frontmatter status 非法：{rel} -> {status}；仅允许 {', '.join(sorted(ALLOWED_STATUS))}"
            )
            continue
        if status == "current authority" and rel not in CURRENT_AUTHORITY_PATHS:
            failures.append(
                f"frontmatter status 越权：{rel} 使用 current authority；仅白名单路径可用。"
            )


def check_banned_words(repo: Path, tracked: list[str], failures: list[str]) -> None:
    for rel in tracked:
        if rel in ALLOWED_BANNED_WORD_FILES:
            continue
        if any(rel.startswith(prefix) for prefix in ALLOWED_BANNED_WORD_PREFIXES):
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

    failures.extend(current_doc_state_failures(current))


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

    changed_paths = run_git_changed_paths(repo)

    check_local_only_tracking(tracked, failures)
    check_markdown_status_taxonomy(repo, tracked, failures, changed_paths=changed_paths)
    check_app_diff_scope_guard(repo, tracked, failures, changed_paths=changed_paths)
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
