# ScoutFlow H5 Design Tokens Extraction

> Status: research-only / not-authority / not-runtime-approval
> Task: `T-P1A-068`
> Source prototype: `~/workspace/scoutflow-prototypes/h5-capture-station/`
> Source files:
> - `design-tokens.json`
> - `capture-station-v0.html`

## 1. Scope

This note extracts the reusable UI token layer from the repo-external H5 prototype and keeps it in research form.
It does not create `apps/`, does not approve frontend implementation, and does not change PRD/SRD authority.

## 2. Source Summary

The prototype metadata in `design-tokens.json` declares:

- name: `ScoutFlow Capture Station v0`
- source: `dispatch PR61 / T-P1A-036`
- status: `repo_external_prototype`
- upstream reference: `nexu-io/open-design (Apache-2.0, local-only read reference)`

The HTML prototype confirms the same token family through `:root` CSS variables and the shell layout used by the 4-panel mock.

## 3. Color Tokens

| Token | Value | Intended use |
|---|---|---|
| `bg_canvas` | `#07111b` | page canvas / deep background |
| `bg_shell` | `#0d1826` | shell backdrop |
| `surface_base` | `#111f31` | default panel surface |
| `surface_elevated` | `#16263c` | lifted cards / inner blocks |
| `surface_muted` | `#0b1624` | muted surfaces / inputs |
| `border_strong` | `#27415d` | emphasized borders |
| `border_soft` | `#1d3148` | default borders |
| `text_primary` | `#eef4ff` | primary text |
| `text_secondary` | `#a6b8cf` | supporting text |
| `text_muted` | `#6d8099` | metadata / labels |
| `accent_live` | `#50d4ff` | live state / primary highlight |
| `accent_success` | `#53d690` | success / ready |
| `accent_warn` | `#ffbe55` | warning |
| `accent_blocked` | `#ff7b7b` | blocked / danger |
| `accent_focus` | `#9a8cff` | focus / secondary glow |

## 4. Typography Tokens

| Token | Value |
|---|---|
| `font_display` | `"Inter", "SF Pro Display", "Helvetica Neue", sans-serif` |
| `font_body` | `"Inter", "PingFang SC", "Noto Sans SC", sans-serif` |
| `font_mono` | `"JetBrains Mono", "SFMono-Regular", monospace` |
| `size_hero` | `28` |
| `size_title` | `20` |
| `size_body` | `14` |
| `size_caption` | `12` |
| `line_height_body` | `1.45` |

## 5. Spacing / Radius / Shadow

### Spacing

| Token | Value |
|---|---|
| `unit` | `8` |
| `xs` | `8` |
| `sm` | `12` |
| `md` | `16` |
| `lg` | `24` |
| `xl` | `32` |

### Radius

| Token | Value |
|---|---|
| `panel` | `8` |
| `chip` | `999` |
| `button` | `10` |

### Shadow

| Token | Value |
|---|---|
| `panel` | `0 24px 48px rgba(0, 0, 0, 0.32)` |
| `focus` | `0 0 0 1px rgba(80, 212, 255, 0.38), 0 0 0 4px rgba(80, 212, 255, 0.08)` |

## 6. Layout Tokens

| Token | Value |
|---|---|
| `canvas_width` | `1440` |
| `canvas_height` | `900` |
| `max_width` | `1360` |
| `header_height` | `72` |
| `top_panel_height` | `112` |
| `content_gap` | `24` |
| `grid_columns` | `12` |

## 7. HTML Cross-check

The prototype HTML mirrors the token JSON in a directly consumable form:

- `:root` contains the same color variables as CSS custom properties
- `.shell` uses `width: 1360px`, `margin: 24px auto`, `padding: 24px`, and a large panel shadow
- `.header` / `.brand h1` / `.brand p` align with the `28 / 14` type scale
- `.url-panel` uses a 4-column grid and `margin-bottom: 24px`
- `.panel` surfaces and button states match the extracted `surface_*`, `border_*`, and `accent_*` tokens

## 8. Reusable Design Conclusions

- The dominant visual pattern is a dark operator console with cyan as the live/action accent and green as the success accent.
- Border density and contrast are restrained; emphasis is created by glow, gradients, and elevated surfaces instead of heavy dividers.
- The spacing system is cleanly 8-based and is already stable enough to seed future frontend implementation.
- The token set is presentation-oriented, not business-domain authoritative. It can guide later `apps/capture-station` work, but does not itself unlock `apps/`.

## 9. Carry-forward

- This extraction is suitable as an input to the later H5 mock and app scaffold slots.
- The repo-external source of truth remains `~/workspace/scoutflow-prototypes/h5-capture-station/design-tokens.json`.
- Any later implementation should preserve the token names where practical, instead of inventing a second token vocabulary without reason.
