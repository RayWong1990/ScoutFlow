---
title: "PAT08 Pattern Spec — badge-dash / poster-radar"
status: "candidate / not-authority"
authority: not-authority
created_at: 2026-05-07
atlas_id: U13-visual-style-brand-atlas-v0
file_kind: pattern
claim_labels:
  - canonical fact from local packet
  - promoted_addendum-aware inference
  - tentative candidate
  - needs_live_web_refresh
boundary: "docs-only; no runtime/package/frontend/browser/vault/migration approval"
---

# PAT08 Pattern Spec — badge-dash / poster-radar

## Scope

Patterns are supporting visual primitives. They must stay below evidence and state text. They are never a substitute for panel borders, badges, graph edges or real audit data.


## Pattern `badge-dash`

| Field | Value |
|---|---|
| pattern_id | `badge-dash` |
| intent | badge dash pattern |
| recommended_use | candidate/future labels |
| token_refs | `sf.canvas.0`, `sf.border.panel`, `sf.accent.cyan` with opacity <= .45 |
| license | ScoutFlow-original candidate geometry |
| asset_type | inline SVG pattern concept |

```svg
<svg viewBox="0 0 160 96" role="img" aria-hidden="true" xmlns="http://www.w3.org/2000/svg">
  <path d="M0 0H160V96H0Z" fill="#07111B"/>
  <path d="M0 16H160 M0 32H160 M0 48H160 M0 64H160 M16 0V96 M32 0V96 M48 0V96 M64 0V96 M80 0V96" stroke="#27415D" stroke-opacity=".45"/>
  <path d="M16 72C40 40 64 40 88 72C112 104 136 104 152 72" stroke="#50D4FF" stroke-opacity=".35" stroke-width="2" fill="none"/>
</svg>
```

### Usage constraints

- Keep opacity restrained. Pattern contrast should never compete with body text or graph edge semantics.
- On app surfaces, patterns belong to canvas or empty-state zones only, not behind URL input, current state, or node labels.
- In PPT/poster/social, pattern may carry brand mood, but evidence copy and state labels still define meaning.
- Reuse the same pattern family across phases to prevent PF-V asset drift.

### Failure cases

- Pattern becomes a fake graph or implies dependencies that do not exist.
- Pattern causes moiré or low contrast in screenshots.
- Pattern is used as a decorative glow around blocked lanes.
- Pattern is exported as a standalone production SVG without license/accessibility review.


## Pattern `poster-radar`

| Field | Value |
|---|---|
| pattern_id | `poster-radar` |
| intent | large poster radar rings |
| recommended_use | poster only |
| token_refs | `sf.canvas.0`, `sf.border.panel`, `sf.accent.cyan` with opacity <= .45 |
| license | ScoutFlow-original candidate geometry |
| asset_type | inline SVG pattern concept |

```svg
<svg viewBox="0 0 160 96" role="img" aria-hidden="true" xmlns="http://www.w3.org/2000/svg">
  <path d="M0 0H160V96H0Z" fill="#07111B"/>
  <path d="M0 20H160 M0 40H160 M0 60H160 M0 80H160 M20 0V96 M40 0V96 M60 0V96 M80 0V96 M100 0V96" stroke="#27415D" stroke-opacity=".45"/>
  <path d="M16 72C40 40 64 40 88 72C112 104 136 104 152 72" stroke="#50D4FF" stroke-opacity=".35" stroke-width="2" fill="none"/>
</svg>
```

### Usage constraints

- Keep opacity restrained. Pattern contrast should never compete with body text or graph edge semantics.
- On app surfaces, patterns belong to canvas or empty-state zones only, not behind URL input, current state, or node labels.
- In PPT/poster/social, pattern may carry brand mood, but evidence copy and state labels still define meaning.
- Reuse the same pattern family across phases to prevent PF-V asset drift.

### Failure cases

- Pattern becomes a fake graph or implies dependencies that do not exist.
- Pattern causes moiré or low contrast in screenshots.
- Pattern is used as a decorative glow around blocked lanes.
- Pattern is exported as a standalone production SVG without license/accessibility review.


## Boundary / 边界声明

- `status`: candidate；`authority`: not-authority；本文件不是 CSS token 合并、frontend implementation、package install、browser automation、runtime、vault true write、migration 或 authority writeback 批准。
- 可被 PF-V / GPT-Image-2 / future dispatch 作为视觉 atlas 输入；不可把本文内任何 token、SVG、layout 或 template 直接解释成 production contract。
- 所有主观 5-Gate 判断保持 human-in-loop；自动化只能提供截图、contrast、DOM 或 manifest evidence，不能替代最终视觉判断。
- 第三方库仅作为参考类别；本 atlas 内联 SVG 均按 ScoutFlow-original candidate 处理，未复制第三方 path。若未来改用第三方 icon/illustration，必须重新验证 license。


### PAT08 Pattern Spec — badge-dash / poster-radar — audit expansion 1

### 5-Gate alignment / 五门对齐

| Gate | Local acceptance | Failure signal |
|---|---|---|
| Gate 1 hierarchy | 主动作或主证据 3 秒内可识别 | 装饰、图表、future lane 抢第一注意点 |
| Gate 2 spacing/alignment | 8dp grid、共同 baseline、稳定 panel padding | row、badge、图节点漂移，导致扫描断裂 |
| Gate 3 occlusion | tooltip/toast/legend 不遮 URL/current state/node label | overlay 遮住可操作或可审计信息 |
| Gate 4 typography/readability | 中英混排、URL、ID、timestamp 可读 | 小字、低对比、截断造成状态误判 |
| Gate 5 visual weight | active/current/proven 高于 blocked/candidate/future | danger 或 decorative glow 反向支配界面 |

本节适用于 `PAT08 Pattern Spec — badge-dash / poster-radar`：审查者应记录 source label、state word、token reference、layout slot、failure class、defer condition 与 human reviewer note。若证据缺失，写 `needs_evidence`，不得写 `passed by assumption`。


### PAT08 Pattern Spec — badge-dash / poster-radar — audit expansion 2

### Implementation seam / 实现缝合位

推荐未来实现路径为 CSS Variables + CSS Modules + container queries。`tokens.ts` 只可作为 typed mirror；Style Dictionary、Tokens Studio、Tailwind、Panda、shadcn、React Flow、Lucide、Radix、TanStack 或 React 版本升级都不得从本文件自动推出。若某个 dispatch 需要这些 package，应在独立 package gate 中提出，不在 visual atlas 中夹带批准。

本节适用于 `PAT08 Pattern Spec — badge-dash / poster-radar`：审查者应记录 source label、state word、token reference、layout slot、failure class、defer condition 与 human reviewer note。若证据缺失，写 `needs_evidence`，不得写 `passed by assumption`。


### PAT08 Pattern Spec — badge-dash / poster-radar — audit expansion 3

### Linked-state grammar / 状态语法

每个视觉对象至少绑定一个 state word：`idle`、`editing`、`requested`、`settling`、`ready`、`allowed`、`candidate`、`future_gate`、`blocked`、`stale`、`probe_failed`、`preview_only`。状态应同时体现在文案、badge、border/fill、position/order 与可访问名称中。`audio_transcript`、media processing、browser automation、migration、vault true write 仍必须以 blocked/future-gated 方式出现，不得藏进 tooltip。

本节适用于 `PAT08 Pattern Spec — badge-dash / poster-radar`：审查者应记录 source label、state word、token reference、layout slot、failure class、defer condition 与 human reviewer note。若证据缺失，写 `needs_evidence`，不得写 `passed by assumption`。


### PAT08 Pattern Spec — badge-dash / poster-radar — audit expansion 4

### Review discipline / 审查纪律

1. 先判断 L1 information architecture：URL Bar → Live Metadata → Capture Scope → Trust Trace 的扫描顺序不可被模板、装饰图、sidebar 或 KPI 区域改写。
2. 再判断 L2 structure：panel、row、badge、detail shelf、graph node、template slot 必须共享 8dp rhythm 与同一套语义 token，不允许在局部硬编码新的蓝色、阴影或圆角。
3. 最后判断 L3 mood：深海蓝、低眩光、operator workstation、evidence-first、single-user dense surface；强视觉不是荧光科技感，也不是营销 hero 图。
4. 对任何 `blocked` / `future_gate` / `candidate` lane，必须有文字、badge、位置与视觉权重共同表达；颜色不能成为唯一信号。
5. 任何截图、render pass、contrast pass 都只能作为 evidence；若 Gate 1-5 任一失败，最终 verdict 必须是 `visual_not_passed`。

本节适用于 `PAT08 Pattern Spec — badge-dash / poster-radar`：审查者应记录 source label、state word、token reference、layout slot、failure class、defer condition 与 human reviewer note。若证据缺失，写 `needs_evidence`，不得写 `passed by assumption`。


### PAT08 Pattern Spec — badge-dash / poster-radar — audit expansion 5

### 5-Gate alignment / 五门对齐

| Gate | Local acceptance | Failure signal |
|---|---|---|
| Gate 1 hierarchy | 主动作或主证据 3 秒内可识别 | 装饰、图表、future lane 抢第一注意点 |
| Gate 2 spacing/alignment | 8dp grid、共同 baseline、稳定 panel padding | row、badge、图节点漂移，导致扫描断裂 |
| Gate 3 occlusion | tooltip/toast/legend 不遮 URL/current state/node label | overlay 遮住可操作或可审计信息 |
| Gate 4 typography/readability | 中英混排、URL、ID、timestamp 可读 | 小字、低对比、截断造成状态误判 |
| Gate 5 visual weight | active/current/proven 高于 blocked/candidate/future | danger 或 decorative glow 反向支配界面 |

本节适用于 `PAT08 Pattern Spec — badge-dash / poster-radar`：审查者应记录 source label、state word、token reference、layout slot、failure class、defer condition 与 human reviewer note。若证据缺失，写 `needs_evidence`，不得写 `passed by assumption`。


### PAT08 Pattern Spec — badge-dash / poster-radar — audit expansion 6

### Implementation seam / 实现缝合位

推荐未来实现路径为 CSS Variables + CSS Modules + container queries。`tokens.ts` 只可作为 typed mirror；Style Dictionary、Tokens Studio、Tailwind、Panda、shadcn、React Flow、Lucide、Radix、TanStack 或 React 版本升级都不得从本文件自动推出。若某个 dispatch 需要这些 package，应在独立 package gate 中提出，不在 visual atlas 中夹带批准。

本节适用于 `PAT08 Pattern Spec — badge-dash / poster-radar`：审查者应记录 source label、state word、token reference、layout slot、failure class、defer condition 与 human reviewer note。若证据缺失，写 `needs_evidence`，不得写 `passed by assumption`。
