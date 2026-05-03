---
title: T-P1A-007 Explore URL UX / Risk / Trust Trace Brainstorm
date: 2026-05-03
owner_tool: codex-desktop
status: note-draft
not_authority: true
not_implementation_approval: true
not_runtime_approval: true
scope: Explore URL paste, preview-before-capture, risk prompts, Trust Trace / receipt display
not_for_change:
  - apps/**
  - services/**
  - workers/**
  - packages/**
  - data/**
  - referencerepo/**
  - runtime capture
recommendation: Explore should be a capture intent confirmation page, not a recommendation evaluation page.
---

# 1. Boundary

- 本 note 只做 `T-P1A-007` 的 UX brainstorm / decision pack 草案。
- 本 note 不写 frontend，不改 API，不创建 worker，不运行 `BBDown` / `yt-dlp` / `ffmpeg` / `ASR`。
- 本 note 不批准 `audio_transcript` runtime，不更改 schema，不让 `recommendation / keyword / RAW gap` 直接创建 capture。
- 当前仓库的已合入事实仍是 `T-P1A-001` metadata-only API-side baseline、`T-P1A-002` receipt / artifact ledger baseline、`T-P1A-004` redaction / secret-scan baseline。
- 当前代码事实与本 note 的 UX 候选状态必须分开：
  - 代码事实：`/captures/discover` 当前只接受 `platform=bilibili`、`source_kind=manual_url`、`quick_capture_preset=metadata_only`。
  - 代码事实：`audio_transcript` 当前返回 `422 not_implemented_in_T-P1A-001`。
  - UX 候选：`preview_ready`、`probe_blocked`、`audio_eval_ready`、`Trust Trace` 等是 Explore 决策包，不代表当前代码已实现。
- 相关边界来源：
  - [AGENTS.md](/Users/wanglei/workspace/ScoutFlow/AGENTS.md)
  - [docs/current.md](/Users/wanglei/workspace/ScoutFlow/docs/current.md)
  - [docs/task-index.md](/Users/wanglei/workspace/ScoutFlow/docs/task-index.md)
  - [docs/PRD-v1.1-amendment-2026-05-02.md](/Users/wanglei/workspace/ScoutFlow/docs/PRD-v1.1-amendment-2026-05-02.md)
  - [docs/SRD-v1.1-amendment-2026-05-03.md](/Users/wanglei/workspace/ScoutFlow/docs/SRD-v1.1-amendment-2026-05-03.md)
  - [docs/specs/worker-receipt-contract.md](/Users/wanglei/workspace/ScoutFlow/docs/specs/worker-receipt-contract.md)
  - [docs/specs/platform-adapter-risk-contract.md](/Users/wanglei/workspace/ScoutFlow/docs/specs/platform-adapter-risk-contract.md)
  - [docs/specs/raw-response-redaction.md](/Users/wanglei/workspace/ScoutFlow/docs/specs/raw-response-redaction.md)

# 2. Core Narrative

Explore 的定位应固定为：

```text
采集意图确认页
  -> 确认我想采什么
  -> 当前是否能安全预览
  -> 是否允许 quick_capture
  -> 是否需要 Scope Gate
```

Explore 不是：

- 推荐评估页
- 内容消费页
- 热度评估页
- source discovery 页
- `/captures/discover` 语义扩展页
- 技术日志页

当前主叙事应保持：

```text
左侧：我想采什么
中间：这到底是什么对象
右侧：机器现在有没有开始、有没有留下可信轨迹
底部：我下一步能做什么
```

# 3. Confirmed Decisions

## 3.1 Decision 1 - B Layout

- decision：
  - 采用 B 布局：左侧 `URL 输入 + Preview`，右侧 `Status / Trust Trace`。
- rationale：
  - 比极简单列更容易承载状态和审计轨迹。
  - 比 gate-first 向导更适合 `Phase 1A` 的 `metadata_only quick_capture`。
- current boundary：
  - 这是信息架构决策，不等于 frontend 实现批准。

## 3.2 Decision 2 - 右侧栏按阶段改语义

- decision：
  - 未创建 capture 前，右侧不叫 `Receipt`，只叫 `Status / Trust Trace / 采集状态`。
  - capture 创建后，右侧才进入 `Receipt / Ledger Trace` 语义。
- rationale：
  - 避免 URL 已粘贴但系统尚未创建 capture 时出现“已经有 receipt”的语义错觉。
- current boundary：
  - 这是 Explore UX 命名规则，不改变 receipt contract。

## 3.3 Decision 3 - Preview Before Capture

- decision：
  - 粘贴 URL 后先 preview，不创建 capture。
  - 只有用户点击 `metadata_only` 后才创建 capture。
  - `preview / probe / validation != capture creation`。
- rationale：
  - 符合 LP-001 的“信号、预览、采集分层”精神。
  - 避免 capture 噪声和无意创建 artifact root。
- current boundary：
  - 当前代码没有 preview-only endpoint；本条是 Explore 决策包，不是 API 已实现事实。

## 3.4 Decision 4 - `metadata_only` 是唯一默认 primary

- decision：
  - 只有 `manual_url + low risk` 时，`metadata_only` 是 primary。
- rationale：
  - Explore 首屏应始终只有一个真正的 primary action，减少单人误点。
- current boundary：
  - 当前代码事实与此一致：`metadata_only` 是 `/captures/discover` 唯一允许的 quick_capture preset。

## 3.5 Decision 5 - `audio_transcript` 只作评估入口

- decision：
  - `audio_transcript` 只能写成“评估 audio_transcript”。
  - 不写成“开始 audio_transcript”或“采集音频转写”。
- rationale：
  - 当前仓库基线中，`audio_transcript` 会被 `422 not_implemented_in_T-P1A-001` 拒绝。
  - UX 不能伪装成当前可直接执行能力。
- current boundary：
  - 不批准任何 `audio / ffmpeg / ASR` runtime。

## 3.6 Decision 6 - Local Validation 与 Platform Probe 分层

- decision：
  - `local validation` 只判断 `URL / host / scheme / BV / URL type`。
  - `platform probe / adapter` 才能给出 `auth_required / vip_required / region_blocked / forbidden / parser_drift` 等风险。
- rationale：
  - 避免纯字符串校验阶段声称“已经知道需要登录 / 付费 / 地区受限”。
- current boundary：
  - 当前代码入口已有 `unsupported_platform`、`invalid_bilibili_url`、`source_kind_not_allowed`、`lp001_direct_capture_forbidden`、`not_implemented_in_T-P1A-001`。

## 3.7 Decision 7 - `parser_drift` 分阶段处理

- decision：
  - URL parse / preview 阶段：可显示黄色“解析可能不准”。
  - adapter / metadata_fetch 阶段：`platform_result=parser_drift` 应阻断 quick_capture 或触发修复任务。
- rationale：
  - `parser_drift` 在 contract 层是 stop-the-line 倾向，不能在 adapter 阶段继续凑合。
- current boundary：
  - 该 typed result 已在 platform risk contract 和 receipt tests 中存在。

## 3.8 Decision 8 - 审计块必须脱敏

- decision：
  - 默认只复制脱敏审计块。
  - 不允许把 `raw response` 或 `stderr` 原文放进审计块。
- rationale：
  - `raw response`、`logs`、`stderr` 受 redaction contract 约束。
- current boundary：
  - 与 `redaction_applied`、`redaction_policy`、`sensitive_fields_removed` contract 保持一致。

## 3.9 Decision 9 - 非手动来源统一走 Scope Gate

- decision：
  - `recommendation / keyword / RAW gap` 进入 Explore 时，禁止 quick_capture。
  - primary action 改为 `打开 Scope`，并解释原因。
- rationale：
  - LP-001 明确禁止这些来源默认直接进入采集。
  - 同样是 URL，也必须解释为什么 action 不同。
- current boundary：
  - 当前 `/captures/discover` 已拒绝 `recommendation / keyword / raw_gap` 直接创建 capture。

## 3.10 Decision 10 - 保持当前 schema 命名分层

- decision：
  - 保持：
    - `captures.source_kind = manual_url | capture_plan`
    - `captures.created_by_path = quick_capture | capture_plan | manual_admin`
    - `signals.origin_kind = source_item | recommendation | raw_node | manual | agent`
- rationale：
  - 当前 SRD amendment、代码和测试都已按该分层命名。
  - UI / audit 可展示更易懂的 origin label，但不改当前 contract。
- current boundary：
  - `v_captures_with_origin`、ledger origin summary、重命名 `quick_capture -> manual_url` 只列入 `Phase 2+` 候选。

# 4. UI State Table

| state | capture_created? | source context | primary action | secondary action | right panel label | right panel content | stop / gate reason |
|---|---|---|---|---|---|---|---|
| `empty` | no | none | disabled | none | `Status / Trust Trace` | empty hint | no URL yet |
| `local_url_parsed` | no | `manual_url` candidate | disabled | none | `Status / Trust Trace` | parsed URL shell, no preview yet | waiting local parse completion |
| `invalid_url` | no | malformed / unsupported input | none | fix hint only | `Status / Trust Trace` | `URL 校验失败` tag + fix hint | local validation failed |
| `unsupported_url_type` | no | B 站但不是视频 URL | none | fix hint only | `Status / Trust Trace` | unsupported type hint | local validation failed |
| `preview_ready_manual_low_risk` | no | `manual_url` | `只采 metadata` | `评估 audio_transcript` | `Status / Trust Trace` | preview summary, low-risk tags, `未创建 capture` | no gate |
| `preview_ready_manual_probe_blocked` | no | `manual_url` | disabled | `打开 Scope` | `Status / Trust Trace` | blocking risk tag, probe result, no capture | `auth_required` / `vip_required` / `region_blocked` / `forbidden` |
| `preview_ready_non_manual_scope_required` | no | `recommendation / keyword / raw_gap` | `打开 Scope` | `查看详情` | `Status / Trust Trace` | source label, scope-required reason | LP-001 source gate |
| `audio_eval_ready` | no | `manual_url` | `确认 audio 评估` | `返回 metadata_only` | `Status / Trust Trace` | budget summary, ffmpeg / ASR notice, signed URL warning | confirmation required |
| `capture_created_metadata_only` | yes | `manual_url -> quick_capture` | `复制审计块` | `查看状态` | `Receipt / Ledger Trace` | capture_id shell, status, artifact_count | capture created |
| `metadata_fetch_running` | yes | existing capture | `查看状态` | `查看错误` if failure-ready | `Receipt / Ledger Trace` | `⏳`, last_event, platform_result | job running |
| `metadata_fetched` | yes | existing capture | `复制审计块` | `复制脱敏专业审计块` | `Receipt / Ledger Trace` | `✅`, artifact_count, receipt summary | success |
| `metadata_failed` | yes | existing capture | `复制审计块` | `查看错误` | `Receipt / Ledger Trace` | `❌`, failure summary, last_event | metadata fetch failed |
| `parser_drift_blocked` | yes or no | probe or adapter stage | none | `打开 Scope` or repair note | `Status / Trust Trace` or `Receipt / Ledger Trace` | parser drift summary | stop-the-line |
| `receipt_ready` | yes | existing capture with receipt summary | `复制审计块` | `复制脱敏专业审计块` | `Receipt / Ledger Trace` | receipt / ledger summary | receipt available |

说明：

- `audio_eval_ready` 是 UX 候选状态，不代表当前 API 已支持该 runtime。
- `parser_drift_blocked` 允许在未创建 capture 的 probe 阶段出现，也允许在已创建 capture 的 metadata job 阶段出现。

# 5. State Machine

建议的 Explore 状态机：

```text
empty
  -> local_url_parsed
  -> preview_ready
  -> capture_created
```

补充失败 / gate 分支：

```text
empty
  -> local_url_parsed
    -> invalid_url
    -> unsupported_url_type
    -> preview_ready
      -> probe_blocked
      -> scope_required
      -> audio_eval_ready
      -> capture_created
        -> metadata_fetch_running
          -> metadata_fetched
          -> metadata_failed
          -> parser_drift_blocked
        -> receipt_ready
```

约束：

- `preview_ready` 之前没有 capture。
- `capture_created` 只能由用户明确点击 `metadata_only` 触发。
- `scope_required` 不得旁路成 direct capture。
- `parser_drift_blocked` 在 adapter 阶段是阻断，不是普通黄色提醒。

# 6. Preview Card Field Policy

## 6.1 Default Visible Fields

- 平台：`Bilibili`
- 来源标签：`manual_url / recommendation / keyword / raw_gap`
- `BV`
- 标题
- `UP` 主
- 总时长
- 分 `P` 数
- 字幕状态
- 风险标签
- 建议动作

规则：

- 封面只保留小缩略图，用来确认对象。
- 封面不能成为内容消费入口，也不能抢过标题和建议动作。
- 默认层服务“确认采集对象”和“确认下一步动作”，不服务热度判断。

## 6.2 Details Expanded Fields

- 发布时间
- 简介摘要
- 分 `P` 列表
- 播放量 / 点赞 / 评论 / 收藏 / 弹幕
- `aid / cid`
- 版权 / 付费 / 下载权限 flags

规则：

- 这些字段默认不进首屏。
- `播放量 / 点赞 / 评论` 属于“内容评估”，不应让 Explore 滑向推荐评估页。

## 6.3 Professional / Audit Fields

- `capture_id`
- `job_id`
- `platform_result`
- `producer`
- `artifact_count`
- `ledger path`
- `redaction_applied`

规则：

- 这些不是 Preview 内容，而是信任轨迹。
- 默认进入右侧专业版或审计块，不进入默认 Preview Card。

# 7. Risk Prompt Policy

## 7.1 `metadata_only`

- 轻量风险标签。
- 不做二次确认。
- 阻断风险出现时，禁用按钮或转 `Scope`。

示例：

- low：
  - `public`
  - `metadata-only`
- medium：
  - `parser suspected`
  - `over budget warning`
- blocking：
  - `auth_required`
  - `vip_required`
  - `region_blocked`
  - `forbidden`
  - `parser_drift` at adapter stage

## 7.2 `audio_transcript`

- 必须二次确认。
- 展示预算和范围：
  - 预计音频时长
  - 预计 `ASR` 时长
  - 媒体大小
  - 是否触碰 `audio / ffmpeg / ASR`
  - `signed URL` / temporary media URL 不可保存

## 7.3 文案层级

- UI 层默认说人话，不用法务腔。
- contract / audit 层保留 typed 术语。
- 但 `vip_required / forbidden / signed URL / raw response` 这类边界问题必须明确阻断，不软化成“你自己看着办”。

推荐阻断文案：

- 这是付费视频，当前不支持采集
- 需要登录，当前 quick_capture 不继续
- 解析结构变化，已停止，需修复 adapter
- signed URL 不可保存为 evidence

# 8. URL Error Copy

## 8.1 Local Validation Errors

| code family | example copy | UI position | note |
|---|---|---|---|
| host unsupported | 当前只支持 Bilibili 视频链接 | input inline error | local only |
| missing BV | 未识别到 BV 号，请检查 URL | input inline error | local only |
| unsupported type | 这是 B 站专栏链接，当前只支持视频 | input inline error | local only |
| scheme invalid | 链接格式不对，请用 http 或 https | input inline error | local only |
| repair hint | 试试只粘贴 BV 号：`BV1xx411c7xx` | inline hint | local only |

规则：

- local validation 只说自己确实知道的事实。
- 不在 local validation 阶段声称“需要登录 / 付费 / 地区受限”。

## 8.2 Platform Probe / Adapter Risks

| typed result | example copy | UI surface | note |
|---|---|---|---|
| `auth_required` | 需要登录，当前 quick_capture 不继续 | risk tag / scope gate | from probe/adapter only |
| `vip_required` | 这是付费视频，当前不支持采集 | risk tag / scope gate | from probe/adapter only |
| `region_blocked` | 地区限制，需人工判断 | risk tag / scope gate | from probe/adapter only |
| `forbidden` | 当前访问被拒绝，需人工判断 | risk tag / scope gate | from probe/adapter only |
| `parser_drift` | 解析结构变化，已停止，需修复 adapter | blocking error / stop line | from adapter stage |

规则：

- `auth_required / vip_required / region_blocked / forbidden / parser_drift` 必须来自 platform probe 或 adapter。
- probe 风险和 local validation 错误是两套不同来源，不应混写。

# 9. Trust Trace / Receipt Panel

## 9.1 Before Capture

- label = `Status / Trust Trace / 采集状态`
- no receipt yet
- no `capture_id` yet
- 只显示：
  - local validation / probe 结果
  - 风险标签
  - 当前建议动作
  - `未创建 capture`

## 9.2 After Capture

- label = `Receipt / Ledger Trace`
- 可以显示 receipt / artifact ledger summary

## 9.3 简版字段

- `status`
- `platform_result`
- `risk tags`
- `last_event`
- `artifact_count`
- `复制审计块`

补充：

- 图标可用：
  - 成功 `✅`
  - 失败 `❌`
  - 进行中 `⏳`
- 正常状态不显示日志入口。
- 失败时可以显示小按钮：`查看错误`。

## 9.4 专业版字段

- `capture_id`
- `job_id`
- `platform_result`
- `producer`
- `artifact_assets summary`
- `ledger path`
- `logs.job_log_path`
- `redaction_applied`

补充：

- 可显示 `查看日志摘要`
- 可显示 `打开日志文件`
- 日志只允许脱敏摘要，不允许 raw response / stderr 原文

## 9.5 复制按钮文案

- `复制审计块`
- `复制脱敏专业审计块`

tooltip：

```text
仅复制脱敏后的 job / receipt / ledger 摘要，不包含 raw response / stderr 原文。
```

# 10. Scope Gate And Source Origin

当前 rule：

- 只有 `manual_url` 才能 quick_capture `metadata_only`。
- `recommendation / keyword / RAW gap` 只能 `打开 Scope`。

当前 schema / contract 命名保持不变：

```text
captures.source_kind
  manual_url
  capture_plan

captures.created_by_path
  quick_capture
  capture_plan
  manual_admin

signals.origin_kind
  source_item
  recommendation
  raw_node
  manual
  agent
```

UI / audit 展示层可显示 human-friendly origin label：

- `manual_url`
- `recommendation`
- `keyword`
- `raw_gap`

审计链路表达：

```text
capture
  -> capture_plan
  -> signal
  -> origin_kind=recommendation / raw_node / ...
```

当前不作为 requirement：

- `v_captures_with_origin`
- ledger `origin_kind` 摘要
- `created_by_path=quick_capture` 改名为 `manual_url`

这些只列为 `Phase 2+ / future schema amendment candidate`。

# 11. Copy Audit Block Draft

脱敏审计块样例：

```yaml
source_context:
  ui_origin_label: manual_url
  capture_source_kind: manual_url
  capture_created_by_path: quick_capture
  canonical_url: https://www.bilibili.com/video/BV1AB411c7mD
  platform: bilibili
  platform_item_id: BV1AB411c7mD
ui_state:
  state: metadata_fetched
  panel_label: Receipt / Ledger Trace
  primary_action: 复制审计块
capture_summary:
  capture_id: 01HXCAP0001
  job_id: 01HXJOB0001
  capture_mode: metadata_only
platform_result:
  value: ok
  last_event: metadata_fetched
risk_summary:
  tags:
    - public
    - metadata-only
  blocking: false
artifact_summary:
  artifact_count: 1
  artifact_kinds:
    - capture_manifest
redaction_summary:
  redaction_applied: true
  redaction_policy: credentials-v1
  sensitive_fields_removed:
    - headers.cookie
    - headers.authorization
    - set_cookie
    - token
open_questions:
  - Should Trust Trace default label use Chinese or mixed English?
```

规则：

- 不包含 `raw response` 原文
- 不包含 `stderr` 原文
- 不包含 `Cookie / Authorization / token / signed URL` 原文

# 12. Open Decisions

- 右侧栏最终中文名：
  - `Status`
  - `Trust Trace`
  - `采集状态`
- 风险标签的最终视觉分级：
  - 是否使用固定 `low / medium / blocking` 三档样式
- `audio_transcript` 二次确认框是否允许“记住我的选择”
  - 当前建议：允许作为候选，但默认不记住
- `Phase 2+` 是否增加 `v_captures_with_origin`

# 13. Rejected / Deferred

- 不把 Explore 做成推荐评估页
- 不让 `播放量 / 点赞 / 评论` 进入默认首屏
- 不在 `T-P1A-007` 写 frontend
- 不在 `T-P1A-007` 改 API / schema
- 不把 `audio_transcript` 写成当前可执行
- 不把 `raw response / stderr` 原文写入审计块
- 不让 `recommendation / keyword / RAW gap` 直接 quick_capture
- 不把 adapter 阶段的 `parser_drift` 软化成黄色提醒
