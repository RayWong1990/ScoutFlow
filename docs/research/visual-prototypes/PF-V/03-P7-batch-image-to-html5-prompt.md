---
title: PF-V P7 — Batch Image-to-HTML5 Prompt (single GPT Pro session, 50-image bundle)
status: candidate / batch_conversion_prompt / not-authority / not-implementation-approval
created_at: 2026-05-06
purpose: After P0-P6 complete, pack 50 V-PASS images and convert to N HTML5 + 2N component files in one GPT Pro session
target: GPT Pro web (云端，token unlimited per user statement)
---

# How to use this file

1. After S00-S18 complete and INDEX.csv has ≥ 12-15 V-PASS images covering critical surfaces, you're ready for P7.
2. Open a NEW GPT Pro session.
3. Paste `00-master-context.md` first.
4. Upload (drag/drop) up to 50 V-PASS images selected per the bundle plan below.
5. Paste the **P7 PROMPT** from this file (the fenced block).
6. GPT Pro outputs a structured zip (or chat-attached files) with:
   - `html5-rough/*.html` — N surface files
   - `css-modules-candidate/*.module.css` — 2N component candidates
   - `icons-svg/*.svg` — extracted icons
   - `MAPPING.md` — image → file output map
7. Download, unzip into `docs/research/visual-prototypes/PF-V/`.

---

# Bundle plan (which 50 images to upload)

Selection rule: **1-3 V-PASS variants per surface** + **1-2 icon grids**. Total ~50.

| Surface | Suggested image count | Source sessions |
|---|---|---|
| Capture-station 4-panel desktop | 3 (default + filled + error) | S00, S01 |
| Capture-station mobile | 2 (default + scroll state) | S02 |
| Capture-station tablet | 2 (default + drawer expanded) | S03 |
| URL Bar component | 4 (empty / pasted / error / success) | S04 |
| Live Metadata Panel | 3 (long content + sparse + tags overflow) | S05 |
| Capture Scope Panel | 3 (default + blocked-tooltip + stepper) | S06 |
| Trust Trace Graph | 3 (default + filtered + selected-node) | S07 |
| Vault Preview Panel | 4 (idle / ready / blocked / diff) | S08 |
| Vault Commit Dry-Run | 3 (button + modal-pass + modal-fail) | S09 |
| Topic Card Lite | 3 (default + signals + tags-overflow) | S10 |
| Topic Card Vault | 3 (list + filter + edit) | S11 |
| Signal-Hypothesis IA | 2 | S12 |
| Capture-Plan IA | 2 | S12 |
| State matrix grid | 3 | S13 |
| Lifecycle flow | 2 | S14 |
| System icons grid | 1 | S15 |
| State icons grid | 1 | S16 |
| Refinement winners | 2 | S17, S18 |
| **TOTAL** | **~46** | (slack room for 4 more if needed) |

If your INDEX.csv shows a surface lacks V-PASS, skip it for P7 (don't generate H5 from V-CONCERN images — they'll produce flawed wireframes).

---

# P7 PROMPT (paste this whole block after uploading bundle)

```
===BEGIN PF-V P7 BATCH PROMPT===

# Task

You are converting a bundle of ~50 ScoutFlow visual mockup images into a downstream-consumable rough HTML5 wireframe set, plus extracted CSS Modules candidates and SVG icons. The downstream lane (PF-C4-01 Local Frontend Bootstrap) will translate your output to React TSX in `apps/capture-station/`.

# Three-step pipeline (apply to entire bundle)

## Step 1 — Decompose (intermediate UI structural model)

Before writing any HTML, produce a JSON UI structural model for each surface:

For each surface (group images by surface — see MAPPING below), output:

```json
{
  "surface_id": "capture-station-desktop",
  "source_images": ["img-S00-01.png", "img-S01-03.png"],
  "viewport": "1920x1080",
  "ia": {
    "type": "shell-with-panels",
    "regions": [
      { "id": "url-bar", "role": "input-primary", "position": "top-full-width" },
      { "id": "live-metadata", "role": "panel-evidence", "position": "lower-left" },
      { "id": "capture-scope", "role": "panel-state", "position": "lower-middle" },
      { "id": "trust-trace", "role": "panel-graph", "position": "lower-right-wide" }
    ]
  },
  "elements": [
    {
      "id": "url-input",
      "tag": "input",
      "type": "url",
      "placeholder": "粘贴一个 URL 或拖入文件",
      "tokens": ["surface_muted", "border_soft", "text_primary"],
      "states": ["empty", "focus", "filled", "error"]
    },
    {
      "id": "capture-button",
      "tag": "button",
      "label": "Create capture",
      "tokens": ["accent_live", "text_primary"],
      "disabled_when": "url_input.empty"
    },
    ...
  ],
  "components_extracted": [
    { "name": "url-bar", "reuse_count": 1 },
    { "name": "panel-card", "reuse_count": 4, "reason": "appears in metadata/scope/trace/preview" },
    { "name": "capture-id-chip", "reuse_count": 6 }
  ],
  "icons_referenced": ["capture", "preview", "blocked", "live"]
}
```

Surface this model in plain text BEFORE generating HTML. This intermediate model is your self-check — if a surface's IA can't be cleanly decomposed, regenerate the model before HTML.

## Step 2 — Generate per-surface HTML5

For each surface, write one `*.html` file. Rules:

### Semantic markup (hard contract)
- `<main>` for the shell, `<header>` for URL Bar region, `<aside>` for sidebar (if present), `<section>` for each panel
- Headings: `<h1>` for surface title, `<h2>` for panel titles
- Text: `<p>` for body, `<code>` for IDs/URLs/timestamps (inline mono treatment)
- Tables: `<table><thead><tbody>` not `<div>` grids when rendering tabular metadata
- Lists: `<ul>` for tag chips, `<ol>` for ordered steppers
- Buttons: `<button>` not `<div role="button">`
- NO `<div>` wrappers without semantic purpose. If you can't justify a wrapper, remove it.

### CSS rules (hard contract)
- Single linked stylesheet per HTML: `<link rel="stylesheet" href="./{surface_id}.module.css">`
- `class` naming: BEM-lite — `block__element--modifier` (lower-kebab)
- NO Tailwind. NO utility classes. NO inline `style="..."` attributes (with the single exception of CSS Variable definitions on `<html>` if needed for demo)
- NO hardcoded hex values in CSS files. ALL color, spacing, typography MUST be `var(--token-name)`
- Token CSS Variables defined ONCE in a shared `tokens.css` file (you generate this once, reference from all surface CSS)

### Interactivity
- NO JavaScript inline in HTML
- States visualized via CSS class modifiers (`.button--disabled`, `.input--focus`, `.input--error`)
- For state demos: render the surface in 2-4 state variants per HTML file (e.g., `<section class="state-demo state-demo--idle">...<section class="state-demo state-demo--loading">...`)

### Image / icon handling (per the user's PPT-prompt-derived principle)
- Icons → INLINE `<svg>` element, stroke 1.5px, `var(--accent-live)` default
- Decorative photos (if any) → `<img src="./assets/{name}.png" alt="...">` (PNG retained)
- Logo placeholders → `<svg>` geometric, never raster
- Background gradients (if absolutely necessary) → CSS `linear-gradient()` using tokens, but prefer flat surfaces
- NO base64 images embedded
- NO automatic raster→SVG dirty paths (if a logo or complex graphic can't be cleanly drawn as SVG, leave a `<img>` PNG placeholder with TODO comment)

### Responsive
- Use `@container` queries (container queries) preferred, `@media` queries as fallback
- Breakpoints: container width 768px (tablet), 1280px (desktop). Below 768px = mobile linearized.
- Mobile layout: vertical stack of all panels in IA order
- Tablet: 2-column [Metadata + Scope stacked left | Trust Trace right] with URL Bar full width
- Desktop: 3-column with Trust Trace widest

## Step 3 — Extract reusable components

Any element that appears in 2+ surfaces with similar structure → extract as a `*.module.css` candidate.

For each extracted component, write:
- `css-modules-candidate/{component_name}.module.css` — the styles
- `css-modules-candidate/{component_name}.html` — a usage example snippet (NOT a full page, just the markup pattern)

Expected ~2N components for N surfaces (each surface contributes ~2 reusable patterns on average).

Examples of likely extracted components:
- `panel-card.module.css` (the dark-cool panel container with border + shadow)
- `capture-id-chip.module.css` (mono ID chip with copy affordance)
- `state-badge.module.css` (state semantic badges: live/blocked/loading)
- `url-input.module.css` (the URL input with all 5 states)
- `mono-meta-row.module.css` (label-value rows with mono values)
- `dry-run-button.module.css` (write_enabled=false visualization button)
- `topic-card-frame.module.css` (3-section topic card structure)

# Output structure (deliver as zip OR as chat-attached files)

```
PF-V-P7-output/
├── tokens.css                         # CSS Variables for all 15 tokens
├── html5-rough/
│   ├── capture-station-desktop.html
│   ├── capture-station-mobile.html
│   ├── capture-station-tablet.html
│   ├── url-bar-states.html            # Multi-state demo file
│   ├── live-metadata.html
│   ├── capture-scope.html
│   ├── trust-trace.html
│   ├── vault-preview.html
│   ├── vault-commit-dry-run.html
│   ├── topic-card-lite.html
│   ├── topic-card-vault.html
│   ├── signal-hypothesis-ia.html
│   ├── capture-plan-ia.html
│   ├── state-matrix.html
│   └── lifecycle-flow.html
├── css-modules-candidate/
│   ├── panel-card.module.css
│   ├── panel-card.html               # Usage snippet
│   ├── capture-id-chip.module.css
│   ├── capture-id-chip.html
│   ├── url-input.module.css
│   ├── url-input.html
│   ├── state-badge.module.css
│   ├── state-badge.html
│   ├── ... (~30 component files = 15 components × 2 files each)
├── icons-svg/
│   ├── capture.svg
│   ├── preview.svg
│   ├── commit.svg
│   ├── dry-run.svg
│   ├── blocked.svg
│   ├── signal.svg
│   ├── hypothesis.svg
│   ├── plan.svg
│   ├── trace.svg
│   ├── evidence.svg
│   ├── live.svg
│   ├── success.svg
│   ├── warning.svg
│   ├── focus.svg
│   ├── locked.svg
│   ├── loading.svg
│   ├── error.svg
│   ├── empty.svg
│   ├── ready.svg
│   └── (~20 icons total)
├── MAPPING.md                          # image filename → output file map
└── README.md                          # P7 output overview + how to consume
```

# Quality contract (every output file must satisfy)

For each `.html` file:
- [ ] Valid HTML5 (passes W3C validator semantic check)
- [ ] Semantic tags only (<main>, <section>, <header>, <nav>, <aside>, <h1>-<h3>, <p>, <ul>, <table>, <button>)
- [ ] No `<div>` without justification
- [ ] No inline `style=` (except `<html style="...">` for CSS Variable demo if needed)
- [ ] Single `<link>` to its `.module.css`
- [ ] All visible text is real (not lorem ipsum) and matches mockup image
- [ ] Mono text in `<code>` tags
- [ ] Icons are inline `<svg>` (not `<img>`)
- [ ] State variants demonstrated as CSS class modifiers
- [ ] Container queries for responsive (or @media as fallback)

For each `.module.css` file:
- [ ] All values are `var(--token-name)` — zero hardcoded hex / px sizes outside the 8px grid
- [ ] BEM-lite class naming
- [ ] No Tailwind / shadcn / utility classes
- [ ] States as `&--modifier` (or `.block--modifier` if not nested syntax)

For each `.svg` icon:
- [ ] viewBox `0 0 256 256`
- [ ] Stroke 1.5px (`stroke-width="1.5"`)
- [ ] `stroke="var(--accent-live)"` or appropriate semantic accent
- [ ] No fill except where structurally necessary
- [ ] Clean geometry (≤ 20 path commands per icon — if you exceed this, the icon is too complex; redraw simpler)
- [ ] No gradients, no filters, no clip paths beyond the absolutely necessary

For `tokens.css`:
- [ ] All 15 color tokens as CSS Variables on `:root`
- [ ] Typography family + size + line-height tokens
- [ ] Spacing tokens (--space-xs, --space-sm, --space-md, --space-lg, --space-xl)
- [ ] Radius tokens
- [ ] Shadow tokens

# Trade-off rule (from user's PPT prompt principle, hard)

**保真度 vs 可编辑性 → 优先可编辑性 + 视觉结构保真。**

If a mockup detail (like an exotic gradient, a complex illustration, a photo background) cannot be cleanly represented as semantic HTML + CSS Variables + clean SVG:
- DO NOT mechanically retain it as a noisy auto-vectorized SVG (dirty paths)
- DO NOT embed as base64 inline image
- INSTEAD: leave a TODO comment in the HTML pointing to the original PNG, and use a clean placeholder element

Example:
```html
<!-- TODO: source mockup img-S07-04.png shows a complex graph rendering. 
     Downstream PF-C4 lane should consume the original image as visual reference 
     and implement using a graph library. This is a placeholder. -->
<section class="trust-trace-placeholder">
  <p>Trust Trace graph (visual reference: img-S07-04.png)</p>
</section>
```

This is intentional. PF-C4 lane will consume the image directly as visual reference and implement properly with a graph library.

# Self-verify before delivering

Before finalizing the bundle:
[ ] Every HTML file passes the quality contract above
[ ] Every CSS file uses only CSS Variables
[ ] Every SVG is clean (no dirty paths)
[ ] MAPPING.md cross-references every image to at least one output file
[ ] No file references a token name that doesn't exist in tokens.css
[ ] No file uses a class name not defined in some .module.css
[ ] README.md explains how PF-C4 should consume the bundle

If any check fails, regenerate the failing file with delta correction. Do not deliver flawed bundle.

# Final deliverable summary

Output 1 ZIP file (or attached files) containing:
- 1 tokens.css
- ~15 *.html surface files
- ~30 *.module.css + matching *.html usage snippets (component candidates)
- ~20 *.svg icons
- 1 MAPPING.md
- 1 README.md

Estimated total: ~70-80 files, ~5000-8000 lines of code.

This is "rough HTML5" — wireframe quality. Production polish is downstream.

===END PF-V P7 BATCH PROMPT===
```

---

# Notes for the human operator

## Why we go through an intermediate UI model

Per BESSER/IFML academic research (ICWE 2025), direct image→code is unreliable. Going image→UI structural model (JSON)→deterministic code is more robust. The model layer also gives you a debug surface: if HTML output is wrong, check the JSON model first.

## Why no Tailwind output

Per OpenDesign reuse strategy §5.2, package adoption (Tailwind/shadcn/Panda) is not approved. Output goes to CSS Variables + CSS Modules — fits zero-install policy.

## Why TODO placeholders for complex graphics

Per your PPT prompt principle ("可编辑性优先于像素级复刻"). If gpt-image-2/auto-vectorize would produce dirty SVG paths, leave a clean placeholder + TODO. Downstream lane reads the original mockup and implements properly.

## Why container queries first, media queries as fallback

Container queries are 2024+ standard, supported in all modern browsers. They scope responsive behavior to component context, not viewport — which matches our "panels can rearrange" model better than @media. If a downstream lane has older-browser constraints, they switch to @media.

## Token discipline

The single biggest debt-prevention is "every CSS value is a token reference". This is what enables PF-C4 to swap themes / adjust density / change branding without touching HTML structure.

## How to verify output quality

Open one of the `.html` files in a browser:
```
cd docs/research/visual-prototypes/PF-V/html5-rough/
python3 -m http.server 8080
# open http://localhost:8080/capture-station-desktop.html
```

If it renders recognizably as the target surface (allowing for "rough" quality), it's a good wireframe. If it's broken layout or missing tokens, regen.

## Iteration if output is poor

If P7 output quality is low (anti-patterns leak in / hardcoded hex / incorrect semantic tags):
1. Identify the failing surfaces (check MAPPING.md)
2. Regen ONLY those surfaces with explicit correction in delta prompt
3. Don't regen the whole 50-image bundle

Typical issues to watch for:
- Decorative `<div>` proliferation → "Replace decorative `<div>` with `<section>` or remove"
- Inline hex values → "Replace all hex with var(--token-name) reference"
- Tailwind classes leaking in → "Remove all utility classes; use semantic BEM-lite class names only"
- Auto-vectorized icons (dirty paths with 50+ commands) → "Redraw icon with ≤ 20 path commands; if not possible, leave TODO placeholder"

# After P7 → P8

Once you have the bundle:
1. Place files in `docs/research/visual-prototypes/PF-V/`
2. Open `05-HANDOFF-to-PF-C4-protocol.md`
3. Fill in the handoff manifest and create the single batch PR
