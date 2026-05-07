---
title: Cloud Prompt — U6 Retrieval & DAM Layer (单人混合检索 + 视觉资产管理)
status: candidate / cloud_prompt / not-authority
authority: not-authority
created_at: 2026-05-07
target_window: GPT Pro web 浏览模式
new_lane: yes
---

# Cloud Prompt — U6 Retrieval & DAM Layer

## §1 Mission

ScoutFlow 累积: 240+ PR / 18 memory file / 数十 handoff / 数百 dispatch transcript / ~160-180 PF-V GPT-Image-2 输出 / 1000+ 张 image (~6 月内增长). **当前没有任何检索 / DAM 基础设施** — `git log` + `grep` + Finder 在 ~500 张图就崩.

本任务: 写两个底层 service 的完整 candidate spec — 
1. `visual-DAM` (thumbnail + perceptual hash dedup + grid browser + EXIF-equivalent metadata, 单人量级 ≤800 行 Python + sqlite-vss / FAISS)
2. `hybrid-local-search` (FTS5 + sentence embedding hybrid index, 跨 PR + memory + handoff + dispatch transcript), 单人量级 ≤500 行 Python + SQLite FTS5 + 本地 embedding model (本机 sentence-transformers / ollama / Apple Foundation Models)

不是企业 ElasticSearch / pgvector 集群; 是单人本机 SQLite + 本地 model.

## §2 Inputs

1. https://github.com/RayWong1990/ScoutFlow/blob/main/docs/PRD-v2-2026-05-04.md
2. https://github.com/RayWong1990/ScoutFlow/blob/main/docs/SRD-v2-2026-05-04.md (FTS5 / SQLite 既有 base)
3. PF-V INDEX.csv 19 列 (用户另窗口在跑) — visual asset 元数据来源
4. ScoutFlow 240+ PR / docs/research/ / docs/decision-log.md / handoff trail (检索语料)
5. **Live web** 真实 search 单人本机检索 / DAM / embedding 选型
6. 本机已装 Whisper / 是否已装 sentence-transformers / ollama 状态

## §3 Multi-pass Work Plan (≥10 pass, ≥120 min)

1. **Pass 1**: 读 PRD / SRD / 现有 FTS5 sqlite_fts5 既有 impl (如有) / PF-V INDEX.csv schema
2. **Pass 2 — Live web**: 真实 search ≥18: SQLite FTS5 best practice 2026 / sqlite-vss / sqlite-vec / Chroma local / LanceDB / DuckDB vector / sentence-transformers Apple Silicon / ollama embedding (mxbai / nomic / bge-m3) / Apple Foundation Models embedding / perceptual hash (pHash / dHash / aHash) / image dedup / Finder integration / Spotlight metadata / mdimporter / Eagle / Pixelmator app DAM internal
3. **Pass 3 — visual-DAM module spec**: 
   - SQLite 表 `visual_dam_index` (asset_id FK visual_asset / thumbnail_path / phash_64 / dhash_64 / dimensions / file_size / format / created_at / last_seen)
   - Thumbnail generator (Pillow / Sharp WASM)
   - Perceptual hash + dedup query (距离阈值)
   - Grid browser (本机 web UI 单页 ≤300 行 React or 简易 HTML5)
   - Spotlight integration (mdimporter / xattr metadata)
4. **Pass 4 — hybrid-local-search module spec**:
   - SQLite FTS5 表 (doc_id / kind ∈ {PR / memory / handoff / dispatch_transcript / decision_log / wiki / candidate / source_code} / title / body / file_path / created_at / phase / cluster)
   - Embedding column (sqlite-vec or sqlite-vss extension)
   - Hybrid query (BM25 from FTS5 + cosine from embedding, weighted sum reranking)
   - Index pipeline (file watcher + 增量 reindex + 定期 full rebuild)
   - 选型: sentence-transformers `bge-m3` (中英双语) on Apple Silicon, fallback `ollama` 本机 model
5. **Pass 5 — Cross-module integration**: 
   - visual-DAM 与 visual_asset (U4) 表 join 查询 ("过去 30 天哪些 GPT-Image-2 输出与 mockup XX 视觉相似度 ≥85%")
   - hybrid-local-search 跨 PR + memory + dispatch_transcript ("Codex 在 May 4 关于 supersession 的决定")
   - Replay tool (U5) 用 hybrid-search 找 dispatch lineage
6. **Pass 6 — Single-user budget**: 
   - visual-DAM ≤800 行 (Python core 500 + thumbnail/grid HTML 300)
   - hybrid-local-search ≤500 行
   - 总 ≤1300 行 / ≤1.5 周 / 模型 cache ≤2GB / SQLite db ≤500MB
7. **Pass 7 — Apple Silicon path**: M-series 优化 (Metal Performance Shaders / Core ML / mlx)
8. **Pass 8 — Privacy / no cloud**: 本机 model only, 不 send anything to OpenAI / Anthropic embedding API
9. **Pass 9 — Self-audit ≥15**
10. **Pass 10**: README + truthful stdout

## §4 Hard Boundaries

- candidate / not-authority
- write_enabled=False 不变
- 仅 spec, 不实际部署 service 或写 production code
- 不批准 cloud embedding API 调用 (单人 privacy-first)
- 不批准 Spotlight write (只读 metadata, 不写 xattr 不可逆操作)
- DAM 不 touch 原图文件位置, 仅生成 thumbnail / phash 副本

## §5 Live Web Evidence Refresh

≥18 真实 search:
- SQLite FTS5 / sqlite-vec / sqlite-vss 2026
- sentence-transformers + bge-m3 / nomic / mxbai 中英双语
- Apple Foundation Models embedding 2026
- ollama 本机 model 2026 (Llama 3.3 / Qwen 2.5 / DeepSeek)
- LanceDB / DuckDB vector / Chroma local 2026
- Eagle / Mylio prosumer DAM 2026
- pHash / dHash / aHash benchmark
- BM25 + dense hybrid retrieval 2026 (Reciprocal Rank Fusion / weighted sum)
- Apple Silicon mlx / MPS 加速

## §6 Cross-local Search

- 本机 `which whisper` / `pip show sentence-transformers` / `which ollama`
- ScoutFlow 现有 SQLite FTS5 schema (services/api/scoutflow_api/**)
- DiloFlow 是否需要相同检索 (可能复用)
- `~/.claude/skills/` 是否已有 search / retrieval skill
- ContentFlow L1 wiki 检索踩坑

## §7 Output Deliverables

ZIP filename: `cloud-output-U6-retrieval-dam-layer-2026-05-07.zip`
File count: **9**

| # | File | min 字 | claim label |
|---|---|---:|---|
| 1 | MODULE-visual-dam-spec-2026-05-07.md | 3500 (SQLite DDL + thumbnail/pHash pipeline + grid UI) | ≥95% |
| 2 | MODULE-hybrid-local-search-spec-2026-05-07.md | 3500 (FTS5 + embedding + hybrid query + 索引 pipeline) | ≥95% |
| 3 | EMBEDDING-MODEL-SELECTION-2026-05-07.md | 2500 (≥6 candidate model 对比 + Apple Silicon 优化) | ≥95% |
| 4 | INDEX-PIPELINE-DESIGN-2026-05-07.md | 2500 (file watcher + 增量 + full rebuild + 错误恢复) | ≥95% |
| 5 | CROSS-MODULE-QUERY-EXAMPLES-2026-05-07.md | 2200 (≥15 真实 query 示例: 跨 PR 检索 / 视觉相似 / 时间维度) | ≥95% |
| 6 | APPLE-SILICON-PATH-2026-05-07.md | 1800 (mlx / MPS / Core ML 加速选型) | ≥95% |
| 7 | LIVE-WEB-EVIDENCE-2026-05-07.md | 2500 (≥18 vendor + 访问日期) | ≥95% |
| 8 | SINGLE-USER-IMPLEMENTATION-BUDGET-2026-05-07.md | 1500 (≤1300 行 / ≤1.5 周 / 资源开销) | ≥95% |
| 9 | README-deliverable-index-2026-05-07.md | 1200 | 100% |

总字数 ≥**21000**

## §8 Self-audit (≥15)

- 单人本机 vs 企业集群 drift
- privacy: 是否暗示 cloud embedding
- Apple Silicon path 真实 vs 复制 generic 文档
- live web URL 真访问
- 与 U4 (visual_asset) 表 FK 是否对齐
- hybrid query 排序是否真合理
- index pipeline 错误恢复路径
- 单人 budget 数字真实

## §9 Truthful Stdout Contract

```yaml
CLOUD_U6_RETRIEVAL_DAM_LAYER_COMPLETE: true
zip_filename: cloud-output-U6-retrieval-dam-layer-2026-05-07.zip
files_count: 9
total_words_cjk_latin_approx: <真实>
total_thinking_minutes: <真实>
live_web_browsing_used: <true|false>
live_verified_count: <真实>
embedding_models_compared: <真实>
hybrid_query_examples_count: <真实>
single_user_budget_loc: <真实>
single_user_budget_dev_days: <真实>
single_user_budget_disk_mb: <真实>
multi_pass_completed: <真实/10>
self_audit_findings: <真实>
privacy_check: <"local-only" | concerns_listed>
boundary_preservation_check: clear
ready_for_user_audit: yes
```

## §10 ZIP Filename

`cloud-output-U6-retrieval-dam-layer-2026-05-07.zip`
