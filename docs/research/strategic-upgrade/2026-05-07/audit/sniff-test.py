#!/usr/bin/env python3
"""Sniff-test 16 cloud outputs under outputs/ for boundary, secret, claim-label, truthful-stdout integrity.

Run from docs/research/strategic-upgrade/2026-05-07/:
    python3 audit/sniff-test.py
"""

import os
import re
import sys
from pathlib import Path

OUTPUTS_DIR = Path("outputs")
AUDIT_DIR = Path("audit")

BOUNDARY_PATTERNS = {
    "write_enabled_True": re.compile(r"write_enabled\s*[=:]\s*True", re.I),
    "BBDown_run": re.compile(r"\bBBDown\b[^a-zA-Z].{0,40}\b(run|exec|subprocess|invoke|spawn|launch)\b", re.I),
    "yt_dlp_run": re.compile(r"\byt[-_]dlp\b.{0,40}\b(run|exec|subprocess|invoke|spawn|launch)\b", re.I),
    "ffmpeg_run": re.compile(r"\bffmpeg\b.{0,40}\b(run|exec|subprocess|invoke|spawn|launch)\b", re.I),
    "subprocess_run": re.compile(r"\bsubprocess\.(run|Popen|check_output|call)\b"),
    "playwright_selenium_active": re.compile(r"\b(playwright|selenium|puppeteer)\b.{0,40}\b(launch|browser|page|navigate)\b", re.I),
    "alembic_new_migration": re.compile(r"alembic\s+revision|services/api/migrations/", re.I),
    "can_open_C4_true": re.compile(r"can_open_C4\s*[=:]\s*[Tt]rue"),
    "can_open_runtime_true": re.compile(r"can_open_runtime\s*[=:]\s*[Tt]rue"),
    "can_open_migration_true": re.compile(r"can_open_migration\s*[=:]\s*[Tt]rue"),
    "vendor_accepted": re.compile(r"vendor[\s_]+(已采纳|已批准|accepted|approved)\b", re.I),
}

SECRET_PATTERNS = {
    "api_key_assignment": re.compile(r"\b(api[_-]?key|secret[_-]?key)\s*[=:]\s*['\"][A-Za-z0-9_-]{20,}['\"]", re.I),
    "openai_sk": re.compile(r"\bsk-[A-Za-z0-9]{40,}"),
    "jwt_token": re.compile(r"\beyJ[A-Za-z0-9_-]{40,}\.[A-Za-z0-9_-]{20,}"),
    "bearer_token": re.compile(r"\bBearer\s+[A-Za-z0-9_.-]{30,}"),
    "aws_akia": re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
    "volc_key": re.compile(r"\bVOLC_(SECRET|ACCESS)_KEY\s*[=:]\s*['\"][A-Za-z0-9_-]+['\"]"),
}

CLAIM_LABEL_PATTERN = re.compile(
    r"\[(canonical fact|promoted_addendum-aware inference|candidate carry-forward|tentative candidate|candidate|evidence|boundary|risk|decision|audit|procedure|prompt-web-evidence|live-verified-\d{4}-\d{2}-\d{2}|paste-time|hypothetical|reference)\]",
    re.I,
)

MERMAID_PATTERN = re.compile(r"```mermaid", re.I)
FRONTMATTER_STATUS = re.compile(r"^status:\s*(.+)$", re.M)
FRONTMATTER_AUTHORITY = re.compile(r"^authority:\s*(.+)$", re.M)

STDOUT_FIELDS = [
    "files_count",
    "total_words_cjk_latin_approx",
    "total_thinking_minutes",
    "live_web_browsing_used",
    "self_audit_findings",
    "boundary_preservation_check",
    "ready_for_user_audit",
]


def estimate_words(text: str) -> int:
    cjk = len(re.findall(r"[一-鿿]", text))
    latin_tokens = len(re.findall(r"\b[A-Za-z][A-Za-z0-9_-]*\b", text))
    return cjk + latin_tokens


def sniff_file(path: Path):
    text = path.read_text(encoding="utf-8", errors="ignore")
    metrics = {
        "path": str(path),
        "name": path.name,
        "size": len(text),
        "words": estimate_words(text),
        "frontmatter_status": None,
        "frontmatter_authority": None,
        "boundary_hits": {},
        "secret_hits": {},
        "claim_labels": 0,
        "mermaid_blocks": 0,
    }

    fm_status = FRONTMATTER_STATUS.search(text[:2000])
    fm_authority = FRONTMATTER_AUTHORITY.search(text[:2000])
    metrics["frontmatter_status"] = fm_status.group(1).strip() if fm_status else None
    metrics["frontmatter_authority"] = fm_authority.group(1).strip() if fm_authority else None

    for name, pat in BOUNDARY_PATTERNS.items():
        hits = len(pat.findall(text))
        if hits:
            metrics["boundary_hits"][name] = hits

    for name, pat in SECRET_PATTERNS.items():
        hits = len(pat.findall(text))
        if hits:
            metrics["secret_hits"][name] = hits

    metrics["claim_labels"] = len(CLAIM_LABEL_PATTERN.findall(text))
    metrics["mermaid_blocks"] = len(MERMAID_PATTERN.findall(text))

    return metrics


def sniff_zip(zip_dir: Path):
    name = zip_dir.name
    files = sorted(zip_dir.glob("**/*.md"))

    agg = {
        "name": name,
        "files_count": len(files),
        "total_size": 0,
        "total_words": 0,
        "frontmatter_candidate_count": 0,
        "frontmatter_not_authority_count": 0,
        "frontmatter_missing_count": 0,
        "boundary_hits": {},
        "secret_hits": {},
        "claim_labels": 0,
        "mermaid_blocks": 0,
        "files_with_secret": [],
        "files_with_boundary_violation": [],
        "files_with_no_frontmatter_status": [],
        "readme_path": None,
        "self_audit_path": None,
        "master_path": None,
        "stdout_extracted": {},
    }

    for f in files:
        m = sniff_file(f)
        agg["total_size"] += m["size"]
        agg["total_words"] += m["words"]

        if m["frontmatter_status"]:
            if "candidate" in m["frontmatter_status"].lower():
                agg["frontmatter_candidate_count"] += 1
        else:
            agg["frontmatter_missing_count"] += 1
            agg["files_with_no_frontmatter_status"].append(f.name)

        if m["frontmatter_authority"] and "not-authority" in m["frontmatter_authority"].lower():
            agg["frontmatter_not_authority_count"] += 1

        for k, v in m["boundary_hits"].items():
            agg["boundary_hits"][k] = agg["boundary_hits"].get(k, 0) + v
            agg["files_with_boundary_violation"].append((f.name, k, v))

        for k, v in m["secret_hits"].items():
            agg["secret_hits"][k] = agg["secret_hits"].get(k, 0) + v
            agg["files_with_secret"].append((f.name, k, v))

        agg["claim_labels"] += m["claim_labels"]
        agg["mermaid_blocks"] += m["mermaid_blocks"]

        nm_low = f.name.lower()
        if "readme" in nm_low and ("deliverable" in nm_low or "index" in nm_low):
            agg["readme_path"] = str(f)
        if "self-audit" in nm_low or "self_audit" in nm_low:
            if not agg["self_audit_path"]:
                agg["self_audit_path"] = str(f)
        if ("master" in nm_low and ("atlas" in nm_low or "index" in nm_low or "roadmap" in nm_low)):
            if not agg["master_path"]:
                agg["master_path"] = str(f)

    if agg["readme_path"]:
        readme_text = Path(agg["readme_path"]).read_text(encoding="utf-8", errors="ignore")
        for fld in STDOUT_FIELDS:
            m = re.search(rf"^\s*{fld}\s*:\s*(.+?)\s*$", readme_text, re.M)
            if m:
                agg["stdout_extracted"][fld] = m.group(1).strip()

    return agg


def write_report(agg, audit_path):
    name = agg["name"]
    boundary_violations_set = set((f, k) for f, k, _ in agg["files_with_boundary_violation"])
    secret_set = set((f, k) for f, k, _ in agg["files_with_secret"])

    body = f"""---
title: Sniff Report — {name}
status: candidate / audit_report / not-authority
created_at: 2026-05-07
---

# Sniff Report — {name}

## §1 Quantity
| Metric | Value |
|---|---:|
| Files | {agg['files_count']} |
| Total size (bytes) | {agg['total_size']:,} |
| Total words (CJK+Latin token approx) | {agg['total_words']:,} |
| Avg words / file | {agg['total_words'] // max(agg['files_count'], 1):,} |
| Mermaid blocks | {agg['mermaid_blocks']} |
| Claim labels | {agg['claim_labels']} |

## §2 Frontmatter Discipline
| Metric | Value |
|---|---:|
| status: candidate | {agg['frontmatter_candidate_count']} / {agg['files_count']} ({100*agg['frontmatter_candidate_count']//max(agg['files_count'],1)}%) |
| authority: not-authority | {agg['frontmatter_not_authority_count']} / {agg['files_count']} ({100*agg['frontmatter_not_authority_count']//max(agg['files_count'],1)}%) |
| Missing status frontmatter | {agg['frontmatter_missing_count']} |
"""
    if agg["files_with_no_frontmatter_status"]:
        body += "\n**Files missing frontmatter status (sample ≤10):**\n"
        for f in agg["files_with_no_frontmatter_status"][:10]:
            body += f"- {f}\n"

    body += "\n## §3 Boundary Scan\n"
    if agg["boundary_hits"]:
        body += "| Pattern | Hits |\n|---|---:|\n"
        for k, v in sorted(agg["boundary_hits"].items()):
            body += f"| `{k}` | {v} |\n"
        body += f"\n⚠️ **{len(boundary_violations_set)} (file, pattern) pairs hit.** May be quote/reference; requires Phase B2 spot inspection.\n"
        body += "\n**Top 10 file-pattern pairs:**\n"
        for f, k in sorted(boundary_violations_set)[:10]:
            body += f"- `{f}` → `{k}`\n"
    else:
        body += "✅ No boundary regex hit\n"

    body += "\n## §4 Secret Scan\n"
    if agg["secret_hits"]:
        body += "| Pattern | Hits |\n|---|---:|\n"
        for k, v in sorted(agg["secret_hits"].items()):
            body += f"| `{k}` | {v} |\n"
        body += f"\n🚨 **{len(secret_set)} (file, pattern) pairs hit secret regex.** Inspect immediately.\n"
        body += "\n**Files:**\n"
        for f, k in sorted(secret_set):
            body += f"- `{f}` → `{k}`\n"
    else:
        body += "✅ No secret pattern hit\n"

    body += "\n## §5 Truthful Stdout (extracted from README)\n"
    if agg["stdout_extracted"]:
        body += "| Field | Value |\n|---|---|\n"
        for k, v in agg["stdout_extracted"].items():
            body += f"| {k} | {v} |\n"
    else:
        body += "⚠️ README not found or stdout fields not extracted\n"

    body += "\n## §6 Key Files Detected\n"
    body += f"- README: `{agg['readme_path'] or 'NOT FOUND'}`\n"
    body += f"- SELF-AUDIT: `{agg['self_audit_path'] or 'NOT FOUND'}`\n"
    body += f"- MASTER: `{agg['master_path'] or 'NOT FOUND'}`\n"

    body += "\n## §7 Sniff Verdict\n"
    verdict = "CLEAR"
    reasons = []
    if agg["secret_hits"]:
        verdict = "REJECT"
        reasons.append("secret pattern hit")
    if boundary_violations_set:
        if verdict == "CLEAR":
            verdict = "CONCERN"
        reasons.append(f"{len(boundary_violations_set)} boundary regex pairs (may be quote, inspect Phase B2)")
    if agg["frontmatter_missing_count"] > agg["files_count"] * 0.15:
        if verdict == "CLEAR":
            verdict = "CONCERN"
        reasons.append(f"{agg['frontmatter_missing_count']} files missing status frontmatter")
    cpct = 100 * agg["frontmatter_candidate_count"] // max(agg["files_count"], 1)
    if cpct < 80:
        if verdict == "CLEAR":
            verdict = "CONCERN"
        reasons.append(f"only {cpct}% files marked status: candidate")

    body += f"\n**Verdict: `{verdict}`**\n"
    if reasons:
        body += "\nReasons:\n"
        for r in reasons:
            body += f"- {r}\n"
    else:
        body += "\nNo issues detected by automated sniff.\n"

    audit_path.write_text(body, encoding="utf-8")


def write_master(aggs, master_path):
    body = """---
title: Sniff Master Summary — 16 ZIP overall
status: candidate / audit_report / not-authority
created_at: 2026-05-07
---

# Sniff Master Summary — 16 ZIP

> 自动化 sniff test for 16 cloud-output ZIPs under `outputs/`. 不替代人审; 是 Phase B2 spot check 的输入信号。

## §1 Quantity Overview
| ZIP | Files | Words | Mermaid | Claim Labels | Verdict |
|---|---:|---:|---:|---:|---|
"""
    total_files = 0
    total_words = 0
    total_mermaid = 0
    for a in aggs:
        v = "✅"
        if a["secret_hits"]:
            v = "🚨"
        elif a["boundary_hits"] or a["frontmatter_missing_count"] > a["files_count"] * 0.15:
            v = "⚠️"
        body += f"| `{a['name']}` | {a['files_count']} | {a['total_words']:,} | {a['mermaid_blocks']} | {a['claim_labels']} | {v} |\n"
        total_files += a["files_count"]
        total_words += a["total_words"]
        total_mermaid += a["mermaid_blocks"]
    body += f"| **TOTAL** | **{total_files}** | **{total_words:,}** | **{total_mermaid}** | — | — |\n"

    body += """
## §2 Frontmatter Discipline
| ZIP | candidate% | not-authority% | missing |
|---|---:|---:|---:|
"""
    for a in aggs:
        cpct = 100 * a["frontmatter_candidate_count"] // max(a["files_count"], 1)
        npct = 100 * a["frontmatter_not_authority_count"] // max(a["files_count"], 1)
        body += f"| `{a['name']}` | {cpct}% | {npct}% | {a['frontmatter_missing_count']} |\n"

    body += "\n## §3 Boundary Scan Cross-ZIP\n"
    any_boundary = False
    for a in aggs:
        if a["boundary_hits"]:
            any_boundary = True
            body += f"\n### {a['name']}\n"
            for k, v in sorted(a["boundary_hits"].items()):
                body += f"- `{k}`: {v} hits\n"
    if not any_boundary:
        body += "\n✅ **No boundary regex hits across 16 ZIP**\n"

    body += "\n## §4 Secret Scan Cross-ZIP\n"
    any_secret = False
    for a in aggs:
        if a["secret_hits"]:
            any_secret = True
            body += f"\n### {a['name']}\n"
            for k, v in sorted(a["secret_hits"].items()):
                body += f"- `{k}`: {v} hits\n"
    if not any_secret:
        body += "\n✅ **No secret pattern hits across 16 ZIP**\n"

    body += "\n## §5 Truthful Stdout Cross-ZIP\n"
    body += "| ZIP | files (self-rep) | thinking_min | live_web | self_audit | ready |\n|---|---|---|---|---|---|\n"
    for a in aggs:
        s = a["stdout_extracted"]
        body += f"| `{a['name']}` | {s.get('files_count', '?')} | {s.get('total_thinking_minutes', '?')} | {s.get('live_web_browsing_used', '?')} | {s.get('self_audit_findings', '?')} | {s.get('ready_for_user_audit', '?')} |\n"

    body += "\n## §6 Per-ZIP Verdict & Reasons\n"
    for a in aggs:
        verdict = "CLEAR"
        reasons = []
        if a["secret_hits"]:
            verdict = "REJECT"
            reasons.append("secret hit")
        boundary_pairs = set((f, k) for f, k, _ in a["files_with_boundary_violation"])
        if boundary_pairs:
            if verdict == "CLEAR":
                verdict = "CONCERN"
            reasons.append(f"{len(boundary_pairs)} boundary pairs")
        if a["frontmatter_missing_count"] > a["files_count"] * 0.15:
            if verdict == "CLEAR":
                verdict = "CONCERN"
            reasons.append(f"{a['frontmatter_missing_count']} missing frontmatter")
        cpct = 100 * a["frontmatter_candidate_count"] // max(a["files_count"], 1)
        if cpct < 80:
            if verdict == "CLEAR":
                verdict = "CONCERN"
            reasons.append(f"candidate% only {cpct}%")
        body += f"- **`{a['name']}`**: `{verdict}`"
        if reasons:
            body += f" — {', '.join(reasons)}"
        body += "\n"

    body += "\n## §7 Phase B2 Spot Check Targets\n"
    body += "Tier 1 (high promote probability): U1-deep, U2-deep, U3-deep, U4-visual-asset, U9-dispatch-catalog, U10-runbook, U11-anti-pattern, U13-visual-brand, U15-decision-log\n"
    body += "\nFor each Tier 1 ZIP, read README + SELF-AUDIT + MASTER + 2 random working files. Output `audit/02-spot-U[X].md`.\n"

    master_path.write_text(body, encoding="utf-8")


def main():
    audit_dir = AUDIT_DIR
    audit_dir.mkdir(parents=True, exist_ok=True)

    if not OUTPUTS_DIR.exists():
        print(f"❌ {OUTPUTS_DIR} not found. Run from strategic-upgrade/2026-05-07/.", file=sys.stderr)
        sys.exit(1)

    zip_dirs = sorted([d for d in OUTPUTS_DIR.iterdir() if d.is_dir()])
    print(f"Found {len(zip_dirs)} ZIP dirs to sniff")

    aggs = []
    for zd in zip_dirs:
        print(f"  Sniffing {zd.name}...", end=" ", flush=True)
        agg = sniff_zip(zd)
        aggs.append(agg)
        sniff_path = audit_dir / f"01-sniff-{zd.name}.md"
        write_report(agg, sniff_path)
        print(f"OK ({agg['files_count']} files, {agg['total_words']:,} words)")

    write_master(aggs, audit_dir / "00-sniff-master.md")
    print(f"\n✅ Sniff complete. Master report: {audit_dir / '00-sniff-master.md'}")
    print(f"   Per-ZIP reports: {audit_dir}/01-sniff-U*.md")


if __name__ == "__main__":
    main()
