---
title: PF-V Self-Check + Verdict Protocol
status: candidate / verdict_protocol / not-authority
created_at: 2026-05-06
purpose: Operator-side checklist for V-PASS / V-CONCERN / V-REJECT decisions on every output
---

# When to use this file

After every session output (10 images), and after every P7 file (HTML/CSS/SVG), open this file and run the relevant checklist before filling INDEX.csv.

5-Gate principles come from `~/.claude/rules/aesthetic-first-principles.md` (cross-project rule). Anti-patterns come from `00-master-context.md`.

---

# Per-image verdict protocol (sessions S00-S18)

## Step 1 — Anti-pattern scan (binary, hard reject if any present)

For each image, scan for ALL 14 anti-patterns from master context. **One present = V-REJECT** regardless of other qualities.

```
[ ] No SaaS admin dashboard chrome (sidebar with logo / breadcrumb / unrelated nav tabs)
[ ] No landing page elements (hero / marketing copy / "Sign up free")
[ ] No card-inside-card stacking
[ ] No decorative gradients (purple→pink, orange→red, "tech glow")
[ ] No glassmorphism (frosted glass surfaces)
[ ] No neon glow / cyberpunk treatment
[ ] No stock photography / AI-illustration in panel backgrounds
[ ] No emoji icons
[ ] No "Premium" / "Pro" / "Try free" / "Upgrade" badges
[ ] No multiple unrelated chart types in one panel
[ ] No real company logos
[ ] No "AI Agent" / "Magic Wand" iconography
[ ] No round avatars
[ ] No notifications / inbox / chat surfaces
```

If any unchecked → **V-REJECT**, do not proceed.

## Step 2 — 5-Gate visual check (rate P/F per gate)

```
Gate 1: Visual Hierarchy
[ ] Primary action (URL submit / capture button) one-eye distinguishable
[ ] Scan path matches reading direction (top→bottom, left→right desktop)
[ ] Trust Trace is visually prominent but does not steal focus from URL Bar
→ Pass / Fail

Gate 2: Spacing / Alignment
[ ] All visible gaps are multiples of 8px
[ ] Text + icon baseline aligned in label-value rows
[ ] Equal margins on parallel borders
→ Pass / Fail

Gate 3: Occlusion Safety
[ ] No popup / modal covers key info (capture_id, URL, primary action)
[ ] Scroll bars / system bars don't cover important elements
[ ] Safe-area respected (especially mobile)
→ Pass / Fail

Gate 4: Typography Legibility
[ ] Body text contrast ≥ 4.5:1 on its surface
[ ] Main heading ≥ 20px (visible at intended viewing size)
[ ] CN + EN mixed lines: same baseline, no jitter
[ ] Mono font used for IDs / URLs / timestamps (not body sans)
→ Pass / Fail

Gate 5: Visual Weight
[ ] accent_live (#50d4ff) appears in ≤ 2 spots per panel
[ ] Blocked layers visually downgraded but still readable (not hidden)
[ ] No high-saturation color competing with primary action
→ Pass / Fail
```

Score: e.g., `PPPPP` (5 pass) / `PPFPP` (gate 3 fails) / `PFFPF` (3 fails).

## Step 3 — Token discipline check

```
[ ] All visible colors map to one of 15 design tokens
[ ] No raw hex appears in the visible mockup that isn't in the token list
[ ] Special check: accent_live #50d4ff matches exactly (not #4FCAEF or other near-match)
```

If a token mismatch → V-CONCERN (single-axis fixable via Pattern J forensic check).

## Step 4 — Text accuracy check

```
[ ] All visible text strings render correctly (no scribbles, no garbled characters)
[ ] CN characters: 标点 (punctuation) correct (not full-width when half-width expected, not vice-versa)
[ ] EN words: spelled correctly (gpt-image-2 has 95-99% accuracy but spot-check)
[ ] Mono content (IDs / URLs / timestamps): format consistent with master context
[ ] capture_id format: `cap_YYYYMMDD_5hexchars`
[ ] URL format: realistic Bilibili / generic web pattern
[ ] Timestamp format: ISO `YYYY-MM-DD HH:MM UTC`
```

If text errors → V-CONCERN if 1 minor error, V-REJECT if multiple errors or critical strings (capture_id / URL) wrong.

## Step 5 — Mood / archetype check

```
[ ] Looks like operator workstation (compact, focused, evidence-arriving)
[ ] Does NOT look like dashboard / landing / chat / notification UI
[ ] Palette consistent with master anchor (S00 winner)
[ ] Density consistent with master anchor (not significantly tighter/looser unless intentional variant)
```

If mood drift → V-CONCERN (Pattern A density, Pattern B typography, or Pattern C accent might fix).
If complete archetype miss (e.g., generated a dashboard) → V-REJECT, regenerate session prompt.

## Step 6 — Verdict assignment

Based on Steps 1-5:

| Step Result | Verdict |
|---|---|
| Step 1 fails (any anti-pattern present) | V-REJECT |
| Steps 2-5: 5-Gate all P + tokens clean + text clean + mood right | V-PASS |
| Steps 2-5: 4-Gate P + 1 single-axis fixable issue | V-CONCERN, candidate for image-to-image evolution |
| Steps 2-5: 3-Gate or below P, OR multiple-axis issues, OR mood off | V-REJECT |

Edge case: If 5-Gate is `PPPPP` but a minor token drift → V-PASS-with-concern (use this label sparingly; only if overall gestalt is right).

# Per-P7-output verdict protocol

P7 outputs (HTML/CSS/SVG/tokens.css) follow a different verdict criteria — structural, not visual.

## For each .html file:

```
[ ] HTML5 valid (passes W3C validator on quick scan)
[ ] Semantic tags only (<main>, <section>, <header>, <h1-h3>, <p>, <ul>, <table>, <button>) — no decorative <div>
[ ] Single <link rel="stylesheet" href="./{surface}.module.css">
[ ] Zero inline style="" attributes (except <html style> for CSS Variables demo)
[ ] All visible text matches the source mockup
[ ] Mono text in <code> or <pre> tags
[ ] Icons inline <svg> (not <img>)
[ ] State variants demonstrated as CSS class modifiers (.surface__element--state)
[ ] Container queries used for responsive (@container) or @media as fallback
[ ] Opens in browser without errors (test by opening with file:// or local server)
```

If all P → V-PASS for P7 file.
If 1-2 fail → V-CONCERN, fixable via re-run on that single surface.
If 3+ fail → V-REJECT, regenerate that surface in P7 with explicit corrections.

## For each .module.css file:

```
[ ] All values are var(--token-name) — zero hardcoded hex / px outside 8px multiples
[ ] BEM-lite class naming (block__element--modifier)
[ ] No Tailwind / shadcn / utility classes
[ ] States as &--modifier (or .block--modifier without nesting)
[ ] Single component scope (one component per file)
```

## For each .svg icon:

```
[ ] viewBox 0 0 256 256
[ ] stroke-width 1.5
[ ] stroke="var(--accent-live)" or appropriate semantic accent
[ ] No fill except where structurally necessary
[ ] ≤ 20 path commands per icon
[ ] No gradients / filters / clip paths beyond minimum
```

## For tokens.css:

```
[ ] All 15 color tokens defined as CSS Variables on :root
[ ] Typography tokens (font family, size, line-height)
[ ] Spacing tokens (--space-xs through --space-xl)
[ ] Radius tokens
[ ] Shadow tokens
[ ] No JS / no SCSS / pure CSS
[ ] Comment header explains "not-implementation-approval"
```

# Verdict cadence

- After each session: 10 verdicts, ~3-5 min review time per session
- After P7: ~15-30 P7 file verdicts, ~10 min review time
- Total review time across PF-V: ~90 min

This is built into the 3-4h total estimate.

# Common pitfalls during review

## "It looks beautiful but..."
If the image is beautiful but the anti-pattern is "decorative gradient" or "neon glow" or "round avatars" — V-REJECT anyway. Beauty is not the verdict criterion; operator-workstation discipline is.

## "It's almost there, just one fix..."
That's V-CONCERN, not V-PASS. Use image-to-image Pattern A-J to fix the single axis. Don't promote to V-PASS to "save effort".

## "Two images both look good..."
Both can be V-PASS. INDEX.csv supports multiple V-PASS per surface. P7 bundle plan suggests 1-3 V-PASS per surface, so multiple winners is fine.

## "The text is in English but I asked for Chinese..."
This is text accuracy failure (Step 4). V-REJECT. Regenerate with explicit "all text in 简体中文" instruction.

## "The accent_live is slightly different shade..."
Token discipline failure (Step 3). Use Pattern J forensic check to confirm. If confirmed off-token → V-CONCERN, fixable via Pattern C accent restraint or Pattern I failure recovery.

# Acceptance threshold for advancing PF-V phases

| Phase | Min V-PASS count to advance |
|---|---|
| P0 (S00) | 1 V-PASS (the master anchor) |
| P1 (S01-S03) | 1 per device archetype = 3 total |
| P2 (S04-S09) | 1 per panel = 6 total |
| P3 (S10-S12) | 1 per surface = 4 total (TopicCardLite + TopicCardVault + Signal + Plan) |
| P4 (S13-S14) | 1 state-grid + 1 lifecycle = 2 total |
| P5 (S15-S16) | 1 system-icon-grid + 1 state-icon-grid = 2 total |
| P6 (S17-S18) | optional refinements; can have 0 if P0-P5 winners are already strong |

If a phase doesn't hit min → re-shoot that phase before advancing. Don't accumulate V-CONCERN debt.

# Final acceptance for P7 trigger

Before P7 (image-to-HTML5 batch):

- [ ] ≥ 18 V-PASS images total covering ≥ 12 distinct surfaces
- [ ] At least 1 V-PASS for each critical surface: capture-station-desktop, url-bar, vault-preview, capture-scope, trust-trace
- [ ] Master anchor (S00 V-PASS) preserved as visual reference
- [ ] All V-CONCERN images either resolved or documented in INDEX with reason

If any criterion fails → don't trigger P7 yet. Resolve gaps.

# Final acceptance for P8 trigger (handoff)

Before P8 (PF-V → PF-C4 handoff):

- [ ] All P7 outputs pass P7 file verdict (above)
- [ ] INDEX.csv complete: every row has verdict + downstream_use
- [ ] HANDOFF doc filled with `accepted_files` + `not_accepted_files` lists
- [ ] Master batch PR drafted, sub-agents prepared

If criterion fails → fix before opening handoff PR.

---

# Quick-reference: V-verdict legend

| Verdict | Meaning | Action |
|---|---|---|
| **V-PASS** | All checks pass, ready for downstream | Filed in INDEX, candidate for P7 bundle |
| **V-PASS-with-concern** | 5-Gate all P but minor non-axis-fixable concern | Filed in INDEX with feedback note, can enter P7 bundle |
| **V-CONCERN** | 1-axis-fixable issue, base structure good | Image-to-image evolution attempt; if fixed → V-PASS, if not → V-REJECT |
| **V-REJECT** | Anti-pattern present OR multiple-axis issues OR archetype miss | Excluded from INDEX (or marked excluded), do NOT carry forward |

This 4-level scale balances rigor with practical iteration speed.
