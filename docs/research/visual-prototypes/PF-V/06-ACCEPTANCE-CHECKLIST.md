# P8 Acceptance Checklist — PF-C4 receiving pass

本清单是 candidate / not-authority receiving audit。PF-C4 在宣布 “handoff received” 前，按六类各 5 项一次性检查；每项都应可观察或可运行验证。通过本清单只代表 PF-C4 可以安全开始 bootstrap，不代表生产实现已经完成，也不代表 PF-V 资产升级为 authority。若某项失败，先记录具体文件和失败原因，再决定由 CC0 修正 P8 应用问题，还是由 PF-C4 在自己的 lane 中处理实现差异。

## 1. File presence

File checks come first because every later semantic review depends on a complete tree. Do not substitute screenshots or partial downloads for missing files.

- [ ] `p7-output/` contains exactly 76 files at receive time (verify: `find docs/research/visual-prototypes/PF-V/p7-output -type f | wc -l` returns `76`).
- [ ] `p7-output/html5-rough/` contains 13 `.html`, 13 `.module.css`, and 13 `.model.json` files with matching numeric prefixes `00` through `12`.
- [ ] `p7-output/css-modules-candidate/` contains 15 component pairs: every `*.module.css` has a same-stem `.html` usage snippet.
- [ ] `p7-output/icons/system.svg` and `p7-output/icons/state.svg` both exist and each contains 10 `<symbol>` IDs, including the dual `icon-blocked` semantic.
- [ ] PF-V source inventory is present: `PF-V-INDEX.csv` has 152 data rows / 19 columns and `images-P*/` contains 152 PNG mockups in the receiving repository checkout; missing PNGs mean provenance is incomplete even if P7 HTML exists.

## 2. Token discipline

- [ ] `p7-output/tokens.css` defines the 15 canonical color tokens plus 4 derived state backgrounds, typography, spacing, radius, and shadow variables.
- [ ] Zero hardcoded hex values exist outside `p7-output/tokens.css` (verify: `grep -R "#[0-9a-fA-F]" docs/research/visual-prototypes/PF-V/p7-output --include="*.css" | grep -v "tokens.css"` returns no rows).
- [ ] `density-compact.css` only changes density-related variables (`--type-title`, `--type-body`, `--space-md`, `--space-sm`) and does not introduce new colors or component selectors.
- [ ] `type-weight-heavy.css` only changes typography-related variables (`--font-weight-*`, `--type-mono`) and does not introduce new colors or component selectors.
- [ ] Every surface/component stylesheet continues to use `var(--token-name)` for color, border, background, radius, spacing, typography, and shadow decisions; no local token namespace is invented.

## 3. Semantic HTML

- [ ] All 13 surface HTML files open with `<!doctype html>`, `lang="zh-CN"`, a `<main>` root, and visible Simplified Chinese surface titles.
- [ ] Zero `<div>` proliferation exists in surface/component HTML (verify: `grep -R "<div\b" docs/research/visual-prototypes/PF-V/p7-output/html5-rough docs/research/visual-prototypes/PF-V/p7-output/css-modules-candidate` returns no rows).
- [ ] Surface structure uses semantic tags such as `<main>`, `<header>`, `<section>`, `<article>`, `<aside>`, `<figure>`, `<table>`, `<dialog>`, `<ol>`, and `<ul>` where appropriate.
- [ ] Evidence-heavy surfaces (`04-trust-trace`, `09-signal-hypothesis`, `10-capture-plan`, density/type specs) use real `<table>` markup for field evidence or execution logs instead of layout-only tables.
- [ ] Modal examples using `<dialog open>` remain review-only static states; PF-C4 has logged any older-browser fallback decision separately before runtime implementation, so the static reference does not silently become a browser support promise.

## 4. Anti-pattern absence

- [ ] No Tailwind / shadcn / Panda styling adoption appears in HTML/CSS output; explanatory mentions in README/HANDOFF are reject-list prose, not implementation usage or dependency approval.
- [ ] No inline `style=` attributes, `<script>` tags, or React `className=` fragments appear in `p7-output/`; the bundle stays browser-openable HTML/CSS reference only.
- [ ] No SaaS/admin/landing-page vocabulary or marketing badges appear in visible UI strings (`Premium`, `Pro`, `Try free`, `Upgrade`, `Powered by AI`, `Magic Wand` should not appear).
- [ ] No emoji icons are used as UI icons; iconography comes from geometric SVG symbols or CSS-only status indicators.
- [ ] English UI chrome is absent except allowed code-format values: URLs, IDs, file paths, YAML keys, DOM-path fields, technical field names, and backend code values shown in monospace.

## 5. Cross-system / boundary

- [ ] Every visible vault target uses `~/workspace/raw/00-Inbox/` or a project-scoped `~/workspace/raw/...` path; no virtual ScoutFlow vault path appears in P7 output or P8 docs.
- [ ] Vault preview/commit copy makes clear that ScoutFlow delivers clean Markdown to the Obsidian raw vault inbox and does not own enrich/wiki/knowledge-flywheel steps.
- [ ] `sync-badge` implements exactly three tiers: `synced` / `pending` / `external-changed`, with Chinese labels `已同步` / `待同步` / `外部已改`.
- [ ] `08-topic-card-vault.html` pairs sync tiers with `icons/state.svg#icon-success`, `#icon-warning`, and `#icon-focus`; system icons are not substituted for sync semantics.
- [ ] LESSONS L2 and L8 are referenced in PF-C4 handoff notes before implementation work begins, so path boundary and cross-system state are not rediscovered later as a bug or a new design dispute.

## 6. PF-C4 readiness

- [ ] All 13 surface HTML files render in a local browser without blocking console errors, broken stylesheet links, or missing SVG `<use>` references.
- [ ] `p7-output/MAPPING.md` lists task IDs `00` through `64` and maps each source image to a surface, component, icon, or global output file.
- [ ] Component candidate pairs can be ported 1:1 into PF-C4 component folders as CSS Modules after renaming conventions are chosen; no raw class name must be copied verbatim.
- [ ] The four `<!-- TODO -->` placeholders are triaged with owner, priority, and candidate implementation approach before PF-C4 closes its first scaffold PR.
- [ ] PF-C4 can open its own first PR from a clean lane, e.g. `feat(capture-station): scaffold p7-reference`, without modifying PF-V research lane files or reopening PF-V generation work.
