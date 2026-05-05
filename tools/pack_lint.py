#!/usr/bin/env python3
"""Lint ScoutFlow dispatch packs before commander execution."""

from __future__ import annotations

import argparse
import json
import os
from dataclasses import asdict, dataclass, field
from pathlib import Path
import re
import subprocess
import sys
from typing import Callable

import yaml


SEVERITY_ORDER = {"p1": 1, "p2": 2, "p3": 3}
ALWAYS_EXIST_FILES = {
    "AGENTS.md",
    "CLAUDE.md",
    "README.md",
    "docs/current.md",
    "docs/task-index.md",
}
PACK_INTERNAL_NAME_RE = re.compile(r"(scoutflow-doc\d|amend|README\.md|self-audit-report\.md|execution-plan)", re.IGNORECASE)
STRAY_COPY_RE = re.compile(r"(_副本| copy|\.bak)(?:\.md)?$", re.IGNORECASE)
PR_FILENAME_RE = re.compile(r"^PR(?P<pr>\d+).+\.md$")
FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n?", re.DOTALL)
SECTION_RE_TEMPLATE = r"^##\s+{name}\s*$"
LIST_LINE_RE = re.compile(r"^\s*-\s+(.*\S)\s*$")
TEST_F_RE = re.compile(r"test\s+-f\s+([^\s#]+)")
PRIOR_PR_RE = re.compile(r"PR\s*#(?P<pr>\d+)")
PORCELAIN_GREP_RE = re.compile(r"git status --short --porcelain \| grep -E \"([^\"]+)\"")
STATUS_TOKEN_RE = re.compile(r"([A-Za-z0-9_.-]+)/")
PATH_HINT_RE = re.compile(r"([A-Za-z0-9_./-]+\.(?:tsx|ts|json|md|py))")
LINE_RANGE = 240


@dataclass
class Finding:
    rule_id: str
    severity: str
    file: str
    line: int
    snippet: str
    suggested_fix: str
    context: dict[str, object] = field(default_factory=dict)


@dataclass
class DispatchDoc:
    path: Path
    text: str
    frontmatter_raw: str
    frontmatter: dict[str, object]
    allowed_paths: list[str]
    forbidden_paths: list[str]
    manual_gates_required: list[str]

    @property
    def name(self) -> str:
        return self.path.name


def git_origin_main(repo: Path) -> str:
    result = subprocess.run(
        ["git", "rev-parse", "--short", "origin/main"],
        cwd=repo,
        check=False,
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        raise RuntimeError(f"git rev-parse origin/main failed: {result.stderr.strip()}")
    return result.stdout.strip()


def extract_frontmatter(text: str) -> tuple[str, dict[str, object]]:
    match = FRONTMATTER_RE.match(text)
    if not match:
        return "", {}
    raw = match.group(1)
    parsed = yaml.safe_load(raw) or {}
    if not isinstance(parsed, dict):
        raise yaml.YAMLError("frontmatter must parse to a mapping")
    return raw, parsed


def extract_section_list(text: str, section: str) -> list[str]:
    heading_re = re.compile(SECTION_RE_TEMPLATE.format(name=re.escape(section)), re.MULTILINE)
    match = heading_re.search(text)
    if not match:
        return []

    items: list[str] = []
    started = False
    for line in text[match.end() :].splitlines():
        stripped = line.strip()
        if stripped.startswith("## "):
            break
        list_match = LIST_LINE_RE.match(line)
        if list_match:
            started = True
            items.append(list_match.group(1).strip())
            continue
        if started and stripped and not stripped.startswith("#"):
            break
    return items


def parse_dispatch_docs(pack_dir: Path) -> list[DispatchDoc]:
    docs: list[DispatchDoc] = []
    for path in sorted(pack_dir.glob("PR*.md")):
        if path.name == "PR76-PR125-execution-plan-2026-05-05.md":
            continue
        text = path.read_text(encoding="utf-8")
        try:
            frontmatter_raw, frontmatter = extract_frontmatter(text)
        except yaml.YAMLError:
            frontmatter_raw, frontmatter = "", {}
        docs.append(
            DispatchDoc(
                path=path,
                text=text,
                frontmatter_raw=frontmatter_raw,
                frontmatter=frontmatter,
                allowed_paths=extract_section_list(text, "allowed_paths"),
                forbidden_paths=extract_section_list(text, "forbidden_paths"),
                manual_gates_required=_normalize_string_list(frontmatter.get("manual_gates_required")),
            )
        )
    return docs


def _normalize_string_list(value: object) -> list[str]:
    if isinstance(value, list):
        return [str(item) for item in value]
    return []


def line_number(text: str, needle: str) -> int:
    index = text.find(needle)
    if index < 0:
        return 1
    return text[:index].count("\n") + 1


def resolve_rule_selection(name: str) -> str:
    cleaned = name.lower().strip()
    if cleaned in {"l1", "baseline-freshness"}:
        return "pack-lint/baseline-freshness"
    if cleaned in {"l2", "amend-file-relative-path"}:
        return "pack-lint/amend-file-relative-path"
    if cleaned in {"l3", "forbid-require-collision"}:
        return "pack-lint/forbid-require-collision"
    if cleaned in {"l4", "authority-gate-unreachable"}:
        return "pack-lint/authority-gate-unreachable"
    if cleaned in {"l5", "weak-noop-test-gate"}:
        return "pack-lint/weak-noop-test-gate"
    if cleaned in {"l6", "inline-exception-in-forbidden"}:
        return "pack-lint/inline-exception-in-forbidden"
    if cleaned in {"l7", "frontmatter-yaml-parse"}:
        return "pack-lint/frontmatter-yaml-parse"
    if cleaned in {"l8", "required-fields-missing"}:
        return "pack-lint/required-fields-missing"
    if cleaned in {"l9", "handoff-chain-broken"}:
        return "pack-lint/handoff-chain-broken"
    if cleaned in {"l10", "live-pr-number-mismatch"}:
        return "pack-lint/live-pr-number-mismatch"
    if cleaned in {"l11", "pack-internal-relative-reference"}:
        return "pack-lint/pack-internal-relative-reference"
    if cleaned in {"l12", "self-audit-narrative-contradiction"}:
        return "pack-lint/self-audit-narrative-contradiction"
    if cleaned in {"l13", "duplicate-dispatch-slot"}:
        return "pack-lint/duplicate-dispatch-slot"
    if cleaned in {"l14", "inventory-count-mismatch"}:
        return "pack-lint/inventory-count-mismatch"
    return name


def lint_pack(pack_dir: Path, repo: Path, origin_main_sha: str, selected_rules: set[str] | None = None) -> list[Finding]:
    docs = parse_dispatch_docs(pack_dir)
    findings: list[Finding] = []
    inventory_names = {path.name for path in pack_dir.glob("*.md")}
    dispatch_outputs = {
        doc.name: set(doc.allowed_paths)
        for doc in docs
    }

    def enabled(rule_id: str) -> bool:
        return not selected_rules or rule_id in selected_rules

    if enabled("pack-lint/frontmatter-yaml-parse"):
        findings.extend(rule_frontmatter_yaml_parse(pack_dir))
    if enabled("pack-lint/required-fields-missing"):
        findings.extend(rule_required_fields(docs))
    if enabled("pack-lint/baseline-freshness"):
        findings.extend(rule_baseline_freshness(docs, origin_main_sha))
    if enabled("pack-lint/amend-file-relative-path"):
        findings.extend(rule_amend_file_paths(docs, pack_dir, inventory_names))
    if enabled("pack-lint/pack-internal-relative-reference"):
        findings.extend(rule_pack_internal_refs(docs, pack_dir, inventory_names))
    if enabled("pack-lint/forbid-require-collision"):
        findings.extend(rule_forbid_require_collision(docs))
    if enabled("pack-lint/authority-gate-unreachable"):
        findings.extend(rule_authority_gate_reachability(docs, dispatch_outputs, repo))
    if enabled("pack-lint/weak-noop-test-gate"):
        findings.extend(rule_weak_noop_gates(docs))
    if enabled("pack-lint/inline-exception-in-forbidden"):
        findings.extend(rule_inline_exception_in_forbidden(docs))
    if enabled("pack-lint/handoff-chain-broken"):
        findings.extend(rule_handoff_chain(docs, repo))
    if enabled("pack-lint/live-pr-number-mismatch"):
        findings.extend(rule_live_pr_number_mismatch(docs))
    if enabled("pack-lint/self-audit-narrative-contradiction"):
        findings.extend(rule_self_audit_narrative(pack_dir))
    if enabled("pack-lint/duplicate-dispatch-slot"):
        findings.extend(rule_duplicate_dispatch_slot(pack_dir))
    if enabled("pack-lint/inventory-count-mismatch"):
        findings.extend(rule_inventory_count_mismatch(pack_dir))

    return findings


def rule_frontmatter_yaml_parse(pack_dir: Path) -> list[Finding]:
    findings: list[Finding] = []
    for path in sorted(pack_dir.glob("PR*.md")):
        if path.name == "PR76-PR125-execution-plan-2026-05-05.md":
            continue
        text = path.read_text(encoding="utf-8")
        match = FRONTMATTER_RE.match(text)
        if not match:
            findings.append(
                Finding(
                    rule_id="pack-lint/frontmatter-yaml-parse",
                    severity="p2",
                    file=path.name,
                    line=1,
                    snippet=path.name,
                    suggested_fix="Add YAML frontmatter at the top of the dispatch file.",
                )
            )
            continue
        try:
            yaml.safe_load(match.group(1))
        except yaml.YAMLError as exc:
            findings.append(
                Finding(
                    rule_id="pack-lint/frontmatter-yaml-parse",
                    severity="p2",
                    file=path.name,
                    line=1,
                    snippet=str(exc).splitlines()[0],
                    suggested_fix="Fix YAML indentation / quoting so frontmatter parses cleanly.",
                )
            )
    return findings


def rule_required_fields(docs: list[DispatchDoc]) -> list[Finding]:
    findings: list[Finding] = []
    for doc in docs:
        is_out_of_band = bool(doc.frontmatter.get("dispatch_slot"))
        required_frontmatter = (
            ["dispatch_id", "dispatch_slot", "title", "type", "lane", "suggested_branch"]
            if is_out_of_band
            else ["dispatch_id", "pr_number", "title", "type", "lane", "suggested_branch", "prior_pr_required"]
        )
        missing = [field for field in required_frontmatter if not doc.frontmatter.get(field)]
        if not doc.allowed_paths and not is_out_of_band:
            missing.append("allowed_paths section")
        if not doc.forbidden_paths and not is_out_of_band:
            missing.append("forbidden_paths section")
        if missing:
            findings.append(
                Finding(
                    rule_id="pack-lint/required-fields-missing",
                    severity="p2",
                    file=doc.name,
                    line=1,
                    snippet=", ".join(missing),
                    suggested_fix="Add the missing frontmatter fields or markdown sections required for pack execution.",
                )
            )
    return findings


def rule_baseline_freshness(docs: list[DispatchDoc], origin_main_sha: str) -> list[Finding]:
    findings: list[Finding] = []
    for doc in docs:
        drafting = str(doc.frontmatter.get("current_main_head_at_drafting_time", "")).strip()
        if not drafting or drafting == origin_main_sha:
            continue
        has_annotation = "actual_origin_main_at_audit_time:" in doc.text
        has_drift_note = "## Audit-time drift note" in doc.text
        if has_annotation or has_drift_note:
            continue
        findings.append(
            Finding(
                rule_id="pack-lint/baseline-freshness",
                severity="p1",
                file=doc.name,
                line=line_number(doc.text, "current_main_head_at_drafting_time:"),
                snippet=f"drafting={drafting} origin/main={origin_main_sha}",
                suggested_fix="Add actual_origin_main_at_audit_time annotation and an Audit-time drift note section.",
            )
        )
    return findings


def rule_amend_file_paths(docs: list[DispatchDoc], pack_dir: Path, inventory_names: set[str]) -> list[Finding]:
    findings: list[Finding] = []
    for doc in docs:
        for match in TEST_F_RE.finditer(doc.text):
            target = match.group(1)
            if not PACK_INTERNAL_NAME_RE.search(target):
                continue
            if not target.startswith("/"):
                findings.append(
                    Finding(
                        rule_id="pack-lint/amend-file-relative-path",
                        severity="p1",
                        file=doc.name,
                        line=line_number(doc.text, target),
                        snippet=target,
                        suggested_fix=f"Rewrite as absolute path under {pack_dir}.",
                    )
                )
                continue
            resolved = Path(target)
            if not _path_within(resolved, pack_dir):
                findings.append(
                    Finding(
                        rule_id="pack-lint/amend-file-relative-path",
                        severity="p1",
                        file=doc.name,
                        line=line_number(doc.text, target),
                        snippet=target,
                        suggested_fix=f"Rewrite the path so it points inside the current pack root {pack_dir}.",
                    )
                )
    return findings


def rule_pack_internal_refs(docs: list[DispatchDoc], pack_dir: Path, inventory_names: set[str]) -> list[Finding]:
    findings: list[Finding] = []
    abs_path_re = re.compile(r"`([^`]+\.md)`|(/[^\\s`'\"]+\.md)")
    for doc in docs:
        for line in doc.text.splitlines():
            targets: list[str] = []
            if "test -f" in line:
                targets.extend(match.group(1) for match in TEST_F_RE.finditer(line))
            if re.match(r"^\s*\d+\.\s+`?/", line) or "dispatch_pack_path:" in line:
                for match in abs_path_re.finditer(line):
                    targets.append(match.group(1) or match.group(2))

            for target in targets:
                basename = Path(target).name
                if basename not in inventory_names:
                    continue
                if not PACK_INTERNAL_NAME_RE.search(basename):
                    continue
                if not target.startswith("/"):
                    findings.append(
                        Finding(
                            rule_id="pack-lint/pack-internal-relative-reference",
                            severity="p2",
                            file=doc.name,
                            line=line_number(doc.text, target),
                            snippet=target,
                            suggested_fix=f"Use an absolute path rooted at {pack_dir}.",
                        )
                    )
                    continue
                resolved = Path(target)
                if not _path_within(resolved, pack_dir):
                    findings.append(
                        Finding(
                            rule_id="pack-lint/pack-internal-relative-reference",
                            severity="p2",
                            file=doc.name,
                            line=line_number(doc.text, target),
                            snippet=target,
                            suggested_fix=f"Point this pack-internal reference at the current pack root {pack_dir}.",
                        )
                    )
    return findings


def rule_forbid_require_collision(docs: list[DispatchDoc]) -> list[Finding]:
    findings: list[Finding] = []
    for doc in docs:
        allowed_roots = {path.split("/")[0] for path in doc.allowed_paths if "/" in path}
        if not allowed_roots:
            continue
        for line in doc.text.splitlines():
            if "git status --short --porcelain | grep -E" not in line or "awk '{print $NF}'" in line:
                continue
            grep_match = PORCELAIN_GREP_RE.search(line)
            if not grep_match:
                continue
            parents = {token.rstrip("/") for token in STATUS_TOKEN_RE.findall(grep_match.group(1))}
            collisions = sorted(root for root in allowed_roots if root in parents)
            if collisions:
                findings.append(
                    Finding(
                        rule_id="pack-lint/forbid-require-collision",
                        severity="p1",
                        file=doc.name,
                        line=line_number(doc.text, line),
                        snippet=line.strip(),
                        suggested_fix="Remove the colliding parent from the porcelain forbid grep and add a sub-tree safety-net check.",
                        context={"colliding_roots": collisions, "allowed_paths": doc.allowed_paths},
                    )
                )
                break
    return findings


def rule_authority_gate_reachability(docs: list[DispatchDoc], dispatch_outputs: dict[str, set[str]], repo: Path) -> list[Finding]:
    findings: list[Finding] = []
    all_outputs = set().union(*dispatch_outputs.values()) if dispatch_outputs else set()
    for doc in docs:
        prior = str(doc.frontmatter.get("prior_pr_required", "")).strip()
        if not prior:
            continue
        clauses = [clause.strip(" '\"") for clause in prior.split("+")]
        manual_gates = " ".join(doc.manual_gates_required)
        for clause in clauses:
            if not clause:
                continue
            if PRIOR_PR_RE.search(clause):
                continue
            path_match = PATH_HINT_RE.search(clause)
            if path_match:
                candidate_path = path_match.group(1)
                if candidate_path in all_outputs or (repo / candidate_path).exists():
                    continue
            if any(keyword in clause.lower() for keyword in ("promoted", "promotion", "approved", "unlock", "manual gate")):
                if manual_gates:
                    continue
            elif " exists" in clause.lower():
                continue
            findings.append(
                Finding(
                    rule_id="pack-lint/authority-gate-unreachable",
                    severity="p1",
                    file=doc.name,
                    line=line_number(doc.text, prior),
                    snippet=clause,
                    suggested_fix="Move extra-pack prerequisites into manual_gates_required with a verification command.",
                )
            )
            break
    return findings


def rule_weak_noop_gates(docs: list[DispatchDoc]) -> list[Finding]:
    findings: list[Finding] = []
    for doc in docs:
        lines = doc.text.splitlines()
        for idx, line in enumerate(lines):
            test_match = TEST_F_RE.search(line)
            if not test_match:
                continue
            target = test_match.group(1)
            if target not in ALWAYS_EXIST_FILES:
                continue
            window = "\n".join(lines[max(0, idx - 2) : min(len(lines), idx + 5)])
            if re.search(r"\b(grep|rg)\b", window):
                continue
            findings.append(
                Finding(
                    rule_id="pack-lint/weak-noop-test-gate",
                    severity="p2",
                    file=doc.name,
                    line=idx + 1,
                    snippet=line.strip(),
                    suggested_fix="Add a nearby grep/rg content check proving the prerequisite state, not just file existence.",
                )
            )
    return findings


def rule_inline_exception_in_forbidden(docs: list[DispatchDoc]) -> list[Finding]:
    findings: list[Finding] = []
    for doc in docs:
        for item in doc.forbidden_paths:
            if "(exception:" not in item:
                continue
            findings.append(
                Finding(
                    rule_id="pack-lint/inline-exception-in-forbidden",
                    severity="p2",
                    file=doc.name,
                    line=line_number(doc.text, item),
                    snippet=item,
                    suggested_fix="Extract this exception into a forbidden_paths_exceptions block with machine-readable fields.",
                )
            )
    return findings


def rule_handoff_chain(docs: list[DispatchDoc], repo: Path) -> list[Finding]:
    findings: list[Finding] = []
    pack_prs = {_first_pr_number(doc.name) for doc in docs}
    for doc in docs:
        prior = str(doc.frontmatter.get("prior_pr_required", "")).strip()
        if not prior:
            continue
        match = PRIOR_PR_RE.search(prior)
        if not match:
            continue
        pr_num = int(match.group("pr"))
        if pr_num in pack_prs:
            continue
        # If it is not in-pack, we only warn when it clearly points to a future PR.
        current_pr = _first_pr_number(doc.name)
        if pr_num >= current_pr:
            findings.append(
                Finding(
                    rule_id="pack-lint/handoff-chain-broken",
                    severity="p3",
                    file=doc.name,
                    line=line_number(doc.text, prior),
                    snippet=prior,
                    suggested_fix="Clarify whether this prior PR is in-pack, already merged, or an external manual gate.",
                )
            )
    return findings


def rule_live_pr_number_mismatch(docs: list[DispatchDoc]) -> list[Finding]:
    findings: list[Finding] = []
    for doc in docs:
        if doc.frontmatter.get("dispatch_slot") and not doc.frontmatter.get("live_github_pr_number"):
            findings.append(
                Finding(
                    rule_id="pack-lint/live-pr-number-mismatch",
                    severity="p3",
                    file=doc.name,
                    line=1,
                    snippet="dispatch_slot without live_github_pr_number",
                    suggested_fix="Add a live_github_pr_number note or an explicit resolved-at-create-time marker.",
                )
            )
    return findings


def rule_self_audit_narrative(pack_dir: Path) -> list[Finding]:
    findings: list[Finding] = []
    target = pack_dir / "self-audit-report.md"
    if not target.exists():
        return findings
    text = target.read_text(encoding="utf-8")
    not_hash = re.search(r"NOT\s+([0-9a-f]{7,40})", text)
    uses_hash = re.search(r"uses that.*?([0-9a-f]{7,40})", text, re.IGNORECASE | re.DOTALL)
    if not_hash and uses_hash and not_hash.group(1) == uses_hash.group(1):
        findings.append(
            Finding(
                rule_id="pack-lint/self-audit-narrative-contradiction",
                severity="p3",
                file=target.name,
                line=line_number(text, not_hash.group(0)),
                snippet=not_hash.group(0),
                suggested_fix="Rewrite the narrative so drafting baseline truth and audit-time truth are distinguished without contradiction.",
            )
        )
    return findings


def rule_duplicate_dispatch_slot(pack_dir: Path) -> list[Finding]:
    findings: list[Finding] = []
    slot_to_files: dict[int, list[str]] = {}
    for path in sorted(pack_dir.glob("PR*.md")):
        match = PR_FILENAME_RE.match(path.name)
        if not match or path.name == "PR76-PR125-execution-plan-2026-05-05.md":
            continue
        slot_to_files.setdefault(int(match.group("pr")), []).append(path.name)
        if STRAY_COPY_RE.search(path.name):
            findings.append(
                Finding(
                    rule_id="pack-lint/duplicate-dispatch-slot",
                    severity="p2",
                    file=path.name,
                    line=1,
                    snippet=path.name,
                    suggested_fix="Delete the stray copy or rename it out of the active pack inventory.",
                )
            )
    for slot, names in slot_to_files.items():
        if len(names) <= 1:
            continue
        findings.append(
            Finding(
                rule_id="pack-lint/duplicate-dispatch-slot",
                severity="p2",
                file=names[0],
                line=1,
                snippet=", ".join(names),
                suggested_fix=f"Keep only one active dispatch file for slot PR{slot}.",
            )
        )
    return findings


def rule_inventory_count_mismatch(pack_dir: Path) -> list[Finding]:
    findings: list[Finding] = []
    actual_dispatches = len(
        [
            path
            for path in pack_dir.glob("PR*.md")
            if path.name != "PR76-PR125-execution-plan-2026-05-05.md"
        ]
    )
    for name in ("README.md", "self-audit-report.md"):
        path = pack_dir / name
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        declared = _extract_declared_dispatch_count(text)
        if declared is None or declared == actual_dispatches:
            continue
        findings.append(
            Finding(
                rule_id="pack-lint/inventory-count-mismatch",
                severity="p2",
                file=name,
                line=1,
                snippet=f"declared={declared} actual={actual_dispatches}",
                suggested_fix="Align inventory language with actual filesystem dispatch count, including any out-of-band pre-gate dispatches.",
            )
        )
    return findings


def _extract_declared_dispatch_count(text: str) -> int | None:
    total = 0
    found = False
    main_range = re.search(r"(\d+)\s+main-range .*dispatch markdown files?", text, re.IGNORECASE)
    generic = re.search(r"(\d+)\s+(?:Codex CLI )?dispatch markdown files?", text, re.IGNORECASE)
    if main_range:
        total += int(main_range.group(1))
        found = True
    elif generic:
        total += int(generic.group(1))
        found = True

    out_of_band_words = re.search(r"\bone out-of-band [^\n]*dispatch\b", text, re.IGNORECASE)
    out_of_band_numeric = re.search(r"(\d+)\s+out-of-band [^\n]*dispatch", text, re.IGNORECASE)
    if out_of_band_words:
        total += 1
        found = True
    elif out_of_band_numeric:
        total += int(out_of_band_numeric.group(1))
        found = True
    return total if found else None


def _first_pr_number(name: str) -> int:
    match = PR_FILENAME_RE.match(name)
    return int(match.group("pr")) if match else -1


def _path_within(path: Path, root: Path) -> bool:
    try:
        path.resolve().relative_to(root.resolve())
        return True
    except Exception:
        return False


def filter_findings(findings: list[Finding], severity: str, selected_rules: set[str] | None) -> list[Finding]:
    max_level = SEVERITY_ORDER[severity]
    filtered = [finding for finding in findings if SEVERITY_ORDER[finding.severity] <= max_level]
    if not selected_rules:
        return filtered
    return [finding for finding in filtered if finding.rule_id in selected_rules]


def build_summary(findings: list[Finding]) -> dict[str, object]:
    p1 = sum(1 for item in findings if item.severity == "p1")
    p2 = sum(1 for item in findings if item.severity == "p2")
    p3 = sum(1 for item in findings if item.severity == "p3")
    return {
        "total_dispatches": sum(1 for item in findings),  # overwritten by caller when known
        "p1_findings": p1,
        "p2_findings": p2,
        "p3_findings": p3,
        "verdict": "clear" if not findings else "fail",
    }


def format_text(findings: list[Finding], pack_path: Path) -> str:
    if not findings:
        return f"pack-lint passed: {pack_path}"
    lines = [f"pack-lint findings for {pack_path}:"]
    for finding in findings:
        lines.append(
            f"- [{finding.severity.upper()}] {finding.rule_id} {finding.file}:{finding.line}: {finding.snippet}"
        )
    return "\n".join(lines)


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("pack_dir", help="Pack directory to lint")
    parser.add_argument("--repo", default=os.getcwd(), help="Repo root used for repo-relative checks (default: cwd)")
    parser.add_argument("--origin-main-sha", help="Override origin/main SHA (useful for tests)")
    parser.add_argument("--severity", choices=("p1", "p2", "p3"), default="p3")
    parser.add_argument("--output", choices=("text", "json"), default="text")
    parser.add_argument("--rule", action="append", default=[], help="Rule selector (e.g. l3 or pack-lint/forbid-require-collision)")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv or sys.argv[1:])
    pack_dir = Path(args.pack_dir).expanduser().resolve()
    repo = Path(args.repo).expanduser().resolve()

    if not pack_dir.exists():
        print(f"pack-lint: pack dir not found: {pack_dir}", file=sys.stderr)
        return 2

    try:
        origin_main_sha = args.origin_main_sha or git_origin_main(repo)
    except RuntimeError as exc:
        print(f"pack-lint: {exc}", file=sys.stderr)
        return 2

    selected_rules = {resolve_rule_selection(rule) for rule in args.rule} if args.rule else None
    findings = lint_pack(pack_dir, repo, origin_main_sha, selected_rules)
    filtered = filter_findings(findings, args.severity, selected_rules)

    summary = build_summary(filtered)
    summary["total_dispatches"] = len([path for path in pack_dir.glob("PR*.md") if path.name != "PR76-PR125-execution-plan-2026-05-05.md"])
    payload = {
        "pack_path": str(pack_dir),
        "lint_run_at": __import__("datetime").datetime.now().astimezone().isoformat(timespec="seconds"),
        "lint_version": "0.1.0",
        "summary": summary,
        "findings": [asdict(finding) for finding in filtered],
    }

    if args.output == "json":
        print(json.dumps(payload, ensure_ascii=False, indent=2))
    else:
        print(format_text(filtered, pack_dir))

    return 1 if filtered else 0


if __name__ == "__main__":
    sys.exit(main())
