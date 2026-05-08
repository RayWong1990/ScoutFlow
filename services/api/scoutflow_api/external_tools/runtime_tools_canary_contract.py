from __future__ import annotations

from pathlib import Path
import re
from typing import Literal

from pydantic import BaseModel, ConfigDict, Field

from scoutflow_api.platform_result import PlatformResult


RuntimeToolExecutionStatus = Literal["not_executed", "preflight_only", "future_approved_run"]

DEFAULT_LANE_ID = "Lane B"
DEFAULT_TASK_ID = "T-P1A-161"
DEFAULT_SOURCE_FAMILY = "bilibili"
DEFAULT_SOURCE_KIND = "manual_url"
DEFAULT_ROUTE_HYPOTHESIS = "yt-dlp metadata-first"
DEFAULT_FALLBACK_HYPOTHESIS = "BBDown fallback-comparator"
DEFAULT_REPO_EXTERNAL_TEMP_ROOT = "/tmp/scoutflow-runtime-tools"
DEFAULT_FAILURE_REASON = "not_executed_by_dispatch_boundary"
DEFAULT_REMAINING_HOLDS = (
    "write_enabled=False",
    "runtime_tools",
    "true_vault_write",
    "browser_automation",
    "dbvnext_migration",
    "full_signal_workbench",
)

FORBIDDEN_EXCERPT_PATTERNS: tuple[tuple[str, re.Pattern[str]], ...] = (
    ("cookie header", re.compile(r"\bCookie\s*:\s*(?!\[[^\]]+\])", re.IGNORECASE)),
    ("authorization header", re.compile(r"\bAuthorization\s*:\s*(?!\[[^\]]+\])", re.IGNORECASE)),
    ("proxy authorization header", re.compile(r"\bProxy-Authorization\s*:\s*(?!\[[^\]]+\])", re.IGNORECASE)),
    ("access token", re.compile(r"\baccess_token\s*=\s*(?!\[REDACTED\])", re.IGNORECASE)),
    ("refresh token", re.compile(r"\brefresh_token\s*=\s*(?!\[REDACTED\])", re.IGNORECASE)),
    ("sessdata cookie", re.compile(r"\bSESSDATA\s*=\s*(?!\[REDACTED\])", re.IGNORECASE)),
    ("bili_jct cookie", re.compile(r"\bbili_jct\s*=\s*(?!\[REDACTED\])", re.IGNORECASE)),
    ("signed url", re.compile(r"https?://[^\s]+[?&](?:token|sig|signature|expires|auth_key)=", re.IGNORECASE)),
    ("browser profile path", re.compile(r"(?:Chrome|Chromium|Google/Chrome|Profile\s+\d+|User Data)", re.IGNORECASE)),
    ("local auth path", re.compile(r"(?:/Users/|/private/|/tmp/|/var/|/Volumes/)[^\s]*", re.IGNORECASE)),
)


class RuntimeCanaryManifestV1(BaseModel):
    model_config = ConfigDict(extra="forbid")

    manifest_version: Literal["RuntimeCanaryManifestV1"] = "RuntimeCanaryManifestV1"
    lane_id: str = Field(default=DEFAULT_LANE_ID)
    task_id: str = Field(default=DEFAULT_TASK_ID)
    source_family: str = Field(default=DEFAULT_SOURCE_FAMILY)
    source_kind: str = Field(default=DEFAULT_SOURCE_KIND)
    route_hypothesis: str = Field(default=DEFAULT_ROUTE_HYPOTHESIS)
    fallback_hypothesis: str = Field(default=DEFAULT_FALLBACK_HYPOTHESIS)
    tool_execution_status: RuntimeToolExecutionStatus = "not_executed"
    repo_external_temp_root: str = Field(default=DEFAULT_REPO_EXTERNAL_TEMP_ROOT)
    network_used: Literal[False] = False
    media_downloaded: Literal[False] = False
    raw_stdout_tracked: Literal[False] = False
    raw_stderr_tracked: Literal[False] = False
    credential_material_seen: Literal[False] = False
    safe_stdout_excerpt_path: str | None = None
    safe_stderr_excerpt_path: str | None = None
    platform_result: PlatformResult | None = None
    failure_classification_reason: str = Field(default=DEFAULT_FAILURE_REASON)
    remaining_holds: tuple[str, ...] = Field(default=DEFAULT_REMAINING_HOLDS)
    human_runtime_gate_required: Literal[True] = True


def build_runtime_canary_manifest(
    *,
    repo_root: Path,
    repo_external_temp_root: Path | str = DEFAULT_REPO_EXTERNAL_TEMP_ROOT,
    safe_stdout_excerpt_path: str | None = None,
    safe_stderr_excerpt_path: str | None = None,
    platform_result: PlatformResult | None = None,
    failure_classification_reason: str = DEFAULT_FAILURE_REASON,
    tool_execution_status: RuntimeToolExecutionStatus = "not_executed",
) -> RuntimeCanaryManifestV1:
    temp_root = Path(repo_external_temp_root).expanduser()
    validate_repo_external_temp_root(repo_root=repo_root, repo_external_temp_root=temp_root)

    return RuntimeCanaryManifestV1(
        tool_execution_status=tool_execution_status,
        repo_external_temp_root=str(temp_root),
        safe_stdout_excerpt_path=safe_stdout_excerpt_path,
        safe_stderr_excerpt_path=safe_stderr_excerpt_path,
        platform_result=platform_result,
        failure_classification_reason=failure_classification_reason,
    )


def validate_repo_external_temp_root(*, repo_root: Path, repo_external_temp_root: Path) -> None:
    repo_root_resolved = repo_root.expanduser().resolve()
    temp_root_resolved = repo_external_temp_root.expanduser().resolve()

    if _is_within(repo_root_resolved, temp_root_resolved):
        raise ValueError("repo_external_temp_root must live outside the ScoutFlow repo.")
    if _is_within(repo_root_resolved / "data", temp_root_resolved):
        raise ValueError("repo_external_temp_root must not live under data/.")
    if _is_within(repo_root_resolved / "referencerepo", temp_root_resolved):
        raise ValueError("repo_external_temp_root must not live under referencerepo/.")


def validate_safe_excerpt_text(text: str) -> list[str]:
    violations: list[str] = []
    for label, pattern in FORBIDDEN_EXCERPT_PATTERNS:
        if pattern.search(text):
            violations.append(label)
    return violations


def _is_within(parent: Path, child: Path) -> bool:
    try:
        child.relative_to(parent)
    except ValueError:
        return False
    return True
