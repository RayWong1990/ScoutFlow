---
title: "I20 Icon Spec — amend / handoff"
status: "candidate / not-authority"
authority: not-authority
created_at: 2026-05-07
atlas_id: U13-visual-style-brand-atlas-v0
file_kind: icon
claim_labels:
  - canonical fact from local packet
  - promoted_addendum-aware inference
  - tentative candidate
  - needs_live_web_refresh
boundary: "docs-only; no runtime/package/frontend/browser/vault/migration approval"
---

# I20 Icon Spec — amend / handoff

## Scope

This file contributes two renderable 24×24 SVG icon candidates. Paths are ScoutFlow-original geometric drafts; no third-party SVG path is copied. Use them as semantic asset specs, not as approved production SVG exports.


## Icon entry `amend`

| Field | Value |
|---|---|
| icon_id | `amend` |
| semantic_intent | Amend note |
| preferred_surface | Operations |
| linked_state | `candidate` |
| linked_visual_asset | `U4:amend` / pending external U4 refresh |
| license | ScoutFlow-original candidate path; third-party license not invoked |
| viewBox | `0 0 24 24` |

```svg
<svg viewBox="0 0 24 24" role="img" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M12 4L20 8V16L12 20L4 16V8Z M12 8V16 M7 10L12 13L17 10"/></svg>
```

### Usage

- Use stroke-only at 1.5–1.8px on dark panels; inherit `currentColor` from semantic token, usually `sf.text.secondary`, `sf.accent.cyan`, `sf.success`, `sf.warning` or `sf.error`.
- Pair icon with visible text. For state-bearing icons, screen reader label must include the state word, for example `amend: candidate`.
- Do not use this icon as a decorative watermark behind evidence rows; it belongs inside row headers, badges, compact buttons or template annotations.

### State variants

| State | Color token | Text requirement | 5-Gate note |
|---|---|---|---|
| idle | `sf.text.secondary` | neutral label | may be subdued |
| ready/allowed | `sf.success` or `sf.accent.cyan` | explicit ready/allowed | must not imply runtime unlock |
| candidate/future_gate | `sf.warning` | candidate/future text | never green |
| blocked | `sf.error` with low-saturation bg | blocked reason | visible but lower than current action |

### Good vs bad

Good: icon + short label + badge in a row that preserves alignment. Bad: icon-only state, neon glow, hidden blocked reason, or third-party library path copied without license proof.


## Icon entry `handoff`

| Field | Value |
|---|---|
| icon_id | `handoff` |
| semantic_intent | Cold-start handoff |
| preferred_surface | Operations |
| linked_state | `ready` |
| linked_visual_asset | `U4:handoff` / pending external U4 refresh |
| license | ScoutFlow-original candidate path; third-party license not invoked |
| viewBox | `0 0 24 24` |

```svg
<svg viewBox="0 0 24 24" role="img" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12L10 17L20 7 M4 20H20"/></svg>
```

### Usage

- Use stroke-only at 1.5–1.8px on dark panels; inherit `currentColor` from semantic token, usually `sf.text.secondary`, `sf.accent.cyan`, `sf.success`, `sf.warning` or `sf.error`.
- Pair icon with visible text. For state-bearing icons, screen reader label must include the state word, for example `handoff: ready`.
- Do not use this icon as a decorative watermark behind evidence rows; it belongs inside row headers, badges, compact buttons or template annotations.

### State variants

| State | Color token | Text requirement | 5-Gate note |
|---|---|---|---|
| idle | `sf.text.secondary` | neutral label | may be subdued |
| ready/allowed | `sf.success` or `sf.accent.cyan` | explicit ready/allowed | must not imply runtime unlock |
| candidate/future_gate | `sf.warning` | candidate/future text | never green |
| blocked | `sf.error` with low-saturation bg | blocked reason | visible but lower than current action |

### Good vs bad

Good: icon + short label + badge in a row that preserves alignment. Bad: icon-only state, neon glow, hidden blocked reason, or third-party library path copied without license proof.


## Boundary / 边界声明

- `status`: candidate；`authority`: not-authority；本文件不是 CSS token 合并、frontend implementation、package install、browser automation、runtime、vault true write、migration 或 authority writeback 批准。
- 可被 PF-V / GPT-Image-2 / future dispatch 作为视觉 atlas 输入；不可把本文内任何 token、SVG、layout 或 template 直接解释成 production contract。
- 所有主观 5-Gate 判断保持 human-in-loop；自动化只能提供截图、contrast、DOM 或 manifest evidence，不能替代最终视觉判断。
- 第三方库仅作为参考类别；本 atlas 内联 SVG 均按 ScoutFlow-original candidate 处理，未复制第三方 path。若未来改用第三方 icon/illustration，必须重新验证 license。


### I20 Icon Spec — amend / handoff — audit expansion 1

### Review discipline / 审查纪律

1. 先判断 L1 information architecture：URL Bar → Live Metadata → Capture Scope → Trust Trace 的扫描顺序不可被模板、装饰图、sidebar 或 KPI 区域改写。
2. 再判断 L2 structure：panel、row、badge、detail shelf、graph node、template slot 必须共享 8dp rhythm 与同一套语义 token，不允许在局部硬编码新的蓝色、阴影或圆角。
3. 最后判断 L3 mood：深海蓝、低眩光、operator workstation、evidence-first、single-user dense surface；强视觉不是荧光科技感，也不是营销 hero 图。
4. 对任何 `blocked` / `future_gate` / `candidate` lane，必须有文字、badge、位置与视觉权重共同表达；颜色不能成为唯一信号。
5. 任何截图、render pass、contrast pass 都只能作为 evidence；若 Gate 1-5 任一失败，最终 verdict 必须是 `visual_not_passed`。

本节适用于 `I20 Icon Spec — amend / handoff`：审查者应记录 source label、state word、token reference、layout slot、failure class、defer condition 与 human reviewer note。若证据缺失，写 `needs_evidence`，不得写 `passed by assumption`。


### I20 Icon Spec — amend / handoff — audit expansion 2

### 5-Gate alignment / 五门对齐

| Gate | Local acceptance | Failure signal |
|---|---|---|
| Gate 1 hierarchy | 主动作或主证据 3 秒内可识别 | 装饰、图表、future lane 抢第一注意点 |
| Gate 2 spacing/alignment | 8dp grid、共同 baseline、稳定 panel padding | row、badge、图节点漂移，导致扫描断裂 |
| Gate 3 occlusion | tooltip/toast/legend 不遮 URL/current state/node label | overlay 遮住可操作或可审计信息 |
| Gate 4 typography/readability | 中英混排、URL、ID、timestamp 可读 | 小字、低对比、截断造成状态误判 |
| Gate 5 visual weight | active/current/proven 高于 blocked/candidate/future | danger 或 decorative glow 反向支配界面 |

本节适用于 `I20 Icon Spec — amend / handoff`：审查者应记录 source label、state word、token reference、layout slot、failure class、defer condition 与 human reviewer note。若证据缺失，写 `needs_evidence`，不得写 `passed by assumption`。


### I20 Icon Spec — amend / handoff — audit expansion 3

### Implementation seam / 实现缝合位

推荐未来实现路径为 CSS Variables + CSS Modules + container queries。`tokens.ts` 只可作为 typed mirror；Style Dictionary、Tokens Studio、Tailwind、Panda、shadcn、React Flow、Lucide、Radix、TanStack 或 React 版本升级都不得从本文件自动推出。若某个 dispatch 需要这些 package，应在独立 package gate 中提出，不在 visual atlas 中夹带批准。

本节适用于 `I20 Icon Spec — amend / handoff`：审查者应记录 source label、state word、token reference、layout slot、failure class、defer condition 与 human reviewer note。若证据缺失，写 `needs_evidence`，不得写 `passed by assumption`。


### I20 Icon Spec — amend / handoff — audit expansion 4

### Linked-state grammar / 状态语法

每个视觉对象至少绑定一个 state word：`idle`、`editing`、`requested`、`settling`、`ready`、`allowed`、`candidate`、`future_gate`、`blocked`、`stale`、`probe_failed`、`preview_only`。状态应同时体现在文案、badge、border/fill、position/order 与可访问名称中。`audio_transcript`、media processing、browser automation、migration、vault true write 仍必须以 blocked/future-gated 方式出现，不得藏进 tooltip。

本节适用于 `I20 Icon Spec — amend / handoff`：审查者应记录 source label、state word、token reference、layout slot、failure class、defer condition 与 human reviewer note。若证据缺失，写 `needs_evidence`，不得写 `passed by assumption`。
