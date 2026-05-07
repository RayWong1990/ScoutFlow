---
title: ScoutFlow 采集线 Master SPEC — PR #243 Baseline Long-term North Star
status: candidate north-star
authority: not-authority
created_at: 2026-05-07
baseline_pr: 243
baseline_commit: e1deda6
baseline_lane: PF-C4-01 closed
canonical_path: docs/COLLECTION-LINE-MASTER-SPEC-2026-05-07.md
mv_from: docs/research/post-frozen/PR243-baseline-collection-line-master-spec-2026-05-07.md
purpose: 采集线全生命周期路线图 + 现在没做的全部 inventory + 11 wave routing + 4-agent v3 分工 + 算法/UX/Memory 4 视角综合
authors: cc1 (Anthropic) + integrated audit from cc0 (5 漏洞修订)
sources_synthesized:
  - 16 ZIP cloud audit (U1-U16 储能层 / 1.1M 字 / 895 file / Phase A+B 已 audit)
  - PRD-v2.1 amendment (单人 prosumer / 强视觉 capture-side)
  - SRD-v3 amendment (h5-bridge-para-vault, 5 routes 边界)
  - OpenDesign reuse strategy candidate (PR #122, §10 reject list / D5/E1/E6)
  - PF-V P0-P8 lane (PR #241, 76 file p7 wireframe)
  - PF-C4-01 lane (PR #243, 13 surface 静态壳)
  - Run-1/2 + Run-3+4 + Window-2 + ContentFlow L1 跨 5 run + 21 swap 战绩
  - 4-agent 分工 v3 (project_4_agent_division_v3.md)
  - Codex Long Runner Coder (feedback_codex_long_runner.md)
---

# ScoutFlow 采集线 Master SPEC — PR #243 Baseline 后续整体推进计划

> ## 边界声明 (必读, 防止误读)
>
> - **本文件不是 PRD-v3** — PRD canonical 仍为 `docs/PRD-v2-2026-05-04.md` + `docs/PRD-amendments/prd-v2.1-strong-visual-h5-para-pr-factory-candidate-2026-05-04.md` (promoted addendum).
> - **本文件不是 SRD-v3** — SRD canonical 仍为 `docs/SRD-v2-2026-05-04.md` + `docs/SRD-amendments/h5-bridge-para-vault-srd-v3-candidate-2026-05-04.md` (promoted addendum).
> - **本文件状态词**: `candidate north-star` (4 状态词体系: current authority / promoted addendum / candidate north-star / reference storage).
> - **不构成**: runtime approval / migration approval / frontend execution gate / authority writer / package strategy approval.
> - **构成**: PR #243 baseline 之后采集线全生命周期路线图 + 现在没做的全部 inventory + 11 wave routing + 4-agent v3 分工.
> - **更新规则**: 跨 wave 持续 reference; 当 PRD-v3 / SRD-v3 promoted 时, 本 spec §1-§9 (vision + 7 阶段 + 模块 spec + 算法层) 可吸收进 PRD-v3 / SRD-v3; §13-§18 (wave routing + governance) 演化为长期 governance manual, 不会被 PRD/SRD 吸收.
> - **入口**: `docs/00-START-HERE.md` — 新 agent / 新 session cold start ladder.

> **存档目的**: 这份 spec 是 PR #243 land 之后, 采集线**全生命周期 + 现在没做的全部 inventory** 的长期 north star reference.
> **核心论点**: 采集线 (capture → 视频→音频→文字 → 改写 → 入库 raw) 是 ScoutFlow 横切后续一切的基础, 不可跳过.
> **不是 paste-ready prompt, 是战略地图 + 模块化 spec**.

---

# §0 Why This Spec — 为什么现在写

PR #243 land 前: 采集线只有"概念 + p7 wireframe + 80-pack 部分 cluster + 16 ZIP 储能层 candidate". 未结构化, 难推进.

PR #243 land 后: 采集线**有了物理底座** — 13 surface workstation shell + tokens 三层 overlay + 15 共享组件 + L8 sync-badge 3 状态 + 4 honest TODO. 这是从"愿景"到"可派单"的转换点.

但下面这些**现在没做**, 没有 master spec 的话每个 lane 都重新发明轮子:

1. **Source adapter matrix** — B 站(BBDown) / XHS / Research / YouTube / 抖音 / 评论楼中楼 / 图文 / RSS / PDF / Image OCR — 缺统一 adapter interface
2. **Audio-to-Text pipeline** — ASR 选型 / 并行 / 后处理 / 数据库 schema 全空白
3. **Rewrite pipeline** — LLM router / 风格库 / skills 固化 / prompt 模板库 全空白
4. **Trust Trace 算法** — D3 graph / time-axis / error-path / citation chain 都是 honest TODO
5. **Capture Station UX 第二波** — 真数据接线 + 微交互 + 13 surface 状态机
6. **横切 system 模块** — Asset DAM / Agent fleet / Memory graph / Cost ledger / Skills catalog / Anti-pattern hooks / Visual brand cascade / Apple Silicon 优化 / State machine / Cross-system egress / Decision log atlas (12 子系统)
7. **U16 cross-session memory graph** — 跨 session 记忆图谱 (现 17 条 → 50-100 条 graph)
8. **Pre-flight governance** — current.md / task-index.md / decision-log.md / Hermes pre-flight 在新一轮 lane 启动前必须走

本 spec 把这 8 块系统化, 7 wave routing + 4-agent v3 分工, 让每个 lane 启动时**有真态 reference**, 不再重新发明.

---

# §1 Vision — 北极星: 单人 prosumer 操作员工作站

| 要素 | 描述 |
|---|---|
| 用户 | 1 人 (战友本人), 本地优先, 不是 SaaS |
| 价值主张 | 把"信息采集 + 转录 + 改写 + 入库 + 双链"全链路压在一个本地 H5 工作站 |
| 视觉气质 | 操作员工作站 (operator workstation), 不是 generic admin/dashboard |
| 信任层 | 来源可溯 (Trust Trace) + frontmatter 全字段 + citation chain |
| 出口 | ~/workspace/raw/00-Inbox/ 干净 Markdown → Obsidian 接管 (双链回填, 知识飞轮) |
| 性能 | Apple Silicon native (Metal MPS / VideoToolbox / CoreML / mlx) |
| 边界 | 4-layer architecture (L0 Authority / L1 Workers / L2 Thin API / L3 Console) + 5 overflow lane Hold |
| 终极闭环 | ScoutFlow 采集 → ContentFlow 生产 → DiloFlow 终点 (兄弟项目) |

---

# §2 PR #243 Baseline 真态盘点

| 维度 | 真态 |
|---|---|
| main HEAD | `e1deda6` (PF-C4-01 squash) ← `00917fe` (PF-C2) ← `b20b60a` (PF-V) |
| capture-station stack | React 18.3.1 + Vite 5.4.10 + CSS Modules + tokens.css 三层 overlay + 自写 SVG sprite |
| 13 surface | App Shell / URL Bar / Live Metadata / Capture Scope / Trust Trace / Vault Preview / Vault Commit / Topic Card Lite / Topic Card Vault / Signal Hypothesis / Capture Plan / Density Spec / Type Spec |
| 15 共享组件 | Button / TopicCard / SyncBadge / StateBadge / EvidenceTable / FrontmatterBlock / GovernanceTooltip / Icon / LifecycleStepper / LivePulse / Modal / PanelCard / PromoteGate / SurfaceFrame / TagList / UrlInput |
| token 引用 | var(--*) 375 处 (远超 ≥100 baseline) |
| 4 honest TODO | thumbnail (BBDown 阻塞) / D3 graph (W1B 待) / timeline hover (W1B 待) / error-path (W1B 待) |
| L8 sync-badge | 3 状态齐 (synced=已同步 / pending=待同步 / external-changed=外部已改) |
| 边界 | write_enabled=False / 5 overflow lane Hold / authority files 0 改 / immutable ledger 0 改 |
| 5 run 累计 | ~83 dispatch / 5 PR / 3 amend |

---

# §3 采集线 7 阶段全貌 (Capture Pipeline)

```
[Stage 1] 信号发现 (Signal Discovery)
  - URL Bar / Signal Hypothesis / Topic Card Lite / Capture Plan
  - 用户输入 URL OR 系统推荐 OR RSS 信号 OR 评论关注

[Stage 2] 元数据获取 (Metadata Fetch)
  - GET /captures/discover → metadata
  - Live Metadata / Capture Scope (生命周期 stepper)
  - 元数据: title / author / publish_at / duration / format / source_platform

[Stage 3] 内容下载 (Content Fetch) ← 5 overflow "runtime_tools" Hold
  - 视频: BBDown (B站) / yt-dlp (YouTube/Twitter/抖音) / Cobalt (跨平台)
  - 音频: 视频→音频抽取 (ffmpeg) / 直接音频 source
  - 图文: XHS adapter (Codex 成熟 skill) / 抖音图文
  - 评论 / 楼中楼: 平台 specific scraper
  - 文档: PDF / Markdown / EPUB
  - 图片: 单图 / 相册

[Stage 4] 转码处理 (Transcoding)
  - 视频→音频: ffmpeg -vn -acodec pcm_s16le -ar 16000 (Whisper 16k 输入)
  - 音频→文字: Whisper.cpp Metal / Whisper API / DeepSeek ASR / 通义/讯飞
  - 图片→文字: Tesseract / PaddleOCR / 通义 vision / Claude vision
  - PDF→文字: pdfplumber / pymupdf / Marker
  - 后处理: 标点恢复 / 说话人分离 / 语种检测 / 关键帧抽取 / pHash

[Stage 5] 内容改写 (Rewrite)
  - LLM router: Claude / GPT-4 / Gemini / DeepSeek / Qwen / 通义
  - 风格: academic / casual / technical / 翻译 / 摘要 / 双链 / Obsidian-friendly
  - prompt 模板: zero-shot / few-shot / chain-of-thought / self-refine
  - 质量评估: ROUGE / 人工抽查
  - skills 固化: 每种风格独立 skill file

[Stage 6] 信任溯源 (Trust Trace)
  - DOM 图谱: D3 self-rolled (CSS + SVG + 纯 React)
  - 时间轴 hover: 毫秒精度 + evidence focus
  - 错误路径 highlight: 路径回溯 + 视觉反馈
  - Citation chain: 跨 capture reference
  - Trust score: auto-computed

[Stage 7] 入库 raw (Vault Commit) ← 5 overflow "true_vault_write" Hold
  - ~/workspace/raw/00-Inbox/{capture_id}/{capture_id}.md
  - frontmatter: source / capture_at / source_url / sha256 / asset_ref / promotion_state / state / trust_chain
  - 子目录: transcripts/ / rewrites/ / assets/ / commentaries/
  - Obsidian 接管 (双链回填, 知识飞轮)
```

**横切 axis**: 每个 stage 都跟 **Source matrix** + **Modality** + **State machine** + **Asset lifecycle** + **Storage** + **Authority** 6 个维度交叉.

---

# §4 Source Adapter Matrix (现在没做的全部)

## §4.1 Adapter 接口规范 (统一 contract, 当前 0 实施)

```
class SourceAdapter(Protocol):
    vendor: str                         # 'bilibili' / 'xhs' / 'youtube' / ...
    cease_desist_risk: Literal["low", "medium", "high"]
    capabilities: set[Modality]         # {video, audio, image, text, comment}

    def discover(url) -> CaptureMetadata
    def fetch_video(capture_id) -> Path | None
    def fetch_audio(capture_id) -> Path | None
    def fetch_image(capture_id) -> list[Path]
    def fetch_text(capture_id) -> str
    def fetch_comments(capture_id, depth=3) -> CommentTree
    def fetch_metadata(capture_id) -> dict
```

## §4.2 Source 矩阵 (每个 source × modality)

| Source | Vendor 名 | Adapter 状态 | 视频 | 音频 | 图文 | 评论 | 楼中楼 | Cease-Desist Risk |
|---|---|---|:-:|:-:|:-:|:-:|:-:|---|
| B 站 | bilibili / BBDown | ✅ 已 PoC (live blocked) | ✅ | ✅ | ❌ | ⚠️ partial | ❌ | **HIGH** (2026-01-28 cease-and-desist 信号) |
| YouTube | yt-dlp | ❌ 未做 | ✅ | ✅ | ❌ | ✅ | ✅ | LOW |
| 抖音 | yt-dlp / DouyinDL | ❌ 未做 | ✅ | ✅ | ✅ (图文) | ✅ | ✅ | MEDIUM |
| Twitter / X | yt-dlp / snscrape | ❌ 未做 | ✅ | ❌ | ✅ | ✅ | ✅ | LOW |
| Reddit | yt-dlp / PRAW | ❌ 未做 | ✅ | ❌ | ✅ | ✅ | ✅ | LOW |
| **小红书 (XHS)** | xhs-tool (Codex 成熟 skill) | ⚠️ skill ready, integration 0 | ✅ | ❌ | ✅ (图文主) | ✅ | ✅ | MEDIUM |
| **Research (Codex)** | codex search / web | ⚠️ skill ready, integration 0 | ❌ | ❌ | ✅ | ❌ | ❌ | LOW |
| RSS | feedparser | ❌ 未做 | ❌ | ✅ podcast | ❌ | ❌ | ❌ | LOW |
| PDF | pdfplumber + Marker | ❌ 未做 | ❌ | ❌ | ✅ | ❌ | ❌ | LOW |
| Image | Tesseract + Claude vision | ❌ 未做 | ❌ | ❌ | ✅ | ❌ | ❌ | LOW |

## §4.3 Vendor diversification 策略 (源自 memory: feedback_vendor_diversification)

- BBDown 是当前 only video adapter, cease-and-desist 信号已现, **必须多元化**
- 优先级: yt-dlp (LGPL, 跨平台) > Cobalt (开源) > BBDown (备份)
- 单 source 失败时跨 vendor fallback 链

## §4.4 评论 / 楼中楼 子系统 (现在没做)

| 子模块 | 描述 | 算法 | 数据库 schema |
|---|---|---|---|
| 评论树解析 | 楼中楼递归解析 | quote tree DFS | comments(capture_id, parent_id, author, content, timestamp, like_count, depth) |
| 情感分析 | 评论情感分类 | VADER / SnowNLP / Claude classifier | comment_sentiment(comment_id, polarity, subjectivity, classifier) |
| 关键评论提取 | 高赞 / 时序 / 互动 | TextRank / LLM summarization | comment_summary(capture_id, summary_md, top_k_comment_ids) |
| 用户行为图谱 | 用户互动网络 | graph clustering | user_interaction(user_a, user_b, capture_id, interaction_type) |

---

# §5 Audio-to-Text Pipeline (战友说"还没系统设计")

## §5.1 ASR 模型选型矩阵 (现在 0 实施)

| 模型 | 部署 | 速度 (Apple Silicon) | 中文质量 | 英文质量 | 成本 | 推荐场景 |
|---|---|---|---|---|---|---|
| **Whisper.cpp Metal** | local | 1.5-3x realtime (M-series) | 良 | 优 | $0 | 默认本地 ASR |
| Whisper API | cloud | unbounded | 良 | 优 | $0.006/min | 长视频快速 |
| DeepSeek ASR | cloud | unbounded | 优 | 良 | low | 中文优先 |
| 通义千问 ASR | cloud | unbounded | 优 | 良 | low | 中文 + 多模态 |
| 讯飞 ASR | cloud | unbounded | 优 | 中 | low | 中文专精 |
| pyannote-audio | local | depends | — | — | $0 | 说话人分离 |

## §5.2 长音频分片策略 (现在 0 实施)

| 策略 | 描述 | 优势 | 劣势 |
|---|---|---|---|
| Silence-based split (pyannote VAD) | 静音检测分片 | 边界自然, 无截断 | 需要 VAD 模型 |
| Fixed-window 60-90s | 固定窗口 + overlap 5s | 简单 | 边界可能截断词 |
| Semantic boundary | LLM 语义边界 | 最自然 | 慢 + 贵 |
| Hybrid (silence + max 90s) | silence 优先, 超 90s 强切 | 平衡 | 实现稍复杂 |

**推荐**: Hybrid (silence + max 90s), pyannote VAD baseline.

## §5.3 并行架构 (现在 0 实施)

```
┌─────────────────────────────────────────────────────┐
│  CaptureID                                          │
│      ↓                                              │
│  [VAD 分片 (pyannote)]                              │
│      ↓                                              │
│  [SegmentQueue (multiprocessing.Queue)]             │
│      ↓                                              │
│  [Worker pool × N (multiprocessing, N = cpu_count)] │
│   - Each worker: Whisper.cpp Metal (per-process MPS)│
│   - Output: SegmentTranscript                       │
│      ↓                                              │
│  [Reassembler (sort by start_ts)]                   │
│      ↓                                              │
│  [Post-processor (标点 / 说话人 / 语种)]            │
│      ↓                                              │
│  TranscriptMD + frontmatter                         │
└─────────────────────────────────────────────────────┘
```

## §5.4 数据库 schema (db_vnext, 现在 0 实施)

```sql
CREATE TABLE transcripts (
    id INTEGER PRIMARY KEY,
    capture_id TEXT NOT NULL REFERENCES captures(id),
    source_audio_sha256 TEXT NOT NULL,
    asr_model TEXT NOT NULL,           -- 'whisper.cpp' / 'whisper-api' / ...
    asr_version TEXT,
    language TEXT,                     -- 'zh' / 'en' / 'mixed' / 'auto-detected'
    segments_json TEXT NOT NULL,       -- list[Segment]
    full_text TEXT NOT NULL,
    full_text_with_timestamps TEXT,    -- '[00:01:23.456] ...'
    confidence_avg REAL,
    duration_sec REAL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    promotion_state TEXT,              -- 'L1-only' / 'L2-validated' / 'L-global'
    state TEXT                         -- 'raw' / 'candidate' / 'locked' / 'deprecated'
);

CREATE TABLE transcript_segments (
    id INTEGER PRIMARY KEY,
    transcript_id INTEGER REFERENCES transcripts(id),
    start_ts_ms INTEGER NOT NULL,
    end_ts_ms INTEGER NOT NULL,
    text TEXT NOT NULL,
    speaker_id TEXT,                   -- 'speaker_1' / 'speaker_2' (pyannote)
    confidence REAL,
    has_punctuation BOOLEAN
);
```

## §5.5 后处理 chain (现在 0 实施)

| 步骤 | 输入 | 输出 | 模型 |
|---|---|---|---|
| 标点恢复 | 无标点 transcript | 有标点 | BERT-punctuator (中文) / WhisperX (英文) |
| 说话人分离 | 单声道 transcript | 多 speaker_id 标注 | pyannote-audio diarization |
| 语种自动检测 | mixed transcript | per-segment language tag | langid / fasttext-lid |
| 关键句提取 | 全文 | top-k 关键句 | TextRank / LLM |
| 章节分段 | 全文 | TOC + 锚点 | LLM segment + summarize |

## §5.6 质量评估 (现在 0 实施)

- WER baseline (per-vendor 对照人工标注 sample)
- Confidence score (per-segment) 时序图
- 抽样人工抽查 (per-week 5%)
- 跨 ASR 一致性 (多模型同输入 → 三方投票)

---

# §6 Rewrite Pipeline (战友说"还没系统设计")

## §6.1 LLM Router 架构 (现在 0 实施)

```
TaskSpec
  → router(model, style, budget)
      → Claude API ┐
      → GPT-4     ├── 多 LLM 同时跑 (A/B 模式)
      → Gemini    │
      → DeepSeek  │
      → Qwen      │
      → 通义       ┘
  → 投票 / 选优 / fallback
  → RewriteOutput
```

## §6.2 风格库 (10 候选风格, 现在 0 固化)

| 风格 | 描述 | 输出长度 | 受众 | skill 文件 (待写) |
|---|---|---|---|---|
| `academic` | 学术风, 严谨, 引用规范 | 长 | 学者 / 研究者 | `~/.claude/skills/scoutflow-rewrite-academic.md` |
| `casual` | 轻松, 口语化, emoji | 中 | 大众 | `scoutflow-rewrite-casual.md` |
| `technical` | 技术 doc 风, code block, table | 中-长 | 工程师 | `scoutflow-rewrite-technical.md` |
| `translation` | 中→英 / 英→中 | 同长 | 跨语言 | `scoutflow-rewrite-translation.md` |
| `summary` | 摘要 (TL;DR) | 短 | 信息扫描 | `scoutflow-rewrite-summary.md` |
| `outline` | 大纲提取 (H1/H2/H3) | 短 | 速览 | `scoutflow-rewrite-outline.md` |
| `obsidian-friendly` | 双链 + tags + frontmatter | 中-长 | 双链回填 | `scoutflow-rewrite-obsidian.md` |
| `annotated` | 关键点批注 + highlight | 长 | 深读 | `scoutflow-rewrite-annotated.md` |
| `qa-pair` | Q-A 抽取 | 中 | 知识库构建 | `scoutflow-rewrite-qa.md` |
| `flashcard` | 抽卡片 (Anki-friendly) | 短 | 记忆 | `scoutflow-rewrite-flashcard.md` |

## §6.3 Prompt 模板架构 (现在 0 固化)

每个风格 skill 文件 schema:

```yaml
---
name: scoutflow-rewrite-{style}
description: ScoutFlow 改写 pipeline {style} 风格 skill
input_schema:
  transcript: full_text
  metadata: { source, author, language, ... }
  user_context: { 偏好 / 已有知识 / 关注点 }
output_schema:
  rewritten_md: 改写后 Markdown (含 frontmatter)
  rationale: 风格选择 reasoning
  cost_estimate: token / wallclock
prompt_strategy:
  - zero_shot: 直接 prompt
  - few_shot: 含 3-5 example
  - chain_of_thought: 逐步推理
  - self_refine: 改写 → 自审 → 再改
quality_check:
  - rouge_against_source: 0.4-0.6 (avoid plagiarism)
  - faithfulness: claim 与 source 一致 (LLM-as-judge)
  - readability: Flesch / 中文易读度
---
```

## §6.4 数据库 schema (现在 0 实施)

```sql
CREATE TABLE rewrites (
    id INTEGER PRIMARY KEY,
    capture_id TEXT NOT NULL REFERENCES captures(id),
    transcript_id INTEGER REFERENCES transcripts(id),
    style TEXT NOT NULL,                -- 'academic' / 'casual' / ...
    llm_model TEXT NOT NULL,            -- 'claude-opus-4-7' / 'gpt-4-turbo' / ...
    llm_version TEXT,
    prompt_strategy TEXT,               -- 'zero_shot' / 'few_shot' / ...
    output_md_path TEXT NOT NULL,       -- ~/workspace/raw/rewrites/{capture_id}/{style}.md
    output_md_sha256 TEXT NOT NULL,
    cost_token_input INTEGER,
    cost_token_output INTEGER,
    cost_usd REAL,
    quality_rouge REAL,
    quality_faithfulness REAL,          -- 0-1
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    promotion_state TEXT,
    state TEXT
);
```

## §6.5 跨 LLM A/B 测试 (现在 0 实施)

- 同 input → N 个 LLM 同时跑
- 投票选最优 (LLM-as-judge: Claude 4 elder)
- 跨 LLM 一致性指标 (pairwise rouge / semantic similarity)
- 成本-质量 Pareto frontier 选模型

## §6.6 Cost / Token Budget (现在 0 实施)

- per-task token budget cap (避免单次烧钱)
- per-day total budget cap
- per-week / per-month dashboard
- attribution (per project / per lane / per agent / per style)

---

# §7 Trust Trace + Frontmatter (现在 4 honest TODO)

## §7.1 Trust Trace 4 子模块 (PR #243 全 honest TODO)

| 子模块 | Surface | 算法 | 实现路径 |
|---|---|---|---|
| **DOM 图谱** | 04 Trust Trace `data-todo="trust-trace-graph"` | D3 force-directed layout 自写 (CSS + SVG + 纯 React, 不引 npm d3) | W1B PF-C4-EXT D3 |
| **时间轴 hover** | 04 Trust Trace `data-todo="trust-trace-timeline"` | requestAnimationFrame + CSS Variables 同步 + evidence focus | W1B PF-C4-EXT timeline |
| **错误路径 highlight** | 04 Trust Trace `data-todo="trust-trace-error-path"` | 路径回溯算法 + red trace + breadcrumb | W1B PF-C4-EXT error-path (依赖 graph) |
| **Citation chain** | 跨 capture reference | graph traversal + cross-capture link | 后续 wave |

## §7.2 Frontmatter 全字段 spec (待固化)

```yaml
---
# 来源溯源
source: bilibili|xhs|youtube|...
source_url: https://...
source_id: native_id
source_platform_version: 2026.05  # 平台快照

# 时间
captured_at: 2026-05-07T15:30:00+08:00
source_published_at: 2026-05-01T...
processed_at: 2026-05-07T15:35:00+08:00

# 内容指纹
sha256_video: ...
sha256_audio: ...
sha256_transcript: ...
sha256_rewrite: ...
phash_keyframe: ...                     # 视频指纹
phash_thumbnail: ...

# Asset 引用 (不是 path 是 asset_id)
asset_ref:
  video_id: A-V-{capture_id}-001
  audio_id: A-A-{capture_id}-001
  thumbnail_id: A-T-{capture_id}-001

# 状态
state: raw|candidate|locked|deprecated|forbidden
promotion_state: L1-only|L2-validated|L-global
promotion_evidence: ""

# 信任链
trust_chain:
  - source_authority: bilibili_official  # vs ugc / mirror / aggregated
  - download_method: bbdown_v1.2.3
  - download_at: 2026-05-07T15:30:01+08:00
  - download_signature: ...
  - chain_length: 3                       # 跨多少层加工
trust_score: 0.85                        # auto-computed

# 内容元数据
title: ...
author: ...
duration_sec: ...
language: zh|en|mixed
modality: video+audio+text+image+comment
---
```

## §7.3 Trust Score 算法 (现在 0 实施)

```
trust_score = w1 * source_authority_score    # bilibili_official: 1.0, ugc: 0.5
            + w2 * (1 / chain_length)         # 越短越可信
            + w3 * sha256_verifiable          # 1 if 可校验, 0 otherwise
            + w4 * timestamp_freshness        # 越近越可信
            + w5 * citation_in_count          # 被多少其他 capture 引用 (越多越可信)
```

## §7.4 Citation Chain Visualization (现在 0 实施)

跨 capture reference graph (D3 自写):
- node = capture, edge = "引用" / "反驳" / "补充"
- L0 = 原始 source, L1 = 一手 capture, L2 = 改写, L3 = 综合
- 视觉 hierarchy: 越深层颜色越淡

---

# §8 Capture Station UX 第二波 (PF-C4-02 主菜)

## §8.1 13 surface × Bridge API mapping (修订自另一个 CC0 漏洞 2)

| Surface | Route | Method | 状态 | UX 行为 |
|---|---|---|---|---|
| URL Bar | `POST /captures/discover` | POST | ✅ existing | 输入 URL → 校验 → 历史 |
| Live Metadata | `GET /captures/{id}/metadata` | GET read-only | ✅ existing | metadata 卡片 + thumbnail TODO 占位 |
| Capture Scope | `GET /captures/{id}/scope` | GET read-only | ✅ existing | 生命周期 stepper 实时同步 |
| Trust Trace | `GET /captures/{id}/trust-trace` | GET read-only | ✅ existing (DTO 锁定) | DOM 图谱 + 时间轴 + error-path (W1B 后实施) |
| Vault Preview | `GET /captures/{id}/vault-preview` | GET read-only | ✅ existing (新加 PR #205) | frontmatter + Markdown 预览 |
| **Vault Commit** | `POST /captures/{id}/vault-commit` | POST | 🚫 **future-gated, MUST NOT RUN** | UI disabled state + write_disabled badge |
| **Transcribe** | `POST /captures/{id}/transcribe` | POST | 🚫 **blocked until Wave 6 unlock** | UI "blocked" badge + 等待解禁说明 |
| Topic Card Lite | `GET /topic-cards/{id}` | GET read-only | 待实施 | 新闻/视频/对比三态 |
| Topic Card Vault | `GET /topic-cards?promote_state=L2` | GET read-only | 待实施 | 聚合 + L8 sync-badge 3 状态 |
| Signal/Hypothesis | `GET /signals` + `GET /hypotheses` | GET read-only | 待实施 | 展开/对比/生命周期 |
| Capture Plan | `GET /captures/plan/{plan_id}` | GET read-only | 待实施 | I/O 字段 + 干跑日志 |
| Density Spec | static (V3 reference) | — | 静态 | overlay 验证 |
| Type Spec | static (V4 reference) | — | 静态 | overlay 验证 |

**硬约束 (来自 SRD-amendments + current.md)**:
- Trust Trace DTO 字段 + shape 锁定, 通宵 lane 不许改
- Vault Commit + Transcribe 必须保持 disabled UI state, **commander prompt 明文锁**

## §8.2 状态机 UX (PF-C4-02 主体, 现在 0 实施)

每个 surface 的 4 状态:

| 状态 | UI | API 状态 | 持续时间 |
|---|---|---|---|
| **Loading** | skeleton (差异化, 不是统一) / spinner / progress bar | API in-flight | <500ms 或长 |
| **Empty** | 引导 + 空白 | 200 OK + 空 result | 持续 |
| **Error** | toast (transient) / inline (modal-less) / modal (severe) | 4xx / 5xx / network | 直到 dismiss |
| **Success** | 微动画 + 状态切换 | 200 OK + 数据 | 持续 |

## §8.3 微交互动画 vocabulary (现在 0 实施)

**硬约束 (来自 PRD-v2.1 + 另一个 CC0 漏洞 5)**: motion **仅 capture-side**, 不渗透 wiki/reading surface (现在 ScoutFlow 还没 wiki surface, spec 显式声明仍然必要 prevent rule 入 contract).

| 微交互 | 触发 | CSS Variables | 时长 |
|---|---|---|---|
| state transition | sync-badge 3 状态切换 | `--anim-duration-fast` 200ms | 200ms |
| progress feedback | 长 task 进度 | `--anim-duration-medium` 400ms | continuous |
| hover affordance | button / card hover | `--anim-duration-fast` 150ms | hover 持续 |
| loading skeleton | API in-flight | `--anim-duration-shimmer` 1500ms | until ready |
| focus highlight | keyboard focus | `--anim-duration-instant` 100ms | focus 持续 |
| error shake | 校验失败 | `--anim-duration-shake` 300ms | once |

**严禁**: third-party motion lib (framer-motion / react-spring / lottie 等) — 全 CSS Variables-only.

## §8.4 L8 sync-badge 全 surface 推广 (现在仅 TopicCardVault)

PR #243 仅 TopicCardVault 用 sync-badge. PF-C4-02 推广到:
- Topic Card Lite (单卡片 sync 状态)
- Vault Preview (preview 是否最新)
- Capture Plan (plan execution 状态)
- Signal/Hypothesis (是否同步到 vault)

**3 状态契约不变**: synced / pending / external-changed.

## §8.5 Capture state machine 6 状态 (U7 state-library 素材)

```
discovered → downloading → transcoding → rewritten → trusted → committed
   ↓             ↓              ↓             ↓           ↓          ↓
 [URL Bar]  [Capture Scope]  [Trust Trace] [Vault Preview] [Vault Commit]
```

每个状态:
- 视觉 hierarchy: 进度条 + 状态 badge + transition animation
- 错误恢复路径 visible (可重试 / 可放弃 / 可 escalate)
- Capture 可同时多个 (multi-capture 视图)

---

# §9 横切 system 模块 (12 子系统, 现在 0 系统化)

## §9.1 Asset DAM (Digital Asset Management, U6 retrieval-dam 素材)

| 子模块 | 描述 | 数据库 schema | 状态 |
|---|---|---|---|
| Asset registry | 全 asset 索引 (video/audio/image/transcript/rewrite) | `assets(id, type, sha256, phash, capture_id, path, state, promotion_state)` | 0 |
| Thumbnail 生成 | smart crop + focus point | — | 0 |
| pHash de-dup | 跨 capture 视觉 de-dup | `asset_phash_index(phash, asset_ids)` | 0 |
| Asset promote gate | L1 → L2 → L-global | promotion_state field + evidence | 0 |
| 视觉 search | CLIP-based "find similar" | CLIP embedding index | 0 |

## §9.2 Agent Fleet Dispatch Ledger (U5 素材)

```sql
CREATE TABLE agent_fleet_dispatch_ledger (
    id INTEGER PRIMARY KEY,
    dispatch_id TEXT UNIQUE,
    lane TEXT NOT NULL,                  -- 'PF-C4-02' / 'PF-C4-EXT' / ...
    agent TEXT NOT NULL,                 -- 'codex' / 'gpt-pro' / 'cc1' / 'hermes'
    started_at TIMESTAMP,
    completed_at TIMESTAMP,
    status TEXT,                         -- 'pending' / 'running' / 'success' / 'failed' / 'amended'
    receipt_path TEXT,
    cost_tokens_input INTEGER,
    cost_tokens_output INTEGER,
    cost_usd REAL,
    amend_trail_count INTEGER DEFAULT 0,
    introduced_or_exposed TEXT           -- §1.8 metacognition rule
);
```

跨 lane view: 全 dispatch 历史 / amend trail / cost attribution.

## §9.3 Memory Graph (U16 素材, 现状 17 → 50-100 升级)

详见 §13.

## §9.4 Cost / Budget Ledger (新增, 战友单人 prosumer 没 explicit 设计)

```sql
CREATE TABLE cost_ledger (
    id INTEGER PRIMARY KEY,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    project TEXT,                        -- 'scoutflow' / 'contentflow' / ...
    lane TEXT,
    agent TEXT,
    operation TEXT,                      -- 'asr' / 'rewrite-{style}' / 'dispatch' / ...
    capture_id TEXT,
    cost_usd REAL,
    cost_tokens INTEGER,
    notes TEXT
);
```

UI dashboard: per-day / per-week / per-month / per-project / per-agent.

## §9.5 Skills / Tools / MCP Catalog (U12 素材)

跨项目 skill 复用注册表:
- skill_registry: { name, project, location, last_updated, dependencies }
- tool_registry: { name, vendor, type=cli|mcp|sdk, install_status }
- MCP server registry: firecrawl / github / supabase / context7 / playwright / sequential-thinking
- Plugin catalog: everything-claude-code / superpowers / token-optimizer / dx

战友手动维护 vs 自动 discovery.

## §9.6 Anti-pattern Defense (U11 素材)

| 防御层 | 实施 | 状态 |
|---|---|---|
| Pre-commit hook | husky / pre-commit 检查 (shadcn/Tailwind/hex/generic admin) | 0 |
| `~/.claude/rules/anti-patterns.md` | 全集汇总 | 部分 |
| Runtime checker | production guard (生产期检测违规导入) | 0 |
| 跨 lane catalog | 历史 anti-pattern 库 + introduced vs exposed 归因 | 部分 (memory) |

## §9.7 Visual Brand Atlas Cascade (U13 素材)

| 层 | 内容 | 当前状态 |
|---|---|---|
| Token (15 色 + 字体 + 间距 + 圆角 + 阴影) | tokens.css | ✅ PR #243 |
| Density overlay (V3 紧凑) | density-compact.css | ✅ PR #243 |
| Type-weight overlay (V4 高字重) | type-weight-heavy.css | ✅ PR #243 |
| Reduced-density mode | TBD css | 0 |
| Reduced-motion mode | TBD css + media query | 0 |
| High-contrast mode (a11y AAA) | TBD css | 0 |
| Component vocabulary (跨项目共享) | shared lib | 0 |
| Motion vocabulary | CSS Variables-only motion lib | 0 (W2C 实施) |
| 8 panel × 3 density × 2 type-weight 组合验证 | spec 文档 | 0 |
| 30 icon (system 10 + state 10 + 待加 10: capture/vault/asset/agent/signal/hypothesis/trust/cost/sync/overlay) | sprite 扩充 | ⚠️ 20 (state.svg + system.svg 各 10) |

## §9.8 Apple Silicon 优化 (U14 素材)

| 优化项 | 描述 | Speed up | 状态 |
|---|---|---|---|
| Whisper.cpp Metal | Metal MPS GPU 加速 | 3x vs CPU | 0 (W4F) |
| ffmpeg VideoToolbox | 硬件 encode/decode | 5-10x | 0 |
| CoreML 模型转换 | PyTorch → CoreML 部署 | 2-5x | 0 |
| Pillow-SIMD ARM64 | 图像处理 SIMD | 4-6x | 0 |
| OpenCV ARM64 | 图像 / 视频 native | 2-3x | 0 |
| mlx (Apple ML framework) | Apple-native ML | varies | 0 |
| asyncio + multiprocessing | 多核并发 | N cores | 部分 |

## §9.9 State Machine Library (U7 素材)

| State machine | 状态数 | 跨 surface 同步 | 实施状态 |
|---|---|---|---|
| Capture lifecycle | 6 (discovered → committed) | yes | 0 |
| Asset lifecycle | 5 (raw → forbidden) | yes | 0 (frontmatter only) |
| Topic card lifecycle | 3 (pending → committed → external-changed) | yes (L8 sync-badge) | ✅ PR #243 |
| Dispatch lifecycle | 5 (pending → success / failed / amended) | yes | 0 |
| Promotion state | 3 (L1-only → L2-validated → L-global) | yes | partial (frontmatter) |

## §9.10 Cross-System Egress (U8 素材)

| 出口 | Manifest | Contract | 状态 |
|---|---|---|---|
| → Obsidian | `~/workspace/raw/00-Inbox/{capture_id}/{capture_id}.md` + frontmatter | Markdown only, 双链回填 由 Obsidian 接管 | partial |
| → ContentFlow | TBD | 内容生产闭环 | 0 |
| → DiloFlow | TBD | 兄弟项目终点 | 0 |
| → External backup | TBD | sha256 校验 + offsite | 0 |

## §9.11 Decision Log Atlas (U15 素材)

- 240+ PR decision log
- Per-decision rationale + reverse chronology
- Cross-decision impact graph
- Decision review cycle (quarterly)

## §9.12 Prosumer SOP Runbook (U10 素材)

- 单人 prosumer 操作 SOP (per-task type)
- 跨 session 复用
- 失败 / amend / retry pattern catalog
- 跨项目 SOP 共享

## §9.13 16 U → § 9.x 子模块对应表 (CC1 retrospective sediment, 2026-05-07)

> 解决 "可见性断层" — 16 ZIP 储能层跟 § 9.x 子模块 12/16 1:1 映射, 之前没显式标. 新 agent 起手凭此表立刻知道 U → wave 桥 (元认知 instinct §3 第 14 条).

| U | 主题 | § 9.x 对应 | 消费 wave |
|---|---|---|---|
| U6-retrieval-dam | Asset DAM | § 9.1 | W2C 后续 / W6J |
| U5-agent-fleet | Agent Fleet Dispatch Ledger | § 9.2 | W3E 80packs |
| U16-memory-graph | Memory Graph (现状 17 → 50-100) | § 9.3 | W2D / W6K |
| U12-tools-catalog | Skills/Tools/MCP Catalog | § 9.5 | W6K |
| U11-anti-pattern | Anti-pattern Defense | § 9.6 | pre-commit hook + ~/.claude/rules/anti-patterns.md |
| U13-visual-brand | Visual Brand Atlas Cascade | § 9.7 | W2C 主菜视觉 input |
| U14-apple-silicon | Apple Silicon 优化 | § 9.8 | W4F (Phase 2 ASR 解禁后) |
| U7-state-library | State Machine Library | § 9.9 | W2C state machine |
| U8-egress | Cross-System Egress | § 9.10 | W2C 输出 contract / 跨项目 |
| U15-decision-log | Decision Log Atlas | § 9.11 | ~/.claude/skills/ScoutFlow-pr-decisions |
| U10-runbook | Prosumer SOP Runbook | § 9.12 | ~/.claude/skills/ScoutFlow-runbooks |

**Gap (4 U 没显式 § 9.x 对应)**:

| U | 主题 | 真路线 |
|---|---|---|
| U1-deep | PRD-v3/SRD-v3 supplement + NFR | § 19.2 / 升 PRD-v3 candidate shell |
| U2-deep | 5 Lane spike + vendor matrix + fail-mode | § 4-§ 6 / W4F+W4G+W5H spec 输入 |
| U3-deep | 4 entity v0→v1 + RI test + OpenAPI | § 5.4 / W4F (Lane-4 dbvnext) |
| U4-visual-asset | Visual asset DDL + CRUD | § 9.x gap, 待补 (W2C 后续 services/api/scoutflow_api/visual/) |

---

# §10 算法工程师视角 — Implementation 细节 inventory (现在没做)

## §10.1 视频处理算法层

| 算法 | 库 / 工具 | 用途 | 状态 |
|---|---|---|---|
| 关键帧抽取 | PySceneDetect | thumbnail 生成 | 0 |
| 视频指纹 | videohash / pHash | 跨 capture de-dup | 0 |
| Subtitle 提取 | ffmpeg + 自动 OCR | 已有字幕直接用 | 0 |
| Chapter 检测 | YouTube chapter / 视觉切换 | 自动分章 | 0 |
| 视频质量评估 | VMAF / SSIM | 下载质量校验 | 0 |

## §10.2 音频处理算法层

| 算法 | 库 / 工具 | 用途 | 状态 |
|---|---|---|---|
| VAD 静音检测 | pyannote-audio / silero-vad | 长音频分片 | 0 |
| Speaker diarization | pyannote-audio | 多说话人分离 | 0 |
| 标点恢复 | BERT-punctuator | transcript 后处理 | 0 |
| 语种检测 | langid / fasttext-lid | 自动语言标注 | 0 |
| 音频指纹 | acoustid / chromaprint | 跨 capture 音频 de-dup | 0 |
| 音频降噪 | RNNoise | 提升 ASR 质量 | 0 |

## §10.3 文本算法层

| 算法 | 库 / 工具 | 用途 | 状态 |
|---|---|---|---|
| NER (命名实体识别) | spaCy / HanLP / Claude | 信号提取 | 0 |
| Topic modeling | LDA / BERTopic | 主题聚类 | 0 |
| Embedding | sentence-transformers / OpenAI ada | 语义 search | 0 |
| Chunking | RecursiveCharacterTextSplitter | 长文本分片 | 0 |
| ROUGE / BLEU | nltk / rouge-score | 改写质量评估 | 0 |
| Readability | textstat / 中文易读度 | 风格评估 | 0 |

## §10.4 图片算法层

| 算法 | 库 / 工具 | 用途 | 状态 |
|---|---|---|---|
| OCR | Tesseract / PaddleOCR / 通义 vision | 图文提取 | 0 |
| 图片描述 | BLIP-2 / Qwen-VL / Claude vision | 自动 caption | 0 |
| Smart crop | focus point detection | thumbnail 生成 | 0 |
| pHash | imagehash | de-dup | 0 |
| CLIP embedding | transformers | 视觉 search | 0 |

## §10.5 评论算法层 (已在 §4.4)

## §10.6 信号 / 假设 / topic_card 算法层

| 算法 | 描述 | 状态 |
|---|---|---|
| 信号提取 | NER + topic + LLM extraction | 0 |
| 假设生成 | LLM + template | 0 |
| topic_card 聚合 | DBSCAN / K-means / agglomerative | 0 |
| 跨 capture 关联 | similarity / co-occurrence graph | 0 |
| topic_card promote gate | L1 → L2 → L-global | 0 |

## §10.7 Trust Trace 算法层 (在 §7)

## §10.8 数据库算法层

| 算法 | 描述 | 状态 |
|---|---|---|
| Index strategy | sha256 / phash / created_at / state 全索引 | 0 |
| Migration plan | v0 → v1 (db_vnext) | Hold lane |
| Backup / snapshot | per-day SQLite snapshot + sha256 | 0 |
| Vacuum / optimize | per-week | 0 |
| Cross-capture join performance | 优化 trust_chain query | 0 |

---

# §11 UX 设计师视角 — 操作员气质细节 inventory (现在没做)

## §11.1 信息密度 ladder (U13 type-weight-heavy 素材)

| 层 | 字号 | 字重 | 用途 |
|---|---|---|---|
| Display (XL) | 36-48px | 700 | 仪表盘大数 |
| H1 | 28-32px | 600 | 页面主标题 |
| H2 | 22-24px | 600 | 段落标题 |
| H3 | 18-20px | 500 | 子段落 |
| Body | 14-16px | 400 | 正文 |
| Caption | 12-13px | 400 | 注释 / metadata |
| Code | 13-14px | 400 (mono) | code block / inline code |
| Numeric tabular | mono + tabular-nums | — | cost / SHA / timestamp |

CJK + Latin baseline 锚定: CJK 主导, 英文 follow CJK baseline.

## §11.2 Color system 操作员气质 (U13 token cascade)

15 token 完整集 (PR #243 已 implement):
- Background 3 层: canvas / surface / elevated
- Foreground 3 层: primary / secondary / tertiary
- 状态 5: success / warning / error / info / neutral
- Focus / border / shadow / accent

待加 mode:
- Reduced-density mode (compact V3)
- Reduced-motion mode (accessibility)
- High-contrast mode (a11y AAA)
- Light mode (战友默认 dark, light optional)

## §11.3 Keyboard shortcut 全局 (现在 0)

| 快捷键 | 动作 | 范围 |
|---|---|---|
| `J / K` | next/prev surface (sidebar nav) | global |
| `Cmd+K` | command palette (open / capture / search) | global |
| `Cmd+/` | search | global |
| `Cmd+Shift+P` | dispatch agent | global |
| `1-9` | 直接跳第 N 个 surface | global |
| `Esc` | close modal / cancel | modal-context |
| `Cmd+Enter` | confirm / submit | form-context |

## §11.4 Layout system (现在简单 sidebar)

| Layout 元素 | 现状 | PF-C4-02 升级 |
|---|---|---|
| Sidebar | 固定列表 | dock-style: collapsible / hover preview / drag reorder |
| Header | 无 | sticky header: capture id / state / action menu |
| Main panel | 单 surface | split-pane: surface + side context (e.g. trust trace 同时展示) |
| Status bar | 无 | bottom: connection / vault state / agent fleet status / cost today |
| Modal | static | layered: backdrop / panel / nested |
| Toast | 无 | transient stack |

## §11.5 Onboarding / Help-in-context (现在 0)

| Element | 描述 | 状态 |
|---|---|---|
| First-run tutorial | 5-step guide (paste URL → wait → preview → commit (disabled) → vault) | 0 |
| Empty vault guidance | 示例 capture 演示 | 0 |
| Tooltip | hover 微提示 | partial (GovernanceTooltip 组件已有) |
| Overlay help | Cmd+? 全屏 overlay | 0 |
| Cheatsheet | keyboard shortcut 速查 | 0 |

## §11.6 Cost / Time UX (现在 0)

| Element | 描述 |
|---|---|
| Per-capture cost ribbon | 每个 capture 显示 LLM + ASR + storage 总 cost |
| Daily / weekly / monthly cost dashboard | 折线图 + per-LLM 分饼 |
| Budget cap warning | 接近 cap 时 warning, 超 cap block 高 cost 操作 |
| Wallclock estimate | 长 task 预估剩余时间 |

## §11.7 Agent Fleet UX (U5 素材)

| Element | 描述 |
|---|---|
| Active dispatch panel | 实时显示当前 dispatch 进度 + agent + ETA |
| Wait queue | 排队 dispatch 列表 |
| History | 历史 dispatch + receipt + amend trail |
| Per-agent ledger | per-agent cost / 次数 / 成功率 |
| Cross-lane view | 跨 lane 横切 (lane × agent matrix) |

## §11.8 Stale data indicator (现在 0)

每个 surface:
- last_sync_at timestamp visible
- staleness >5min → 颜色变浅 + "outdated" badge
- Manual refresh button

## §11.9 Capture Detail Drawer (现在 0)

点 capture 任意位置 → 右侧 drawer:
- 全 metadata
- Trust trace 缩略
- 全 transcript / rewrite versions
- Asset thumbnail grid
- Comments preview
- Quick action: re-fetch / re-transcribe / re-rewrite / commit (disabled)

## §11.10 Multi-capture View (现在 0)

| View | 描述 |
|---|---|
| Grid | thumbnail × 4-column |
| List | 紧凑表格 (capture_id / title / state / time) |
| Timeline | 时序 (横轴时间, 竖轴 capture) |
| Graph | 跨 capture trust 图谱 (citation chain) |

---

# §12 U16 Cross-Session Memory Graph (现在 17 条 → 升级 50-100 条 graph)

## §12.1 Memory graph schema (现在 0 实施)

| Graph | Node | Edge | Source |
|---|---|---|---|
| Decision graph | decision (D-XXX) | depends_on / supersedes / amends | decision-log.md |
| Runbook graph | runbook | precedes / depends_on | U10 prosumer SOP runbook |
| Anti-pattern graph | anti-pattern | catches / triggered-by | U11 anti-pattern encyclopedia |
| PR-history graph | PR | introduced / exposed / amends / supersedes | git log + closeout |
| Skill graph | skill | composes / depends_on | U12 tools catalog |

## §12.2 Memory ingest pipeline (现在 0 实施)

```
SessionEnd → 自动从 (handoff + retrospective + closeout) 提取 condensed memory
          → de-dup (semantic similarity vs existing memory)
          → 写 ~/.claude/projects/.../memory/{type}_{topic}.md
          → 更新 MEMORY.md index
SessionStart → 自动注入相关 memory (按 topic / lane / time 排序)
```

## §12.3 Memory query interface (现在 0)

| Query | 描述 |
|---|---|
| `query(topic="visual", limit=5)` | 按 topic 取 |
| `query(lane="PF-C4")` | 按 lane 取 |
| `query(agent="codex", since="2026-04")` | 按 agent + 时序 |
| `semantic("vendor lock-in")` | embedding-based |
| `graph_traverse(start="D-001", depth=2)` | 图遍历 |

## §12.4 ScoutFlow memory 升级路线 (现在 17 → 目标 50-100)

| 升级项 | 来源 | 数量 |
|---|---|---|
| 5 run + 协作模式 沉淀 | Run-1/2/3+4 + Window-2 + ContentFlow L1 | +10 |
| 16 ZIP audit insights | U1-U16 audit findings | +20 |
| Anti-pattern catalog | U11 + 历史 amend | +10 |
| 决策时序 (D-XXX) | decision-log.md | +20 |
| Operator workstation 视觉规范 | U13 + 战友审美红线 | +5 |
| 跨项目 skill 复用 | U12 | +10 |

总目标: 50-100 条 condensed memory + cross-link graph.

## §12.5 跟 ScoutFlow project 当前 memory 衔接

现 17 条:
- user_multi_agent / project_shape / probe_remediation
- vendor_diversification / sidecar_writeback / pre_diagnose_git_fetch
- external_facts_authority / gh_delete_branch / github_pr_auto_retarget
- stacked_pr_worktree / wave3_refdocs / working_pacing
- tone_comrade / gpt_pro_heavy_producer / 4_agent_division_v3 / codex_long_runner / prompt_design_principles

升级后目标增加:
- 5 run 战绩 (Run-1/2/3+4) condensed
- 16 ZIP audit findings condensed
- Anti-pattern catalog (10+)
- 决策时序 (D-XXX cross-reference)
- 操作员气质审美红线 (capture-side motion / 不引 vendored shadcn)

---

# §13 7 Wave Routing + 4-agent v3 分工 (集成另一个 CC0 5 漏洞修订)

## §13.1 Wave 列表 (按战略 × ROI × 视觉强化排序)

| # | Wave | 主体 | 阻塞 | 时间 | 视觉强化 | 战略 |
|---|---|---|---|---|---|---|
| **W1A** | untracked batch land (含 16 ZIP 储能层 Tier 1+2 落 main, Tier 3 archive) | git + commit + 单 PR squash | 无 | 30-45 min | — | ⭐⭐ |
| **W1B** | PF-C4-EXT 3 TODO 实施 (D3 graph + timeline + error-path 自写) | 升级 OpenDesign reuse strategy v2 + Codex 通宵 | OpenDesign v2 | 升级 1.5h + Codex 5-7h | ⭐⭐⭐ | ⭐⭐ |
| **W2C** | PF-C4-02 真数据接线 + 微交互 (Stage 2-6 read-only) | GPT Pro spec + Codex 通宵 + V-PASS | dispatch 注册 + Hermes pre-flight | spec 30min + Codex 5-7h + V-PASS 1h | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ |
| **W2D** | U16 memory ingest (50-100 条) | sniff U16 + 提取 + 写 memory | 无 | 60-90 min | — | ⭐⭐⭐ |
| **W3E** | 80-pack 余量 cluster (PF-C0 / O1 / C3 等) | U9 dispatch-catalog + Codex multi-PR | 无 (各 cluster 独立) | 多日 (单 cluster 一夜) | ⭐⭐ | ⭐⭐⭐⭐ |
| **W4F** | Phase 2 LANE-2 ASR spike (Whisper.cpp + benchmark) | runtime_tools 解禁 + true_vault_write 解禁 + OpenDesign v2 | 多个 authority 升级 PR | 多日 | — | ⭐⭐⭐⭐⭐ |
| **W4G** | Phase 2 LANE-3 Rewrite spike (LLM router + 10 风格 skill) | 配套 LANE-2 (ASR 输出) | LANE-2 transcript ready | 多日 | — | ⭐⭐⭐⭐⭐ |
| **W5H** | Source matrix 扩展 (yt-dlp / XHS / 抖音 / Research) | adapter interface 统一 + per-source PoC | runtime_tools 解禁 | 多日 (per-source 一夜) | — | ⭐⭐⭐⭐ |
| **W5I** | 评论 / 楼中楼 子系统 | 评论树 + 情感 + 关键评论 | 配套 W5H | 多日 | — | ⭐⭐⭐ |
| **W6J** | Vault commit 真解禁 | true_vault_write 解禁 + 完整 frontmatter contract | 多个 authority + 7 阶段 pipeline 全通 | 多周 | — | ⭐⭐⭐⭐⭐ (终极闭环) |
| **W6K** | Memory + 协作模式沉淀 (5G) | 长期资产 | 无 | 任何 session 间隙 | — | ⭐⭐ |

## §13.2 4-agent v3 分工矩阵 (cross 11 wave)

| Wave | GPT Pro | Codex | CC1 (我) | Hermes | 战友 |
|---|---|---|---|---|---|
| **W1A** | — | — | ⭐ 主: classify Tier 1/2/3 + git + PR + merge | — | 拍板 + 看 PR diff |
| **W1B** | spec: D3 选型 (一次性 24min) | ⭐ 通宵实施 3 dispatch | ⭐ 写 OpenDesign v2 + 派单 + audit | ⭐ external audit (D5/§10) | V-PASS + 拍板 |
| **W2C** | ⭐ spec one-shot: bridge contract + 真接线 schema + motion vocab | ⭐ 通宵实施 ~15 dispatch | ⭐ dispatch 注册 + commander prompt + audit | ⭐ pre-flight external audit | V-PASS + 拍板 |
| **W2D** | — | — | ⭐ 主: U16 sniff + 提取 + 写 memory | — | 看 diff + 拍板 |
| **W3E** | spec: 跨 cluster handoff (PF-V P8 模式) | ⭐ 通宵 multi-PR | ⭐ U9 选 cluster + 优先级 + commander prompt | external audit (跨 cluster 一致性) | 拍板 cluster |
| **W4F** | ⭐ spec: U2-deep + U14 综合 + ASR runbook | ⭐ Whisper.cpp 真 install + benchmark | ⭐ 派单 + 边界 + 升级 PR | ⭐ external audit (解禁 risk) | ⭐ 拍板解禁 |
| **W4G** | ⭐ spec: 10 风格 prompt + LLM router | ⭐ LLM router 实施 + 10 skill 写 | ⭐ 派单 + audit + skill catalog | external audit (LLM router 一致性) | V-PASS |
| **W5H** | spec: per-source adapter contract | ⭐ adapter 实施 (per-source 一夜) | ⭐ adapter interface 统一 + 派单 | external audit (vendor 多元化 + cease-desist) | 拍板 source 优先级 |
| **W5I** | spec: 评论树 + 情感 schema | ⭐ 实施 | ⭐ 派单 | — | V-PASS |
| **W6J** | ⭐ spec: vault commit 完整 contract + frontmatter | ⭐ vault commit 真实施 | ⭐ 派单 + 边界 + 升级 PR | ⭐ external audit (true_vault_write 解禁) | ⭐ 拍板解禁 |
| **W6K** | — | — | ⭐ 主: 写 memory + 沉淀 | external audit (memory 准确度) | 看 + 拍板 |

## §13.3 集成另一个 CC0 5 漏洞修订

| 漏洞 | 修订 | 落地位置 |
|---|---|---|
| 1. W2C 启动需 dispatch 注册 | 不直接 paste, 先 task-index.md + decision-log.md + Hermes pre-flight | W2C §13.2 / §14 governance |
| 2. surface-to-route mapping 显式列 | 6 routes 表锁定, vault-commit + transcribe 必须 disabled UI | §8.1 表 |
| 3. Trust Trace DTO 不得改 | commander prompt 明文锁字段名 + shape | §8.1 + W2C commander prompt 写时锁 |
| 4. 16 ZIP batch land 分类 | Tier 1+2 → main, Tier 3 archive | W1A § |
| 5. capture-side motion 边界 | spec 显式声明 motion 仅 capture-side, 不渗透 wiki | §8.3 |

---

# §14 Pre-flight Governance (现在 0 系统化)

## §14.1 ScoutFlow 治理硬规则 (来自 docs/current.md)

```
"code-bearing migration / runtime / worker / frontend 启动都必须新 dispatch + 外审"
"不创建或修改 workers/、packages/; apps/、services/ 仅当前 dispatch 明确授权路径时可动"
"Active product lane 0/3, Authority writer 0/1"
"PlatformResult enum / WorkerReceipt schema / Trust Trace DTO 未经新 dispatch + 外审不得改动"
```

## §14.2 每个 wave 启动前必走 5 步

1. **task-index.md** Active row 注册 (Active 1/3 → 2/3 → 3/3, max=3)
2. **decision-log.md** D-XXX entry (Authority writer 1/1, 单写)
3. **Hermes pre-flight external audit** (不是 post-flight, 是 pre-flight)
4. **commander prompt v1** 由 CC1 写 (基于 GPT Pro spec one-shot)
5. **paste 给 Codex 通宵实施**

## §14.3 Pre-flight 不通过的处置

- task-index 已满 → wait or 关闭一个 Active lane 再启动
- decision-log 单写冲突 → 串行, 不并行
- Hermes V-REJECT → 修 spec 再 pre-flight, 不直接派 Codex

## §14.4 Post-flight (V-PASS 阶段)

每个 wave 完成后:
- CC1 audit (sniff + spot + cross-link)
- 战友 V-PASS (浏览器审 + 5 Gate)
- 路径 1 merge / 路径 2 amend / 路径 3 root cause
- 写 closeout receipt (类似 PF-C4-01-v-pass-merged-2026-05-07.md)

---

# §15 真态依赖图 + 优先级排序

## §15.1 依赖图

```
[W1A untracked batch] ─── 不阻塞 ─────────────────────────────────────────┐
[W2D U16 memory ingest] ─ 不阻塞 ─────────────────────────────────────────┤
[W2C PF-C4-02] ←── 先走 dispatch 注册 + Hermes pre-flight (修订) ────────┤
[W1B PF-C4-EXT]                                                          │
   │                                                                     │
   └── 依赖 ──→ [OpenDesign reuse strategy v2 升级 PR] ──────────────────┤
                                                                         ├── main
[W3E 80-pack 余量] ──── 不阻塞 (各 cluster 独立) ─────────────────────────┤
                                                                         │
[W4F Phase 2 ASR]                                                        │
   ├── 依赖 ──→ [runtime_tools authority 升级]                            │
   └── 依赖 ──→ [部分 true_vault_write 升级]                              │
                                                                         │
[W4G Phase 2 Rewrite] ── 依赖 ──→ [W4F transcript ready] ────────────────┤
                                                                         │
[W5H Source matrix 扩展] ── 依赖 ──→ [runtime_tools 升级] ────────────────┤
                                                                         │
[W5I 评论 / 楼中楼] ── 依赖 ──→ [W5H source adapter 落 main] ────────────┤
                                                                         │
[W6J Vault commit 解禁]                                                  │
   ├── 依赖 ──→ [W4F + W4G + W5H 全 ready]                                │
   └── 依赖 ──→ [true_vault_write authority 升级]                         │
                                                                         │
[W6K Memory 沉淀] ── 不阻塞 ─────────────────────────────────────────────┘
```

## §15.2 优先级 (战友拍板视角)

**P0 (今晚必跑, 0 阻塞)**:
- W1A untracked batch land (但走 Tier 1+2/3 分类) — CC1 30-45min
- W2D U16 memory ingest — CC1 60-90min

**P1 (今晚启动, 高 ROI 视觉强化)**:
- W2C PF-C4-02 真数据接线 + 微交互 (含 dispatch 注册 + Hermes pre-flight) — GPT Pro spec + Codex 通宵
- W1B 第 1 步: 写 OpenDesign reuse strategy v2 candidate (D3 单点引 vs 自写选项) — CC1 + Hermes 外审

**P2 (明日 / 后日)**:
- W2C V-PASS + audit + merge
- W1B Codex 通宵实施 (OpenDesign v2 merged 后)
- W3E 80-pack 第一个 cluster (推荐 PF-C3 跟 PF-C4 强相关)

**P3 (中期 1-2 月)**:
- W4F Phase 2 ASR spike (需 authority 升级 PR)
- W4G Phase 2 Rewrite spike (依赖 W4F)
- W5H Source matrix 扩展 (yt-dlp / XHS / 抖音 / Research)
- W5I 评论 / 楼中楼 子系统

**P4 (长期 2+ 月, 终极闭环)**:
- W6J Vault commit 真解禁 (true_vault_write 升级)
- W6K Memory + 协作模式沉淀

---

# §16 风险 + 边界守护硬红线

## §16.1 永不踩的硬红线

1. ❌ `write_enabled=False` (bridge/config.py:24,36) 不能改
2. ❌ 5 overflow lane 永不"偷开" (`true_vault_write` / `runtime_tools` / `browser_automation` / `dbvnext_migration` / `full_signal_workbench`) — 必须走 authority 升级 PR
3. ❌ Authority files 永不写 (`docs/current.md` / `docs/task-index.md` / `docs/decision-log.md` / `AGENTS.md` / 根 `CLAUDE.md`)
4. ❌ 历史 ledger immutable (`CHECKPOINT-Run*.json` / `EXTERNAL-AUDIT-REPORT-*.md` / `PF-C4-01-CHECKPOINT.json`)
5. ❌ `~/workspace/raw/` 永不污染 (除真 vault commit 解禁后)
6. ❌ 引整套 vendored shadcn / Radix / TanStack 全家桶 / React Flow / Zustand (即使 vendored 也不行, §10 reject list)
7. ❌ Tailwind / shadcn / Panda / Lucide / styled-components / @emotion / @stitches / panda-css / Mantine / Ant Design / Chakra UI / @mui (任意 styling/UI npm package install)
8. ❌ Hex 硬编码 (除 tokens.css / density / type-weight 三文件)
9. ❌ generic admin/dashboard 视觉气质 (战友审美红线)
10. ❌ Browser automation (playwright / selenium) — 视觉终判战友亲眼
11. ❌ Trust Trace DTO 改字段名 / shape (current.md 明文锁)
12. ❌ `PlatformResult` enum / `WorkerReceipt` schema 改 (current.md 明文锁)
13. ❌ `Vault Commit` + `Transcribe` 真接 future-gated route (UI 必须 disabled state)
14. ❌ Motion 渗透 wiki/reading surface (现在没 wiki, 但 spec 显式锁)
15. ❌ Vendor lock-in (BBDown 当前 only video, cease-and-desist 信号已现, 必须多元化)

## §16.2 候选 / authority 升级路径 (合法解禁)

| 解禁项 | 路径 | 必走步骤 |
|---|---|---|
| 单点引 D3 (npm d3) | OpenDesign reuse strategy v2 candidate (D5/§5.2 升级 single-point graph lib slot) | spec PR + Hermes 外审 + merge |
| Whisper.cpp Metal (runtime_tools) | runtime_tools authority 升级 PR | spec PR + Hermes 外审 + merge + benchmark evidence |
| Vault commit (true_vault_write) | true_vault_write authority 升级 PR | spec PR + Hermes 外审 + merge + 全 7 阶段 pipeline 通 + 完整 frontmatter contract |
| browser automation | browser_automation authority 升级 PR | spec PR + Hermes 外审 + merge (需要明确 use case, 当前无) |
| db_vnext migration | dbvnext_migration authority 升级 PR | spec PR + Hermes 外审 + merge + backup plan |

**绝不**: 跳过 authority 升级路径直接派 Codex / GPT Pro 实施.

## §16.3 风险矩阵

| 风险 | 概率 | 影响 | 缓解 |
|---|---|---|---|
| Codex 跑超时 / silent flexibility 触发 | LOW | 单 lane 失败 | amend_and_proceed pattern 已立 (lane total ≤ 1) |
| GPT Pro spec 漂移 (一次性 thinking 偏离) | LOW | 单 spec 重写 | architect verdict + 反模式扫描 |
| Hermes pre-flight 不及时 | MED | 阻塞 lane 启动 | 战友提前 paste, Hermes 不在线时 fallback CC1 self-audit |
| OpenDesign reuse strategy 升级争议 | MED | 阻塞 W1B / W4F | 候选 doc + 三方外审 + 战友拍板 |
| 16 ZIP batch land 噪声化 main | MED | grep 噪声 | Tier 1/2/3 分类 (修订自 CC0 漏洞 4) |
| BBDown cease-and-desist 升级 | HIGH | B 站 source fail | 优先 yt-dlp 多元化 (W5H) |
| Apple Silicon 兼容性 (库) | MED | 性能 / 失败 | U14 baseline + 多模型 fallback |

---

# §17 时间预算 (近 / 中 / 长)

## §17.1 近期 (今晚 + 明日 / 1-3 day)

| Wave | 时间 | 派给 |
|---|---|---|
| W1A untracked batch land (Tier 分类) | 30-45 min | CC1 |
| W2D U16 memory ingest | 60-90 min | CC1 |
| W2C dispatch 注册 + Hermes pre-flight | 1.5h | CC1 + Hermes |
| W2C GPT Pro spec one-shot | 30 min thinking | GPT Pro |
| W2C commander prompt 整合 | 1h | CC1 |
| W2C Codex 通宵实施 | 5-7h | Codex |
| W2C V-PASS + audit + merge | 1.5h | 战友 + CC1 |
| W1B OpenDesign v2 candidate | 1.5h | CC1 + Hermes |
| W1B Codex 通宵实施 | 5-7h | Codex |

**今晚开足马力总投入**: CC1 4-5h / GPT Pro 30min / Codex 通宵 / Hermes 1-2h / 战友 V-PASS 1.5h.

## §17.2 中期 (1 周 - 1 月)

| Wave | 时间 |
|---|---|
| W3E 80-pack 第一 cluster (PF-C3) | 一夜 Codex multi-PR |
| W3E 后续 cluster (PF-C0 / O1) | 各一夜 |
| W4F Phase 2 ASR authority 升级 PR | 1-2 天 |
| W4F Phase 2 ASR spec + 实施 | 2-4 天 |
| W4G Phase 2 Rewrite | 2-4 天 (依赖 W4F) |
| W5H Source matrix yt-dlp adapter | 一夜 |
| W5H XHS adapter | 一夜 |

## §17.3 长期 (1-3 月)

| Wave | 时间 |
|---|---|
| W5H 全 source matrix (YouTube / 抖音 / Research / RSS / PDF / Image) | 数周 |
| W5I 评论 / 楼中楼 全功能 | 1-2 周 |
| W6J Vault commit 真解禁 + 完整闭环 | 数周 (依赖前置全 ready) |
| W6K Memory 沉淀全集 | 任何间隙 |

---

# §18 战友 Next Action Checklist

## §18.1 今晚 (open-mike, 4 并行)

- [ ] **W1A**: 我跑 untracked batch (Tier 分类 → 单 PR squash → merge)
- [ ] **W2D**: 我跑 U16 memory ingest (sniff + 提取 + 写 memory)
- [ ] **W2C 启动 pre-flight**: 我先注册 task-index.md / decision-log.md → 你 paste 给 Hermes pre-flight
- [ ] **W1B 第 1 步**: 我写 OpenDesign reuse strategy v2 candidate (你拍板 A 单点 D3 vs B 自写) → 你 paste 给 Hermes 外审
- [ ] **W2C 第 2 步**: Hermes pre-flight V-PASS 后, 我写 commander prompt → 你 paste 给 GPT Pro spec → 整合 → paste 给 Codex 通宵

## §18.2 明日 (V-PASS + 第二轮)

- [ ] **W2C V-PASS**: 你浏览器走 13 surface (动态 + 真数据)
- [ ] **W2C audit + merge**: 我跑 audit + merge (路径 1 / 2 / 3)
- [ ] **W1B Codex 实施** (如 OpenDesign v2 merged): 你 paste W1B commander prompt 给 Codex 通宵
- [ ] **W3E 启动**: 你拍板第一个 cluster (PF-C3 / PF-C0 / O1)

## §18.3 1 周内

- [ ] W3E 80-pack 第一 cluster 完成
- [ ] W4F Phase 2 ASR authority 升级 PR

## §18.4 1 月内

- [ ] W4F 全 ASR pipeline 落地
- [ ] W4G Rewrite pipeline 落地
- [ ] W5H Source matrix 至少 yt-dlp + XHS 落地

## §18.5 长期 (2-3 月)

- [ ] W6J Vault commit 真解禁 + 全 7 阶段闭环
- [ ] W5I 评论 / 楼中楼 全功能
- [ ] W6K Memory 沉淀

---

# §19 引用 + 单源 anchor

## §19.1 真 authority 文档

- `docs/current.md` — 当前真态 (治理硬规则)
- `docs/task-index.md` — Active lane registry (max=3)
- `docs/decision-log.md` — Authority writer (max=1, 单写)
- `docs/research/repairs/opendesign-reuse-strategy-candidate-2026-05-05.md` (PR #122 merged) — 真 stack authority + §10 reject list
- `docs/PRD-amendments/prd-v2.1-...-candidate-2026-05-04.md` — 单人 prosumer + 强视觉 capture-side
- `docs/SRD-amendments/h5-bridge-para-vault-srd-v3-candidate-2026-05-04.md` — 5 routes 边界 + Trust Trace DTO 锁
- `bridge/config.py:24,36` — write_enabled=False invariant
- `~/.claude/rules/aesthetic-first-principles.md` — 5 Gate Checklist

## §19.2 储能层 reference (16 ZIP)

`docs/research/strategic-upgrade/2026-05-07/`:
- `outputs/U1-deep/` — PRD-v3 candidate / SRD-v3 candidate / 4 entity v0
- `outputs/U2-deep/` — 5 lane playbook (含 LANE-2 ASR runbook)
- `outputs/U3-deep/` — 4 entity v0 contract lock + RI-test
- `outputs/U4-visual-asset/` — visual_asset SQLite spec
- `outputs/U5-agent-fleet/` — agent_fleet_dispatch_ledger schema
- `outputs/U6-retrieval-dam/` — visual-DAM thumbnail+pHash spec
- `outputs/U7-state-library/` — state machine library
- `outputs/U8-egress/` — cross-system egress manifest
- `outputs/U9-dispatch-catalog/` — Phase 2-4 dispatch catalog (≥71 prompt)
- `outputs/U10-runbook/` — prosumer SOP runbook library
- `outputs/U11-anti-pattern/` — anti-pattern encyclopedia
- `outputs/U12-tools-catalog/` — kills + tools + MCP + plugin catalog
- `outputs/U13-visual-brand/` — visual style brand atlas (token + 8 panel + 30 icon)
- `outputs/U14-apple-silicon/` — Apple Silicon optimization 全集
- `outputs/U15-decision-log/` — 240+ PR decision log atlas
- `outputs/U16-memory-graph/` — cross-session memory graph (将 ingest)

## §19.3 历史 PR baseline

- PR #122 — OpenDesign reuse strategy candidate merged
- PR #205 — bridge vault preview smoke
- PR #206 — bridge openapi golden contract
- PR #239 — Run-2 amendment
- PR #240 — Run-3+4 PF-C1+C2 single-PR squash
- PR #241 — PF-V P0-P8 closeout (152 PNG + 76 H5 + tokens)
- PR #242 — PF-C2 closure
- **PR #243 — PF-C4-01 baseline (本 spec 起点)** ← `e1deda6`

## §19.4 协作模式 reference

- `~/.claude/projects/.../memory/project_4_agent_division_v3.md` — 4-agent v3 分工
- `~/.claude/projects/.../memory/feedback_codex_long_runner.md` — Codex Long Runner 战绩
- `~/.claude/projects/.../memory/feedback_gpt_pro_heavy_producer.md` — GPT Pro 角色
- `~/.claude/projects/.../memory/feedback_prompt_design_principles.md` — 重型派单 prompt 7 原则
- `~/.claude/projects/.../memory/working_pacing_and_preferences.md` — Codex 节奏 + 战友偏好
- `~/.claude/rules/codex-metacognition-learnings.md` — Codex 8 元认知 + 实战命中

## §19.5 跨项目兄弟项目

- `~/workspace/contentflow/` — ContentFlow legacy (内容生产闭环)
- `~/workspace/DiloFlow/` — DiloFlow (兄弟项目终点)
- `~/workspace/hermes-agent/` — Hermes (3rd party auditor, openai venv)

---

> 本 spec by CC1 (Anthropic), 2026-05-07 post 刑部尚书严审 + 综合另一个 CC0 5 漏洞修订 + 4 角色视角 (CC conductor / 算法工程师 / UX 设计师 / U16 cross-session memory) 综合
> 起点: PR #243 baseline (commit e1deda6)
> 文件路径: `docs/research/post-frozen/PR243-baseline-collection-line-master-spec-2026-05-07.md`
> 下一步: 战友拍板 §18.1 今晚 4 并行 是否启动
