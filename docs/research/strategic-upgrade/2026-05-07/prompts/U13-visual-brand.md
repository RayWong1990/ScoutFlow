---
title: Cloud Prompt — U13 Visual Style System & Brand Atlas v0 (≥80 文件)
status: candidate / cloud_prompt / not-authority
authority: not-authority
created_at: 2026-05-07
target_window: GPT Pro web 浏览模式
expected_zip_files: 80+
expected_zip_words_cjk_latin: 120000+
expected_thinking_minutes: 150+
---

# Cloud Prompt — U13 Visual Style System & Brand Atlas

## §1 Mission

ScoutFlow 是 single-user / strong visual / 深海蓝 operator workstation 定位. 用户已沉淀深海蓝 15 色 palette + 4 panel layout + 8dp grid + 5-Gate audit, 但**没有完整品牌 atlas** — 没有 token 全谱 / 没有 icon library / 没有 illustration / 没有 motion / 没有跨媒介 (PPT/poster/H5/social-card) 模板, 跨 phase 视觉资产无复用机制.

本任务: 写**完整 visual style system & brand atlas**, ≥70 个 single-file asset/spec markdown + ≥10 cluster index + 5 supporting = **≥85 文件**. PF-V 跑 GPT-Image-2 时直接对接此 atlas, 不需要每次重新推理.

## §2 Inputs

### A. ScoutFlow 现有视觉
1. ~/workspace/ScoutFlow/apps/capture-station/src/styles/ (既有 token / CSS)
2. ~/workspace/ScoutFlow/apps/capture-station/src/features/**/*.tsx (8 panel 实际样式)
3. ~/workspace/ScoutFlow/docs/visual/ (如有)
4. PF-V 当前进度 (S00-S18 prompt + Pattern A-J + INDEX.csv 19 列, 用户另窗口)
5. https://github.com/RayWong1990/ScoutFlow/blob/main/docs/research/strategic-upgrade/2026-05-07/cloud-prompt-U4-visual-asset-spine.md
6. https://github.com/RayWong1990/ScoutFlow/blob/main/docs/research/strategic-upgrade/2026-05-07/cloud-prompt-U7-state-library-quality.md

### B. 全局视觉规则
7. ~/.claude/rules/aesthetic-first-principles.md (5 Gate)

### C. 设计参考 (引用不复制)
8. Apple HIG 2026 / Material 3 expressive 2026 / WCAG 2.2

### D. Live web (asset library refresh)
9. 2026 prosumer icon library (Phosphor / Lucide / Heroicons / Tabler / Iconoir / Feather)
10. 2026 illustration source (unDraw / Storyset / Open Peeps / Lukasz Adam / Reshot)

## §3 Multi-pass Work Plan (≥10 pass, ≥150 min)

1. **Pass 1**: 读 §2 A/B + capture-station code 抽出现 token / palette / typo
2. **Pass 2 — Live web**: ≥15 真实 search prosumer icon/illustration/pattern library 2026
3. **Pass 3 — Token system 全谱 (~5 entry)**: 
   - PALETTE-15-color-deep-blue + 5 衍生 (warning/error/success/neutral/accent)
   - TYPOGRAPHY-ramp (中英双语 5 size × 4 weight, 含字体选型: Inter / SF Pro / 苹方 / 思源黑体)
   - SPACING-8dp-grid + radius (4/8/12/16/24)
   - SHADOW-elevation (5 层)
   - MOTION-token (duration 4 档 + easing curve)
4. **Pass 4 — Icon library 30 entry (汇总)**: 选 ≥50 icon (capture / vault / preview / scope / trust / amend / dispatch / vendor / signal / hypothesis 等), 每 entry 含 SVG path / 用法 / 5-Gate 状态
5. **Pass 5 — Illustration library 15 entry (汇总)**: hero illustration (8 panel 各一) / spot illustration / empty-state / error-state / loading-state, 每 entry 含 SVG / 风格 / 用法
6. **Pass 6 — Pattern library 10 entry (汇总)**: background pattern / texture / divider / 装饰元素
7. **Pass 7 — 8 panel design spec (8 entry)**: URL bar / live metadata / capture scope / trust trace / topic-card-preview / topic-card-vault / four-panel-shell / main-nav, 每 entry 含 layout / token 引用 / state variants link to U7 / 5-Gate audit case
8. **Pass 8 — Multi-medium template library (10 entry)**: PPT cover/中页/对比/数据/总结 (5) + Poster (3 sizes) + Social card (3 platform) + H5 page (10 layout 抽样)
9. **Pass 9 — 5-Gate audit test cases (5 entry 汇总, ≥30 case)**: 每 gate × ≥6 case (good vs bad 对照)
10. **Pass 10 — 跨 phase 视觉演化 + 10 cluster index + 5 supporting (master atlas / brand voice / 5-gate-test-suite / linked-asset-and-state / README) + truthful stdout**

## §4 Hard Boundaries

- candidate / not-authority 全 ≥85 文件
- 不修改 capture-station production CSS / tsx (只读)
- 不直接 commit 新 SVG/PNG 到 repo (asset 文件以 inline SVG / 描述 / hash 形式存在 markdown 内)
- 不批准实际部署 token 替换 (留给 Phase 2 dispatch)
- icon/illustration 引用第三方 library 必须标 license (MIT / OFL / CC0 等)
- 字体选型必须考虑授权 (商用 OK / 中文字体 license 注意)
- 5-Gate 主观 gate 仍 human-in-loop, 不许伪自动化

## §5 Live Web Evidence

≥15 真实 search:
- Phosphor / Lucide / Heroicons / Tabler / Iconoir / Feather icon library 2026
- unDraw / Storyset / Open Peeps illustration 2026
- Style Dictionary v4 / Tokens Studio Figma
- Apple HIG 2026 / Material 3 expressive
- WCAG 2.2 contrast standard
- Inter / SF Pro / 苹方 / 思源黑体 字体 license
- prosumer template (Canva pro / Figma Community / Webflow template)

## §6 Cross-local Search

- ~/workspace/ScoutFlow/apps/capture-station/src/styles/
- ~/workspace/ScoutFlow/docs/visual/ 如有
- ~/workspace/ScoutFlow/docs/research/ PF-V 既有沉淀
- ~/.claude/rules/aesthetic-first-principles.md
- DiloFlow 视觉风格期望
- 本机字体 ~/Library/Fonts/

## §7 Output Deliverables

ZIP filename: `cloud-output-U13-visual-style-brand-atlas-2026-05-07.zip`
File count: **≥85**

| 类别 | 文件数 | min 字 |
|---|---:|---:|
| Token system | 5 | 1800 |
| Icon library (≥50 icon, 30 file 汇总) | 30 | 800 |
| Illustration library (≥30 illustration, 15 汇总) | 15 | 1200 |
| Pattern library (≥20, 10 汇总) | 10 | 1000 |
| 8 panel design spec | 8 | 2000 |
| Multi-medium template (PPT/Poster/Social/H5) | 10 | 1500 |
| 5-Gate audit test (≥30 case, 5 汇总) | 5 | 2500 |
| 跨 phase 视觉演化 map | 5 | 1500 |
| Cluster index (10) | 10 | 1500 |
| MASTER-BRAND-ATLAS | 1 | 3500 |
| BRAND-VOICE-AND-TONE | 1 | 2200 |
| 5-GATE-TEST-SUITE-MASTER | 1 | 2500 |
| LINKED-ASSET-AND-STATE | 1 | 2000 |
| README | 1 | 1500 |
| **总计** | **≥103** | ≥130000 |

claim label coverage ≥85%; Mermaid: token relationship + 跨 phase 演化 + cluster ≥3 = ≥5 张

## §8 Self-audit (≥25)

- token 体系是否真单源 (vs 散落多文件)
- icon/illustration license 真合规 (MIT/OFL/CC0)
- 字体 license 真考虑商用
- WCAG contrast ≥4.5:1 真测每 palette 组合
- 5-Gate test case 是否真覆盖好坏对照
- 8 panel design spec 是否真用 token 引用 (无硬编码 hex)
- multi-medium template 是否真考虑跨平台尺寸 / 安全区
- 与 U4 visual_asset / U7 state-library 是否双向映射
- 单人 prosumer vs 企业品牌系统 drift

## §9 Truthful Stdout Contract

```yaml
CLOUD_U13_VISUAL_STYLE_BRAND_ATLAS_COMPLETE: true
zip_filename: cloud-output-U13-visual-style-brand-atlas-2026-05-07.zip
files_count: <真实, ≥85>
total_words_cjk_latin_approx: <真实, ≥120000>
total_thinking_minutes: <真实>
token_entries: <真实, 期望 5>
icon_count: <真实, ≥50>
illustration_count: <真实, ≥30>
pattern_count: <真实, ≥20>
panel_design_specs: 8
template_count: <真实, ≥10>
five_gate_test_cases: <真实, ≥30>
mermaid_diagrams: <真实, ≥5>
license_validated: <真实, OFL/MIT/CC0/商用 OK list>
wcag_contrast_validated_pairs: <真实>
multi_pass_completed: <真实/10>
self_audit_findings: <真实, ≥25>
boundary_preservation_check: clear
ready_for_user_audit: yes
```

## §10 ZIP Filename

`cloud-output-U13-visual-style-brand-atlas-2026-05-07.zip`

## §11 Format Guard

- icon SVG path 真实可渲染 (24×24 viewBox)
- 每 token entry 含 ref name / value / usage example
- 5-Gate test case 含 good vs bad 对照
- license 字段每 third-party asset 必填
- linked_visual_asset (U4) / linked_state (U7) 双向 cross-link
