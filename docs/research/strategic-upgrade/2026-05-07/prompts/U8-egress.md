---
title: Cloud Prompt — U8 Egress & Cross-System Manifest (DiloFlow / RAW / Obsidian / hermes-agent 交付契约)
status: candidate / cloud_prompt / not-authority
authority: not-authority
created_at: 2026-05-07
target_window: GPT Pro web 浏览模式
new_lane: yes
---

# Cloud Prompt — U8 Egress & Cross-System Manifest

## §1 Mission

PRD-v2 §0.1 已声明: "RAW / Obsidian / DiloFlow 是下游消费者, 不是本项目的一部分". 但**当前没有定义 ScoutFlow 写出去的格式**, 下游每次都在猜. 这导致:
- DiloFlow / RAW 读 ScoutFlow 输出时各自实现 parser, 字段命名不一致
- ScoutFlow 偶尔 output 字段变化, 下游静默坏掉
- 没有 redaction rule (法律敏感字段 / PII / 凭据残影 是否过滤)
- 没有 handoff manifest (一次 handoff 含哪些 asset / 时间戳 / origin)
- 没有 supersede 规则 (旧版本 asset 是否仍有效)

本任务: 写 ScoutFlow → 4 下游的 egress contract — **不是 SDK / OpenAPI client, 是文件级约定 (frontmatter / 目录结构 / handoff manifest JSON)** + redaction rule + supersede rule. 单人量级 (≤400 行 Python + 4 个 JSON schema 文件).

## §2 Inputs

1. https://github.com/RayWong1990/ScoutFlow/blob/main/docs/PRD-v2-2026-05-04.md (§0.1 下游声明)
2. https://github.com/RayWong1990/ScoutFlow/blob/main/docs/SRD-v2-2026-05-04.md
3. https://github.com/RayWong1990/ScoutFlow/blob/main/docs/research/post-frozen/raw-handoff-staging/ (Run-3+4 staging 文件集 — 既有约定参考)
4. ~/workspace/DiloFlow/ (sibling, 看其 capture 输入格式期望)
5. ~/workspace/raw/ 既有目录结构 (ScoutFlow 不写, 但 DiloFlow / 用户读)
6. Obsidian vault 默认 frontmatter 约定
7. ~/workspace/hermes-agent/ openai venv side process
8. **Live web** 真实 search 2026 inter-app data exchange / frontmatter 约定 / Markdown export

## §3 Multi-pass Work Plan (≥10 pass, ≥120 min)

1. **Pass 1**: 读 PRD §0.1 + raw-handoff-staging 实际 5 partial dispatch (PF-C2-06/07/08/09/11) + DiloFlow / hermes-agent 期望
2. **Pass 2 — Live web**: 真实 search ≥12: Obsidian frontmatter convention 2026 / Logseq / Tana export / Capacities export / inter-app Markdown / YAML frontmatter standard / digital data egress pattern / Heptabase / Reflect / static site generator frontmatter (Hugo / Jekyll) / file-based event sourcing
3. **Pass 3 — DiloFlow egress contract**: 
   - DiloFlow 期望 capture 输入是什么 (channel-related / 看见看不见 metadata)
   - frontmatter schema (asset_id / kind / source_url / capture_at / scoutflow_version / superseded_by)
   - 目录结构 (按 channel / 按时间 / 按 cluster?)
   - handoff manifest JSON (一次 handoff 的 asset list + timestamp + checksum)
4. **Pass 4 — RAW vault egress contract**: 
   - RAW vault 既有约定 (从 raw-handoff-staging 反推)
   - 哪些 ScoutFlow 输出会被 RAW 接受 (topic_card / signal / not signal-workbench-derived)
   - 写入路径约定 (永不直写 ~/workspace/raw/, 经 staging + 用户手动转)
   - supersede rule (新版本如何标记替代旧)
5. **Pass 5 — Obsidian egress contract**: 
   - Obsidian frontmatter (双链 [[wikilink]] / tags / aliases)
   - 兼容 Obsidian Sync / Obsidian Publish / dataview plugin
   - 不污染 Obsidian template (用户可能有现有 template)
6. **Pass 6 — hermes-agent egress contract**: 
   - hermes-agent (openai venv) 期望读什么 (audit-related / candidate research)
   - 路径约定
7. **Pass 7 — Redaction rule**: 
   - PII / 凭据 / 浏览器 profile 路径 / QR 图片 永不出现在 egress
   - 法律敏感 (Bilibili 抓取的原作者隐私字段) 必须 mask 或 omit
   - 自动化检查 (regex + word boundary)
8. **Pass 8 — Supersede rule**: 旧版本 asset 如何标记 deprecated / superseded_by, 下游何时 prune
9. **Pass 9 — Self-audit ≥15**
10. **Pass 10**: README + truthful stdout

## §4 Hard Boundaries

- candidate / not-authority
- write_enabled=False 不变
- 不批准实际写 ~/workspace/raw/ (永远经 staging + 用户手动)
- 不修改 DiloFlow / Obsidian vault / hermes-agent 任何内容
- redaction rule 仅 spec, 不实际跑
- 4 下游 contract 是 ScoutFlow 单方面声明, 下游不被强制 (但建议遵守)

## §5 Live Web Evidence Refresh

≥12 真实 search:
- Obsidian frontmatter / Logseq / Tana / Capacities export 2026
- YAML frontmatter standard
- Inter-app Markdown exchange pattern 2026
- Static site generator frontmatter (Hugo / Jekyll / 11ty)
- File-based event sourcing
- Heptabase / Reflect 2026
- File-system-as-database pattern
- PII redaction in Markdown (regex / NER)
- Apple Spotlight metadata / xattr 2026

## §6 Cross-local Search

- ~/workspace/DiloFlow/ 全文递归 — 找其期望的 capture 输入 schema
- ~/workspace/raw/ 既有目录结构 (read only)
- ~/workspace/contentflow/ legacy egress 沉淀
- ~/workspace/hermes-agent/ 期望
- ~/Library/Application Support/Obsidian/ (用户有 Obsidian vault?)
- ScoutFlow raw-handoff-staging 5 partial dispatch staging 文件

## §7 Output Deliverables

ZIP filename: `cloud-output-U8-egress-cross-system-manifest-2026-05-07.zip`
File count: **10**

| # | File | min 字 | claim label |
|---|---|---:|---|
| 1 | EGRESS-CONTRACT-DiloFlow-2026-05-07.md | 2500 (frontmatter schema + 目录 + manifest JSON) | ≥95% |
| 2 | EGRESS-CONTRACT-RAW-vault-2026-05-07.md | 2500 (从 staging 反推 + 用户手动转规则) | ≥95% |
| 3 | EGRESS-CONTRACT-Obsidian-2026-05-07.md | 2200 (双链 / tags / dataview 兼容) | ≥95% |
| 4 | EGRESS-CONTRACT-hermes-agent-2026-05-07.md | 1800 | ≥95% |
| 5 | REDACTION-RULE-CATALOG-2026-05-07.md | 2500 (PII / 凭据 / 法律 / 自动化检查) | ≥95% |
| 6 | SUPERSEDE-RULE-CROSS-SYSTEM-2026-05-07.md | 2000 (旧版本标记 + 下游 prune 触发) | ≥95% |
| 7 | HANDOFF-MANIFEST-JSON-SCHEMA-2026-05-07.md | 2000 (manifest.json schema + 4 下游变体) | ≥95% |
| 8 | LIVE-WEB-EVIDENCE-2026-05-07.md | 2200 (≥12 vendor + 访问日期) | ≥95% |
| 9 | SINGLE-USER-IMPLEMENTATION-BUDGET-2026-05-07.md | 1500 (≤400 行 + 4 JSON schema / ≤4 天) | ≥95% |
| 10 | README-deliverable-index-2026-05-07.md | 1200 | 100% |

总字数 ≥**20000**

## §8 Self-audit (≥15)

- 是否漂移成 SDK / OpenAPI / bi-directional broker (企业 pattern)
- 单人 4 下游真实 vs 假想下游
- redaction rule 是否真覆盖 PRD 红线
- supersede rule 是否会破坏 RAW vault 既有约定
- live web URL 真访问
- 与 U1-U7 是否冲突
- 是否暗示 ScoutFlow 直写 ~/workspace/raw/ (永远不许)
- single-user budget 真实

## §9 Truthful Stdout Contract

```yaml
CLOUD_U8_EGRESS_CROSS_SYSTEM_MANIFEST_COMPLETE: true
zip_filename: cloud-output-U8-egress-cross-system-manifest-2026-05-07.zip
files_count: 10
total_words_cjk_latin_approx: <真实>
total_thinking_minutes: <真实>
live_web_browsing_used: <true|false>
live_verified_count: <真实>
downstreams_specced: 4
redaction_rule_count: <真实>
supersede_rule_count: <真实>
manifest_json_variants: 4
single_user_budget_loc: <真实>
single_user_budget_dev_days: <真实>
multi_pass_completed: <真实/10>
self_audit_findings: <真实>
boundary_preservation_check: clear
no_direct_raw_write: confirmed
ready_for_user_audit: yes
```

## §10 ZIP Filename

`cloud-output-U8-egress-cross-system-manifest-2026-05-07.zip`
