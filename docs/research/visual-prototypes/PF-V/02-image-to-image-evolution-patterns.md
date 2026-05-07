---
title: PF-V Image-to-Image Evolution Patterns
status: candidate / evolution_patterns / not-authority
created_at: 2026-05-06
purpose: Reusable delta-prompt templates for refining V-CONCERN images and creating winner variants
---

# When to use image-to-image evolution

Use image-to-image (uploading a winner/near-winner image as anchor + delta text) instead of from-scratch generation when:

- A V-PASS image needs ONE specific dimension adjusted (density / typography / color saturation / one element)
- A V-CONCERN image is 80% there but has 1-2 fixable issues
- You want to generate variants of a confirmed winner WITHOUT risking palette drift
- P6 refinement passes (S17, S18)

Don't use image-to-image when:
- Master anchor needs to change (start over from S00, this is a from-scratch decision)
- Multiple axes need adjustment (do single-axis evolutions sequentially, not multi-axis at once)
- The base image is V-REJECT (don't compound flaws)

---

# Pattern library

## Pattern A — Single-axis density adjustment

```
[Upload winner image as base]

Same composition as input. Adjust ONE dimension only:

Density: increase / decrease by ~15%
- "increase": tighter row spacing (24px → 16px), smaller body text by 1px, remove 1 redundant divider
- "decrease": looser spacing (16px → 24px), restore breathing room, larger touch targets

Keep palette IDENTICAL (every hex unchanged).
Keep all text content IDENTICAL.
Keep panel structure IDENTICAL.
Keep IA ordering IDENTICAL.

Output 1 variant only.
```

## Pattern B — Typography precision fix

```
[Upload near-winner with typography issue]

Same composition as input. Fix typography only:

[Pick the relevant correction]
- Body text: switch to Inter regular (not light, not medium)
- Mono text: switch to JetBrains Mono regular (not light)
- CN+EN mixed lines: align on shared baseline
- Heading weight: 600 (not 700, not 500)
- Letter-spacing: default (no negative tracking)

Keep palette + layout + content IDENTICAL.

Output 1 variant.
```

## Pattern C — Color accent restraint

```
[Upload image where accent_live appears too many times]

Same composition. Reduce accent_live (#50d4ff) usage to ≤ 2 spots per panel.

Keep the accent on the highest-priority element only:
- URL Bar: keep accent on the active capture button OR on the focused input border (not both)
- Panel headers: ≤ 1 accent per panel
- State badges: only the currently-active state gets accent_live; others use border_strong or text_secondary

Demote excess accents to text_secondary (#a6b8cf) or border_soft (#1d3148).

Keep all other dimensions IDENTICAL.
Output 1 variant.
```

## Pattern D — Single-element replacement

```
[Upload near-winner with one element off]

Same composition. Replace ONE element only:

Element to replace: [name the element, e.g. "the icon in the top-right of the URL Bar"]
Replace with: [describe replacement, e.g. "a settings cog icon at 16x16, stroke 1.5px, accent_live"]

Keep all other elements IDENTICAL (positions, sizes, colors, typography).

Output 1 variant.
```

## Pattern E — State variant generation

```
[Upload V-PASS base in idle state]

Same composition as input. Render the same surface in [target state]:

Target state: [loading / error / blocked / success / etc.]

State change rules:
- loading: replace populated content areas with skeleton shimmer rows (text_muted at low opacity); add accent_focus pulse on primary input
- error: add accent_warn banner at top with mock error message; tint affected fields with subtle accent_warn border
- blocked: apply accent_blocked muted treatment to the primary action button; add lock icon + tooltip text
- success: green accent_success checkmark next to capture_id chip; transient toast at top
- empty: keep skeleton structure visible but with explicit "no data yet" hint text

Keep palette tokens consistent. Keep all unchanged elements IDENTICAL.

Output 1 variant.
```

## Pattern F — Anti-pattern correction

```
[Upload image with an anti-pattern present]

Same composition. Remove anti-pattern:

Detected anti-pattern: [pick from master context list]
- "decorative gradient on header" → replace with flat surface_elevated
- "card-inside-card stacking" → flatten to single card with internal divider lines
- "emoji icon" → replace with line-icon at 16x16 stroke 1.5px
- "rounded avatar circle" → remove (this is single-operator surface; no avatars)
- "premium/upgrade badge" → remove entirely
- "marketing CTA button" → replace with operational action button (action verb, mono-inline label)

Keep all non-anti-pattern elements IDENTICAL.

Output 1 variant.
```

## Pattern G — Aspect ratio adaptation

```
[Upload V-PASS desktop image as base]

Same surface, same mood, same palette, same content. Adapt to:

Target aspect: [9:16 mobile / 4:3 tablet / 1:1 square thumbnail]

Layout transformation rules:
- 9:16 mobile: linearize panels vertically in IA order; URL Bar sticky top; Trust Trace compact mode
- 4:3 tablet: 2-column [Metadata + Scope stacked left | Trust Trace right]; URL Bar full width top
- 1:1 thumbnail: hero shot of the surface, 1 primary element + 2 supporting; for marketing-style preview only

Keep palette + typography + content semantics IDENTICAL.

Output 1 variant.
```

## Pattern H — Cross-surface mood lock

```
[Upload S00 master anchor]

For the next 3 image generations in this session, treat the uploaded image as the EXACT mood reference:
- Palette: every hex must match
- Typography: every font family + weight must match
- Spacing rhythm: every gap multiple-of-8 like the anchor
- Surface treatment: panel borders, shadows, corner radius all match anchor

I'll send 3 separate prompts for: [surface 1], [surface 2], [surface 3]. Each one inherits anchor mood.

Confirm you've locked the mood reference before I send the first prompt.
```

This is a meta-pattern that doesn't generate an image; it primes the session.

## Pattern I — Failure recovery

```
[Upload a V-REJECT image that's worth recovering]

This image fails on: [name 1-2 specific failures]

Regenerate from the SAME composition, but:
- [explicit correction 1]
- [explicit correction 2]

Do not introduce other changes. Do not "improve" elements that don't need fixing. Surgical correction only.

Output 1 variant.
```

## Pattern J — Forensic verification

For when you suspect the model is "cheating" (using slightly different hex than the tokens):

```
[Upload a V-PASS image you want to verify]

Examine this image. For each visible color in the image, identify which design token (from master context) it corresponds to. Output a table:

| Element | Visible color (approx hex) | Intended token | Match? |
|---|---|---|---|

If any element does NOT cleanly map to a token, flag it. Do NOT regenerate yet — just audit.

After audit, I'll decide whether to regenerate or accept as V-CONCERN.
```

This uses the model itself as a self-audit tool. Useful when you have many images and need to spot drift.

---

# Sequencing rules

1. **Single-axis only**: One Pattern at a time. Do NOT combine "fix density + fix typography + fix color" in one delta — model will under-correct or over-correct.
2. **Anchor discipline**: Always upload the original V-PASS as base. Don't chain "winner-of-winner-of-winner" — drift compounds.
3. **Save intermediates**: Each evolution outcome → save with parent_id reference in INDEX.csv. If a 3-step evolution drifts off-target, you can roll back.
4. **Limit chain length**: Don't go more than 3 evolution steps from any single anchor. After step 3, decide: accept, re-anchor (treat current as new anchor), or abandon.

# When to give up and re-shoot

If you've run 5+ evolution attempts on one image and it's still V-CONCERN:
- The base image is probably the wrong starting point
- Go back to a different V-PASS from the same session, or re-issue the original session prompt with explicit constraint correction

Don't sink-cost into evolution chains.

# INDEX.csv tracking for evolutions

Every evolved image gets:
- new `pfv_id` (e.g., `pfv-S04-03-evo-A` for first density evolution of S04 image #3)
- `parent_id` field filled with the source pfv_id
- `evolution_pattern` field with the Pattern letter (A through J)
- `delta_axis` field describing the single-axis change
- new V-verdict (could be V-PASS even if parent was V-CONCERN)

This lets you reconstruct the evolution graph at P8 handoff time.
