---
title: Cloud Prompt — U2 Deep Supplement (Phase 2 Unlock Playbook 二轮深化)
status: candidate / cloud_prompt / not-authority
authority: not-authority
created_at: 2026-05-07
target_window: GPT Pro web 浏览模式 (live web browsing required)
prev_zip: cloud-output-U2-phase-2-unlock-playbook-2026-05-07.zip
---

# Cloud Prompt — U2 Deep Supplement

## §1 Mission

你已交付 cloud-output-U2 ZIP 11 文件（5 lane playbook + VENDOR-MATRIX 40 行 + RISK-REGISTER 45 条 + SPIKE-RUNBOOK + AUDIT-FRAMEWORK + DECISION-TREE + README）。**坦白记录: live web browsing was unavailable; run receipt URLs returned 404; vendor evidence is paste-time only**.

本轮任务: **在已有 ZIP 基础上写 supplementary ZIP**, 补每 lane 的实际命令清单 / 真实 fail-mode case study / 三维 vendor 矩阵 (risk × cost × quality) / 时间估算 / live web evidence refresh / 二轮 self-audit。**不重写**, 是补充。

## §2 Inputs

1. 前轮 ZIP 11 文件（你自己产物）— 重读 LANE-1 ~ LANE-5 playbook + VENDOR-MATRIX + RISK-REGISTER 识别浅处
2. https://github.com/RayWong1990/ScoutFlow/blob/main/docs/research/post-frozen/overflow-registry-v0.md
3. https://github.com/RayWong1990/ScoutFlow/blob/main/docs/research/t-p1a-021-bbdown-runtime-gate-matrix-2026-05-04.md
4. https://github.com/RayWong1990/ScoutFlow/blob/main/docs/research/t-p1a-022-asr-pipeline-prestudy-2026-05-04.md
5. https://github.com/RayWong1990/ScoutFlow/blob/main/docs/research/t-p1a-023-llm-normalization-schema-2026-05-04.md
6. https://github.com/RayWong1990/ScoutFlow/blob/main/docs/research/t-p1a-025-db-ledger-vnext.md
7. https://github.com/RayWong1990/ScoutFlow/blob/main/services/api/scoutflow_api/bridge/config.py (write_enabled=False)
8. https://github.com/RayWong1990/ScoutFlow/blob/main/docs/research/strategic-upgrade/2026-05-07/cloud-prompt-U2-phase-2-unlock-playbook.md
9. **Live web** 真实 search 2-month evidence

## §3 Multi-pass Work Plan (≥10 pass, ≥120 min wall-clock)

1. **Pass 1**: 重读 cloud-output-U2 ZIP 11 文件，每文件标 ≥3 处深度不足
2. **Pass 2**: 读 base 6 个 t-p1a-021/022/023/025 + overflow-registry + bridge/config.py
3. **Pass 3 — Live web refresh**: 真实联网 search ≥20 vendor 现状 — 不许复用 paste-time
4. **Pass 4 — Spike runbook expansion**: 5 lane 每 lane 加实际命令清单（具体 shell / python / docker invocation, ≥30 命令 / lane）
5. **Pass 5 — 3D vendor matrix**: VENDOR-MATRIX 40 行升级到 (vendor × dim) — 每 vendor 加 risk_score / cost_per_1k_capture / quality_score / legal_posture / sandboxability_score 5 维数字打分
6. **Pass 6 — Fail-mode case study**: 每 lane 加 ≥3 真实 fail-mode case study（描述 input / 触发条件 / 失败现象 / detect signal / rollback step / 时间成本）
7. **Pass 7 — Time/cost estimation**: 每 lane unlock 估算总时间（spike + audit + dispatch + 收尾），单人量级 (1 dev) / 实际工作日数 / Claude+GPT 预算
8. **Pass 8 — Cross-lane dependency graph**: Mermaid graph 显示 5 lane 互相依赖（Lane-2 ASR 依赖 Lane-1 vault 真写? Lane-5 Signal Workbench 依赖 entity v0 contract?）
9. **Pass 9 — Self-audit v2**: ≥20 新 finding
10. **Pass 10**: README-supplement + truthful stdout

## §4 Hard Boundaries

- candidate / not-authority 全文件
- write_enabled=False 不变
- 不批准任何 lane unlock — 仍然只是 candidate playbook
- 不写 services/api/migrations/** workers/** 等 production path
- vendor 仍然是 [evaluation-candidate], 不许出现"已采纳"
- 命令清单仅供 spike 用, 不许暗示"立即执行"

## §5 Live Web Evidence Refresh

**禁止**复用上轮 paste-time。真实 search ≥20:
- Bilibili C&D 后续 (BiliFix / 第三方代理服务 / 法务 update)
- yt-dlp 2026 美国 EU 法律 + DMCA / safe harbor
- Whisper-large-v3-turbo / Parakeet-TDT-0.6B / Voxtral-Mini Apple Silicon benchmark
- Apple Foundation Models 2026-04 ~ 05 update
- Apify / Bright Data / ScraperAPI 2026 价格 + ToS
- Playwright / browser-use / claude-computer-use 2026
- XHS scraper landscape 2026 (无官方 API 现状)
- yt-dlp CVE 2026
- Temporal 2026 durable agent execution
- 中国大陆 ASR 选型 (paraformer / 通义听悟 / 讯飞)

## §6 Cross-local Search

- `~/.local/bin/whisper` / `pip show openai-whisper` / brew list 验证本机已装 ASR
- `~/workspace/contentflow/` 历史 ASR 踩坑记录
- `~/workspace/hermes-agent/` openai venv 配置
- `~/workspace/DiloFlow/` 期望的 capture 输入格式
- `~/.claude/skills/` 是否已有 vendor / runtime / browser 相关 skill

## §7 Output Deliverables

ZIP filename: `cloud-output-U2-deep-supplement-2026-05-07.zip`
File count: **9** (exactly)

| # | File | min 字 | min Mermaid | claim label |
|---|---|---:|---:|---|
| 1 | LANE-1-true-vault-write-spike-commands-2026-05-07.md | 2500 | 1 | ≥95% |
| 2 | LANE-2-runtime-tools-spike-commands-2026-05-07.md | 3500 | 2 | ≥95% |
| 3 | LANE-3-browser-automation-spike-commands-2026-05-07.md | 2500 | 1 | ≥95% |
| 4 | LANE-4-dbvnext-migration-spike-commands-2026-05-07.md | 2500 | 1 | ≥95% |
| 5 | LANE-5-signal-workbench-spike-commands-2026-05-07.md | 2500 | 1 | ≥95% |
| 6 | VENDOR-MATRIX-3D-SCORED-2026-05-07.md | 4000 | 0 | ≥95% (每 vendor 5 维数字打分) |
| 7 | FAIL-MODE-CASE-STUDIES-2026-05-07.md | 4500 | 0 | ≥95% (≥15 case across 5 lane) |
| 8 | TIME-COST-ESTIMATION-CROSS-LANE-2026-05-07.md | 2200 | 1 (cross-lane Mermaid graph) | ≥95% |
| 9 | README-supplement-index-2026-05-07.md | 1200 | 0 | 100% |

总字数 ≥**25000**

## §8 Self-audit (Pass 9)

≥20 findings inline fix。涵盖:
- spike 命令是否泄露 vendor 偏好（应保持 vendor-neutral）
- 三维矩阵是否暴露 unlock 暗示
- fail-mode case 是否真实可触发（不是脑补）
- time/cost 估算是否单人量级 vs 团队估算
- live web evidence URL 是否真访问
- cross-local search 是否真做
- 与 U1 deep + U3 ZIP 是否冲突

## §9 Truthful Stdout Contract

```yaml
CLOUD_U2_DEEP_SUPPLEMENT_COMPLETE: true
zip_filename: cloud-output-U2-deep-supplement-2026-05-07.zip
files_count: 9
total_words_cjk_latin_approx: <真实>
total_thinking_minutes: <真实，不许伪造>
live_web_browsing_used: <true|false>
live_search_queries_count: <真实>
live_verified_vendor_count: <真实>
paste_time_vendor_count: <真实>
multi_pass_completed: <真实/10>
self_audit_findings: <真实>
spike_commands_count_total: <真实>
fail_mode_cases_count: <真实>
boundary_preservation_check: clear
ready_for_user_audit: yes
```

## §10 ZIP Filename

`cloud-output-U2-deep-supplement-2026-05-07.zip`
