#!/usr/bin/env python3
"""ScoutFlow tracked-file secret redline checks."""

from __future__ import annotations

from dataclasses import dataclass
import importlib.util
from pathlib import Path
import re
import subprocess
import sys
from typing import Pattern


ROOT = Path(__file__).resolve().parents[1]
REDACTION_MODULE_PATH = ROOT / "services" / "api" / "scoutflow_api" / "redaction.py"


def load_redact_sensitive_text():
    spec = importlib.util.spec_from_file_location("scoutflow_redaction_for_secret_scan", REDACTION_MODULE_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load redaction module: {REDACTION_MODULE_PATH}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module.redact_sensitive_text


redact_sensitive_text = load_redact_sensitive_text()


MAX_EXCERPT_CHARS = 220
ALLOWED_DEFINITION_FILES = {
    "docs/specs/raw-response-redaction.md",
    "tools/check-secrets-redlines.py",
}
# reference storage (储能层 + archive + post-frozen 历史 commander prompt) 是 grep-able
# reference, 内含 redacted demo / 反例 narrative / 历史 commander prompt 引用 [REDACTED]
# 字面均为合法 mention, 跟 4 状态词体系 reference storage 一致 (docs/00-START-HERE.md §2).
ALLOWED_REDACTED_PREFIXES = (
    "docs/research/strategic-upgrade/",
    "docs/archive/",
    "docs/research/post-frozen/run-",  # historical run-1/run-2 amendment commander prompt
)
DEFINITION_CONTEXT_MARKERS = (
    "SECRET_PATTERNS",
    "PatternSpec",
    "Raw Response",
    "脱敏",
    "凭据",
    "敏感字段",
    "禁止保存",
    "常见敏感字段",
    "redaction",
    "definition",
)


@dataclass(frozen=True)
class PatternSpec:
    name: str
    regex: Pattern[str]


@dataclass(frozen=True)
class SecretFinding:
    path: str
    line_number: int
    pattern_name: str
    redacted_excerpt: str


SECRET_PATTERNS = (
    PatternSpec(
        "sessdata cookie value",
        re.compile(r"\bSESSDATA\s*=\s*(?!\[REDACTED\])[^&;\s\"'`]+", re.IGNORECASE),
    ),
    PatternSpec(
        "bili jct cookie value",
        re.compile(r"\bbili_jct\s*=\s*(?!\[REDACTED\])[^&;\s\"'`]+", re.IGNORECASE),
    ),
    PatternSpec(
        "dede user id cookie value",
        re.compile(r"\bDedeUserID\s*=\s*(?!\[REDACTED\])[^&;\s\"'`]+", re.IGNORECASE),
    ),
    PatternSpec(
        "proxy authorization header",
        re.compile(r"\bProxy-Authorization\s*:\s*(?!\[[^\]]+\])\S+", re.IGNORECASE),
    ),
    PatternSpec(
        "authorization header",
        re.compile(r"\bAuthorization\s*:\s*(?!\[[^\]]+\])\S+", re.IGNORECASE),
    ),
    PatternSpec(
        "access token value",
        re.compile(r"\baccess_token\s*=\s*(?!\[REDACTED\])[^&;\s\"'`]+", re.IGNORECASE),
    ),
    PatternSpec(
        "refresh token value",
        re.compile(r"\brefresh_token\s*=\s*(?!\[REDACTED\])[^&;\s\"'`]+", re.IGNORECASE),
    ),
    PatternSpec(
        "api key header",
        re.compile(r"\bX-API-Key\s*:\s*(?!\[[^\]]+\])\S+", re.IGNORECASE),
    ),
    PatternSpec(
        "set cookie header",
        re.compile(r"\bSet-Cookie\s*:\s*(?!\[[^\]]+\])[^;\r\n]*\w+\s*=", re.IGNORECASE),
    ),
    PatternSpec(
        "cookie header",
        re.compile(r"\bCookie\s*:\s*(?!\[[^\]]+\])[^;\r\n]*\w+\s*=", re.IGNORECASE),
    ),
    PatternSpec(
        "auth key value",
        re.compile(r"\bauth_key\s*=\s*(?!\[REDACTED\])[^&;\s\"'`]+", re.IGNORECASE),
    ),
)


def run_git_ls_files(repo: Path) -> list[str]:
    result = subprocess.run(
        ["git", "ls-files"],
        cwd=repo,
        check=False,
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        raise RuntimeError(f"git ls-files failed: {result.stderr.strip()}")
    return [line.strip() for line in result.stdout.splitlines() if line.strip()]


def read_text_if_text(path: Path) -> str | None:
    data = path.read_bytes()
    if b"\0" in data:
        return None
    try:
        return data.decode("utf-8")
    except UnicodeDecodeError:
        return None


def find_secret_redlines(repo: Path, tracked_paths: list[str] | None = None) -> list[SecretFinding]:
    tracked = tracked_paths if tracked_paths is not None else run_git_ls_files(repo)
    findings: list[SecretFinding] = []

    for rel in tracked:
        path = repo / rel
        if not path.is_file():
            continue
        text = read_text_if_text(path)
        if text is None:
            continue

        # reference storage prefix 豁免 (储能层 + archive + 历史 commander prompt 是 grep-able
        # reference, 内含 narrative "authorization: ..." / regex demo "SESSDATA=..." 等合法 mention,
        # 跟 4 状态词体系 reference storage 一致, 跟 BANNED_WORD scan 对称).
        if any(rel.startswith(prefix) for prefix in ALLOWED_REDACTED_PREFIXES):
            continue

        lines = text.splitlines()
        for index, line in enumerate(lines):
            for pattern in SECRET_PATTERNS:
                if not pattern.regex.search(line):
                    continue
                if is_allowed_definition_context(rel, lines, index):
                    continue
                findings.append(
                    SecretFinding(
                        path=rel,
                        line_number=index + 1,
                        pattern_name=pattern.name,
                        redacted_excerpt=redacted_excerpt(line),
                    )
                )
                break

    return findings


def is_allowed_definition_context(rel: str, lines: list[str], index: int) -> bool:
    if rel not in ALLOWED_DEFINITION_FILES:
        return False
    context = "\n".join(lines[max(0, index - 8) : min(len(lines), index + 9)])
    context_lower = context.lower()
    return any(marker.lower() in context_lower for marker in DEFINITION_CONTEXT_MARKERS)


def redacted_excerpt(line: str) -> str:
    redacted = redact_sensitive_text(line.strip())
    if len(redacted) <= MAX_EXCERPT_CHARS:
        return redacted
    return redacted[: MAX_EXCERPT_CHARS - 3] + "..."


def main() -> int:
    repo = Path.cwd()
    failures: list[str] = []

    if not (repo / ".git").exists():
        failures.append("请从 ScoutFlow 仓库根目录运行本脚本。")

    if not failures:
        try:
            findings = find_secret_redlines(repo)
        except RuntimeError as exc:
            failures.append(str(exc))
            findings = []
        for finding in findings:
            failures.append(
                f"{finding.path}:{finding.line_number}: {finding.pattern_name}: "
                f"{finding.redacted_excerpt}"
            )

    if failures:
        print("Secret redline scan failed:")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("Secret redline scan passed: tracked text files contain no obvious credential patterns.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
