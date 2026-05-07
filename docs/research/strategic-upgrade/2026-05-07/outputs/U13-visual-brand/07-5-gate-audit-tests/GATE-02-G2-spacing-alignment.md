---
title: GATE-02 Spacing & Alignment Test Cases
status: "candidate / not-authority"
authority: not-authority
created_at: 2026-05-07
atlas_id: U13-visual-style-brand-atlas-v0
file_kind: five_gate
claim_labels:
  - canonical fact from local packet
  - promoted_addendum-aware inference
  - tentative candidate
  - needs_live_web_refresh
boundary: "docs-only; no runtime/package/frontend/browser/vault/migration approval"
---

# GATE-02 Spacing & Alignment Test Cases

## Gate mission

8dp grid, shared baseline, stable density. This file contains six good-vs-bad audit cases for the gate. Cases are deliberately reusable across app panels, PPT/poster/social templates and PF-V generated images.

| Case | Scenario | Good | Bad | Disposition |
|---|---|---|---|---|
| `G2-spacing-alignment-case-01` | Spacing & Alignment scenario 1 | good keeps 8dp grid, shared baseline, stable density | bad violates gate through drift/overclaim | stop/repair if critical |
| `G2-spacing-alignment-case-02` | Spacing & Alignment scenario 2 | good keeps 8dp grid, shared baseline, stable density | bad violates gate through drift/overclaim | stop/repair if critical |
| `G2-spacing-alignment-case-03` | Spacing & Alignment scenario 3 | good keeps 8dp grid, shared baseline, stable density | bad violates gate through drift/overclaim | stop/repair if critical |
| `G2-spacing-alignment-case-04` | Spacing & Alignment scenario 4 | good keeps 8dp grid, shared baseline, stable density | bad violates gate through drift/overclaim | stop/repair if critical |
| `G2-spacing-alignment-case-05` | Spacing & Alignment scenario 5 | good keeps 8dp grid, shared baseline, stable density | bad violates gate through drift/overclaim | stop/repair if critical |
| `G2-spacing-alignment-case-06` | Spacing & Alignment scenario 6 | good keeps 8dp grid, shared baseline, stable density | bad violates gate through drift/overclaim | stop/repair if critical |


### case_id: `G2-spacing-alignment-case-01`

**Good**: The screen/template keeps `8dp grid, shared baseline, stable density`. State copy is visible, token references are consistent, and the reviewer can explain why the object passes without relying on subjective taste.

**Bad**: The same surface fails because a decoration, misalignment, overlay, typography collapse or future-lane overemphasis changes user interpretation. This is not polish if the operator could misread state.

**Expected verdict**: `pass` for the good example; `major_visual_defect` or `design_gate_failure` for the bad example. Record screenshot path if available, otherwise `visual_evidence_deferred`.


### case_id: `G2-spacing-alignment-case-02`

**Good**: The screen/template keeps `8dp grid, shared baseline, stable density`. State copy is visible, token references are consistent, and the reviewer can explain why the object passes without relying on subjective taste.

**Bad**: The same surface fails because a decoration, misalignment, overlay, typography collapse or future-lane overemphasis changes user interpretation. This is not polish if the operator could misread state.

**Expected verdict**: `pass` for the good example; `major_visual_defect` or `design_gate_failure` for the bad example. Record screenshot path if available, otherwise `visual_evidence_deferred`.


### case_id: `G2-spacing-alignment-case-03`

**Good**: The screen/template keeps `8dp grid, shared baseline, stable density`. State copy is visible, token references are consistent, and the reviewer can explain why the object passes without relying on subjective taste.

**Bad**: The same surface fails because a decoration, misalignment, overlay, typography collapse or future-lane overemphasis changes user interpretation. This is not polish if the operator could misread state.

**Expected verdict**: `pass` for the good example; `major_visual_defect` or `design_gate_failure` for the bad example. Record screenshot path if available, otherwise `visual_evidence_deferred`.


### case_id: `G2-spacing-alignment-case-04`

**Good**: The screen/template keeps `8dp grid, shared baseline, stable density`. State copy is visible, token references are consistent, and the reviewer can explain why the object passes without relying on subjective taste.

**Bad**: The same surface fails because a decoration, misalignment, overlay, typography collapse or future-lane overemphasis changes user interpretation. This is not polish if the operator could misread state.

**Expected verdict**: `pass` for the good example; `major_visual_defect` or `design_gate_failure` for the bad example. Record screenshot path if available, otherwise `visual_evidence_deferred`.


### case_id: `G2-spacing-alignment-case-05`

**Good**: The screen/template keeps `8dp grid, shared baseline, stable density`. State copy is visible, token references are consistent, and the reviewer can explain why the object passes without relying on subjective taste.

**Bad**: The same surface fails because a decoration, misalignment, overlay, typography collapse or future-lane overemphasis changes user interpretation. This is not polish if the operator could misread state.

**Expected verdict**: `pass` for the good example; `major_visual_defect` or `design_gate_failure` for the bad example. Record screenshot path if available, otherwise `visual_evidence_deferred`.


### case_id: `G2-spacing-alignment-case-06`

**Good**: The screen/template keeps `8dp grid, shared baseline, stable density`. State copy is visible, token references are consistent, and the reviewer can explain why the object passes without relying on subjective taste.

**Bad**: The same surface fails because a decoration, misalignment, overlay, typography collapse or future-lane overemphasis changes user interpretation. This is not polish if the operator could misread state.

**Expected verdict**: `pass` for the good example; `major_visual_defect` or `design_gate_failure` for the bad example. Record screenshot path if available, otherwise `visual_evidence_deferred`.


## Reviewer protocol

1. Label the surface: panel, template, illustration, icon or pattern.
2. Identify state words and claim labels.
3. Check good-vs-bad against screenshots or rendered artifacts.
4. Write `pass`, `minor_polish`, `major_visual_defect`, `design_gate_failure`, `boundary_failure` or `authority_failure`.
5. Never convert technical render pass into visual pass.


## Boundary / 边界声明

- `status`: candidate；`authority`: not-authority；本文件不是 CSS token 合并、frontend implementation、package install、browser automation、runtime、vault true write、migration 或 authority writeback 批准。
- 可被 PF-V / GPT-Image-2 / future dispatch 作为视觉 atlas 输入；不可把本文内任何 token、SVG、layout 或 template 直接解释成 production contract。
- 所有主观 5-Gate 判断保持 human-in-loop；自动化只能提供截图、contrast、DOM 或 manifest evidence，不能替代最终视觉判断。
- 第三方库仅作为参考类别；本 atlas 内联 SVG 均按 ScoutFlow-original candidate 处理，未复制第三方 path。若未来改用第三方 icon/illustration，必须重新验证 license。


### GATE-02 Spacing & Alignment Test Cases — audit expansion 1

### Linked-state grammar / 状态语法

每个视觉对象至少绑定一个 state word：`idle`、`editing`、`requested`、`settling`、`ready`、`allowed`、`candidate`、`future_gate`、`blocked`、`stale`、`probe_failed`、`preview_only`。状态应同时体现在文案、badge、border/fill、position/order 与可访问名称中。`audio_transcript`、media processing、browser automation、migration、vault true write 仍必须以 blocked/future-gated 方式出现，不得藏进 tooltip。

本节适用于 `GATE-02 Spacing & Alignment Test Cases`：审查者应记录 source label、state word、token reference、layout slot、failure class、defer condition 与 human reviewer note。若证据缺失，写 `needs_evidence`，不得写 `passed by assumption`。


### GATE-02 Spacing & Alignment Test Cases — audit expansion 2

### Review discipline / 审查纪律

1. 先判断 L1 information architecture：URL Bar → Live Metadata → Capture Scope → Trust Trace 的扫描顺序不可被模板、装饰图、sidebar 或 KPI 区域改写。
2. 再判断 L2 structure：panel、row、badge、detail shelf、graph node、template slot 必须共享 8dp rhythm 与同一套语义 token，不允许在局部硬编码新的蓝色、阴影或圆角。
3. 最后判断 L3 mood：深海蓝、低眩光、operator workstation、evidence-first、single-user dense surface；强视觉不是荧光科技感，也不是营销 hero 图。
4. 对任何 `blocked` / `future_gate` / `candidate` lane，必须有文字、badge、位置与视觉权重共同表达；颜色不能成为唯一信号。
5. 任何截图、render pass、contrast pass 都只能作为 evidence；若 Gate 1-5 任一失败，最终 verdict 必须是 `visual_not_passed`。

本节适用于 `GATE-02 Spacing & Alignment Test Cases`：审查者应记录 source label、state word、token reference、layout slot、failure class、defer condition 与 human reviewer note。若证据缺失，写 `needs_evidence`，不得写 `passed by assumption`。


### GATE-02 Spacing & Alignment Test Cases — audit expansion 3

### 5-Gate alignment / 五门对齐

| Gate | Local acceptance | Failure signal |
|---|---|---|
| Gate 1 hierarchy | 主动作或主证据 3 秒内可识别 | 装饰、图表、future lane 抢第一注意点 |
| Gate 2 spacing/alignment | 8dp grid、共同 baseline、稳定 panel padding | row、badge、图节点漂移，导致扫描断裂 |
| Gate 3 occlusion | tooltip/toast/legend 不遮 URL/current state/node label | overlay 遮住可操作或可审计信息 |
| Gate 4 typography/readability | 中英混排、URL、ID、timestamp 可读 | 小字、低对比、截断造成状态误判 |
| Gate 5 visual weight | active/current/proven 高于 blocked/candidate/future | danger 或 decorative glow 反向支配界面 |

本节适用于 `GATE-02 Spacing & Alignment Test Cases`：审查者应记录 source label、state word、token reference、layout slot、failure class、defer condition 与 human reviewer note。若证据缺失，写 `needs_evidence`，不得写 `passed by assumption`。


### GATE-02 Spacing & Alignment Test Cases — audit expansion 4

### Implementation seam / 实现缝合位

推荐未来实现路径为 CSS Variables + CSS Modules + container queries。`tokens.ts` 只可作为 typed mirror；Style Dictionary、Tokens Studio、Tailwind、Panda、shadcn、React Flow、Lucide、Radix、TanStack 或 React 版本升级都不得从本文件自动推出。若某个 dispatch 需要这些 package，应在独立 package gate 中提出，不在 visual atlas 中夹带批准。

本节适用于 `GATE-02 Spacing & Alignment Test Cases`：审查者应记录 source label、state word、token reference、layout slot、failure class、defer condition 与 human reviewer note。若证据缺失，写 `needs_evidence`，不得写 `passed by assumption`。


### GATE-02 Spacing & Alignment Test Cases — audit expansion 5

### Linked-state grammar / 状态语法

每个视觉对象至少绑定一个 state word：`idle`、`editing`、`requested`、`settling`、`ready`、`allowed`、`candidate`、`future_gate`、`blocked`、`stale`、`probe_failed`、`preview_only`。状态应同时体现在文案、badge、border/fill、position/order 与可访问名称中。`audio_transcript`、media processing、browser automation、migration、vault true write 仍必须以 blocked/future-gated 方式出现，不得藏进 tooltip。

本节适用于 `GATE-02 Spacing & Alignment Test Cases`：审查者应记录 source label、state word、token reference、layout slot、failure class、defer condition 与 human reviewer note。若证据缺失，写 `needs_evidence`，不得写 `passed by assumption`。


### GATE-02 Spacing & Alignment Test Cases — audit expansion 6

### Review discipline / 审查纪律

1. 先判断 L1 information architecture：URL Bar → Live Metadata → Capture Scope → Trust Trace 的扫描顺序不可被模板、装饰图、sidebar 或 KPI 区域改写。
2. 再判断 L2 structure：panel、row、badge、detail shelf、graph node、template slot 必须共享 8dp rhythm 与同一套语义 token，不允许在局部硬编码新的蓝色、阴影或圆角。
3. 最后判断 L3 mood：深海蓝、低眩光、operator workstation、evidence-first、single-user dense surface；强视觉不是荧光科技感，也不是营销 hero 图。
4. 对任何 `blocked` / `future_gate` / `candidate` lane，必须有文字、badge、位置与视觉权重共同表达；颜色不能成为唯一信号。
5. 任何截图、render pass、contrast pass 都只能作为 evidence；若 Gate 1-5 任一失败，最终 verdict 必须是 `visual_not_passed`。

本节适用于 `GATE-02 Spacing & Alignment Test Cases`：审查者应记录 source label、state word、token reference、layout slot、failure class、defer condition 与 human reviewer note。若证据缺失，写 `needs_evidence`，不得写 `passed by assumption`。


### GATE-02 Spacing & Alignment Test Cases — audit expansion 7

### 5-Gate alignment / 五门对齐

| Gate | Local acceptance | Failure signal |
|---|---|---|
| Gate 1 hierarchy | 主动作或主证据 3 秒内可识别 | 装饰、图表、future lane 抢第一注意点 |
| Gate 2 spacing/alignment | 8dp grid、共同 baseline、稳定 panel padding | row、badge、图节点漂移，导致扫描断裂 |
| Gate 3 occlusion | tooltip/toast/legend 不遮 URL/current state/node label | overlay 遮住可操作或可审计信息 |
| Gate 4 typography/readability | 中英混排、URL、ID、timestamp 可读 | 小字、低对比、截断造成状态误判 |
| Gate 5 visual weight | active/current/proven 高于 blocked/candidate/future | danger 或 decorative glow 反向支配界面 |

本节适用于 `GATE-02 Spacing & Alignment Test Cases`：审查者应记录 source label、state word、token reference、layout slot、failure class、defer condition 与 human reviewer note。若证据缺失，写 `needs_evidence`，不得写 `passed by assumption`。


### GATE-02 Spacing & Alignment Test Cases — audit expansion 8

### Implementation seam / 实现缝合位

推荐未来实现路径为 CSS Variables + CSS Modules + container queries。`tokens.ts` 只可作为 typed mirror；Style Dictionary、Tokens Studio、Tailwind、Panda、shadcn、React Flow、Lucide、Radix、TanStack 或 React 版本升级都不得从本文件自动推出。若某个 dispatch 需要这些 package，应在独立 package gate 中提出，不在 visual atlas 中夹带批准。

本节适用于 `GATE-02 Spacing & Alignment Test Cases`：审查者应记录 source label、state word、token reference、layout slot、failure class、defer condition 与 human reviewer note。若证据缺失，写 `needs_evidence`，不得写 `passed by assumption`。


### GATE-02 Spacing & Alignment Test Cases — audit expansion 9

### Linked-state grammar / 状态语法

每个视觉对象至少绑定一个 state word：`idle`、`editing`、`requested`、`settling`、`ready`、`allowed`、`candidate`、`future_gate`、`blocked`、`stale`、`probe_failed`、`preview_only`。状态应同时体现在文案、badge、border/fill、position/order 与可访问名称中。`audio_transcript`、media processing、browser automation、migration、vault true write 仍必须以 blocked/future-gated 方式出现，不得藏进 tooltip。

本节适用于 `GATE-02 Spacing & Alignment Test Cases`：审查者应记录 source label、state word、token reference、layout slot、failure class、defer condition 与 human reviewer note。若证据缺失，写 `needs_evidence`，不得写 `passed by assumption`。


### GATE-02 Spacing & Alignment Test Cases — audit expansion 10

### Review discipline / 审查纪律

1. 先判断 L1 information architecture：URL Bar → Live Metadata → Capture Scope → Trust Trace 的扫描顺序不可被模板、装饰图、sidebar 或 KPI 区域改写。
2. 再判断 L2 structure：panel、row、badge、detail shelf、graph node、template slot 必须共享 8dp rhythm 与同一套语义 token，不允许在局部硬编码新的蓝色、阴影或圆角。
3. 最后判断 L3 mood：深海蓝、低眩光、operator workstation、evidence-first、single-user dense surface；强视觉不是荧光科技感，也不是营销 hero 图。
4. 对任何 `blocked` / `future_gate` / `candidate` lane，必须有文字、badge、位置与视觉权重共同表达；颜色不能成为唯一信号。
5. 任何截图、render pass、contrast pass 都只能作为 evidence；若 Gate 1-5 任一失败，最终 verdict 必须是 `visual_not_passed`。

本节适用于 `GATE-02 Spacing & Alignment Test Cases`：审查者应记录 source label、state word、token reference、layout slot、failure class、defer condition 与 human reviewer note。若证据缺失，写 `needs_evidence`，不得写 `passed by assumption`。


### GATE-02 Spacing & Alignment Test Cases — audit expansion 11

### 5-Gate alignment / 五门对齐

| Gate | Local acceptance | Failure signal |
|---|---|---|
| Gate 1 hierarchy | 主动作或主证据 3 秒内可识别 | 装饰、图表、future lane 抢第一注意点 |
| Gate 2 spacing/alignment | 8dp grid、共同 baseline、稳定 panel padding | row、badge、图节点漂移，导致扫描断裂 |
| Gate 3 occlusion | tooltip/toast/legend 不遮 URL/current state/node label | overlay 遮住可操作或可审计信息 |
| Gate 4 typography/readability | 中英混排、URL、ID、timestamp 可读 | 小字、低对比、截断造成状态误判 |
| Gate 5 visual weight | active/current/proven 高于 blocked/candidate/future | danger 或 decorative glow 反向支配界面 |

本节适用于 `GATE-02 Spacing & Alignment Test Cases`：审查者应记录 source label、state word、token reference、layout slot、failure class、defer condition 与 human reviewer note。若证据缺失，写 `needs_evidence`，不得写 `passed by assumption`。


### GATE-02 Spacing & Alignment Test Cases — audit expansion 12

### Implementation seam / 实现缝合位

推荐未来实现路径为 CSS Variables + CSS Modules + container queries。`tokens.ts` 只可作为 typed mirror；Style Dictionary、Tokens Studio、Tailwind、Panda、shadcn、React Flow、Lucide、Radix、TanStack 或 React 版本升级都不得从本文件自动推出。若某个 dispatch 需要这些 package，应在独立 package gate 中提出，不在 visual atlas 中夹带批准。

本节适用于 `GATE-02 Spacing & Alignment Test Cases`：审查者应记录 source label、state word、token reference、layout slot、failure class、defer condition 与 human reviewer note。若证据缺失，写 `needs_evidence`，不得写 `passed by assumption`。


### GATE-02 Spacing & Alignment Test Cases — audit expansion 13

### Linked-state grammar / 状态语法

每个视觉对象至少绑定一个 state word：`idle`、`editing`、`requested`、`settling`、`ready`、`allowed`、`candidate`、`future_gate`、`blocked`、`stale`、`probe_failed`、`preview_only`。状态应同时体现在文案、badge、border/fill、position/order 与可访问名称中。`audio_transcript`、media processing、browser automation、migration、vault true write 仍必须以 blocked/future-gated 方式出现，不得藏进 tooltip。

本节适用于 `GATE-02 Spacing & Alignment Test Cases`：审查者应记录 source label、state word、token reference、layout slot、failure class、defer condition 与 human reviewer note。若证据缺失，写 `needs_evidence`，不得写 `passed by assumption`。
