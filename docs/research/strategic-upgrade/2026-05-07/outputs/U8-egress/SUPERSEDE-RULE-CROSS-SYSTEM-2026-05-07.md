---
title: SUPERSEDE RULE — Cross-System ScoutFlow Egress
status: candidate / supersede-rule / not-authority
authority: not-authority
claim_label: "95%"
created_at: 2026-05-07
generated_in_environment: 2026-05-06
write_enabled: false
---

# SUPERSEDE RULE — Cross-System ScoutFlow Egress

## 0. 证据与边界口径

本交付只声明 ScoutFlow 单方面写出的文件级 egress contract，不定义 SDK、OpenAPI client、双向同步 broker，也不修改任何下游。PRD v2 的最高边界是：ScoutFlow 是单 user、local-first 的采集与证据工作台；RAW、Obsidian、DiloFlow 是下游消费者，不是 ScoutFlow 项目的一部分。SRD v2 的最高边界是：当前生效的是 metadata-only、receipt、trust trace、redaction/secret scan baseline；Phase 2+ 对象仍主要是 outline，不能被文件导出契约误读成 runtime unlock。

本环境已经读取上传的 post176 audit pack 与 GitHub 上的 PRD/SRD、Run-3+4 C2 文件。普通 live web 浏览在当前会话被禁用，所以本文所有外部 vendor/frontmatter 口径只作为“需刷新验证的公共模式候选”，不标记为 live verified。`~/workspace/DiloFlow/`、`~/workspace/raw/`、`~/workspace/hermes-agent/` 与 Obsidian 本地 vault 在当前容器没有出现；因此 DiloFlow 与 hermes-agent 的 receiver-side parser 只能给出单方、保守、低耦合的文件契约，不能声称已经被下游 repo 实测接受。

硬边界在所有下游一致：`write_enabled=false` 保持；ScoutFlow 永不直写 `~/workspace/raw/`；凭据、cookie、token、QR 图片、browser profile path、auth sidecar、raw stdout/stderr 中可能含秘密的片段不得进入 egress；Bilibili/XHS 等平台原作者隐私字段只允许最小必要、脱敏后的事实摘要；manifest 是一次 handoff 的索引，不是下游 acceptance 证明；supersede 只能标记资产生命周期，不允许反向覆盖下游知识库事实。

## 1. 为什么需要 supersede

ScoutFlow 可能重新生成同一 capture 的更好 topic card、修正 metadata、更新 redaction、合并重复资产、或把旧版 handoff 从 `needs_edit` 改成新的候选版本。如果没有 supersede 规则，下游会看到多个文件，却不知道哪一个仍有效；更糟的是，旧版本如果包含 redaction 缺陷，下游可能继续引用。U8 supersede 只做“软生命周期标记”，不执行下游删除，不覆盖 RAW/Obsidian/DiloFlow/hermes 的本地事实。

## 2. 状态枚举

| status | 含义 | 是否可被新下游默认采用 |
|---|---|---:|
| `active` | 当前推荐版本 | yes |
| `deprecated` | 不推荐，但未明确替代 | no by default |
| `superseded` | 已被具体资产替代 | no |
| `retracted` | 因 redaction/法律/事实错误撤回 | no，且需人工处理 |
| `archived` | 历史保留 | no by default |
| `duplicate` | 与另一资产重复 | no，指向 canonical |

frontmatter 简化字段：

```yaml
supersede_status: active
supersedes: []
superseded_by: null
supersede_reason: null
```

manifest 完整对象：

```json
{
  "supersede": {
    "status": "active",
    "revision": 1,
    "supersedes": [],
    "superseded_by": null,
    "canonical_asset_id": "sfa_..._r001",
    "reason": null,
    "effective_at": "2026-05-07T00:00:00Z",
    "human_note": ""
  }
}
```

## 3. asset_id 与 revision

`asset_id` 不应复用同一字符串表示不同内容。推荐：

```text
sfa_<capture_id>_<kind>_r001
sfa_<capture_id>_<kind>_r002
```

同一 `asset_id` 的 checksum 如果变化，应视为错误；正确做法是生成 r002，并在 manifest 写：r001 `superseded_by=[r002]`，r002 `supersedes=[r001]`。如果只是 manifest 新增 readback 状态，不改变 asset 文件，可生成新的 handoff manifest，但不改 asset checksum。

## 4. supersede 原因枚举

| reason | 场景 | 下游动作建议 |
|---|---|---|
| `metadata_correction` | title/date/platform_item_id 修正 | 新版本替代旧版本，旧版本保留 archive |
| `redaction_update` | 旧版本有敏感字段风险 | 旧版本标 retracted，人工检查下游是否撤下 |
| `duplicate_merge` | 两个 capture 或 note 重复 | 指向 canonical asset |
| `better_topic_angle` | 新 topic seed 更准确 | 旧版本 deprecated，不紧急撤回 |
| `schema_upgrade` | schema v1 → v2 | 旧版可读但不推荐 |
| `receiver_feedback` | 下游 needs-edit 后修订 | 新版 active，旧版 superseded |
| `manual_retract` | 用户要求撤回 | retracted |

## 5. 下游 prune 触发

ScoutFlow 只发出 prune 建议，不自动 prune。触发条件：

1. `retracted` + `redaction_update`：下游应尽快人工撤下或隔离旧文件。
2. `superseded` + 同一 target folder：下游可把旧版本移入 archive。
3. `duplicate`：下游可保留 canonical，删除/归档 duplicate。
4. `deprecated` 超过本地保留期：下游按自己的知识库策略处理。
5. RAW acceptance 已经把旧版本编译进知识：不要自动删除，需要 RAW 侧合并/修订。

## 6. RAW 特殊规则

RAW 02-Raw note frontmatter 保持四字段，不强加 supersede 字段。supersede 写在 manifest 和正文 `## Preview Boundary` 中。若旧 note 已由用户复制进入 `~/workspace/raw/00-Inbox/`，ScoutFlow 只能在新的 staging README 中提示：旧版 `<asset_id>` 已被 `<asset_id_r002>` 替代；用户/RAW 决定是否删除旧 note。若旧 note 已 compiled 成 01-Wiki，ScoutFlow 不直接改 Wiki，最多生成 readback request。

## 7. Obsidian 特殊规则

Obsidian 可以接受 `scoutflow_supersede_status`、`scoutflow_superseded_by` 字段，因为 namespace 避免撞模板。下游用户可以用 Dataview 查 `scoutflow_supersede_status != "active"`。但 ScoutFlow 不改 `.obsidian` 查询和模板。

## 8. DiloFlow 特殊规则

DiloFlow task 如果基于旧 asset 创建，应保留其原任务历史。新 supersede 包只能建议：`old_task_should_reference_new_asset=true`。不要删除旧 DiloFlow 任务，避免破坏流程审计。

## 9. hermes-agent 特殊规则

如果 hermes 正在审计旧版本，新的 supersede 包应在 manifest 写 `audit_target_superseded=true`。hermes 输出应标记“审计基于旧版本”，而不是试图合并上下文。若 supersede 原因是 `redaction_update`，hermes 不应继续读取旧 asset。

## 10. manifest supersede_summary

```json
{
  "supersede_summary": {
    "has_supersede_events": true,
    "events": [
      {
        "old_asset_id": "sfa_01K..._raw_note_candidate_r001",
        "new_asset_id": "sfa_01K..._raw_note_candidate_r002",
        "reason": "redaction_update",
        "old_status": "retracted",
        "new_status": "active",
        "downstream_prune_recommended": true,
        "automatic_prune_performed": false
      }
    ]
  }
}
```

## 11. 验证规则

- `superseded_by` 指向的 asset 必须在同一 manifest 或可解析历史 manifest 中出现。
- `supersedes` 不得形成循环。
- `retracted` 必须有 reason。
- `redaction_update` 必须触发人工审计提示。
- `active` asset 不应同时被别的 active asset supersede，除非它是不同 downstream variant。
- RAW variant 不在四字段 frontmatter 加复杂 supersede。
- 所有 supersede 事件都要出现在 README-handoff 的人读摘要。

## 12. 迁移到未来 schema

若未来 `scoutflow.egress.v2` 引入更强 lifecycle，旧 v1 仍保留可读。v2 不应要求下游重写旧文件；只需通过 manifest 明确 v1 asset 的状态。跨版本 supersede 示例：`sfa_<capture_id>_topic_card_v1_r003` 被 `sfa_<capture_id>_topic_card_v2_r001` 替代；reason=`schema_upgrade`。

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
## 13. Supersede graph 示例

假设 r001 是最初 RAW note candidate，r002 只是改进 topic angle，r003 是 redaction_update。正确图谱：r001 → r002 → r003，且 r003 active，r001/r002 superseded。若 r003 是 redaction_update，r001/r002 至少 deprecated，必要时 retracted。manifest 不能只写“latest=r003”，因为下游需要知道为什么旧版不再推荐。更不能把 r001 文件删除后只留下 r003；删除会破坏 audit trail，也让 RAW/Obsidian/DiloFlow 已引用的旧 asset 失去解释。

## 14. Cross-downstream 不同版本的关系

同一 capture 可以同时有 RAW、Obsidian、DiloFlow、hermes 四种 variant。RAW r002 不必自动 supersede Obsidian r001，因为它们是不同下游、不同 frontmatter、不同正文风险。只有当修订原因影响共同事实，比如 `metadata_correction` 或 `redaction_update`，才建议同时生成四个新 variant。manifest 的 `affected_downstreams` 可写：`["raw_vault", "obsidian"]`，避免 DiloFlow/hermes 被不必要的版本噪声污染。

## 15. Human-readable supersede notice

README-handoff 必须用人话写 supersede，不只写 JSON：

```text
This package supersedes one prior RAW candidate:
- old: sfa_01K..._raw_note_candidate_r001
- new: sfa_01K..._raw_note_candidate_r002
- reason: redaction_update
- action: do not copy old note; if already copied to RAW, manually review and remove/archive it.
```

下游很多时候是人工消费，JSON schema 只能防 parser 错，不能防用户误会。README 是必需资产。
