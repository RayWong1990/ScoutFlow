---
title: A11Y-CONTRAST-VALIDATOR-2026-05-07
status: candidate / not-authority / not-production-approval
claim_label: ≥95% candidate-spec confidence
request_date_label: 2026-05-07
generated_at_actual: 2026-05-06
write_enabled: false
boundary: spec-only; no apps/** mutation; no screenshots generated
---

# A11Y-CONTRAST-VALIDATOR-2026-05-07

> 口径：本文件是 U7 candidate spec，不是 authority，不批准 runtime、frontend implementation、package install、browser automation、migration、vault true write 或 production 修改。文件名沿用用户 prompt 的 2026-05-07；实际生成环境日期为 2026-05-06。所有 “state” 都是可注册、可审计、可迁移的视觉状态，不等同于当前组件已经有完整可控 props。


## 1. Scope and truth boundary

This validator spec covers measurable accessibility checks for U7 states. It does not claim the current app is WCAG compliant. It defines how to measure contrast and typography for every rendered state. The sample ratios below were computed from color literals visible in the fetched TSX snippets, not from a live browser screenshot. A future authorized local run must re-measure against computed styles because nested backgrounds and disabled states can change the effective result.

## 2. Contrast rule baseline

Use the stable WCAG 2.x contrast model as baseline: relative luminance for foreground/background colors, ratio `(L1 + 0.05) / (L2 + 0.05)`, normal text threshold 4.5:1, large text threshold 3:1, and non-text UI/focus indicators target 3:1. Because live standards refresh was unavailable in this environment, this file marks the standards source as not-live-verified and requires local refresh before authority promotion.

## 3. Sample measured color pairs from current TSX literals

| fg token | fg | bg token | bg | measured ratio | result |
|---|---|---|---|---:|---|
| `text_primary` | `#eef4ff` | `bg_main` | `#07111b` | 17.21 | pass |
| `text_primary` | `#eef4ff` | `bg_panel` | `#111f31` | 15.05 | pass |
| `text_secondary` | `#a6b8cf` | `bg_panel` | `#111f31` | 8.21 | pass |
| `text_muted` | `#6d8099` | `bg_panel` | `#111f31` | 4.11 | fail for normal 12px |
| `cyan` | `#50d4ff` | `nav_chip` | `#16263c` | 8.86 | pass |
| `green` | `#7adf9b` | `bg_panel` | `#111f31` | 10.17 | pass |
| `red` | `#ff7b7b` | `bg_panel` | `#111f31` | 6.62 | pass |
| `pink` | `#ff9db2` | `alert_bg` | `#24131b` | 9.05 | pass |
| `yellow` | `#ffcf7a` | `bg_panel` | `#111f31` | 11.44 | pass |
| `orange` | `#ff9b7a` | `bg_panel` | `#111f31` | 8.09 | pass |
| `disabled_dark` | `#27415d` | `bg_panel` | `#111f31` | 1.58 | disabled/advisory only |

The important actionable finding is `#6d8099` on `#111f31`: ratio ≈ 4.11. That color appears as 12px labels in several components. Under normal text rules it fails 4.5:1. Fix options:

- raise muted label color to approximately `#7f95b0` or another token that passes;
- increase text size/weight only if it qualifies as large text, which 12px labels do not;
- mark truly decorative labels as exempt, but do not exempt panel labels or status labels that carry meaning;
- use token names so future audit does not chase raw hex literals.

## 4. Python contrast function

```python
from __future__ import annotations
import re

def _srgb_to_linear(channel: float) -> float:
    return channel / 12.92 if channel <= 0.04045 else ((channel + 0.055) / 1.055) ** 2.4

def _hex_to_rgb(color: str) -> tuple[float, float, float]:
    if not re.fullmatch(r"#[0-9a-fA-F]{6}", color):
        raise ValueError(f"expected #RRGGBB, got {color!r}")
    return tuple(int(color[i:i+2], 16) / 255 for i in (1, 3, 5))

def relative_luminance(color: str) -> float:
    r, g, b = (_srgb_to_linear(c) for c in _hex_to_rgb(color))
    return 0.2126 * r + 0.7152 * g + 0.0722 * b

def contrast_ratio(fg: str, bg: str) -> float:
    l1, l2 = relative_luminance(fg), relative_luminance(bg)
    light, dark = max(l1, l2), min(l1, l2)
    return (light + 0.05) / (dark + 0.05)

def passes_text_contrast(fg: str, bg: str, font_px: float, is_bold: bool = False) -> dict:
    ratio = contrast_ratio(fg, bg)
    is_large = font_px >= 24 or (is_bold and font_px >= 18.66)
    threshold = 3.0 if is_large else 4.5
    return {"ratio": round(ratio, 2), "threshold": threshold, "pass": ratio >= threshold}
```

## 5. Browser collection strategy

A real validator should not parse TSX and stop. It must render the state and collect computed styles:

```ts
async function collectTextContrast(page) {
  return await page.evaluate(() => {
    function visible(el) {
      const s = getComputedStyle(el);
      const r = el.getBoundingClientRect();
      return s.visibility !== 'hidden' && s.display !== 'none' && r.width > 0 && r.height > 0;
    }
    function bgFor(el) {
      let cur = el;
      while (cur) {
        const bg = getComputedStyle(cur).backgroundColor;
        if (bg && bg !== 'rgba(0, 0, 0, 0)' && bg !== 'transparent') return bg;
        cur = cur.parentElement;
      }
      return 'rgb(7, 17, 27)';
    }
    return Array.from(document.querySelectorAll('body *'))
      .filter((el) => visible(el) && (el.textContent || '').trim().length > 0)
      .map((el) => {
        const s = getComputedStyle(el);
        const r = el.getBoundingClientRect();
        return {
          selector: el.getAttribute('data-testid') || el.tagName.toLowerCase(),
          text: (el.textContent || '').trim().slice(0, 120),
          color: s.color,
          backgroundColor: bgFor(el),
          fontSize: parseFloat(s.fontSize),
          fontWeight: s.fontWeight,
          lineHeight: s.lineHeight,
          disabled: el.hasAttribute('disabled') || el.getAttribute('aria-disabled') === 'true',
          rect: { x: r.x, y: r.y, width: r.width, height: r.height }
        };
      });
  });
}
```

## 6. Typography checks beyond contrast

Contrast alone is insufficient. Gate 4 should also validate:

- line-height ratio: normal prose should be ≥1.35; dense pre blocks may use 1.5 or higher;
- font size: 12px minimum for secondary labels, 13–14px for body copy, 20px+ for panel headings;
- truncation: important statuses should not be hidden by ellipsis unless a title/tooltip exists;
- word break: long URLs and target paths need `word-break: break-all` or equivalent;
- uppercase tags: 11px uppercase badges are risky and should be contrast-checked aggressively;
- disabled controls: disabled appearance may be lower contrast, but the surrounding explanatory text must pass.

## 7. Report format

```json
{
  "state_id": "live_meta.full.safe_metadata_complete",
  "viewport": "desktop-1360x900",
  "text_contrast": [
    {"selector":"panel-label", "text":"live-metadata", "fg":"#6d8099", "bg":"#111f31", "ratio":4.11, "threshold":4.5, "pass":false}
  ],
  "typography": {
    "min_font_px": 12,
    "line_height_violations": [],
    "overflow_violations": []
  },
  "gate_4_status": "fail"
}
```

## 8. Acceptance criteria

- Every screenshot-bearing state has at least one contrast report.
- Reports include numeric ratio and threshold.
- Muted label failures are not silently waived.
- Disabled-state exemptions are explicit.
- Text overflow is tested at desktop, tablet and mobile viewports.
- The final claim never says “WCAG compliant” unless all measured text/control pairs pass for the relevant viewport and state.


## 9. Effective background challenge

Real contrast measurement is harder than pairing raw hex literals because effective background can come from ancestors. For example, a badge might have `background:#16263c` inside a panel with `background:#111f31`; the text contrast should use the badge background, not the panel background. The browser collector must walk ancestors until it finds a non-transparent background. If gradients or opacity are introduced later, the validator needs pixel sampling or conservative failure.

## 10. Token remediation proposal

The current palette can be organized into tokens:

| Token | Current | Suggested use | Audit note |
|---|---|---|---|
| `text.primary` | `#eef4ff` | headings/body | strong pass |
| `text.secondary` | `#a6b8cf` | normal secondary text | pass |
| `text.muted` | `#6d8099` | decorative or large labels only | fails normal 12px on panel bg |
| `accent.cyan` | `#50d4ff` | primary action/status | pass on dark chips |
| `accent.green` | `#7adf9b` | success/ready | pass |
| `accent.red` | `#ff7b7b` | blocked/error | pass |
| `surface.panel` | `#111f31` | panels | dark base |
| `surface.deep` | `#0b1624` | inputs/pre blocks | dark base |

A future token fix can change `text.muted` to a lighter value. Until then, U7 audit should flag every small muted label. This is not pedantry: panel labels like `trust-trace` and `capture-scope` help orient the operator and should be legible.

## 11. Text node grouping

A naive collector will double-count nested elements because parent textContent includes child text. Use one of two strategies:

- collect leaf elements that have direct text nodes; or
- collect accessible name-bearing elements by role and visible text.

For visual audit, leaf direct text is usually better because it maps to actual painted text. For accessibility audit, accessible names matter too. U7 should record both only if the report labels them clearly.

## 12. False-positive controls

Allow explicit exemptions but require reasons:

```json
{
  "selector": "button[disabled]",
  "text": "Create capture",
  "ratio": 1.58,
  "threshold": 4.5,
  "pass": false,
  "exempt": true,
  "exemption_reason": "disabled control; adjacent status text explains manual_url required"
}
```

Exemptions should be rare. A disabled action label may be lower contrast, but a blocked runtime warning cannot be exempt just because it is secondary.

## 13. Test fixtures for validator

Create tiny tests independent of the H5 app:

```python
def test_primary_text_passes_panel_bg():
    assert passes_text_contrast('#eef4ff', '#111f31', 14)['pass']

def test_muted_label_fails_panel_bg():
    result = passes_text_contrast('#6d8099', '#111f31', 12)
    assert result['ratio'] == 4.11
    assert not result['pass']

def test_large_text_threshold():
    assert passes_text_contrast('#6d8099', '#111f31', 24)['threshold'] == 3.0
```

These tests protect the math and make the muted-label issue explicit.

## 14. Cross-state report aggregation

After per-state reports, aggregate by token and component:

```text
contrast_failures_by_token:
  text.muted: 41
contrast_failures_by_component:
  LiveMetadataPanel: 6
  CaptureScopePanel: 8
  TrustTraceGraph: 8
```

This lets the project fix a token once instead of patching every component. If most failures are the same muted label, the right fix is palette/token adjustment, not per-component exception churn.

## 15. Accessibility beyond contrast

U7’s a11y validator starts with contrast because the prompt names it explicitly, but a complete future pass should include:

- keyboard focus order for UrlBar and buttons;
- role=alert for error banners;
- aria-labels for icon-only controls if any appear;
- reduced-motion respect for loading animations;
- no color-only communication for allowed/blocked/candidate statuses;
- visible focus indicator contrast;
- headings in logical order within state browser and component frames.

These checks can be added later with axe-core or custom Playwright assertions. They still do not replace the 5-Gate human visual review.

## 16. Pass/fail wording

Reports should say `measured_pass` or `measured_fail`, never `WCAG compliant` unless the full state, all viewports and all relevant success criteria are measured. For this package, the honest wording is: “contrast validation method specified; sample TSX literal ratios computed; live rendered state measurement pending.”


## 17. Per-panel a11y priorities

| Panel | Priority check |
|---|---|
| URL Bar | input placeholder/readiness text/button disabled contrast; role=alert error |
| Live Metadata | 12px labels and fixture badge contrast |
| Capture Scope | status badges must include text, not color alone |
| Trust Trace | node states and graph labels must remain readable |
| Topic Card Preview | dense metrics and counter-note contrast |
| Topic Card Vault | pre block readability and target path wrapping |
| Four Panel Shell | heading hierarchy and preview error visibility |
| Main Navigation | active item, focus state and unknown-route error |

This lets audit triage focus on the most likely failures first.

## 18. Remediation example for muted label

If `#6d8099` fails on `#111f31`, test candidate replacements with the same function. For example, a lighter muted token can be selected only after computing ratio. Do not choose by eye alone. The fix should be centralized:

```css
:root {
  --sf-text-muted: #7f95b0; /* example only; verify ratio before adoption */
}
```

Then replace raw literals gradually under a dedicated frontend/style dispatch. U7 spec does not authorize that mutation.

## 19. Why rendered measurement must follow literal measurement

Literal measurement catches obvious token risks before rendering. Rendered measurement catches actual inheritance, opacity, disabled state and responsive layout. Both are needed. For example, `#50d4ff` might pass on a chip but fail if placed on a light background later. The validator should therefore store `source=literal_scan` or `source=rendered_computed_style` for every ratio.

## 20. Minimum proof before claiming pass

A state can claim Gate 4 pass only if:

- every meaningful text element has computed ratio meeting threshold or explicit exemption;
- every important non-text indicator has visible text or non-color cue;
- no important text is clipped at the tested viewport;
- line-height and font-size are within thresholds;
- the report is attached to the state audit row.

Anything less is “method ready” or “partial measurement”, not pass.


## 21. Integration with 5-Gate report

Gate 4 output should be embedded inside the 5-Gate report, but also exportable alone. The standalone export helps a developer fix tokens without reading hierarchy/weight commentary. The embedded report helps a reviewer see why a state cannot yet be human-passed.

```json
{
  "gate_4_typography": {
    "status": "fail",
    "failure_count": 3,
    "worst_ratio": 4.11,
    "violations_ref": "contrast/url_bar.error.desktop.json"
  }
}
```

## 22. Contrast and state semantics

Some text is more semantically important than other text. The validator should add severity:

- `critical`: blocked/runtime/write-disabled/manual_url_only text;
- `high`: panel title, status badge, primary action;
- `medium`: descriptive body copy;
- `low`: decorative labels.

A low-severity failure can still block if it is meaningful text, but severity helps triage. Critical boundary copy must never be waived.
