---
title: "ILL10 Illustration Spec — poster-hero / social-card-hero"
status: "candidate / not-authority"
authority: not-authority
created_at: 2026-05-07
atlas_id: U13-visual-style-brand-atlas-v0
file_kind: illustration
claim_labels:
  - canonical fact from local packet
  - promoted_addendum-aware inference
  - tentative candidate
  - needs_live_web_refresh
boundary: "docs-only; no runtime/package/frontend/browser/vault/migration approval"
---

# ILL10 Illustration Spec — poster-hero / social-card-hero

## Scope

Each illustration is an inline SVG concept spec, not an exported PNG/SVG asset. The style is deep-sea blueprint: large quiet canvas, restrained cyan linework, evidence panels, low-noise geometry, no mascot clutter, no generic SaaS people scene.


## Illustration `poster-hero`

| Field | Value |
|---|---|
| illustration_id | `poster-hero` |
| intent | Poster hero |
| concept | large format campaign but evidence-first |
| linked_state | `idle / ready / candidate / future_gate / blocked` as applicable |
| linked_visual_asset | `U4:poster-hero` pending external refresh |
| license | ScoutFlow-original candidate geometry; no third-party art copied |
| format | Inline SVG concept, scalable |

```svg
<svg viewBox="0 0 640 360" role="img" aria-hidden="true" fill="none" xmlns="http://www.w3.org/2000/svg">
  <path d="M32 300H608V64H32Z" fill="#07111B"/>
  <path d="M64 92H576V280H64Z" fill="#111F31" stroke="#27415D" stroke-width="3"/>
  <path d="M64 122H320V162H64Z" fill="#0B1624" stroke="#3A5879" stroke-width="2"/>
  <path d="M64 188H260V228H64Z" fill="#10233D" stroke="#27415D" stroke-width="2"/>
  <path d="M360 118H520V240H360Z" fill="#0B1624" stroke="#50D4FF" stroke-width="3"/>
  <path d="M384 156H496 M384 188H476 M384 220H456" stroke="#A6B8CF" stroke-width="6" stroke-linecap="round"/>
  <path d="M86 302C152 250 226 252 288 302C354 354 478 348 568 302" stroke="#50D4FF" stroke-opacity=".45" stroke-width="4"/>
</svg>
```

### Composition recipe

- Background: `sf.canvas.0` or `sf.canvas.1` with a quiet grid or topographic line.
- Panels: `sf.panel.bg` with `sf.border.panel`; one evidence object may use `sf.accent.cyan` or `sf.success`.
- Human presence, if any, is abstracted as operator focus lines, not cartoon personas. This keeps ScoutFlow single-user and technical.
- Empty/error/loading variants must keep the same frame so state changes do not look like a different product.

### Use cases

- Hero / cover when explaining the station to a reviewer.
- Empty-state in H5 or H5 export when no data is present.
- Poster/social/PPT template if paired with precise state copy.
- Not for production UI until final SVG and accessibility alt text are approved.

### 5-Gate notes

Gate 1 fails if this illustration steals attention from the URL action on an app screen. Gate 5 fails if decorative waves, glows or pseudo-3D depth are heavier than the evidence path. Gate 3 fails if the illustration becomes a background behind state text and reduces readability.


## Illustration `social-card-hero`

| Field | Value |
|---|---|
| illustration_id | `social-card-hero` |
| intent | Social card hero |
| concept | portable 1:1/16:9/9:16 summaries |
| linked_state | `idle / ready / candidate / future_gate / blocked` as applicable |
| linked_visual_asset | `U4:social-card-hero` pending external refresh |
| license | ScoutFlow-original candidate geometry; no third-party art copied |
| format | Inline SVG concept, scalable |

```svg
<svg viewBox="0 0 640 360" role="img" aria-hidden="true" fill="none" xmlns="http://www.w3.org/2000/svg">
  <path d="M32 300H608V64H32Z" fill="#07111B"/>
  <path d="M64 92H576V280H64Z" fill="#111F31" stroke="#27415D" stroke-width="3"/>
  <path d="M72 122H320V162H72Z" fill="#0B1624" stroke="#3A5879" stroke-width="2"/>
  <path d="M72 188H260V228H72Z" fill="#10233D" stroke="#27415D" stroke-width="2"/>
  <path d="M360 118H520V240H360Z" fill="#0B1624" stroke="#50D4FF" stroke-width="3"/>
  <path d="M384 156H496 M384 188H476 M384 220H456" stroke="#A6B8CF" stroke-width="6" stroke-linecap="round"/>
  <path d="M86 302C152 250 226 252 288 302C354 354 478 348 568 302" stroke="#50D4FF" stroke-opacity=".45" stroke-width="4"/>
</svg>
```

### Composition recipe

- Background: `sf.canvas.0` or `sf.canvas.1` with a quiet grid or topographic line.
- Panels: `sf.panel.bg` with `sf.border.panel`; one evidence object may use `sf.accent.cyan` or `sf.success`.
- Human presence, if any, is abstracted as operator focus lines, not cartoon personas. This keeps ScoutFlow single-user and technical.
- Empty/error/loading variants must keep the same frame so state changes do not look like a different product.

### Use cases

- Hero / cover when explaining the station to a reviewer.
- Empty-state in H5 or H5 export when no data is present.
- Poster/social/PPT template if paired with precise state copy.
- Not for production UI until final SVG and accessibility alt text are approved.

### 5-Gate notes

Gate 1 fails if this illustration steals attention from the URL action on an app screen. Gate 5 fails if decorative waves, glows or pseudo-3D depth are heavier than the evidence path. Gate 3 fails if the illustration becomes a background behind state text and reduces readability.


## Boundary / 边界声明

- `status`: candidate；`authority`: not-authority；本文件不是 CSS token 合并、frontend implementation、package install、browser automation、runtime、vault true write、migration 或 authority writeback 批准。
- 可被 PF-V / GPT-Image-2 / future dispatch 作为视觉 atlas 输入；不可把本文内任何 token、SVG、layout 或 template 直接解释成 production contract。
- 所有主观 5-Gate 判断保持 human-in-loop；自动化只能提供截图、contrast、DOM 或 manifest evidence，不能替代最终视觉判断。
- 第三方库仅作为参考类别；本 atlas 内联 SVG 均按 ScoutFlow-original candidate 处理，未复制第三方 path。若未来改用第三方 icon/illustration，必须重新验证 license。


### ILL10 Illustration Spec — poster-hero / social-card-hero — audit expansion 1

### Review discipline / 审查纪律

1. 先判断 L1 information architecture：URL Bar → Live Metadata → Capture Scope → Trust Trace 的扫描顺序不可被模板、装饰图、sidebar 或 KPI 区域改写。
2. 再判断 L2 structure：panel、row、badge、detail shelf、graph node、template slot 必须共享 8dp rhythm 与同一套语义 token，不允许在局部硬编码新的蓝色、阴影或圆角。
3. 最后判断 L3 mood：深海蓝、低眩光、operator workstation、evidence-first、single-user dense surface；强视觉不是荧光科技感，也不是营销 hero 图。
4. 对任何 `blocked` / `future_gate` / `candidate` lane，必须有文字、badge、位置与视觉权重共同表达；颜色不能成为唯一信号。
5. 任何截图、render pass、contrast pass 都只能作为 evidence；若 Gate 1-5 任一失败，最终 verdict 必须是 `visual_not_passed`。

本节适用于 `ILL10 Illustration Spec — poster-hero / social-card-hero`：审查者应记录 source label、state word、token reference、layout slot、failure class、defer condition 与 human reviewer note。若证据缺失，写 `needs_evidence`，不得写 `passed by assumption`。


### ILL10 Illustration Spec — poster-hero / social-card-hero — audit expansion 2

### 5-Gate alignment / 五门对齐

| Gate | Local acceptance | Failure signal |
|---|---|---|
| Gate 1 hierarchy | 主动作或主证据 3 秒内可识别 | 装饰、图表、future lane 抢第一注意点 |
| Gate 2 spacing/alignment | 8dp grid、共同 baseline、稳定 panel padding | row、badge、图节点漂移，导致扫描断裂 |
| Gate 3 occlusion | tooltip/toast/legend 不遮 URL/current state/node label | overlay 遮住可操作或可审计信息 |
| Gate 4 typography/readability | 中英混排、URL、ID、timestamp 可读 | 小字、低对比、截断造成状态误判 |
| Gate 5 visual weight | active/current/proven 高于 blocked/candidate/future | danger 或 decorative glow 反向支配界面 |

本节适用于 `ILL10 Illustration Spec — poster-hero / social-card-hero`：审查者应记录 source label、state word、token reference、layout slot、failure class、defer condition 与 human reviewer note。若证据缺失，写 `needs_evidence`，不得写 `passed by assumption`。


### ILL10 Illustration Spec — poster-hero / social-card-hero — audit expansion 3

### Implementation seam / 实现缝合位

推荐未来实现路径为 CSS Variables + CSS Modules + container queries。`tokens.ts` 只可作为 typed mirror；Style Dictionary、Tokens Studio、Tailwind、Panda、shadcn、React Flow、Lucide、Radix、TanStack 或 React 版本升级都不得从本文件自动推出。若某个 dispatch 需要这些 package，应在独立 package gate 中提出，不在 visual atlas 中夹带批准。

本节适用于 `ILL10 Illustration Spec — poster-hero / social-card-hero`：审查者应记录 source label、state word、token reference、layout slot、failure class、defer condition 与 human reviewer note。若证据缺失，写 `needs_evidence`，不得写 `passed by assumption`。


### ILL10 Illustration Spec — poster-hero / social-card-hero — audit expansion 4

### Linked-state grammar / 状态语法

每个视觉对象至少绑定一个 state word：`idle`、`editing`、`requested`、`settling`、`ready`、`allowed`、`candidate`、`future_gate`、`blocked`、`stale`、`probe_failed`、`preview_only`。状态应同时体现在文案、badge、border/fill、position/order 与可访问名称中。`audio_transcript`、media processing、browser automation、migration、vault true write 仍必须以 blocked/future-gated 方式出现，不得藏进 tooltip。

本节适用于 `ILL10 Illustration Spec — poster-hero / social-card-hero`：审查者应记录 source label、state word、token reference、layout slot、failure class、defer condition 与 human reviewer note。若证据缺失，写 `needs_evidence`，不得写 `passed by assumption`。


### ILL10 Illustration Spec — poster-hero / social-card-hero — audit expansion 5

### Review discipline / 审查纪律

1. 先判断 L1 information architecture：URL Bar → Live Metadata → Capture Scope → Trust Trace 的扫描顺序不可被模板、装饰图、sidebar 或 KPI 区域改写。
2. 再判断 L2 structure：panel、row、badge、detail shelf、graph node、template slot 必须共享 8dp rhythm 与同一套语义 token，不允许在局部硬编码新的蓝色、阴影或圆角。
3. 最后判断 L3 mood：深海蓝、低眩光、operator workstation、evidence-first、single-user dense surface；强视觉不是荧光科技感，也不是营销 hero 图。
4. 对任何 `blocked` / `future_gate` / `candidate` lane，必须有文字、badge、位置与视觉权重共同表达；颜色不能成为唯一信号。
5. 任何截图、render pass、contrast pass 都只能作为 evidence；若 Gate 1-5 任一失败，最终 verdict 必须是 `visual_not_passed`。

本节适用于 `ILL10 Illustration Spec — poster-hero / social-card-hero`：审查者应记录 source label、state word、token reference、layout slot、failure class、defer condition 与 human reviewer note。若证据缺失，写 `needs_evidence`，不得写 `passed by assumption`。
