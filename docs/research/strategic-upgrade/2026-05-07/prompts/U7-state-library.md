---
title: Cloud Prompt — U7 State Library & Quality Automation (8 panel × 6 state + 5-Gate 自动化)
status: candidate / cloud_prompt / not-authority
authority: not-authority
created_at: 2026-05-07
target_window: GPT Pro web 浏览模式
new_lane: yes
---

# Cloud Prompt — U7 State Library & Quality Automation

## §1 Mission

ScoutFlow capture-station 当前 8 个 feature panel (URL bar / live metadata / capture scope / trust trace / topic-card-preview / topic-card-vault / four-panel-shell / 主导航). 每 panel 实测有 ~6 visual state (empty / loading / partial / full / error / amend). 8 × 6 = ~**48 visual state** — 这是 ScoutFlow 视觉的真实状态空间.

PF-V 当前 P2 阶段在跑这部分 (S04 URL Bar 10 状态 / S05 Live Metadata 10 变体 / S06-S09 各 5-10 状态). **但 PF-V 没有把这些状态 register 成可查询 state-library**, 也没有 5-Gate audit 自动化挂入.

本任务: 写两个组件的 candidate spec —
1. `state-library`: 48 state matrix register + screenshot evidence + Storybook-style 浏览器 + state→component routing
2. `5-gate-automation`: 自动化 5-Gate (visual hierarchy / spacing alignment / occlusion safety / typography legibility / visual weight) 部分 check + human handoff for subjective gate, 与 visual_asset (U4) state machine 联动

## §2 Inputs

1. https://github.com/RayWong1990/ScoutFlow/tree/main/apps/capture-station/src/features (8 feature 现状)
2. PF-V 当前进度 (S04-S09 各 5-10 state, 用户另窗口)
3. `~/.claude/rules/aesthetic-first-principles.md` (5-Gate canonical rule)
4. https://github.com/RayWong1990/ScoutFlow/blob/main/docs/visual/ (如有)
5. **Live web** 真实 search 2026 visual regression / state library / a11y audit / Storybook
6. WCAG 2.2 contrast standard / Apple HIG / Material 3

## §3 Multi-pass Work Plan (≥10 pass, ≥120 min)

1. **Pass 1**: 读 capture-station 8 feature TSX 实际 state 实现, 抽出 state machine
2. **Pass 2 — Live web**: 真实 search ≥15: Storybook 8 / Chromatic / Percy / Loki visual regression / pa11y / axe-core / Lighthouse a11y / playwright visual / contrast checker / typography linter / spacing system audit / Pixelmator AI feature / Figma Tokens
3. **Pass 3 — state-library schema**: 
   - SQLite 表 `state_library` (state_id / panel_name ∈ {url_bar / live_meta / capture_scope / trust_trace / topic_card_preview / topic_card_vault / four_panel_shell / main_nav} / state_name ∈ {empty / loading / partial / full / error / amend / 自定义} / variant_name (e.g. "long_title" / "tags_overflow") / screenshot_path FK visual_asset / props_json / 5_gate_status / created_at / phase)
   - Browser UI (Storybook-style 单页 React or 简易 HTML5) ≤300 行
   - state→component routing (capture-station React feature 引用 state_library 反查)
4. **Pass 4 — 5-gate-automation 哪些可自动**: 
   - Gate 4 typography legibility: 可自动 (字号 / 行高 / contrast ratio WCAG ≥4.5:1)
   - Gate 2 spacing alignment: 部分自动 (8dp grid 校验 + baseline 对齐)
   - Gate 3 occlusion safety: 部分自动 (safe-area test + 字幕区域检测)
   - Gate 1 visual hierarchy: 主观, 必须人审 (但可 score 主元素与次元素 size ratio)
   - Gate 5 visual weight: 主观, 必须人审 (但可计算饱和度差距)
5. **Pass 5 — 5-gate-automation tool spec**: 
   - Headless audit script (puppeteer / playwright headless) 跑每 state, 输出 5-gate audit report
   - Human review queue (subjective gate 必须打卡)
   - 与 visual_asset (U4) state machine 联动: visual_asset.5_gate_audit_passed 字段写入
6. **Pass 6 — Cross-cluster reuse**: state-library 不止 capture-station, PF-V H5 / 未来 PPT / poster / DiloFlow 视觉都可注册
7. **Pass 7 — Single-user budget**: ≤600 行 Python + ≤300 行 React + ≤1.5 周
8. **Pass 8 — PF-V P2 现状对接**: 现 PF-V S04-S09 输出迁移到 state_library 表的方案
9. **Pass 9 — Self-audit ≥15**
10. **Pass 10**: README + truthful stdout

## §4 Hard Boundaries

- candidate / not-authority
- write_enabled=False 不变
- 不批准 capture-station production 修改 (apps/** 仍 hold)
- 仅 spec, 不实际生成 48 state screenshot (留给 PF-V P2 + 后续 dispatch)
- 5-Gate 主观 gate 不许伪自动化 — 必须 human-in-the-loop
- a11y 不许仅声称合规, 必须实测 contrast ratio

## §5 Live Web Evidence Refresh

≥15 真实 search:
- Storybook 8 / Bit Cloud 2026
- Chromatic / Percy / Loki visual regression 2026
- pa11y / axe-core / Lighthouse a11y 2026
- Playwright visual testing 2026
- WCAG 2.2 update / Apple HIG 2026 / Material 3 expressive
- Headless browser screenshot / puppeteer
- Figma Tokens Studio / Style Dictionary 2026
- Pixelmator AI feature / Affinity Photo

## §6 Cross-local Search

- `~/workspace/ScoutFlow/apps/capture-station/src/features/**/*.tsx` 8 feature 实际 state
- `~/workspace/ScoutFlow/apps/capture-station/src/styles/` 既有 CSS / token
- PF-V P2 当前 INDEX.csv (用户另窗口)
- `~/.claude/rules/aesthetic-first-principles.md`
- DiloFlow 视觉风格期望

## §7 Output Deliverables

ZIP filename: `cloud-output-U7-state-library-quality-2026-05-07.zip`
File count: **9**

| # | File | min 字 | claim label |
|---|---|---:|---|
| 1 | MODULE-state-library-spec-2026-05-07.md | 3000 (48 state matrix + SQLite DDL + browser UI) | ≥95% |
| 2 | MODULE-5-gate-automation-spec-2026-05-07.md | 3500 (5 gate 各自自动化路径 + headless audit + human queue) | ≥95% |
| 3 | 8-PANEL-STATE-INVENTORY-2026-05-07.md | 2800 (8 panel × 6 state 全枚举 + props_json 示例) | ≥95% |
| 4 | INTEGRATION-WITH-VISUAL-ASSET-2026-05-07.md | 2000 (与 U4 visual_asset state machine FK + audit_passed 字段) | ≥95% |
| 5 | PF-V-P2-MIGRATION-PATH-2026-05-07.md | 2200 (现 PF-V S04-S09 输出 → state_library 迁移方案) | ≥95% |
| 6 | A11Y-CONTRAST-VALIDATOR-2026-05-07.md | 2000 (WCAG 2.2 实测 + 自动化 script) | ≥95% |
| 7 | LIVE-WEB-EVIDENCE-2026-05-07.md | 2500 (≥15 vendor + 访问日期) | ≥95% |
| 8 | SINGLE-USER-IMPLEMENTATION-BUDGET-2026-05-07.md | 1500 (≤900 行 / ≤1.5 周) | ≥95% |
| 9 | README-deliverable-index-2026-05-07.md | 1200 | 100% |

总字数 ≥**20000**

## §8 Self-audit (≥15)

- 5-Gate 主观 gate 是否伪自动化
- 48 state 真覆盖 8 panel 现实状态空间
- a11y contrast ratio 是否真测
- 与 PF-V 工作是否冲突 (PF-V 在产 image, 这里在 register state)
- live web URL 真访问
- 与 U4 visual_asset / U5 dispatch ledger / U6 visual-DAM 表 FK 是否对齐
- single-user budget 真实
- Storybook reuse vs 自建简易 browser

## §9 Truthful Stdout Contract

```yaml
CLOUD_U7_STATE_LIBRARY_QUALITY_COMPLETE: true
zip_filename: cloud-output-U7-state-library-quality-2026-05-07.zip
files_count: 9
total_words_cjk_latin_approx: <真实>
total_thinking_minutes: <真实>
live_web_browsing_used: <true|false>
live_verified_count: <真实>
panels_inventoried: 8
states_per_panel_avg: <真实>
state_total_count: <真实, 期望 ≥48>
auto_gate_count: <真实, 期望 3 部分自动 + 2 human-in-loop>
single_user_budget_loc: <真实>
single_user_budget_dev_days: <真实>
multi_pass_completed: <真实/10>
self_audit_findings: <真实>
boundary_preservation_check: clear
ready_for_user_audit: yes
```

## §10 ZIP Filename

`cloud-output-U7-state-library-quality-2026-05-07.zip`
