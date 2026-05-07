---
title: EGRESS CONTRACT — ScoutFlow to RAW Vault
status: candidate / egress-contract / not-authority
authority: not-authority
claim_label: "95% based on Run-3+4 staging evidence and RAW 4-field candidate contract"
created_at: 2026-05-07
generated_in_environment: 2026-05-06
target_downstream: RAW vault
write_enabled: false
no_direct_raw_write: true
---

# EGRESS CONTRACT — ScoutFlow → RAW vault

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

## 2. RAW 的核心边界

RAW 是长期知识、入库、编译后段、脚本种子与交付资产的 SoR；ScoutFlow 是采集、证据、preview、proof 与 handoff candidate 的 SoR。U8 只能声明 ScoutFlow 如何把文件放到 repo-local staging，让用户或 RAW 侧手动决定是否进入 RAW。ScoutFlow 不写 `~/workspace/raw/00-Inbox/`，不修改 RAW `System/`，不生成 RAW acceptance verdict，不把 staging note 写成 compiled knowledge。

Run-3+4 已经证明两个 staging note 可以生成，但 C2 仍是 partial：用户未手动复制，RAW 未给 intake verdict，第二 inbox 风险未解除。因此 RAW egress contract 必须把初始状态写成 `pending_user_manual_transfer` 或 `staged`，不能写成 `accepted`。

## 3. RAW 允许接收的 ScoutFlow 输出

| 输出 | 是否允许进入 RAW staging | 原因 | 初始状态 |
|---|---:|---|---|
| `raw_note_candidate` | yes | 与四字段 frontmatter + 四段 body 一致 | `pending_user_manual_transfer` |
| `topic_card` / `topic_card_lite` | yes, 作为正文段 | 可作为选题预览，不是知识最终态 | `staged` |
| `signal` | conditional | 仅作为上下文，不触发 capture | `needs_review` |
| `script_seed_candidate` | conditional | 必须是一段候选文案，且回链 staged note | `candidate` |
| `receipt_summary` | yes, 摘要式 | 有助追溯，不包含 raw API response | `staged` |
| `raw_api_response` | no | 即使 redacted，也不应直接进入 RAW 知识流 | `blocked` |
| `media/audio/asr transcript` | no | 当前 runtime blocked | `blocked` |
| `signal-workbench-derived final conclusion` | no by default | Phase 2+ outline，不等于稳定知识 | `blocked_or_future` |

## 4. RAW frontmatter schema

RAW candidate note 继承 Run-3+4 的最小四字段：

```yaml
---
title: ScoutFlow <platform_item_id>
date: 2026-05-07
tags: 调研/ScoutFlow采集
status: pending
---
```

规则：

1. `title` 单行、非空、不可包含换行。建议 `ScoutFlow BV...` 或 `ScoutFlow <short-title>`。
2. `date` 使用 `YYYY-MM-DD`，来自 capture created_at 或 handoff created_at 的日期部分。
3. `tags` 使用 RAW 02-Raw 原始材料简化口径，默认 `调研/ScoutFlow采集`；不要把 Obsidian/compiled 内联数组强行引入 02-Raw candidate。
4. `status` 固定 `pending`。ScoutFlow 不得写 `compiled`, `active`, `accepted`。
5. 不重复字段。任何 importer 写入 RAW 前都应检查 YAML key 唯一性。
6. 不在 RAW candidate frontmatter 中加入 `cookie`, `token`, `author_private_id`, `browser_profile_path`, `signed_url`, `qrcode_path`。

## 5. RAW body schema

RAW body 固定四段，继承既有 staging 文件：

```markdown
## Source Snapshot

- capture_id: `<capture_id>`
- platform_item_id: `<BV...>`
- canonical_url: https://www.bilibili.com/video/<BV...>/

## Topic Card Lite

- export_posture: `handoff_candidate`
- target_path: `<preview target path, if any>`
- topic_seed: <redacted short seed>
- operator_angle: <why it may matter>

## Preview Boundary

- preview_only: `true`
- write_enabled: `false`
- evidence_source: existing capture truth only
- downstream_acceptance_claimed: `false`
- blocked_lanes: media_download, ffmpeg, asr, browser_automation, audio_transcript

## Transfer Note

This note was staged from ScoutFlow proof artifacts only. RAW intake is pending user manual transfer.
```

`target_path` 只能是 preview 目标或建议路径，不是实际写入证明。如果 target_path 指向 `/tmp/scoutflow-vault/00-Inbox/...`，它仍只是 preview path；如果指向 `~/workspace/raw/00-Inbox/...`，必须在正文旁边写明 `manual_transfer_required=true`，避免误读为已写。

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

## 6. RAW staging 目录

推荐路径：

```text
ScoutFlow/docs/research/post-frozen/raw-handoff-staging/<handoff_id>/
  manifest.json
  README-manual-transfer.md
  note-1-<capture_id>.md
  note-2-<capture_id>.md
  receipts/
    redaction-report.json
    checksum-report.json
```

兼容 Run-3+4 的历史路径时，也允许：

```text
ScoutFlow/docs/research/post-frozen/raw-handoff-staging/
  README-manual-transfer.md
  note-1-<capture_id>.md
  note-2-<capture_id>.md
```

但 U8 之后建议每次 handoff 使用独立 `<handoff_id>/` 子目录，防止多个批次混在一起造成第二 inbox 风险。README 必须包含：目标 RAW 路径、用户手动复制步骤、当前 notes 列表、boundary、C2 verdict/pending 状态、不要把 staging 当 acceptance。

## 7. RAW manifest variant

```json
{
  "schema_version": "scoutflow.egress.v1",
  "target_downstream": "raw_vault",
  "handoff_id": "sfh_20260507_raw_01",
  "created_at": "2026-05-07T00:00:00Z",
  "write_enabled": false,
  "handoff_state": "pending_user_manual_transfer",
  "manual_steps_required": [
    "User reviews README-manual-transfer.md",
    "User copies note-*.md into ~/workspace/raw/00-Inbox/",
    "RAW performs intake and records accepted / needs-edit / rejected"
  ],
  "assets": [
    {
      "asset_id": "sfa_01K..._raw_note_candidate_r001",
      "kind": "raw_note_candidate",
      "relative_path": "note-1-01K....md",
      "target_hint": "~/workspace/raw/00-Inbox/",
      "acceptance_state": "pending_user_manual_transfer",
      "frontmatter": {"title": "ScoutFlow BV...", "status": "pending"},
      "checksums": {"sha256": "<hash>", "size_bytes": 892},
      "redaction": {"applied": true, "masked_fields": []},
      "supersede": {"status": "active", "supersedes": [], "superseded_by": null}
    }
  ]
}
```

## 8. RAW acceptance readback

RAW acceptance 只能来自 RAW 侧实际 intake 或用户手动 readback，不能由 ScoutFlow 预先写入。建议 RAW 侧回读文件命名：

```text
ScoutFlow/docs/research/post-frozen/raw-intake-readback/<handoff_id>/
  RAW-INTAKE-READBACK-<YYYY-MM-DD>.md
```

回读字段：`handoff_id`, `asset_id`, `raw_path`, `verdict`, `cleanup_reason`, `consumed_at`, `reviewer_role`, `notes`。其中 `verdict` 枚举为：`accepted`, `needs-edit`, `rejected`, `pending_user_manual_transfer`。如果只是复制到了 00-Inbox，但没有分类、编译或脚本种子回链，仍不能写 `accepted`，最多 `copied_no_intake_yet` 或保持 `pending`。

## 9. Supersede 在 RAW 中的特殊处理

RAW 既有 note 不应被 ScoutFlow 覆盖。若新版本替代旧版本：

1. 新 staging note frontmatter 仍四字段，不新增复杂 supersede 字段，避免污染 RAW 02-Raw template。
2. 在正文 `## Preview Boundary` 增加：`supersedes: <old_asset_id>` 与 `supersede_reason: corrected_metadata | redaction_update | duplicate_merge | better_topic_angle`。
3. 在 manifest 的 `supersede_summary` 写完整映射。
4. 用户手动进入 RAW 后，RAW 自己决定是否删除旧 note、合并旧 note、或保留为 archive。
5. ScoutFlow 不对 RAW 内旧文件执行 prune。

## 10. 禁止字段

RAW note candidate 不得包含：真实 cookie/token、authorization header、auth sidecar 路径、QR 图片路径、浏览器 profile path、`BBDown.data`/`BBDownTV.data`、raw command stream、未脱敏 phone/email/id、平台作者私人字段、评论区个人信息、signed URL query、机器用户名 home path、`runtime_approved=true`、`vault_committed=true`、`knowledge_final=true`、`raw_acceptance=accepted`（除非 RAW readback 证明）。

## 11. 最小验收

- staging 目录存在，且不在 `~/workspace/raw/`。
- 所有 note frontmatter 为四字段，status pending。
- 所有 note body 四段齐全。
- manifest `write_enabled=false`。
- checksum 对 redacted payload 计算。
- README 明确用户手动复制。
- C2 partial/pending 状态没有被改成 pass。

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
## 12. RAW staging 文件名与冲突处理补充

RAW staging 文件名建议稳定、短、可人工判断：`note-<ordinal>-<capture_id>.md` 或 `scoutflow-<capture_id>-<platform_item_id>.md`。`ordinal` 只是本次 handoff 内排序，不是长期 ID；长期 ID 必须是 manifest 的 `asset_id`。如果同一 handoff 中出现两个相同 `capture_id`，生成器应停止，因为这通常代表重复采集或重复渲染。如果历史 staging 中已经存在同名文件，不能覆盖，应生成新的 handoff_id 子目录，或者生成 r002 asset 并写 supersede。RAW 侧用户如果已经复制旧 note，新版本 README 必须写明“旧文件可能已在 RAW 00-Inbox，需要人工判断是否移除”。

冲突处理顺序：先看 `asset_id`，再看 checksum，再看 `capture_id/platform_item_id`，最后才看文件名。文件名冲突不是证据冲突；checksum 不一致才说明内容不同；同一 capture 的不同 topic angle 应用不同 kind 或 revision 表达。这个规则可以防止用户在 RAW inbox 看到两个相似 note 时误删真正需要保留的版本。

## 13. RAW 与 script seed 的连接补充

`script_seed_candidate` 只能在 RAW handoff 包内作为候选段落或单独 asset 出现，不能写成 RAW 已经产出脚本。脚本种子最低要求是一段连贯文字、明确主体、回链 staged note / capture、语气保持 candidate。若 RAW 尚未 acceptance，script seed 的 frontmatter 或正文必须写 `raw_acceptance_claimed=false`。如果后续 RAW 真的把 note 编译成脚本种子，应由 RAW readback 提供 `raw_path`, `seed_path`, `verdict`, `created_at`，ScoutFlow 再在 readback lane 中记录，而不是在首次 egress 中预设。
