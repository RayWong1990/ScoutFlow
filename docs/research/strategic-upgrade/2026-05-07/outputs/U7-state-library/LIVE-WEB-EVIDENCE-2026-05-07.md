---
title: LIVE-WEB-EVIDENCE-2026-05-07
status: candidate / not-authority / not-production-approval
claim_label: not claimed: live web disabled; refresh checklist only
request_date_label: 2026-05-07
generated_at_actual: 2026-05-06
write_enabled: false
boundary: spec-only; no apps/** mutation; no screenshots generated
---

# LIVE-WEB-EVIDENCE-2026-05-07

> 口径：本文件是 U7 candidate spec，不是 authority，不批准 runtime、frontend implementation、package install、browser automation、migration、vault true write 或 production 修改。文件名沿用用户 prompt 的 2026-05-07；实际生成环境日期为 2026-05-06。所有 “state” 都是可注册、可审计、可迁移的视觉状态，不等同于当前组件已经有完整可控 props。


## 1. Truthful status

The original cloud prompt requested at least fifteen live web searches covering Storybook, visual regression vendors, a11y audit tools, WCAG 2.2, Apple HIG, Material 3, token tools and image tools. In this execution environment, live web browsing is disabled. Therefore this file is **not** a live-verified evidence report. It is a refresh checklist and adoption analysis scaffold. It must not be promoted as “visited URL evidence”.

This is a deliberate truth-preserving downgrade. Fabricating vendor visits would be worse than delivering a partial evidence file. The rest of the U7 package can still specify state-library and 5-Gate automation because it uses uploaded prompt, local audit pack and GitHub connector evidence. The web-evidence pass remains blocked until a browsing-enabled environment runs it.

## 2. Refresh checklist, not live evidence

| Target | U7 relevance | URL to refresh | Status |
|---|---|---|---|
| Storybook | component state browser/story source of truth | `https://storybook.js.org/` | Not live verified in this environment; refresh official docs for current major version and portable stories. |
| Chromatic | hosted visual regression + Storybook integration | `https://www.chromatic.com/` | Not live verified; verify pricing, CI integration and Storybook compatibility. |
| Percy | visual regression screenshots | `https://percy.io/` | Not live verified; verify current Playwright SDK behavior. |
| Loki | open-source visual regression for Storybook | `https://loki.js.org/` | Not live verified; check maintenance status before adoption. |
| Playwright | headless browser rendering, screenshot and viewport testing | `https://playwright.dev/` | Not live verified; local repo already has Playwright trajectory. |
| Puppeteer | headless Chromium screenshot fallback | `https://pptr.dev/` | Not live verified; candidate fallback, not preferred. |
| axe-core | automated accessibility rule engine | `https://github.com/dequelabs/axe-core` | Not live verified; useful adjunct but contrast sampling still needs state-specific report. |
| Lighthouse | browser audit including accessibility | `https://developer.chrome.com/docs/lighthouse/` | Not live verified; coarse page-level audit, not enough for 48 state matrix alone. |
| pa11y | command-line accessibility testing | `https://pa11y.org/` | Not live verified; useful for CI text reports. |
| WCAG 2.2 | contrast and accessibility normative reference | `https://www.w3.org/TR/WCAG22/` | Not live verified; refresh exact success criteria before authority use. |
| Apple Human Interface Guidelines | platform design guidance | `https://developer.apple.com/design/human-interface-guidelines/` | Not live verified; use for qualitative guidance only. |
| Material 3 | design system guidance and expressive direction | `https://m3.material.io/` | Not live verified; do not transplant material styling into ScoutFlow automatically. |
| Tokens Studio | design tokens pipeline from Figma | `https://tokens.studio/` | Not live verified; useful if PF-V tokenizes palette/spacing. |
| Style Dictionary | token transformation pipeline | `https://styledictionary.com/` | Not live verified; candidate for token export only. |
| Bit Cloud | component composition/catalog reference | `https://bit.cloud/` | Not live verified; likely overkill for single-user U7. |
| BackstopJS | open-source visual regression screenshots | `https://github.com/garris/BackstopJS` | Not live verified; alternative to Playwright screenshot diff. |
| Figma Variables/Tokens | design token source-of-truth option | `https://help.figma.com/` | Not live verified; use only as reference if PF-V works in Figma. |
| Pixelmator / Photomator | image tooling inspiration | `https://www.pixelmator.com/` | Not live verified; not part of automation stack. |
| Affinity | image tooling inspiration | `https://affinity.serif.com/` | Not live verified; not part of automation stack. |

## 3. How to perform the missing live refresh

A future browser-enabled operator should do the following:

1. Visit each URL above and record actual access date, page title, stable URL and retrieved version claim.
2. For tools with versioned docs, record current major version and release notes relevant to 2026.
3. Distinguish vendor marketing claims from docs/API guarantees.
4. Check whether open-source projects are actively maintained.
5. Confirm whether Storybook/Chromatic/Percy/Loki/Backstop support the current ScoutFlow stack without package policy changes.
6. Confirm WCAG 2.2 thresholds and any active WCAG 3 draft status separately; do not mix drafts into pass/fail criteria.
7. Record whether Apple HIG and Material 3 are used only as design references, not binding product authority.
8. Record whether Tokens Studio/Style Dictionary are useful enough for a single-user budget.
9. Append screenshots or saved HTML only if policy permits and no credentials are involved.
10. Update this file’s claim label after live verification.

## 4. Preliminary adoption analysis without live claims

### Storybook vs tiny browser

Storybook is excellent when a team needs rich component docs, addon ecosystem, design review, and hosted visual regression. U7’s immediate need is narrower: register 48 states, render them, screenshot them, and audit them. A tiny browser can be under 300 lines and avoids new package decisions. Recommendation: implement tiny browser first; keep state rows Storybook-compatible so future adoption is easy.

### Chromatic/Percy/Loki/Backstop

Hosted tools reduce operational burden but may add cost and CI coupling. Open-source tools avoid vendor lock but may require maintenance. For ScoutFlow’s single-user local-first model, Playwright screenshot + U7 state registry is the leanest starting point. External visual regression tools become useful once the state matrix is stable and package/CI policy approves them.

### axe-core/Lighthouse/pa11y

These tools can find many accessibility defects, but they do not replace explicit contrast reports attached to each state. U7 should treat them as adjuncts. For the prompt’s hard boundary, the minimum is measured contrast ratio per text/control pair. Axe or Lighthouse pass alone is not enough.

### Design systems and token tooling

Material 3 and Apple HIG can inform spacing, type and accessibility expectations, but ScoutFlow should not import their visual language wholesale. Tokens Studio and Style Dictionary become useful if PF-V formalizes colors/spacing/radii into tokens. Until then, the audit can parse computed styles directly.

### Pixelmator/Affinity and image tools

These are not automation dependencies. They may help manual image preparation or visual inspiration, but they do not belong in the state-library quality pipeline. Do not let image-editor exploration distract from measurable state evidence.

## 5. Required future evidence format

```yaml
live_web_refresh:
  refreshed_at: <actual date/time>
  operator: <name/tool>
  entries:
    - target: Storybook
      url: https://storybook.js.org/
      page_title: <actual>
      version_or_claim: <actual>
      relevance: <actual>
      adopted_in_u7: yes|no|deferred
      notes: <actual>
```

## 6. Self-audit finding for this file

- `live_web_browsing_used=false`.
- `live_verified_count=0`.
- Claim label is intentionally downgraded.
- Do not cite this file as proof that vendors were visited.
- Use it only as the checklist for the missing Pass 2.


## 7. Decision matrix to use after refresh

| Category | Preferred if live refresh confirms | Defer if | U7 v1 decision before refresh |
|---|---|---|---|
| State browser | Storybook portable stories or tiny browser | package policy unclear | tiny browser |
| Screenshot automation | Playwright screenshots | browser automation still blocked | spec only, no run |
| Hosted visual regression | Chromatic/Percy | cost/CI coupling too high | defer |
| Open-source visual regression | Loki/Backstop | maintenance stale | defer |
| A11Y engine | axe-core/pa11y adjunct | setup cost high | contrast custom first |
| Standards | WCAG 2.2 official | cannot verify exact text | baseline only, not authority |
| Design guidance | Apple HIG/Material 3 | conflicts with ScoutFlow visual language | reference only |
| Tokens | Tokens Studio/Style Dictionary | PF-V has no token source | defer |
| Image tooling | Pixelmator/Affinity | irrelevant to automation | not adopted |

## 8. Search queries to run in browser-enabled environment

Use focused queries and record dates:

```text
Storybook 8 visual testing portable stories 2026
Chromatic Storybook Playwright visual regression 2026
Percy Playwright screenshot visual testing current docs
Loki Storybook visual regression maintenance status 2026
BackstopJS visual regression current maintenance
axe-core Playwright accessibility testing 2026
pa11y CI accessibility testing current docs
Lighthouse accessibility audit contrast limitations
Playwright screenshot visual comparisons current docs
Puppeteer screenshot fullPage current docs
WCAG 2.2 contrast success criterion current W3C
Apple Human Interface Guidelines accessibility visual design 2026
Material 3 expressive design accessibility 2026
Tokens Studio Figma tokens current docs
Style Dictionary design tokens current docs
```

The search result itself is not enough. Open the relevant official pages and record the official URL. Avoid citing scraped summaries when official docs exist.

## 9. Evidence entry template

Each live entry should have this shape:

```markdown
### Storybook

- visited_at: 2026-05-07T<time><tz>
- official_url: <actual>
- page_title: <actual>
- observed_version_or_current_claim: <actual>
- relevant_to_u7: yes/no/deferred
- key_takeaway: <one sentence>
- adoption_decision: adopt/defer/reject/reference-only
- caveat: <one sentence>
```

The adoption decision should be conservative. A tool can be excellent and still be deferred if it breaks single-user budget or package policy.

## 10. Why live web matters here

Tool status changes quickly. Storybook major versions, visual regression vendor features, token tools and browser APIs can shift after the model knowledge cutoff. Standards pages also matter because accessibility claims should cite the official text. That is why this file refuses to call itself evidence. It is safer to deliver no live claim than a stale claim disguised as research.

## 11. Current non-live technical stance

Even without live refresh, the design direction is clear enough for a candidate spec:

- Use Playwright-style browser rendering for headless state screenshots and DOM metrics.
- Use custom contrast math because it is small, auditable and required by the prompt.
- Use a tiny browser first because it avoids package decisions.
- Keep Storybook compatibility by generating stories later from state rows.
- Defer hosted visual regression until screenshot matrix stabilizes.
- Treat design systems as references, not imported visual authority.

These are candidate decisions, not post-refresh conclusions.

## 12. Required update after live refresh

After live refresh, update:

- `live_web_browsing_used: true`;
- `live_verified_count: <number>`;
- claim label from `not claimed` to a percentage tied to actual evidence;
- vendor table statuses from `Not live verified` to `visited_at=...`;
- adoption matrix decisions if current docs contradict this candidate stance.

If only some pages can be accessed, keep partial counts. Do not round up to fifteen.

## 13. Common false claims to avoid

- “Storybook is current” without recording version/page.
- “Chromatic supports our stack” without checking docs and package constraints.
- “axe-core proves WCAG compliance” when it only finds rule violations and may miss state-specific contrast contexts.
- “Material 3 expressive should be adopted” when ScoutFlow has its own visual language.
- “WCAG 3 changed contrast” without separating draft guidance from enforceable WCAG 2.2 criteria.
- “Pixelmator AI helps visual regression” when it is image editing, not audit automation.

## 14. Status summary

This file intentionally fails the prompt’s live-web requirement. It is still useful because it makes the missing work explicit, lists the targets, and prevents hallucinated citations. The rest of the package should be reviewed as a repo/prompt/local-evidence candidate spec with one known external-evidence gap.


## 15. Live refresh scoring rubric

After browsing is available, score each source:

| Score | Meaning |
|---|---|
| 0 | inaccessible or irrelevant |
| 1 | accessible but stale or not useful |
| 2 | useful reference but no adoption impact |
| 3 | directly informs U7 but not adopted in v1 |
| 4 | adopted as candidate implementation input |
| 5 | adopted and validated against repo constraints |

The final evidence confidence should not be the average of vendor scores. It should be based on whether the required categories were covered: component state browser, visual regression, a11y audit, contrast standard, design guidance, token tooling and image-tool non-adoption.

## 16. Expected likely outcomes to verify

These are hypotheses, not live facts:

- Playwright remains the most practical local screenshot/DOM metric runner.
- Storybook remains valuable but heavier than a tiny U7 browser for v1.
- Hosted visual regression remains optional because ScoutFlow is single-user/local-first.
- Axe/Lighthouse/pa11y remain useful but insufficient for per-state contrast proof alone.
- WCAG 2.2 remains the safest official baseline for contrast thresholds.
- Token tools become useful only after PF-V wants palette/spacing governance.

The live refresh should confirm, correct, or reject these hypotheses.

## 17. How to update package after refresh

Create a replacement file, not a silent edit, if audit trace matters:

```text
LIVE-WEB-EVIDENCE-2026-05-07.md              # current blocked scaffold
LIVE-WEB-EVIDENCE-REFRESHED-2026-05-07.md    # real browser run
```

Then update README stdout. If the user wants exactly nine files, replace the blocked scaffold in a new zip and record that replacement in README.

## 18. Why this downgrade does not invalidate the core specs

The core state-library and 5-Gate designs rely primarily on project state, component structure and stable accessibility math. Live web would strengthen tool/version recommendations, not change the core requirement that states be registered, screenshots linked, contrast measured and subjective gates human-reviewed. Therefore the package is still useful, but it is not fully complete against the original cloud prompt.


## 19. Minimum acceptable refreshed evidence count

The original requirement asked for at least fifteen searches. A useful refresh should cover at least these fifteen distinct targets:

1. Storybook official docs.
2. Chromatic official docs.
3. Percy official docs.
4. Loki official docs or repository.
5. BackstopJS official repository.
6. Playwright official docs.
7. Puppeteer official docs.
8. axe-core official repository/docs.
9. Lighthouse official docs.
10. pa11y official docs.
11. WCAG 2.2 official W3C recommendation.
12. Apple HIG accessibility/design page.
13. Material 3 current design page.
14. Tokens Studio official docs.
15. Style Dictionary official docs.

Pixelmator/Affinity can be additional non-adoption references, but they should not replace core automation/a11y sources.

## 20. Evidence freshness flags

Use freshness flags:

- `fresh_current`: official page visited and clearly current.
- `fresh_but_version_unclear`: official page visited but version not obvious.
- `stale_or_archived`: project appears unmaintained or archived.
- `vendor_marketing_only`: page is marketing, not docs.
- `blocked_access`: page inaccessible.

A source with `vendor_marketing_only` should not be used for technical implementation decisions.

## 21. Refresh failure handling

If fewer than fifteen sources can be verified, report the actual number. Do not retry with random blog posts just to hit a count. The evidence goal is trustworthy decision support, not numeric padding.
