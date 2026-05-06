---
title: Cloud GPT Pro Prompt — U2 Phase 2 Unlock Playbook (5-lane comprehensive)
status: candidate / cloud-prompt / not-authority
authority: not-authority
execution_approval: not-approved
runtime_approval: not-approved
migration_approval: not-approved
created_at: 2026-05-07
target_writer: Cloud ChatGPT Pro single window (deep thinking mode, ≥2h)
project_root: /Users/wanglei/workspace/ScoutFlow
github_repo: https://github.com/RayWong1990/ScoutFlow (public during the 4h cloud window)
target_output: ZIP bundle, 11 markdown files, total ~15K Chinese+English words
deliverable_kind: download_link
expected_thinking_time: 120-150 minutes
relates_to:
  - overflow registry v0: docs/research/post-frozen/overflow-registry-v0.md
  - BBDown gate matrix: docs/research/t-p1a-021-bbdown-runtime-gate-matrix-2026-05-04.md
  - ASR prestudy: docs/research/t-p1a-022-asr-pipeline-prestudy-2026-05-04.md
  - LLM normalization: docs/research/t-p1a-023-llm-normalization-schema-2026-05-04.md
  - DB ledger vNext: docs/research/t-p1a-025-db-ledger-vnext.md
---

# Cloud GPT Pro Prompt — U2 Phase 2 Unlock Playbook (5 Lanes)

> Paste this entire document into Cloud ChatGPT Pro deep-thinking window (separate from U1, U3 windows).
> Output deliverable = a single download link to a ZIP file containing 11 markdown files.
> Expected total deep-thinking duration: 120-150 minutes minimum.

---

## §0 Pre-flight (user 已跑过，此处仅 reminder)

- repo PUBLIC during 4h cloud window
- baseline_origin_main: `ea509022eb05a552777373394a6fc2a5077f27f6`
- 3 cloud window 同时跑 (U1 / U2 / U3)，互相不知道对方产物

---

```
<<<CLOUD U2 BEGIN>>>

You are Cloud ChatGPT Pro acting as a senior Phase 2 unlock architect for the ScoutFlow project. Your single mission is to author a comprehensive Phase 2 Unlock Playbook covering all 5 currently-Hold lanes (true_vault_write / runtime_tools / browser_automation / dbvnext_migration / signal_workbench), each with vendor multi-matrix, spike runbook, audit framework, decision tree, and risk register. Output is a downloadable ZIP bundle with 11 markdown files.

This is candidate research authoring only. It is NOT runtime approval, NOT migration approval, NOT vault true-write approval, NOT browser-automation approval, NOT BBDown / yt-dlp / ffmpeg / ASR unlock. You are authoring the **conditions / steps / evidence required** to unlock each lane, not unlocking them.

You must take at least 90 minutes of deep thinking BEFORE producing the final output.

## §1 Project Identity

- repo: https://github.com/RayWong1990/ScoutFlow (PUBLIC during your 4h work)
- live status: WAVE_6_CANDIDATE_OPEN / NOT_EXECUTION_APPROVED
- baseline_origin_main: `ea509022eb05a552777373394a6fc2a5077f27f6` (Run-3+4 receipt amendment merged)
- Single-user, local-first, Bilibili first / XHS later / YouTube outlook
- 4 run + 1 window-2 实证 ScoutFlow 工程纪律 (80-pack 7-cluster + 3-window cloud audit + amend_and_proceed)
- 当前局部最优: preview-only / metadata_only / write_enabled=False / forbidden vendor 全 Hold

## §2 5 Lane Definition (sourced from overflow-registry-v0.md)

### Lane-1 `true_vault_write`
- **现状**: Bridge + Vault preview-only / dry-run；`write_enabled=False` hardcoded at `services/api/scoutflow_api/bridge/config.py:24,36`；no RAW handoff proof exists
- **解禁价值**: 真把 ScoutFlow capture 写入用户 RAW 知识库 (`~/workspace/raw/00-Inbox/`)，从 staged note 升到 real intake
- **当前红线**: `write_enabled=False` invariant + RAW staging 在 repo 内 + 不写 `~/workspace/raw/`

### Lane-2 `runtime_tools`
含 4 个 sub-lane:
- **2a BBDown live**: 当前 BBDown / `audio_transcript` blocked。Bilibili 2026-01-28 cease-and-desist 已发，第三方 API doc 受法律压力
- **2b yt-dlp**: 当前 blocked。但 yt-dlp metadata-only `skip_download:True` 在 US/EU 法律安全
- **2c ffmpeg**: 当前 blocked (audio extraction toolchain)
- **2d ASR (Whisper / Parakeet / Voxtral)**: 当前 `audio_transcript` runtime blocked。但 Whisper 大量优化 + Apple Silicon 支持成熟
- **解禁价值**: 真 metadata fetch + 真 audio transcript + 真内容理解
- **当前红线**: 不解禁任何一个 (整组 forbidden lane)

### Lane-3 `browser_automation`
- **现状**: Playwright / Selenium / Puppeteer all blocked
- **解禁价值**: 真 visual UAT (替代 Run-2 之 synthetic UAT) + 真 frontend smoke test + 真 e2e
- **当前红线**: 不 default execution；视觉 gate 走 human-reviewed screenshot packet

### Lane-4 `dbvnext_migration`
- **现状**: `services/api/migrations/**` FORBIDDEN; DB schema 不动；topic_card / signal / hypothesis / capture_plan 不在 SQLite authority schema
- **解禁价值**: Phase 2 entity (signal/hypothesis/capture_plan/topic_card) 真上库
- **当前红线**: 任何 migration 须独立 dispatch + user 显式授权 + 单独 PR + 外审

### Lane-5 `full_signal_workbench`
- **现状**: Signal Workbench (ranking / scoring / recommendation) 是 future product line。当前只有 topic-card-lite v0
- **解禁价值**: 真产品价值 (帮 user 决定 follow / park / reject)
- **当前红线**: docs-only / preview-only output 不构成 unlock 理由

## §3 Required Inputs

If the repo is reachable (PUBLIC), fetch each. If not, ask user to paste.

### §3.1 Base authority

- https://github.com/RayWong1990/ScoutFlow/blob/main/docs/current.md
- https://github.com/RayWong1990/ScoutFlow/blob/main/AGENTS.md
- https://github.com/RayWong1990/ScoutFlow/blob/main/docs/PRD-v2-2026-05-04.md
- https://github.com/RayWong1990/ScoutFlow/blob/main/docs/SRD-v2-2026-05-04.md

### §3.2 Lane-specific candidate research

- Lane-1 / Lane-4: https://github.com/RayWong1990/ScoutFlow/blob/main/docs/research/post-frozen/overflow-registry-v0.md
- Lane-2a / 2b / 2c: https://github.com/RayWong1990/ScoutFlow/blob/main/docs/research/t-p1a-021-bbdown-runtime-gate-matrix-2026-05-04.md
- Lane-2d (ASR): https://github.com/RayWong1990/ScoutFlow/blob/main/docs/research/t-p1a-022-asr-pipeline-prestudy-2026-05-04.md
- LLM normalization: https://github.com/RayWong1990/ScoutFlow/blob/main/docs/research/t-p1a-023-llm-normalization-schema-2026-05-04.md
- Lane-4 DB vNext: https://github.com/RayWong1990/ScoutFlow/blob/main/docs/research/t-p1a-025-db-ledger-vnext.md
- Lane-5 future signal: https://github.com/RayWong1990/ScoutFlow/blob/main/docs/research/post-dispatch176-roadmap-candidate-2026-05-05.md
- ScoutFlow ↔ RAW SoR: https://github.com/RayWong1990/ScoutFlow/blob/main/docs/research/post-dispatch176-scoutflow-raw-bridge-candidate-2026-05-05.md

### §3.3 4 run receipts (evidence layer)

- Run-1: https://github.com/RayWong1990/ScoutFlow/blob/main/docs/research/post-frozen/runs/RUN-1-CODEX0-REPORT-2026-05-06.md
- Run-2: https://github.com/RayWong1990/ScoutFlow/blob/main/docs/research/post-frozen/runs/RUN-2-CODEX0-REPORT-2026-05-06.md
- Run-3+4: https://github.com/RayWong1990/ScoutFlow/blob/main/docs/research/post-frozen/runs/RUN-3-4-CODEX0-REPORT-2026-05-06.md
- Window-2: https://github.com/RayWong1990/ScoutFlow/blob/main/docs/research/post-frozen/runs/RUN-W2-CODEX0-DOCS-REPORT-2026-05-06.md

### §3.4 Live truth bridge code

- bridge/config.py: https://github.com/RayWong1990/ScoutFlow/blob/main/services/api/scoutflow_api/bridge/config.py
- bridge/router.py: https://github.com/RayWong1990/ScoutFlow/blob/main/services/api/scoutflow_api/bridge/router.py
- bridge/schemas.py: https://github.com/RayWong1990/ScoutFlow/blob/main/services/api/scoutflow_api/bridge/schemas.py
- main.py: https://github.com/RayWong1990/ScoutFlow/blob/main/services/api/scoutflow_api/main.py

## §4 Required Output Structure — ZIP Bundle Schema (STRICT)

Output **a single download link** to a ZIP named `cloud-output-U2-phase-2-unlock-playbook-2026-05-07.zip`, containing **11 markdown files** with the following STRICT schema:

### §4.1 Files 1-5: Lane Unlock Playbooks (5 files, ≥1500 字 each)

For each lane, file name `LANE-N-<slug>-unlock-playbook-2026-05-07.md`. Required sections per file:

1. **frontmatter** (status: candidate / lane_unlock_playbook / not-authority)
2. **§1 Lane Identity**: which lane, current state, blocked since when, blocked reason
3. **§2 Why Unlock Now (or Defer)**: 实证 + product value + opportunity cost
4. **§3 Vendor Multi-Matrix** (Lane-2 必须含 BBDown + yt-dlp + 商业 API + DIY scrape; Lane-2d 必须含 Whisper + Parakeet + Voxtral + Apple Foundation Models; Lane-3 必须含 Playwright + Selenium + Puppeteer + Stagehand)
   - 每 vendor: 法律风险 / 技术成熟度 / 单 user 适配性 / 维护成本 / unlock complexity / sample code skeleton
5. **§4 4-Step Unlock Path**: spike → audit → review → unlock
   - spike: 安全实验范围 / 不动 production code / 仅 docs/research/spike/<lane>/ 写
   - audit: 3-window cloud audit (沿用 Run-2 amendment 模式)
   - review: user 显式 authorization + amendment ledger
   - unlock: 单独 dispatch + 单独 PR + amendment ledger
6. **§5 Evidence Required**: 至少 N 条 evidence 才能进入 unlock step (具体化)
7. **§6 Reverse Path**: 解禁后若发现重大问题，如何 rollback (force-disable + emergency dispatch)
8. **§7 Risk Register Excerpt**: 此 lane 5+ identified risks
9. **§8 Cross-Lane Dependencies**: 此 lane 与其它 4 lane 的依赖关系
10. **§9 Sample Spike Dispatch Skeleton**: 1 个完整的 dispatch.md 骨架（含 §1 Goal / §3 Deps / §4 allowed_paths / §8 acceptance bar）

### §4.2 File 6: `VENDOR-MULTI-MATRIX-2026-05-07.md` (≥2000 字)

跨 5 lane 的 vendor 大矩阵。每行 1 vendor / 每列:
- 适用 lane
- legal risk (low / med / high) + jurisdiction
- 技术成熟度 (mature / emerging / experimental)
- 单 user 适配性 (excellent / good / poor)
- maintenance burden (per-month hours expected)
- 单元成本 (free / per-call / subscription)
- sample code link / 文档链接
- 2 月内（2026-03-07 to 2026-05-07）vendor 状态变化

至少含 25 个 vendor 行。必含 2-month web evidence 引用（≥6 条）：
- BiliFix (vxbilibili.com) 第三方 oEmbed
- bilibili-API-collect (受 cease-and-desist)
- Apify Bilibili Scraper / Bright Data
- yt-dlp + extractor 接口
- Whisper large-v3-turbo + WhisperKit / faster-whisper / mlx-whisper / whisper.cpp
- Parakeet v3 + parakeet-mlx + FluidAudio + parakeet.cpp (March 2026 release)
- Voxtral Mini-4B Realtime (Mistral, 2026-02 release)
- Apify XiaoHongShu Scraper / Bright Data XHS / MediaCrawler
- Playwright / Selenium / Puppeteer / Stagehand
- Apple Foundation Models (on-device, March 2026 update)
- Alembic / Diesel / sqlx-migrate (Lane-4 migration tools)

### §4.3 File 7: `SPIKE-RUNBOOK-TEMPLATE-2026-05-07.md` (≥1500 字)

通用 spike methodology — 任一 lane 都能套。必含:
- spike 定义（vs production）
- spike 安全协议（不写 production / 不动 authority / 仅 docs/research/spike/<lane>/<spike-id>/ 写）
- spike 6 阶段: brainstorm → tool inventory → spike code (sandbox) → evidence collection → spike report → handoff to audit lane
- spike 失败处理: 不污染 mainline / 直接 archive 整个 spike folder
- spike → real unlock 转化条件: 至少 3 条 evidence + 1 cloud audit + user verdict

### §4.4 File 8: `AUDIT-FRAMEWORK-LANE-UNLOCK-2026-05-07.md` (≥1500 字)

如何 audit 一个 lane unlock claim。必含:
- 3-window cloud audit pattern (沿用 Run-2 amendment 模式)
- 10 audit 检查点 specific to lane unlock (e.g. did spike stay in sandbox? did vendor choice align with cease-and-desist constraint? does unlock plan include reverse path?)
- audit verdict 四级: V-PASS / V-PASS_WITH_AMENDMENTS / V-PASS_WITH_HEAVY_EDIT_REQUIRED / REJECT
- audit failure → amendment 路径 (沿用 Run-1/Run-2 amendment_and_proceed)

### §4.5 File 9: `DECISION-TREE-LANE-PRIORITY-2026-05-07.md` (≥1200 字)

5 lane 哪个先解禁? 必含:
- Mermaid decision tree (用户在哪个状态 → 推荐解哪个 lane)
- 推荐顺序的 3 种选择: (a) 价值优先 / (b) 风险最低优先 / (c) 用户特定 use case 优先
- 每分支 trade-off 分析
- 反推: "如果用户已 unlock Lane-X，下一步推荐什么"
- 必含 cross-lane synergy / conflict 分析
- 推荐 default 顺序 + 备选 2 个

### §4.6 File 10: `RISK-REGISTER-2026-05-07.md` (≥1500 字)

跨 5 lane 总 risk register。每 risk:
- ID
- lane 关联
- 严重度 (CRITICAL / HIGH / MEDIUM / LOW)
- 描述
- 触发条件
- 已知 mitigation
- contingency plan
- watch metric (如何监测 risk 是否触发)

至少 30 risks。必含特殊章节:
- "Bilibili cease-and-desist 引入的法律新风险" (≥3 risks)
- "vendor 多元化失败 risk" (≥3 risks)
- "spike 污染 production risk" (≥3 risks)
- "amendment ledger 不被遵守 risk" (≥2 risks)
- "single-user local-first 假设被破坏 risk" (≥3 risks)

### §4.7 File 11: `README-deliverable-index-2026-05-07.md` (≥600 字)

- 列全 11 文件 + 每文件字数 + claim label 占比
- 多 pass 工作流摘要
- post-cloud audit checklist (user 收到 ZIP 后该做的 5+ 件事)

---

## §5 Multi-Pass Work Plan (10 Pass, ≥90 min cumulative)

### Pass 1: 5 lane current state read (15 min)
Read overflow registry + BBDown gate matrix + ASR prestudy + DB vNext + LLM normalization. For each lane: extract current blocked reason, blocked-since when, what evidence would unblock.

### Pass 2: 4 run + 1 window-2 receipt evidence read (15 min)
For each run: identify what evidence was produced that **brings each lane closer to unlock criteria**. E.g. Run-3+4 produced topic-card-lite v0 → Lane-5 signal_workbench gets v0 anchor.

### Pass 3: 2-month web evidence integration (20 min)
Integrate ALL the following 2-month findings (cite per vendor row):
- 2026-01-28 Bilibili cease-and-desist letter to bilibili-API-collect (legal risk dimension new)
- 2026-02-04 Mistral Voxtral Mini 4B Realtime release (Apache-2.0)
- 2026-03 Parakeet C++ implementation (96x faster on Apple Silicon GPU, FluidAudio Swift SDK)
- yt-dlp 2026 status: legal in US/EU, metadata-only via `skip_download:True` safest path, CVE-2026-26331 patched
- Whisper large-v3-turbo: 6x faster than large-v3, 99 languages, MIT license
- Apple Silicon: WhisperKit + parakeet-mlx + FluidAudio CoreML+Neural Engine path
- XHS 2026 scraper landscape (no official API, residential proxy required, Apify / Bright Data / MediaCrawler)
- Apple Foundation Models on-device (March 2026 update, single-user privacy)
- BiliFix vxbilibili.com (third-party oEmbed shim)
- 2026 ontology renaissance year (Lane-5 signal workbench design input)
- AI agent fleet patterns (orchestrator-worker 80% production)
- Local-first 2026 stack (plain text + SQLite FTS + local embeddings + MCP)

### Pass 4: Vendor multi-matrix authoring (20 min)
Build the 25+ row vendor matrix (File 6). Per vendor: legal / 成熟度 / 单 user 适配 / 维护成本 / unlock complexity / sample code link.

### Pass 5: Lane-by-lane playbook authoring (30 min)
Author all 5 lane playbooks (Files 1-5). Strict schema per §4.1. Include sample spike dispatch skeleton each.

### Pass 6: Cross-cutting documents authoring (20 min)
Author Files 7 (spike runbook) + 8 (audit framework) + 9 (decision tree) + 10 (risk register).

### Pass 7: Cross-reference + consistency check (10 min)
Verify lane playbooks reference vendor matrix correctly / decision tree priority aligns with playbook risk / audit framework's 10 checkpoints maps to playbooks.

### Pass 8: Adversarial self-audit (15 min)
Find ≥10 issues in own output:
- claim label drift
- vendor matrix legal label conservative enough?
- spike runbook 是否泄露 production code 路径
- decision tree 是否暗推某 lane（违反 user neutrality）
- risk register 是否覆盖 single-user local-first 假设破坏 (≥3 risks)
- audit framework 4 verdict 等级是否完整
- cross-lane dependency 是否漏了 conflict
- single 文件不达 word target
- amendment_and_proceed pattern 是否被 cite
Document in Self-audit section of File 11.

### Pass 9: Format guard + frontmatter scan (5 min)
Run scanners per §9.

### Pass 10: README index authoring + ZIP package (10 min)
Author File 11. Package ZIP with 11 files. Generate download link.

---

## §6 Self-Audit Checklist (20 items, embed in File 11)

1. ZIP contains exactly 11 files (no more, no less)
2. Each lane playbook ≥1500 字
3. Vendor matrix ≥25 rows
4. Risk register ≥30 risks
5. Decision tree includes Mermaid diagram
6. Spike runbook includes 6-stage methodology
7. Audit framework includes 10 checkpoints
8. Each file frontmatter has `status: candidate / [type] / not-authority`
9. No file claims any lane is unlocked
10. No file claims `write_enabled=True` is acceptable in current state
11. No file claims migration is approved
12. No file claims BBDown live / yt-dlp execution / ffmpeg / ASR is unlocked
13. Lane-2 vendor matrix includes ≥3 BBDown alternatives + ≥4 ASR options + ≥2 commercial scrapers
14. Lane-3 vendor matrix includes ≥3 browser automation framework comparisons
15. Bilibili 2026-01-28 cease-and-desist explicitly cited in Lane-2 + vendor matrix
16. Apple Silicon WhisperKit + parakeet-mlx + FluidAudio path explicitly evaluated
17. Each lane has ≥1 sample spike dispatch skeleton (full §1-§8 structure)
18. Decision tree's default order has measurable rationale, not vague preference
19. Risk register includes "amendment_and_proceed pattern not respected" risk
20. Cross-lane dependencies map all 5 lanes (no isolated lane)

---

## §7 Hard Boundaries (违反任一即整 ZIP reject)

1. 不 enable any lane (此 prompt 是 author conditions, not unlock)
2. 不修任何 production code path
3. 不破 write_enabled=False invariant
4. 不绕 cease-and-desist 风险（任何 vendor 推荐必须 explicitly 评 legal risk）
5. 不假设 user 接受任何 vendor — 提供选项不指定
6. 不 silent-upgrade spike 到 production
7. 不 skip claim label
8. 不 over-promise 任何 lane unlock 时间表
9. 不引用 ScoutFlow 项目 之外的 user 私事 / persona / 个人偏好
10. 不 deliver < 11 files / < 13K cumulative words

---

## §8 Quality Criteria (per-file rubric)

Each file judged on:

| 维度 | 权重 | 评分细节 |
|---|---:|---|
| Lane / vendor coverage | 25% | 每 lane 含全 sub-lane / 每 vendor 5 维评 |
| Legal risk dimension | 20% | cease-and-desist 等近期事件 explicitly cited |
| Spike → unlock 路径清晰 | 15% | 4 步 + evidence required + reverse path |
| Cross-lane synergy / conflict | 10% | dependency map 完整 |
| Web evidence integration | 15% | ≥6 of 12 web 2-month findings used |
| Boundary preservation | 15% | no Phase 2 enable / runtime / migration leak |

---

## §9 Format Guard

- frontmatter scanner: 11 文件全 `candidate / not-authority`
- claim label scanner: 80%+ paragraphs labeled
- hard-redline scanner: no occurrence of "Phase 2 is unlocked" / "vendor X is approved" / "migration approved" outside `[tentative candidate]` future-conditional context
- vendor matrix legal column scanner: every vendor has explicit risk level + jurisdiction
- decision tree mermaid scanner: valid syntax + at least 3 branch points
- word count scanner: each file meets §4 word target

---

## §10 Stdout Output Contract

```
CLOUD U2 PHASE-2-UNLOCK COMPLETE
deliverable_url: <download link>
zip_filename: cloud-output-U2-phase-2-unlock-playbook-2026-05-07.zip
files_count: 11
total_words: <number ≥13000>
total_thinking_minutes: <number, ≥90>
multi_pass_completed: 10/10
self_audit_findings: <count of issues found by Pass 8>
critical_issues_fixed_inline: <count>
critical_issues_remaining: <count, should be 0>
lane_coverage:
  lane_1_true_vault_write: <wordcount>
  lane_2_runtime_tools: <wordcount>
  lane_3_browser_automation: <wordcount>
  lane_4_dbvnext_migration: <wordcount>
  lane_5_signal_workbench: <wordcount>
vendor_matrix_rows: <number, ≥25>
risk_register_count: <number, ≥30>
web_evidence_findings_used: <number out of 12>
boundary_preservation_check: clear / concern / reject
ready_for_user_audit: yes / no
```

---

## §11 Web Evidence (paste-time evidence layer, 必引)

When integrating these findings into your authoring, cite explicitly. Example: "[tentative candidate] 2026-01-28 Bilibili cease-and-desist (Source: SocialSisterYi/bilibili-API-collect maintainer notice) means BBDown unlock playbook must explicitly evaluate vendor diversification requirement."

### §11.1 Bilibili landscape

- 2026-01-28: SocialSisterYi/bilibili-API-collect maintainer received law-firm warning letter from Bilibili. Implication: third-party API documentation projects under legal pressure. Vendor diversification mandatory for any BBDown / metadata extraction lane.
- BiliFix (vxbilibili.com): third-party oEmbed shim. Add `vx` prefix to bilibili.com URL. Open-Graph + oEmbed + Twitter Card metadata.
- bilibili-embed (GitHub duoduoeeee): embeds video info via AV/aid. Note: under development considering possible random API changes by Bilibili itself.
- Apify Bilibili Video Search & Metadata MCP: returns BV-id, title, author, play count, like, danmaku, duration, publish date, thumbnail.
- Apify Bilibili Video Downloader: extracts direct video/audio URLs + rich metadata.
- Bright Data: scraping with web-unlocker for 412 errors.
- LangChain Bilibili integration: text transcripts via bilibili-api with sessdata/bili_jct/buvid3 cookies.
- Bilibili MCP Server (yixiaowang2001): search_videos / search_articles / get_video_info via MCP.

### §11.2 yt-dlp landscape

- Tool itself legal in US/EU/most jurisdictions.
- Metadata-only via `skip_download:True` is the safest legal path. Returns massive Python dict with all metadata fields.
- CVE-2026-26331 (April 2026, --netrc-cmd related) patched in core.
- Geo-restricted content: requires proxy/VPN.
- Bright Data Web Unlocker integration available for region-locked workflows.

### §11.3 ASR landscape (Whisper / Parakeet / Voxtral)

- Whisper large-v3-turbo: 809M params (pruned from 1.55B large-v3 by cutting decoder 32→4 layers), 6x faster than large-v3, 99+ languages, MIT license. 216x real-time on GPU.
- Whisper Apple Silicon paths: faster-whisper (CTranslate2) / WhisperKit (CoreML via Argmax) / mlx-whisper / whisper.cpp. Mature ecosystem of years.
- Parakeet v3 (NVIDIA): 600M params (less than half of large-v3), tops Open ASR Leaderboard at 1.8% WER. Apple Silicon: 80ms latency, 3-6x faster than Whisper.
- Parakeet C++ (March 2026): ~27ms encoder inference on Apple Silicon GPU, 96x faster than CPU, no Python runtime, native via Metal. Streaming Nemotron variant 80ms-1120ms.
- FluidAudio (open-source Swift SDK by FluidInference, 37 releases in 9 months): compiles Parakeet to CoreML + Neural Engine, powers VoiceInk + Spokenly.
- Voxtral Mini 4B Realtime (Mistral, 2026-02-04): Apache-2.0, 8.87GB Hugging Face download, novel causal audio encoder for true streaming, 16GB VRAM BF16 inference. Implementations: voxtral.c / Rust / MLX / ExecuTorch (mobile) / WASM+WebGPU.
- Counter-evidence: Parakeet on M4 Max consumed 22GB unified memory, pinned core, 3x slower than faster-whisper on same file (one practitioner). Whisper still safer default for 8GB MacBook Air.
- Hallucination caveat: all weakly-supervised models can predict text not actually spoken. Hybrid ASR+LLM postprocess pipeline standard for PKM transcript clean-up.

### §11.4 XHS / RedNote landscape

- No official API for international developers in 2026.
- Anti-scraping aggressive. Datacenter IPs blocked within minutes. Residential proxy + Asia-Pacific geo required.
- Per-IP rate limit: ~10-20 req/min before 412/418 errors.
- Vue.js inline window.__INITIAL_STATE__ extraction or Playwright rendering required.
- Apify XHS Scraper / Bright Data / MediaCrawler (NanmiCoder open-source).
- MCP servers: Chen Ningling v2.0 (with strategic commenting capabilities).
- RedShop e-commerce data new frontier (April 2026 launch).

### §11.5 Browser automation 2026

- Playwright dominant in production (cross-browser, async/sync).
- Selenium legacy but stable.
- Puppeteer Chrome-only.
- Stagehand (Browserbase 2026): higher-level AI-driven action framework.

### §11.6 Local-first 2026 (Lane-4 / Lane-5 design input)

- Canonical stack: plain text + SQLite FTS + local embeddings + MCP server.
- SwarmVault: local-first RAG knowledge vault example.
- Triplit / Evolu / Zero / LiveStore / Electric SQL / WatermelonDB / TanStack DB sync engine landscape.
- CRDTs for multi-device conflict-free merge.

### §11.7 Ontology / signal workbench design (Lane-5)

- 2026 ontology renaissance year. Gartner D&A Summit 2026 positioned semantic layers + knowledge graphs as foundational for agentic AI.
- Ontology defines meaning + rules; knowledge graph contains instance data.
- Agentic PKM Patterns gist (MarkBruns): auto-classification + capture pipeline + voice/multimodal + bridge/hypothesis notes + self-evolving systems.
- Eric J. Ma March 2026 blog: Obsidian + AI coding agents + structured note types reduced KM time from 30-40% to <10%.
- Supertags (Tana) / object-like tags (Capacities) as schema model for Obsidian YAML.

---

## §12 Sibling Project Cross-Reference (use as design input)

- **DiloFlow** at `/Users/wanglei/workspace/DiloFlow`: channel 看见看不见, EP01-script-v1 exists, downstream consumer of ScoutFlow. Lane-1 unlock implies ScoutFlow → DiloFlow handoff matures.
- **ContentFlow** at `/Users/wanglei/workspace/contentflow`: legacy ingest-pipeline / topic-engine / data-platform / creator-research. Reference only for Lane-5 design (don't directly couple).
- **hermes-agent** at `/Users/wanglei/workspace/hermes-agent`: orchestration sidecar with `openai` Python lib already in venv. Phase 2 LLM normalization (per t-p1a-023) could host here.

## §13 If Repo is Private (Inline Fallback Mode)

If fetch returns 404, ask user to flip public OR paste inline content of: 4 run reports + 5 lane research files + bridge code (config.py + router.py + schemas.py). Do NOT proceed without these inputs.

---

## §14 Final Mission Statement

Deliver a download link to an 11-file ZIP that gives the user a comprehensive Phase 2 Unlock Playbook covering all 5 currently-Hold lanes with vendor diversification, spike methodology, audit framework, decision tree, and risk register. The ZIP must be saturating enough that a 30-minute user audit can decide which 1-2 lanes to attempt first.

Take 90+ minutes. Use 10 passes. Adversarially audit yourself. Then deliver.

Begin Pass 1 now. Do not skip to authoring.

<<<CLOUD U2 END>>>
```

---

## Use guide

- 复制 `<<<CLOUD U2 BEGIN>>> ... <<<CLOUD U2 END>>>` 整段
- 粘到 cloud GPT Pro 深度思考窗口 2 (与 U1, U3 并行)
- 等 2-2.5h
- 收 download link → 下载到 `/tmp/strategic-upgrade-cloud-out/u2/`

## Acceptance criteria (user 后续审 ZIP 时用)

- 11 个文件全在
- 总字数 ≥ 13000
- 5 lane playbook 各 ≥ 1500 字
- vendor matrix ≥ 25 rows
- risk register ≥ 30 risks
- web 2-month 至少 6 项被 cite
- 无 Phase 2 unlock / runtime / migration / true-write 偷写
- 每 lane 含 sample spike dispatch skeleton

任一不达 → 重 paste 整段 prompt 给同窗或新窗。
