---
title: PF-V Session Prompts S00-S18 (P0 through P6)
status: candidate / generation_prompts / not-authority
created_at: 2026-05-06
purpose: 18 paste-ready prompts for image generation phases. Use after pasting 00-master-context.md.
---

# How to use this file

1. Each section below is **one GPT Pro session**.
2. Order: S00 → S01 → ... → S18. Don't skip P0 — it anchors all downstream visual language.
3. For each session: paste `00-master-context.md` first (if new session), then paste the session prompt below.
4. After each session: download the 10 images, fill 1 row per image in `04-INDEX-template.csv`, mark V-PASS / V-CONCERN / V-REJECT.
5. Image-to-image evolution sessions (P6 + selectively in P2-P4): use patterns from `02-image-to-image-evolution-patterns.md`.

---

# Phase 0 — Bootstrap (1 session, 10 images, 10 min)

## S00 — Master anchor: capture-station 4-panel desktop

> **Purpose**: Establish the visual anchor for the entire 180-image set. Pick 1 V-PASS as the master mood reference for all downstream sessions.

```
Generate 10 mockup variants of the ScoutFlow Capture Station at desktop resolution (16:9, 2K). All 10 must share these constants:

- Layout: top URL Bar (full width), then 3-column [Live Metadata | Capture Scope | Trust Trace] with Trust Trace as the widest column (~1.4× the others)
- Operator workstation mood (dark cool, focused, evidence-arriving)
- All visible text rendered correctly
- Tokens: bg_canvas page background, bg_shell shell card, surface_base panels, border_soft default borders
- Realistic dummy content from master context

Vary across the 10 images on these axes (one variant per axis combination):
1. Default empty state (URL bar empty, panels showing skeletal placeholders)
2. URL pasted, capture button armed, metadata loading skeleton
3. Metadata loaded, scope panel shows metadata_only state, trust trace not yet populated
4. Full state: metadata + scope + trust trace populated, vault preview drawer collapsed
5. Vault preview drawer expanded showing markdown excerpt
6. Vault commit dry-run button visible (write_enabled=false visualization, accent_blocked muted treatment)
7. Multi-capture history sidebar collapsed, current capture in focus
8. Error banner state at top (accent_warn) — preview unavailable, retry CTA shown
9. High-density mode (compact spacing, more rows visible)
10. Reduced-density mode (lg/xl spacing, larger touch targets)

For each image, plan the layout BEFORE generating. Use thinking mode. Verify against the 5-Gate rules and 14 anti-patterns from master context. Render all text strings exactly as specified.

Output: 10 images, all 16:9, 2K resolution. Provide a 1-line caption for each (variant axis position).
```

**Self-check after S00:**
- [ ] At least 1 image V-PASS (調性對 + 5-Gate 全過 + 文本準確)
- [ ] Anti-pattern 全清
- [ ] Token 色 hex 沒漂（重點看 accent_live #50d4ff 是否準確）
- [ ] 文本中 capture_id / URL / timestamp 格式正確

如果 V-PASS 0 张 → 不进 P1，先 image-to-image 修，或回 S00 改 prompt 重发。

---

# ⚠️ PHASE 1 决策修订 — S02/S03 跳过 (2026-05-07)

ScoutFlow 是 localhost 桌面操作员工作站，**不是** SaaS / consumer app / 跨设备产品。S02 (mobile) + S03 (tablet) 跳过，省 20 张 + ~40 min。详见 `LESSONS-LEARNED.md` L5。

P1 实际仅做 S01 (desktop foundation 10 张)，已完成。

# Phase 1 — Foundation device variants (原计划 3 sessions，实际 1 session)

## S01 — Desktop foundation, locked mood, 10 detail variants

```
Take the master anchor image (image #N from S00, the V-PASS one) as visual reference for mood, palette, and typography. Generate 10 desktop variants (16:9, 2K) that explore detail-level variations while keeping the master anchor's mood EXACT:

Vary across:
1. Header treatment: minimal vs slightly elevated (background tint shift only)
2. URL Bar: input style — line-only vs filled surface_muted
3. Metadata panel header: with capture_id chip vs without
4. Scope panel: progress timeline vs state badges
5. Trust Trace: graph-only vs graph + side legend
6. Vault preview button: icon-only vs icon+label vs label-only
7. Top-right utility area: empty vs settings cog vs status pill
8. Footer: hidden vs build version pill (mono font)
9. Border weight: 1px soft vs 1.5px strong on key panels
10. Gap rhythm: 24px between panels vs 32px

Self-verify each: anti-patterns absent, text correct, palette unchanged from anchor.
```

## S02 — Mobile linearized, 10 device variants

```
Take master anchor (S00 winner) as mood reference. Generate 10 MOBILE variants at 9:16 portrait, 1024×1820 minimum.

Layout rule: same 4-panel IA but linearized vertically (URL Bar → Live Metadata → Capture Scope → Trust Trace). Trust Trace MUST remain visible (no hide-on-mobile pattern); it can show a compact graph mode.

Vary across:
1. Sticky URL Bar (top fixed, body scrolls)
2. URL Bar with collapse-on-scroll
3. Capture-action revealed via swipe gesture indicator
4. Live Metadata in card list (vertical stack)
5. Live Metadata in chip row (horizontal scroll)
6. Capture Scope as state stepper (vertical)
7. Trust Trace compact (single column tree view)
8. Trust Trace expanded full-screen overlay (one variant showing the overlay state)
9. Vault preview as bottom-sheet draft state
10. Error/blocked state showing accent_blocked treatment on disabled capture

Verify mobile-friendly tap targets (≥ 44px), 8px grid maintained, no card-inside-card.
```

## S03 — Tablet 2-column, 10 device variants

```
Take master anchor as mood reference. Generate 10 TABLET variants at 4:3 landscape (1366×1024 minimum).

Layout rule: top URL Bar full width, then 2-column [Metadata + Scope stacked left | Trust Trace right]. This is the design-brief 2-column tablet rule.

Vary across:
1. Default state, both columns equal width
2. Trust Trace gets 60% width, left stack 40%
3. Vault preview as bottom drawer collapsed
4. Vault preview as bottom drawer expanded
5. Settings panel slide-out from right (overlapping Trust Trace)
6. Capture history list overlaid on left stack
7. Reduced-density variant
8. High-density variant
9. Error banner state
10. Loading skeleton state

Verify tablet-appropriate density (between mobile and desktop), 8px grid, anti-patterns absent.
```

---

# Phase 2 — Panel detail (6 sessions, 60 images, 60 min)

## S04 — URL Bar component, 10 states

```
Generate 10 detail mockups of the URL Bar component (16:9 or 21:9 framing showing only URL Bar area + hint of context above/below). Higher zoom, more detail visible.

10 states:
1. Empty state — placeholder text "粘贴一个 URL 或拖入文件" (gray text_muted)
2. Focus state — border_strong accent, no content
3. Pasted unverified — URL text in mono, capture button greyed (accent_focus pending)
4. Pasted verified — URL valid, capture button armed (accent_live)
5. Validating — small inline spinner inside the input area
6. Error — invalid URL, accent_warn border + small error message below
7. Success — capture created, capture_id chip appears with mono text
8. Disabled — entire bar greyed (accent_blocked low opacity), explain text below
9. History dropdown open — last 5 captures listed below input, mono URLs
10. Active drag-over state — border_focus glow, "拖放以创建 capture" hint

For each: render exact dummy URL `https://www.bilibili.com/video/BV1xK4y1f7yC` where applicable. Verify focus rings use accent_live, error uses accent_warn (not accent_blocked — blocked is for write-disabled, warn is for input error).
```

## S05 — Live Metadata Panel, 10 content variants

```
Generate 10 detail mockups of the Live Metadata Panel (4:3 or 1:1 framing, single panel filling the frame).

Each shows the panel after metadata has loaded. Vary the content to test layout robustness:
1. Long Chinese title (40+ chars), short uploader, normal duration
2. Short Latin title, long uploader handle (truncates with ellipsis), short duration
3. CN/EN mixed title with em-dashes, normal fields
4. Numbers-heavy: views 1,234,567 / likes 89,012 / comments 4,321
5. Sparse data: many fields show "—" placeholder (text_muted)
6. Tags overflow: 8+ tag chips, with "+3" overflow chip at end
7. Live duration counter (mock real-time updating, mono)
8. Multilingual title (CN + EN + JP)
9. Page-count metadata (for paginated sources): "1 / 12"
10. Thumbnail field shown (small 64×36 image placeholder, NOT a stock photo — geometric placeholder)

Layout: panel header (capture_id chip mono) + metadata table (label : value rows), 8px row gap. Verify text alignment, baseline, no card-inside-card.
```

## S06 — Capture Scope Panel, 10 state-machine views

```
Generate 10 detail mockups of the Capture Scope Panel.

The panel shows a state machine from `metadata_only` to future blocked layers. Blocked layers MUST stay visible but visually downgraded (not hidden — visible-but-blocked is the design contract).

10 state combinations:
1. Default: metadata_only active (accent_live), media_layer / audio_layer / vault_layer all blocked (accent_blocked muted)
2. Hover/focus on a blocked layer showing tooltip "blocked_by: PF-O1-02 true_vault_write_overflow_gate"
3. Mid-transition: metadata_only → preview_ready (animation frame)
4. preview_ready active, vault_commit_dry_run as next available (accent_focus pending)
5. vault_commit_dry_run completed, write_enabled=false visualization
6. All 4 layers shown vertically as a stepper
7. Compact mode: layers as horizontal pills
8. Detail expanded: clicking a layer opens its evidence panel inline
9. Error state: a layer failed, accent_warn treatment + retry button
10. Multi-capture comparison: 2 captures side by side showing different scope states

Verify: blocked layers visually downgraded (lower opacity, muted color) but still readable; state names rendered correctly.
```

## S07 — Trust Trace Graph, 10 graph variants

```
Generate 10 detail mockups of the Trust Trace Graph.

Trust Trace = graph view of `capture → state → job → probe → receipt → media/audio → audit`. It's the primary deep-inspection surface. Operator zooms / filters / clicks nodes.

10 variants:
1. Default linear flow (left to right)
2. Branching: 1 capture → 2 parallel jobs → merged audit
3. Compact density (12+ nodes visible)
4. Expanded density (5 nodes, more detail per node)
5. Single node selected, side panel showing that node's evidence
6. Filter active (some nodes greyed via accent_blocked low opacity)
7. Search highlight (1 node accent_focus glow + connecting edges accent_live)
8. Time-axis variant (nodes positioned by timestamp on horizontal axis)
9. Error path highlighted (one branch in accent_warn)
10. Empty state (graph not yet populated, skeleton placeholder showing structure)

Node rendering: mono caption for node ID, body text for node label, accent_live edge for active path, border_soft for inactive. No emoji. No team-avatar circles.
```

## S08 — Vault Preview Panel, 10 state variants

```
Generate 10 detail mockups of the Vault Preview Panel.

This panel shows the markdown preview that WOULD be written to vault if write_enabled=true. Currently write_enabled=false, so this is preview-only.

10 states:
1. Idle (no capture selected, hint text)
2. Loading (skeleton with mono pulse animation hint)
3. Ready — markdown excerpt shown (15-25 lines), syntax highlighted in mono with CN/EN content
4. Error — preview fetch failed, accent_warn banner + retry
5. Blocked — write_enabled=false explicit overlay text "Preview only. Write disabled by overflow registry."
6. Long content — scroll indicator visible, fade at top/bottom
7. Frontmatter expanded — YAML block visible at top with capture_id, status: preview_only, write_enabled: false
8. Copy action triggered — toast confirmation "Markdown copied"
9. Download action — small download icon highlighted, tooltip "Download .md"
10. Diff state — comparing two versions of preview side-by-side (split view)

Verify: markdown rendered as actual readable markdown (not lorem ipsum); frontmatter YAML format correct; write_enabled=false ALWAYS visible (this is a hard contract).
```

## S09 — Vault Commit Dry-Run UI, 10 disabled-state visualizations

```
Generate 10 mockups of the Vault Commit Dry-Run button + surrounding UI context.

Critical contract: `write_enabled=false` is hardcoded for the entire current localhost loop. The button MUST visually communicate "preview-only / write disabled / no actual file write happens" without being invisible.

10 variants (all show the disabled-but-visible state):
1. Standard: button labeled "Vault commit (dry-run)" with accent_blocked muted treatment, lock icon
2. With tooltip on hover: "write_enabled is false. This dry-run validates the markdown but does not write to disk."
3. Click triggered → modal showing dry-run result (no actual file written)
4. Modal expanded: dry-run validation passes (3 green check rows: schema valid, frontmatter valid, path resolvable)
5. Modal expanded: dry-run validation fails (1 red row: invalid frontmatter field)
6. Inline result (no modal): dry-run report inline below button
7. Compact form: small icon-only variant for narrow viewport
8. Expanded form: full button + descriptive text below
9. Multi-capture batch dry-run: 3 captures listed with per-row dry-run status
10. Educational state (first-time user): disabled button + "Dry-run is disabled until preview loads. Why?" link

Render the lock/disabled treatment using accent_blocked at low saturation, NOT by removing the button. Operators must see what they cannot do.
```

---

# Phase 3 — Extended surfaces (3 sessions, 30 images, 30 min)

## S10 — Topic Card Lite v0, 10 markdown content variants

```
Generate 10 mockups of the Topic Card Lite v0 detail view.

Topic Card Lite is the FIRST output ScoutFlow proves human-useful (PF-C1 milestone). It's a compact markdown card capturing one captured URL's signal/insight in a structured form.

Layout: card with 3-section structure:
- Header: capture_id chip + source URL (mono, truncated) + timestamp
- Body: markdown content with frontmatter visible (title, signal, hypothesis_seed, evidence_pointers, tags)
- Footer: action row (copy md / download / mark useful / mark not-useful)

10 content variants:
1. News article topic card
2. Bilibili video topic card with tags
3. Long-form blog post topic card (truncated body with "expand" affordance)
4. Empty signal state (no signal extracted, placeholder)
5. Multiple signals (3 bulleted signal lines)
6. Hypothesis_seed prominent (a hypothesis statement highlighted in accent_focus)
7. Evidence_pointers list (3-5 mono URLs)
8. Tags overflow (8+ tags, wraps to multiple rows)
9. Marked not-useful state (card visually downgraded with accent_blocked treatment, but still readable)
10. Side-by-side comparison: 2 topic cards from same source URL with different extraction strategies

Verify: actual readable markdown content (not lorem ipsum); frontmatter YAML format consistent; mono font for IDs/URLs/timestamps.
```

## S11 — Topic Card Vault detail surface, 10 variants

```
Generate 10 mockups of the Topic Card Vault detail surface.

This is where multiple Topic Card Lite outputs aggregate into a vault view. Operator can browse, filter, mark useful, export.

Layout: 2-column [card list left | selected-card detail right]

10 variants:
1. Default — list with 8 cards visible, first selected showing detail
2. Filter active — list filtered to "marked useful" only
3. Search query active — list filtered with search highlight
4. Sort by timestamp — descending
5. Sort by signal density — most signal-rich at top
6. Bulk action mode — checkboxes shown beside each list item, batch action bar at top
7. Empty filter result — "0 cards match" state with reset CTA
8. Detail right pane in edit mode — markdown editor visible
9. Detail right pane showing diff (vs previous version)
10. Export modal triggered — "Export selected to .md / .csv" options

Verify: 8px grid, mono for IDs, no avatar circles, no card-inside-card.
```

## S12 — Signal-Hypothesis IA + Capture-Plan IA mixed, 10 variants

```
Generate 10 mockups split 5+5 across two Wave 5 IA candidates:

5 for Signal-Hypothesis IA (frontend candidate from `docs/visual/h5-capture-station/wave5/h5-panel-to-signal-hypothesis-mapping-candidate-2026-05-05.md`):
1. Signal list view with hypothesis count chips per signal
2. Single signal expanded showing 3 supporting hypotheses
3. Hypothesis comparison view (2 hypotheses side by side, evidence weighting visible)
4. Signal lifecycle stepper (raw → vetted → linked → archived)
5. Empty signal state with create-signal affordance

5 for Capture-Plan IA (from `docs/visual/h5-capture-station/wave5/capture-plan-frontend-ia-candidate-candidate-2026-05-05.md`):
6. Capture plan detail view (header: plan name + status + run-count)
7. Plan input/output contract visible (input captures, output topic cards)
8. Plan dry-run review (3 sample captures shown with predicted outputs)
9. Plan execution log (mono timestamp + status rows)
10. Plan empty state ready to define inputs

All 10 must respect master anchor mood (S00 winner) — no IA divergence in palette/typography. IA candidates are NEW concepts but visual language stays unified.
```

---

# Phase 4 — States + transitions (2 sessions, 20 images, 20 min)

## S13 — State matrix grid, 10 mixed-surface state demos

```
Generate 10 images each showing a 2×2 grid of states (so 4 states per image, 40 state demos total in this session).

Each image: 4 state demos arranged as quadrants, taken from a randomized surface (capture-station / vault preview / topic card / capture scope etc.). The state per quadrant:
- Top-left: idle/empty
- Top-right: loading
- Bottom-left: success/ready
- Bottom-right: error/blocked

10 images covering surfaces:
1. Capture-station 4-panel × 4 states
2. URL Bar component × 4 states
3. Live Metadata Panel × 4 states
4. Capture Scope Panel × 4 states
5. Trust Trace Graph × 4 states
6. Vault Preview Panel × 4 states (this is the most critical — write_enabled=false in all 4)
7. Vault Commit Dry-Run × 4 states
8. Topic Card Lite × 4 states (idle list / loading / loaded / empty filter)
9. Topic Card Vault × 4 states
10. Signal-Hypothesis IA × 4 states

Each quadrant labeled with mono text in corner: "idle / loading / ready / error" etc. Verify: state semantics consistent across surfaces (loading always shows skeleton + mono pulse; error always uses accent_warn for input error vs accent_blocked for write-disabled).
```

## S14 — Lifecycle visualization, 10 transition flows

```
Generate 10 mockups visualizing capture lifecycle transitions.

Each image shows a horizontal flow strip with 5 frames left-to-right, demonstrating a capture's journey:

Frame 1: capture creation (URL pasted)
Frame 2: metadata loading
Frame 3: preview ready
Frame 4: dry-run validation
Frame 5: blocked at write (write_enabled=false visualization)

10 variants showing different lifecycle scenarios:
1. Happy path (all 5 frames green/accent_live progression)
2. Error at frame 2 (metadata fetch fails, accent_warn)
3. Error at frame 3 (preview parse fails)
4. Error at frame 4 (dry-run schema invalid)
5. Frame 5 always blocked (write_enabled=false), but the path up to it is happy
6. Multi-capture batch lifecycle (3 captures in parallel)
7. Slow path (extended timeline, frames spaced out)
8. Fast path (compressed timeline)
9. Annotation mode (each frame has a small label below explaining state)
10. Comparison: side-by-side happy vs error lifecycle

Use accent_live for active proof, accent_warn for errors at input, accent_blocked for the write-disabled terminal state. No accent_success for the final state — successful "preview-only" still ends at accent_blocked because nothing was actually written.
```

---

# Phase 5 — Icons (2 sessions, 20 icons, 20 min)

## S15 — System icons, 10 line-icons

```
Generate 1 image containing 10 system line-icons arranged in a 5×2 grid on a single bg_canvas (#07111b) background.

Each icon: 256×256 cell within a 1280×512 composite image. Line-icon style only. Stroke 1.5px in accent_live (#50d4ff). No fill. No emoji. No isometric. No 3D.

The 10 icons (one per cell):
1. capture (an inbox-arrow geometric mark)
2. preview (eye with cleaner geometry, no pupil dot)
3. commit (paper-with-checkmark)
4. dry-run (paper-with-magnifying-glass)
5. blocked (lock with subtle X)
6. signal (radial pulse 3-ring)
7. hypothesis (lightbulb geometric, hexagonal)
8. plan (clipboard-with-numbered-rows)
9. trace (graph-with-3-nodes)
10. evidence (stack-of-papers with corner fold)

Each icon must:
- Use only line strokes (no fill except for tiny accent dots if structurally needed)
- Be vectorizable (clean geometry, no scribbles, no soft edges)
- Sit at the cell center with ~20% padding margin
- Have small mono caption below at body text size labeling its name (e.g., "capture", "preview", ...)

Output 1 image, then a separate row of 10 individual 256×256 versions if your tool supports it.
```

## S16 — State icons, 10 line-icons

```
Generate 1 image containing 10 state line-icons arranged in a 5×2 grid on bg_canvas background.

Same style rules as S15 (line-only, 1.5px stroke, 256×256 cells, mono captions).

The 10 state icons:
1. live (single pulse dot inside ring)
2. success (clean checkmark in ring)
3. warning (triangle with exclamation, accent_warn stroke)
4. blocked (lock, accent_blocked stroke)
5. focus (radiating-lines around center dot, accent_focus stroke)
6. locked (closed padlock, slightly different from blocked — full padlock body)
7. loading (3-dot horizontal, mid-pulse implied)
8. error (X mark in ring, accent_warn stroke)
9. empty (dotted circle, hollow)
10. ready (filled checkmark in ring, accent_success stroke)

Vary stroke color per icon to match its semantic accent (live = accent_live, success = accent_success, warn = accent_warn, blocked = accent_blocked, focus = accent_focus). Keep the line geometry style consistent.
```

---

# Phase 6 — Refinement (image-to-image, 2 sessions, 20 images, 20 min)

## S17 — Refinement A: density adjustment on winners

```
Take the V-PASS winners from P1-P5 (you'll have ~10-15 winning images by this point). Pick the top 10 candidates that are visually strong but feel "slightly off" on density (too tight or too loose).

For each, run image-to-image with delta:

"Same composition as input image. Increase visible content density by ~15%: tighter row spacing (24px → 16px), smaller body text (14px → 13px), remove 1 redundant divider. Keep all colors, text content, and panel structure identical. Output 1 variant."

Or the opposite delta:
"Same composition. Decrease density by ~15%: looser spacing, larger touch targets, restore breathing room. Keep palette + text identical."

10 outputs total: each one a refined-density variant of a P1-P5 winner. Compare side-by-side to decide which density wins for which surface.
```

## S18 — Refinement B: typography precision

```
Take the V-PASS winners that have any text-rendering issue (CN/EN baseline jitter, mono-font inconsistency, weight too thin/thick). 10 candidates.

For each, image-to-image with delta:

"Same composition. Fix typography: ensure all body text is Inter regular (not Inter light or Inter medium); ensure all monospace text is JetBrains Mono regular (not light); ensure CN + EN mixed lines align on the same baseline; ensure heading weight is 600 (not 700 or 500). Keep palette + layout + content identical."

10 outputs: each a typography-tightened variant of a winner.

After S18, you should have ~12-15 final V-PASS images covering all critical surfaces, ready for P7 image-to-HTML5 batch.
```

---

# Session checklist (apply to every session)

After each S0X session:

```
[ ] 10 images generated
[ ] All visible text renders correctly (first sanity check)
[ ] Anti-patterns: zero present
[ ] Token palette: only the 15 defined tokens used (spot check 2-3 hex)
[ ] 5-Gate: applies on at least 3 of 10 (don't need all 10 to pass — pick winners)
[ ] At least 1 V-PASS identified
[ ] INDEX.csv updated: 1 row per image with verdict + variant_axis + state_shown filled
```

If 0 V-PASS in a session, do NOT proceed to next session. Either:
- Run image-to-image on the closest-to-pass image (delta: fix the failing axis)
- Re-issue the session prompt with explicit constraint correction

# Cross-session checklist (after P0, P1, P3, P5)

```
[ ] Master anchor mood preserved across all sessions (palette didn't drift)
[ ] Token name discipline: no raw hex in any session prompt (always token name)
[ ] All 18 surfaces covered (S00-S18 = 9 phases worth of surfaces)
[ ] V-PASS coverage: ≥ 1 per surface (some surfaces have 2-3 V-PASS variants OK)
[ ] No surface skipped (if a surface is too risky to attempt, document why in INDEX.csv `notes` column)
```

# Cost estimate

- 18 sessions × 10 images = 180 images
- @ ~$0.21/image high quality = ~$38 total
- User said unlimited budget — can go higher quality / more variants if early sessions reveal need

# After S18 → P7

Once S18 complete:
1. Pick top ~12-15 images representing each critical surface (1 per surface).
2. Pick top 6-8 icons (you may have 20 generated; not all need to enter P7).
3. Bundle into a 50-image zip (or whatever GPT Pro batch limit is).
4. Open `03-P7-batch-image-to-html5-prompt.md`, follow that protocol.

P7 is where mockups become consumable HTML5/SVG/CSS for downstream PF-C4 lane.
