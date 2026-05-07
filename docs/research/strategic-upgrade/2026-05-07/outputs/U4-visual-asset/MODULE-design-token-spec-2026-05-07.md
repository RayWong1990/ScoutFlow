---
status: candidate / not-authority / not-runtime-approval
created_for: Cloud Prompt U4 Visual Asset Spine
requested_date: 2026-05-07
generated_in_session_date: 2026-05-06
write_enabled: false
claim_scope: spec-only; no production code modification; no dispatch authorization
---

# MODULE — design_token spec

> claim label: ≥95% for candidate token shape; no claim that this is an approved package, CSS contract, or production replacement.

## 1. Module mission

`design_token` gives the visual system a single candidate source for color, spacing, radius, typography, shadow, motion, graph, and status semantics. It is explicitly **not** a Tailwind config, not a Panda token package, not a Style Dictionary build approval, and not a CSS replacement for current Capture Station code. The module should preserve the deep-sea blue operator-workstation palette already visible in Capture Station while making token usage reusable for PF-V H5 mockups, future PPT/poster assets, image prompts, and code translation prompts.

The design-token module differs from `visual_asset`: it stores abstract values and cascade rules, not rendered images. It differs from `pattern_library`: it stores stable primitives, not reusable workflows. It differs from `prompt_template`: it can be referenced by prompts but does not contain prompt text.


## Source Register / 证据边界

- PRD-v2/SRD-v2 的稳定事实：ScoutFlow 是 single-user、local-first、SQLite + FS + state words 的 authority-first 工作台；当前不得自动批准 SaaS、多用户、runtime 扩张、media/ASR、browser automation、vault true write 或 migration。
- Capture Station 的已读事实：`apps/capture-station/package.json` 是 React 18 + Vite 5，未把 Tailwind/shadcn/Panda/Radix/React Flow/TanStack/Lucide 写成已批准依赖；现有 H5 代码使用深海蓝 palette、inline style、URL Bar + Vault Preview/Dry Run + Live Metadata + Capture Scope + Trust Trace 的工作台结构。
- Visual docs 的已读事实：`design-brief.md` 固定 4 面板扫描顺序；`five-gate-checklist.md` 要求 5 gate 全过才可称 visual pass；`trust-trace-graph-spec.md` 固定 `capture -> capture_state -> metadata_job -> probe_evidence -> receipt_ledger -> media_audio -> audit` 节点链。
- 本地缺口：容器内没有 `~/workspace/ScoutFlow`、没有 `~/.claude/rules/aesthetic-first-principles.md`、没有 PF-V 实际 `INDEX.csv`，因此相关内容均标为 `needs_local_refresh`。
- Live web 缺口：本运行环境禁用实时网页浏览；任何 vendor / 2026 工具状态只能列为待验证 URL 种子，不得写成已访问事实。

## 2. Candidate cascade rule

```text
design-tokens.json
  -> generated CSS variables candidate
     -> capture-station React seam (future only)
     -> PF-V H5 prompt variables
     -> future PPT/poster/export specs
```

Cascade discipline:

1. `design-tokens.json` is the only source that may introduce or rename semantic token names.
2. Generated CSS variables may flatten names, but cannot change values or semantics.
3. Consumers may override density variables such as panel padding, but not status colors for `blocked`, `candidate`, or `allowed` without recording a token decision.
4. Tokens are semantic: `state.danger` means blocked/failure, not “pretty red.”
5. If current Capture Station keeps inline styles, the token spec can audit drift, not force replacement.

## 3. Complete candidate `design-tokens.json`

```json
{
  "$schema": "https://design-tokens.github.io/community-group/format/",
  "meta": {
    "status": "candidate/not-authority",
    "source": "ScoutFlow U4",
    "generator": "manual candidate spec"
  },
  "color": {
    "canvas": {
      "0": {
        "$type": "color",
        "$value": "#07111B"
      },
      "1": {
        "$type": "color",
        "$value": "#0D1826"
      },
      "2": {
        "$type": "color",
        "$value": "#101A27"
      }
    },
    "panel": {
      "bg": {
        "$type": "color",
        "$value": "#111F31"
      },
      "low": {
        "$type": "color",
        "$value": "#0B1624"
      },
      "raised": {
        "$type": "color",
        "$value": "#16263C"
      },
      "hover": {
        "$type": "color",
        "$value": "#172A42"
      }
    },
    "border": {
      "subtle": {
        "$type": "color",
        "$value": "#1D3148"
      },
      "panel": {
        "$type": "color",
        "$value": "#27415D"
      },
      "strong": {
        "$type": "color",
        "$value": "#3A5879"
      }
    },
    "text": {
      "primary": {
        "$type": "color",
        "$value": "#EEF4FF"
      },
      "secondary": {
        "$type": "color",
        "$value": "#A6B8CF"
      },
      "muted": {
        "$type": "color",
        "$value": "#6D8099"
      },
      "disabled": {
        "$type": "color",
        "$value": "#50647D"
      }
    },
    "accent": {
      "cyan": {
        "$type": "color",
        "$value": "#50D4FF"
      },
      "cyanBg": {
        "$type": "color",
        "$value": "#0D3344"
      },
      "violet": {
        "$type": "color",
        "$value": "#9A7CFF"
      }
    },
    "state": {
      "success": {
        "$type": "color",
        "$value": "#7ADF9B"
      },
      "successBg": {
        "$type": "color",
        "$value": "#10291F"
      },
      "warning": {
        "$type": "color",
        "$value": "#FFBE55"
      },
      "warningBg": {
        "$type": "color",
        "$value": "#332512"
      },
      "danger": {
        "$type": "color",
        "$value": "#FF7B7B"
      },
      "dangerBg": {
        "$type": "color",
        "$value": "#33191E"
      },
      "info": {
        "$type": "color",
        "$value": "#7DB7FF"
      },
      "infoBg": {
        "$type": "color",
        "$value": "#10233D"
      }
    },
    "graph": {
      "edge": {
        "$type": "color",
        "$value": "#27415D"
      },
      "edgeActive": {
        "$type": "color",
        "$value": "#50D4FF"
      },
      "edgeSuccess": {
        "$type": "color",
        "$value": "#7ADF9B"
      },
      "edgeBlocked": {
        "$type": "color",
        "$value": "#8F5C5C"
      },
      "nodeFill": {
        "$type": "color",
        "$value": "#0B1624"
      },
      "nodeActive": {
        "$type": "color",
        "$value": "#113448"
      }
    },
    "overlay": {
      "bg": {
        "$type": "color",
        "$value": "rgba(7,17,27,.88)"
      }
    }
  },
  "space": {
    "1": {
      "$type": "dimension",
      "$value": "4px"
    },
    "2": {
      "$type": "dimension",
      "$value": "8px"
    },
    "3": {
      "$type": "dimension",
      "$value": "12px"
    },
    "4": {
      "$type": "dimension",
      "$value": "16px"
    },
    "5": {
      "$type": "dimension",
      "$value": "24px"
    }
  },
  "radius": {
    "panel": {
      "$type": "dimension",
      "$value": "8px"
    },
    "control": {
      "$type": "dimension",
      "$value": "10px"
    },
    "pill": {
      "$type": "dimension",
      "$value": "999px"
    }
  },
  "shadow": {
    "workstation": {
      "$type": "shadow",
      "$value": "0 24px 48px rgba(0,0,0,.32)"
    },
    "focus": {
      "$type": "shadow",
      "$value": "0 0 0 2px rgba(80,212,255,.32)"
    }
  },
  "font": {
    "family": {
      "sans": {
        "$type": "fontFamily",
        "$value": "Inter, PingFang SC, Helvetica Neue, sans-serif"
      }
    },
    "size": {
      "stationTitle": {
        "$type": "dimension",
        "$value": "28px"
      },
      "panelTitle": {
        "$type": "dimension",
        "$value": "20px"
      },
      "body": {
        "$type": "dimension",
        "$value": "14px"
      },
      "caption": {
        "$type": "dimension",
        "$value": "12px"
      },
      "badge": {
        "$type": "dimension",
        "$value": "11px"
      }
    },
    "lineHeight": {
      "tight": {
        "$type": "number",
        "$value": 1.15
      },
      "body": {
        "$type": "number",
        "$value": 1.45
      }
    }
  },
  "motion": {
    "durationFast": {
      "$type": "duration",
      "$value": "120ms"
    },
    "durationNormal": {
      "$type": "duration",
      "$value": "180ms"
    },
    "easingState": {
      "$type": "cubicBezier",
      "$value": [
        0.2,
        0,
        0,
        1
      ]
    }
  },
  "z": {
    "tooltip": {
      "$type": "number",
      "$value": 30
    },
    "toast": {
      "$type": "number",
      "$value": 40
    }
  }
}
```

## 4. Consumer map

| Consumer | How it references tokens | Current permission | Risk guard |
|---|---|---|---|
| `apps/capture-station` React | future CSS variables / CSS Modules seam | candidate only | no package install, no production CSS replacement |
| PF-V H5 prompt system | inject token names + values into image/code prompts | allowed as prompt reference | prompt must state candidate token source |
| visual_asset token_visual | generate swatches / graph examples from tokens | allowed in sidecar | stored as `kind=token_visual` |
| pattern_library | patterns reference token family names | allowed | pattern cannot redefine token values |
| future PPT/poster | export token JSON or CSS var list | candidate | not a brand system authority |

## 5. Watch-and-rebuild script (candidate ≤300 LOC)

```python
#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, time
from pathlib import Path

SRC = Path('visual-assets/design-tokens.json')
OUT = Path('visual-assets/generated/design-tokens.css')

def flatten(prefix, obj, out):
    if isinstance(obj, dict) and '$value' in obj:
        out[prefix] = obj['$value']
    elif isinstance(obj, dict):
        for k, v in obj.items():
            if k.startswith('$'): continue
            flatten(f'{prefix}-{k}' if prefix else k, v, out)

def build_css():
    data = json.loads(SRC.read_text())
    flat = {}
    flatten('sf', data, flat)
    lines = [':root {']
    for name, value in sorted(flat.items()):
        css_name = '--' + name.replace('_','-').replace('.', '-')
        if isinstance(value, list):
            value = ', '.join(map(str, value))
        lines.append(f'  {css_name}: {value};')
    lines.append('}')
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text('\n'.join(lines) + '\n')


def watch(interval=1.0):
    last = None
    while True:
        mtime = SRC.stat().st_mtime if SRC.exists() else None
        if mtime != last:
            build_css(); last = mtime
            print(f'rebuilt {OUT}')
        time.sleep(interval)
```

This script is a candidate seam. It does not edit `apps/capture-station`; it writes under `visual-assets/generated/` only.

## 6. Token review rules

### Color

- Canvas and panel colors should preserve deep-sea contrast.
- Cyan is active proof/action; green is ready/allowed; amber is candidate/gated; red is blocked/failure.
- Status colors must always pair with text labels; color-only state is invalid.

### Typography

- Station title can be 24-28px. Panel title should be 16-20px. Machine values should not fall below 12px/18px.
- Chinese text should not be forced into uppercase tracking. English state tokens can use compact labels only if readable.
- Monospace is reserved for URL, ID, timestamp, route, hash, prompt_id, asset_id.

### Spacing / radius

- 8dp rhythm is represented by `space.2=8px`, `space.4=16px`, `space.5=24px`.
- Panel radius is 8px for stable workstation panels. Control radius is 10px for input/button affordance.
- Do not create card-inside-card noise: row shelf can use `panel.low`, but nested surface count should stay low.

### Motion

- Motion expresses state change, not delight. Metadata rows may fade/slide 120-180ms; Trust Trace path may transition stroke opacity; no looping neon pulse.
- Reduced motion must preserve semantic state through text/badge/border/position.

## 7. Drift audit query / report shape

A future audit can compare inline hex values in `apps/capture-station` with token values and produce a report, but it must not auto-edit production files.

```text
TOKEN_DRIFT_REPORT
  scanned_paths: apps/capture-station/src/**/*.tsx
  known_token_values: 44+
  unknown_hex_values: [...]
  inline_values_matching_tokens: [...]
  recommended_action: candidate_patch_only
```

## 8. Acceptance checklist

- `design-tokens.json` is valid JSON and Style Dictionary compatible enough for future transform.
- Generated CSS writes outside production app.
- Existing inline styles can be audited without being replaced.
- Token semantics preserve H5 4-panel and 5-Gate requirements.
- Status colors never become decorative palette slots.
- No package install or build pipeline change is implied.


## 9. Generated CSS variable naming

A future generator should flatten the JSON into names that are readable to both designers and engineers:

```css
:root {
  --sf-color-canvas-0: #07111B;
  --sf-color-panel-bg: #111F31;
  --sf-color-border-panel: #27415D;
  --sf-color-text-primary: #EEF4FF;
  --sf-color-accent-cyan: #50D4FF;
  --sf-color-state-success: #7ADF9B;
  --sf-space-4: 16px;
  --sf-radius-panel: 8px;
  --sf-shadow-workstation: 0 24px 48px rgba(0,0,0,.32);
}
```

The flattening prefix should include category names (`color`, `space`, `radius`) to avoid collisions. `state.warning` should become `--sf-color-state-warning`, not a free-floating `--sf-warning`, unless backward compatibility with existing inline conventions is explicitly chosen.

## 10. Prompt injection block for PF-V

The token module should export a compact text block that can be copied into image-generation or audit prompts:

```text
Candidate ScoutFlow H5 token spine:
canvas=#07111B/#0D1826, panel=#111F31, row=#0B1624,
border=#27415D, text=#EEF4FF/#A6B8CF/#6D8099,
action cyan=#50D4FF, success=#7ADF9B, warning=#FFBE55, danger=#FF7B7B,
radius panel=8px, control=10px, grid gaps=16/24px,
motion 120-180ms, no decorative neon pulse, no generic SaaS dashboard palette.
```

This block is intentionally smaller than the full JSON. Prompt use should be concise so token context does not crowd out panel semantics and boundaries.

## 11. Accessibility preflight

Before any token set is promoted, run a contrast preflight. The first v0 can calculate WCAG contrast ratios for common pairs:

| foreground | background | expectation |
|---|---|---|
| `text.primary` | `panel.bg` | strong body/title readability |
| `text.secondary` | `panel.bg` | readable long metadata |
| `text.muted` | `panel.bg` | label only, not critical state |
| `accent.cyan` | `canvas.0` | action/focus visible |
| `state.danger` | `dangerBg` | blocked badge readable |
| `state.warning` | `warningBg` | candidate/gated badge readable |

If a pair fails, do not silently tweak only CSS output. Update `design-tokens.json`, record a token decision note, and regenerate consumers.

## 12. Token decision log shape

```yaml
decision_id: tok_20260507_001
token: color.state.warning
old_value: "#FFBE55"
new_value: "#F6C15C"
reason: "improve contrast on warningBg while preserving gated semantics"
affected_consumers:
  - PF-V prompt block
  - token_visual swatch
  - generated CSS candidate
approved_for_production: false
```

The log can be a markdown file or a SQLite event table later. For v0, a markdown log is enough because single-user token churn is low.

## 13. What not to tokenize yet

Do not tokenize every possible component dimension. The current target is a spine, not a full UI library. Avoid tokens for arbitrary card variants, marketing gradients, chart palettes, sidebar sizes, enterprise tables, theme modes, or animation choreography. Add tokens only when two or more consumers need the same semantic value or when a gate requires a stable rule.

## 14. Token visual assets

The token module can generate `kind=token_visual` assets: swatch sheets, status badge examples, Trust Trace node color examples, and typography ramps. These images should be registered in `visual_asset` with `prompt_id` pointing to the token extraction/audit prompt and `pattern_tag=F` if Pattern F is kept as token extraction. This closes the loop between abstract JSON and visible design review.


## 15. Density modes

The first token JSON should not create full themes, but it may allow density aliases:

| density | intended use | values |
|---|---|---|
| compact | high-density operator review | panel padding 12-14px, row gap 8-10px |
| default | Capture Station baseline | panel padding 16px, grid gap 24px |
| presentation | PPT/poster/export | larger type, more breathing room |

Density changes are layout rhythm changes, not color theme changes. A compact mode cannot make blocked lanes less visible, and a presentation mode cannot promote future lanes as active.

## 16. Token-to-component mapping

| H5 surface | token families |
|---|---|
| Station shell | canvas, border.subtle, shadow.workstation, space.5 |
| URL Bar | panel.bg, accent.cyan, radius.control, text.primary |
| Live Metadata | panel.bg, panel.low, text.secondary, space.3 |
| Capture Scope | state.success/warning/danger, radius.pill, text.primary |
| Trust Trace | graph.edge, graph.edgeActive, graph.nodeFill, graph.nodeActive |
| Toast/tooltip | overlay.bg, z.toast, z.tooltip, shadow.focus |

This mapping is useful for future drift reports. If a component uses a value that does not belong to its surface, the report can say “ScopePanel uses graph token” instead of only “unknown hex.”

## 17. Candidate build outputs

Possible outputs from the same JSON:

```text
design-tokens.css        CSS variables for future app seam
design-tokens.prompt.txt compact prompt block for PF-V
design-tokens.swatch.png token_visual asset for review
design-tokens.report.md  drift and contrast report
```

Only the JSON is canonical inside the sidecar. Generated files can be deleted and rebuilt. This prevents drift between token text and visible swatches.


## 18. Token naming stability

Renaming tokens is more expensive than changing values because prompts, assets, drift reports, and future CSS can all reference names. The token module should therefore treat names as stable once they are used by a locked asset. If a name is wrong, add an alias or deprecate it with a note rather than silently changing it. Example: if `accent.cyan` later becomes `action.primary`, keep a compatibility alias until all prompts and token visuals are migrated.

## 19. Visual token acceptance

A token visual is useful only if it shows semantics, not just swatches. A good token visual includes a URL action, allowed badge, candidate badge, blocked badge, Trust Trace active edge, and muted edge. A bad token visual is a grid of colors without usage labels. The registry should treat unlabeled swatches as candidate only because they do not help 5-Gate review.


## Appendix B — token governance without enterprise overhead

本模块不引入 design system committee。单人治理只需要三个动作：新增 token、替换 token、废弃 token。新增 token 必须写 `source` 和 `reason`；替换 token 必须保留旧名到新名的 alias 至少一个版本；废弃 token 不立即删除，而是在 `deprecated` 分组里保留注释，避免 H5、PPT、poster、PF-V mockup 同步期间出现静默断链。

推荐把 `design-tokens.json` 拆分视为 future，不在 U4 直接做。当前单文件更利于审计：capture-station React、PF-V H5、PPT/poster prompt 都读取同一个文件或同一个导出的 CSS variables。若未来文件超过 400 行，再拆为 `color.json`、`type.json`、`motion.json`，但生成产物仍保持一个 `dist/design-tokens.css`。

### Visual prompt token injection

PF-V 图像生成 prompt 可以引用 token 名，而不是把颜色散写在 prompt 里。例如：`use color.background.canvas=#07111b, color.accent.cyan=#50d4ff, grid.8dp`. 这样视觉反推 H5 时，图像资产、React 实现、spec 文档不会分叉成三套蓝色。
