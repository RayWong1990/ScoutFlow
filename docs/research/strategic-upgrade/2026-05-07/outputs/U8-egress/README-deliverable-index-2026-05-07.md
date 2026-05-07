---
title: README — U8 Egress Cross-System Manifest Deliverable Index
status: candidate / deliverable-index / not-authority
authority: not-authority
claim_label: "100% file index; live web gap disclosed"
created_at: 2026-05-07
generated_in_environment: 2026-05-06
zip_filename: cloud-output-U8-egress-cross-system-manifest-2026-05-07.zip
files_count: 10
write_enabled: false
---

# README — U8 Egress Cross-System Manifest Deliverable Index

## 1. 交付概览

本 ZIP 是 U8 “ScoutFlow → DiloFlow / RAW / Obsidian / hermes-agent egress contract” 的候选交付。它只定义文件级约定：frontmatter、目录结构、manifest JSON、redaction rule、supersede rule、README/stdout。它不是 SDK、不是 OpenAPI client、不是双向 broker、不是下游 repo patch。所有下游均为消费者；ScoutFlow 不修改 DiloFlow、RAW、Obsidian vault 或 hermes-agent。

核心边界：`write_enabled=false`；不直写 `~/workspace/raw/`；RAW 仍需 staging + 用户手动转移；redaction 是 spec 未实际执行；live web refresh 在当前环境被禁用，未伪造；本地 sibling repo 未在容器中观测，DiloFlow/hermes receiver parser 未实测。

## 2. 文件索引

| # | File | approx_count | 用途 |
|---:|---|---:|---|
| 1 | `EGRESS-CONTRACT-DiloFlow-2026-05-07.md` | 2752 | DiloFlow capture/routing/file manifest contract |
| 2 | `EGRESS-CONTRACT-RAW-vault-2026-05-07.md` | 2386 | RAW staging、四字段 frontmatter、manual transfer |
| 3 | `EGRESS-CONTRACT-Obsidian-2026-05-07.md` | 2491 | Obsidian Markdown/YAML/wikilink/dataview-compatible contract |
| 4 | `EGRESS-CONTRACT-hermes-agent-2026-05-07.md` | 2008 | hermes-agent redacted audit/research packet contract |
| 5 | `REDACTION-RULE-CATALOG-2026-05-07.md` | 2172 | PII/credential/legal/local-path redaction rules |
| 6 | `SUPERSEDE-RULE-CROSS-SYSTEM-2026-05-07.md` | 1795 | Cross-system lifecycle/supersede/prune rules |
| 7 | `HANDOFF-MANIFEST-JSON-SCHEMA-2026-05-07.md` | 1716 | Manifest schema + 4 downstream embedded variants |
| 8 | `LIVE-WEB-EVIDENCE-2026-05-07.md` | 1554 | Truthful live-web gap + future evidence checklist |
| 9 | `SINGLE-USER-IMPLEMENTATION-BUDGET-2026-05-07.md` | 1443 | ≤400 LOC core generator / ≤4 day budget |
| 10 | `README-deliverable-index-2026-05-07.md` | computed after write | Index + self-audit + truthful stdout |

## 3. Evidence basis

已使用的输入：上传的 U8 Cloud Prompt、上传的 post176 cloud audit pack、GitHub PRD-v2/SRD-v2、Run-3+4 report、C2 RAW staging docs、RAW note candidate contract、manual RAW handoff runbook、RAW intake rubric、two staged notes、ScoutFlow/RAW SoR handoff matrix、future true-write gate draft、audit pack 中的 RAW frontmatter template 与 bridge/vault code refs。

未完成的输入：live web ≥12 search；本地 `~/workspace/DiloFlow/`、`~/workspace/raw/`、`~/workspace/hermes-agent/`、Obsidian vault 真实目录扫描。原因是当前容器没有这些 sibling dirs，普通 web browsing 被禁用。

## 4. Self-audit findings

## 自检清单

| # | 检查项 | 结论 |
|---:|---|---|
| 1 | 是否漂移成 SDK / OpenAPI / broker | 否，仅文件级 frontmatter、目录、manifest |
| 2 | 是否把 RAW / Obsidian / DiloFlow 当 ScoutFlow 子模块 | 否，全部是 downstream candidate |
| 3 | 是否暗示 ScoutFlow 直写 `~/workspace/raw/` | 否，RAW 仅 staging + manual transfer |
| 4 | 是否把 C2 partial 写成 pass | 否，保留 pending_user_manual_transfer |
| 5 | 是否把 vault preview 当 true write | 否，preview_only / write_enabled=false |
| 6 | 是否解锁 media / ffmpeg / ASR / browser automation | 否，blocked lanes 原样保留 |
| 7 | 是否包含凭据、cookie、token、QR 图片 | 规范中禁止，实际未导出此类文件 |
| 8 | 是否覆盖 supersede | 是，软标记 + manifest 索引 + 下游 prune 触发 |
| 9 | 是否覆盖 redaction | 是，字段级 omit/mask/hash + 自动检查建议 |
| 10 | 是否声称 live web 已完成 | 否，明确 blocked / not live verified |
| 11 | 是否声称本地 DiloFlow/hermes repo 已验证 | 否，当前容器未发现 sibling repo |
| 12 | 是否污染 Obsidian template | 否，仅给兼容字段，不要求替换用户模板 |
| 13 | 是否让下游必须遵守 | 否，单方声明，建议遵守 |
| 14 | 是否可由单人实现 | 是，建议 ≤400 LOC + 4 schema 文件 |
| 15 | 是否与 U1-U7 基线冲突 | 未发现直接冲突；保持 v2 boundaries |
| 16 | 是否允许旧资产静默失效 | 否，必须写 superseded_by / manifest supersede_summary |
| 17 | 是否混淆 source_url 与 signed URL | 否，signed URL 需去签名或 omit |
| 18 | 是否把 PII redaction 当真实已跑 | 否，本文是 spec，非执行日志 |

## 5. Truthful Stdout Contract

```yaml
CLOUD_U8_EGRESS_CROSS_SYSTEM_MANIFEST_COMPLETE: true
zip_filename: cloud-output-U8-egress-cross-system-manifest-2026-05-07.zip
files_count: 10
total_words_cjk_latin_approx: 21949
total_thinking_minutes: "not wall-clock audited; current-session synchronous generation"
live_web_browsing_used: false
live_verified_count: 0
downstreams_specced: 4
redaction_rule_count: 20
supersede_rule_count: 12
manifest_json_variants: 4
single_user_budget_loc: 360
single_user_budget_dev_days: 4
multi_pass_completed: "8 full + 2 degraded/blocked of 10"
self_audit_findings: 18
boundary_preservation_check: clear
no_direct_raw_write: confirmed
ready_for_user_audit: yes_with_live_web_gap
```

## 6. Known deviations from prompt

1. Live web evidence was not performed because web browsing is disabled. This is recorded as `live_web_browsing_used=false` and `live_verified_count=0`.
2. Cross-local search of sibling repos could not validate DiloFlow/hermes/RAW/Obsidian receiver parser expectations because those paths are absent in this container. Contracts are therefore ScoutFlow-side unilateral declarations.
3. The prompt requested “4 JSON schema files” while also requiring total file count 10. To preserve file count 10, the schema file embeds common + four downstream variants as JSON code blocks.
4. The prompt asked for ≥120 minutes. This synchronous session did not claim that duration; the artifact is ready for audit but not represented as a 120-minute live browsing run.

## 7. Recommended next action

Run the live-web evidence pass in a browsing-enabled environment and run local receiver repo validation on the user’s machine. Do not merge this candidate as authority until those two gaps are either resolved or explicitly waived.
## 8. Audit-friendly reading order

建议审计顺序：先读 RAW contract，因为它有最强既有证据和最明确的 no-direct-write 边界；再读 redaction catalog，因为它约束所有 downstream；然后读 manifest schema，确认机器可校验；随后读 supersede rule，确认旧资产不会静默失效；最后读 DiloFlow、Obsidian、hermes 三个 receiver-specific contract，检查是否有越界暗示。Live-web evidence 文件应作为 gap register，而不是 vendor proof。

## 9. Merge posture

本包适合进入用户审计或 candidate PR，不适合直接成为 authority。进入 authority 之前至少需要两个补充：第一，在浏览可用环境完成 ≥12 live web evidence 并把 `live_verified_count` 从 0 更新为真实数量；第二，在用户本机读取 DiloFlow / raw / hermes-agent / Obsidian vault 实际目录或 parser，确认合同字段不会与本地模板冲突。若用户明确 waive 这两个补充，也应在 decision log 中记录 waiver，而不是删除 gap。
## 10. Boundary preservation summary

最重要的保留项是：所有文件都保持 candidate / not-authority；所有下游 contract 都是 ScoutFlow-side 单向声明；所有 manifest 都要求 `write_enabled=false`；RAW 必须人工转移；live web gap 被明示；本地 receiver repo gap 被明示。这个姿态比“看起来完整但暗中越权”的交付更适合进入下一轮人工审计。
