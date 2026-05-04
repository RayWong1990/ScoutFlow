# T-P1A-023 LLM Normalization Schema
> Status: **draft / not yet PR-ready** — blocked by T-P1A-022 unmerged; research / candidate only; not authority; not runtime approval; not implementation approval.
> Date: 2026-05-04
> Depends on: T-P1A-022 merged (hard gate)
> Dependency snapshot: PR #38 is open draft at head `50c80519e9744c2b4abfe8c57f6da4cd5d6c0799`; this note must be reconciled after that PR merges.

---

## 1. Scope

This note drafts a candidate LLM normalization schema for transcript-derived knowledge
artifacts:

```text
transcript/raw.json
  -> transcript/segments.jsonl
  -> normalized/summary.md
  -> normalized/claims.jsonl
  -> normalized/quotes.jsonl
  -> normalized/topic_candidates.jsonl
  -> normalized/structured.md
```

It does not run an LLM, install packages, call a vendor API, create a prompt runner, or
change authority docs. Because T-P1A-022 has not merged, all references to
`transcript/segments.jsonl` are compatibility assumptions against the current T-P1A-022
draft, not a final schema.

Allowed write scope for this task:

- `docs/research/t-p1a-023-llm-normalization-schema-2026-05-04.md`

No service code, worker code, test file, migration, credential, prompt runner, generated
artifact, or authority document is added by this task.

---

## 2. Boundary State Machine

Candidate future pipeline, shown only as a state model:

```text
segments_not_available
  -- future ASR/postprocess gate clear + T-P1A-022 schema accepted -->
segments_candidate_ready
  -- future normalization gate clear + prompt contract approved -->
normalization_candidate_ready
  -- provenance validator clear + hallucination guard clear -->
knowledge_artifacts_candidate_ready
  -- future human review / authority promotion gate clear -->
knowledge_artifacts_reviewed
```

Transition gates:

| Transition | Gate | Current status |
|---|---|---|
| `segments_not_available -> segments_candidate_ready` | T-P1A-022 merged; future ASR/postprocess output exists | blocked |
| `segments_candidate_ready -> normalization_candidate_ready` | LLM prompt contract approved; no production runner in this task | blocked |
| `normalization_candidate_ready -> knowledge_artifacts_candidate_ready` | provenance validator checks every claim / quote against segment ids | candidate only |
| `knowledge_artifacts_candidate_ready -> knowledge_artifacts_reviewed` | human review records accepted / rejected / revised artifacts | Phase 2+ outline |

Invariant: an LLM output without segment provenance is not a ScoutFlow knowledge artifact.
It is an untrusted draft and must not enter future `artifact_assets` as reviewed material.

---

## 3. Input Assumptions From ASR Segments

These fields mirror the merged T-P1A-022 §4.3 candidate `segments.jsonl` schema
(`scoutflow.asr.segment.v0.candidate`). Reconciliation §10 step 3 verified field-level
alignment after T-P1A-022 merged.

Candidate input line from `transcript/segments.jsonl`:

```json
{"schema":"scoutflow.asr.segment.v0.candidate","segment_id":"seg_000001","source":"asr_raw","start_ms":0,"end_ms":4210,"text":"候选原始转写文本","speaker":null,"confidence":0.86,"chunk_id":"chunk_000","char_start":0,"char_end":9,"review_state":"unreviewed","raw_refs":["raw.segments[0]"]}
```

Required downstream assumptions:

| Field | Normalizer use | Guardrail |
|---|---|---|
| `segment_id` | primary citation key for claims, quotes, summary anchors, and structured sections | must be stable; no generated segment ids |
| `start_ms` / `end_ms` | time provenance and quote replay | must be integer ms; `start_ms < end_ms`; monotonic enough for display |
| `text` | only source text the LLM may summarize or quote | empty text segments excluded from prompt payload |
| `confidence` | risk signal for claims and quotes | low confidence should add `needs_check`, not be hidden |
| `speaker` | optional attribution | nullable; never invent speaker labels |
| `chunk_id` | retry / batching trace | used for prompt chunking and error localization |
| `review_state` | source quality marker | unreviewed segments can feed candidate outputs only |
| `raw_refs` | audit trace to ASR raw output | preserved in provenance metadata, not shown to user by default |

Prompt payload should include `segment_id`, timestamps, text, speaker if present, and
confidence. It should not include absolute local paths, raw ASR JSON, cookies, URLs with
tracking params, or hidden operator notes.

> Engine note (informational): Per merged T-P1A-022 §8, the first-gate ASR engine is
> `faster-whisper` with Claude cleanup. This schema remains engine-agnostic by design;
> downstream normalization does not depend on engine identity. The engine note is
> informational only and does not constrain future engine swaps as long as
> `scoutflow.asr.segment.v0.candidate` is honored.

---

## 4. Candidate Output Contracts

All paths below are future capture-root relative paths. They are candidate names, not
approved filesystem authority.

### 4.1 `normalized/summary.md`

Human-readable summary for quick review. It must stay traceable to segment ranges.

Candidate front matter:

```yaml
schema: scoutflow.normalized.summary.v0.candidate
source_segments: transcript/segments.jsonl
normalizer: llm-candidate
review_state: unreviewed
segment_coverage:
  first_segment_id: seg_000001
  last_segment_id: seg_000042
  omitted_segment_ids: []
```

Body rules:

- Summary paragraphs should reference source segment ranges with compact anchors, for
  example `[seg_000001..seg_000006]`.
- The model may compress wording but must not introduce facts absent from source segments.
- Low-confidence sections should be marked `needs_check` in a short reviewer note rather
  than smoothed into confident prose.
- The summary is for scanning. It is not the source of truth for claim extraction.

Validation ideas:

- Every segment anchor resolves to an input `segment_id`.
- `first_segment_id` and `last_segment_id` are within the input file.
- `omitted_segment_ids` are explicit when large transcript blocks are skipped.
- Markdown front matter parses as YAML and has `schema`, `source_segments`, and
  `review_state`.

### 4.2 `normalized/claims.jsonl`

One factual claim per line. A claim is a paraphrased assertion that may be useful for
research, planning, or later knowledge graph linking.

Candidate line:

```json
{"schema":"scoutflow.normalized.claim.v0.candidate","claim_id":"claim_000001","text":"候选主张文本","claim_type":"fact|interpretation|recommendation|open_question","supporting_segments":["seg_000003","seg_000004"],"source_span":{"start_ms":11800,"end_ms":23400},"confidence":"high|medium|low","risk_flags":["needs_check"],"status":"candidate"}
```

Field rules:

| Field | Requirement |
|---|---|
| `claim_id` | deterministic within one normalization run; no global authority implied |
| `text` | concise claim, not a quote; must be supportable by segment text |
| `claim_type` | candidate-local classification only |
| `supporting_segments` | non-empty list; every id must exist in `segments.jsonl` |
| `source_span` | derived min/max timestamps from supporting segments |
| `confidence` | model confidence about extraction quality, not truth authority |
| `risk_flags` | include `needs_check`, `low_asr_confidence`, `ambiguous_subject`, or `weak_support` when relevant |
| `status` | candidate-local value; default `candidate` |

Validation ideas:

- Reject claims with empty `supporting_segments`.
- Reject claims whose `source_span` does not cover all cited segments.
- Flag claims where cited segment text has no lexical overlap with claim text. This is
  not a perfect semantic test, but catches many unsupported hallucinations.
- Flag claims supported only by low-confidence ASR segments.

### 4.3 `normalized/quotes.jsonl`

One quote per line. A quote is an extractive text span, not a paraphrase.

Candidate line:

```json
{"schema":"scoutflow.normalized.quote.v0.candidate","quote_id":"quote_000001","text":"候选原文摘录","segment_ids":["seg_000012"],"start_ms":50200,"end_ms":57800,"speaker":null,"asr_confidence":0.82,"quote_kind":"verbatim|lightly_cleaned","status":"candidate","notes":[]}
```

Field rules:

| Field | Requirement |
|---|---|
| `quote_id` | deterministic within one normalization run |
| `text` | should be copied from segment text; cleanup must be minimal |
| `segment_ids` | non-empty and ordered |
| `start_ms` / `end_ms` | derived from cited segment range |
| `speaker` | nullable; never invented |
| `asr_confidence` | min or weighted average across cited segments; method recorded later |
| `quote_kind` | `verbatim` when exact, `lightly_cleaned` for punctuation / filler cleanup |
| `status` | candidate-local value; default `candidate` |

Validation ideas:

- Exact quotes should be substring-matchable after whitespace normalization.
- `lightly_cleaned` quotes must retain a source segment id and should be marked
  `needs_check` if edits change meaning.
- Do not emit quotes across unrelated segment gaps without an explicit reason.

### 4.4 `normalized/topic_candidates.jsonl`

One candidate topic per line. This is selection input, not a final recommendation.

Candidate line:

```json
{"schema":"scoutflow.normalized.topic_candidate.v0.candidate","topic_id":"topic_000001","title":"候选选题标题","angle":"候选切入角度","supporting_claims":["claim_000001"],"supporting_quotes":["quote_000001"],"source_segments":["seg_000003","seg_000012"],"score":null,"score_basis":[],"status":"candidate"}
```

Field rules:

- `score` is nullable in this layer. Scoring can wait for a future selection lane.
- If a score is present, `score_basis` must explain the dimensions used, for example
  novelty, evidence density, creator fit, or user interest.
- Topics must cite either supporting claims, supporting quotes, or direct source segments.
- `title` is a working label. It should not be treated as a published title.

Validation ideas:

- Reject topics with no provenance.
- Reject topics that cite claim or quote ids not present in the same artifact set.
- Flag scored topics whose `score_basis` is empty.

### 4.5 `normalized/structured.md`

Reviewable long-form synthesis for human editing or Obsidian-like note taking.

Candidate front matter:

```yaml
schema: scoutflow.normalized.structured.v0.candidate
source_segments: transcript/segments.jsonl
source_claims: normalized/claims.jsonl
source_quotes: normalized/quotes.jsonl
source_topics: normalized/topic_candidates.jsonl
review_state: unreviewed
target_surface: local_markdown_candidate
```

Body sections:

```markdown
## 核心观点

- 候选观点。[claim_000001; seg_000003..seg_000004]

## 可引用原话

> 候选原文摘录
> [quote_000001; seg_000012; 00:50.200-00:57.800]

## 可发展选题

### 候选选题标题

Evidence: topic_000001 / claim_000001 / quote_000001
```

Rules:

- `structured.md` is assembled from validated claims, quotes, and topics. It should not
  introduce new unsupported facts.
- Every bullet or paragraph carrying factual content should include at least one
  `claim_id`, `quote_id`, or segment range.
- The file can be useful for Obsidian / local Markdown later, but storage target is a
  future decision. This task does not decide Obsidian vs SQLite vs another surface.

---

## 5. Prompt Contract Candidate

The prompt should be treated as a structured transformer, not a creative writer.

Required prompt inputs:

- Task name and schema version, for example `scoutflow.normalization.v0.candidate`.
- Explicit instruction: use only provided segment text.
- Segment array with `segment_id`, `start_ms`, `end_ms`, `text`, nullable `speaker`,
  `confidence`, `review_state`, and `chunk_id`.
- Output schema names and one JSONL object per line for JSONL artifacts.
- Refusal condition: if evidence is insufficient, emit `risk_flags=["weak_support"]`
  or skip the claim/topic.

Required prompt constraints:

```text
You may summarize and classify only the supplied transcript segments.
Every claim must cite one or more segment_id values.
Every quote must be extractive and cite one or more segment_id values.
Never invent speaker names, timestamps, URLs, metrics, citations, or external facts.
If a segment is low confidence, preserve that uncertainty in risk_flags.
Return JSONL objects only for JSONL artifacts.
```

Recommended execution shape for a future runner:

1. Chunk transcript by `chunk_id` or bounded token window.
2. Extract local claims and quotes per chunk.
3. Run a merge pass that only deduplicates already-cited objects.
4. Generate summary and structured markdown from validated intermediate objects.
5. Run post-processing validators before any artifact is admitted to a future ledger.

Not approved here: API client, provider selection, retry code, token budgeting, model
download, local vLLM, prompt runner CLI, or background worker.

---

## 6. Hallucination Guardrails

Guardrails should be both prompt-level and post-processing. Prompt instructions alone are
not enough.

| Risk | Prompt-level guard | Post-processing guard |
|---|---|---|
| unsupported claim | require `supporting_segments` | reject empty or invalid segment refs |
| fake quote | require extractive quote | substring / fuzzy source check |
| invented speaker | speaker may only copy nullable input | reject speaker not present in cited segments |
| timestamp drift | timestamps derived from segments, not model | recompute `source_span` from input |
| low-confidence smoothing | require `risk_flags` | flag objects citing low-confidence segments |
| cross-chunk contradiction | mark uncertainty | human review or later conflict detector |
| external fact injection | use only supplied text | reject URLs / citations / numbers absent from source text unless quoted |

Candidate validator sequence:

```text
load segments.jsonl
  -> validate segment ids / timestamps / text
load candidate JSONL artifacts
  -> validate schema keys
  -> resolve every segment / claim / quote reference
  -> recompute time spans
  -> run quote source check
  -> flag weak lexical support for claims
  -> emit review report
```

The validator should fail closed for missing provenance. It can flag semantic uncertainty
for human review, but it should not silently repair unsupported content.

---

## 7. Future `artifact_assets` Mapping

This section is a candidate map for future receipt integration. It does not change the
current receipt schema.

| Future path | Candidate artifact kind | Current status | Ledger rule |
|---|---|---|---|
| `transcript/raw.json` | `transcript_raw_candidate` | owned by future ASR gate | raw evidence, not reviewed |
| `transcript/segments.jsonl` | `transcript_segments_candidate` | depends on T-P1A-022 | source for normalization |
| `normalized/summary.md` | `llm_summary_candidate` | Phase 1A-end research candidate | cite segment ranges |
| `normalized/claims.jsonl` | `llm_claims_candidate` | Phase 1A-end research candidate | every line cites segments |
| `normalized/quotes.jsonl` | `llm_quotes_candidate` | Phase 1A-end research candidate | extractive check required |
| `normalized/topic_candidates.jsonl` | `topic_candidates_candidate` | Phase 2+ selection input | no final score required |
| `normalized/structured.md` | `structured_note_candidate` | Phase 2+ human review surface | assembled from validated objects |

Admission rule candidate: future `artifact_assets` should store relative paths, sha256,
byte size, producing job id, schema string, review state, and validator result. It should
not store full prompt text, provider secrets, raw API responses, or absolute local paths.

---

## 8. Phase Split

Phase 1A-end candidate:

- Define the artifact names and schema intent.
- Keep all schemas `candidate / not authority`.
- Require segment provenance for claims and quotes.
- Define prompt constraints and validator ideas.
- Preserve `audio_transcript`, ASR, LLM runtime, workers, and frontend as blocked.

Phase 2+ outline:

- Decide whether `claims.jsonl` and `quotes.jsonl` stay separate or merge into one
  evidence object stream.
- Decide whether `topic_candidates.jsonl` receives scoring here or in a later selection
  lane.
- Decide target surface for `structured.md`: Obsidian, local Markdown, SQLite-backed note,
  or another review UI.
- Implement prompt runner only after provider, secret handling, redaction, retry, cost,
  and receipt contracts are approved.
- Promote any schema to authority only through a later explicit contract task.

---

## 9. Brainstorm Questions For User Review

1. Should `claims.jsonl` and `quotes.jsonl` remain separate? Separate files give better
   provenance discipline; a combined evidence stream reduces mapping overhead.
2. Should `topic_candidates.jsonl` include scores in the normalization layer? A null
   score keeps this layer evidence-first; scoring early helps ranking but risks mixing
   extraction with selection.
3. Should hallucination control rely more on prompt constraints or post-processing?
   Recommendation candidate: both, with post-processing as the enforceable gate.
4. What is the first target for `structured.md`: Obsidian-style local Markdown,
   plain repo-external capture folder, or SQLite-backed review state?

---

## 10. Reconciliation Checklist After T-P1A-022 Merge

Before opening a PR for this task:

1. Rebase `task/T-P1A-023-llm-normalization-schema` onto updated `origin/main`.
2. Confirm T-P1A-022 is merged and `docs/research/t-p1a-022-asr-pipeline-prestudy-2026-05-04.md`
   exists on `main`.
3. Compare this note's assumed `segments.jsonl` fields with the merged T-P1A-022 schema.
4. If T-P1A-023 needs additional fields, add a candidate delta section instead of
   redefining `segments.jsonl`.
5. Run shared validation and open PR only after the dependency is satisfied.

---

## 11. Boundary Confirmation

- No LLM runtime is executed in this task.
- No prompt runner, API client, provider config, model download, or credential is added.
- No ASR, ffmpeg, BBDown, browser automation, worker, frontend, or `audio_transcript`
  runtime is approved.
- No service code, test code, migration, `data/`, `referencerepo/`, `apps/`, `workers/`,
  or `packages/` path is modified.
- No authority document is modified.
- No schema is final authority.
- PR is intentionally not opened while T-P1A-022 remains unmerged.

---

## 12. Shared 5-Part Self-Audit

1. Scope check - changed file is limited to this research note under `docs/research/`.
2. Authority check - PRD / SRD / locked principles / spec contracts remain untouched.
3. Safety check - `audio_transcript` remains blocked; this note does not create workers,
   receipt schema, PlatformResult values, provider config, credentials, prompt runner,
   generated transcript artifacts, or runtime gate.
4. Validation result - local validation clear on 2026-05-04:
   `python tools/check-docs-redlines.py`;
   `python tools/check-secrets-redlines.py`;
   `python -m pytest tests/api tests/contracts -q` = 116 passed;
   `git diff --check`; forbidden tracked/root directory checks empty.
5. Next gate - T-P1A-022 must merge first; then rebase, reconcile `segments.jsonl`, run
   shared validation, push, and open PR.
