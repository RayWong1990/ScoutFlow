---
title: Cloud Prompt — U4 Visual Asset Spine (单人 prosumer 视觉资产骨架)
status: candidate / cloud_prompt / not-authority
authority: not-authority
created_at: 2026-05-07
target_window: GPT Pro web 浏览模式
new_lane: yes (not deepening; first-pass authoring)
---

# Cloud Prompt — U4 Visual Asset Spine

## §1 Mission

ScoutFlow 是 single-user local-first 项目, 但用户运行在 **max horsepower + 强视觉 + 高质量 + 多 AI agent fleet** 模式下。当前 PRD-v3 / SRD-v3 / U1-U3 ZIP **完全没覆盖**视觉资产 / prompt / token / pattern 这 4 类原生横切支撑面。

PF-V 在跑 GPT-Image-2 逆向 H5 (~160-180 张图 / 18 GPT Pro session prompt S00-S18 / 10 evolution pattern A-J / INDEX.csv 19 列追踪)。这些**事实上已运转**的视觉资产生态当前**没有数据库表 / 没有 schema / 没有 contract / 没有跨 phase 复用机制**。

本任务: 写 4 类 prosumer 资产骨架 (visual_asset / prompt_template / design_token / pattern_library) 的完整 candidate spec, 单人量级实现 (30-100 行 SQLite 表 + ≤300 行 Python script per module)。**不是企业 DAM, 不是 minimalist YAGNI**。

## §2 Inputs

1. https://github.com/RayWong1990/ScoutFlow/blob/main/docs/PRD-v2-2026-05-04.md (单人 local-first base)
2. https://github.com/RayWong1990/ScoutFlow/blob/main/docs/SRD-v2-2026-05-04.md
3. https://github.com/RayWong1990/ScoutFlow/blob/main/docs/visual/ (如存在 design token 既有沉淀)
4. https://github.com/RayWong1990/ScoutFlow/tree/main/apps/capture-station (深海蓝 palette + 4 panel layout 既有 impl)
5. PF-V 当前进度 (用户另窗口跑) — 参考 INDEX.csv 19 列 / Pattern A-J / S00-S18 prompt 体系
6. **Live web** 真实 search 2026 prosumer 工具
7. 全局 5-Gate 视觉规则: `~/.claude/rules/aesthetic-first-principles.md` (Apple HIG + Material 3 + WCAG)

## §3 Multi-pass Work Plan (≥10 pass, ≥120 min)

1. **Pass 1**: 读 PRD-v2 / SRD-v2 / capture-station code / PF-V 当前进度, 识别 4 类资产事实运转点
2. **Pass 2 — Live web**: 真实 search ≥20: prosumer DAM (Air / Brandfolder / Eagle / Mylio / Raycast / Pixelmator) / prompt registry pattern / design token (Style Dictionary / Theo / Tokens Studio) / pattern library (Storybook / Bit / pattern lab) / 2026 image-to-code (Anima / Locofy / Builder.io / Visual Copilot)
3. **Pass 3 — visual_asset 模块 spec**: SQLite 表 schema (asset_id / kind ∈ {raw_screenshot / gpt_image_2 / svg / mockup / icon / illustration / token_visual} / state ∈ {gen / candidate / refined / locked / deprecated} / parent_asset_id / prompt_id FK / pattern_tag (A-J or null) / sha256 / perceptual_hash / dimensions / file_path / phase / 5_gate_audit_passed / created_at), CRUD script, thumbnail+pHash 生成 cron, 跨 phase 复用 query
4. **Pass 4 — prompt_template 模块 spec**: SQLite 表 (prompt_id / kind ∈ {gpt_pro_session / dispatch_prompt / image_gen / code_gen / audit_prompt} / version / parent_prompt_id (lineage) / template_body / parameter_schema / cost_per_run_usd / output_quality_score / used_in_phase[] / created_at / superseded_by), CRUD, lineage tree query, S00-S18 + Run-1 ~ Run-5 dispatch prompt 全收编为 v0 backfill
5. **Pass 5 — design_token 模块 spec**: 单文件 `design-tokens.json` (Style Dictionary 兼容) + cascade rule (深海蓝 palette + typography ramp + 8dp grid + radius + shadow + motion), 引用方: capture-station React + PF-V H5 + 未来 PPT/poster, watch-and-rebuild script
6. **Pass 6 — pattern_library 模块 spec**: SQLite 表 (pattern_id / domain ∈ {image_refine / code_refactor / copy / data_extract / dispatch_prompt} / pattern_letter (A-J 或扩展) / description / when_to_use / when_not_to_use / usage_count / success_rate / example_artifacts[]), 与 visual_asset.pattern_tag 双向 link
7. **Pass 7 — 4 模块互通 contract**: visual_asset.prompt_id → prompt_template.prompt_id, visual_asset.pattern_tag → pattern_library.pattern_letter, pattern_library.example_artifacts → visual_asset.asset_id, design_token cascade 引用方记录
8. **Pass 8 — Single-user implementation budget**: 4 模块各 ≤ 300 行 Python + SQLite + 1 cron + 1 watch script, 总 ≤ 1500 行 / ≤ 1 周开发
9. **Pass 9 — Self-audit ≥15**: prosumer 量级 vs 企业 DAM drift / single-user vs multi-user / boundary preservation / 5-Gate 集成是否真覆盖
10. **Pass 10**: README + truthful stdout

## §4 Hard Boundaries

- candidate / not-authority 全文件
- write_enabled=False 不变 (本 lane 不解禁 vault write; visual_asset 写自己的 SQLite 表)
- 不批准 production code 修改 (apps/capture-station/** services/** 等仍 hold)
- spec 仅描述，不附带 dispatch authorization
- design token cascade 仅 candidate JSON, 不替换现有 capture-station 任何 CSS / token
- 5-Gate 引用 `~/.claude/rules/aesthetic-first-principles.md` (canonical, 不重写)

## §5 Live Web Evidence Refresh

≥20 真实 search:
- prosumer DAM 2026: Air, Brandfolder, Eagle, Mylio, Raycast, Pixelmator, Bear DAM
- design token 2026: Style Dictionary v4, Tokens Studio Figma, Theo, Specify
- image-to-code 2026: Anima, Locofy, Builder.io Visual Copilot, v0.dev, screenshot-to-code
- prompt registry pattern: PromptLayer, LangSmith Hub, Helicone, prompt-as-code
- pattern library 2026: Storybook 8, Bit Cloud, Pattern Lab
- single-creator workflow: ImagineArt, Raelume, Freepik Spaces, Krea, MindStudio
- Apple HIG 2026 update / Material 3 expressive 2026

## §6 Cross-local Search

- `~/workspace/ScoutFlow/apps/capture-station/src/styles/` 既有深海蓝 token (如有)
- `~/workspace/ScoutFlow/docs/research/` PF-V / wave / 视觉相关沉淀
- `~/workspace/ScoutFlow/docs/visual/` 如存在
- PF-V 当前 INDEX.csv 19 列 schema (用户另窗口在跑)
- `~/.claude/rules/aesthetic-first-principles.md` 5-Gate canonical
- DiloFlow 是否有视觉风格期望

## §7 Output Deliverables

ZIP filename: `cloud-output-U4-visual-asset-spine-2026-05-07.zip`
File count: **10**

| # | File | min 字 | claim label |
|---|---|---:|---|
| 1 | MODULE-visual-asset-spec-2026-05-07.md | 3000 (含 SQLite DDL + Python CRUD + thumbnail/pHash cron) | ≥95% |
| 2 | MODULE-prompt-template-spec-2026-05-07.md | 2800 (含 lineage tree + S00-S18 backfill 清单) | ≥95% |
| 3 | MODULE-design-token-spec-2026-05-07.md | 2500 (含完整 design-tokens.json + cascade 引用方) | ≥95% |
| 4 | MODULE-pattern-library-spec-2026-05-07.md | 2500 (Pattern A-J + 扩展 domain) | ≥95% |
| 5 | CROSS-MODULE-CONTRACT-2026-05-07.md | 2000 (4 模块 FK + 互通 query) | ≥95% |
| 6 | SINGLE-USER-IMPLEMENTATION-BUDGET-2026-05-07.md | 1800 (≤1500 行代码 / ≤1 周 / ≤$X 预算) | ≥95% |
| 7 | PF-V-INTEGRATION-MAP-2026-05-07.md | 2000 (现 PF-V INDEX.csv ↔ visual_asset 表迁移) | ≥95% |
| 8 | 5-GATE-AUTOMATION-HOOKS-2026-05-07.md | 1800 (5-Gate audit 自动化挂入 visual_asset state machine) | ≥95% |
| 9 | LIVE-WEB-EVIDENCE-2026-05-07.md | 2500 (≥20 vendor / pattern URL + access date) | ≥95% |
| 10 | README-deliverable-index-2026-05-07.md | 1200 | 100% |

总字数 ≥**22000**

## §8 Self-audit (≥15 finding)

- prosumer DAM vs 企业 DAM drift
- single-user vs multi-user 假设
- design token JSON cascade 是否真单源
- prompt lineage 是否真覆盖 S00-S18 + dispatch prompt
- pattern A-J 是否真覆盖 image / 是否真延伸到 code/copy/data
- 5-Gate 集成是否真自动化（不是手动 review）
- live web URL 真访问
- 与 U1/U2/U3 是否冲突 (entity vs visual_asset 混淆?)
- single-user budget 数字真实可达 vs 一厢情愿

## §9 Truthful Stdout Contract

```yaml
CLOUD_U4_VISUAL_ASSET_SPINE_COMPLETE: true
zip_filename: cloud-output-U4-visual-asset-spine-2026-05-07.zip
files_count: 10
total_words_cjk_latin_approx: <真实>
total_thinking_minutes: <真实>
live_web_browsing_used: <true|false>
live_verified_vendor_count: <真实>
modules_specced: 4
sqlite_ddl_count: <真实, 表数>
python_pseudocode_loc_total: <真实, 估算>
single_user_budget_estimate_loc: <真实>
single_user_budget_estimate_dev_days: <真实>
multi_pass_completed: <真实/10>
self_audit_findings: <真实>
boundary_preservation_check: clear
ready_for_user_audit: yes
```

## §10 ZIP Filename

`cloud-output-U4-visual-asset-spine-2026-05-07.zip`
