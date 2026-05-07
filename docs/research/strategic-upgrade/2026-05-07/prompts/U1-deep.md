---
title: Cloud Prompt — U1 Deep Supplement (PRD-v3 / SRD-v3 二轮深化)
status: candidate / cloud_prompt / not-authority
authority: not-authority
created_at: 2026-05-07
target_window: GPT Pro web 浏览模式 (live web browsing required)
prev_zip: cloud-output-U1-prd-v3-srd-v3-2026-05-07.zip
---

# Cloud Prompt — U1 Deep Supplement

## §1 Mission

你已交付 cloud-output-U1 ZIP 7 文件（PRD-v3 / SRD-v3 / AMENDMENT-FOLD / TRANSITION / TRACEABILITY / SELF-AUDIT / README）。**坦白记录：上轮无 live web browsing，wall-clock 不足 90 min，是 compressed best-effort**。

本轮任务：**在已有 ZIP 基础上写 supplementary ZIP**，补 worked example / anti-pattern / NFR / sibling egress / 真实 web evidence refresh / 二轮 self-audit。**不重写**前轮文件，是补充。

## §2 Inputs (must read or fetch in this order)

1. 前轮 ZIP 7 文件（你自己产物）— 读 PRD-v3-candidate.md 和 SRD-v3-candidate.md 全文识别浅处
2. https://github.com/RayWong1990/ScoutFlow/blob/main/docs/PRD-v2-2026-05-04.md (base)
3. https://github.com/RayWong1990/ScoutFlow/blob/main/docs/SRD-v2-2026-05-04.md (base)
4. https://github.com/RayWong1990/ScoutFlow/blob/main/docs/research/post-frozen/runs/EXTERNAL-AUDIT-REPORT-2026-05-07.md (Run-3+4 audit)
5. https://github.com/RayWong1990/ScoutFlow/blob/main/docs/research/strategic-upgrade/2026-05-07/cloud-prompt-U1-prd-v3-srd-v3.md (上轮 prompt 自检)
6. https://github.com/RayWong1990/ScoutFlow/blob/main/services/api/scoutflow_api/bridge/config.py (write_enabled=False:24,36)
7. https://github.com/RayWong1990/ScoutFlow/blob/main/docs/research/post-frozen/overflow-registry-v0.md (5 overflow lane)
8. **Live web** 真实 search 2-month vendor / pattern 现状（不许复用 paste-time）

## §3 Multi-pass Work Plan (≥10 pass, ≥120 min wall-clock)

1. **Pass 1 — Gap scan**: 重读 cloud-output-U1 ZIP 7 文件，每文件标 ≥3 处深度不足（缺 example / 缺反例 / 缺数字 / 缺 cross-link）
2. **Pass 2 — Base re-read**: PRD-v2 / SRD-v2 全文 + 4 run amendment trail (PR #199 / #231 / #239 / #240)
3. **Pass 3 — Live web refresh**: 真实 search ≥15 条 2-month evidence (Bilibili 法务 update / Whisper-Parakeet-Voxtral on Apple Silicon / yt-dlp 2026 法务 / Apple Foundation Models / ontology renaissance / agentic PKM / single-user DAM / multi-agent orchestration / structured outputs / Temporal durable / prompt caching) — 每条标 [live-verified-2026-05-07-yyyy-mm-dd] vs [paste-time-only]
4. **Pass 4 — Worked example expansion**: 对 PRD-v3 §1-§N 各加 ≥2 worked example（真实场景：用户当前正在 PF-V 跑 GPT-Image-2 / 4 run 协作 / Claude+Codex+Hermes 切换）
5. **Pass 5 — Anti-pattern extraction**: 对 SRD-v3 §1-§N 各加 ≥2 anti-pattern（错误实现 / 4 run 中实际触发的 silent flexibility / amendment trigger）
6. **Pass 6 — NFR for single-user**: 加 NFR 章 — 单人量级 capacity (Signal/天 5-50, SQLite N 万行, p99 < 100ms 本地, cost ≤ $X/天 GPT/Claude) — **不是企业 SLO**
7. **Pass 7 — Sibling egress**: 加 SIBLING-EGRESS 章 — DiloFlow / RAW vault / Obsidian / hermes-agent 4 个下游各自 manifest contract（约定 frontmatter / 目录结构 / handoff timestamp / redaction rule）— **不是 SDK，是文件约定**
8. **Pass 8 — Traceability extension**: TRACEABILITY-MATRIX 从 50 行扩到 ≥80 行，每行 cross-link 到具体 PR # / commit SHA / file:line
9. **Pass 9 — Deep self-audit v2**: 在前轮 self-audit 基础上找 ≥20 新 finding，分 critical / high / medium，每条 fix-or-bound inline
10. **Pass 10 — README + truthful stdout**: 写 README-supplement-index + truthful stdout contract（**禁止伪造 wall-clock**）

## §4 Hard Boundaries (不可越界)

- candidate / not-authority frontmatter 全文件强制
- write_enabled=False (bridge/config.py:24,36) 不变
- authority files (current.md / task-index.md / decision-log.md / AGENTS.md) **不写**
- 5 overflow lane (true_vault_write / runtime_tools / browser_auto / dbvnext_migration / signal_workbench) 全 Hold
- 不批准: BBDown live / yt-dlp / ffmpeg / ASR / browser automation / migration
- 不修改 services/** apps/** workers/** packages/** data/** referencerepo/**
- 不引入新 vendor 作为"已采纳"，所有 vendor 都是 [evaluation-candidate]

## §5 Live Web Evidence Refresh (硬要求)

**禁止**复用上轮 paste-time evidence。本轮**必须**真实联网 search ≥15 vendor / pattern，每条带 URL + 访问日期 + 摘要 + [live-verified-2026-05-07] 标签。覆盖：
- 法务: Bilibili C&D 后续 / yt-dlp 美国 EU 法律 / 抓取数据合规 / GDPR 个人数据
- ASR: Whisper-Parakeet-Voxtral 2026-04 ~ 2026-05 性能 benchmark / Apple Silicon path / hallucination 率
- LLM: Apple Foundation Models / Claude 4.7 / GPT-5 / 国内大模型选型
- PKM: 2026 ontology vs KG / agentic capture pattern / local-first stack
- DAM: prosumer 单人 DAM 选型 (Air / Brandfolder / Eagle / Mylio) — 你之前没研究 prosumer 段
- Orchestration: multi-agent fleet / Temporal / LangGraph / dispatch ledger pattern

## §6 Cross-local Search (本机交叉)

- `~/workspace/ScoutFlow/docs/research/` 全目录递归 — 找 PF-V / wave / dispatch / candidate 既有沉淀
- `~/workspace/DiloFlow/` (sibling, 频道看见看不见 downstream consumer) — 看其期望的 capture 输入格式
- `~/workspace/contentflow/` (legacy) — 历史踩坑沉淀
- `~/.claude/skills/` 看是否已有相关 skill 可引
- 本机 Whisper 安装路径 — 验证 ASR vendor 现实可行性

## §7 Output Deliverables (严格 schema)

ZIP filename: `cloud-output-U1-deep-supplement-2026-05-07.zip`
File count: **8** (exactly)

| # | File | min 字 | min Mermaid | claim label coverage |
|---|---|---:|---:|---|
| 1 | PRD-v3-supplement-worked-examples-2026-05-07.md | 4500 | 2 | ≥95% paragraph |
| 2 | SRD-v3-supplement-anti-patterns-2026-05-07.md | 4500 | 2 | ≥95% |
| 3 | NFR-SINGLE-USER-CAPACITY-2026-05-07.md | 2200 | 1 | ≥95% |
| 4 | SIBLING-PROJECT-EGRESS-CONTRACT-2026-05-07.md | 3500 | 2 | ≥95% |
| 5 | TRACEABILITY-MATRIX-EXTENDED-2026-05-07.md | (≥80 row) | 0 | ≥90% |
| 6 | WEB-EVIDENCE-REFRESH-LIVE-2026-05-07.md | 3000 | 0 | ≥95% (每条带 URL + 访问日期) |
| 7 | DEEP-AUDIT-V2-FINDINGS-2026-05-07.md | (≥20 finding) | 0 | ≥95% |
| 8 | README-supplement-index-2026-05-07.md | 1200 | 0 | 100% |

总字数 ≥**19000** (CJK + Latin tokens approx)

## §8 Self-audit (Pass 9)

≥20 findings，每条 inline fix-or-bound。涵盖：
- claim label coverage 是否真 ≥95%（非自报）
- web evidence 是否真 live（非 paste-time）— 列出 search query 历史
- single-user vs enterprise drift（是否又写了 enterprise pattern）
- boundary leak（是否暗示 unlock）
- worked example 是否真用 4 run 实际场景
- anti-pattern 是否真用历史 amendment trigger
- NFR 数字是否单人量级 vs 企业 SLO
- TRACEABILITY-MATRIX 抽样 10 行核 GitHub URL 是否真存在
- cross-local search 是否真做（不是宣称做）
- 与 U2 / U3 ZIP cross-reference 一致性

## §9 Truthful Stdout Contract

输出 README-supplement-index.md §5 必须含:
```yaml
CLOUD_U1_DEEP_SUPPLEMENT_COMPLETE: true
zip_filename: cloud-output-U1-deep-supplement-2026-05-07.zip
files_count: 8
total_words_cjk_latin_approx: <真实数>
total_thinking_minutes: <真实分钟，不许伪造>
live_web_browsing_used: <true|false>
live_search_queries_count: <真实数>
live_verified_evidence_count: <真实数>
paste_time_evidence_count: <真实数>
multi_pass_completed: <真实/10>
self_audit_findings: <真实数>
critical_issues_fixed_inline: <真实数>
known_limitations:
  - <如有任何环境限制必须显式列出>
boundary_preservation_check: clear
ready_for_user_audit: yes
```

**禁止**: 伪造 wall-clock 分钟 / 伪造 live web 但实际未联网 / 伪造 cross-local search

## §10 ZIP Filename

`cloud-output-U1-deep-supplement-2026-05-07.zip` — 严格匹配
