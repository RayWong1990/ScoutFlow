---
status: candidate / not-authority / not-runtime-approval
created_for: Cloud Prompt U4 Visual Asset Spine
requested_date: 2026-05-07
generated_in_session_date: 2026-05-06
write_enabled: false
claim_scope: spec-only; no production code modification; no dispatch authorization
---

# README — U4 Visual Asset Spine deliverable index

> claim label: 100% for index accuracy of this ZIP; completeness is truthful-partial because live web and local PF-V CSV were unavailable.

## 1. Package contents

| # | file | role |
|---:|---|---|
| 1 | `MODULE-visual-asset-spec-2026-05-07.md` | visual asset schema, CRUD, thumbnail/pHash cron, state guard |
| 2 | `MODULE-prompt-template-spec-2026-05-07.md` | prompt registry schema, lineage, S00-S18 and Run-1~Run-5 backfill plan |
| 3 | `MODULE-design-token-spec-2026-05-07.md` | candidate Style Dictionary-compatible JSON and cascade/watch script |
| 4 | `MODULE-pattern-library-spec-2026-05-07.md` | Pattern A-J placeholders and multi-domain pattern registry |
| 5 | `CROSS-MODULE-CONTRACT-2026-05-07.md` | foreign-key/soft-link contract and lock-readiness queries |
| 6 | `SINGLE-USER-IMPLEMENTATION-BUDGET-2026-05-07.md` | ≤1500 LOC / ≤1 week implementation budget |
| 7 | `PF-V-INTEGRATION-MAP-2026-05-07.md` | PF-V INDEX.csv migration strategy and 19-column normalization target |
| 8 | `5-GATE-AUTOMATION-HOOKS-2026-05-07.md` | 5-Gate audit table, payload, state-machine lock guard |
| 9 | `LIVE-WEB-EVIDENCE-2026-05-07.md` | truthful no-live-web matrix + 28 URL seeds for future verification |
| 10 | `README-deliverable-index-2026-05-07.md` | this index, self-audit, stdout contract |

## 2. Boundary summary

This ZIP is candidate-only. It does not approve production code modifications, Capture Station CSS replacement, token package installation, browser automation, dispatch execution, vault true write, migration, BBDown runtime, media, ASR, or `audio_transcript`. The proposed SQLite writes are sidecar-only under `visual-assets/` or equivalent local paths.

## 3. Self-audit findings

| # | finding | disposition |
|---:|---|---|
| 1 | Prosumer DAM drift is the main scope risk. | Avoid roles, approvals, cloud sync, brand portal, CDN. |
| 2 | Minimalist YAGNI would fail because PF-V already has many images/prompts/patterns. | Keep hash, pHash, prompt, pattern, phase, gate fields. |
| 3 | Single-user assumption is preserved. | One writer, local SQLite, no RBAC. |
| 4 | visual_asset could be confused with ScoutFlow `artifact_assets`. | Mark sidecar visual inventory, not capture authority. |
| 5 | prompt_template could be mistaken for dispatch authorization. | All dispatch rows carry `authorization:none`. |
| 6 | S00-S18 bodies are not available. | Backfill placeholders only; never fabricate bodies. |
| 7 | Pattern A-J actual definitions are unavailable. | Candidate placeholders marked replaceable. |
| 8 | design tokens could be mistaken for production CSS contract. | Generated CSS writes outside app; no package install. |
| 9 | 5-Gate global rule file unavailable. | Use available H5 checklist and mark `needs_local_refresh`. |
| 10 | Render pass could be mislabeled visual pass. | Hook requires explicit five gate pass booleans. |
| 11 | Live web requirement could tempt fabricated vendor evidence. | Vendor file states not accessed, count 0. |
| 12 | PF-V CSV 19 columns are not present. | Importer is header-driven and dry-run first. |
| 13 | pHash duplicates may incorrectly merge variants. | pHash is advisory; sha256/file lineage remains primary. |
| 14 | `locked` state may look too authoritative. | Define as visual asset lock only, not product authority. |
| 15 | Token colors need accessibility validation. | Add contrast/gate checks before production use. |
| 16 | Cross-module links can break if DBs split. | Use soft-FK contract audit before lock/handoff. |
| 17 | Budget may be optimistic if PF-V CSV is messy. | One-week budget includes importer buffer. |
| 18 | Image-to-code tooling may overreach. | U4 records assets/prompts; code changes remain separate lane. |
| 19 | External vendor recommendations are stale without browsing. | Keep URL seeds only and future verification template. |
| 20 | The package cannot satisfy ≥120 min research literally. | Stdout reports actual session constraints, not inflated time. |

## 4. Truthful stdout contract

```yaml
CLOUD_U4_VISUAL_ASSET_SPINE_COMPLETE: false
completion_reason: "10 files produced, but live web browsing and local PF-V/current-rule refresh were unavailable"
zip_filename: cloud-output-U4-visual-asset-spine-2026-05-07.zip
files_count: 10
total_words_cjk_latin_approx: 22699
total_thinking_minutes: "not ≥120; single-session generation under environment constraints"
live_web_browsing_used: false
live_verified_vendor_count: 0
modules_specced: 4
sqlite_ddl_count: 10
python_pseudocode_loc_total: 260
single_user_budget_estimate_loc: 1250
single_user_budget_estimate_dev_days: "4.75-5.5 focused days / <=1 calendar week"
multi_pass_completed: "8/10"
self_audit_findings: 20
boundary_preservation_check: "clear; no production/runtime/write authorization"
ready_for_user_audit: yes
```

## 5. Recommended next audit step

Run a browse-enabled refresh for `LIVE-WEB-EVIDENCE-2026-05-07.md`, then provide the actual PF-V `INDEX.csv` so `PF-V-INTEGRATION-MAP` can be upgraded from header-driven migration design to concrete column mapping.


## 6. Package validation performed

```text
zip file created: cloud-output-U4-visual-asset-spine-2026-05-07.zip
file count: 10
folder source: /mnt/data/cloud-output-U4-visual-asset-spine-2026-05-07
all files: markdown
production code touched: no
live web used: no
```

The package intentionally includes the limitation inside the deliverables rather than hiding it in chat. That makes the ZIP itself auditable after download.

## 7. How to audit this ZIP

1. Open `README-deliverable-index-2026-05-07.md` and check stdout.
2. Open `LIVE-WEB-EVIDENCE-2026-05-07.md` and confirm it does not claim live browsing.
3. Open module files 1-4 and confirm each has `candidate / not-authority` boundaries.
4. Check that all production-sensitive actions are described as candidate scripts or sidecar writes.
5. Check `5-GATE-AUTOMATION-HOOKS` to confirm `locked` requires all five gates.
6. Check `PF-V-INTEGRATION-MAP` to confirm the importer is header-driven and does not assume actual CSV headers.

## 8. Known incomplete items

| item | why incomplete | next input needed |
|---|---|---|
| live vendor evidence | browser disabled | browse-enabled session |
| PF-V INDEX concrete mapping | actual CSV not uploaded | `INDEX.csv` or header sample |
| S00-S18 prompt bodies | bodies not provided | prompt files / session exports |
| Pattern A-J canon | actual definitions not provided | PF-V pattern notes |
| canonical 5-Gate file | local file unavailable | `~/.claude/rules/aesthetic-first-principles.md` contents |

## 9. Handoff note

The deliverable is still useful because the hardest product decision is not vendor comparison; it is preserving the boundary between high-horsepower visual iteration and ScoutFlow authority discipline. The ZIP gives a concrete schema and script plan for that boundary. The missing inputs should refine names, evidence counts, and exact backfill mappings, not overturn the core sidecar architecture unless a future audit finds a direct conflict.


## 10. Minimum word-count note

The package was expanded to meet the requested deep-research shape as closely as possible under the disabled-web constraint. The count in stdout uses an approximate `CJK character + Latin token` method, because Chinese text does not split into whitespace-delimited words cleanly.

## 11. Final boundary assertion

No generated file claims that live web was browsed. No generated file claims PF-V `INDEX.csv` was read. No generated file claims the canonical global 5-Gate file was read. The architecture, however, is fully specified enough for a user audit and for a later implementation pass once those inputs are supplied.


## 12. Audit-ready summary

This deliverable gives the user a concrete sidecar architecture for four native visual support planes: visual assets, prompts, tokens, and patterns. It also includes the critical glue: cross-module contract, PF-V import map, 5-Gate lock hook, budget, and evidence limitations. The right next move is not to merge code; it is to audit the candidate spec against the missing PF-V/local/live inputs.

## 13. File count verification

The ZIP contains exactly the 10 requested markdown files and no hidden production patch. The directory version under `/mnt/data/cloud-output-U4-visual-asset-spine-2026-05-07/` mirrors the ZIP entries for quick inspection.


## Audit note

本包的价值在于把 U4 的四类视觉原生横切面先做成可落地骨架：表、字段、状态、互通 query、CLI 行为、预算、PF-V 回填、5-Gate 自动化。它不是最终 authority，也不是 production patch。审计时建议先看 README 的 truthful stdout，再看 LIVE-WEB-EVIDENCE 的限制说明，最后审四个 MODULE 文件是否符合“prosumer but not minimalist”的定位。

若后续补齐 live web 和本地 PF-V INDEX.csv，本包最适合升级的地方是：把 `needs_local_refresh` 条目替换成真实文件行、把 vendor 候选改成 verified evidence、把 S00-S18 prompt stub 补成真实 lineage。
