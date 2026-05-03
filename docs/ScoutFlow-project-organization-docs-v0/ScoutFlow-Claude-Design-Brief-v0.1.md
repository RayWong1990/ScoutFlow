# ScoutFlow Claude Design Brief v0.1

> 用途：给 Claude Design / Opus / user 生成 ScoutFlow UI 原型时使用。Claude Design 负责探索与原型，不是生产代码真源。

---

## 0. 工具定位

Claude Design 用于：

```text
视觉方向探索
高保真 UI mock
交互原型
Signal Workbench 三栏布局推演
Pitch / review deck
handoff 给 Claude Code / Codex 的设计说明
```

不用于：

```text
直接生成生产 React 代码并合入 repo
决定 API contract
决定 DB schema
决定 LP 规则
```

---

## 1. 产品气质

ScoutFlow 是：

```text
本地优先的内容采集 / 转写 / 证据沉淀 / 选题发现工作站
```

它不是：

```text
视频下载器
通用 SaaS 后台
Notion 风知识库
纯 RSS reader
营销增长工具
```

视觉关键词：

```text
dark-first
high-density
research workstation
evidence ledger
mission control
pipeline visibility
calm but precise
```

---

## 2. 设计红线

```text
推荐流不出现主按钮 [采集]
默认动作为 [打开 Scope] / [验证信号]
quick_capture 只作为 manual_url 的例外
RAW 只写 inbox，不出现 [自动合并]
Evidence Browser Phase 1 不真嵌平台登录页
不要使用 crawler/spider/scrape/harvest 词汇
```

---

## 3. 需要生成的核心页面

### 3.1 Mission Control

目标：5 秒看懂今天要处理什么。

组件：

```text
Today numbers
Source health
Pipeline map
Decision dock
Recommended/Signal feed
```

### 3.2 Signal Radar

目标：看新信号，不直接采集。

卡片必须包括：

```text
platform
creator
title
score
reason
origin/source hits
actions: Open Scope / Verify Signal / Watch / Ignore
```

### 3.3 Signal Workbench

三栏：

```text
Left: Signal Board
Middle: Signal Brief + Hypotheses + related signals
Right: Evidence Workspace
  - Evidence Browser
  - Brainstorm Notes
  - Scope Builder
```

Brainstorm Notes 常驻，不可隐藏。

### 3.4 Capture Pipeline

目标：显示 plan / capture / worker 当前状态。

必须有：

```text
plan grouped view
capture row matrix
pipeline node graph
job detail drawer
retry/cancel controls
logs tail preview
```

### 3.5 Transcript Studio

目标：审校、标记、播放片段。

必须有：

```text
media preview
waveform
timestamped transcript timeline
segment tags
LLM action side panel
```

### 3.6 Copy Library

目标：本地文案库搜索。

必须有：

```text
search
filters
tags
capture cards
segment preview
normalized summary
promotion state
```

### 3.7 Knowledge Bridge

目标：capture → RAW inbox，不自动合并。

必须有：

```text
raw suggestions
patch preview
accept/reject/edit
write to RAW inbox
```

### 3.8 Agent Dispatch

Phase 4 才实现。Phase 0 只做静态占位。

---

## 4. Claude Design Prompt 1：三种视觉方向

```text
Create three distinct high-fidelity visual directions for ScoutFlow, a dark-first local-first research workstation for content capture, ASR transcription, evidence management, capture planning, and topic discovery.

Do not make it look like a generic SaaS dashboard or video downloader.

Direction A: Dense Console / Linear-like precision.
Direction B: Evidence Lab / research workstation.
Direction C: Mission Control / pipeline and signal orchestration.

Each direction should include:
- Mission Control screen
- Signal Radar screen
- Signal Workbench three-column detail screen
- Capture Pipeline screen
- Copy Library screen

Important product rules:
- Recommendations cannot directly capture.
- The primary action is Open Scope or Verify Signal.
- quick_capture only appears for a manual single URL.
- RAW writes only go to inbox; never auto-merge.
- Avoid words: crawl, crawler, spider, scrape_all, auto_capture, harvest.

Use a dark, information-dense interface with strong status semantics.
```

---

## 5. Claude Design Prompt 2：Signal Workbench 深化

```text
Design the Signal Workbench for ScoutFlow.

Layout:
- Left column: Signal Board grouped by status: observed, opened, hypothesized, browsing, plan_ready, capturing, evidence_locked, dismissed.
- Middle column: Signal Brief with title, score, reason, origin, related RAW nodes, hypotheses list, confidence controls, topic card link.
- Right column: Evidence Workspace with three stacked areas:
  1. Evidence Browser metadata preview
  2. Brainstorm Notes, always visible and not collapsible
  3. Scope Builder with targets, budget, estimate, approve, run

Rules:
- No direct Capture button from a signal.
- Show Open Scope / Verify Signal language.
- Plan must show estimate before approve.
- Visualize budget: media MB, ASR minutes, LLM tokens, risk.
- Include browsing session event trail.

Style:
- Dark-first
- high-density
- professional research console
- precise status chips
- subtle grid/panel layout
```

---

## 6. Claude Design Prompt 3：Capture Pipeline

```text
Design the Capture Pipeline screen for ScoutFlow.

It should support two modes:
1. Grouped by capture_plan
2. Flat list by capture

Show:
- plan progress
- capture lifecycle nodes
- worker job matrix
- current status
- failed nodes
- job detail drawer with produced artifacts, logs, receipts, retry/cancel actions

Artifact zones:
- bundle
- media
- transcript
- normalized
- links
- logs

Make the interface feel like an evidence ledger and worker control room, not a downloader queue.
```

---

## 7. Claude Design Prompt 4：Copy Library + Knowledge Bridge

```text
Design Copy Library and Knowledge Bridge for ScoutFlow.

Copy Library:
- searchable capture cards
- transcript segment search
- tags and filters
- promotion_state: L1-only, L2-validated, L-global
- normalized summary and quotes preview

Knowledge Bridge:
- raw-suggestions list
- patch preview with diff-like formatting
- relation_type chips: supports, contradicts, extends, example_of, quote_for, topic_seed, script_material
- accept/reject/edit
- write to RAW inbox only

Do not show auto-merge.
Do not imply ScoutFlow is the RAW authority.
```

---

## 8. Handoff 给 Codex 的格式

Claude Design 原型完成后，输出给 Codex 的 handoff 应该是：

```markdown
# UI Handoff

## Selected direction

## Screens included

## Design tokens
- colors
- typography
- spacing
- status chips

## Components
- AppShell
- SignalCard
- SignalWorkbenchLayout
- ScopeBuilder
- BudgetMeter
- PipelineCanvas
- JobDetailDrawer
- TranscriptTimeline
- LibraryCard
- RawPatchPreview

## Redlines
- no direct capture from recommendation
- no auto merge to RAW
- no forbidden naming

## Implementation notes
- React/Vite/shadcn
- TanStack Router
- TanStack Query
- Zustand for UI-only state
- React Flow for pipeline
```

---

## 9. Claude Design 已知限制记录

Claude Design 是 research preview。使用时要注意：

```text
inline comments 可能偶发丢失，关键反馈应同时写到 chat
compact view 可能有保存问题，出现时切 full view 重试
生成结果必须经过 user / Opus / Codex review，不直接落生产
```

---

## 10. 最终建议

ScoutFlow 前端设计应让 Claude Design 做“最快探索”，但让 React/Vite/shadcn 做“工程落地”。

```text
Claude Design = 视觉和交互的扩散器
Opus = 设计判断与 IA 修正
Codex = 生产实现与 contract 对齐
user = 最终 taste 和方向裁决
```
