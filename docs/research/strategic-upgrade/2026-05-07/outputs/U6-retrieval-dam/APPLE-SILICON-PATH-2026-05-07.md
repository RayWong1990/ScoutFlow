<!--
U6 Retrieval & DAM Layer candidate package.
Status: candidate / not-authority.
Boundary: spec only; no service deployment; no production code write; no ScoutFlow authority write.
Live web note: this execution environment had web browsing disabled. External 2026 freshness is therefore marked as not live-verified.
-->

# APPLE SILICON PATH — 2026-05-07

> Claim label: candidate ≥95% for practical M-series implementation path; exact Apple Foundation Models/OS API status requires live-web refresh.  
> Scope: MLX / MPS / Core ML / Ollama-local acceleration choices for U6 search and visual-DAM.

## Source Basis / 读取依据

- U6 cloud prompt: visual-DAM + hybrid-local-search, single-user local SQLite, output ZIP with 9 files, candidate / not-authority, no production deployment, no cloud embedding, no Spotlight write. 引用标记：fileciteturn0file0
- PRD v2: ScoutFlow 是 single-user、local-first 的内容采集与证据整理系统；authority 由 SQLite + FS + state words 构成；不做 SaaS、多用户、浏览器自动化、平台互动、runtime 越权。引用标记：fileciteturn1file0
- SRD v2: 默认本机 127.0.0.1、SQLite + FS 双事实源；API 负责 validation/idempotency/state transition/receipt/trust trace；Worker 不直连 authority SQLite；当前不批准 BBDown/ffmpeg/ASR/frontend/runtime 扩张。引用标记：fileciteturn2file0
- Local audit pack: `/mnt/data/ScoutFlow-post176-cloud-audit-pack-2026-05-05.zip`，已解包读取 repo docs、current、contracts、dispatch127-176、external reports、code refs。
- Execution-environment probe, not user's physical Mac: SQLite FTS5 available; Pillow installed; `sentence-transformers` not installed; `ollama` not found; `whisper` not found; FAISS/Chroma/LanceDB/DuckDB Python imports not found in this sandbox.


## 1. Working Assumption

The target machine is likely an Apple Silicon Mac because the prompt calls out Apple Silicon, local model cache, and local-first operation. The U6 implementation should run acceptably on M-series hardware without requiring cloud GPUs or external services. The design does not assume the execution sandbox is the user’s Mac; sandbox probe only confirmed SQLite FTS5 and Pillow availability, not user-local hardware.

## 2. What Needs Acceleration

U6 has three workloads:

1. **FTS5 lexical search** — CPU + SQLite, already fast enough.
2. **Text embeddings** — the only workload that may need MPS/MLX/Core ML/Ollama acceleration.
3. **Image hashing/thumbnails** — CPU/Pillow/NumPy is enough for ~1000-5000 images; no GPU required.

Therefore the Apple Silicon path should focus on embedding throughput and memory control. pHash does not need a neural visual model in the first release.

## 3. PyTorch MPS via sentence-transformers

This is the recommended first path for `BAAI/bge-m3` or E5/MiniLM candidates. It is easy to reason about and does not require conversion.

Config:

```yaml
embedding_runtime:
  provider: sentence_transformers
  device_order: [mps, cpu]
  normalize: true
  index_batch_size:
    8gb: 4
    16gb: 8
    32gb: 16
  query_batch_size: 1
  failover: cpu
```

Operational guidance:

- If MPS produces instability or memory pressure, fall back to CPU; indexing can run overnight.
- Keep chunk length modest. Long chunks waste memory and reduce retrieval precision.
- Store embeddings as float32 initially; quantization can wait.
- Print model/device at startup so the user knows whether acceleration is active.

## 4. MLX Path

MLX is attractive on Apple Silicon because it is built around Apple unified memory and local model execution. For U6, MLX is a **second-stage optimization**, not the first dependency. Use it when:

- a chosen embedding model has a maintained MLX conversion,
- local benchmark shows faster indexing or lower memory,
- embedding output dimensions and normalization can be kept identical enough to version safely,
- the implementation does not balloon beyond the ≤500 LOC search budget.

A practical MLX path might be a separate provider class:

```text
EmbeddingProvider
  - SentenceTransformersProvider
  - OllamaProvider
  - MlxProvider  # optional, later
```

The DB does not care which provider produced embeddings as long as `provider`, `model_name`, `dimensions`, and `embedding_version` are recorded.

## 5. Core ML Path

Core ML is useful if the user wants a stable, app-like local model runtime or if a future native macOS UI is built. It is not required for a Python sidecar MVP. Core ML conversion has costs:

- model conversion and validation work,
- potential pooling/normalization differences,
- extra files and versioning,
- harder debugging when retrieval quality changes.

Use Core ML only after the chosen model is settled and benchmarked. The acceptance condition is not “Core ML runs”; it is “Core ML produces retrieval quality comparable to the baseline provider and lowers latency/memory enough to justify the extra maintenance.”

## 6. Ollama Path

Ollama can be a low-friction local provider if already installed. It may use Apple Metal acceleration internally depending on model/runtime. U6 should treat Ollama as local only:

- endpoint must be loopback by default,
- model name must be explicit,
- query/index timeouts must be visible,
- failure falls back to lexical-only search rather than blocking all retrieval.

Example config:

```yaml
embedding_provider:
  name: ollama
  endpoint: http://127.0.0.1:11434
  model: bge-m3
  allow_non_loopback: false
```

If `ollama` is not installed, do not require it. The sandbox probe found no `ollama`, so this package cannot claim Ollama availability.

## 7. Apple Foundation Models Caveat

The prompt asks for Apple Foundation Models embedding 2026 evidence. Because live web is disabled, this package cannot verify current API status, availability, embedding dimensions, licensing, or local-only guarantees. Treat it as a future candidate. It should not be the first implementation default until the user’s actual macOS version and Apple documentation are checked.

Decision gate for Apple-local/Foundation Models:

```text
Must prove:
  - embedding API exists for local app/script use
  - no cloud request for private corpus
  - stable vector dimensions
  - quality on ScoutFlow benchmark >= fallback model
  - can store provider/model/version metadata
```

## 8. Memory and Disk Budget

Apple unified memory makes model choice important. Approximate first-release targets:

| Item | Target |
|---|---:|
| model cache | ≤2 GB |
| embedding DB | ≤250 MB for initial corpus |
| search DB total | ≤500 MB |
| visual thumbnails | 100-300 MB for ~1000-3000 images |
| query latency | interactive, with lexical fallback always available |
| indexing | can be batch/offline; does not need realtime |

If the model alone exceeds 2 GB, require explicit user acceptance and document why. A smaller model that runs reliably may outperform a larger model that causes swap and makes the user stop using the tool.

## 9. pHash and Thumbnail Performance

For ~1000 images, Pillow + NumPy pHash is sufficient on CPU. The expensive part is image decode, not hash math. Optimize by:

- skipping unchanged files by `mtime/size/sha256`,
- writing thumbnails only when original hash changes,
- using hash-band candidate lookup to avoid all-pairs comparison,
- lazy-generating detail thumbnails,
- keeping thumbnails under one derived root with sharded subdirectories.

Do not introduce OpenCV or a GPU image stack unless a real bottleneck appears.

## 10. Recommended Runtime Matrix

| Workload | First choice | Fallback | Later optimization |
|---|---|---|---|
| FTS search | SQLite FTS5 CPU | trigram/bigram fallback | none needed |
| Dense text embeddings | sentence-transformers + MPS/CPU | Ollama loopback or MiniLM | MLX/Core ML |
| Vector search | SQLite BLOB + NumPy | FAISS sidecar | sqlite-vec/vss after verification |
| Thumbnails | Pillow CPU | skip unsupported formats with error row | Sharp/libvips if real bottleneck |
| Image similarity | pHash/dHash CPU | sha256 exact only if hash fails | CLIP/SigLIP local model later |

The path is deliberately conservative: get a local searchable memory first, then optimize.


## 11. Practical Benchmark Script Shape

The user-Mac benchmark should report device, batch, model, and memory symptoms:

```yaml
benchmark:
  model: BAAI/bge-m3
  provider: sentence_transformers
  device: mps
  corpus_chunks: 1260
  batch_size: 8
  index_seconds: 180
  query_embedding_ms_p50: 120
  query_embedding_ms_p95: 250
  recall_at_5: 0.84
  authority_correct: 0.92
  swap_observed: false
  cloud_calls: 0
```

If `device=mps` is slower or less stable than CPU for a given model, CPU is acceptable. This is a local utility; predictable behavior is more important than theoretical acceleration.

## 12. Thermal and Battery Considerations

Indexing hundreds of docs or thousands of images can heat a laptop. Keep defaults polite:

- no automatic background rebuild on battery unless user opts in;
- batch embeddings with pause points;
- allow `--limit` and `--resume`;
- print progress every N files/chunks;
- let the user cancel safely without corrupting current DB.

Visual-DAM scan should be I/O-light after first run because unchanged files are skipped. Search embedding rebuild is the only heavy path.

## 13. When to Upgrade Beyond MVP

Move beyond PyTorch/Ollama baseline only when one of these is proven:

1. Query latency is unacceptable on the actual corpus.
2. Full rebuild takes so long that the user avoids reindexing.
3. Model memory causes swap on the user’s machine.
4. SQLite BLOB + NumPy vector scan exceeds the DB/latency budget.
5. A live-verified Apple-local API offers simpler, faster, local embeddings with comparable quality.

Until then, keep the path conservative. Every acceleration framework also creates a maintenance surface.


## 14. Provider Decision Tree

```text
Need fast first value?
  -> SQLite FTS5 only; no model required.
Need semantic recall and sentence-transformers works?
  -> bge-m3 or multilingual model on MPS/CPU.
Already have Ollama with embedding model?
  -> loopback Ollama provider; benchmark before default.
Need lower memory?
  -> MiniLM or E5 base; smaller chunks.
Need native Apple optimization?
  -> evaluate MLX/Core ML after baseline quality is known.
Need visual semantic search?
  -> defer CLIP/SigLIP until pHash DAM is useful.
```

The decision tree ensures the project never blocks on the most complex path. The first useful version can run with FTS5, Pillow, and SQLite only.

## 15. User-Mac Probe Output

Future implementation should write a local readiness file:

```yaml
machine:
  chip: Apple M-series detected by system_profiler
  memory_gb: <value>
python:
  version: <value>
  sqlite_fts5: true|false
  pillow: true|false
models:
  sentence_transformers: installed|missing
  ollama: installed|missing
  mlx: installed|missing
  torch_mps: available|missing
recommendation: lexical_first | bge_m3_mps | ollama_fallback
```

Do not infer this from the generation sandbox.


## 16. Why CPU Fallback Is Acceptable

A local search tool can tolerate slower indexing because indexing is batch work. Query-time embedding is the only interactive dense operation, and even that can fall back to lexical search. Therefore CPU fallback is not a failure; it is part of the reliability design. If MPS, MLX, or Ollama fails, the user should still be able to search exact IDs and authority boundaries immediately.

## 17. Avoiding Swap

The simplest swap prevention is conservative batch sizing and chunk limits. If the user observes swap or UI sluggishness, reduce batch size before changing model. A 16GB Mac running a smaller model smoothly is usually better than a larger model that monopolizes unified memory.


## 18. Recommended First Run on Mac

Run lexical index first, then a 20-query benchmark with the smallest acceptable local embedding provider. Only after the benchmark passes should the user spend time on MLX/Core ML optimization. This order protects momentum and avoids turning U6 into a model-runtime project.


## 19. Final Apple Silicon Decision

Default to boring success: SQLite and Pillow on CPU, embeddings through the simplest local provider that passes benchmark. Optimize only after measured pain.


## 20. Final Runtime Acceptance Sentence

Apple Silicon support is successful when it improves local responsiveness without making installation, rebuild, or privacy harder.


## 21. Extra Guard

Acceleration is optional; local correctness is mandatory.
