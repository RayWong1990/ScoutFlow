# T-P1A-022 ASR Pipeline Prestudy
> Status: **research / candidate** — not authority; not runtime approval; not implementation approval.
> Date: 2026-05-04
> Depends on: T-P1A-017 merged (Wave 2 ledger open)
> Reconciliation: T-P1A-022 must merge before T-P1A-023 fixes any `segments.jsonl` schema.

---

## 1. Scope

This note designs a candidate ASR artifact shape and local spike plan for a future
`audio_transcript` chain. It does not enable ASR, ffmpeg, workers, or runtime capture.

Allowed write scope for this task:

- `docs/research/t-p1a-022-asr-pipeline-prestudy-2026-05-04.md`

No sample audio, binary fixture, service code, worker code, migration, test, or authority
document is added by this task.

---

## 2. Boundary State Machine

Candidate future pipeline, shown only as a state model:

```text
media_not_available
  -- future audio_extract gate clear -->
audio_candidate_available
  -- future ASR gate clear + input receipt verified -->
asr_raw_ready
  -- future postprocess gate clear -->
segments_candidate_ready
  -- future human review gate clear -->
reviewed_transcript_ready
```

Transition gates:

| Transition | Gate | Current status |
|---|---|---|
| `media_not_available -> audio_candidate_available` | future media / audio extraction approval; ffmpeg boundary decided | blocked |
| `audio_candidate_available -> asr_raw_ready` | future ASR runtime approval; engine preflight; receipt contract | blocked |
| `asr_raw_ready -> segments_candidate_ready` | timestamp normalization and segmentation contract | candidate only |
| `segments_candidate_ready -> reviewed_transcript_ready` | human review workflow and edit provenance | candidate only |

Invariant: `audio_transcript` remains blocked until a later user-approved dispatch opens
the relevant runtime gate. This note is only design input.

---

## 3. Public Source Snapshot

Checked public primary sources on 2026-05-04 for candidate-engine framing only.
No package was installed and no ASR command was executed.

| Source | Evidence used |
|---|---|
| [SYSTRAN faster-whisper README](https://github.com/SYSTRAN/faster-whisper/blob/master/README.md) | faster-whisper is a CTranslate2-based Whisper implementation; supports CPU / GPU deployment choices, int8 quantization, batching, and PyAV-based audio decoding. |
| [modelscope FunASR README](https://github.com/modelscope/FunASR/blob/main/README.md) | FunASR includes offline file transcription releases, timestamp / hotword capability references, Mandarin-oriented Paraformer models, SenseVoice, and multilingual model options. |
| [FunASR offline file transcription guide](https://github.com/modelscope/FunASR/blob/main/runtime/docs/SDK_advanced_guide_offline_en.md) | FunASR runtime combines VAD, ASR, and punctuation for file transcription and exposes local deployment / hotword configuration surfaces. |

These sources do not override ScoutFlow authority. They only shape what a later spike
should verify with local evidence.

---

## 4. Candidate Artifact Contract

All paths below are future capture-root relative paths. They are candidate names, not
approved filesystem authority.

### 4.1 Input

| Candidate path | Role | Required metadata | Current approval |
|---|---|---|---|
| `media/audio.wav` | normalized audio input for ASR | sample rate, channels, codec, duration_ms, sha256, bytes, produced_by_job | not approved |
| `media/audio.m4a` | compressed audio input when previous gate chooses not to normalize to wav | codec, container, duration_ms, sha256, bytes, produced_by_job | not approved |

Input rules:

- ASR does not own extraction from video. A prior future `audio_extract` job must create
  and receipt the input artifact first.
- The first ASR spike should prefer `media/audio.wav` as the canonical input because it
  makes sample rate / channel assumptions explicit.
- `media/audio.m4a` can remain a tolerated candidate only if the chosen ASR engine can
  decode it locally without leaking ffmpeg or media extraction into the ASR job boundary.
- Absolute local paths must never enter receipt payloads.

### 4.2 `transcript/raw.json`

Raw engine output, minimally normalized for storage, but not edited.

Candidate shape:

```json
{
  "schema": "scoutflow.asr.raw.v0.candidate",
  "capture_id": "01HXCAP...",
  "job_id": "01HXJOB...",
  "engine": {
    "name": "faster-whisper | funasr | other",
    "version": "candidate-to-record",
    "model": "candidate-to-record",
    "device": "cpu | gpu | mps | unknown",
    "compute_type": "int8 | float16 | float32 | unknown"
  },
  "input": {
    "relative_path": "media/audio.wav",
    "sha256": "candidate-sha256",
    "duration_ms": 1800000
  },
  "language": {
    "detected": "zh",
    "confidence": 0.91
  },
  "segments": [
    {
      "engine_segment_id": "seg-000001",
      "start_ms": 0,
      "end_ms": 4210,
      "text": "候选原始转写文本",
      "confidence": 0.86,
      "words": [
        {
          "start_ms": 120,
          "end_ms": 420,
          "text": "候选",
          "confidence": 0.78
        }
      ]
    }
  ],
  "warnings": []
}
```

Storage rules:

- Raw output may contain hallucinations, filler, repeated text, or punctuation drift.
- It should be stored as raw evidence, not as reviewed prose.
- If a selected engine does not provide word timestamps, `words` must be omitted rather
  than synthesized.

### 4.3 `transcript/segments.jsonl`

Postprocessed segment stream for downstream normalization and citation back to media.

One JSON object per line:

```json
{"schema":"scoutflow.asr.segment.v0.candidate","segment_id":"seg_000001","source":"asr_raw","start_ms":0,"end_ms":4210,"text":"候选原始转写文本","speaker":null,"confidence":0.86,"chunk_id":"chunk_000","char_start":0,"char_end":9,"review_state":"unreviewed","raw_refs":["raw.segments[0]"]}
```

Candidate rules:

- Timestamp precision should be stored as integer milliseconds.
- UI display can round to 100ms or 1s later, but storage should preserve ms to support
  citation, subtitle generation, and later alignment repair.
- `segment_id` must be stable across deterministic reprocessing of the same raw output.
- `speaker` is nullable until a diarization gate exists.
- `review_state` is one of candidate-local values: `unreviewed`, `needs_check`,
  `reviewed`. This is not a global state-word change.

### 4.4 `transcript/subtitle.srt`

Generated subtitle derivative from `segments.jsonl`, not source authority.

Rules:

- SRT timestamps are derived from `start_ms` / `end_ms`.
- Text line wrapping is presentation-only and should not feed back into
  `segments.jsonl`.
- If segment boundaries overlap or are invalid, SRT generation should fail instead of
  silently rewriting the source segments.

### 4.5 `transcript/reviewed.md`

Human-readable reviewed transcript. Candidate format:

```markdown
---
schema: scoutflow.transcript.reviewed.v0.candidate
capture_id: 01HXCAP...
source_segments: transcript/segments.jsonl
review_state: reviewed
reviewed_by: human
reviewed_at: 2026-05-04T00:00:00Z
---

## Transcript

[00:00.000-00:04.210] 候选人工校订文本。
```

Rules:

- `reviewed.md` must never overwrite `raw.json` or `segments.jsonl`.
- Human edits need provenance: reviewer, timestamp, and source segment reference.
- This file is not an LLM normalization result. T-P1A-023 owns the later normalization
  discussion.

---

## 5. Chunking Strategy

Recommended candidate strategy for future spike:

| Layer | Candidate default | Rationale |
|---|---|---|
| ASR engine input chunk | 30-60 seconds with 1-2 seconds overlap | Small enough for retry and memory safety; overlap reduces boundary word loss |
| Postprocess merge window | punctuation / silence / max 12-20 seconds per segment | Keeps citations readable for Bilibili 10-30 minute videos |
| Long-video batch | deterministic chunk ids: `chunk_000`, `chunk_001` | Allows retrying failed chunks without rerunning the whole file |
| Boundary repair | trim duplicate overlap text only when confidence and text similarity are clear | Avoids aggressive merge hallucinations |

Open design question for user review: if the main source corpus is mostly 10-30 minute
Bilibili videos, the initial spike should compare 30s and 60s chunks before considering
5-minute chunks. Five-minute chunks are simpler operationally but worse for retry,
memory spikes, and local progress feedback.

---

## 6. Timestamp Precision

Candidate storage precision: **integer milliseconds**.

Reasoning:

- 10ms display precision is probably too noisy for most UI and manual review.
- 100ms display precision is readable, but storing only 100ms may degrade downstream
  quote-to-source alignment.
- 1s precision is too coarse for sentence-level citations and subtitle correction.
- Storing ms and displaying rounded values gives the least lock-in.

Contract caution: this note does not finalize `segments.jsonl`. T-P1A-023 must not
define a conflicting segment schema until this research note has merged and been
reconciled.

---

## 7. Retry / Fallback Strategy

Candidate retry policy:

| Failure class | Retry? | Fallback |
|---|---|---|
| `asr_engine_not_found` | no | block until dependency installed / configured |
| `asr_model_missing` | no automatic network download | block or use pre-approved local model cache |
| `input_missing` | no | return to prior `audio_extract` gate |
| `input_decode_failed` | no automatic ffmpeg conversion | return to prior audio gate; ASR does not own extraction |
| `chunk_timeout` | yes, bounded retry for same chunk | retry once with smaller chunk size |
| `oom_or_memory_pressure` | yes, bounded | lower batch size / smaller model / CPU int8 fallback |
| `low_confidence` | no runtime retry by default | mark `needs_check`; require human review |
| `timestamp_unstable` | no blind retry | mark `needs_check`; compare engine settings in spike |
| `hallucination_suspected` | no blind retry | mark `needs_check`; preserve raw evidence |
| `redaction_or_receipt_failure` | no | stop before ledger write |

Fallback priority:

1. Same engine, safer settings: smaller batch, smaller chunk, explicit language.
2. CPU-safe mode if GPU path fails.
3. Alternative engine only after the task records why the first engine failed.
4. Human review marker instead of forcing a second model to agree.

---

## 8. Engine Candidates And CPU / GPU Notes

This section is spike input only; no engine is selected by this note.

| Candidate | Possible strength | Main risk to test |
|---|---|---|
| `faster-whisper` | strong general Whisper ecosystem; CPU / GPU / int8 choices; multilingual baseline | Chinese punctuation / segmentation quality; Apple Silicon support path; dependency/version friction |
| `FunASR` | Chinese-first model ecosystem; timestamp / hotword / punctuation surfaces; offline file service references | packaging weight; model cache policy; English / multilingual tradeoff; Docker/runtime complexity |
| platform subtitle first | avoids ASR when official subtitles exist | source availability and trust; subtitle drift; platform adapter scope |

CPU / GPU candidate rules:

- The first spike should be CPU-safe and deterministic unless user explicitly approves GPU
  dependency work.
- GPU acceleration must be a preflight result, not an assumption.
- Model download must be pre-approved and should stay outside repo.
- Record `engine`, `engine_version`, `model`, `device`, `compute_type`, `batch_size`,
  `chunk_seconds`, and wall-clock duration in local spike evidence.
- Do not treat a successful local transcription as product approval; it only informs the
  next gate.

Selection questions for user review:

- Is Chinese accuracy more important than broad English / multilingual coverage for the
  first `audio_transcript` gate?
- Should the initial comparison be `faster-whisper` vs `FunASR`, or should platform
  subtitles be the first baseline before any ASR?
- Is hotword support important for names, project terms, and technical vocabulary, or can
  it wait until after the first transcript loop exists?

---

## 9. Error Classes

Candidate error classes, scoped to future ASR chain:

| Error class | Meaning | Safe outcome |
|---|---|---|
| `asr_runtime_blocked` | user has not approved ASR runtime | stop before execution |
| `audio_input_not_approved` | input artifact has no prior receipt / gate | stop before ASR |
| `asr_engine_not_found` | configured engine import / executable unavailable | no receipt; dependency blocker |
| `asr_model_missing` | model not available in approved local cache | no automatic download |
| `input_decode_failed` | audio artifact cannot be decoded by selected engine | return to audio gate |
| `chunk_timeout` | one chunk exceeded timeout | bounded retry |
| `oom_or_memory_pressure` | local memory/device pressure | lower batch / smaller model fallback |
| `timestamp_unstable` | invalid, overlapping, or non-monotonic timestamps | mark output invalid; no SRT |
| `low_confidence` | confidence below future threshold | mark `needs_check` |
| `hallucination_suspected` | repeated text / no-speech hallucination pattern | mark `needs_check` |
| `redaction_or_receipt_failure` | output cannot safely enter ledger | stop before write |

These are candidate-local labels. They do not change current `PlatformResult`, capture
state words, or receipt schema.

---

## 10. Local Spike Plan

Future spike must be a separate approved task. Candidate plan:

1. Use a repo-external temp directory and a user-approved short audio artifact.
2. Verify no raw audio or model cache enters Git.
3. Run engine preflight only after dependency gate is opened.
4. Transcribe one short clip with fixed settings.
5. Emit local-only evidence packet: command shape, engine version, model, device, runtime,
   candidate artifact hashes, and redacted excerpt.
6. Generate `raw.json`, `segments.jsonl`, `subtitle.srt`, and `reviewed.md` in a temp
   capture root.
7. Run a schema validator in temp context, then decide whether to promote schema into a
   later authority task.

Not approved in this task:

- ASR execution.
- ffmpeg execution.
- Media download or audio extraction.
- Worker runtime.
- Model download.
- Writing generated transcript artifacts into repo.
- Updating PRD / SRD / locked principles / spec contracts.

---

## 11. T-P1A-023 Reconciliation Rule

T-P1A-023 owns LLM normalization schema, but it must not finalize `segments.jsonl` before
this note lands. Proposed reconciliation order:

1. Merge T-P1A-022 research note.
2. T-P1A-023 reads this candidate `segments.jsonl` and decides which fields it needs for
   normalization and quote provenance.
3. If T-P1A-023 needs different fields, it should write a candidate delta rather than
   silently redefining the ASR segment shape.
4. A later authority task can promote a combined transcript / normalization contract.

---

## 12. Boundary Confirmation

- No ASR runtime is executed in this task.
- No ffmpeg or audio extraction is executed in this task.
- No binary / audio sample enters the repository.
- No `audio_transcript` approval is granted.
- No schema is final authority.
- No authority document is modified.

---

## 13. Shared 5-Part Self-Audit

1. Scope check - changed file is limited to this research note under `docs/research/`.
2. Authority check - PRD / SRD / locked principles / spec contracts remain untouched.
3. Safety check - `audio_transcript` remains blocked; this note does not create workers,
   receipt schema, PlatformResult values, model cache, audio files, or runtime gate.
4. Validation result - local validation clear on 2026-05-04:
   `python tools/check-docs-redlines.py`;
   `python tools/check-secrets-redlines.py`;
   `python -m pytest tests/api tests/contracts -q` = 109 tests clear;
   `git diff --check`; forbidden tracked/root directory checks empty.
5. Next gate - still unapproved: workers, frontend, BBDown runtime, ffmpeg, ASR,
   `audio_transcript`, model download, generated transcript artifacts, and Phase 2-4
   runtime.
