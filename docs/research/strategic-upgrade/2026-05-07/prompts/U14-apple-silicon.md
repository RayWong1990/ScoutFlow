---
title: Cloud Prompt — U14 Apple Silicon Optimization Encyclopedia v0 (≥75 文件)
status: candidate / cloud_prompt / not-authority
authority: not-authority
created_at: 2026-05-07
target_window: GPT Pro web 浏览模式
expected_zip_files: 75+
expected_zip_words_cjk_latin: 110000+
expected_thinking_minutes: 150+
---

# Cloud Prompt — U14 Apple Silicon Optimization Encyclopedia

## §1 Mission

ScoutFlow 用户跑 Mac M-series (Darwin 25.5.0). 单人 max horsepower 模式下, **本机性能是天花板** — Whisper / sentence-transformers / ollama / llama.cpp / FFmpeg / Image-2 后处理 / Metal Performance Shaders / Core ML / mlx / VideoToolbox 等全栈 Apple Silicon 优化是 ScoutFlow Phase 2-4 unlock 后**性能差距决定生产率**.

本任务: 把 Apple Silicon 单人 prosumer 全栈优化沉淀为 **≥60 个 single-file optimization recipe**, 每 recipe = 一个具体场景的最优配置 + benchmark + fallback. 涵盖 ASR / Embedding / LLM / 视频 / 图像 / 系统集成 / 监控 / 资源管理.

外加 8 cluster index + 5 supporting (master atlas / hardware-spec-reference / energy-thermal-budget / linked-runbook / README) = **≥75 文件**.

## §2 Inputs

### A. 本机硬件 (硬证据 — Apple M5 假设)
1. ~/.claude/rules/parallel-safety.md (Mac vs Windows 历史踩坑)
2. ~/.claude/rules/codex-metacognition-learnings.md (ContentFlow L1 跨平台经验)
3. 本机 `system_profiler SPHardwareDataType` (chip / cores / memory)
4. `sysctl -a hw.optional.arm` (ARM extensions)
5. `system_profiler SPDisplaysDataType` (GPU cores)

### B. ScoutFlow 上下文 (优化目标)
6. https://github.com/RayWong1990/ScoutFlow/blob/main/docs/research/strategic-upgrade/2026-05-07/cloud-prompt-U2-phase-2-unlock-playbook.md (LANE-2 ASR / LANE-1 vault write 性能要求)
7. https://github.com/RayWong1990/ScoutFlow/blob/main/docs/research/strategic-upgrade/2026-05-07/cloud-prompt-U6-retrieval-dam-layer.md (visual-DAM + hybrid search)
8. PF-V GPT-Image-2 后处理 (cropping / pHash / thumbnail) 性能需求

### C. Live web (vendor / framework 现状)
9. 2026 Apple Silicon framework: mlx / Core ML / Metal Performance Shaders / MPSX / ANE
10. 2026 model 选型 Apple Silicon: Whisper.cpp / faster-whisper / Whisper-MPS / Parakeet / Voxtral / Phi / Qwen / DeepSeek / Llama.cpp Metal / ollama / llama.cpp v0.X
11. Vision framework / ImageIO / VideoToolbox
12. Apple Foundation Models 2026 (Swift API)

## §3 Multi-pass Work Plan (≥10 pass, ≥150 min)

1. **Pass 1 — Hardware spec reference**: M-series 架构 (P-core / E-core / GPU / ANE / Memory bandwidth / Unified Memory) + 当前用户机型 specs
2. **Pass 2 — Live web ≥18**: Apple Silicon framework 2026 / model benchmark / framework comparison
3. **Pass 3 — Cluster A: ASR Optimization (~10 recipe)**:
   - Whisper.cpp Metal optimization (model size / quant / threads)
   - faster-whisper CTranslate2 + MPS (vs Metal cpp)
   - Whisper-MPS (Apple-optimized fork)
   - Parakeet TDT 0.6B Apple Silicon
   - Voxtral Mini Apple Silicon
   - Real-time transcription (streaming + chunking)
   - Hallucination detection + recovery
   - Speaker diarization (pyannote MPS)
   - Multi-language switching (中英混排)
   - VAD pre-processing (silero MPS)
4. **Pass 4 — Cluster B: Embedding & Retrieval (~8 recipe)**:
   - sentence-transformers MPS (bge-m3 / nomic / mxbai)
   - sqlite-vec / sqlite-vss Apple Silicon
   - LanceDB Apple Silicon
   - DuckDB vector
   - Ollama embedding API
   - Apple Foundation Models embedding (Swift)
   - Hybrid BM25 + dense reranking
   - Index incremental + full rebuild
5. **Pass 5 — Cluster C: LLM Inference (~10 recipe)**:
   - llama.cpp Metal (Llama 3.3 / Qwen 2.5 / DeepSeek / Phi)
   - Ollama Apple Silicon (model selection / quant)
   - mlx-lm (Apple ML framework)
   - Apple Foundation Models 2026 (Swift API integration)
   - Multi-model concurrent (ollama serve)
   - Quantization tradeoff (Q4_K_M vs Q5_K_M vs Q8_0)
   - Context window optimization
   - Prompt caching (本机 KV cache)
   - 流式输出 + token throughput
   - LLM-as-a-judge benchmark
6. **Pass 6 — Cluster D: Image / Visual Processing (~8 recipe)**:
   - Pillow / Sharp / OpenCV Apple Silicon
   - Vision framework (Swift) face / text detection
   - Core ML model conversion + inference
   - GPT-Image-2 后处理 pipeline (crop / dedup / thumbnail)
   - Perceptual hash batch
   - Stable Diffusion local (mlx-stable-diffusion)
   - Background removal (rembg MPS)
   - 8K image handling (memory pressure)
7. **Pass 7 — Cluster E: Video / Audio Pipeline (~6 recipe)**:
   - FFmpeg VideoToolbox HW accel
   - VideoToolbox encoder/decoder
   - Audio extraction (44.1k → 16k mono for ASR)
   - Subtitle render
   - Frame extraction
   - Container conversion
8. **Pass 8 — Cluster F: System Integration (~8 recipe)**:
   - LaunchAgent / launchd
   - Spotlight / mdimporter
   - xattr metadata
   - Activity Monitor / powermetrics 监控
   - Energy budget management (低能耗 vs 高性能)
   - Thermal throttle 检测 + 降级策略
   - Memory pressure 检测
   - Background task assertion
9. **Pass 9 — Cluster G: Resource Management (~6 recipe)**:
   - Unified Memory budget (单进程 vs 跨进程)
   - GPU/ANE 调度 (低负载 ANE / 高负载 GPU)
   - Process priority
   - I/O throttle
   - Disk cache policy (APFS)
   - Battery vs A/C 模式策略
10. **Pass 10 — Cluster H: Benchmarking & Profiling (~6) + 8 cluster index + 5 supporting + truthful stdout**

## §4 Hard Boundaries

- candidate / not-authority 全 ≥75 文件
- 不实际跑 benchmark (仅 spec; benchmark 数字标 [reference / paste-time / vendor-claimed])
- 不修改本机配置 (LaunchAgent 仅 spec, 不实际 install)
- 不批准 cloud API 替代本机 model (privacy-first)
- 不暗示 production 部署 (仍 candidate research)

## §5 Live Web Evidence

≥18 真实 search:
- Apple Silicon M5 / M4 max benchmark 2026
- mlx 0.X 2026 / Core ML 8 / Metal 4
- Whisper.cpp / faster-whisper / whisper-mps 2026
- Parakeet TDT 0.6B / Voxtral / Apple Speech 2026
- llama.cpp Metal / ollama / mlx-lm 2026
- bge-m3 / nomic-embed / mxbai 2026
- VideoToolbox / FFmpeg HW accel
- Vision framework 2026 / Core ML 转换工具

## §6 Cross-local Search

- 本机 `system_profiler` / `sysctl` / `powermetrics` 实跑
- `which whisper` / `pip show ollama` / `brew list` 验证已装
- `~/Library/Application Support/ollama/` 已下 model list
- ContentFlow L1 ASR 踩坑历史

## §7 Output Deliverables

ZIP filename: `cloud-output-U14-apple-silicon-optimization-2026-05-07.zip`
File count: **≥75**

| 类别 | 文件数 | min 字 |
|---|---:|---:|
| Cluster A ASR | 10 | 1500 |
| Cluster B Embedding/Retrieval | 8 | 1500 |
| Cluster C LLM Inference | 10 | 1500 |
| Cluster D Image/Visual | 8 | 1500 |
| Cluster E Video/Audio | 6 | 1500 |
| Cluster F System Integration | 8 | 1500 |
| Cluster G Resource Mgmt | 6 | 1500 |
| Cluster H Benchmarking | 6 | 1500 |
| Cluster index (8) | 8 | 1500 |
| MASTER-OPTIMIZATION-ATLAS | 1 | 3000 |
| HARDWARE-SPEC-REFERENCE | 1 | 2200 |
| ENERGY-THERMAL-BUDGET | 1 | 2000 |
| LINKED-RUNBOOK-AND-DISPATCH | 1 | 2000 |
| README | 1 | 1500 |
| **总计** | **≥75** | ≥115000 |

claim label coverage ≥90%; Mermaid: hardware topology + cluster ≥3 = ≥4 张

## §8 Self-audit (≥25)

- benchmark 数字真标 [reference] vs 自跑 (无伪造)
- model selection 是否考虑 license (MIT / Apache / 商用 OK)
- privacy-first: cloud API 是否真排除
- thermal/energy budget 是否真考虑 (vs 一直 P-core max)
- mlx vs Core ML vs Metal 选择是否真合理 (各场景)
- 与 U6 retrieval-dam-layer 是否对齐 (embedding 选型)
- 与 U2-deep LANE-2 ASR 是否对齐
- 单人 prosumer vs 企业 server farm drift

## §9 Truthful Stdout Contract

```yaml
CLOUD_U14_APPLE_SILICON_OPTIMIZATION_COMPLETE: true
zip_filename: cloud-output-U14-apple-silicon-optimization-2026-05-07.zip
files_count: <真实, ≥75>
total_words_cjk_latin_approx: <真实, ≥110000>
total_thinking_minutes: <真实>
recipes_count: <真实, ≥60>
asr_recipes: <真实>
embedding_recipes: <真实>
llm_recipes: <真实>
image_recipes: <真实>
video_recipes: <真实>
system_integration_recipes: <真实>
resource_mgmt_recipes: <真实>
benchmarking_recipes: <真实>
benchmark_numbers_attributed: <true|false; if true, all marked [reference] not self-run>
mlx_recipes_count: <真实>
core_ml_recipes_count: <真实>
metal_recipes_count: <真实>
multi_pass_completed: <真实/10>
self_audit_findings: <真实, ≥25>
boundary_preservation_check: clear
ready_for_user_audit: yes
```

## §10 ZIP Filename

`cloud-output-U14-apple-silicon-optimization-2026-05-07.zip`

## §11 Format Guard

- 每 recipe frontmatter 含 `recipe_id` `cluster` `framework` `model` `min_chip ∈ {M1/M2/M3/M4/M5}` `memory_required_gb` `expected_speed`
- benchmark 数字标 [reference-vendor-claimed] / [reference-third-party] / [paste-time-2026-05]
- 任何 cloud API 替代必须显式标 not-recommended (privacy)
