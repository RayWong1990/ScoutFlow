---
title: PF-V → PF-C4 Handoff Protocol v1 (post-P7 finalized)
status: candidate / handoff_contract / not-authority
authority: not-authority
from_lane: PF-V (Visual Prototype Lane, P0-P8)
to_lane: PF-C4-01 (Local Frontend Bootstrap)
date: 2026-05-07
supersedes: 05-HANDOFF-to-PF-C4-protocol.md (v0 candidate, 2026-05-06)
---

# PF-V → PF-C4 Handoff Protocol v1

中文副线：PF-V 视觉原型研究 lane 在 P8 关闭，并把 P0-P7 产生的视觉证据、rough HTML5 结构、token discipline 与边界规则交给 PF-C4-01。本文是交接契约，不是 implementation approval，也不替代 PF-C4 自己的 React TSX 设计判断。It is deliberately written as an audit-readable contract: every consumer should be able to trace a claim back to an actual file, a lesson ID, an INDEX row, or a P7 output artifact.

## §1 What you receive — PF-C4 收到什么

PF-C4 收到的是一组候选研究资产，全部位于 `docs/research/visual-prototypes/PF-V/` 语义下。它们可作为本地前端 bootstrap 的参考输入，但不能升格为 runtime code、approved IA、package adoption 或 authority source。

1. **152 source mockup PNGs**：源图分布在 `docs/research/visual-prototypes/PF-V/images-P*/` 目录族中，覆盖 P0 anchor、P1 desktop foundation、P2 panel detail、P3 extended surfaces、P5 icons、P6 density/type refinement。P4 states 被显式跳过，因为 P2/P3 已经在真实 surface 语境中覆盖 idle/loading/ready/error/blocked/disabled/active/empty/success 等状态。所有 PNG 都是 visual evidence，不是 pixel-perfect implementation source。
2. **`PF-V-INDEX.csv`**：152 data rows、19 columns，是图像 provenance、session、surface、variant axis、V-verdict、local path、downstream_use 与 forbidden_use 的来源表。PF-C4 应用它确认某个图为什么进入 P7 bundle，而不是凭文件名倒推来源。
3. **`p7-output/`**：实际 handoff target，共 76 files。它包含 13 个 `html5-rough/*.html` surface、13 个同名 `*.module.css` surface stylesheet、13 个 `*.model.json` structural model、15 组 component candidate（每组 `.module.css` + `.html`，合计 30 files）、2 个 SVG sprite（`icons/system.svg` + `icons/state.svg`）、3 个全局 CSS 文件（`tokens.css`、`density-compact.css`、`type-weight-heavy.css`）、`MAPPING.md` 与 `README.md`。`MAPPING.md` 已把 65 张输入 mockup task 一一映射到输出文件。
4. **`PF-V-LESSONS-LEARNED.md`**：落地 P8 patch 后应包含 L1-L13。PF-C4 特别需要读取 L2（Obsidian raw vault boundary）、L8（cross-system sync badge pattern）、L10（caption-as-spec）与 L11/L13（density × typography orthogonal matrix）。这些 lessons 是 PF-V 过程中已经 settle 的设计判断，不在 PF-C4 bootstrap 时重新争辩。
5. **`PF-V-00-master-context.md`**：包含 token system definitions、anti-patterns、language policy、realistic dummy content、Obsidian boundary 与 P7 image-to-code 输出期待。PF-C4 可读它理解视觉规则，但不应把它当生产实现规范；生产命名、组件拆分与类型接口由 PF-C4 lane 自行决定。
6. **Lane support docs**：`PF-V-README.md` 提供 lane overview 与 PM 记录；`PF-V-MAINTENANCE-PROTOCOL.md` 解释 CC0 如何维持 INDEX/LESSONS/README 同步；`PF-V-03-P7-batch-prompt-v2.md` 记录 P7 prompt 与 P8 deferred references；v0 handoff 只作为被本 v1 替换的 baseline。


Receive interpretation: PF-C4 should treat the bundle as a layered reference stack. The PNG layer answers “what visual evidence existed”; the INDEX layer answers “why this image was accepted and where it came from”; the P7 layer answers “how the surface can be decomposed into browser-readable HTML/CSS/SVG”; the LESSONS layer answers “which mistakes have already been found and fixed”; the handoff layer answers “what PF-C4 may and may not do next.” Reading only one layer is insufficient. In particular, looking only at the pretty PNGs risks pixel-copying, while looking only at HTML risks missing the session-level provenance and V-verdict context.

The handoff also preserves the single-writer boundary from `PROJECT-CLAUDE.md`. CC0 applies PF-V research edits and opens the P8 PR; PF-C4 consumes the merged research bundle later. PF-C4 should not use this protocol to justify edits to authority docs, project trackers, production directories, or dependency manifests. If PF-C4 needs an implementation decision, it records that decision inside its own lane artifacts and PR, not by retroactively changing PF-V.

## §2 What PF-C4 should DO with each deliverable — 如何消费每类资产

PF-C4 应按“先结构、再样式、再实现”的顺序消费，而不是直接从 PNG 临摹。推荐阅读顺序是：`p7-output/README.md` → `p7-output/MAPPING.md` → `html5-rough/*.model.json` → `html5-rough/*.html` → `tokens.css` 与 component candidates → INDEX/LESSONS 交叉验证。

- **`p7-output/html5-rough/*.html`**：读取它们的 IA skeleton、scan order、semantic tag choice 与 state class semantics。每个 surface 通常把多个状态放在同一个 HTML 文件中，例如 URL Bar 的 empty/focus/validating/error/history-open，或 Topic Card Vault 的 default/aggregated/promote/modal/sync。PF-C4 转成 TSX 时应保留“多状态语义”，但不导入原始 HTML。
- **`p7-output/html5-rough/*.model.json`**：作为 Step 1 JSON UI structural model 使用。它们能帮助 PF-C4 先确认区域、元素、复用组件和 icon 引用，再决定 React component tree。若最终 component tree 与 JSON 不一致，PF-C4 可忽略 JSON；JSON 是 bonus reference，不是约束。
- **`p7-output/tokens.css`**：作为全局 CSS Variables 的 single source of truth 复制/迁移。它定义 15 个主色 token、4 个 derived state background、字体、字号、字重、间距、圆角、阴影。任何 PF-C4 CSS Module 中出现颜色时，应继续引用变量，不在 `tokens.css` 外写 hex。
- **`p7-output/css-modules-candidate/`**：把 15 个 component candidates 翻译成 PF-C4 自己 component folder 内的真实 CSS Modules。候选包括 `panel-card`、`url-input`、`state-badge`、`lifecycle-stepper`、`evidence-table`、`tag-list`、`capture-id-chip`、`topic-card`、`sync-badge`、`modal`、`governance-tooltip`、`live-pulse`、`btn`、`frontmatter-block`、`promote-gate`。这些名字是参考边界，不是必须照抄的 production class name。
- **`p7-output/icons/*.svg`**：通过 `<svg><use href="...#icon-id"></use></svg>` 语义引用或迁移到 PF-C4 的图标系统，优先保留 sprite + symbol 的复用方式。不要把 symbol path 随意内联复制到多个组件中，避免后续 icon drift。
- **`PF-V-LESSONS-LEARNED.md`**：遵守 L8 sync badge 跨系统模式：凡是 ScoutFlow ↔ Obsidian raw vault 的本地状态对比，都应有 synced/pending/external-changed 三档。遵守 L11/L13：density 与 typography 是正交二维矩阵，不把密度调整和字重调整混成一次重写。
- **`PF-V-INDEX.csv`**：在需要追溯 source mockup 时，从 `downstream_use=PF-C4-html-source-priority` 或 `PF-C4-svg-source-priority` 的行开始核对，再回看非 priority rows。INDEX 的 `forbidden_use=not-implementation-source` 是硬边界。


Practical receive workflow: first open `00-app-shell.html` to understand the full workstation composition, then inspect `01-url-bar.html` through `06-vault-commit.html` for core capture station flow, then inspect `07-topic-card-lite.html` through `10-capture-plan.html` for downstream topic/signal/plan surfaces, and finally inspect `11-density-spec.html` plus `12-type-spec.html` for refinement layers. This order follows the original P7 surface groups and avoids treating a refinement example as the main application shell.

During translation, PF-C4 should keep a separation between **surface semantics**, **component extraction**, and **state modifiers**. Surface semantics come from the 13 H5 files. Component extraction comes from the 15 candidate pairs. State modifiers come from class suffixes such as `--error`, `--ready`, `--sync`, `--external-changed`, and from INDEX session notes. The final TSX may rename all of them, but the semantic distinctions should survive the rename.

## §3 What PF-C4 must NOT do — 明确拒绝清单

以下条目是 handoff 的 STOP line，任何一项违反都意味着 PF-C4 没有正确接收 PF-V：

- **不要在 runtime 导入 raw HTML**。`html5-rough/*.html` 只用于阅读结构和状态，不是可部署代码。
- **不要逐字照搬 class names**。P7 的 class name 主要服务于 review 和状态说明；PF-C4 应按项目自己的 React/CSS Module conventions 翻译。
- **不要在 `tokens.css` 外硬编码 hex**。P7 已验证 `.module.css` 中没有硬编码颜色；PF-C4 迁移时应保持这个 token discipline。
- **不要采用 Tailwind / shadcn / Panda 或其他 styling package**。PF-V handoff 没有 package approval，也不改变 zero-install policy。
- **不要把 vault path mock 成其他路径**。ScoutFlow 的交付边界是 `~/workspace/raw/00-Inbox/`；后续 enrich、wiki link backfill、Dataview rollup 与知识飞轮发生在 Obsidian 内，不发生在 ScoutFlow 内。
- **不要修改 PF-V research lane files**。PF-V 在 P8 后锁定；PF-C4 写自己的 TSX、CSS Modules 与测试，不回写 `docs/research/visual-prototypes/PF-V/`。
- **不要把 PNG 当 approved IA 或 pixel-perfect spec**。Mockup 宽度是视觉参考，目标是保留 mood、hierarchy、状态语义和 token discipline，而不是逐像素复刻。
- **不要重开 L1-L11 已 settle 的判断**。PF-C4 可以发现新的 implementation issue，但不在 bootstrap 阶段重新争论 UI chrome 是否中文、Obsidian boundary 是否属于 ScoutFlow、P4 是否应补跑等问题。


The reject list is intentionally strict because P7 succeeded by constraining ambiguity. PF-C4 can make implementation tradeoffs, but those tradeoffs must be explicit in PF-C4. For example, choosing a graph library for Trust Trace is a PF-C4 implementation decision; replacing the PF-V token palette with a new namespace during bootstrap is not. Similarly, creating a TSX component with different naming is normal; keeping raw HTML as a hidden runtime fixture is not.

If a future reviewer asks whether a PF-C4 choice is allowed, use this decision test: does the choice preserve PF-V's reference evidence while moving implementation responsibility into PF-C4? If yes, it is likely allowed. Does the choice mutate PF-V, claim PF-V is authority, bypass tokens, invent a new visual system, or move Obsidian work into ScoutFlow? If yes, reject it or open a separate candidate decision for review.

## §4 TODO placeholders inventory — P7 留下的动态接线占位

`p7-output/README.md` 已声明 TODO 占位只涉及图谱、时间轴、缩略图数据与真实后端状态接线。逐项 inventory 如下；这里的 library 是候选建议，不是 package approval，PF-C4 仍需按自己的 zero-install/approval 流程决定。

| File + line | Reason | Suggested implementation library / approach | Priority |
|---|---|---|---|
| `p7-output/html5-rough/02-live-metadata.html:69` | 来源图 `task-10_thumbnail-field.png` 展示真实视频缩略图；P7 只能放结构占位，不能从 BBDown/metadata pipeline 取得真实 asset。 | 使用 PF-C4 的 metadata result 接线到 `<img>`/thumbnail component；若 BBDown metadata 暴露 thumbnail URL，则接入缓存与 fallback placeholder。 | P1 — post-skeleton；首个 scaffold 可保留占位。 |
| `p7-output/html5-rough/04-trust-trace.html:21` | 来源图 `task-14_filter-dom-only.png` 包含复杂 DOM-tree visualization；rough HTML 不能可靠手写交互图谱。 | D3 / vis-network / cytoscape 任选其一作为候选图谱实现方向；PF-C4 也可用自研 SVG/canvas graph，前提是状态语义可测试。 | P1 — 信任溯源核心交互，skeleton 后优先。 |
| `p7-output/html5-rough/04-trust-trace.html:40` | 来源图 `task-15_time-axis.png` 包含 D3 timeline、hover timestamp tooltip 与证据定位；P7 仅保留时间刻度 placeholder。 | D3 timeline 或轻量 SVG timeline；必须支持 hover timestamp、field evidence 定位、UTC 时间显示。 | P2 — polish；不阻塞 first commit。 |
| `p7-output/html5-rough/04-trust-trace.html:64` | 来源图 `task-16_error-path.png` 展示 graph error path highlight；需要与真实 field extraction error 数据绑定。 | 与 line 21 的 graph implementation 共用 graph lib；给 error path 增加 highlighted edge/node layer 与 evidence row sync。 | P1 — 与 graph implementation 同批处理。 |


Priority meanings: P0 would block PF-C4's first scaffold commit because the reference cannot be safely rendered or reasoned about. P1 belongs immediately after the scaffold because it affects core interaction truth. P2 is polish or richer interaction fidelity that can wait until skeleton, tokens, and state semantics are already ported. None of the four TODOs are P0 because P7 provided honest placeholders and the HTML remains reviewable; however, the two graph-related P1 items should not be ignored indefinitely because Trust Trace is one of the visual anchors inherited from the super anchor work.

## §5 Density × Typography matrix — 100-cell 正交配置空间

P6 的 S17 density 与 S18 typography 是 PF-V 最重要的 refinement 资产。两组 session 都固定 SUPER-ANCHOR-FINAL 的 IA、调色板和 dummy content，只改变一个 axis，因此 PF-C4 可以把它们看成 **10 × 10 = 100 个潜在配置组合**，而不是 20 张互不相干的图。

- **Density axis（S17, V1-V10）**：覆盖 default、comfortable、compact、dense、ultra-dense、spacious、operator-focused、mixed-dense 等谱系。PF-V 推荐 baseline 是 **V3 Compact**，对应 `pfv-S17-V3-cn-density-compact-TOP1.png` 与 `p7-output/density-compact.css`。P7 输出的 override 只调整 `--type-title`、`--type-body`、`--space-md`、`--space-sm`，作为 additive layer 叠在 `tokens.css` 后面。
- **Typography axis（S18, V1-V10）**：覆盖 default、larger title、mono emphasis、weight heavy 等谱系。PF-V 推荐 baseline 是 **V4 Weight Heavy**，对应 `pfv-S18-V4-cn-type-weight-heavy-TOP2.png` 与 `p7-output/type-weight-heavy.css`。P7 输出的 override 调整 `--font-weight-hero`、`--font-weight-title`、`--font-weight-body`、`--font-weight-mono`、`--type-mono`。

PF-C4 的实现原则是：先导入 `tokens.css`；需要 operator-daily compact baseline 时再叠加 `density-compact.css`；需要 production recommended weight baseline 时再叠加 `type-weight-heavy.css`。这两个 layer 应保持正交，不能把 density toggle 写进组件 prop drilling，也不能为了局部组件重写 token 值。若 PF-C4 未来要支持 100-cell toggle UI，应从 token layer 组合开始，而不是从 PNG 重画或复制样式块。


The matrix should be implemented as a system-level styling concern, not a per-component feature flag. A correct PF-C4 bootstrap can start with one baseline combination and still keep the matrix future-ready by retaining token names and override file boundaries. A risky bootstrap would bake compact spacing into every component file, because later switching to a different density would require manual rewrites. The whole reason S17/S18 were designed as single-axis sessions is to prevent that rewrite debt.

The P7 files give concrete proof that the approach is lossless enough for handoff: `11-density-spec.html` demonstrates the compact baseline in a full workstation composition, and `12-type-spec.html` demonstrates heavy typography without changing the IA. This is the minimal evidence PF-C4 needs at bootstrap. It does not need to implement all 100 combinations immediately; it only needs to avoid closing the door on them.

## §6 Cross-system Sync semantic — sync-badge 跨系统语义

LESSONS L8 把 ScoutFlow ↔ Obsidian raw vault 的一致性问题固化为三档 sync badge。P7 已把它落在 `p7-output/css-modules-candidate/sync-badge.*` 和 `p7-output/html5-rough/08-topic-card-vault.html` 的 `topic-card-vault--sync` 状态中。

Contract 如下：

| State | UI label | CSS state | Icon pairing | Token intent |
|---|---|---|---|---|
| synced | 已同步 | `sync-badge--synced` | `icons/state.svg#icon-success` | `accent_success` + `state-bg-success` |
| pending | 待同步 | `sync-badge--pending` | `icons/state.svg#icon-warning` | `accent_warn` + `state-bg-warn` |
| external-changed | 外部已改 | `sync-badge--external-changed` | `icons/state.svg#icon-focus` | `accent_focus` + muted surface |

这不是 Topic Card Vault 的局部装饰，而是跨系统数据交互模式。凡是 UI 同时展示 ScoutFlow 本地状态和 Obsidian raw vault 状态，PF-C4 都应优先复用这三档语义。badge 应始终与 `state.svg` 的 success/warning/focus icon 配对；不要用 system icon 的 blocked/trace/signal 语义替代 sync state。


Operationally, this pattern covers at least three situations: ScoutFlow has written a Markdown file and Obsidian has indexed it (`synced`); ScoutFlow has a local preview or pending write that Obsidian has not yet reflected (`pending`); Obsidian has changed the note after ScoutFlow's last known state (`external-changed`). PF-C4 may refine copy or data wiring, but it should not collapse these into a binary “saved / not saved” model because that loses the cross-system consistency signal discovered in S11.

## §7 Acceptance criteria for PF-C4 to “receive” the handoff — 接收完成判定

PF-C4 宣布“handoff received / ready to start implementation”前，至少满足以下条件：

1. `p7-output/` 的 76 个文件都存在；13 个 `html5-rough/*.html` 可在浏览器打开，能看出对应 surface、状态段落和中文 UI 文案；无 console error 影响静态渲染。
2. `tokens.css`、`density-compact.css`、`type-weight-heavy.css` 复制到 PF-C4 codebase 后语义无损：变量名和值不漂移，additive layer 顺序明确，且 `.module.css` 中继续只引用变量。
3. `P8-ACCEPTANCE-CHECKLIST.md` 的 30 项检查全部为 green，特别是 file presence、token discipline、semantic HTML、anti-pattern absence、cross-system boundary、PF-C4 readiness 六类。
4. PF-C4 已确认 raw HTML 不会进入 runtime，PNG 不会被声明为 approved IA，PF-V lane 不会被 PF-C4 修改。
5. PF-C4 lane 可以打开自己的第一条实现 PR，例如 `feat(capture-station): scaffold p7-reference`，并在该 PR 中说明 P7 rough HTML5 只是 reference material。


Receiving the handoff does not require PF-C4 to solve every downstream TODO, choose every library, or finish every component. It only requires PF-C4 to prove that the research bundle is complete, internally consistent, and safe to consume. This distinction matters: PF-V closes with a clean reference contract; PF-C4 opens with implementation planning. Mixing those phases would either keep PF-V artificially open or force PF-C4 to accept unreviewed implementation choices too early.

## §8 Risk register + acknowledgements — 已知摩擦与确认事项

- **Mockup 尺寸风险**：PF-V mockups 以 1152px 宽呈现，是从更高分辨率视觉源压缩/整理后的证据。PF-C4 不追求 pixel-perfect implementation；目标是保留 hierarchy、density、token discipline、状态语义和 Obsidian boundary。
- **Native dialog 风险**：部分 P7 surface 使用 `<dialog open>` 展示 modal 状态。老浏览器可能需要 polyfill 或替代实现；是否支持、如何支持，由 PF-C4 按项目 target browser 决定。
- **Container query 风险**：P7 CSS 倾向使用 container-oriented 思路而不是全局 `@media`。Safari < 16 可能需要 fallback；PF-C4 在 bootstrap 时先确认项目浏览器支持线。
- **JSON model 风险**：13 个 `.model.json` 是 Step 1 structural model，用于帮助 review，不保证与最终 React component tree 一致。PF-C4 可局部忽略，不构成 implementation blocker。
- **Historical path concern**：S08 的 10 张 vault-preview PNG 在 INDEX 中标记为 `V-PASS-with-path-concern`，因为历史图曾出现路径 concern。P7 输出与本 handoff 统一使用 `~/workspace/raw/00-Inbox/`，PF-C4 不能回到历史 dummy path。
- **Deferred library choice**：图谱、时间轴、thumbnail 接线均在 TODO inventory 中。P8 提供 candidate implementation direction，但不授予 package adoption，也不指定 React state/data library。


Risk treatment rule: document rather than silently correct. If PF-C4 discovers that a model JSON omits a component, or that a placeholder needs a different graph approach, the correct action is to record a PF-C4 implementation note and proceed within PF-C4. The incorrect action is to edit PF-V history or regenerate a new PF-V mockup. PF-V is closed evidence; PF-C4 is the living implementation lane.

## §9 P8 deferred items (from CC1 audit) — 候选参考，不并入 P7

`PF-V-03-P7-batch-prompt-v2.md` 的 “P8 Handoff Backlog” 记录了 5 个 deferred references。它们都保持 `candidate / not-authority`，PF-C4 可以选择采用、忽略或部分移植；P7 output 有效性不依赖它们。

| # | Candidate reference | PF-C4 may use it for | Boundary |
|---|---|---|---|
| 1 | `outputs/U7-state-library/MODULE-state-library-spec.md` + `8-PANEL-STATE-INVENTORY.md` | 48-state matrix 与 `props_json` schema；当 PF-C4 把 P7 HTML state classes 翻译成 React component props interface 时，可作为候选 cross-check。 | 不要求 P7 或 PF-C4 首个 PR 直接采用。 |
| 2 | `outputs/U4-visual-asset/MODULE-visual-asset-spec.md` | SQLite `visual_asset` schema 与 5-state lifecycle（gen / candidate / refined / locked / deprecated）；PF-C4 可评估是否把 PF-V images 注册成 asset rows。 | 若不采用，继续以 INDEX.csv 管理 provenance。 |
| 3 | `outputs/U4-visual-asset/PF-V-INTEGRATION-MAP.md` | `PF-V-INDEX.csv` 19 columns → `visual_asset` table migration plan。 | 只在 PF-C4 决定落 SQLite schema 时相关。 |
| 4 | `outputs/U8-egress/HANDOFF-MANIFEST-JSON-SCHEMA.md` | 4 downstream-variant manifest schemas；未来 packaging handoff bundle 时可引用。 | P8 当前 ZIP 不需要 manifest。 |
| 5 | `outputs/U13-visual-brand/05-panel-design-spec/PANEL-01.md ~ PANEL-08.md` | 6-state grammar（idle / loading / ready / candidate / blocked / stale）与 good-vs-bad panel examples；可 cross-validate state class naming。 | CC1 audit 提到其中有 30-40% audit-expansion boilerplate；消费前需清理，不覆盖 PF-V token/icon winners。 |


The reject rationale from P7 remains active in P8. U13 token namespace replacement would diverge from the 152 mockups and P7 `tokens.css`; U13 SVG candidates would conflict with the P5 icon winners already selected; U7 `props_json` becomes useful when PF-C4 writes component interfaces, not while PF-V is producing rough HTML. Therefore these references are intentionally placed in the handoff notes rather than merged into P7 output.

## §10 Sign-off statement — PF-V lane closure

PF-V 在 P8 handoff PR 合并后进入 `closed_with_handoff_to_PF-C4`。PF-V 不再 regen、不再 evolve、不再产出新图或新 H5。未来任何视觉问题、实现取舍、组件命名、浏览器支持、graph/timeline library 选择，都由 PF-C4-01 或后续 PF-C4 子 lane 发起；如需引用 PF-V，只能引用本 handoff、INDEX、LESSONS 与 `p7-output/` 中已存在的候选资产。

本文件本身仍是 `candidate / not-authority`。它的作用是让 PF-C4 明确收到什么、如何消费、哪些边界不能越过；它不批准 runtime implementation，不修改 authority files，不替代 CC0 single-writer 对 project authority docs 的控制。


Sign-off also means no “small extra” PF-V tasks after merge. A stable handoff is valuable because downstream reviewers can compare PF-C4 code against one frozen evidence set, one frozen INDEX, one frozen P7 output tree, and one dated handoff contract. If reference material keeps changing during implementation, audit cannot distinguish deliberate implementation choice from moving-source drift. Therefore archive stability is part of the contract, not clerical cleanup. If PF-C4 later needs a new density baseline, a new icon, a modified state grammar, or a different graph visualization, that work belongs in PF-C4 or a separately opened future visual lane. The historical PF-V bundle should remain stable so reviewers can compare implementation against the exact evidence that was handed off on 2026-05-07, with no hidden regeneration and no retroactive provenance changes.

Final audit note: PF-C4 should preserve a written trace from each implementation decision back to this bundle. A compact example is: “state semantics from `08-topic-card-vault.html`, sync contract from LESSONS L8, icon pairing from `icons/state.svg`, visual provenance from INDEX row `pfv-S11-V10`.” This style of trace keeps the implementation review concrete. It also prevents a common failure mode where a developer says “the prototype looked like this” without naming which prototype, which state, and which accepted row. PF-V already paid the cost of indexing 152 images; PF-C4 should use that provenance instead of re-creating informal memory.
