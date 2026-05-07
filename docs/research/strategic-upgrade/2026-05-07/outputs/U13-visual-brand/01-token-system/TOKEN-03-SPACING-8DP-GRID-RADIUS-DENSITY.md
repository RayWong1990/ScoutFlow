---
title: TOKEN-03 Spacing 8dp Grid Radius Density
status: "candidate / not-authority"
authority: not-authority
created_at: 2026-05-07
atlas_id: U13-visual-style-brand-atlas-v0
file_kind: token
claim_labels:
  - canonical fact from local packet
  - promoted_addendum-aware inference
  - tentative candidate
  - needs_live_web_refresh
boundary: "docs-only; no runtime/package/frontend/browser/vault/migration approval"
---

# TOKEN-03 Spacing 8dp Grid Radius Density

## Purpose

Spacing is the main difference between a trustworthy operator station and a crowded pseudo-dashboard. ScoutFlow uses an 8dp grid with a controlled 4px micro-step for badges and hairline adjustments.

| Ref name | Value | Role | Usage example |
|---|---:|---|---|
| `sf.space.0` | `0` | reset | Use as token alias, not magic number |
| `sf.space.1` | `4px` | micro | Use as token alias, not magic number |
| `sf.space.2` | `8px` | badge/control | Use as token alias, not magic number |
| `sf.space.3` | `12px` | row inner | Use as token alias, not magic number |
| `sf.space.4` | `16px` | panel padding | Use as token alias, not magic number |
| `sf.space.5` | `24px` | grid gap | Use as token alias, not magic number |
| `sf.space.6` | `32px` | page/presentation | Use as token alias, not magic number |
| `sf.radius.1` | `4px` | micro chip | Use as token alias, not magic number |
| `sf.radius.2` | `8px` | panel | Use as token alias, not magic number |
| `sf.radius.3` | `12px` | control/card | Use as token alias, not magic number |
| `sf.radius.4` | `16px` | template/hero | Use as token alias, not magic number |
| `sf.radius.5` | `24px` | poster/splash | Use as token alias, not magic number |

## Density modes

| Mode | Page padding | Station max | Grid gap | Panel padding | Use case |
|---|---:|---:|---:|---:|---|
| compact | 16px | 1200px | 16px | 14px | laptop / high data density |
| default | 24px | 1360px | 24px | 16px | normal desktop review |
| relaxed | 32px | 1440px | 28px | 20px | presentation / screenshot export |

## Four-panel layout

```mermaid
flowchart TB
  D[Desktop >=1180] --> D1[URL Bar full width]
  D1 --> D2[Metadata 0.85fr | Scope 0.95fr | Trust Trace 1.45fr]
  T[Tablet 720-1179] --> T1[URL Bar]
  T1 --> T2[Metadata | Scope]
  T2 --> T3[Trust Trace full width]
  M[Mobile <720] --> M1[URL]
  M1 --> M2[Metadata]
  M2 --> M3[Scope]
  M3 --> M4[Trust Trace]
```

## Review checks

- Panel edges must align across columns; tiny differences in panel padding create cognitive noise.
- Badge padding may use 4px/8px; never let badges look like primary buttons.
- Trust Trace requires extra horizontal room; however, URL action remains the first attention stop.
- Mobile safe area must preserve URL action, current state and graph/list fallback.


## Boundary / 边界声明

- `status`: candidate；`authority`: not-authority；本文件不是 CSS token 合并、frontend implementation、package install、browser automation、runtime、vault true write、migration 或 authority writeback 批准。
- 可被 PF-V / GPT-Image-2 / future dispatch 作为视觉 atlas 输入；不可把本文内任何 token、SVG、layout 或 template 直接解释成 production contract。
- 所有主观 5-Gate 判断保持 human-in-loop；自动化只能提供截图、contrast、DOM 或 manifest evidence，不能替代最终视觉判断。
- 第三方库仅作为参考类别；本 atlas 内联 SVG 均按 ScoutFlow-original candidate 处理，未复制第三方 path。若未来改用第三方 icon/illustration，必须重新验证 license。


### TOKEN-03 Spacing 8dp Grid Radius Density — audit expansion 1

### Implementation seam / 实现缝合位

推荐未来实现路径为 CSS Variables + CSS Modules + container queries。`tokens.ts` 只可作为 typed mirror；Style Dictionary、Tokens Studio、Tailwind、Panda、shadcn、React Flow、Lucide、Radix、TanStack 或 React 版本升级都不得从本文件自动推出。若某个 dispatch 需要这些 package，应在独立 package gate 中提出，不在 visual atlas 中夹带批准。

本节适用于 `TOKEN-03 Spacing 8dp Grid Radius Density`：审查者应记录 source label、state word、token reference、layout slot、failure class、defer condition 与 human reviewer note。若证据缺失，写 `needs_evidence`，不得写 `passed by assumption`。


### TOKEN-03 Spacing 8dp Grid Radius Density — audit expansion 2

### Linked-state grammar / 状态语法

每个视觉对象至少绑定一个 state word：`idle`、`editing`、`requested`、`settling`、`ready`、`allowed`、`candidate`、`future_gate`、`blocked`、`stale`、`probe_failed`、`preview_only`。状态应同时体现在文案、badge、border/fill、position/order 与可访问名称中。`audio_transcript`、media processing、browser automation、migration、vault true write 仍必须以 blocked/future-gated 方式出现，不得藏进 tooltip。

本节适用于 `TOKEN-03 Spacing 8dp Grid Radius Density`：审查者应记录 source label、state word、token reference、layout slot、failure class、defer condition 与 human reviewer note。若证据缺失，写 `needs_evidence`，不得写 `passed by assumption`。


### TOKEN-03 Spacing 8dp Grid Radius Density — audit expansion 3

### Review discipline / 审查纪律

1. 先判断 L1 information architecture：URL Bar → Live Metadata → Capture Scope → Trust Trace 的扫描顺序不可被模板、装饰图、sidebar 或 KPI 区域改写。
2. 再判断 L2 structure：panel、row、badge、detail shelf、graph node、template slot 必须共享 8dp rhythm 与同一套语义 token，不允许在局部硬编码新的蓝色、阴影或圆角。
3. 最后判断 L3 mood：深海蓝、低眩光、operator workstation、evidence-first、single-user dense surface；强视觉不是荧光科技感，也不是营销 hero 图。
4. 对任何 `blocked` / `future_gate` / `candidate` lane，必须有文字、badge、位置与视觉权重共同表达；颜色不能成为唯一信号。
5. 任何截图、render pass、contrast pass 都只能作为 evidence；若 Gate 1-5 任一失败，最终 verdict 必须是 `visual_not_passed`。

本节适用于 `TOKEN-03 Spacing 8dp Grid Radius Density`：审查者应记录 source label、state word、token reference、layout slot、failure class、defer condition 与 human reviewer note。若证据缺失，写 `needs_evidence`，不得写 `passed by assumption`。


### TOKEN-03 Spacing 8dp Grid Radius Density — audit expansion 4

### 5-Gate alignment / 五门对齐

| Gate | Local acceptance | Failure signal |
|---|---|---|
| Gate 1 hierarchy | 主动作或主证据 3 秒内可识别 | 装饰、图表、future lane 抢第一注意点 |
| Gate 2 spacing/alignment | 8dp grid、共同 baseline、稳定 panel padding | row、badge、图节点漂移，导致扫描断裂 |
| Gate 3 occlusion | tooltip/toast/legend 不遮 URL/current state/node label | overlay 遮住可操作或可审计信息 |
| Gate 4 typography/readability | 中英混排、URL、ID、timestamp 可读 | 小字、低对比、截断造成状态误判 |
| Gate 5 visual weight | active/current/proven 高于 blocked/candidate/future | danger 或 decorative glow 反向支配界面 |

本节适用于 `TOKEN-03 Spacing 8dp Grid Radius Density`：审查者应记录 source label、state word、token reference、layout slot、failure class、defer condition 与 human reviewer note。若证据缺失，写 `needs_evidence`，不得写 `passed by assumption`。


### TOKEN-03 Spacing 8dp Grid Radius Density — audit expansion 5

### Implementation seam / 实现缝合位

推荐未来实现路径为 CSS Variables + CSS Modules + container queries。`tokens.ts` 只可作为 typed mirror；Style Dictionary、Tokens Studio、Tailwind、Panda、shadcn、React Flow、Lucide、Radix、TanStack 或 React 版本升级都不得从本文件自动推出。若某个 dispatch 需要这些 package，应在独立 package gate 中提出，不在 visual atlas 中夹带批准。

本节适用于 `TOKEN-03 Spacing 8dp Grid Radius Density`：审查者应记录 source label、state word、token reference、layout slot、failure class、defer condition 与 human reviewer note。若证据缺失，写 `needs_evidence`，不得写 `passed by assumption`。


### TOKEN-03 Spacing 8dp Grid Radius Density — audit expansion 6

### Linked-state grammar / 状态语法

每个视觉对象至少绑定一个 state word：`idle`、`editing`、`requested`、`settling`、`ready`、`allowed`、`candidate`、`future_gate`、`blocked`、`stale`、`probe_failed`、`preview_only`。状态应同时体现在文案、badge、border/fill、position/order 与可访问名称中。`audio_transcript`、media processing、browser automation、migration、vault true write 仍必须以 blocked/future-gated 方式出现，不得藏进 tooltip。

本节适用于 `TOKEN-03 Spacing 8dp Grid Radius Density`：审查者应记录 source label、state word、token reference、layout slot、failure class、defer condition 与 human reviewer note。若证据缺失，写 `needs_evidence`，不得写 `passed by assumption`。


### TOKEN-03 Spacing 8dp Grid Radius Density — audit expansion 7

### Review discipline / 审查纪律

1. 先判断 L1 information architecture：URL Bar → Live Metadata → Capture Scope → Trust Trace 的扫描顺序不可被模板、装饰图、sidebar 或 KPI 区域改写。
2. 再判断 L2 structure：panel、row、badge、detail shelf、graph node、template slot 必须共享 8dp rhythm 与同一套语义 token，不允许在局部硬编码新的蓝色、阴影或圆角。
3. 最后判断 L3 mood：深海蓝、低眩光、operator workstation、evidence-first、single-user dense surface；强视觉不是荧光科技感，也不是营销 hero 图。
4. 对任何 `blocked` / `future_gate` / `candidate` lane，必须有文字、badge、位置与视觉权重共同表达；颜色不能成为唯一信号。
5. 任何截图、render pass、contrast pass 都只能作为 evidence；若 Gate 1-5 任一失败，最终 verdict 必须是 `visual_not_passed`。

本节适用于 `TOKEN-03 Spacing 8dp Grid Radius Density`：审查者应记录 source label、state word、token reference、layout slot、failure class、defer condition 与 human reviewer note。若证据缺失，写 `needs_evidence`，不得写 `passed by assumption`。


### TOKEN-03 Spacing 8dp Grid Radius Density — audit expansion 8

### 5-Gate alignment / 五门对齐

| Gate | Local acceptance | Failure signal |
|---|---|---|
| Gate 1 hierarchy | 主动作或主证据 3 秒内可识别 | 装饰、图表、future lane 抢第一注意点 |
| Gate 2 spacing/alignment | 8dp grid、共同 baseline、稳定 panel padding | row、badge、图节点漂移，导致扫描断裂 |
| Gate 3 occlusion | tooltip/toast/legend 不遮 URL/current state/node label | overlay 遮住可操作或可审计信息 |
| Gate 4 typography/readability | 中英混排、URL、ID、timestamp 可读 | 小字、低对比、截断造成状态误判 |
| Gate 5 visual weight | active/current/proven 高于 blocked/candidate/future | danger 或 decorative glow 反向支配界面 |

本节适用于 `TOKEN-03 Spacing 8dp Grid Radius Density`：审查者应记录 source label、state word、token reference、layout slot、failure class、defer condition 与 human reviewer note。若证据缺失，写 `needs_evidence`，不得写 `passed by assumption`。


### TOKEN-03 Spacing 8dp Grid Radius Density — audit expansion 9

### Implementation seam / 实现缝合位

推荐未来实现路径为 CSS Variables + CSS Modules + container queries。`tokens.ts` 只可作为 typed mirror；Style Dictionary、Tokens Studio、Tailwind、Panda、shadcn、React Flow、Lucide、Radix、TanStack 或 React 版本升级都不得从本文件自动推出。若某个 dispatch 需要这些 package，应在独立 package gate 中提出，不在 visual atlas 中夹带批准。

本节适用于 `TOKEN-03 Spacing 8dp Grid Radius Density`：审查者应记录 source label、state word、token reference、layout slot、failure class、defer condition 与 human reviewer note。若证据缺失，写 `needs_evidence`，不得写 `passed by assumption`。


### TOKEN-03 Spacing 8dp Grid Radius Density — audit expansion 10

### Linked-state grammar / 状态语法

每个视觉对象至少绑定一个 state word：`idle`、`editing`、`requested`、`settling`、`ready`、`allowed`、`candidate`、`future_gate`、`blocked`、`stale`、`probe_failed`、`preview_only`。状态应同时体现在文案、badge、border/fill、position/order 与可访问名称中。`audio_transcript`、media processing、browser automation、migration、vault true write 仍必须以 blocked/future-gated 方式出现，不得藏进 tooltip。

本节适用于 `TOKEN-03 Spacing 8dp Grid Radius Density`：审查者应记录 source label、state word、token reference、layout slot、failure class、defer condition 与 human reviewer note。若证据缺失，写 `needs_evidence`，不得写 `passed by assumption`。


### TOKEN-03 Spacing 8dp Grid Radius Density — audit expansion 11

### Review discipline / 审查纪律

1. 先判断 L1 information architecture：URL Bar → Live Metadata → Capture Scope → Trust Trace 的扫描顺序不可被模板、装饰图、sidebar 或 KPI 区域改写。
2. 再判断 L2 structure：panel、row、badge、detail shelf、graph node、template slot 必须共享 8dp rhythm 与同一套语义 token，不允许在局部硬编码新的蓝色、阴影或圆角。
3. 最后判断 L3 mood：深海蓝、低眩光、operator workstation、evidence-first、single-user dense surface；强视觉不是荧光科技感，也不是营销 hero 图。
4. 对任何 `blocked` / `future_gate` / `candidate` lane，必须有文字、badge、位置与视觉权重共同表达；颜色不能成为唯一信号。
5. 任何截图、render pass、contrast pass 都只能作为 evidence；若 Gate 1-5 任一失败，最终 verdict 必须是 `visual_not_passed`。

本节适用于 `TOKEN-03 Spacing 8dp Grid Radius Density`：审查者应记录 source label、state word、token reference、layout slot、failure class、defer condition 与 human reviewer note。若证据缺失，写 `needs_evidence`，不得写 `passed by assumption`。
