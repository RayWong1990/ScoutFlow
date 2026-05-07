---
title: "Whisper-MPS fork evaluation lane"
status: "candidate / not-authority"
authority: "not-authority"
recipe_id: "A04"
cluster: "A_ASR"
framework: "Whisper-MPS / PyTorch MPS"
model: "Whisper PyTorch checkpoint"
min_chip: "M2"
memory_required_gb: 16
expected_speed: "paste-time benchmark required; no number asserted"
benchmark_numbers: "none_self_run_none_vendor_claimed"
created_at: "2026-05-07"
---

# A04 — Whisper-MPS fork evaluation lane


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

## ScoutFlow alignment

[prompt-provided] U14 asks for a full Apple Silicon optimization encyclopedia for a one-person ScoutFlow prosumer workflow on a Mac M-series / Darwin 25.5.0 context, with an Apple M5 hypothesis that still needs hard local capture. The target lanes are ASR, embedding/retrieval, local LLM inference, image post-processing, video/audio preprocessing, system integration, monitoring, and resource management.

[post176-evidence] The uploaded post176 audit pack repeatedly says prior batches did not prove runtime unlock, vault true write, FFmpeg, ASR, browser automation, or `audio_transcript` approval. Therefore, U14 recipes are written as future unlock research. They deliberately preserve dry-run and fallback language even when the technical path is plausible.

[privacy-boundary] ScoutFlow inputs can include private audio, screenshots, generated images, unpublished notes, research hypotheses, and operator context. Cloud API substitution is not treated as an optimization in this pack; local-first processing with auditable provenance is the design center.

## Scenario

[recipe-spec] A fork or MPS-backed route can be useful only if it is maintained and output-compatible.

## Optimal local configuration

[recipe-spec] Treat any Whisper-MPS implementation as experimental. Capture repository or package identity, PyTorch MPS availability, exact checkpoint, output schema, and error behavior. Do not make it default until it beats the Metal baseline on quality and reliability.

[requires-local-verification] The local operator must verify three layers before treating this recipe as evidence: hardware identity, package identity, and model identity. Hardware identity includes chip, CPU core split, GPU core count, unified memory, display state, power source, and thermal state. Package identity includes binary path, package version, build flags, Python environment if any, and whether the backend is actually Metal, MPS, Core ML, ANE, VideoToolbox, Accelerate, or CPU. Model identity includes model path, hash, quantization, license note, and any conversion record.

## Benchmark contract

[requires-local-verification] No benchmark was run here. The table is a paste-time contract, not a result table.

| Metric | Required capture | Current value |
|---|---|---|
| import_success | paste-time measurement | no value included |
| mps_available | paste-time measurement | no value included |
| rtf | paste-time measurement | no value included |
| output_schema_match | paste-time measurement | no value included |
| failure_rate | paste-time measurement | no value included |
| input_hash | source fixture hash or manifest id | no value included |
| command_id | exact command, script revision, or git hash | no value included |
| model_hash | local model file hash or system model identity | no value included |
| package_version | exact package or binary version | no value included |
| power_source | battery or A/C | no value included |
| memory_pressure | normal/yellow/red if observable | no value included |
| thermal_state | normal/warm/throttled if observable | no value included |

## Command snippets

[recipe-spec] These commands are examples for a future local run. They were not executed by this pack.

```bash
python -c "import torch; print(torch.backends.mps.is_available())"
```

```bash
python run_whisper_mps_candidate.py --input fixture.wav
```

## Fallback ladder

[recipe-spec] Use this ladder in order. The first fallback preserves quality, the second preserves completion, and the final fallback preserves raw evidence for manual handling.

- whisper.cpp
- official CPU path
- faster-whisper CPU
- hold candidate

## Failure modes and observability

[requires-local-verification] Watch for missing acceleration despite an accelerator-labelled framework, memory pressure, swap growth, thermal throttling, output schema drift, invalid JSON, timestamp drift, segmentation mistakes, model load failure, package incompatibility, silent partial output, and ambiguous model licensing. Every derived artifact should point back to source hash, recipe id, command id, model identity, and downgrade flag.

## License, privacy, and data handling

[privacy-boundary] Verify fork license and maintenance status. Local artifacts may contain private research context. Raw media, transcripts, prompts, embeddings, thumbnails, masks, profile bundles, and generated derivatives stay local unless a separate privacy review explicitly approves sharing. Cloud API substitution is not recommended and is not approved as a replacement by this recipe.

## Watchlist note

[not-web-verified-2026] Fork freshness and compatibility are not web-verified.

## Acceptance gate

A future implementation can graduate this recipe only when the operator has pasted local hardware capture, package capture, model/license capture, benchmark log, quality review, fallback run evidence, rollback notes, and data-classification notes. Until those items exist, the status remains `candidate / not-authority`.

## Extended operating rationale — Whisper-MPS fork evaluation lane

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

