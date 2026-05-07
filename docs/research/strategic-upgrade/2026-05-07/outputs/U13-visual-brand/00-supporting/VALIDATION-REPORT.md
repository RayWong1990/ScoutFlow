---
title: VALIDATION-REPORT
status: candidate / not-authority
authority: not-authority
created_at: 2026-05-07
atlas_id: U13-visual-style-brand-atlas-v0
file_kind: supporting
claim_labels:
  - canonical fact from generated artifact metrics
  - tentative candidate
boundary: docs-only; no runtime/package/frontend/browser/vault/migration approval
---

# VALIDATION-REPORT


## Generated artifact metrics

| Metric | Value |
|---|---:|
| Markdown files | 108 |
| Approx CJK+Latin units | 199750 |
| Token files | 5 |
| Icon entries | 60 |
| SVG icon 24x24 viewBox snippets | 60 |
| Illustration entries | 30 |
| Pattern entries | 20 |
| Panel specs | 8 |
| Templates | 10 |
| 5-Gate case markers | 30 |
| Mermaid diagrams | 37 |
| Claim-label coverage | 100.0% |
| WCAG contrast pairs calculated | 37 |

## Files by top-level folder

| Folder | Files |
|---|---:|
| `00-supporting` | 9 |
| `01-token-system` | 5 |
| `02-icon-library` | 30 |
| `03-illustration-library` | 15 |
| `04-pattern-library` | 10 |
| `05-panel-design-spec` | 8 |
| `06-multi-medium-template` | 10 |
| `07-5-gate-audit-tests` | 5 |
| `08-cross-phase-evolution` | 5 |
| `09-cluster-index` | 10 |
| `README.md` | 1 |

## WCAG sample pairs

| Pair | Ratio | Verdict |
|---|---:|---|
| `sf.text.primary` on `sf.canvas.0` | 17.21:1 | pass for normal text |
| `sf.text.primary` on `sf.canvas.1` | 16.18:1 | pass for normal text |
| `sf.text.primary` on `sf.panel.bg` | 15.05:1 | pass for normal text |
| `sf.text.primary` on `sf.panel.bg.low` | 16.47:1 | pass for normal text |
| `sf.text.primary` on `sf.panel.bg.raised` | 13.82:1 | pass for normal text |
| `sf.text.secondary` on `sf.canvas.0` | 9.39:1 | pass for normal text |
| `sf.text.secondary` on `sf.canvas.1` | 8.83:1 | pass for normal text |
| `sf.text.secondary` on `sf.panel.bg` | 8.21:1 | pass for normal text |
| `sf.text.secondary` on `sf.panel.bg.low` | 8.99:1 | pass for normal text |
| `sf.text.secondary` on `sf.panel.bg.raised` | 7.54:1 | pass for normal text |
| `sf.text.muted` on `sf.canvas.0` | 4.70:1 | pass for normal text |
| `sf.text.muted` on `sf.canvas.1` | 4.42:1 | non-critical only |
| `sf.text.muted` on `sf.panel.bg` | 4.11:1 | non-critical only |
| `sf.text.muted` on `sf.panel.bg.low` | 4.50:1 | pass for normal text |
| `sf.text.muted` on `sf.panel.bg.raised` | 3.78:1 | non-critical only |
| `sf.accent.cyan` on `sf.canvas.0` | 11.04:1 | pass for normal text |
| `sf.accent.cyan` on `sf.canvas.1` | 10.38:1 | pass for normal text |
| `sf.accent.cyan` on `sf.panel.bg` | 9.65:1 | pass for normal text |
| `sf.accent.cyan` on `sf.panel.bg.low` | 10.57:1 | pass for normal text |
| `sf.accent.cyan` on `sf.panel.bg.raised` | 8.86:1 | pass for normal text |

## Validator conclusions

- File count exceeds the ≥85 hard boundary and the table's ≥103 expectation.
- Content unit count exceeds the requested ≥120000/≥130000 approximate mixed CJK+Latin target.
- Inline icon snippets include 24×24 viewBox and path-only vector geometry.
- All files preserve candidate/not-authority frontmatter and boundary copy.
- Live web and external repo gaps are documented as limitations rather than silently passed.



## Boundary / 边界声明

- `status`: candidate；`authority`: not-authority；本文件不是 CSS token 合并、frontend implementation、package install、browser automation、runtime、vault true write、migration 或 authority writeback 批准。
- 可被 PF-V / GPT-Image-2 / future dispatch 作为视觉 atlas 输入；不可把本文内任何 token、SVG、layout 或 template 直接解释成 production contract。
- 所有主观 5-Gate 判断保持 human-in-loop；自动化只能提供截图、contrast、DOM 或 manifest evidence，不能替代最终视觉判断。
- 第三方库仅作为参考类别；本 atlas 内联 SVG 均按 ScoutFlow-original candidate 处理，未复制第三方 path。若未来改用第三方 icon/illustration，必须重新验证 license。
