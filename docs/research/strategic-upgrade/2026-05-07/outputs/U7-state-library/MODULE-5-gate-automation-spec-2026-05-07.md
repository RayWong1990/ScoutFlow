---
title: MODULE-5-gate-automation-spec-2026-05-07
status: candidate / not-authority / not-production-approval
claim_label: ≥95% candidate-spec confidence
request_date_label: 2026-05-07
generated_at_actual: 2026-05-06
write_enabled: false
boundary: spec-only; no apps/** mutation; no screenshots generated
---

# MODULE-5-gate-automation-spec-2026-05-07

> 口径：本文件是 U7 candidate spec，不是 authority，不批准 runtime、frontend implementation、package install、browser automation、migration、vault true write 或 production 修改。文件名沿用用户 prompt 的 2026-05-07；实际生成环境日期为 2026-05-06。所有 “state” 都是可注册、可审计、可迁移的视觉状态，不等同于当前组件已经有完整可控 props。

## Source snapshot used

| Surface | Path / source | Evidence read | Confidence |
|---|---|---|---|
| URL Bar | `apps/capture-station/src/features/url-bar/UrlBar.tsx` | `value`, `isSubmitting`, `errorMessage`, `isManualUrlReady`, sample suggestions, role=alert branch | high |
| Live Metadata | `apps/capture-station/src/features/live-metadata/LiveMetadataPanel.tsx` | static `metadataRows` for platform/probe/evidence/audio_transcript | medium-high; state props absent |
| Capture Scope | `apps/capture-station/src/features/capture-scope/CaptureScopePanel.tsx` | `scopeRows` with allowed / blocked / candidate and status colors | high |
| Trust Trace | `apps/capture-station/src/features/trust-trace/TrustTraceGraph.tsx` | `nodes` with ready / pending / blocked projection graph | high |
| Topic Card Preview | `apps/capture-station/src/features/topic-card-preview/TopicCardPreviewCandidate.tsx` + `topicCardLite.ts` | data model, review steps, metrics, counterNote | high |
| Topic Card Vault | `apps/capture-station/src/features/topic-card-vault/TopicCardVaultCandidate.tsx` + data file | write_disabled gate, evidence balance, markdown preview | high |
| Four Panel Shell | `apps/capture-station/src/layout/FourPanelShell.tsx` | `captureId`, `previewState` idle/loading/error/ready and reset flow | high |
| Main Navigation | `apps/capture-station/src/layout/panels.ts` + shell header | `PANEL_SPECS` lists four core panels; eight-panel nav is candidate state-library route | medium; explicit nav component not found |


## 1. What should be automated and what must stay human

The 5-Gate model is valuable only if it refuses fake certainty. A visual automation harness can catch measurable defects, but it cannot honestly decide whether the screen feels balanced, whether the hierarchy matches product intent, or whether the composition has the right emotional weight for ScoutFlow. U7 therefore splits the five gates into **automatic**, **partial automatic**, and **human-final** categories:

| Gate | Name | Automation status | Machine output | Human requirement |
|---|---|---:|---|---|
| Gate 1 | visual hierarchy | assist only | primary/secondary area ratio, heading/body ratio, contrast prominence, focus order | final pass/fail required |
| Gate 2 | spacing alignment | partial auto | 8dp/4dp grid deviation, bounding-box gutters, baseline drift, overflow | human spot-check on intentional exceptions |
| Gate 3 | occlusion safety | partial auto | viewport overflow, overlap, safe-area intrusion, clipped actionable controls | human spot-check on complex overlays |
| Gate 4 | typography legibility | auto for measurable criteria | font size, line-height, text contrast ratio, text overflow, word-break | human only for prose quality |
| Gate 5 | visual weight | assist only | saturation/luminance imbalance, accent density, component area heatmap | final pass/fail required |

This matrix protects the prompt boundary: the subjective gates are never “passed by AI”. They can be scored, sorted and queued, but a human must check them off.

## 2. Headless audit architecture

Recommended flow:

```text
state_library rows
  -> render state browser route /?state_id=...
  -> Playwright opens viewport(s)
  -> collect DOM boxes, computed styles, screenshots
  -> run Gate 2/3/4 checks + Gate 1/5 assist metrics
  -> write state_gate_audit.machine_report_json
  -> enqueue human review for Gate 1 and Gate 5
  -> after human review, update state_library.five_gate_status
```

No production app mutation is required. The state browser can run locally in preview mode; the audit script consumes rows from SQLite and writes reports. In CI, the same script can be read-only except for test artifact output. In local commander mode, it may write to the U4/U7 database only after an explicit dispatch.

## 3. Gate 4 typography legibility: fully measurable subset

Gate 4 should be the strictest automation gate because it is the easiest to measure truthfully. For every visible text node or text-bearing element, collect:

- `font-size` in px
- `line-height` in px or computed normal
- foreground color and effective background color
- contrast ratio using WCAG relative luminance math
- bounding client rect and scrollWidth/clientWidth for truncation
- element role, disabled state, aria-hidden state, and whether text is decorative

Default thresholds:

| Text kind | Font / line-height | Contrast threshold | Notes |
|---|---|---:|---|
| normal body text | font-size ≥ 12px, preferred ≥ 13px; line-height ≥ 1.35 | ≥ 4.5:1 | small labels must still pass unless purely decorative |
| large text | ≥ 18.66px bold or ≥24px normal | ≥ 3:1 | ScoutFlow headings usually exceed this |
| disabled controls | advisory only | target ≥ 3:1 when possible | disabled state may be exempt but should not hide critical information |
| focus/outline/icon | visible non-text UI | ≥ 3:1 | do not rely on color alone |

The fetched TSX literals already show one useful risk: `#6d8099` on `#111f31` is about `4.11:1`, below the normal-text `4.5:1` threshold. If that muted color is used for 12px label text, automation should fail Gate 4 unless the element is decorative/disabled and marked as exempt. Primary text pairs such as `#eef4ff` on `#111f31` are much higher and should pass.

## 4. Gate 2 spacing and alignment: partial automation

ScoutFlow’s current component styles use a mix of 8/10/12/14/16/24 px spacing. A strict “every value must be multiple of 8” rule would create false positives because micro-spacing around chips and text fields often uses 4px increments. Candidate rule:

- Macro containers: margin/padding/gap should align to 8px grid with ±1px tolerance.
- Micro elements: chips, text padding, inline badges may use 4px grid with explicit `micro_token` classification.
- Baseline alignment: headings in sibling cards should start within 2px vertical drift unless there is intentional content asymmetry.
- Gutters: shell grid gutters should be 24px or another explicit token; mixed `14px` two-column gap in TopicCard surfaces should be flagged for review, not automatic fail.
- Panel border radius: repeated 8px/10px/999px patterns are acceptable if tokens name them (`radius_panel`, `radius_control`, `radius_pill`).

Machine report fields:

```json
{
  "gate_2_spacing": {
    "status": "warn",
    "macro_grid_violations": [
      {"selector":"[data-testid=topic-card-preview-candidate] > div", "gap_px":14, "expected":"8px or 16px token"}
    ],
    "baseline_drift_px": 1.2,
    "max_gutter_deviation_px": 0
  }
}
```

Gate 2 should fail only for clear geometry bugs: overlapping spacing, off-grid shell gutters, clipped content due to insufficient padding, or inconsistent panel alignment across the same row. Everything else becomes a human-review warning.

## 5. Gate 3 occlusion safety: partial automation

Occlusion safety means no important text/control is hidden, clipped, overlaid, or outside the safe viewport. For web/H5, the script can test:

1. `rect.right <= viewport.width` and `rect.bottom <= viewport.height` for visible critical elements.
2. `elementFromPoint` at control center resolves to the same element or a child; otherwise an overlay is blocking it.
3. `scrollWidth > clientWidth` or `scrollHeight > clientHeight` on text containers without intentional scroll styling.
4. Safe-area padding on mobile viewport and notched devices, using `env(safe-area-inset-*)` emulation where available.
5. Footer/pre blocks with `white-space: pre-wrap` do not cover buttons or badges.
6. Error banners with role=alert do not push primary action off-screen at 375×812.

This gate should cover desktop, tablet and mobile viewports. It is not enough to test only 1360×900 because the shell has two/three-column grids that can collapse badly on small screens. If responsive behavior is not implemented, Gate 3 should produce a “viewport unsupported / human decision required” result rather than claiming pass.

## 6. Gate 1 visual hierarchy: assistive metrics only

Hierarchy is a product judgment. The machine can provide:

- main heading bounding box area / secondary label area ratio
- largest accent element area and color contrast vs background
- focus order sequence compared with visible order
- h1/h2/h3 count and font-size progression
- primary CTA prominence vs secondary chips
- top-of-panel scan path: label → title → summary → status → actions

But the human must decide whether the hierarchy communicates “manual_url metadata-only capture station” rather than “general media downloader” or “vault commit UI”. For example, UrlBar’s cyan Create Capture button is visually strong; it is acceptable only if the surrounding copy keeps the manual_url and metadata-only constraints visible. Automation can flag a high CTA ratio; it cannot decide intent.

Human review fields:

```yaml
gate_1_visual_hierarchy:
  reviewer: <name-or-initials>
  verdict: pass|fail|revise
  required_observation: "What does the eye read first? Does that match the state intent?"
  evidence_asset_id: <visual_asset_id>
  note: <free text>
```

## 7. Gate 5 visual weight: assistive metrics only

Visual weight covers density, saturation, accent distribution and emotional balance. The machine can compute luminance histograms, accent-color count, area-weighted saturation, and component area heatmaps. It can flag obvious risk such as too many red badges, overly dense markdown preview blocks, or cyan accents appearing on every small item. It still cannot decide if the screen feels trustworthy or aesthetically appropriate.

Candidate machine metrics:

- accent pixel ratio for cyan/green/red/yellow families
- total card density: text node count / panel area
- max text column width
- pre/code block area ratio in vault surfaces
- alert color dominance when error state is shown
- muted color ratio for secondary copy

Human review question: “Does this state look like a calm audit workstation, or does visual weight imply urgency/capability that the product boundary does not approve?”

## 8. Audit report schema

```json
{
  "audit_run_id": "u7-2026-05-07-local-001",
  "state_id": "url_bar.error.create_capture_error",
  "viewport": "desktop-1360x900",
  "screenshot_asset_id": "va_...",
  "gate_1_hierarchy": {"machine_score": 0.82, "status": "human_pending"},
  "gate_2_spacing": {"status": "pass", "violations": []},
  "gate_3_occlusion": {"status": "pass", "violations": []},
  "gate_4_typography": {"status": "fail", "violations": [{"text":"url-bar", "ratio":4.11, "threshold":4.5}]},
  "gate_5_visual_weight": {"machine_score": 0.74, "status": "human_pending"},
  "final_machine_status": "human_pending",
  "boundary_flags": ["screenshot_only_not_visual_approval"]
}
```

## 9. Headless implementation sketch

The script should use Playwright when possible because capture-station already has a visual/e2e testing trajectory. Puppeteer is acceptable for a tiny standalone proof, but Playwright’s multi-browser and viewport ergonomics make it better for state matrix work.

```ts
import {{ chromium }} from '@playwright/test';
import {{ readStates, writeAudit }} from './state-db';
import {{ contrastRatio, collectTextNodes, collectBoxes }} from './audit-metrics';

const viewports = [
  {{ name: 'desktop-1360x900', width: 1360, height: 900 }},
  {{ name: 'tablet-834x1112', width: 834, height: 1112 }},
  {{ name: 'mobile-390x844', width: 390, height: 844 }},
];

for (const state of await readStates()) {{
  for (const vp of viewports) {{
    const browser = await chromium.launch();
    const page = await browser.newPage({{ viewport: {{ width: vp.width, height: vp.height }} }});
    await page.goto(`http://127.0.0.1:5173/state-library?state_id=${{state.state_id}}`);
    const textNodes = await collectTextNodes(page);
    const boxes = await collectBoxes(page);
    const typography = textNodes.map((n) => contrastRatio(n.fg, n.bg));
    const report = {{ state_id: state.state_id, viewport: vp.name, typography, boxes }};
    await page.screenshot({{ path: `artifacts/${{state.state_id}}-${{vp.name}}.png`, fullPage: true }});
    await writeAudit(report);
    await browser.close();
  }}
}}
```

## 10. Human queue

Subjective review must be first-class rather than a comment in a report. Add a queue table:

```sql
CREATE TABLE IF NOT EXISTS human_visual_review_queue (
  queue_id TEXT PRIMARY KEY,
  state_id TEXT NOT NULL REFERENCES state_library(state_id),
  audit_id TEXT NOT NULL REFERENCES state_gate_audit(audit_id),
  gate_name TEXT NOT NULL CHECK (gate_name IN ('gate_1_visual_hierarchy','gate_5_visual_weight')),
  priority TEXT NOT NULL DEFAULT 'normal',
  screenshot_asset_id TEXT NOT NULL,
  machine_summary TEXT NOT NULL,
  reviewer TEXT NULL,
  verdict TEXT NOT NULL DEFAULT 'pending' CHECK (verdict IN ('pending','pass','fail','revise')),
  reviewed_at TEXT NULL,
  review_note TEXT NOT NULL DEFAULT ''
);
```

The final `five_gate_status='human_pass'` is legal only when Gate 2/3/4 have pass or approved warning status and both subjective queue rows are pass. If a human says revise, the state remains registered but not approved; the screenshot may remain as evidence of a failed state.

## 11. Integration with visual_asset state machine

Automation should update visual_asset only after a screenshot exists. Proposed fields:

- `visual_asset.state_id` or join table from visual_asset to state_library
- `visual_asset.five_gate_audit_passed` boolean, default false
- `visual_asset.five_gate_audit_id` nullable text
- `visual_asset.human_review_required` boolean, true for all U7 state screenshots
- `visual_asset.audit_status` enum: `not_run / machine_failed / human_pending / human_passed / human_failed`

This avoids a common failure mode: a screenshot is uploaded, someone sees it, and the project treats it as “visual approved”. Under U7, screenshot attachment and visual approval are separate states.

## 12. Acceptance and redlines

- No subjective gate is marked auto-pass.
- Contrast ratios are computed and written for text elements.
- Spacing/occlusion checks run across at least three viewports or explicitly mark smaller viewports as unsupported.
- Machine report includes selectors and numeric evidence, not generic prose.
- Human review queue is non-empty for every screenshot-bearing state.
- The script does not create captures, call BBDown, use ffmpeg, call ASR, read cookies, or write vault files.
- CI may produce test artifacts; production data writes require explicit dispatch.


## 13. Selector and metric conventions

Automation must produce reviewable evidence, not mystery scores. Every violation should include selector, text sample if relevant, bounding box, viewport, threshold and observed value. Avoid reports like “spacing failed”. Prefer:

```json
{
  "gate": "gate_2_spacing",
  "selector": "[data-testid=topic-card-preview-candidate] article:nth-of-type(2)",
  "viewport": "mobile-390x844",
  "metric": "right_overflow_px",
  "observed": 32,
  "threshold": 0,
  "severity": "fail",
  "note": "second column grid did not collapse"
}
```

This format lets the reviewer locate the defect without re-running the script. It also lets the project compare regressions over time.

## 14. Viewport policy

Use three default viewports:

- desktop: `1360×900` because the shell max width is 1360 and current layout uses multi-column grids;
- tablet: `834×1112` because it stresses two-column layout and vertical density;
- mobile: `390×844` because it exposes horizontal overflow and safe-area risks.

If a production component intentionally supports desktop only, the mobile result should be `unsupported_requires_decision`, not pass. A human can decide whether mobile support is out-of-scope for that state. The report must not hide unsupported viewports because the prompt explicitly wants browser-style state browsing and visual safety.

## 15. Gate 2 algorithm details

The spacing algorithm should walk visible panels and collect:

- outer panel rects and grid columns;
- parent `display:grid` / `display:flex` gaps;
- padding and margin values;
- card-to-card gutter consistency;
- heading top alignment within sibling cards;
- repeated radius and border values.

Pseudo-rules:

```text
if container is shell or panel grid:
  require gap in {16, 24, 32} or token_exception
if element is chip/badge/control:
  allow padding in {4, 6, 8, 10, 12, 14} but warn when not tokenized
if sibling cards share a row:
  heading_y_delta <= 2px unless content_top_variance_allowed
if panel padding:
  prefer 16px or 24px; fail below 12px for dense card content
```

This intentionally avoids a brittle “every number multiple of 8” rule. ScoutFlow’s current code uses 10px and 14px in controls. A good audit should identify and classify these, not explode into false failures.

## 16. Gate 3 algorithm details

Occlusion safety should be evaluated at three layers:

1. **Viewport containment**: visible critical elements fit inside viewport or intentional scroll containers.
2. **Overlap**: controls are not covered by overlays or adjacent blocks.
3. **Content clipping**: text, pre blocks and badges are not clipped in a way that changes meaning.

The `elementFromPoint` test is useful for controls:

```ts
const center = { x: rect.x + rect.width / 2, y: rect.y + rect.height / 2 };
const hit = await page.evaluate(({x,y}) => document.elementFromPoint(x,y)?.outerHTML, center);
```

If the hit element is not the button or a child, report occlusion. For text blocks, use overflow metrics instead. For pre blocks, allow internal scrolling only if the scroll affordance is visible and does not hide primary actions.

## 17. Gate 4 remediation policy

When Gate 4 fails, do not jump directly to redesign. Categorize failures:

| Failure | Likely fix | Notes |
|---|---|---|
| muted 12px text ratio <4.5 | adjust token color | most likely in current code |
| long URL clipped | add word-break or max width | target paths already use word-break in some places |
| line-height too low | raise line-height token | body copy currently often 1.45, likely OK |
| uppercase 11px badge hard to read | increase size or contrast | status badges are meaningful |
| disabled button unreadable | add adjacent explanatory text | disabled control itself may be exempt |

A failed Gate 4 should block `human_pass` regardless of subjective approval. Human reviewers should not override numeric accessibility failures unless the element is truly decorative and documented.

## 18. Gate 1 human review rubric

For every state screenshot, ask the reviewer to answer these questions:

1. What is the first thing your eye reads?
2. Does that match the state’s semantic intent?
3. Is the boundary copy visible enough, especially `write_disabled`, `preview_only`, `manual_url_only`, or blocked runtime language?
4. Does the primary action imply an unapproved capability?
5. In error states, does the error dominate appropriately without hiding recovery context?
6. In loading states, is pending status visible without pretending completion?

The reviewer can pass only if the visual order communicates the correct product boundary. A beautiful screenshot that implies “vault commit is ready” must fail.

## 19. Gate 5 human review rubric

Visual weight review asks whether the screen feels balanced for an audit workstation. The reviewer should inspect:

- number and intensity of accent colors;
- density of markdown/pre blocks;
- balance between status badges and explanatory text;
- whether red/yellow alerts create panic beyond the state intent;
- whether cyan primary buttons overpower boundary warnings;
- whether blocked/candidate badges are visible but not sensationalized.

Machine metrics can sort likely problems. Final judgment is human because visual weight depends on composition, product tone and trust.

## 20. Failure handling

A state can fail in three ways:

- **machine_fail**: contrast, clipping, overlap or severe spacing issue;
- **human_fail**: hierarchy/weight does not match intent;
- **blocked**: no screenshot, stale screenshot, unsupported viewport, or source drift.

Failed states stay registered. The registry should not delete failures. The failure report is useful evidence for PF-V, designers and future regression checks.

## 21. Commands and outputs

Candidate local commands:

```bash
python tools/u7_seed_state_library.py --db .u7/state-library.sqlite
npm run dev --workspace apps/capture-station
python tools/u7_audit_states.py --db .u7/state-library.sqlite --viewport desktop-1360x900
python tools/u7_export_human_queue.py --db .u7/state-library.sqlite --out .u7/human-queue.md
```

Expected artifacts:

```text
.u7/audit-runs/u7-001/report.jsonl
.u7/audit-runs/u7-001/screenshots/*.png
.u7/audit-runs/u7-001/human-queue.md
.u7/audit-runs/u7-001/summary.md
```

These paths are illustrative. The actual repo path must be authorized by a later dispatch.

## 22. CI posture

CI should initially run in report-only mode. It can fail on syntax or missing required rows, but visual pass/fail should not block production until the human review process is proven. Once stable, CI can fail on Gate 4 contrast and severe Gate 3 occlusion because those are objective. Gate 1 and Gate 5 should never be CI auto-pass gates.


## 23. Audit status calculation rules

Final status should be calculated, not hand-written. Candidate logic:

```text
if screenshot missing or stale:
  final_status = blocked
else if Gate 4 typography fails:
  final_status = machine_failed
else if Gate 3 severe occlusion fails:
  final_status = machine_failed
else if Gate 2 severe shell spacing fails:
  final_status = machine_failed
else if Gate 1 human verdict missing or Gate 5 human verdict missing:
  final_status = human_pending
else if Gate 1 or Gate 5 human verdict is fail/revise:
  final_status = human_failed
else:
  final_status = human_passed
```

Warnings do not disappear. A human-passed state can still retain warnings in its report. The final pass means the warnings were judged acceptable for that state, not that the screenshot is mathematically perfect.

## 24. Machine score humility

Scores must be phrased as ranking aids. A `hierarchy_score=0.82` does not mean 82% visually good. It means the heuristic observed strong heading/action prominence or an expected scan path. The report should say `machine_assist_score`, not `quality_score`. This keeps the spec aligned with the hard boundary that subjective gates cannot be faked.

## 25. Reduced-motion and loading states

Loading states often use animation. If PF-V or future H5 adds shimmer/spinner behavior, the audit runner should emulate reduced motion:

```ts
await page.emulateMedia({ reducedMotion: 'reduce' });
```

Then screenshot both normal and reduced-motion only if animation is visually material. For U7 v1, animation can be out-of-scope, but loading states should not rely on motion alone. Text such as `loading`, `submitting capture...`, or `metadata probe pending` must remain visible.

## 26. Color-only communication guard

CaptureScope and TrustTrace use green/red/yellow/cyan status colors. The text labels (`allowed`, `blocked`, `candidate`, `ready`, `pending`) must remain visible. Gate 4 validates contrast; Gate 1 human review validates that the text is readable in the scan path. A color dot without text is not enough for state meaning.

## 27. Report retention

Keep reports for failed and stale states. The historical sequence is useful:

```text
u7-001: url_bar.error failed contrast
u7-002: token fix applied, machine pass, human pending
u7-003: human pass after hierarchy review
```

This sequence gives PF-V and future regression work a factual trail. Do not overwrite reports in place; write run ids and compare.

## 28. Integration with existing Wave 4/Wave 5 posture

The local audit pack records prior visual reporting and Playwright harness work but also says screenshots and human visual verdict were not proven. U7 should extend that posture: it can create a better framework for proof, but it must not retroactively claim proof. Every stdout and README should preserve the distinction between static readiness, automated execution, screenshot evidence and human verdict.


## 29. Human handoff markdown shape

Human reviewers should receive a compact card, not a raw JSON blob:

```markdown
# Human visual review: topic_card_preview.full.reviewed_handoff_candidate

- screenshot: va_...
- viewport: desktop-1360x900
- machine summary: Gate 2 pass; Gate 3 pass; Gate 4 pass; hierarchy assist score 0.78; weight assist score 0.64
- required checks:
  - Gate 1: Does the eye read title → summary → review state → counter-note in the intended order?
  - Gate 5: Does markdown/evidence density feel balanced and not too heavy?
- boundary copy that must remain visible: preview_only, handoff_candidate, human usefulness verdict pending
- verdict: pass / fail / revise
```

This format is easy to audit and can be generated from the queue table. It also reduces reviewer fatigue because every question is tied to state intent.

## 30. Data minimization

The audit runner should store only what it needs: selector, computed style values, ratios, bounding boxes, screenshot hash and reviewer notes. It should not store full page HTML unless explicitly needed, because HTML can contain local paths or source details. If full HTML is required for debugging, save it in a local-only artifact folder and do not promote it to DAM.
