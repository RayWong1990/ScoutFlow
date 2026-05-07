<!--
U6 Retrieval & DAM Layer candidate package.
Status: candidate / not-authority.
Boundary: spec only; no service deployment; no production code write; no ScoutFlow authority write.
Live web note: this execution environment had web browsing disabled. External 2026 freshness is therefore marked as not live-verified.
-->

# EMBEDDING MODEL SELECTION — 2026-05-07

> Claim label: candidate ≥95% for selection criteria and local-only architecture; model availability/version freshness requires live-web refresh.  
> Decision posture: recommend a primary path, fallback path, and emergency path; do not approve cloud embedding.

## Source Basis / 读取依据

- U6 cloud prompt: visual-DAM + hybrid-local-search, single-user local SQLite, output ZIP with 9 files, candidate / not-authority, no production deployment, no cloud embedding, no Spotlight write. 引用标记：fileciteturn0file0
- PRD v2: ScoutFlow 是 single-user、local-first 的内容采集与证据整理系统；authority 由 SQLite + FS + state words 构成；不做 SaaS、多用户、浏览器自动化、平台互动、runtime 越权。引用标记：fileciteturn1file0
- SRD v2: 默认本机 127.0.0.1、SQLite + FS 双事实源；API 负责 validation/idempotency/state transition/receipt/trust trace；Worker 不直连 authority SQLite；当前不批准 BBDown/ffmpeg/ASR/frontend/runtime 扩张。引用标记：fileciteturn2file0
- Local audit pack: `/mnt/data/ScoutFlow-post176-cloud-audit-pack-2026-05-05.zip`，已解包读取 repo docs、current、contracts、dispatch127-176、external reports、code refs。
- Execution-environment probe, not user's physical Mac: SQLite FTS5 available; Pillow installed; `sentence-transformers` not installed; `ollama` not found; `whisper` not found; FAISS/Chroma/LanceDB/DuckDB Python imports not found in this sandbox.


## 1. Selection Criteria

ScoutFlow’s search corpus is unusual: Chinese/English mixed prose, Markdown specs, PR/task IDs, dispatch numbers, source code fragments, and authority/candidate labels. A good embedding model must therefore satisfy these criteria:

1. **Bilingual semantic recall**: Chinese queries must find English docs and English identifiers; English queries must find Chinese reports.
2. **Identifier tolerance**: The embedding layer does not replace FTS, but it should not collapse when chunks contain `T-P1A-104`, `PR #139`, `audio_transcript`, or `superseded_by`.
3. **Local-only operation**: model files live on the user’s machine; no request leaves the machine.
4. **Apple Silicon viability**: usable through PyTorch MPS, MLX, Core ML, or Ollama’s local acceleration path.
5. **Disk budget**: target model cache ≤2 GB for the first release.
6. **Latency**: interactive query embedding should be sub-second to a few seconds; batch indexing can be slower.
7. **Rebuild reproducibility**: model name, dimensions, provider, and embedding version must be stored so old embeddings can be invalidated.
8. **Install friction**: current execution sandbox does not have `sentence-transformers` or `ollama`; the spec must include fallback behavior rather than assuming either is present.

## 2. Candidate Models / Providers

The following table is a candidate selection matrix. Live web was unavailable in this environment, so version/current release facts must be refreshed before implementation.

| Candidate | Provider path | Strength | Risk | Suggested role |
|---|---|---|---|---|
| `BAAI/bge-m3` | sentence-transformers / local HF cache / possibly Ollama | multilingual, strong bilingual retrieval reputation, can support dense + lexical-ish use cases | larger than MiniLM; install/model download needed; exact current packaging needs refresh | **Primary recommendation** if local install succeeds |
| `nomic-embed-text` | Ollama or local transformer path | widely used local embedding option, simple Ollama UX | bilingual quality must be tested on ScoutFlow Chinese/English corpus; live version check needed | Fallback via Ollama |
| `mxbai-embed-large` | Ollama or local model path | strong local retrieval reputation, good for English/general semantic search | Chinese recall and disk/latency need local benchmark | Fallback/benchmark candidate |
| `intfloat/multilingual-e5-base` or large variant | sentence-transformers | multilingual retrieval family; good baseline for bilingual queries | requires query/passsage prefix discipline in many E5 workflows; model size varies | Alternative primary if bge-m3 underperforms |
| `sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2` | sentence-transformers | small, fast, low disk, good emergency install | weaker retrieval for technical authority docs; lower ceiling | Emergency low-footprint path |
| `thenlper/gte-*` multilingual/base variants | sentence-transformers | practical retrieval baseline; may be efficient | exact multilingual and current model status need refresh | Benchmark candidate |
| Apple local/Foundation Models embedding API | Apple-local if available | excellent privacy posture if system-provided and local | API availability and embedding suitability need live/platform verification | Future candidate, not first default |
| CLIP/SigLIP image-text embedding | local transformer/CoreML | useful for semantic visual search beyond pHash | expands DAM scope and model footprint; not required for U6 MVP | Later DAM extension only |

## 3. Recommendation

### 3.1 Primary path

Use `BAAI/bge-m3` through `sentence-transformers` as the first serious candidate **after live verification and local install check**. Reasons:

- The corpus is bilingual, and bge-m3 is a better fit than English-only embedding models.
- It can support Chinese user queries like “May 4 supersession 决定” and English docs containing `superseded_by`.
- It keeps all embeddings local.
- It has enough quality headroom that hybrid search can rely on dense retrieval for paraphrase, not just token overlap.

Implementation contract:

```yaml
embedding_provider:
  name: sentence_transformers
  model: BAAI/bge-m3
  device_preference: [mps, cpu]
  normalize_embeddings: true
  batch_size_indexing: 16
  batch_size_query: 1
  max_sequence_length: 768
  local_files_only_after_first_download: true
```

The indexer stores:

```text
provider = sentence_transformers
model_name = BAAI/bge-m3
dimensions = <actual model output dimension>
embedding_version = sha256(provider + model_name + normalize + max_length + pooling)
```

When any of these change, old embeddings are invalid and must be rebuilt.

### 3.2 Fallback path

Use Ollama embeddings if the user already runs Ollama locally. The first fallback candidates are `nomic-embed-text` and `mxbai-embed-large`, with `bge-m3` via Ollama if available and live-verified. The integration is simple: call local `http://127.0.0.1:<ollama_port>` and treat it as local-only. It still needs explicit config because a local HTTP service is a boundary.

```yaml
embedding_provider:
  name: ollama
  endpoint: http://127.0.0.1:11434
  model: nomic-embed-text
  normalize_embeddings: true
  timeout_seconds: 30
  allow_remote_host: false
```

Security rule: reject any Ollama endpoint that is not loopback unless the user explicitly overrides in a local-only config. The default must not send private docs to a LAN or cloud endpoint.

### 3.3 Emergency path

If no heavy model is installed, use `paraphrase-multilingual-MiniLM-L12-v2` or another small multilingual MiniLM model. It will not be the best answer, but it enables the search pipeline and keeps the model cache low. For a single user, a weaker embedding layer plus strong FTS/metadata often beats no embedding layer.

## 4. Local Benchmark Plan

Before finalizing the model, run a small benchmark with 40-60 known-answer queries. Use ScoutFlow’s own failure cases, not generic datasets.

### 4.1 Query set categories

| Category | Example |
|---|---|
| exact ID | `T-P1A-104`, `PR #93`, `Dispatch176` |
| authority boundary | `audio_transcript 为什么 blocked` |
| paraphrase | `是否可以启动 frontend implementation` |
| bilingual | `May 4 supersession decision` |
| code link | `Vault preview path containment` |
| report insight | `daily loop search/index risk` |
| replay lineage | `Dispatch127-176 task PR artifact chain` |
| visual/DAM | `GPT-Image-2 mockup similar assets` |

### 4.2 Metrics

- Recall@5: does a correct chunk appear in top 5?
- MRR@10: is the first correct result near the top?
- ID exact-hit rate: do exact task/PR queries preserve IDs?
- Authority correctness: does current/contract outrank candidate when answering “allowed now?”
- Latency: query encoding + rerank under interactive threshold.
- Disk: model cache + DB + embeddings within budget.

### 4.3 Acceptance thresholds

For first implementation:

```text
Recall@5 on known-answer set >= 0.80
Exact ID hit top1 >= 0.95
Authority correctness >= 0.90
No cloud request observed
Model cache <= 2 GB unless user explicitly accepts exception
```

If bge-m3 improves semantic recall but exact IDs degrade, keep bge-m3 and adjust hybrid weighting; do not abandon FTS.

## 5. Apple Silicon Optimization

For sentence-transformers on an M-series Mac, try PyTorch MPS first, but keep CPU fallback. Indexing is offline, so correctness and stability beat maximum speed. Suggested behavior:

```python
if torch.backends.mps.is_available():
    device = "mps"
else:
    device = "cpu"
```

Batch sizes should be conservative:

| Machine class | Initial batch | Notes |
|---|---:|---|
| 8GB unified memory | 4-8 | avoid swap during long rebuild |
| 16GB unified memory | 8-16 | likely comfortable for bge-m3-sized models |
| 32GB+ unified memory | 16-32 | tune after measuring |

MLX and Core ML are attractive, but the first implementation should not require model conversion. Conversion increases moving parts and makes rebuild reproducibility harder. Use MLX/Core ML only after the sentence-transformers/Ollama path is proven.

## 6. Why Not Cloud Embeddings

Cloud embeddings would simplify quality and installation, but they violate U6’s privacy-first boundary. The corpus includes private workflows, handoffs, memory, PR strategy, local paths, and possibly sensitive operational notes. Sending that to a cloud embedding API would be a material policy change and would contradict the prompt’s hard boundary. The local-only rule applies even to “just a benchmark” unless the user separately authorizes a redacted test corpus.

## 7. Storage and Versioning

Embedding rows should be normalized and versioned:

```sql
CREATE TABLE IF NOT EXISTS embedding_models (
    model_key TEXT PRIMARY KEY,
    provider TEXT NOT NULL,
    model_name TEXT NOT NULL,
    dimensions INTEGER NOT NULL,
    normalize_embeddings INTEGER NOT NULL CHECK(normalize_embeddings IN (0,1)),
    max_sequence_length INTEGER,
    pooling TEXT,
    local_cache_path TEXT,
    created_at TEXT NOT NULL,
    live_verified_at TEXT,
    notes TEXT
);
```

`live_verified_at` remains null in this package because web browsing was disabled. Implementation should fill it only after actual vendor/source verification.

## 8. Final Selection

Recommended first order:

1. `BAAI/bge-m3` via `sentence-transformers` on MPS/CPU.
2. `bge-m3`, `nomic-embed-text`, or `mxbai-embed-large` via local Ollama if Ollama is already installed and loopback-only.
3. `multilingual-e5-base` if bge-m3 install or latency is unacceptable.
4. `paraphrase-multilingual-MiniLM-L12-v2` as the low-footprint emergency path.
5. Apple local/Foundation Models only after API availability and embedding quality are verified on the user’s actual macOS version.
6. CLIP/SigLIP visual embeddings are deferred; pHash/dHash solves U6’s MVP DAM dedup without adding a large visual model.


## 9. Model Comparison Scoring Rubric

Use a 1-5 score per criterion during local benchmark:

| Criterion | Weight | What 5 means |
|---|---:|---|
| Chinese/English recall | 0.25 | Chinese queries reliably find English/ID-heavy docs and Chinese reports |
| Authority query behavior | 0.15 | works well with hybrid rerank on “approved/blocked/current” questions |
| Exact ID compatibility | 0.10 | does not hurt task/PR/dispatch exact retrieval when blended |
| Apple Silicon runtime | 0.15 | runs without swap, uses MPS/Ollama/CPU reliably |
| Disk footprint | 0.10 | fits model cache budget comfortably |
| Install friction | 0.10 | user can install once and rebuild without drama |
| Privacy certainty | 0.10 | local-only path is obvious and enforceable |
| Maintenance risk | 0.05 | active enough, no fragile conversion path for MVP |

Compute:

```text
model_score = sum(weight_i * score_i)
```

A smaller model can win if the large model causes swap or installation pain. U6 is a daily local utility, not a leaderboard exercise.

## 10. Provider Interface

All providers should implement the same tiny interface:

```python
class EmbeddingProvider:
    provider_name: str
    model_name: str
    dimensions: int | None
    def probe(self) -> ProviderStatus: ...
    def embed_texts(self, texts: list[str]) -> np.ndarray: ...
    def embed_query(self, query: str) -> np.ndarray: ...
```

`probe()` must report:

```yaml
available: true|false
local_only: true|false|unknown
device: mps|cpu|ollama_loopback|mlx|coreml
model_cache_path: ...
dimensions: ...
error: ...
```

If `local_only` is not true, provider is rejected. If dimensions are unknown until first call, write them after the first embedding and refuse to mix vectors with different dimensions.

## 11. Embedding Text Format

Quality depends on what is embedded. Recommended chunk text:

```text
TITLE: <document title>
KIND: <kind>
AUTHORITY: <authority_label>
PHASE: <phase>
TASK: <task_id>
PR: <pr_number>
HEADINGS: <h1 > h2 > h3>
BODY:
<chunk body>
ALIASES:
<normalized ids and known aliases>
```

This helps the dense model preserve context that would otherwise live only in metadata. Do not overdo it; too much metadata can drown body content. Keep the display snippet separate from the embedded text.

## 12. Model Lifecycle

Model changes require explicit rebuild steps:

1. Add new `embedding_models` row.
2. Run benchmark against known-answer set on a subset.
3. If accepted, rebuild embeddings for all chunks into a staging column/table.
4. Switch active model key in config.
5. Keep old embeddings until the new run passes, then delete or archive.

Do not silently overwrite embeddings with a different model. Silent model drift makes search quality impossible to debug.

## 13. Why bge-m3 Is Still Only a Candidate

The architectural recommendation favors bge-m3 because of multilingual retrieval fit, but the package does not claim live 2026 verification. A browsing-enabled pass must confirm current model card, license, dimensions, recommended usage, and Apple Silicon install path. A local benchmark must then confirm it beats at least one smaller fallback on ScoutFlow queries. Only after those two checks should it become the default.


## 14. Installation Decision Tree

The first implementation should probe rather than assume:

```text
if sentence_transformers import succeeds:
    list local cached models
    if bge-m3 cached or user approves local download:
        use bge-m3 benchmark
    else:
        use cached multilingual model if any
elif ollama executable exists and endpoint is loopback:
    list local embedding models
    use first approved candidate benchmark
else:
    run lexical-only mode and print install suggestions
```

This avoids turning search into a dependency debugging session. The tool remains useful in lexical-only mode, and the embedding layer can be added later.

## 15. Bilingual Retrieval Stress Cases

Benchmark queries should include cross-language paraphrases:

| Query | Expected concept |
|---|---|
| `是否可以 true write vault` | `write_enabled=false`, Vault commit dry-run |
| `current gate for browser automation` | browser automation blocked in current |
| `May 4 强视觉 四面板` | strong visual H5 panel docs |
| `superseded_by evidence ledger` | DB vNext candidate supersession DDL |
| `Codex handoff overflow registry` | Dispatch175/176 continuation docs |
| `search old capture reuse time` | product premortem daily loop metric |

If a model cannot handle these without exact keyword help, hybrid search can still compensate, but model score should be lower.

## 16. Local-Only Verification

A provider is accepted only if all are true:

```yaml
network_destination: loopback_or_none
api_key_required: false
model_files_local: true
embedding_request_contains_private_text: local_only
telemetry_disabled_or_none: true
```

If any field is unclear, the provider is `defer`. “Probably local” is not enough for ScoutFlow handoff and memory content.


## 17. Query Prefix Policy

Some embedding families, especially E5-style models, expect prefixes such as `query:` and `passage:`. The provider config should define this explicitly:

```yaml
text_format:
  query_prefix: "query: "
  passage_prefix: "passage: "
```

bge-style and MiniLM-style models may not need the same prefixes. Prefix policy is part of `embedding_version`; changing it requires re-embedding. This prevents silent quality drift when switching model families.

## 18. Final Model Governance

Only one model should be active for production-like daily search. Multiple models are allowed for benchmarking, but the active index should have a single `model_key`. This keeps DB size predictable and makes ranking explanations understandable. If the user later wants model A for Chinese and model B for code, that should be a new candidate spec, not hidden complexity in U6 MVP.


## 19. Small-Model Escape Hatch

If all high-quality models exceed the user’s comfort budget, choose a small multilingual model and lean harder on FTS5. ScoutFlow contains many explicit identifiers, so hybrid retrieval can remain useful even when dense semantic quality is moderate. The escape hatch is not failure; it is budget discipline. Record the compromise in `embedding_models.notes` so future upgrades know why the smaller model was selected.


## 20. Rejection Examples

Reject any embedding option that requires an API key, sends text outside loopback, lacks a clear local model path, or cannot report dimensions/version. Also reject options that require indexing the corpus through a hosted dashboard. Convenience does not outweigh privacy for ScoutFlow memory and handoff content.


## 21. Final Model Acceptance Sentence

The accepted model is the smallest local model that passes the ScoutFlow benchmark with clear privacy, dimensions, and rebuild metadata.
