---
title: PF-V P7 — Batch Image-to-HTML5 Prompt v2 (65-task / 65-image bundle)
status: candidate / batch_conversion_prompt / not-authority / not-implementation-approval
created_at: 2026-05-07
purpose: Convert 65 V-PASS mockup images (13 surface groups + 2 icon sprite groups) into rough HTML5 + CSS Modules + SVG sprite for PF-C4 lane consumption
target: GPT Pro web (云端，thinking mode, 1-2 hour run)
supersedes: 03-P7-batch-image-to-html5-prompt.md (v1, scoped to 50 images)
---

# How to use this file

1. CC0 (Claude Code) generates `pfv-p7-bundle.zip` via `scripts/build-p7-bundle.sh` (pulls 65 images by INDEX V-PASS, renames per ZIP path mapping, optimizes PNG, packs).
2. User opens NEW GPT Pro session.
3. Paste `00-master-context.md` first (the canonical context block).
4. Upload `pfv-p7-bundle.zip` (drag/drop into chat).
5. Paste the **P7 PROMPT v2** from this file (the fenced block below).
6. GPT Pro thinks 30-90 min, outputs structured ZIP via canvas/code-interpreter download:
   - `tokens.css` (15 color tokens + spacing/type/radius/shadow vars)
   - `html5-rough/00-app-shell.html` ... `12-type-spec.html` (13 surface H5 files)
   - `css-modules-candidate/*.module.css` + `*.html` snippet (~30 component pairs)
   - `icons/system.svg` + `icons/state.svg` (2 SVG sprites with `<symbol>` reuse)
   - `MAPPING.md` (image filename → output file map)
   - `README.md` (P7 output overview + how PF-C4 should consume)
7. CC0 downloads, unzips into `docs/research/visual-prototypes/PF-V/p7-output/`.
8. CC0 reviews quality contract per file. If pass → P8 handoff PR. If fail → delta correction prompt for failing tasks only.

---

# Bundle plan (65 images / 65 tasks / 13 H5 + 2 SVG outputs)

| # | Surface group | Tasks | Source images (V-PASS) | Output |
|---|---|---|---|---|
| 00 | App Shell | 1 (Task 00) | SUPER-ANCHOR-FINAL | 00-app-shell.html |
| 01 | URL Bar | 5 (Tasks 01-05) | S04 V1/V2/V5/V6/V9 | 01-url-bar.html |
| 02 | Live Metadata | 5 (Tasks 06-10) | S05 V1/V4/V6/V7/V10 | 02-live-metadata.html |
| 03 | Capture Scope | 3 (Tasks 11-13) | S06 V1/V3/V5 | 03-capture-scope.html |
| 04 | Trust Trace | 3 (Tasks 14-16) | S07 V1/V3/V4 | 04-trust-trace.html |
| 05 | Vault Preview | 5 (Tasks 17-21) | S08 V1/V3/V5/V7/V8 | 05-vault-preview.html |
| 06 | Vault Commit | 5 (Tasks 22-26) | S09 V1/V2/V4/V5/V9 | 06-vault-commit.html |
| 07 | Topic Card Lite | 5 (Tasks 27-31) | S10 V1/V2/V5/V7/V10 | 07-topic-card-lite.html |
| 08 | Topic Card Vault | 5 (Tasks 32-36) | S11 V1/V5/V7/V8/V10 | 08-topic-card-vault.html |
| 09 | Signal/Hypothesis IA | 3 (Tasks 37-39) | S12 V2/V3/V4 | 09-signal-hypothesis.html |
| 10 | Capture Plan IA | 3 (Tasks 40-42) | S12 V7/V8/V9 | 10-capture-plan.html |
| 11 | Density Spec ref | 1 (Task 43) | S17-V3 Compact | 11-density-spec.html |
| 12 | Type Spec ref | 1 (Task 44) | S18-V4 Weight Heavy | 12-type-spec.html |
| 13 | Icons system | 10 (Tasks 45-54) | S15 V1-V10 | icons/system.svg |
| 14 | Icons state | 10 (Tasks 55-64) | S16 V1-V10 | icons/state.svg |
| **Σ** | | **65** | | **13 H5 + 2 SVG + tokens.css + ~30 module css + MAPPING + README** |

---

# ZIP structure (one-to-one with task IDs)

```
pfv-p7-bundle.zip
├── 00_app-shell/
│   └── task-00_master.png
├── 01_url-bar/
│   ├── task-01_state-empty.png
│   ├── task-02_state-focus.png
│   ├── task-03_state-validating.png
│   ├── task-04_state-error.png
│   └── task-05_state-history-dropdown.png
├── 02_live-metadata/
│   ├── task-06_long-cn-title.png
│   ├── task-07_numbers-heavy.png
│   ├── task-08_tags-overflow.png
│   ├── task-09_live-counter.png
│   └── task-10_thumbnail-field.png
├── 03_capture-scope/
│   ├── task-11_lifecycle-start.png
│   ├── task-12_lifecycle-complete.png
│   └── task-13_blocked-layer-tooltip.png
├── 04_trust-trace/
│   ├── task-14_filter-dom-only.png
│   ├── task-15_time-axis.png
│   └── task-16_error-path.png
├── 05_vault-preview/
│   ├── task-17_idle.png
│   ├── task-18_ready.png
│   ├── task-19_blocked-overflow-registry.png
│   ├── task-20_frontmatter-expanded.png
│   └── task-21_copy-action.png
├── 06_vault-commit/
│   ├── task-22_standard.png
│   ├── task-23_tooltip-knowledge-flywheel.png
│   ├── task-24_modal-pass.png
│   ├── task-25_modal-fail.png
│   └── task-26_batch-dry-run.png
├── 07_topic-card-lite/
│   ├── task-27_news-article.png
│   ├── task-28_bilibili-video.png
│   ├── task-29_multi-signal.png
│   ├── task-30_evidence-pointers.png
│   └── task-31_dual-card-compare.png
├── 08_topic-card-vault/
│   ├── task-32_default.png
│   ├── task-33_source-url-aggregate.png
│   ├── task-34_promote-readiness.png
│   ├── task-35_promote-diloflow-modal.png
│   └── task-36_obsidian-sync-status.png
├── 09_signal-hypothesis-ia/
│   ├── task-37_signal-expanded-with-hypotheses.png
│   ├── task-38_hypothesis-compare.png
│   └── task-39_signal-lifecycle-stepper.png
├── 10_capture-plan-ia/
│   ├── task-40_plan-io-contract.png
│   ├── task-41_plan-dry-run.png
│   └── task-42_plan-execution-log.png
├── 11_density-spec/
│   └── task-43_density-compact-baseline.png
├── 12_type-spec/
│   └── task-44_type-weight-heavy.png
├── 13_icons-system/
│   ├── task-45_icon-capture.png
│   ├── task-46_icon-preview.png
│   ├── task-47_icon-commit.png
│   ├── task-48_icon-dry-run.png
│   ├── task-49_icon-blocked.png
│   ├── task-50_icon-signal.png
│   ├── task-51_icon-hypothesis.png
│   ├── task-52_icon-plan.png
│   ├── task-53_icon-trace.png
│   └── task-54_icon-evidence.png
└── 14_icons-state/
    ├── task-55_icon-state-live.png
    ├── task-56_icon-state-success.png
    ├── task-57_icon-state-warning.png
    ├── task-58_icon-state-error.png
    ├── task-59_icon-state-blocked.png
    ├── task-60_icon-state-locked.png
    ├── task-61_icon-state-focus.png
    ├── task-62_icon-state-loading.png
    ├── task-63_icon-state-empty.png
    └── task-64_icon-state-ready.png
```

---

# P7 PROMPT v2 (paste this whole block after uploading bundle)

```
===BEGIN PF-V P7 BATCH PROMPT v2===

# § 0  Role + Output Contract

You are converting 65 ScoutFlow mockup images (uploaded as `pfv-p7-bundle.zip`) into a downstream-consumable rough HTML5 wireframe set, plus extracted CSS Modules candidates, plus 2 SVG sprite files. The downstream PF-C4-01 Local Frontend Bootstrap lane will translate your output to React TSX.

You DO produce:
- 1 `tokens.css` — CSS Variables for all design tokens (15 colors + typography + spacing + radius + shadow)
- 13 `*.html` surface files (rough HTML5, semantic markup, no JS)
- ~30 `*.module.css` + matching `*.html` usage snippet (component candidates extracted from 2+ surface reuse)
- 2 `*.svg` sprite files with `<symbol>` reuse (icons-system / icons-state)
- 1 `MAPPING.md` mapping every input image → at least one output file
- 1 `README.md` explaining the bundle for PF-C4 consumption

You DO NOT produce:
- React / Vue / Svelte component code
- npm install commands or `package.json`
- Tailwind / shadcn / Panda class names
- Inline `style="..."` attributes (single allowed exception: `:root` token definition in `tokens.css`)
- Hardcoded hex colors anywhere
- Production-quality TSX (that's PF-C4's responsibility)

# § 1  Three-Step Pipeline

Apply this pipeline to ALL 65 tasks (BESSER/IFML ICWE 2025 methodology — direct image→code is unreliable; intermediate JSON model gives self-check anchor):

**Step 1 — Decompose into JSON UI structural model**
For each surface group (13 groups), output a JSON model in plain text BEFORE generating HTML:
```json
{
  "surface_id": "01-url-bar",
  "source_images": ["task-01_state-empty.png", "task-02_state-focus.png", "task-03_state-validating.png", "task-04_state-error.png", "task-05_state-history-dropdown.png"],
  "ia": {
    "regions": [{"id": "url-input", "role": "primary-input"}, {"id": "submit-btn", "role": "primary-action"}, {"id": "history-dropdown", "role": "history-list"}]
  },
  "elements": [
    {"id": "url-input", "tag": "input", "type": "url", "states": ["empty", "focus", "validating", "error", "history-open"], "tokens": ["surface_muted", "border_soft", "text_primary", "accent_live"]},
    {"id": "submit-btn", "tag": "button", "label": "创建采集", "states": ["disabled", "active"], "tokens": ["accent_live", "text_primary"]}
  ],
  "components_extracted": [{"name": "url-input", "reuse_count": 1, "tag": "candidate"}, {"name": "submit-btn", "reuse_count": 5, "tag": "definite"}],
  "icons_referenced": []
}
```

If a surface's IA can't be cleanly decomposed, regenerate the model BEFORE writing HTML.

**Step 2 — Generate per-surface HTML5**
For each surface group, write ONE `*.html` file containing all states as nested `<section class="X X--state-Y">` blocks. Multi-state demo per file makes downstream review fast.

**Step 3 — Extract reusable components**
Any element appearing in 2+ surfaces with similar structure → write `css-modules-candidate/{component}.module.css` + `{component}.html` usage snippet.

# § 2  Token CSS file (generate once, reference everywhere)

Generate `tokens.css` with all design tokens as CSS Variables on `:root`:

```css
:root {
  /* Color tokens (15 — exact hex from master context, never invent) */
  --bg-canvas: #07111b;
  --bg-shell: #0d1826;
  --surface-base: #111f31;
  --surface-elevated: #16263c;
  --surface-muted: #0b1624;
  --border-strong: #27415d;
  --border-soft: #1d3148;
  --text-primary: #eef4ff;
  --text-secondary: #a6b8cf;
  --text-muted: #6d8099;
  --accent-live: #50d4ff;
  --accent-success: #53d690;
  --accent-warn: #ffbe55;
  --accent-blocked: #ff7b7b;
  --accent-focus: #9a8cff;

  /* State background colors (tinted dark, for badge/banner backgrounds; cross-validated against U13 derived family) */
  --state-bg-success: #10291f;  /* tinted dark green — pairs with --accent-success */
  --state-bg-warn:    #332512;  /* tinted dark amber — pairs with --accent-warn */
  --state-bg-blocked: #33191e;  /* tinted dark red   — pairs with --accent-blocked */
  --state-bg-info:    #10233d;  /* tinted dark blue  — pairs with --accent-live */
  /* WCAG 2.2 contrast matrix verified against above palette — see audit report:
     docs/research/strategic-upgrade/2026-05-07/outputs/U13-visual-brand/01-token-system/TOKEN-01-PALETTE-15-DEEP-BLUE-AND-DERIVED.md
     PF-C4 lane MAY consume this matrix as accessibility evidence; not required for P7. */

  /* Typography */
  --font-display: "Inter", "SF Pro Display", "Helvetica Neue", sans-serif;
  --font-body: "Inter", "PingFang SC", "Noto Sans SC", sans-serif;
  --font-mono: "JetBrains Mono", "SFMono-Regular", monospace;
  --type-hero: 28px;
  --type-title: 20px;
  --type-body: 14px;
  --type-caption: 12px;
  --line-height-body: 1.45;

  /* Spacing (8px grid) */
  --space-xs: 8px;
  --space-sm: 12px;
  --space-md: 16px;
  --space-lg: 24px;
  --space-xl: 32px;

  /* Radius */
  --radius-panel: 8px;
  --radius-chip: 999px;
  --radius-button: 10px;

  /* Shadow */
  --shadow-panel: 0 24px 48px rgba(0,0,0,0.32);
  --shadow-elevated: 0 12px 24px rgba(0,0,0,0.24);
}
```

EVERY `.module.css` file must reference these via `var(--token-name)`. ZERO hardcoded hex anywhere outside `tokens.css`.

# § 3  HTML5 contract (per file, hard rules)

- `<main>` for page shell, `<header>` for top URL Bar region (when present), `<aside>` for sidebars, `<section>` for each panel
- Headings: `<h1>` for surface title, `<h2>` for panel titles, `<h3>` for sub-blocks
- `<p>` for body text, `<code>` for IDs/URLs/timestamps/paths (mono treatment)
- `<table><thead><tbody>` for tabular metadata, NOT div grids
- `<ul>` for tag chips / evidence lists, `<ol>` for ordered steppers
- `<button>` for actions, NEVER `<div role="button">`
- NO `<div>` without semantic justification — if you can't justify, remove it
- Single linked stylesheet per HTML: `<link rel="stylesheet" href="../tokens.css"><link rel="stylesheet" href="./{surface-id}.module.css">`
- `class` naming: BEM-lite — `block__element--modifier` (lower-kebab-case)
- NO Tailwind / shadcn / utility classes
- NO inline `style="..."` (single exception: `:root` in `tokens.css`)
- States visualized via CSS class modifiers: `.url-bar__input--focus`, `.url-bar__input--error`, `.vault-preview--blocked`, etc.
- Multi-state demo: render multiple state variants in same HTML file as parallel `<section>` blocks with state class modifiers, separated by `<hr class="state-divider">` and labeled `<h3>` with state name

# § 4  CSS Module contract

- All values reference `var(--token-name)` — ZERO hex / px values outside the 8px grid (single allowed: 1px borders, 1.5px stroke svg)
- BEM-lite class naming consistent with HTML
- Nested syntax (PostCSS / native CSS nesting OK): `.url-bar { &__input { ... &--focus { ... } } }`
- `@container` queries for responsive (preferred) or `@media` fallback
  - Breakpoints: 768px (tablet linearize), 1280px (desktop 3-column)
  - Below 768px: vertical stack of all panels
- States via modifier class, NOT inline style or JS

# § 5  SVG sprite contract

For each icon sprite file (`icons/system.svg` and `icons/state.svg`):
- Single `<svg>` root with `display: none` (so file is sprite, not visible standalone)
- Each icon as `<symbol id="icon-{name}" viewBox="0 0 256 256">` inside
- All paths use `stroke="currentColor"` (so consumer can recolor via CSS)
- `stroke-width="1.5"` (maps to 2K visual at native 256 viewBox)
- NO fill except where structurally necessary (e.g., padlock body fill needed; capture arrow stroke-only)
- Each icon ≤ 20 path commands — if exceeded, redraw simpler
- NO gradients / filters / clip paths (clean line geometry only)

Consumer usage example (for downstream documentation):
```html
<svg class="icon"><use href="../icons/system.svg#icon-trace"/></svg>
```
With CSS: `.icon { width: 24px; height: 24px; color: var(--accent-live); }`

# § 6  Trade-off rule (preserve editability over pixel-perfect fidelity)

If a mockup detail (complex graph rendering, exotic gradient, photo background) cannot cleanly become semantic HTML + CSS Variables + clean SVG:
- DO NOT mechanically auto-vectorize into noisy SVG (50+ path commands)
- DO NOT embed as base64 inline image
- INSTEAD: leave a `<!-- TODO: ... -->` comment + clean placeholder element

Example for trust-trace graph:
```html
<!-- TODO: source mockup task-15_time-axis.png shows complex DOM-tree visualization. 
     PF-C4 should consume original image as visual reference and implement using 
     a graph library (D3 / vis-network / cytoscape). This is structural placeholder. -->
<section class="trust-trace__graph-placeholder" data-todo="graph-rendering">
  <p class="placeholder-hint">Trust Trace 图谱（视觉参考: task-15_time-axis.png）</p>
</section>
```

This is intentional. PF-C4 consumes the image and implements properly with the appropriate graph library.

# § 7  Anti-patterns (any one present = REGENERATE that file)

- ❌ `<div>` proliferation without semantic purpose
- ❌ Inline hex values in CSS (must be `var(--token-name)`)
- ❌ Tailwind utility classes (e.g., `bg-blue-500`, `flex`, `mt-4`)
- ❌ Inline `style="..."` attributes
- ❌ `<img>` for icons (must be inline `<svg>` or sprite reference)
- ❌ Auto-vectorized SVG with 50+ path commands (redraw or TODO placeholder)
- ❌ Decorative gradients (purple→pink, neon glow, glassmorphism)
- ❌ Marketing/SaaS chrome (sign up CTA, premium badges, hero banners)
- ❌ Round avatar circles (single-operator surface, no team avatars)
- ❌ Emoji icons (use line-icons via SVG sprite)
- ❌ Real company logos (use generic placeholders)
- ❌ Hardcoded English UI strings (everything in 简体中文 except URLs / IDs / file paths / YAML keys / DOM-path field names)
- ❌ Card-inside-card stacking (max nesting depth = 2 panels)

# § 8  Self-verification checklist (run before delivery)

For EVERY output file:
- [ ] HTML5 valid (semantic tags, no orphan `<div>`)
- [ ] Single `<link>` per HTML referencing `tokens.css` + its `*.module.css`
- [ ] All visible UI text in 简体中文 (only URLs / capture_id / paths / YAML keys English)
- [ ] All colors `var(--token-name)`, zero hex outside `tokens.css`
- [ ] All spacing 8px multiple
- [ ] Icons inline SVG or `<use href="../icons/...svg#icon-X">`
- [ ] State variants demonstrated as `<section class="block--state-X">`
- [ ] BEM-lite naming consistent
- [ ] No Tailwind / utility classes
- [ ] vault path correct: `~/workspace/raw/00-Inbox/cap_20260506_8a3f2.md` (NEVER `~/scoutflow-vault/`)

For `MAPPING.md`:
- [ ] Every 65 input image referenced at least once
- [ ] Every output file lists which input image(s) sourced it

For `README.md`:
- [ ] Explains zero-install consumption (no npm install needed; HTML opens in browser)
- [ ] Explains how PF-C4 should translate to React TSX
- [ ] Lists which TODO placeholders need PF-C4 attention

# § 9  Per-task specifications (Tasks 00-64)

Below are the 65 task specs. Each task references its ZIP-path image and tells you which output file/section to update.

Use the JSON model (Step 1) to GROUP tasks by surface — generate JSON model once per surface (13 models total), then walk through tasks within that surface to populate state classes / inline content / element variants.

---

## Task 00 — App Shell Master

**Input**: `00_app-shell/task-00_master.png`
**Output**: `html5-rough/00-app-shell.html`
**Image content**: Full 4-panel composition — top URL Bar (full width) + 3-column [Live Metadata | Capture Scope | Trust Trace (widest)] + Vault Preview Panel + Vault Commit Dry-Run Button (top-right corner).
**HTML structure**:
```html
<main class="app-shell">
  <header class="app-shell__header">
    <h1 class="app-shell__brand">ScoutFlow 采集线 · 本地操作员工作站 · 仅预览模式</h1>
    <button class="vault-commit-btn" disabled>入库提交（干跑）</button>
  </header>
  <section class="app-shell__url-bar"><!-- url-bar component --></section>
  <div class="app-shell__panels">
    <section class="panel panel--metadata"><!-- live-metadata --></section>
    <section class="panel panel--scope"><!-- capture-scope --></section>
    <section class="panel panel--trace"><!-- trust-trace --></section>
  </div>
  <section class="app-shell__preview"><!-- vault-preview --></section>
</main>
```
**CSS rules**: 3-column grid `grid-template-columns: 1fr 1fr 1.5fr` for panels (Trust Trace wider). `gap: var(--space-md)`. Container query at 768px linearize.

---

## Task 01 — URL Bar / state empty

**Input**: `01_url-bar/task-01_state-empty.png`
**Output**: `html5-rough/01-url-bar.html` → `<section class="url-bar url-bar--empty">`
**Image content**: URL input empty, placeholder "粘贴一个 URL 或拖入文件", border_soft, no focus glow. Submit button "创建采集" disabled.
**HTML**:
```html
<section class="url-bar url-bar--empty">
  <h3 class="state-label">状态: 空闲</h3>
  <input type="url" class="url-bar__input" placeholder="粘贴一个 URL 或拖入文件" />
  <button class="url-bar__submit" disabled>创建采集</button>
</section>
```
**CSS** (`.url-bar__input--empty`):
- `background: var(--surface-muted); border: 1px solid var(--border-soft); padding: var(--space-md); color: var(--text-secondary);`

---

## Task 02 — URL Bar / state focus

**Input**: `01_url-bar/task-02_state-focus.png`
**Output**: same file, `<section class="url-bar url-bar--focus">`
**Image content**: URL input focused, border accent_live cyan glow, cursor visible, placeholder still present.
**HTML**: same skeleton, class modifier `--focus` and add `autofocus` on `<input>`.
**CSS** (`.url-bar__input--focus`): `border-color: var(--accent-live); box-shadow: 0 0 0 2px rgba(80, 212, 255, 0.2);`

---

## Task 03 — URL Bar / state validating

**Input**: `01_url-bar/task-03_state-validating.png`
**Output**: same file, `<section class="url-bar url-bar--validating">`
**Image content**: URL pasted (`https://www.bilibili.com/video/BV1xK4y1f7yC`), inline spinner near submit button, "解析中..." text. Submit button still disabled.
**HTML**: input has `value` attribute filled, add `<span class="url-bar__spinner" aria-busy="true">解析中...</span>` adjacent.
**CSS**: spinner uses `var(--accent-live)`, animated rotation via `@keyframes spin`.

---

## Task 04 — URL Bar / state error

**Input**: `01_url-bar/task-04_state-error.png`
**Output**: same file, `<section class="url-bar url-bar--error">`
**Image content**: URL input filled with invalid URL, border accent_blocked red, error message below "URL 格式无效".
**HTML**: add `<p class="url-bar__error">URL 格式无效</p>` after input.
**CSS** (`.url-bar__input--error`): `border-color: var(--accent-blocked); color: var(--accent-blocked);`

---

## Task 05 — URL Bar / history dropdown

**Input**: `01_url-bar/task-05_state-history-dropdown.png`
**Output**: same file, `<section class="url-bar url-bar--history-open">`
**Image content**: URL input focused, dropdown below with 3-5 recent URLs as `<li>`, each with capture_id mono chip and timestamp.
**HTML**:
```html
<section class="url-bar url-bar--history-open">
  <input ... />
  <ul class="url-bar__history" role="listbox">
    <li class="url-bar__history-item"><code class="capture-id">cap_20260506_8a3f2</code><span class="url-bar__history-time">14:32 UTC</span></li>
    <!-- 4-5 more items -->
  </ul>
</section>
```
**CSS**: dropdown uses `var(--surface-elevated)`, `box-shadow: var(--shadow-elevated)`, items hover `background: var(--surface-base)`.

---

## Task 06 — Live Metadata / long CN title

**Input**: `02_live-metadata/task-06_long-cn-title.png`
**Output**: `html5-rough/02-live-metadata.html` → `<section class="live-metadata live-metadata--long-title">`
**Image content**: 8 metadata fields visible, video title is long CN that wraps 2 lines, uploader chip with avatar-less @ syntax, view/like/comment counts in mono, capture_id and timestamps.
**HTML**:
```html
<section class="live-metadata live-metadata--long-title">
  <h3 class="state-label">状态: 长标题（中文换行）</h3>
  <dl class="metadata-grid">
    <dt>视频标题</dt><dd>深度工作流 vs 普通工作流 — 高效操作员的 5 个习惯</dd>
    <dt>上传者</dt><dd>@scout_ops_archive</dd>
    <dt>时长</dt><dd><code>12:34</code></dd>
    <dt>播放量</dt><dd><code>24,891</code></dd>
    <dt>点赞</dt><dd><code>3,142</code></dd>
    <dt>评论</dt><dd><code>287</code></dd>
    <dt>capture_id</dt><dd><code>cap_20260506_8a3f2</code></dd>
    <dt>最后更新</dt><dd><code>2026-05-06 14:32 UTC</code></dd>
  </dl>
</section>
```
**CSS**: `dl.metadata-grid` uses `display: grid; grid-template-columns: max-content 1fr; gap: var(--space-sm) var(--space-md);`. `dt` is `var(--text-muted)`, `dd` is `var(--text-primary)`. `code` uses `var(--font-mono); color: var(--accent-live);`.

---

## Task 07 — Live Metadata / numbers heavy

**Input**: `02_live-metadata/task-07_numbers-heavy.png`
**Output**: same file, `<section class="live-metadata live-metadata--numbers-heavy">`
**Image content**: numeric fields dominant — large font play count, like count, comment count rendered prominent in accent_live, smaller text labels. Video title secondary.
**HTML**: same `<dl>` structure but use `<strong>` wrapper for numeric values, CSS handles size emphasis.
**CSS**: `.live-metadata--numbers-heavy strong { font-size: var(--type-title); color: var(--accent-live); }`

---

## Task 08 — Live Metadata / tags overflow

**Input**: `02_live-metadata/task-08_tags-overflow.png`
**Output**: same file, `<section class="live-metadata live-metadata--tags-overflow">`
**Image content**: tag chips displayed at bottom of metadata panel, 12+ tags wrapping multiple rows, last row shows "+N more" affordance.
**HTML**:
```html
<section class="live-metadata live-metadata--tags-overflow">
  <dl class="metadata-grid">...</dl>
  <ul class="tag-list">
    <li class="tag-chip">深度工作</li>
    <li class="tag-chip">操作员</li>
    <!-- more tags -->
    <li class="tag-chip tag-chip--more">+5 更多</li>
  </ul>
</section>
```
**CSS**: `.tag-list` uses `flex-wrap: wrap; gap: var(--space-xs);`. `.tag-chip` is `var(--surface-elevated)`, `border-radius: var(--radius-chip)`, `padding: 4px var(--space-sm)`.

---

## Task 09 — Live Metadata / live counter

**Input**: `02_live-metadata/task-09_live-counter.png`
**Output**: same file, `<section class="live-metadata live-metadata--live-counter">`
**Image content**: play count and like count animate as live counters, accent_live pulse dot beside each, last-update timestamp ticks.
**HTML**: add `<span class="live-pulse" aria-live="polite"></span>` next to each animated metric.
**CSS**: `.live-pulse` is animated keyframe pulse using `var(--accent-live)`. `@keyframes pulse { 0% {opacity: 1;} 50% {opacity: 0.4;} 100% {opacity: 1;} }`.

---

## Task 10 — Live Metadata / thumbnail field

**Input**: `02_live-metadata/task-10_thumbnail-field.png`
**Output**: same file, `<section class="live-metadata live-metadata--with-thumbnail">`
**Image content**: thumbnail square 80×80px showing video thumbnail mood (dark canvas placeholder, generic geometry), positioned top-left of metadata panel.
**HTML**:
```html
<section class="live-metadata live-metadata--with-thumbnail">
  <figure class="thumbnail-frame">
    <!-- TODO: source mockup task-10 shows video thumbnail.
         PF-C4 should fetch actual thumbnail from BBDown extracted metadata. -->
    <div class="thumbnail-placeholder" data-todo="thumbnail-fetch"></div>
  </figure>
  <dl class="metadata-grid">...</dl>
</section>
```
**CSS**: `.thumbnail-frame` is 80×80 with `background: var(--surface-elevated)`, `border-radius: var(--radius-panel)`, fixed aspect 1:1.

---

## Task 11 — Capture Scope / lifecycle start

**Input**: `03_capture-scope/task-11_lifecycle-start.png`
**Output**: `html5-rough/03-capture-scope.html` → `<section class="capture-scope capture-scope--start">`
**Image content**: 5-step horizontal stepper (1=URL 验证 / 2=元数据加载 / 3=正文抓取 / 4=入库预览 / 5=入库提交), step 1 active accent_live, steps 2-5 muted. State badges show "仅元数据 / 已折叠".
**HTML**:
```html
<section class="capture-scope capture-scope--start">
  <ol class="lifecycle-stepper" aria-label="生命周期阶段">
    <li class="lifecycle-step lifecycle-step--active"><span class="step-num">1</span><span class="step-name">URL 验证</span></li>
    <li class="lifecycle-step"><span class="step-num">2</span><span class="step-name">元数据加载</span></li>
    <li class="lifecycle-step"><span class="step-num">3</span><span class="step-name">正文抓取</span></li>
    <li class="lifecycle-step"><span class="step-num">4</span><span class="step-name">入库预览</span></li>
    <li class="lifecycle-step"><span class="step-num">5</span><span class="step-name">入库提交</span></li>
  </ol>
  <dl class="scope-state">
    <dt>状态</dt><dd><span class="state-badge state-badge--metadata-only">仅元数据</span></dd>
    <dt>抓取范围</dt><dd>已折叠</dd>
  </dl>
</section>
```
**CSS**: `.lifecycle-stepper` uses `flex` horizontal, connector line via `::before` pseudo. `.lifecycle-step--active .step-num` uses `var(--accent-live)`. `.state-badge` extracted as `state-badge.module.css` candidate.

---

## Task 12 — Capture Scope / lifecycle complete

**Input**: `03_capture-scope/task-12_lifecycle-complete.png`
**Output**: same file, `<section class="capture-scope capture-scope--complete">`
**Image content**: all 5 steps completed (accent_success green checkmarks), step 5 active accent_live, scope state badge "已锁定".
**HTML**: same stepper but `<li class="lifecycle-step lifecycle-step--done">` with `<svg><use href="../icons/state.svg#icon-success"/></svg>` instead of step-num.
**CSS**: `.lifecycle-step--done .step-num` replaced with success icon, `color: var(--accent-success);`.

---

## Task 13 — Capture Scope / blocked layer tooltip

**Input**: `03_capture-scope/task-13_blocked-layer-tooltip.png`
**Output**: same file, `<section class="capture-scope capture-scope--blocked-tooltip">`
**Image content**: stepper at step 5 (入库提交), tooltip overlay on step 5 explaining governance boundary "ScoutFlow 责任边界 / Obsidian 接管 enrich-wiki-知识飞轮", accent_blocked outline.
**HTML**:
```html
<section class="capture-scope capture-scope--blocked-tooltip">
  <ol class="lifecycle-stepper">...</ol>
  <aside class="governance-tooltip" role="tooltip">
    <h4 class="governance-tooltip__title">治理边界</h4>
    <p>ScoutFlow 交付干净 markdown 到 Obsidian raw vault inbox（<code>~/workspace/raw/00-Inbox/</code>）。</p>
    <p>之后 enrich / wiki / 知识飞轮 在 Obsidian 内发生，ScoutFlow 不参与。</p>
  </aside>
</section>
```
**CSS**: `.governance-tooltip` uses `var(--surface-elevated)`, `border: 1px solid var(--accent-blocked)`, `box-shadow: var(--shadow-elevated)`. Anchored to step 5 via absolute positioning.

---

## Task 14 — Trust Trace / filter dom only

**Input**: `04_trust-trace/task-14_filter-dom-only.png`
**Output**: `html5-rough/04-trust-trace.html` → `<section class="trust-trace trust-trace--filter-dom">`
**Image content**: Filter chips at top (DOM / JSON-LD / OpenGraph / Microdata), only DOM active. Below: tree-style graph showing dom.meta paths only, evidence rows below graph.
**HTML**:
```html
<section class="trust-trace trust-trace--filter-dom">
  <ul class="trace-filters" role="tablist">
    <li class="trace-filter trace-filter--active">DOM</li>
    <li class="trace-filter">JSON-LD</li>
    <li class="trace-filter">OpenGraph</li>
    <li class="trace-filter">Microdata</li>
  </ul>
  <!-- TODO: source mockup shows complex DOM-tree visualization.
       PF-C4 should implement using D3 / vis-network / cytoscape graph library.
       This is structural placeholder. -->
  <section class="trust-trace__graph-placeholder" data-todo="graph-rendering">
    <p class="placeholder-hint">Trust Trace 图谱（视觉参考: task-14_filter-dom-only.png）</p>
  </section>
  <table class="evidence-table">
    <thead><tr><th>字段</th><th>DOM 路径</th><th>值</th><th>置信度</th></tr></thead>
    <tbody>
      <tr><td>title</td><td><code>dom.meta.og:title</code></td><td>深度工作流 vs 普通工作流</td><td>98%</td></tr>
      <!-- 4-5 more rows -->
    </tbody>
  </table>
</section>
```
**CSS**: `.trace-filter--active` uses `var(--accent-live)`. `.evidence-table` extracted as `evidence-table.module.css` candidate (used in 04-trust-trace + parts of 05-vault-preview).

---

## Task 15 — Trust Trace / time axis

**Input**: `04_trust-trace/task-15_time-axis.png`
**Output**: same file, `<section class="trust-trace trust-trace--time-axis">`
**Image content**: horizontal time axis at top showing 5 timestamp ticks (24h scale), nodes plotted along axis showing when each evidence was captured, hover state shows tooltip with full timestamp.
**HTML**: TODO placeholder for graph (D3 timeline), but include axis structure as `<header><h4>时间轴 (UTC)</h4><div class="time-axis-placeholder" data-todo="d3-timeline"></div></header>`.

---

## Task 16 — Trust Trace / error path

**Input**: `04_trust-trace/task-16_error-path.png`
**Output**: same file, `<section class="trust-trace trust-trace--error-path">`
**Image content**: graph with one path highlighted in accent_blocked red, error chip "字段缺失: og:duration", error trace in evidence-table row.
**HTML**: evidence-table row with `<tr class="evidence-row--error">`, `<td class="evidence-status"><svg><use href="../icons/state.svg#icon-error"/></svg></td>`.
**CSS**: `.evidence-row--error` uses `background: rgba(255, 123, 123, 0.08)` (semi-transparent accent_blocked).

---

## Task 17 — Vault Preview / idle

**Input**: `05_vault-preview/task-17_idle.png`
**Output**: `html5-rough/05-vault-preview.html` → `<section class="vault-preview vault-preview--idle">`
**Image content**: empty preview panel, hint "尚未生成预览，等待元数据完成", muted state.
**HTML**:
```html
<section class="vault-preview vault-preview--idle">
  <h2 class="vault-preview__title">入库预览</h2>
  <p class="vault-preview__hint">尚未生成预览，等待元数据完成。</p>
</section>
```

---

## Task 18 — Vault Preview / ready

**Input**: `05_vault-preview/task-18_ready.png`
**Output**: same file, `<section class="vault-preview vault-preview--ready">`
**Image content**: full markdown preview rendered, frontmatter YAML at top in mono, body markdown text, vault path shown bottom "目标: ~/workspace/raw/00-Inbox/cap_20260506_8a3f2.md", state badge "预览就绪".
**HTML**:
```html
<section class="vault-preview vault-preview--ready">
  <h2>入库预览</h2>
  <span class="state-badge state-badge--ready">预览就绪</span>
  <pre class="frontmatter-block"><code>---
title: 深度工作流 vs 普通工作流 — 高效操作员的 5 个习惯
capture_id: cap_20260506_8a3f2
status: preview_only
write_enabled: false
vault_target: ~/workspace/raw/00-Inbox/
---</code></pre>
  <article class="preview-body">
    <h3>视频摘要</h3>
    <p>本视频对比了深度工作流与普通工作流的差异...</p>
  </article>
  <footer class="vault-preview__target">
    <span>目标: </span><code>~/workspace/raw/00-Inbox/cap_20260506_8a3f2.md</code>
  </footer>
</section>
```

---

## Task 19 — Vault Preview / blocked overflow registry

**Input**: `05_vault-preview/task-19_blocked-overflow-registry.png`
**Output**: same file, `<section class="vault-preview vault-preview--blocked">`
**Image content**: preview shown but with overlay banner "已阻塞: 写入禁用 / overflow registry queue 持有", padlock icon, accent_blocked.
**HTML**: add `<aside class="vault-preview__block-banner" role="alert"><svg><use href="../icons/state.svg#icon-blocked"/></svg><p>已阻塞: 写入禁用 / overflow registry 队列持有</p></aside>` overlay.

---

## Task 20 — Vault Preview / frontmatter expanded

**Input**: `05_vault-preview/task-20_frontmatter-expanded.png`
**Output**: same file, `<section class="vault-preview vault-preview--frontmatter-expanded">`
**Image content**: full frontmatter visible (10+ fields), each field with field-evidence link to Trust Trace.
**HTML**: `<dl class="frontmatter-fields">` with each `<dt>` linking via `data-trace-id` to evidence row.

---

## Task 21 — Vault Preview / copy action

**Input**: `05_vault-preview/task-21_copy-action.png`
**Output**: same file, `<section class="vault-preview vault-preview--copy-action">`
**Image content**: copy button highlighted, toast shown "Markdown 已复制到剪贴板", checkmark accent_success.
**HTML**: `<button class="vault-preview__copy">复制 Markdown</button>` + `<aside class="toast toast--success" role="status">Markdown 已复制到剪贴板</aside>`.

---

## Task 22 — Vault Commit / standard

**Input**: `06_vault-commit/task-22_standard.png`
**Output**: `html5-rough/06-vault-commit.html` → `<section class="vault-commit vault-commit--standard">`
**Image content**: dry-run button top-right, normal state, accent_live border.
**HTML**:
```html
<section class="vault-commit vault-commit--standard">
  <button class="vault-commit__btn" type="button">
    <svg class="icon"><use href="../icons/system.svg#icon-dry-run"/></svg>
    入库提交（干跑）
  </button>
</section>
```

---

## Task 23 — Vault Commit / tooltip knowledge flywheel

**Input**: `06_vault-commit/task-23_tooltip-knowledge-flywheel.png`
**Output**: same file, `<section class="vault-commit vault-commit--tooltip-flywheel">`
**Image content**: dry-run button hovered, tooltip explaining "实际入库后由 Obsidian 接管 (enrich / wiki / 知识飞轮)".
**HTML**: button + `<aside class="vault-commit__tooltip" role="tooltip">实际入库后由 Obsidian 接管（enrich / wiki / 知识飞轮）</aside>`.

---

## Task 24 — Vault Commit / modal pass

**Input**: `06_vault-commit/task-24_modal-pass.png`
**Output**: same file, `<section class="vault-commit vault-commit--modal-pass">`
**Image content**: modal dialog overlay, dry-run result accent_success, list of validations passed (frontmatter / vault path / write_enabled=false / etc), commit blocked (preview only).
**HTML**:
```html
<section class="vault-commit vault-commit--modal-pass">
  <dialog class="modal modal--pass" open>
    <h2><svg><use href="../icons/state.svg#icon-success"/></svg> 干跑通过</h2>
    <ul class="validation-list">
      <li class="validation-item validation-item--pass">Frontmatter 完整</li>
      <li class="validation-item validation-item--pass">Vault 路径有效</li>
      <li class="validation-item validation-item--pass">write_enabled = false（预期）</li>
      <li class="validation-item validation-item--pass">capture_id 唯一</li>
    </ul>
    <footer class="modal__footer">
      <button class="btn btn--secondary">关闭</button>
      <button class="btn btn--primary" disabled>实际入库（已锁定）</button>
    </footer>
  </dialog>
</section>
```

---

## Task 25 — Vault Commit / modal fail

**Input**: `06_vault-commit/task-25_modal-fail.png`
**Output**: same file, `<section class="vault-commit vault-commit--modal-fail">`
**Image content**: modal with accent_blocked, list with mixed pass/fail items, fail items show error reason.
**HTML**: same modal skeleton but with `validation-item--fail` modifiers and `<p class="validation-item__error">` reason.

---

## Task 26 — Vault Commit / batch dry-run

**Input**: `06_vault-commit/task-26_batch-dry-run.png`
**Output**: same file, `<section class="vault-commit vault-commit--batch">`
**Image content**: batch panel showing 12 captures queued, each row with checkbox + capture_id + status, batch dry-run button bottom.
**HTML**: `<table class="batch-table">` with rows + `<button class="btn--primary">批量干跑</button>`.

---

## Task 27 — Topic Card Lite / news article

**Input**: `07_topic-card-lite/task-27_news-article.png`
**Output**: `html5-rough/07-topic-card-lite.html` → `<section class="topic-card topic-card--news">`
**Image content**: card with news article variant: source URL, title, abstract, single signal chip.
**HTML**:
```html
<section class="topic-card topic-card--news">
  <header class="topic-card__source"><code>https://example.com/article</code></header>
  <h2 class="topic-card__title">新闻标题示例</h2>
  <p class="topic-card__abstract">文章摘要 200 字...</p>
  <ul class="signal-chips">
    <li class="signal-chip"><svg><use href="../icons/system.svg#icon-signal"/></svg>新信号: 高效协作</li>
  </ul>
</section>
```

---

## Task 28 — Topic Card Lite / bilibili video

**Input**: `07_topic-card-lite/task-28_bilibili-video.png`
**Output**: same file, `<section class="topic-card topic-card--video">`
**Image content**: bilibili video variant: thumbnail placeholder + duration overlay + uploader chip + 3 signal chips + capture_id mono.
**HTML**: same skeleton with `<figure class="video-thumb">` + `<span class="video-thumb__duration">12:34</span>`.

---

## Task 29 — Topic Card Lite / multi signal

**Input**: `07_topic-card-lite/task-29_multi-signal.png`
**Output**: same file, `<section class="topic-card topic-card--multi-signal">`
**Image content**: card with 5+ signal chips wrapping multiple rows, each with different accent (live / focus / success).
**HTML**: same `<ul class="signal-chips">` but more `<li>` items with state-modifier classes.

---

## Task 30 — Topic Card Lite / evidence pointers

**Input**: `07_topic-card-lite/task-30_evidence-pointers.png`
**Output**: same file, `<section class="topic-card topic-card--evidence">`
**Image content**: card with evidence pointer arrows linking abstract text to trust-trace evidence rows. Inline mono `<code>` chips next to highlighted abstract phrases.
**HTML**: `<p class="topic-card__abstract">文章摘要 ... <a class="evidence-link" href="#evidence-3" data-trace-id="3">⮕</a> ...</p>`.

---

## Task 31 — Topic Card Lite / dual card compare

**Input**: `07_topic-card-lite/task-31_dual-card-compare.png`
**Output**: same file, `<section class="topic-card-compare">`
**Image content**: 2 topic cards side by side, divider between, similar/diff signals highlighted.
**HTML**: `<section class="topic-card-compare"><article class="topic-card">...</article><aside class="compare-divider">VS</aside><article class="topic-card">...</article></section>`.

---

## Task 32 — Topic Card Vault / default

**Input**: `08_topic-card-vault/task-32_default.png`
**Output**: `html5-rough/08-topic-card-vault.html` → `<section class="topic-card-vault topic-card-vault--default">`
**Image content**: vault list view, ~5 topic cards stacked vertically with full metadata, search/filter bar top.
**HTML**: `<header class="vault-toolbar"><input type="search"/><select class="filter-select">...</select></header>` + `<section class="vault-list">` containing 5 `<article class="topic-card">`.

---

## Task 33 — Topic Card Vault / source url aggregate

**Input**: `08_topic-card-vault/task-33_source-url-aggregate.png`
**Output**: same file, `<section class="topic-card-vault topic-card-vault--aggregated">`
**Image content**: cards grouped by source domain, each group shows total count, expandable.
**HTML**: `<details class="domain-group" open><summary class="domain-summary"><code>bilibili.com</code><span class="count">12 captures</span></summary>...</details>`.

---

## Task 34 — Topic Card Vault / promote readiness

**Input**: `08_topic-card-vault/task-34_promote-readiness.png`
**Output**: same file, `<section class="topic-card-vault topic-card-vault--promote">`
**Image content**: card with promote-readiness gate: 4 criteria checkboxes (signals ≥ 3 / hypotheses ≥ 1 / evidence linked / user-marked-useful), all green = "可晋升 DiloFlow" button enabled.
**HTML**: `<section class="promote-gate"><h3>晋升 DiloFlow 准备度</h3><ul class="gate-criteria"><li class="gate-item gate-item--met"><svg><use href="../icons/state.svg#icon-success"/></svg>信号 ≥ 3</li>...</ul><button class="btn btn--primary">晋升 DiloFlow</button></section>`.

---

## Task 35 — Topic Card Vault / promote diloflow modal

**Input**: `08_topic-card-vault/task-35_promote-diloflow-modal.png`
**Output**: same file, `<section class="topic-card-vault topic-card-vault--promote-modal">`
**Image content**: modal asking user to confirm DiloFlow promotion with summary of what gets transferred.
**HTML**: `<dialog class="modal modal--promote" open>...</dialog>` with confirmation summary.

---

## Task 36 — Topic Card Vault / obsidian sync status

**Input**: `08_topic-card-vault/task-36_obsidian-sync-status.png`
**Output**: same file, `<section class="topic-card-vault topic-card-vault--sync">`
**Image content**: 3-tier sync badge demo: success（已同步）/ warn（待同步）/ focus（外部已改）. Each card shows current sync state via badge.
**HTML**:
```html
<section class="topic-card-vault topic-card-vault--sync">
  <article class="topic-card">
    ...
    <aside class="sync-badge sync-badge--synced">
      <svg><use href="../icons/state.svg#icon-success"/></svg>已同步
    </aside>
  </article>
  <article class="topic-card">
    ...
    <aside class="sync-badge sync-badge--pending">
      <svg><use href="../icons/state.svg#icon-warning"/></svg>待同步
    </aside>
  </article>
  <article class="topic-card">
    ...
    <aside class="sync-badge sync-badge--external-changed">
      <svg><use href="../icons/state.svg#icon-focus"/></svg>外部已改
    </aside>
  </article>
</section>
```
**CSS**: `sync-badge.module.css` extracted as candidate (3 modifier states), used in cross-system surfaces.

---

## Task 37 — Signal/Hypothesis IA / signal expanded

**Input**: `09_signal-hypothesis-ia/task-37_signal-expanded-with-hypotheses.png`
**Output**: `html5-rough/09-signal-hypothesis.html` → `<section class="signal-ia signal-ia--expanded">`
**Image content**: signal card expanded showing 3 child hypotheses with confidence% mono values, parent-child indented.
**HTML**: `<details class="signal-card" open><summary>...</summary><ol class="hypothesis-list"><li>...</li></ol></details>`.

---

## Task 38 — Signal/Hypothesis IA / hypothesis compare

**Input**: `09_signal-hypothesis-ia/task-38_hypothesis-compare.png`
**Output**: same file, `<section class="signal-ia signal-ia--compare">`
**Image content**: 2 hypotheses compared, confidence% bars, supporting/conflicting evidence linked from each.
**HTML**: `<table class="hypothesis-compare-table">` with confidence bars and evidence link cells.

---

## Task 39 — Signal/Hypothesis IA / signal lifecycle stepper

**Input**: `09_signal-hypothesis-ia/task-39_signal-lifecycle-stepper.png`
**Output**: same file, `<section class="signal-ia signal-ia--lifecycle">`
**Image content**: 4-step stepper for signal lifecycle (raw / verified / hypothesis-formed / promoted), current step accent_live.
**HTML**: same `<ol class="lifecycle-stepper">` pattern as capture-scope, reused.

---

## Task 40 — Capture Plan IA / plan io contract

**Input**: `10_capture-plan-ia/task-40_plan-io-contract.png`
**Output**: `html5-rough/10-capture-plan.html` → `<section class="capture-plan capture-plan--io">`
**Image content**: I/O contract block showing input fields (URL / scope / overrides), expected outputs (markdown / frontmatter / preview), all in mono.
**HTML**: `<dl class="io-contract">` with `<dt>` inputs, `<dt>` outputs sections.

---

## Task 41 — Capture Plan IA / plan dry run

**Input**: `10_capture-plan-ia/task-41_plan-dry-run.png`
**Output**: same file, `<section class="capture-plan capture-plan--dry-run">`
**Image content**: plan executing dry-run, automation-layer hooks visible (test signals / validation checkpoints), accent_live progress.
**HTML**: `<ul class="automation-hooks">` with hook items showing pass/pending state.

---

## Task 42 — Capture Plan IA / plan execution log

**Input**: `10_capture-plan-ia/task-42_plan-execution-log.png`
**Output**: same file, `<section class="capture-plan capture-plan--log">`
**Image content**: 5-row mono log: run summary 6m23s + 12 capture + 14 topic card + 1 error + final status.
**HTML**: `<table class="execution-log">` with mono cells, error row highlighted.

---

## Task 43 — Density Spec reference

**Input**: `11_density-spec/task-43_density-compact-baseline.png`
**Output**: `html5-rough/11-density-spec.html` → reference page only (not used by PF-C4 in production, but documents the chosen density baseline)
**Image content**: same as Task 00 master shell but in V3 Compact density (12 metadata fields / 5+sub-state stepper / 8 evidence rows + inline dom-path).
**HTML**: full app-shell composition but with `data-density="compact"` attribute on `<main>`. CSS variables `--type-title: 18px; --type-body: 13px; --space-md: 12px; --space-sm: 8px;` overridden in `density-compact.css`.
**Output also**: `density-compact.css` with the variable overrides — PF-C4 imports this when density toggle is set.

---

## Task 44 — Type Spec reference

**Input**: `12_type-spec/task-44_type-weight-heavy.png`
**Output**: `html5-rough/12-type-spec.html` → reference page documenting the weight-heavy typography baseline
**Image content**: same as Task 00 but with V4 Weight Heavy (hero 28/800 / title 20/700 / body 14/400 / mono 13/500).
**HTML**: app-shell with `data-type="weight-heavy"` attribute. CSS `--font-weight-hero: 800; --font-weight-title: 700;` overrides in `type-weight-heavy.css`.

---

## Tasks 45-54 — Icons system (S15 V1-V10)

For each icon, draw clean line geometry as `<symbol id="icon-{name}" viewBox="0 0 256 256">` inside `icons/system.svg`. All `stroke="currentColor"` `stroke-width="1.5"` `fill="none"` (unless structurally required).

| Task | Input file | Symbol id | Geometry hint |
|---|---|---|---|
| 45 | `13_icons-system/task-45_icon-capture.png` | `icon-capture` | inbox tray + arrow pointing in |
| 46 | `13_icons-system/task-46_icon-preview.png` | `icon-preview` | eye outline (no pupil) |
| 47 | `13_icons-system/task-47_icon-commit.png` | `icon-commit` | document with corner fold + checkmark |
| 48 | `13_icons-system/task-48_icon-dry-run.png` | `icon-dry-run` | document with magnifier overlay |
| 49 | `13_icons-system/task-49_icon-blocked.png` | `icon-blocked` | padlock body with X overlay |
| 50 | `13_icons-system/task-50_icon-signal.png` | `icon-signal` | radar concentric 3 rings + center dot |
| 51 | `13_icons-system/task-51_icon-hypothesis.png` | `icon-hypothesis` | hexagonal lightbulb (geometric, no rays) |
| 52 | `13_icons-system/task-52_icon-plan.png` | `icon-plan` | clipboard with numbered rows |
| 53 | `13_icons-system/task-53_icon-trace.png` | `icon-trace` | 3-node graph (parent + 2 children) |
| 54 | `13_icons-system/task-54_icon-evidence.png` | `icon-evidence` | 3 papers stacked with corner fold |

Each ≤ 20 path commands. If complex geometry would exceed, simplify.

---

## Tasks 55-64 — Icons state (S16 V1-V10)

Same rules as system icons, but for `icons/state.svg`. Use semantic accent colors via `currentColor` so consumer can override per-state.

| Task | Input file | Symbol id | Geometry hint |
|---|---|---|---|
| 55 | `14_icons-state/task-55_icon-state-live.png` | `icon-live` | radar circle + rotation arrow + center dot |
| 56 | `14_icons-state/task-56_icon-state-success.png` | `icon-success` | ring + thin checkmark |
| 57 | `14_icons-state/task-57_icon-state-warning.png` | `icon-warning` | triangle + exclamation |
| 58 | `14_icons-state/task-58_icon-state-error.png` | `icon-error` | ring + X |
| 59 | `14_icons-state/task-59_icon-state-blocked.png` | `icon-blocked` | circle + slash (action denied) |
| 60 | `14_icons-state/task-60_icon-state-locked.png` | `icon-locked` | full padlock body |
| 61 | `14_icons-state/task-61_icon-state-focus.png` | `icon-focus` | viewfinder corner brackets + crosshair + center dot |
| 62 | `14_icons-state/task-62_icon-state-loading.png` | `icon-loading` | 3 dots progressive size (small / large / small) |
| 63 | `14_icons-state/task-63_icon-state-empty.png` | `icon-empty` | dashed circle |
| 64 | `14_icons-state/task-64_icon-state-ready.png` | `icon-ready` | ring + bold checkmark (thicker stroke than success) |

Note: `icon-blocked` exists in both system.svg (id `icon-blocked`, geometry: padlock+X) and state.svg (id `icon-blocked`, geometry: circle+slash). They are distinct semantic — system icon = "this action is blocked"; state icon = "this entity is blocked". Document this in MAPPING.md.

---

# § 10  Output ZIP structure (HARD contract — must produce exactly this)

You MUST deliver ONE downloadable ZIP archive named `PF-V-P7-output.zip` (use canvas / code-interpreter / artifact / file-attached — pick whichever is supported by your runtime). The ZIP root must contain MULTIPLE FOLDERS (not a flat dump) AND TWO INDEX FILES (`MAPPING.md` + `README.md`).

**Folder requirements (all 4 must exist at ZIP root)**:
1. `html5-rough/` — exactly 13 `*.html` files (one per surface group: 00-app-shell, 01-url-bar, ..., 12-type-spec)
2. `css-modules-candidate/` — pairs of `*.module.css` + `*.html` snippet for each extracted component (estimate ~15 components × 2 files = ~30 files)
3. `icons/` — exactly 2 SVG sprite files: `system.svg` (10 `<symbol>`) and `state.svg` (10 `<symbol>`)
4. ROOT level files: `tokens.css` + `density-compact.css` + `type-weight-heavy.css` + `MAPPING.md` + `README.md`

**Two index files (HARD — cannot omit either)**:

`MAPPING.md` (required schema):
```markdown
# P7 Output Mapping — Input Image → Output File(s)

| Task ID | Input image (in pfv-p7-bundle.zip) | Output file(s) | Notes |
|---|---|---|---|
| 00 | `00_app-shell/task-00_master.png` | `html5-rough/00-app-shell.html` | Full 4-panel composition |
| 01 | `01_url-bar/task-01_state-empty.png` | `html5-rough/01-url-bar.html` § `.url-bar--empty` | First state class in URL Bar surface |
| 02 | `01_url-bar/task-02_state-focus.png` | `html5-rough/01-url-bar.html` § `.url-bar--focus` | Adds focus glow |
| ... | ... | ... | ... |
| 64 | `14_icons-state/task-64_icon-state-ready.png` | `icons/state.svg` § `<symbol id="icon-ready">` | Bold checkmark |

# Component extraction map

| Component | Source surfaces (where reused) | Files |
|---|---|---|
| panel-card | 02, 03, 04, 05 (4 surfaces) | `css-modules-candidate/panel-card.{module.css, html}` |
| state-badge | 03, 05, 06, 08 | `css-modules-candidate/state-badge.{module.css, html}` |
| ... | ... | ... |
```

Every one of the 65 input images MUST appear at least once in the input column. Every output file MUST appear at least once in the output column.

`README.md` (required schema):
```markdown
# PF-V P7 Output — Rough HTML5 Wireframe Bundle

This bundle was generated from 65 ScoutFlow visual mockups by GPT Pro batch image-to-HTML5 conversion.

## Quick start (zero-install consumption)
1. Unzip into any directory
2. Open any `html5-rough/*.html` in a browser to verify structure
3. Inspect `tokens.css` for the design system source of truth

## Files
- `tokens.css` — single source of truth for all design tokens (15 colors + typography + spacing + radius + shadow + state-bg)
- `density-compact.css` — CSS variable override for V3 Compact density
- `type-weight-heavy.css` — CSS variable override for V4 Weight Heavy typography
- `html5-rough/*.html` — 13 surface wireframes
- `css-modules-candidate/*.module.css` + `*.html` — extracted reusable components
- `icons/system.svg` — 10 system action icons (capture, preview, commit, ...)
- `icons/state.svg` — 10 state indicator icons (live, success, warning, ...)
- `MAPPING.md` — input → output cross-reference
- `README.md` — this file

## How PF-C4 should consume
1. Read each `html5-rough/*.html` to understand IA + state class semantics
2. Translate to React TSX with conventions chosen by PF-C4 lane
3. Import `tokens.css` as global CSS Variables
4. Convert `*.module.css` to actual CSS Modules in component folders
5. Replace TODO placeholders with real implementations (graph library, data wiring, thumbnail fetch)
6. Test responsive via container queries

## Known TODO placeholders (for PF-C4 attention)
[List every `<!-- TODO: ... -->` placeholder by file + line, with reason]

## What NOT to do
- DO NOT import raw HTML at runtime (wireframe only)
- DO NOT use any class name verbatim (translate via React/CSS Module conventions)
- DO NOT hardcode hex outside tokens.css
- DO NOT use Tailwind / shadcn — zero-install policy
```

The ZIP root tree must look exactly like this:

```
PF-V-P7-output.zip
├── tokens.css
├── html5-rough/
│   ├── 00-app-shell.html
│   ├── 01-url-bar.html
│   ├── 02-live-metadata.html
│   ├── 03-capture-scope.html
│   ├── 04-trust-trace.html
│   ├── 05-vault-preview.html
│   ├── 06-vault-commit.html
│   ├── 07-topic-card-lite.html
│   ├── 08-topic-card-vault.html
│   ├── 09-signal-hypothesis.html
│   ├── 10-capture-plan.html
│   ├── 11-density-spec.html
│   └── 12-type-spec.html
├── density-compact.css
├── type-weight-heavy.css
├── css-modules-candidate/
│   ├── panel-card.module.css
│   ├── panel-card.html
│   ├── url-input.module.css
│   ├── url-input.html
│   ├── state-badge.module.css
│   ├── state-badge.html
│   ├── lifecycle-stepper.module.css
│   ├── lifecycle-stepper.html
│   ├── evidence-table.module.css
│   ├── evidence-table.html
│   ├── tag-list.module.css
│   ├── tag-list.html
│   ├── capture-id-chip.module.css
│   ├── capture-id-chip.html
│   ├── topic-card.module.css
│   ├── topic-card.html
│   ├── sync-badge.module.css
│   ├── sync-badge.html
│   ├── modal.module.css
│   ├── modal.html
│   ├── governance-tooltip.module.css
│   ├── governance-tooltip.html
│   ├── live-pulse.module.css
│   ├── live-pulse.html
│   ├── btn.module.css
│   ├── btn.html
│   ├── frontmatter-block.module.css
│   ├── frontmatter-block.html
│   ├── promote-gate.module.css
│   └── promote-gate.html
├── icons/
│   ├── system.svg
│   └── state.svg
├── MAPPING.md
└── README.md
```

# § 11  Iteration protocol (if some tasks fail)

If a particular task's output fails the quality contract:
1. DO NOT regenerate the whole bundle
2. Identify failing task IDs (e.g., "Task 14, 15, 19 produce dirty SVG / Tailwind class leak")
3. CC0 will write a delta prompt referencing only those task IDs
4. Re-run with delta prompt; replace only those output files

Common fail patterns to watch for:
- Decorative `<div>` proliferation → "Replace decorative `<div>` with semantic tag"
- Inline hex values → "Replace with `var(--token-name)` reference"
- Tailwind classes leaking in → "Remove all utility classes; use BEM-lite class names only"
- Auto-vectorized icons (50+ path commands) → "Redraw with ≤ 20 path commands or leave TODO placeholder"
- Mixed language UI (English leaking in) → "All UI text 简体中文; only URL/ID/path/code English"

# § 12  Final delivery checklist

Before zipping the output:
- [ ] `tokens.css` defines all 15 colors + typography + spacing + radius + shadow
- [ ] 13 surface HTML files exist
- [ ] 2 reference HTML files (density / type spec) exist + their override CSS
- [ ] ~30 component module files (`*.module.css` + `*.html`) extracted
- [ ] `icons/system.svg` has 10 `<symbol>` definitions
- [ ] `icons/state.svg` has 10 `<symbol>` definitions
- [ ] `MAPPING.md` references every 65 input image
- [ ] `README.md` explains zero-install consumption + how to translate to React TSX
- [ ] All HTML opens in browser without console errors
- [ ] Self-verification (§ 8) passes for every file

Total expected: ~75-85 files, ~6000-9000 lines of code.

This is "rough HTML5" — wireframe quality. Production polish is downstream PF-C4's responsibility.

===END PF-V P7 BATCH PROMPT v2===
```

---

# Notes for human operator

## Why 65 tasks (not 50)

Original v1 plan was 50 images, but skipping mobile/tablet/state-matrix/lifecycle (LESSONS L5 + L9) freed budget that we redirected to: full 20-icon coverage (10+10 instead of 5+5) + 2 spec reference pages. PF-C4 gets a complete icon library zero-derive.

## Why density/type spec gets HTML pages (Tasks 43-44)

These don't change the IA — they only override CSS variables. Generating standalone reference pages lets PF-C4 toggle density/type baseline by importing one CSS override file (`density-compact.css` / `type-weight-heavy.css`) without touching HTML structure. This is the "二维矩阵正交叠加" approach from LESSONS L11.

## Why icons get 2 separate sprite files

`system.svg` = action/concept icons (capture / preview / commit etc, used in buttons + section labels)
`state.svg` = status indicators (live / success / blocked / loading etc, used inline next to states)

Separate sprites because PF-C4 may load only the sprite needed per surface (lazy-load icon library). Single combined sprite would force loading 20 symbols when only 5 needed.

## Why the `icon-blocked` collision is intentional

Both system.svg and state.svg have an `icon-blocked` symbol but with different geometry. System version (padlock+X) means "this action you're trying is blocked"; state version (circle+slash) means "this entity's state is blocked". MAPPING.md documents this so PF-C4 picks the right one per usage.

## ZIP size estimate

50 images @ ~1MB each + 15 icons @ ~900KB each = ~63MB original. After `pngquant -Q 85-95` optimization: ~25-30MB. Should fit ChatGPT Pro upload (50MB limit).

If still too large, fallback: split into 2 ZIP (35-task batch 1 / 30-task batch 2), or upload original PNGs in 2 messages.

## Expected output size

- 13 HTML × ~150 lines = ~2K lines
- 30 CSS module pairs × ~30 lines avg = ~900 lines
- tokens.css = ~50 lines
- 2 SVG sprites × ~20 symbols × ~15 lines = ~600 lines
- MAPPING.md + README.md = ~300 lines
- Total = ~3.85K lines, ~6-9K with all comments and snippets

GPT Pro thinking mode 1-1.5 hours. Cost ≈ included in Pro subscription.

## Post-P7 consumption by PF-C4

PF-C4-01 lane unzips P7 output into `apps/capture-station/src/p7-reference/` (or similar staging dir). Then per surface:
1. Read the `.html` to understand IA + state class structure
2. Translate to React TSX with one component per surface (or split if > 200 lines)
3. Import `tokens.css` as global, copy `*.module.css` to component folder as actual CSS Module
4. Replace TODO placeholders with real implementations (graph library / actual data wiring)
5. Test responsive via container queries

PF-C4 NEVER imports the raw HTML at runtime — it's reference material only. Final React TSX is fresh code informed by the wireframe.

---

# P8 Handoff Backlog (deferred from CC1 audit 2026-05-07)

The following items were evaluated during P7 prompt v2 finalization and **deferred to P8 handoff PR notes** rather than embedded in P7. They surface candidate reference material that PF-C4 lane MAY consume during implementation; none are required for P7 output to be valid.

| # | Reference source | What PF-C4 may use it for | Authority |
|---|---|---|---|
| 1 | `outputs/U7-state-library/MODULE-state-library-spec.md` + `8-PANEL-STATE-INVENTORY.md` | 48-state matrix with `props_json` schema — when translating P7 HTML state classes to React TSX component props interfaces, U7 provides candidate `props_json` per state. | candidate / not-authority |
| 2 | `outputs/U4-visual-asset/MODULE-visual-asset-spec.md` | SQLite `visual_asset` schema + 5-state lifecycle (gen / candidate / refined / locked / deprecated). PF-C4 may decide whether to register PF-V images as `visual_asset` rows or keep INDEX.csv as-is. | candidate / not-authority |
| 3 | `outputs/U4-visual-asset/PF-V-INTEGRATION-MAP.md` | Migration plan: PF-V `INDEX.csv` 19 columns → `visual_asset` table. Only relevant if PF-C4 chooses to land the SQLite schema. | candidate / not-authority |
| 4 | `outputs/U8-egress/HANDOFF-MANIFEST-JSON-SCHEMA.md` | 4 downstream-variant manifest schemas. P8 PR description may reference one variant when packaging the handoff bundle. | candidate / not-authority |
| 5 | `outputs/U13-visual-brand/05-panel-design-spec/PANEL-01.md ~ PANEL-08.md` | 6-state grammar (idle / loading / ready / candidate / blocked / stale) + good-vs-bad examples per panel. PF-C4 may cross-validate state class naming if React component naming wants to align. | candidate / not-authority — also has 30-40% audit-expansion boilerplate per CC1 audit; clean before consuming |

**P8 handoff PR description template** (when CC0 writes the actual P8 PR):

```markdown
## P8 — PF-V Handoff to PF-C4-01 Local Frontend Bootstrap

This PR delivers the complete PF-V visual prototype bundle: 152 mockup images
+ INDEX.csv (152 rows) + P7 rough HTML5 output + handoff protocol doc.

### What PF-C4 should consume directly
- `p7-output/html5-rough/*.html` — 13 surface wireframes
- `p7-output/tokens.css` — design tokens (single source of truth)
- `p7-output/icons/*.svg` — 2 SVG sprites
- `p7-output/MAPPING.md` — image → output cross-reference

### What PF-C4 may optionally consume (candidate references)
[insert P8 Handoff Backlog table from 03-P7-batch-prompt-v2.md]

### What PF-C4 should NEVER do
- Import raw HTML at runtime (it's wireframe only)
- Use any P7 CSS class verbatim in production (translate via React conventions)
- Hardcode hex outside tokens.css
```

These deferred items were selected from CC1's parallel audit work on 16 GPT Pro
overnight cloud outputs. PF-V (this lane) chose to keep S00-S18 mockup-derived
master context as authoritative source for tokens/icons/state grammar. The U7/U4/U8/U13
references are candidate cross-validation material — PF-C4 lane decides post-handoff
whether to adopt, ignore, or partially port.

Reject rationale (why not folded into P7 directly):
- U13 token namespace replacement (sf.canvas.0 / sf.panel.bg / sf.text.primary) would
  diverge from the 152 mockups already generated using the underscore namespace
  (bg_canvas / surface_base / text_primary). H5 colors would visually drift from the
  image bundle; PF-C4 verification against mockups would fail.
- U13 60 SVG candidate paths conflict with PF-V P5 winners (S15/S16) which were
  user-verdicted V-PASS with TOP1/TOP2/TOP3 explicit ranking.
- U7 props_json schema would require duplicating state descriptions already implicit
  in P7 task specs; the value lands when PF-C4 translates HTML to React TSX, not earlier.
