---
title: EGRESS CONTRACT — ScoutFlow to hermes-agent
status: candidate / egress-contract / not-authority
authority: not-authority
claim_label: "95% for ScoutFlow-side packet shape; hermes-agent repo not locally verified"
created_at: 2026-05-07
generated_in_environment: 2026-05-06
target_downstream: hermes-agent
write_enabled: false
local_receiver_repo_observed: false
---

# EGRESS CONTRACT — ScoutFlow → hermes-agent

## 0. 证据与边界口径

本交付只声明 ScoutFlow 单方面写出的文件级 egress contract，不定义 SDK、OpenAPI client、双向同步 broker，也不修改任何下游。PRD v2 的最高边界是：ScoutFlow 是单 user、local-first 的采集与证据工作台；RAW、Obsidian、DiloFlow 是下游消费者，不是 ScoutFlow 项目的一部分。SRD v2 的最高边界是：当前生效的是 metadata-only、receipt、trust trace、redaction/secret scan baseline；Phase 2+ 对象仍主要是 outline，不能被文件导出契约误读成 runtime unlock。

本环境已经读取上传的 post176 audit pack 与 GitHub 上的 PRD/SRD、Run-3+4 C2 文件。普通 live web 浏览在当前会话被禁用，所以本文所有外部 vendor/frontmatter 口径只作为“需刷新验证的公共模式候选”，不标记为 live verified。`~/workspace/DiloFlow/`、`~/workspace/raw/`、`~/workspace/hermes-agent/` 与 Obsidian 本地 vault 在当前容器没有出现；因此 DiloFlow 与 hermes-agent 的 receiver-side parser 只能给出单方、保守、低耦合的文件契约，不能声称已经被下游 repo 实测接受。

硬边界在所有下游一致：`write_enabled=false` 保持；ScoutFlow 永不直写 `~/workspace/raw/`；凭据、cookie、token、QR 图片、browser profile path、auth sidecar、raw stdout/stderr 中可能含秘密的片段不得进入 egress；Bilibili/XHS 等平台原作者隐私字段只允许最小必要、脱敏后的事实摘要；manifest 是一次 handoff 的索引，不是下游 acceptance 证明；supersede 只能标记资产生命周期，不允许反向覆盖下游知识库事实。

## 1. hermes-agent 合同定位

hermes-agent 在本合同中被视为“OpenAI venv side process / audit-related candidate research consumer”。它可以读取 ScoutFlow 准备好的候选研究包、审计包或 redacted evidence summary，但不应该获得原始凭据、浏览器登录态、raw API response、未脱敏平台隐私字段，也不应该反向写 ScoutFlow authority。由于当前容器没有 `~/workspace/hermes-agent/`，本文不声称了解其真实 CLI、venv 路径、queue 文件格式或 importer；因此合同采用最小 packet：`manifest.json` + `task.md` + `context.md` + `redaction-report.json`。

## 2. hermes 可接收资产

| kind | 用途 | 是否允许 | 说明 |
|---|---|---:|---|
| `hermes_research_packet` | 候选研究问题与上下文 | yes | 只含 redacted summary |
| `audit_packet` | 让 hermes 审计 contract 或 manifest | yes | 不含 secrets/raw stdout |
| `candidate_topic_brief` | topic card / signal 的安全摘要 | yes | 不触发 capture |
| `receipt_summary` | evidence ledger 摘要 | yes | 只读 locator |
| `raw_api_response` | 原始平台响应 | no | 即便脱敏也不默认交给 LLM side process |
| `credential_context` | 登录、cookie、QR、profile | no | 永不出现在 egress |
| `execution_request` | 让 hermes 执行 runtime | no by default | U8 不是 runtime approval |

## 3. 目录结构

推荐 staging：

```text
ScoutFlow/docs/research/post-frozen/egress-staging/hermes-agent/<YYYY-MM-DD>/<handoff_id>/
  manifest.json
  task.md
  context.md
  assets/
    sfa_<capture_id>_hermes_research_packet_r001.md
  receipts/
    redaction-report.json
    checksum-report.json
```

`task.md` 是 hermes 看到的任务说明；`context.md` 是红线与证据摘要；`assets/*.md` 是可选素材卡。ScoutFlow 不写 hermes-agent repo、不激活 venv、不调用 OpenAI API、不启动 background process。

## 2. 通用字段字典

| 字段 | 必填 | 类型 | 说明 | 红线 |
|---|---:|---|---|---|
| `schema_version` | yes | string | 当前建议 `scoutflow.egress.v1` | 不得省略，避免下游猜格式 |
| `handoff_id` | yes | string | 一次 handoff 的稳定 ID，建议 `sfh_YYYYMMDD_<ulid>` | 不用路径或 URL 充当 ID |
| `asset_id` | yes | string | 单个导出资产 ID，建议 `sfa_<capture_id>_<kind>_<rev>` | 不得含 `/`、`\`、`..` |
| `kind` | yes | enum | `topic_card`, `raw_note_candidate`, `obsidian_note`, `diloflow_capture`, `hermes_research_packet`, `signal`, `receipt_summary` | 不得把 blocked runtime 输出伪装成已批准 kind |
| `source_url` | conditional | string | 原始入口 URL；允许 canonical URL | signed URL / tokenized URL 必须去签名或 omit |
| `source_platform` | conditional | enum/string | `bilibili`, `xhs`, `youtube_later`, `manual`, `unknown` | 当前不因字段存在而解锁平台 runtime |
| `capture_id` | conditional | string | ScoutFlow authority 侧 capture 主键 | 仅 locator，不是下游 SoR |
| `created_at` | yes | RFC3339 | 资产创建时间 | 不用本地自然语言日期 |
| `captured_at` | no | RFC3339 | 外部素材采集时间 | 不得暴露浏览器 profile 或登录态 |
| `scoutflow_version` | yes | string | ScoutFlow 版本、commit 或 doc baseline | 不能用 live PR 猜测 |
| `origin` | yes | object | `system`, `run_id`, `dispatch`, `operator` 摘要 | operator 只写角色，不写个人敏感信息 |
| `redaction` | yes | object | `applied`, `ruleset_version`, `findings_count`, `masked_fields` | `applied=false` 时不得进入 durable egress |
| `supersede` | yes | object | `status`, `supersedes`, `superseded_by`, `reason` | 不允许删除旧资产，先软标记 |
| `checksums` | yes | object | `sha256`, `size_bytes`, `content_encoding` | checksum 只对 redacted payload 计算 |
| `visibility` | yes | enum | `local_only`, `downstream_candidate`, `public_safe` | 默认 `local_only`，除非另有人工批准 |
| `acceptance_state` | yes | enum | `prepared`, `staged`, `pending_user_transfer`, `accepted`, `needs_edit`, `rejected`, `superseded` | ScoutFlow 只能写自己知道的状态 |

## 4. hermes task.md schema

```markdown
---
schema_version: scoutflow.egress.v1
handoff_id: sfh_20260507_hermes_01
target_downstream: hermes-agent
kind: hermes_research_packet
created_at: "2026-05-07T00:00:00Z"
write_enabled: false
execution_approval: false
runtime_approval: false
redaction_applied: true
visibility: local_only
---

# Hermes Task

## Mission
Audit the attached ScoutFlow candidate packet. Do not execute browser automation, media download, ASR, credential access, or downstream writes.

## Inputs
- manifest: `manifest.json`
- context: `context.md`
- assets: `assets/*.md`

## Required Output
- audit verdict: pass | needs_edit | reject | insufficient_evidence
- findings: list concrete contract issues
- do_not_include: secrets, raw platform responses, personal data
```

## 5. context.md schema

```markdown
# Context

## ScoutFlow Boundary
- ScoutFlow is local-first and single-user.
- Current valid runtime is metadata-only evidence / receipt / trust trace.
- RAW, Obsidian, DiloFlow, hermes-agent are downstream consumers.

## Blocked Lanes
- media download
- ffmpeg
- ASR
- browser automation
- audio_transcript
- direct RAW write

## Evidence Summary
- PRD/SRD baseline: v2 2026-05-04
- Run status: C2 partial until manual RAW transfer and RAW intake evidence

## Redaction
- redaction_applied: true
- forbidden fields: cookie, token, qrcode, browser profile path, signed URL, private author fields
```

## 6. hermes manifest variant

```json
{
  "schema_version": "scoutflow.egress.v1",
  "target_downstream": "hermes-agent",
  "handoff_id": "sfh_20260507_hermes_01",
  "created_at": "2026-05-07T00:00:00Z",
  "write_enabled": false,
  "execution_approval": false,
  "runtime_approval": false,
  "allowed_operations": ["read_manifest", "read_redacted_markdown", "produce_audit_report"],
  "forbidden_operations": [
    "browser_automation",
    "media_download",
    "asr",
    "credential_access",
    "raw_vault_write",
    "scoutflow_db_write"
  ],
  "assets": [
    {
      "asset_id": "sfa_01K..._hermes_research_packet_r001",
      "kind": "hermes_research_packet",
      "relative_path": "assets/sfa_01K..._hermes_research_packet_r001.md",
      "input_budget_hint": {"max_tokens": 4000, "must_not_include_raw_api": true},
      "checksums": {"sha256": "<hash>", "size_bytes": 4096},
      "redaction": {"applied": true, "ruleset_version": "scoutflow-redaction-v1"},
      "supersede": {"status": "active", "supersedes": [], "superseded_by": null}
    }
  ]
}
```

## 7. LLM/agent 专属 redaction 要求

LLM side process 风险不同于 RAW/Obsidian：上下文可能被模型供应商处理，且长上下文更容易夹带敏感残影。因此 hermes-agent variant 默认最小化：只给摘要，不给原始 JSON；只给 canonical_url，不给 signed query；只给公开 platform_item_id，不给评论用户列表；只给 redacted trust trace locator，不给本地文件绝对路径；只给 findings_count，不给 secret scan 命中原文。任何需要更完整 evidence 的审计，都应在 ScoutFlow 本地人工打开，不应自动传给 hermes。

## 8. 输出回读约定

如果 hermes-agent 产生审计报告，建议由用户手动放入：

```text
ScoutFlow/docs/research/post-frozen/hermes-readback/<handoff_id>/HERMES-AUDIT-READBACK.md
```

回读报告字段：`handoff_id`, `asset_ids_reviewed`, `verdict`, `findings`, `redaction_concerns`, `schema_concerns`, `boundary_concerns`, `recommended_next_action`。ScoutFlow 只有在单独 readback task 中读取该报告；该报告本身不是 authority，除非另有 authority writeback。

## 9. 失败与停止条件

- manifest `redaction_summary.applied=false`：停止。
- `forbidden_operations` 缺失：停止。
- `execution_approval=true` 或 `runtime_approval=true`：停止。
- 资产包含 raw API response、credential、browser path、QR、cookie/token：停止。
- checksum 不匹配：停止。
- hermes 输出建议 direct RAW write：标记 boundary finding，不执行。

## 10. 单人实现建议

实现 hermes egress 不需要新服务。一个 `build_hermes_packet()` 函数读取 redacted summary、生成 task/context/assets、计算 checksum、写 manifest 到 staging 即可。不要调用 hermes，不要启动 subprocess，不要做 OpenAI request；U8 只定义文件包。

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
