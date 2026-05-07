---
title: EGRESS CONTRACT — ScoutFlow to DiloFlow
status: candidate / egress-contract / not-authority
authority: not-authority
claim_label: "95% for ScoutFlow-side contract; receiver parser not locally verified"
created_at: 2026-05-07
generated_in_environment: 2026-05-06
target_downstream: DiloFlow
write_enabled: false
local_receiver_repo_observed: false
---

# EGRESS CONTRACT — ScoutFlow → DiloFlow

## 0. 证据与边界口径

本交付只声明 ScoutFlow 单方面写出的文件级 egress contract，不定义 SDK、OpenAPI client、双向同步 broker，也不修改任何下游。PRD v2 的最高边界是：ScoutFlow 是单 user、local-first 的采集与证据工作台；RAW、Obsidian、DiloFlow 是下游消费者，不是 ScoutFlow 项目的一部分。SRD v2 的最高边界是：当前生效的是 metadata-only、receipt、trust trace、redaction/secret scan baseline；Phase 2+ 对象仍主要是 outline，不能被文件导出契约误读成 runtime unlock。

本环境已经读取上传的 post176 audit pack 与 GitHub 上的 PRD/SRD、Run-3+4 C2 文件。普通 live web 浏览在当前会话被禁用，所以本文所有外部 vendor/frontmatter 口径只作为“需刷新验证的公共模式候选”，不标记为 live verified。`~/workspace/DiloFlow/`、`~/workspace/raw/`、`~/workspace/hermes-agent/` 与 Obsidian 本地 vault 在当前容器没有出现；因此 DiloFlow 与 hermes-agent 的 receiver-side parser 只能给出单方、保守、低耦合的文件契约，不能声称已经被下游 repo 实测接受。

硬边界在所有下游一致：`write_enabled=false` 保持；ScoutFlow 永不直写 `~/workspace/raw/`；凭据、cookie、token、QR 图片、browser profile path、auth sidecar、raw stdout/stderr 中可能含秘密的片段不得进入 egress；Bilibili/XHS 等平台原作者隐私字段只允许最小必要、脱敏后的事实摘要；manifest 是一次 handoff 的索引，不是下游 acceptance 证明；supersede 只能标记资产生命周期，不允许反向覆盖下游知识库事实。

## 1. 主要输入证据摘录

| Evidence | 用途 | 本交付如何使用 |
|---|---|---|
| PRD v2 §0.1 / §2 / §8 | 定义 ScoutFlow 身份、下游关系、凭据红线 | 所有 contract 都把下游视为消费者而非 ScoutFlow 子模块 |
| SRD v2 §1 / §2 / §5 / §6 | 定义 metadata-only 当前有效范围、redaction、manual auth gate、blocked runtime | egress 不暗示 media / ASR / browser automation / true write 解锁 |
| Run-3+4 C2 report | PF-C2-06/07/08/09/11 为 partial，RAW handoff staging 仍待人工转移 | RAW contract 强制 staging + manual transfer + pending verdict |
| RAW Note Candidate Contract v0 | 四字段 frontmatter + 四段 body | RAW variant 直接继承最小 note shape |
| Manual RAW Handoff Runbook | ScoutFlow stops at repo-local staging；用户手动 copy 到 RAW 00-Inbox | 禁止 ScoutFlow 自动写入 RAW vault |
| RAW Intake Acceptance Rubric | accepted / needs-edit / rejected / pending_user_manual_transfer | manifest 记录 handoff_state，不记录 acceptance 除非 RAW 侧回读 |
| Bridge/Vault code refs | 只允许 manual_url + metadata_only，target 在 00-Inbox，status pending | Obsidian/RAW 的路径与 frontmatter 规则采用相同安全姿态 |

## 2. 目标与非目标

DiloFlow 在本契约中被定义为“后续行动/流程编排/捕获线索消费方”，而不是 ScoutFlow 的 authority writer。ScoutFlow 可以把一个 capture、一个 topic_card、一个 signal 或一个 receipt_summary 写成 DiloFlow 可读的文件包，但不能要求 DiloFlow 反向改 ScoutFlow DB，也不能让 DiloFlow 的 parser 成为 ScoutFlow schema 的隐藏事实源。由于当前容器没有 `~/workspace/DiloFlow/`，本文不声称已经读取 DiloFlow 的真实 capture parser；合同采用 receiver-neutral 设计：字段名稳定、frontmatter 明确、manifest 可校验、正文分段固定，下游即便只做简单 Markdown/YAML parser 也能消费。

非目标包括：不提供 DiloFlow SDK；不定义 HTTP API；不让 ScoutFlow 自动调用 DiloFlow；不把 DiloFlow workflow 状态写入 ScoutFlow authority；不做跨系统双向 event bus；不把下游 task completion 伪装成 ScoutFlow receipt。

## 3. DiloFlow 资产类型

| kind | 用途 | 输入来源 | 下游可见性 | 备注 |
|---|---|---|---|---|
| `diloflow_capture` | 把单条 metadata-only capture 变成行动候选 | `capture_id`, `canonical_url`, metadata summary | 可见正文 + 隐性 manifest metadata | 最保守的默认 kind |
| `topic_card` | 把 topic_card-lite 预览交给流程评审 | preview artifact | 可见正文 | 不代表 RAW/Obsidian 已收录 |
| `signal` | 把选题信号转成待评估动作 | signal candidate IR | 可见正文 | 仍受 LP-001，不能直接 auto-capture |
| `receipt_summary` | 让 DiloFlow 知道证据账本概况 | receipt ledger / trust trace summary | 只读 | 不包含 raw API response |
| `handoff_manifest` | 一次交接的索引 | asset list + checksum | machine-readable | 必须和 assets 同目录 |

DiloFlow contract 的核心是“channel-related capture 输入”：资产可以带 `channel`, `source_platform`, `operator_angle`, `next_action`, `priority_hint`，但这些字段都只是流程提示，不批准扩大采集范围。`recommendation / keyword / RAW gap` 仍不得直接创建 capture；如果 DiloFlow 看到这些字段，只能创建 review task 或 scope_builder task，而不是触发 ScoutFlow runtime。

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

## 4. DiloFlow frontmatter schema

```yaml
---
schema_version: scoutflow.egress.v1
asset_id: sfa_<capture_id>_diloflow_capture_r001
kind: diloflow_capture
title: "ScoutFlow capture candidate — <platform_item_id>"
source_platform: bilibili
source_kind: manual_url
capture_mode: metadata_only
capture_id: "<capture_id>"
source_url: "<canonical_url>"
created_at: "2026-05-07T00:00:00Z"
scoutflow_version: "PRD-v2/SRD-v2 baseline"
channel: "research/intake"
operator_angle: "why this item matters, redacted"
next_action: follow     # follow | park | reject | need_more_evidence
acceptance_state: staged
visibility: local_only
write_enabled: false
redaction_applied: true
redaction_ruleset: scoutflow-redaction-v1
supersede_status: active
supersedes: []
superseded_by: null
---
```

字段设计原则：

1. `channel` 是 DiloFlow 的分流提示，不是 ScoutFlow runtime gate。建议值：`research/intake`, `audit/followup`, `raw/manual-transfer`, `hermes/candidate-review`, `obsidian/reference-note`。
2. `operator_angle` 只写任务角度，不写私人身份、登录信息、浏览器路径、内部凭据路径。
3. `next_action` 必须是显式枚举。`follow` 表示值得继续人工看；`park` 表示暂存；`reject` 表示不要继续；`need_more_evidence` 表示证据不足。没有 `auto_capture` 选项。
4. `acceptance_state` 初始只能是 `prepared` 或 `staged`。DiloFlow 后续若消费，可以写自己的状态文件，但 ScoutFlow manifest 不回填，除非用户另开 readback lane。

## 5. 目录结构

建议 DiloFlow handoff 只写在 ScoutFlow egress staging 内：

```text
ScoutFlow/
  docs/research/post-frozen/egress-staging/diloflow/<YYYY-MM-DD>/<handoff_id>/
    manifest.json
    README-handoff.md
    assets/
      sfa_<capture_id>_diloflow_capture_r001.md
      sfa_<capture_id>_topic_card_r001.md
    receipts/
      redaction-report.json
      checksum-report.json
```

不建议按 DiloFlow 本地真实目录写入，原因是当前 U8 合同不是下游修改授权。下游可以手动复制、拉取、或实现自己的 importer，但 importer 必须把 ScoutFlow asset 当 candidate。

## 6. Markdown body contract

DiloFlow Markdown 正文采用固定分段，避免 parser 猜：

```markdown
# <title>

## Source Snapshot
- capture_id: `<capture_id>`
- source_platform: `bilibili`
- source_kind: `manual_url`
- capture_mode: `metadata_only`
- canonical_url: <redacted or canonical URL>

## Evidence Summary
- trust_trace_locator: `<safe locator>`
- receipt_locator: `<safe locator>`
- metadata_summary: <short redacted text>
- blocked_lanes: media_download, ffmpeg, asr, browser_automation, audio_transcript

## DiloFlow Routing
- channel: `research/intake`
- operator_angle: <why this matters>
- next_action: `need_more_evidence`
- priority_hint: `P2`

## Boundary
- preview_only: `true`
- write_enabled: `false`
- downstream_acceptance_claimed: `false`
```

Parser 约束：frontmatter 是 machine-readable；正文是 human-readable。DiloFlow 不应从正文反推出未在 frontmatter/manifest 中声明的状态。若 DiloFlow 只支持一页 capture 输入，建议读取 frontmatter 的 `capture_id`, `source_url`, `channel`, `next_action`，再展示正文的 Evidence Summary。

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

## 7. DiloFlow manifest variant

```json
{
  "schema_version": "scoutflow.egress.v1",
  "handoff_id": "sfh_20260507_01",
  "target_downstream": "diloflow",
  "write_enabled": false,
  "handoff_state": "staged",
  "manual_steps_required": ["DiloFlow importer/user reads staged package"],
  "assets": [
    {
      "asset_id": "sfa_01K..._diloflow_capture_r001",
      "kind": "diloflow_capture",
      "relative_path": "assets/sfa_01K..._diloflow_capture_r001.md",
      "channel": "research/intake",
      "next_action": "need_more_evidence",
      "source": {"capture_id": "01K...", "source_url": "https://www.bilibili.com/video/BV.../"},
      "checksums": {"sha256": "<sha256-of-redacted-file>", "size_bytes": 1234},
      "redaction": {"applied": true, "ruleset_version": "scoutflow-redaction-v1"},
      "supersede": {"status": "active", "supersedes": [], "superseded_by": null}
    }
  ]
}
```

## 8. DiloFlow 可见/不可见 metadata

可见 metadata：title、platform_item_id、canonical_url、capture_id、created_at、capture_mode、source_kind、safe trust trace locator、人工写入的 operator_angle。不可见 metadata：cookie、token、auth sidecar、QR 图片、本地 profile path、raw stdout/stderr、签名 URL、平台私信/隐私字段、未脱敏作者敏感信息、DiloFlow 本地路径。manifest 可以保留 `origin.dispatch`、`origin.run_id` 这类 audit locator，但不要记录个人真实姓名、机器用户名或 home path。

## 9. 失败与回滚

DiloFlow importer 如果发现 `schema_version` 不认识，应停止并把整个 handoff 标为 `unsupported_schema`，而不是静默解析。若 checksum 不匹配，应停止。若 `redaction.applied=false`，应拒收。若 `write_enabled=true` 出现在 U8 包，应视为合同漂移。若发现同一 `asset_id` 已存在但 checksum 不同，不能覆盖旧文件；应写 readback note，让 ScoutFlow 生成 r002 或 supersede manifest。

## 10. 推荐验收

1. 读取 manifest JSON 成功。
2. 验证所有 asset relative_path 都在 handoff 目录内。
3. 验证 asset frontmatter 与 manifest 一致。
4. 验证 redaction report 存在且 `applied=true`。
5. 验证 `next_action` 枚举合法。
6. 验证没有 `auto_capture`、`runtime_approved`、`vault_committed=true` 等越界字段。
7. 验证 supersede 状态可解释。

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
