# Obsidian Frontmatter Compatibility Scan

> task: `PR #65 / T-P1A-040`
> status: research-only / not-authority / not-runtime-approval
> scope: read-only scan of `~/workspace/raw/System/**`; no vault writes, no repo-runtime changes

本报告只回答一个问题：ScoutFlow 后续如果要把 capture 结果写入用户现有的 RAW / Obsidian vault，最小 frontmatter 契约到底是什么，哪些检查必须过，哪些检查现在还只是 future acceptance gate。

## §1 用户 vault 现状（只读扫描）

本次扫描仅使用以下只读素材：

- `~/workspace/raw/System/frontmatter-templates.md`
- `~/workspace/raw/System/intake-rules.md`
- `~/workspace/raw/System/audit-wiki.py`
- `~/workspace/raw/System/_SPEC_INDEX.md`
- `~/workspace/raw/System/domain-map.md`

从这些文件可以确认 5 个稳定事实：

1. 用户的 RAW vault 已经有稳定的顶层结构，至少包括 `00-Inbox`、`01-Wiki`、`02-Raw`、`03-Output`、`04-Atlas`、`05-Projects`、`System`。
2. `System/frontmatter-templates.md` 是字段定义唯一真相源，`_SPEC_INDEX.md` 也再次声明了这一优先级。
3. `ScoutFlow` 不应该重造 domain 枚举，也不应该改写 `System/` 里的规范文件。
4. `02-Raw` 原始材料模板只有 4 个字段：`title`、`date`、`tags`、`status`。
5. `audit-wiki.py` 当前主流程只遍历 `01-Wiki/**/*.md`，不是对 `00-Inbox` 或 `02-Raw` 全库直接跑。

这意味着 ScoutFlow 后续的 VaultWriter 不是“给 wiki 造一篇完整文章”，而是“向现有 intake 流程提交一份原始材料候选”。两者的契约不能混写。

## §2 raw 4 字段精确映射

基于 `frontmatter-templates.md` 的 `02-Raw 原始材料模板`，ScoutFlow 输出到用户 vault 时应锁定为以下 4 字段：

| ScoutFlow 输出语义 | frontmatter 字段 | 类型 / 约束 | 示例 |
|---|---|---|---|
| 人类可读标题 | `title` | string | `Bilibili - 某 UP 主 - 某视频标题` |
| 导出日期 | `date` | `YYYY-MM-DD` | `2026-05-05` |
| ScoutFlow 分类标签 | `tags` | string，单值，不是 YAML list | `调研/ScoutFlow采集` |
| 下游待处理状态 | `status` | literal | `pending` |

锁定后的最小 frontmatter 模板如下：

```yaml
---
title: "<human-readable title>"
date: 2026-05-05
tags: 调研/ScoutFlow采集
status: pending
---
```

结论：

- `tags: 调研/ScoutFlow采集` 是当前最稳妥默认值，来自既有 RAW 规则与现有 ScoutFlow 候选文档，不需要改 `domain-map.md`。
- `status: pending` 是原始材料状态，不是 wiki 成文状态。
- 这里故意不加入 `type`、`domain`、`last_validated`、`priority`、`source`，因为这些属于 `01-Wiki` 或更高层工作流字段，不属于 00-Inbox 原始导出最小契约。

## §3 `audit-wiki.py` 与 ScoutFlow 相关的检查边界

`audit-wiki.py` 当前脚本的主入口会：

- 以 `System/` 所在目录的上一级作为 vault root。
- 只扫描 `01-Wiki/**/*.md`。
- 不直接遍历 `00-Inbox`。
- 不直接把 `02-Raw` 当作 article 集合审计。

因此必须明确两层边界：

### 3.1 当前脚本直接覆盖的范围

这些检查是 `audit-wiki.py` 已经实现、并且会影响未来“原始材料进入 wiki 后”的稳定性：

- frontmatter 解析是否成功
- 字段名是否重复
- 日期格式是否为 `YYYY-MM-DD`
- tags 是否为合法形式
- domain / priority / source 等字段是否符合 wiki 规则

### 3.2 当前脚本不直接覆盖的范围

这些不是 `audit-wiki.py` 现在就能对 `00-Inbox` 逐文件判定通过/失败的：

- `00-Inbox/scoutflow-*.md` 是否应允许 `status: pending`
- `00-Inbox` 单值 `tags` 是否在 article-level `A7` 规则下被接受
- `00-Inbox` 是否应强制 `type/domain/last_validated/priority`

因此，Wave 4 正确做法不是“把 00-Inbox 文件硬塞进现有 wiki 审计器”，而是：

1. 先锁定 ScoutFlow 的原始导出 frontmatter 契约。
2. 在 preview/commit 路线里加最小 frontmatter 校验。
3. 把 `audit-wiki.py` 作为 downstream compatibility reference，而不是当前 raw export 的唯一执行器。

## §4 与 ScoutFlow 最相关的 `audit-wiki.py` 检查项

虽然 `audit-wiki.py` 现在不直接审 `00-Inbox`，但以下检查逻辑对 ScoutFlow 未来导出仍然是硬约束参考：

| 检查点 | 当前脚本位置 | 与 ScoutFlow 的关系 | 结论 |
|---|---|---|---|
| frontmatter 可解析 | `parse_frontmatter()` | 未来 raw export 也必须先过 YAML 基本解析 | 必须遵守 |
| 重复字段禁令 | `frontmatter-templates.md` + parser 假设 | 不能出现两个同名字段，例如两个 `status` | 必须遵守 |
| `date` 格式检查 | `A6/A8` 风格 | 即便 raw export 不跑 A6，也应统一 `YYYY-MM-DD` | 必须遵守 |
| `tags` 语法检查 | `A7` | wiki 要求 inline array；raw 4 字段模板要求单值 string | 需要分层处理 |
| `status` 枚举检查 | `A5` | wiki 当前只接受 `active/draft/archived/stale`；raw 模板使用 `pending` | 需要分层处理 |
| `source` 路径检查 | `B1/B2` | 仅 `compiled` wiki 文章需要；raw export 不需要 | 不应提前引入 |

这里有两个关键兼容性结论：

1. `tags` 在 raw export 与 wiki article 是两套契约。
   `00-Inbox` 先用 `tags: 调研/ScoutFlow采集`，后续若进入 `01-Wiki`，再按 wiki 规则转成 inline array。
2. `status: pending` 在 raw export 合法，但在当前 `audit-wiki.py` article-level `A5` 下不合法。
   这不代表 raw export 错了，只代表不能把 wiki article 枚举直接拿来判断原始 intake 材料。

## §5 domain 与 tags 决策

本次扫描不修改 `domain-map.md`，只给出 ScoutFlow 的保守落地策略。

### 5.1 domain 决策

- 不新增“内容采集”之类的新 domain。
- ScoutFlow 不直接往 `01-Wiki` 写 article，所以不需要在导出时就写 `domain`。
- 如果后续通过 `/intake` 进入 `02-Raw/调研/`，则由现有 intake 规则和人工二次处理决定更细的归类。

### 5.2 tags 决策

默认标签锁为：

```yaml
tags: 调研/ScoutFlow采集
```

允许的细分扩展只应发生在后续阶段，而不是本 PR 就扩 frontmatter 字段，例如：

- `调研/Bilibili`
- `调研/Xiaohongshu`
- `调研/YouTube`

但 ScoutFlow 初始导出模板仍保持单值默认，避免在第一个 commit 点就引入标签策略分叉。

### 5.3 路径决策

ScoutFlow 后续如果获批写 vault，允许路径应收敛为：

```text
${SCOUTFLOW_VAULT_ROOT}/00-Inbox/scoutflow-{capture_id}-{slug}.md
```

明确禁止：

- `01-Wiki/**`
- `02-Raw/**`
- `03-Output/**`
- `04-Atlas/**`
- `05-Projects/**`
- `System/**`
- `.obsidian/**`

这样才能把 ScoutFlow 保持在“原始材料提交者”的角色，而不是越权改用户知识库结构。

## §6 ScoutFlow 写入 markdown 模板（锁定候选）

本节给 Wave 4 VaultWriter SPEC / implementation 作为候选模板输入，不等于本 PR 已批准 runtime。

```yaml
---
title: "<human-readable title>"
date: 2026-05-05
tags: 调研/ScoutFlow采集
status: pending
---

## ScoutFlow Capture
- capture_id: <capture id>
- platform: bilibili
- platform_item_id: <platform native id>
- canonical_url: https://...
- capture_scope: metadata_only
- metadata_fetched_at: 2026-05-05T10:00:00+08:00

## Metadata
- author: <author name>
- publish_time: <platform publish time if known>
- title_snapshot: <title at capture time>
- description_snapshot: <optional>

## Trust Trace
- receipt_sha256: <sha256>
- trust_trace_url: <future local URL or not_generated>
- source_artifacts:
  - <future evidence path or id>
- media_audio: not_approved

## Notes
- reserved_for_human_edit: true
```

模板锁定规则：

1. frontmatter 只保留 4 字段，不提前偷渡 wiki 字段。
2. body 可以承载平台元数据和 trust trace 摘要，但不应承载 runtime 配置、secret、cookie、token。
3. 写入动作必须分成 `preview` 和 `commit` 两段；`commit` 之前先做人类可读预览。
4. 任何未来实现都不得改写 `~/workspace/raw/System/**`。

## §7 Wave 4 集成验收建议

本次扫描给出的不是 runtime 批准，而是 future acceptance checklist。

建议把 Wave 4 验收拆成 3 层：

### 7.1 raw export contract checks

- 文件路径被 containment 检查锁定在 `${SCOUTFLOW_VAULT_ROOT}/00-Inbox/`
- frontmatter 恰好 4 字段：`title`、`date`、`tags`、`status`
- `tags: 调研/ScoutFlow采集`
- `status: pending`
- 不含重复字段
- `date` 为 `YYYY-MM-DD`

### 7.2 downstream compatibility checks

- 用真实样本跑 `/intake`，确认用户现有流程不报错
- 样本进入后不会要求 ScoutFlow 预先补 `type/domain/priority/source`
- 进入 wiki 之前的转换责任明确属于 downstream，而不是 ScoutFlow export

### 7.3 article-level audit reference checks

- `audit-wiki.py` 当前 article-level 规则应被视为下游兼容性参考
- 若未来希望直接对 ScoutFlow 原始导出做自动审计，应新增 raw-note 专用检查，而不是直接复用当前 `A1-D1 + V1-V8` 全集
- 若未来坚持“audit-wiki.py 0 红线”作为 release 尺，必须先明确该尺是针对 downstream wiki 成品，还是针对 ScoutFlow 00-Inbox 原始导出；这两个对象现在不是同一份文件

最终结论：

- ScoutFlow 对用户 vault 的最小兼容 frontmatter 已可锁定为 4 字段。
- `tags: 调研/ScoutFlow采集` 与 `status: pending` 应作为默认导出契约保留。
- `audit-wiki.py` 是重要参考，但当前并不是 `00-Inbox` raw export 的直接裁判器。
- Wave 4 真正需要补的是 raw export validator，而不是修改用户 vault 规范。
