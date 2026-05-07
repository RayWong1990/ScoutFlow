---
title: "Cluster A — ASR Optimization Index"
status: "candidate / not-authority"
authority: "not-authority"
cluster: "A_ASR"
created_at: "2026-05-07"
---

# Cluster A — ASR Optimization Index


## Claim label legend

This pack uses explicit claim labels because U14 is a candidate research artifact, not production authority.

- `[prompt-provided]` means the item comes from the uploaded U14 prompt or from the uploaded post176 pack inspected in this session.
- `[post176-evidence]` means the note is derived from the local post176 zip contents; the repeated boundary there says ASR, FFmpeg, browser automation, `audio_transcript`, runtime unlock, and vault true write were not proved or approved.
- `[baseline-knowledge]` means stable general engineering knowledge available before the cutoff, such as Apple Silicon unified memory, Metal, MPS, Core ML, VideoToolbox, FFmpeg, PyTorch MPS, MLX, llama.cpp, Ollama, SQLite, and local media processing concepts.
- `[recipe-spec]` means a recommended configuration, benchmark protocol, fallback ladder, or integration shape that still needs local proof.
- `[requires-local-verification]` means the statement must be checked on the user's Mac with `system_profiler`, `sysctl`, `powermetrics`, package introspection, model hashes, and paste-time benchmark logs.
- `[not-web-verified-2026]` means the named framework, model, version, or vendor status would normally require live browsing. Live web was unavailable here, so no current vendor claim is asserted.
- `[privacy-boundary]` means raw materials stay local by default; cloud API replacement is explicitly not approved by this pack.


## Boundary preservation

`candidate / not-authority` is intentional. This file does not install software, does not load LaunchAgents, does not modify macOS settings, does not run ASR, does not transcode media, does not inspect private model directories, does not approve vault true writes, and does not present benchmark numbers as self-run evidence. Any command is a future local run specification only. A future operator must paste evidence before promotion.


## Scope

[prompt-provided] This index covers audio intake, VAD, transcription, diarization, timestamp repair, multilingual routing. It connects the cluster recipes and provides a dispatch surface for a human operator. The design rule is simple: choose the smallest local path that preserves raw evidence, then collect paste-time metrics before expanding model size, accelerator use, or concurrency.

## Recipes

| Recipe | File | Framework | Model | Min chip | Memory |
|---|---|---|---|---|---:|
| A01 | [Whisper.cpp Metal baseline for local ASR intake](A01-whisper-cpp-metal-baseline-for-local-asr-intake.md) | whisper.cpp + Metal | Whisper family GGML/GGUF local models | M1 | 8 GB |
| A02 | [Whisper.cpp quantization and thread tuning](A02-whisper-cpp-quantization-and-thread-tuning.md) | whisper.cpp + Metal + Accelerate | Whisper quantized local variants | M1 | 8 GB |
| A03 | [faster-whisper CTranslate2 Apple Silicon evaluation](A03-faster-whisper-ctranslate2-apple-silicon-evaluation.md) | faster-whisper / CTranslate2 | Whisper converted model | M2 | 16 GB |
| A04 | [Whisper-MPS fork evaluation lane](A04-whisper-mps-fork-evaluation-lane.md) | Whisper-MPS / PyTorch MPS | Whisper PyTorch checkpoint | M2 | 16 GB |
| A05 | [Parakeet TDT 0.6B Apple Silicon ASR candidate](A05-parakeet-tdt-0-6b-apple-silicon-asr-candidate.md) | Parakeet local wrapper | Parakeet TDT 0.6B | M3 | 16 GB |
| A06 | [Voxtral Mini audio-language candidate](A06-voxtral-mini-audio-language-candidate.md) | Voxtral local audio LLM wrapper | Voxtral Mini | M4 | 24 GB |
| A07 | [Real-time transcription with streaming chunks and backpressure](A07-real-time-transcription-with-streaming-chunks-and-backpressure.md) | whisper.cpp streaming controller | Whisper small/base local models | M1 | 8 GB |
| A08 | [Hallucination detection and recovery for transcripts](A08-hallucination-detection-and-recovery-for-transcripts.md) | ASR quality guard | Whisper plus local text/audio checks | M1 | 8 GB |
| A09 | [Speaker diarization and multilingual code-switch policy](A09-speaker-diarization-and-multilingual-code-switch-policy.md) | pyannote-style diarization + language router | speaker diarization model plus multilingual ASR | M2 | 16 GB |
| A10 | [VAD preprocessing with Silero MPS candidate](A10-vad-preprocessing-with-silero-mps-candidate.md) | Silero VAD / PyTorch MPS watchlist | Silero VAD model | M1 | 8 GB |

## Cluster flow


```mermaid
flowchart LR
    raw[Raw local inputs] --> manifest[Manifest + source hash]
    manifest --> fast[Fast local path]
    fast --> gate{Quality + resource gate}
    gate -- pass --> derived[Derived artifact]
    gate -- downgrade --> fallback[Fallback ladder]
    fallback --> derived
    derived --> audit[Run log + provenance]
```


## Decision rules

[recipe-spec] Start with deterministic transformations and explicit manifests. Do not promote a framework because it claims Apple Silicon support; promote it only when local backend evidence and quality review are pasted. Do not compare a tuned fast path against an untuned safe path. Compare full ladder against full ladder: fast path, smaller model path, CPU or deterministic fallback, dry-run path, and manual review path.

[requires-local-verification] This index does not include live 2026 vendor evidence. It therefore does not rank current frameworks by release status. Any MLX, Core ML, Metal, MPS, Foundation Models, VideoToolbox, Ollama, llama.cpp, Whisper, Parakeet, Voxtral, embedding model, or vector-store assumption remains a local verification item.

## Integration contract

[privacy-boundary] Outputs from this cluster may feed ScoutFlow vault, visual-DAM, retrieval, or review lanes only as candidate derivatives. A derived artifact must include source hash, recipe id, model/framework version, command/script revision, run timestamp, and downgrade flag. The raw input and operator approval remain authority.

## Review checklist

- All files preserve `candidate / not-authority`.
- Recipes contain required frontmatter fields.
- Benchmark cells are contracts, not results.
- Cloud API replacement is explicitly not recommended for private material.
- Fallback ladders are specific enough for future local runs.
- Model and framework license capture is required.
- Resource gates include memory pressure and thermal state where relevant.
- Outputs are structured for future vault or DAM consumers.

## Extended operating rationale — Cluster A — ASR Optimization

**Rationale 1.** ASR quality is a compound result of audio extraction, VAD, model choice, decoder settings, timestamp handling, language hints, and post-run repair. Optimizing only the transcriber can hide upstream defects. The ASR lane should therefore log the source media probe, WAV conversion, VAD decisions, transcription command, and repair steps together.

**Rationale 2.** For ScoutFlow, transcript usefulness depends on retrieval and review. Segment timestamps, speaker turns, language labels, hallucination flags, and source hashes are as important as plain text. A transcript that is fast but not traceable should not be written into any vault lane without manual approval.

**Rationale 3.** Use a fixed fixture set before scaling. For audio, include silence, music bed, cross talk, compressed platform audio, Chinese-English code switching, and long-form speech. For images, include screenshots, transparent PNG, huge JPEG, duplicate variants, and generated outputs. For video, include H.264, HEVC, variable frame rate, subtitles, and audio-only cases. The purpose is to reveal bottlenecks that matter to ScoutFlow, not to win a synthetic benchmark.

**Rationale 4.** Prefer local evidence over intuition. Apple Silicon performance can change when model size, quantization, context length, display load, package build flags, power source, and thermal state change. A fast demo is not enough. The run log should include command, input hash, model hash, version, power mode, memory pressure, thermal note, wall time, and fallback status.

**Rationale 5.** Keep the operator in control. In a one-person prosumer system, the fastest path is not always the best path. The better path often keeps the Mac responsive, preserves raw evidence, avoids silent mutation, and creates deterministic derived artifacts. A run that finishes earlier but loses timestamps, EXIF, model identity, or cache provenance should be considered a regression.

**Rationale 6.** Separate hot path and cold path. The hot path should use the smallest reliable model or transform for routing, triage, deduplication, or metadata extraction. The cold path can use a larger model only after chunking, VAD, BM25 filtering, pHash clustering, or reranking reduces the input set. This protects unified memory and keeps the UI usable.

**Rationale 7.** Design fallbacks before celebrating the fast path. Every recipe needs a smaller model fallback, a CPU-only or deterministic fallback, a deferred batch mode, and a dry-run metadata mode. Fallbacks are how the system survives missing frameworks, stale package versions, model license constraints, memory pressure, thermal throttling, and battery operation.

**Rationale 8.** Do not overfit to a single metric. Useful ScoutFlow metrics include throughput, quality, timestamp drift, retrieval success, memory peak, cache hit rate, downgrade frequency, queue latency, UI responsiveness, operator review time, and failure recoverability. A slightly slower configuration can be the better production candidate if it is more stable under mixed workloads.

**Rationale 9.** Treat 2026 framework status as a watchlist until verified. The prompt asks for current MLX, Core ML, Metal, MPS, ANE, Foundation Models, Whisper, Parakeet, Voxtral, Ollama, llama.cpp, and FFmpeg status. Live browsing was disabled, so this pack avoids claiming current releases or vendor benchmark results. It provides capture commands instead.

**Rationale 10.** Protect privacy by default. Local inference is preferred because raw ScoutFlow material may include unpublished ideas, private meetings, research prompts, screenshots, and DAM assets. Cloud endpoints may be useful for public experiments, but they are not approved as a replacement for private workflows in this U14 artifact.

**Rationale 11.** Emit boring structured artifacts. Each candidate run should produce JSONL or Markdown with recipe id, source hash, model identity, package version, command id, output schema version, timestamps, metrics, quality flags, and fallback flags. Structured logs make later vault writes, DAM indexing, retrieval debugging, and regression review possible.

**Rationale 12.** Preserve raw evidence. Optimization should never rewrite source audio, video, images, or notes in place. Derived transcripts, thumbnails, embeddings, crops, masks, frames, subtitles, and benchmark logs should live under a candidate cache with hash-linked paths. If a derivative is wrong, the system must be able to rebuild it without guessing settings.

**Rationale 13.** Use staged concurrency. Running ASR, embedding, local LLM inference, thumbnailing, OCR, and video transcode at once can overwhelm unified memory even on strong Apple Silicon hardware. Start with one heavy accelerator job plus one light coordinator, then increase concurrency only when memory pressure, thermals, and UI responsiveness remain stable.

**Rationale 14.** Define downgrade triggers. A recipe should name the signs that move a run from max-horsepower mode to balanced or safe mode: memory pressure yellow/red, swap growth, battery drain, thermal warnings, lower token throughput, repeated hallucination flags, timestamp gaps, or operator jank. Downgrades are a reliability feature, not a failure.

