---
title: EGRESS CONTRACT — ScoutFlow to Obsidian
status: candidate / egress-contract / not-authority
authority: not-authority
claim_label: "95% for conservative Markdown/YAML compatibility; live vendor refresh blocked"
created_at: 2026-05-07
generated_in_environment: 2026-05-06
target_downstream: Obsidian vault
write_enabled: false
live_web_verified: false
---

# EGRESS CONTRACT — ScoutFlow → Obsidian

## 0. 证据与边界口径

本交付只声明 ScoutFlow 单方面写出的文件级 egress contract，不定义 SDK、OpenAPI client、双向同步 broker，也不修改任何下游。PRD v2 的最高边界是：ScoutFlow 是单 user、local-first 的采集与证据工作台；RAW、Obsidian、DiloFlow 是下游消费者，不是 ScoutFlow 项目的一部分。SRD v2 的最高边界是：当前生效的是 metadata-only、receipt、trust trace、redaction/secret scan baseline；Phase 2+ 对象仍主要是 outline，不能被文件导出契约误读成 runtime unlock。

本环境已经读取上传的 post176 audit pack 与 GitHub 上的 PRD/SRD、Run-3+4 C2 文件。普通 live web 浏览在当前会话被禁用，所以本文所有外部 vendor/frontmatter 口径只作为“需刷新验证的公共模式候选”，不标记为 live verified。`~/workspace/DiloFlow/`、`~/workspace/raw/`、`~/workspace/hermes-agent/` 与 Obsidian 本地 vault 在当前容器没有出现；因此 DiloFlow 与 hermes-agent 的 receiver-side parser 只能给出单方、保守、低耦合的文件契约，不能声称已经被下游 repo 实测接受。

硬边界在所有下游一致：`write_enabled=false` 保持；ScoutFlow 永不直写 `~/workspace/raw/`；凭据、cookie、token、QR 图片、browser profile path、auth sidecar、raw stdout/stderr 中可能含秘密的片段不得进入 egress；Bilibili/XHS 等平台原作者隐私字段只允许最小必要、脱敏后的事实摘要；manifest 是一次 handoff 的索引，不是下游 acceptance 证明；supersede 只能标记资产生命周期，不允许反向覆盖下游知识库事实。

## 1. Obsidian 合同的定位

Obsidian 是通用 Markdown vault，不是 ScoutFlow authority，也不一定等同 RAW vault。用户可能已有自己的 templates、Properties、Dataview 查询、Sync、Publish、frontmatter lint 规则；ScoutFlow egress 不能污染这些模板。因此 Obsidian contract 采用“最小兼容 + 显式 namespace”的策略：只提供可复制的 `.md` 文件、稳定 YAML frontmatter、可读正文、manifest；不要求 Obsidian 安装插件，不创建全局模板，不写入 `.obsidian/` 配置，不改 CSS/snippets，不写 DataviewJS。

普通 live web 被禁用，本文不能声称已刷新 2026 年 Obsidian 官方 Properties 文档、Dataview 插件文档或 Publish/Sync 最新限制。采用的是长期稳定的 Markdown/YAML frontmatter 设计原则：单文件可读、frontmatter 键唯一、数组使用 YAML 合法格式、链接与标签兼容 Obsidian 的常见解析方式。

## 2. Obsidian 输出资产

| kind | 文件 | 说明 |
|---|---|---|
| `obsidian_note` | `.md` | 面向 Obsidian 的单条 reference note |
| `topic_card` | `.md` | 选题卡预览，可包含 wikilink hints |
| `source_index` | `.md` | 一次 handoff 的人读索引 |
| `handoff_manifest` | `manifest.json` | 机器读索引 |
| `redaction_report` | `.json` | 不进入用户可见正文，默认在 receipts |

不输出 `.canvas`、`.base`、`.json` 插件配置、`.obsidian/` 文件。Obsidian 用户若想改成 Canvas/Base，由用户或下游工具从 manifest 再加工。

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

## 3. Obsidian frontmatter schema

建议 Obsidian note 使用一个带 `scoutflow_` namespace 的 frontmatter，避免撞用户原有字段：

```yaml
---
title: "ScoutFlow — <platform_item_id>"
aliases:
  - "<short human title>"
tags:
  - scoutflow/handoff
  - source/bilibili
  - status/pending
created: "2026-05-07"
updated: "2026-05-07"
scoutflow_schema: "scoutflow.egress.v1"
scoutflow_asset_id: "sfa_<capture_id>_obsidian_note_r001"
scoutflow_handoff_id: "sfh_20260507_obsidian_01"
scoutflow_capture_id: "<capture_id>"
scoutflow_kind: "obsidian_note"
scoutflow_source_url: "https://www.bilibili.com/video/<BV...>/"
scoutflow_source_platform: "bilibili"
scoutflow_acceptance_state: "staged"
scoutflow_write_enabled: false
scoutflow_redaction_applied: true
scoutflow_supersede_status: "active"
scoutflow_superseded_by: null
---
```

设计解释：

1. `title`、`aliases`、`tags` 是 Obsidian 常见人机混合字段；但 ScoutFlow 不依赖 Obsidian 插件来解释它们。
2. 所有 ScoutFlow 专用字段都加 `scoutflow_`，避免覆盖用户的 `status`、`source`、`type`、`priority` 等模板字段。
3. `tags` 使用 YAML 列表，兼容 Obsidian tags/Properties 的常见做法；RAW 02-Raw 的简化 `tags: 调研/ScoutFlow采集` 不强行用于一般 Obsidian vault。
4. 日期字段用 `YYYY-MM-DD`；精确时间放 manifest 的 `created_at`。
5. `scoutflow_write_enabled: false` 是硬边界，不允许用 Obsidian contract 偷开 true write。

## 4. Wikilink / backlink / Dataview 兼容

正文允许给出 wikilink hints，但不要假设目标页存在：

```markdown
## Links

- Source platform: [[Bilibili]]
- Project: [[ScoutFlow]]
- Candidate topic: [[<topic seed>]]
- Related capture: `scoutflow_capture_id=<capture_id>`
```

Wikilink 原则：

1. 只把通用概念或用户可接受的新页作为 `[[...]]`。不要把完整 URL、cookie、token、长 capture_id 直接放进 wikilink。
2. 不在 frontmatter 中写 `[[wikilink]]`，避免 YAML parser、Dataview、Properties 解释不一致；wikilink 放正文。
3. Dataview 查询应依赖 `scoutflow_*` 字段，比如 `scoutflow_handoff_id`、`scoutflow_acceptance_state`、`scoutflow_kind`，不要解析正文。
4. Obsidian Publish 场景下，默认所有 note 仍是 `local_only`；若要 publish，需要人工把 `visibility` 从 `local_only` 改为 `public_safe`，并重新跑 redaction。
5. Obsidian Sync 只是同步机制，不是 acceptance proof；Sync 成功不代表 RAW 接收或 DiloFlow 执行。

## 5. 目录结构

ScoutFlow 只准备 staging：

```text
ScoutFlow/docs/research/post-frozen/egress-staging/obsidian/<YYYY-MM-DD>/<handoff_id>/
  manifest.json
  README-handoff.md
  notes/
    ScoutFlow-<capture_id>-<slug>.md
  receipts/
    redaction-report.json
    checksum-report.json
```

若用户要手动复制到 Obsidian vault，建议复制到一个局部文件夹：

```text
<ObsidianVault>/00-Inbox/ScoutFlow/<YYYY-MM-DD>/
```

但这只是建议，不是 ScoutFlow 自动写目标。不要写 `.obsidian/`，不要写模板文件夹，避免污染 vault。

## 3. manifest.json 通用规则

`manifest.json` 是每次 handoff 的目录级目录账本。它不嵌入大正文；正文、附件、摘要文件作为 assets 列表中的独立条目，并以 checksum、relative_path、kind、redaction、supersede 信息登记。manifest 的职责是让下游知道“这次包里有什么、从哪里来、什么时候生成、可不可以信任、是否替代旧资产”。它不负责调度下游，也不能把下游 acceptance 写成事实。

推荐目录：

```text
egress/<downstream>/<YYYY-MM-DD>/<handoff_id>/
  manifest.json
  assets/
    <asset_id>.md
    <asset_id>.json
  receipts/
    redaction-report.json
    checksum-report.json
  README-handoff.md
```

`manifest.json` 至少包含：`schema_version`, `handoff_id`, `target_downstream`, `created_at`, `created_by`, `write_enabled`, `source_baseline`, `assets`, `redaction_summary`, `supersede_summary`, `handoff_state`, `manual_steps_required`, `forbidden_fields_checked`, `audit_notes`。`write_enabled` 在 U8 版本必须固定为 `false`，表示 ScoutFlow 只准备和声明，不替用户执行对下游 vault / repo / agent inbox 的写入。

## 6. Obsidian note body

```markdown
# ScoutFlow — <platform_item_id>

> Candidate note. Prepared by ScoutFlow. Not RAW acceptance. Not final knowledge.

## Source Snapshot

- capture_id: `<capture_id>`
- platform_item_id: `<BV...>`
- canonical_url: <canonical URL>
- source_kind: `manual_url`
- capture_mode: `metadata_only`

## Evidence Summary

- trust_trace_locator: `<safe locator>`
- receipt_locator: `<safe locator>`
- metadata_summary: <redacted short text>

## Topic Card Lite

- topic_seed: <candidate seed>
- operator_angle: <candidate angle>
- confidence_hint: `low | medium | high`

## Links

- [[ScoutFlow]]
- [[Bilibili]]

## Boundary

- preview_only: `true`
- write_enabled: `false`
- downstream_acceptance_claimed: `false`
- blocked_lanes: media_download, ffmpeg, asr, browser_automation, audio_transcript
```

## 7. Obsidian manifest variant

```json
{
  "schema_version": "scoutflow.egress.v1",
  "target_downstream": "obsidian",
  "handoff_id": "sfh_20260507_obsidian_01",
  "write_enabled": false,
  "vault_write": "manual_user_copy_only",
  "assets": [
    {
      "asset_id": "sfa_01K..._obsidian_note_r001",
      "kind": "obsidian_note",
      "relative_path": "notes/ScoutFlow-01K...-bv....md",
      "frontmatter_namespace": "scoutflow_",
      "tags": ["scoutflow/handoff", "source/bilibili", "status/pending"],
      "wikilink_hints": ["ScoutFlow", "Bilibili"],
      "checksums": {"sha256": "<hash>", "size_bytes": 2048},
      "redaction": {"applied": true, "ruleset_version": "scoutflow-redaction-v1"},
      "supersede": {"status": "active", "supersedes": [], "superseded_by": null}
    }
  ]
}
```

## 8. Template 不污染规则

ScoutFlow 不创建、修改、删除用户 Obsidian templates。若用户的 vault 已经有 `type`, `status`, `domain`, `priority`, `source` 等字段，ScoutFlow note 仍保留 `scoutflow_*` 字段而不抢占原字段。用户可以在手动复制后用自己的模板合并；合并动作属于用户/Obsidian 侧，不属于 ScoutFlow egress contract。

## 9. Redaction 与 Publish 风险

Obsidian note 比 RAW staging 更容易被用户搜索、同步、发布。因此 Obsidian variant 默认更严格：`source_url` 要 canonical 化并去除追踪 query；作者信息只保留公开显示名或 platform_item_id，不保留私人 ID；正文不含 raw JSON；图片、二维码、截图路径默认 omit；任何 `public_safe` 可见性需要二次 redaction 证明。若 note 被用户发布到 Obsidian Publish，ScoutFlow manifest 不自动更新 acceptance；Publish 是用户动作。

## 10. 验收

- frontmatter key 不重复。
- 所有 ScoutFlow 专用字段以 `scoutflow_` 开头。
- `scoutflow_write_enabled=false`。
- tags 是 YAML 列表且不含空值。
- wikilink 不含 URL、token、email、phone、home path。
- manifest checksum 与 note 一致。
- note 明确 candidate / preview / no acceptance。

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
