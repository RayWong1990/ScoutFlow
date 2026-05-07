---
title: TOKEN-01 Palette 15 Deep Blue + Derived Status Colors
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

# TOKEN-01 Palette 15 Deep Blue + Derived Status Colors

## Purpose

This file defines the single-source palette nucleus for ScoutFlow's strong visual H5 / operator workstation brand. The visual posture is deep-sea blue, low-glare, evidence-first, and dense enough for a single technical operator. The palette deliberately separates **surface**, **border**, **text**, **accent**, **graph**, and **status** concerns so future PF-V prompts do not reinvent color logic per image.

## Core 15 palette

| Ref name | Value | Role | Usage example |
|---|---:|---|---|
| `sf.canvas.0` | `#07111B` | Core deep-sea/operator color | Use through semantic alias; avoid hardcoded hex |
| `sf.canvas.1` | `#0D1826` | Core deep-sea/operator color | Use through semantic alias; avoid hardcoded hex |
| `sf.canvas.2` | `#101A27` | Core deep-sea/operator color | Use through semantic alias; avoid hardcoded hex |
| `sf.panel.bg` | `#111F31` | Core deep-sea/operator color | Use through semantic alias; avoid hardcoded hex |
| `sf.panel.bg.low` | `#0B1624` | Core deep-sea/operator color | Use through semantic alias; avoid hardcoded hex |
| `sf.panel.bg.raised` | `#16263C` | Core deep-sea/operator color | Use through semantic alias; avoid hardcoded hex |
| `sf.border.subtle` | `#1D3148` | Core deep-sea/operator color | Use through semantic alias; avoid hardcoded hex |
| `sf.border.panel` | `#27415D` | Core deep-sea/operator color | Use through semantic alias; avoid hardcoded hex |
| `sf.border.strong` | `#3A5879` | Core deep-sea/operator color | Use through semantic alias; avoid hardcoded hex |
| `sf.text.primary` | `#EEF4FF` | Core deep-sea/operator color | Use through semantic alias; avoid hardcoded hex |
| `sf.text.secondary` | `#A6B8CF` | Core deep-sea/operator color | Use through semantic alias; avoid hardcoded hex |
| `sf.text.muted` | `#6D8099` | Core deep-sea/operator color | Use through semantic alias; avoid hardcoded hex |
| `sf.accent.cyan` | `#50D4FF` | Core deep-sea/operator color | Use through semantic alias; avoid hardcoded hex |
| `sf.accent.violet` | `#9A7CFF` | Core deep-sea/operator color | Use through semantic alias; avoid hardcoded hex |
| `sf.graph.edge` | `#27415D` | Core deep-sea/operator color | Use through semantic alias; avoid hardcoded hex |

## Derived families

| Ref name | Value | Role | Usage example |
|---|---:|---|---|
| `sf.success` | `#7ADF9B` | Derived status/accent family | Must include state text, not color-only status |
| `sf.warning` | `#FFBE55` | Derived status/accent family | Must include state text, not color-only status |
| `sf.error` | `#FF7B7B` | Derived status/accent family | Must include state text, not color-only status |
| `sf.neutral` | `#7D8DA3` | Derived status/accent family | Must include state text, not color-only status |
| `sf.accent.active` | `#50D4FF` | Derived status/accent family | Must include state text, not color-only status |
| `sf.success.bg` | `#10291F` | Derived status/accent family | Must include state text, not color-only status |
| `sf.warning.bg` | `#332512` | Derived status/accent family | Must include state text, not color-only status |
| `sf.error.bg` | `#33191E` | Derived status/accent family | Must include state text, not color-only status |
| `sf.info.bg` | `#10233D` | Derived status/accent family | Must include state text, not color-only status |

## WCAG 2.2 contrast sample matrix

The matrix below was calculated locally from the included hex values. It is evidence for review, not a full accessibility approval; human review must still check actual font size, weight, rendering, overlays and state wording.

| Pair | Ratio | Verdict |
|---|---:|---|
| `sf.text.primary` on `sf.canvas.0` | 17.21:1 | AA body pass |
| `sf.text.primary` on `sf.canvas.1` | 16.18:1 | AA body pass |
| `sf.text.primary` on `sf.panel.bg` | 15.05:1 | AA body pass |
| `sf.text.primary` on `sf.panel.bg.low` | 16.47:1 | AA body pass |
| `sf.text.primary` on `sf.panel.bg.raised` | 13.82:1 | AA body pass |
| `sf.text.secondary` on `sf.canvas.0` | 9.39:1 | AA body pass |
| `sf.text.secondary` on `sf.canvas.1` | 8.83:1 | AA body pass |
| `sf.text.secondary` on `sf.panel.bg` | 8.21:1 | AA body pass |
| `sf.text.secondary` on `sf.panel.bg.low` | 8.99:1 | AA body pass |
| `sf.text.secondary` on `sf.panel.bg.raised` | 7.54:1 | AA body pass |
| `sf.text.muted` on `sf.canvas.0` | 4.70:1 | AA body pass |
| `sf.text.muted` on `sf.canvas.1` | 4.42:1 | non-critical only / fail for body |
| `sf.text.muted` on `sf.panel.bg` | 4.11:1 | non-critical only / fail for body |
| `sf.text.muted` on `sf.panel.bg.low` | 4.50:1 | AA body pass |
| `sf.text.muted` on `sf.panel.bg.raised` | 3.78:1 | non-critical only / fail for body |
| `sf.accent.cyan` on `sf.canvas.0` | 11.04:1 | AA body pass |
| `sf.accent.cyan` on `sf.canvas.1` | 10.38:1 | AA body pass |
| `sf.accent.cyan` on `sf.panel.bg` | 9.65:1 | AA body pass |
| `sf.accent.cyan` on `sf.panel.bg.low` | 10.57:1 | AA body pass |
| `sf.accent.cyan` on `sf.panel.bg.raised` | 8.86:1 | AA body pass |
| `sf.accent.violet` on `sf.canvas.0` | 6.06:1 | AA body pass |
| `sf.accent.violet` on `sf.canvas.1` | 5.70:1 | AA body pass |
| `sf.accent.violet` on `sf.panel.bg` | 5.30:1 | AA body pass |
| `sf.accent.violet` on `sf.panel.bg.low` | 5.80:1 | AA body pass |
| `sf.accent.violet` on `sf.panel.bg.raised` | 4.87:1 | AA body pass |
| `sf.success` on `sf.canvas.0` | 11.63:1 | AA body pass |
| `sf.success` on `sf.panel.bg` | 10.17:1 | AA body pass |
| `sf.success` on `sf.panel.bg.low` | 11.14:1 | AA body pass |
| `sf.warning` on `sf.canvas.0` | 11.54:1 | AA body pass |
| `sf.warning` on `sf.panel.bg` | 10.08:1 | AA body pass |
| `sf.warning` on `sf.panel.bg.low` | 11.04:1 | AA body pass |
| `sf.error` on `sf.canvas.0` | 7.58:1 | AA body pass |
| `sf.error` on `sf.panel.bg` | 6.62:1 | AA body pass |
| `sf.error` on `sf.panel.bg.low` | 7.25:1 | AA body pass |
| `sf.neutral` on `sf.canvas.0` | 5.62:1 | AA body pass |
| `sf.neutral` on `sf.panel.bg` | 4.91:1 | AA body pass |
| `sf.neutral` on `sf.panel.bg.low` | 5.38:1 | AA body pass |

## Usage examples

```css
:root {
  --sf-canvas-0: #07111B;
  --sf-panel-bg: #111F31;
  --sf-text-primary: #EEF4FF;
  --sf-accent-cyan: #50D4FF;
  --sf-success: #7ADF9B;
  --sf-warning: #FFBE55;
  --sf-danger: #FF7B7B;
}
.captureAction[data-state="ready"] {
  color: var(--sf-canvas-0);
  background: var(--sf-accent-cyan);
}
```

## Mermaid relationship map

```mermaid
flowchart LR
  canvas[Canvas tokens] --> panel[Panel surfaces]
  panel --> border[Border hierarchy]
  panel --> text[Text contrast]
  text --> state[State badges]
  state --> graph[Trust Trace graph]
  graph --> templates[Multi-medium templates]
  tokens[Single-source palette] --> canvas
  tokens --> status[Success / Warning / Error]
```

## Review notes

- `sf.text.muted` is acceptable only for non-critical labels on `canvas.0` or `panel.bg.low`; it is not AA body text on `panel.bg.raised` and should not carry unique state meaning.
- `sf.accent.cyan` is the primary action accent. It must not be reused as decorative glow across the whole surface.
- Warning and error fills remain restrained because the station should not visually punish the operator; active/current must remain the strongest signal.


## Boundary / 边界声明

- `status`: candidate；`authority`: not-authority；本文件不是 CSS token 合并、frontend implementation、package install、browser automation、runtime、vault true write、migration 或 authority writeback 批准。
- 可被 PF-V / GPT-Image-2 / future dispatch 作为视觉 atlas 输入；不可把本文内任何 token、SVG、layout 或 template 直接解释成 production contract。
- 所有主观 5-Gate 判断保持 human-in-loop；自动化只能提供截图、contrast、DOM 或 manifest evidence，不能替代最终视觉判断。
- 第三方库仅作为参考类别；本 atlas 内联 SVG 均按 ScoutFlow-original candidate 处理，未复制第三方 path。若未来改用第三方 icon/illustration，必须重新验证 license。


### TOKEN-01 Palette 15 Deep Blue + Derived Status Colors — audit expansion 1

### Review discipline / 审查纪律

1. 先判断 L1 information architecture：URL Bar → Live Metadata → Capture Scope → Trust Trace 的扫描顺序不可被模板、装饰图、sidebar 或 KPI 区域改写。
2. 再判断 L2 structure：panel、row、badge、detail shelf、graph node、template slot 必须共享 8dp rhythm 与同一套语义 token，不允许在局部硬编码新的蓝色、阴影或圆角。
3. 最后判断 L3 mood：深海蓝、低眩光、operator workstation、evidence-first、single-user dense surface；强视觉不是荧光科技感，也不是营销 hero 图。
4. 对任何 `blocked` / `future_gate` / `candidate` lane，必须有文字、badge、位置与视觉权重共同表达；颜色不能成为唯一信号。
5. 任何截图、render pass、contrast pass 都只能作为 evidence；若 Gate 1-5 任一失败，最终 verdict 必须是 `visual_not_passed`。

本节适用于 `TOKEN-01 Palette 15 Deep Blue + Derived Status Colors`：审查者应记录 source label、state word、token reference、layout slot、failure class、defer condition 与 human reviewer note。若证据缺失，写 `needs_evidence`，不得写 `passed by assumption`。


### TOKEN-01 Palette 15 Deep Blue + Derived Status Colors — audit expansion 2

### 5-Gate alignment / 五门对齐

| Gate | Local acceptance | Failure signal |
|---|---|---|
| Gate 1 hierarchy | 主动作或主证据 3 秒内可识别 | 装饰、图表、future lane 抢第一注意点 |
| Gate 2 spacing/alignment | 8dp grid、共同 baseline、稳定 panel padding | row、badge、图节点漂移，导致扫描断裂 |
| Gate 3 occlusion | tooltip/toast/legend 不遮 URL/current state/node label | overlay 遮住可操作或可审计信息 |
| Gate 4 typography/readability | 中英混排、URL、ID、timestamp 可读 | 小字、低对比、截断造成状态误判 |
| Gate 5 visual weight | active/current/proven 高于 blocked/candidate/future | danger 或 decorative glow 反向支配界面 |

本节适用于 `TOKEN-01 Palette 15 Deep Blue + Derived Status Colors`：审查者应记录 source label、state word、token reference、layout slot、failure class、defer condition 与 human reviewer note。若证据缺失，写 `needs_evidence`，不得写 `passed by assumption`。


### TOKEN-01 Palette 15 Deep Blue + Derived Status Colors — audit expansion 3

### Implementation seam / 实现缝合位

推荐未来实现路径为 CSS Variables + CSS Modules + container queries。`tokens.ts` 只可作为 typed mirror；Style Dictionary、Tokens Studio、Tailwind、Panda、shadcn、React Flow、Lucide、Radix、TanStack 或 React 版本升级都不得从本文件自动推出。若某个 dispatch 需要这些 package，应在独立 package gate 中提出，不在 visual atlas 中夹带批准。

本节适用于 `TOKEN-01 Palette 15 Deep Blue + Derived Status Colors`：审查者应记录 source label、state word、token reference、layout slot、failure class、defer condition 与 human reviewer note。若证据缺失，写 `needs_evidence`，不得写 `passed by assumption`。


### TOKEN-01 Palette 15 Deep Blue + Derived Status Colors — audit expansion 4

### Linked-state grammar / 状态语法

每个视觉对象至少绑定一个 state word：`idle`、`editing`、`requested`、`settling`、`ready`、`allowed`、`candidate`、`future_gate`、`blocked`、`stale`、`probe_failed`、`preview_only`。状态应同时体现在文案、badge、border/fill、position/order 与可访问名称中。`audio_transcript`、media processing、browser automation、migration、vault true write 仍必须以 blocked/future-gated 方式出现，不得藏进 tooltip。

本节适用于 `TOKEN-01 Palette 15 Deep Blue + Derived Status Colors`：审查者应记录 source label、state word、token reference、layout slot、failure class、defer condition 与 human reviewer note。若证据缺失，写 `needs_evidence`，不得写 `passed by assumption`。


### TOKEN-01 Palette 15 Deep Blue + Derived Status Colors — audit expansion 5

### Review discipline / 审查纪律

1. 先判断 L1 information architecture：URL Bar → Live Metadata → Capture Scope → Trust Trace 的扫描顺序不可被模板、装饰图、sidebar 或 KPI 区域改写。
2. 再判断 L2 structure：panel、row、badge、detail shelf、graph node、template slot 必须共享 8dp rhythm 与同一套语义 token，不允许在局部硬编码新的蓝色、阴影或圆角。
3. 最后判断 L3 mood：深海蓝、低眩光、operator workstation、evidence-first、single-user dense surface；强视觉不是荧光科技感，也不是营销 hero 图。
4. 对任何 `blocked` / `future_gate` / `candidate` lane，必须有文字、badge、位置与视觉权重共同表达；颜色不能成为唯一信号。
5. 任何截图、render pass、contrast pass 都只能作为 evidence；若 Gate 1-5 任一失败，最终 verdict 必须是 `visual_not_passed`。

本节适用于 `TOKEN-01 Palette 15 Deep Blue + Derived Status Colors`：审查者应记录 source label、state word、token reference、layout slot、failure class、defer condition 与 human reviewer note。若证据缺失，写 `needs_evidence`，不得写 `passed by assumption`。


### TOKEN-01 Palette 15 Deep Blue + Derived Status Colors — audit expansion 6

### 5-Gate alignment / 五门对齐

| Gate | Local acceptance | Failure signal |
|---|---|---|
| Gate 1 hierarchy | 主动作或主证据 3 秒内可识别 | 装饰、图表、future lane 抢第一注意点 |
| Gate 2 spacing/alignment | 8dp grid、共同 baseline、稳定 panel padding | row、badge、图节点漂移，导致扫描断裂 |
| Gate 3 occlusion | tooltip/toast/legend 不遮 URL/current state/node label | overlay 遮住可操作或可审计信息 |
| Gate 4 typography/readability | 中英混排、URL、ID、timestamp 可读 | 小字、低对比、截断造成状态误判 |
| Gate 5 visual weight | active/current/proven 高于 blocked/candidate/future | danger 或 decorative glow 反向支配界面 |

本节适用于 `TOKEN-01 Palette 15 Deep Blue + Derived Status Colors`：审查者应记录 source label、state word、token reference、layout slot、failure class、defer condition 与 human reviewer note。若证据缺失，写 `needs_evidence`，不得写 `passed by assumption`。


### TOKEN-01 Palette 15 Deep Blue + Derived Status Colors — audit expansion 7

### Implementation seam / 实现缝合位

推荐未来实现路径为 CSS Variables + CSS Modules + container queries。`tokens.ts` 只可作为 typed mirror；Style Dictionary、Tokens Studio、Tailwind、Panda、shadcn、React Flow、Lucide、Radix、TanStack 或 React 版本升级都不得从本文件自动推出。若某个 dispatch 需要这些 package，应在独立 package gate 中提出，不在 visual atlas 中夹带批准。

本节适用于 `TOKEN-01 Palette 15 Deep Blue + Derived Status Colors`：审查者应记录 source label、state word、token reference、layout slot、failure class、defer condition 与 human reviewer note。若证据缺失，写 `needs_evidence`，不得写 `passed by assumption`。


### TOKEN-01 Palette 15 Deep Blue + Derived Status Colors — audit expansion 8

### Linked-state grammar / 状态语法

每个视觉对象至少绑定一个 state word：`idle`、`editing`、`requested`、`settling`、`ready`、`allowed`、`candidate`、`future_gate`、`blocked`、`stale`、`probe_failed`、`preview_only`。状态应同时体现在文案、badge、border/fill、position/order 与可访问名称中。`audio_transcript`、media processing、browser automation、migration、vault true write 仍必须以 blocked/future-gated 方式出现，不得藏进 tooltip。

本节适用于 `TOKEN-01 Palette 15 Deep Blue + Derived Status Colors`：审查者应记录 source label、state word、token reference、layout slot、failure class、defer condition 与 human reviewer note。若证据缺失，写 `needs_evidence`，不得写 `passed by assumption`。
