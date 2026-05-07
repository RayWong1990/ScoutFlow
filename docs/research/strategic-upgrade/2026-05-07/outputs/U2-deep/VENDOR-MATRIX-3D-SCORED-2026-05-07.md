---
title: VENDOR MATRIX 3D SCORED Deep Supplement 2026-05-07
status: candidate / vendor_matrix_3d_scored / not-authority
authority: not-authority
execution_approval: not-approved
runtime_approval: not-approved
migration_approval: not-approved
created_at: 2026-05-07
supplements: cloud-output-U2-phase-2-unlock-playbook-2026-05-07.zip
claim_label_policy: paragraph-level labels; command lines explicitly marked command-candidate
---

# VENDOR-MATRIX-3D-SCORED-2026-05-07

## §0 Source anchors / 输入锚点

[canonical-project-evidence] Overflow registry v0 keeps all five lanes in Hold and defines separate human gates: `true_write_approval`, `explicit_runtime_approval`, `visual_verdict`, `explicit_migration_approval`, and `usefulness_verdict`.

[canonical-project-evidence] T-P1A-021 says BBDown live metadata probe is only a future bounded dispatch; raw stdout, credentials, QR, auth sidecar, and URL parameters must stay local-only, and `PlatformResult` must not be emitted when preflight fails.

[canonical-project-evidence] T-P1A-022 says `audio_transcript`, ASR, ffmpeg, worker runtime, model download, and generated transcript artifacts remain blocked; future ASR must preserve raw evidence, segment provenance, timestamp integrity, and human review state.

[canonical-project-evidence] T-P1A-023 says every normalized claim / quote / topic must cite transcript segment provenance; LLM output without segment provenance is an untrusted draft, not a ScoutFlow knowledge artifact.

[canonical-project-evidence] T-P1A-025 says DB vNext is candidate-only, `artifact_assets` remains file authority, new structured tables must index / project artifacts rather than replace the ledger, and migration files remain out of scope.

[canonical-project-evidence] `services/api/scoutflow_api/bridge/config.py` returns `write_enabled=False` both when `SCOUTFLOW_VAULT_ROOT` is absent and when preview is available. This supplement preserves that invariant.

[limitation] Live web browsing is unavailable in this execution environment. The vendor refresh requested by the deep prompt is therefore not represented as live-verified evidence. All vendor status/cost scores are marked `[scoring-candidate]` or `[paste-time-unverified]` and require future live refresh before any dispatch.

## §1 Scoring rubric / 三维评分法

[scoring-candidate] This matrix upgrades the previous 40-row vendor table into a numeric risk × cost × quality view. It is not vendor selection and not vendor approval.

[scoring-candidate] `risk_score` is 1-5 where 5 means highest legal / operational / platform-pressure risk. `cost_per_1k_capture_usd_est` is a rough envelope, not live price. `quality_score` is 1-5 where 5 means strongest expected output for the lane. `legal_posture` is a compact qualitative label. `sandboxability_score` is 1-5 where 5 means easier to test in repo-external sandbox without touching production or secrets.

[limitation] Live web refresh was requested, but the environment cannot browse live web. Therefore every row has `live_verified=false`. Any future dispatch must refresh price, ToS, release, CVE, benchmark, and legal posture before using a vendor in practice.

[boundary] Numeric scores are triage aids. A high `quality_score` does not imply adoption. A low `risk_score` does not imply unlock. A low cost estimate does not imply the user accepts the vendor.

## §2 3D scored matrix

| ID | Vendor | Lane | Role | risk_score | cost_per_1k_capture_usd_est | quality_score | legal_posture | sandboxability_score | live_verified | score rationale |
|---|---|---|---|---:|---:|---:|---|---:|---|---|
| V01 | [evaluation-candidate] BBDown -info | Lane-2a | Bilibili metadata CLI | 5 | 0.0 | 3.6 | high / CN platform / C&D-sensitive | 3 | false | [paste-time-unverified] CN platform pressure; media-adjacent; parser drift risk. Future live refresh required before dispatch. |
| V02 | [evaluation-candidate] BiliFix vxbilibili.com | Lane-2a | oEmbed / link preview shim | 3 | 0.0 | 2.7 | medium / third-party shim | 4 | false | [paste-time-unverified] Third-party metadata shim; availability and ToS uncertain. Future live refresh required before dispatch. |
| V03 | [evaluation-candidate] bilibili-API-collect | Lane-2a | API documentation reference | 5 | 0.0 | 3.2 | high / Bilibili legal pressure | 2 | false | [paste-time-unverified] Known warning-letter pressure in prompt evidence. Future live refresh required before dispatch. |
| V04 | [evaluation-candidate] bilibili-embed | Lane-2a | embed metadata reference | 3 | 0.0 | 2.4 | medium / drift-sensitive | 3 | false | [paste-time-unverified] Maintainer notes platform API drift. Future live refresh required before dispatch. |
| V05 | [evaluation-candidate] Apify Bilibili Search MCP | Lane-2a | commercial metadata scraper | 4 | 250.0 | 3.4 | medium-high / commercial scraping | 4 | false | [paste-time-unverified] Commercial scraper ToS and pricing require live refresh. Future live refresh required before dispatch. |
| V06 | [evaluation-candidate] Apify Bilibili Downloader | Lane-2a | commercial downloader | 5 | 350.0 | 3.8 | high / media download adjacent | 2 | false | [paste-time-unverified] Downloader framing increases media-rights risk. Future live refresh required before dispatch. |
| V07 | [evaluation-candidate] Bright Data Web Unlocker Bilibili | Lane-2a | commercial proxy/unlocker | 5 | 500.0 | 3.6 | high / proxy + scraping | 3 | false | [paste-time-unverified] Proxy usage can conflict with platform anti-abuse policy. Future live refresh required before dispatch. |
| V08 | [evaluation-candidate] LangChain Bilibili integration | Lane-2a | transcript integration via cookies | 4 | 20.0 | 3.0 | medium-high / auth-sensitive | 2 | false | [paste-time-unverified] Cookie sidecar and transcript access risks. Future live refresh required before dispatch. |
| V09 | [evaluation-candidate] Bilibili MCP Server | Lane-2a | MCP search/info wrapper | 4 | 0.0 | 2.8 | medium-high / MCP wrapper | 3 | false | [paste-time-unverified] Wrapper inherits platform/API drift. Future live refresh required before dispatch. |
| V10 | [evaluation-candidate] yt-dlp metadata-only | Lane-2b | metadata extraction with skip_download | 3 | 0.0 | 4.0 | medium / jurisdiction dependent | 4 | false | [paste-time-unverified] Generally safer than media download but must refresh legal/CVE status. Future live refresh required before dispatch. |
| V11 | [evaluation-candidate] yt-dlp with Bright Data unlocker | Lane-2b | region-locked metadata path | 5 | 500.0 | 4.1 | high / proxy + geo-sensitive | 2 | false | [paste-time-unverified] Proxy + region workflow raises legal/ToS complexity. Future live refresh required before dispatch. |
| V12 | [evaluation-candidate] ffmpeg | Lane-2c | audio normalization/extraction toolchain | 3 | 0.0 | 4.8 | medium / input-rights dependent | 5 | false | [paste-time-unverified] Technically mature; legal risk depends on source media rights. Future live refresh required before dispatch. |
| V13 | [evaluation-candidate] OpenAI Whisper large-v3-turbo | Lane-2d | ASR engine | 2 | 0.0 | 4.3 | low-medium / local model | 4 | false | [paste-time-unverified] Model use safer; transcript hallucination and resource cost remain. Future live refresh required before dispatch. |
| V14 | [evaluation-candidate] faster-whisper | Lane-2d | CTranslate2 Whisper runtime | 2 | 0.0 | 4.4 | low-medium / local runtime | 5 | false | [paste-time-unverified] Mature local runtime; model cache and GPU behavior need spike. Future live refresh required before dispatch. |
| V15 | [evaluation-candidate] WhisperKit | Lane-2d | CoreML/Apple Silicon Whisper | 2 | 0.0 | 4.1 | low-medium / local Apple path | 4 | false | [paste-time-unverified] Apple-specific; packaging drift needs validation. Future live refresh required before dispatch. |
| V16 | [evaluation-candidate] mlx-whisper | Lane-2d | MLX Apple runtime | 2 | 0.0 | 4.0 | low-medium / local Apple path | 4 | false | [paste-time-unverified] Apple Silicon quality/speed candidate; memory profile unknown here. Future live refresh required before dispatch. |
| V17 | [evaluation-candidate] whisper.cpp | Lane-2d | portable C/C++ Whisper | 2 | 0.0 | 3.9 | low-medium / local runtime | 5 | false | [paste-time-unverified] Mature, low-dependency path; quality depends model quantization. Future live refresh required before dispatch. |
| V18 | [evaluation-candidate] NVIDIA Parakeet v3 / TDT 0.6B | Lane-2d | ASR engine | 2 | 0.0 | 4.2 | low-medium / local model | 3 | false | [paste-time-unverified] Prompt evidence suggests strong ASR; local memory and ecosystem uncertainty. Future live refresh required before dispatch. |
| V19 | [evaluation-candidate] parakeet-mlx / parakeet.cpp | Lane-2d | Apple native Parakeet path | 2 | 0.0 | 4.0 | low-medium / local Apple path | 3 | false | [paste-time-unverified] Promising but needs actual local benchmark. Future live refresh required before dispatch. |
| V20 | [evaluation-candidate] FluidAudio Swift SDK | Lane-2d | CoreML/Neural Engine ASR wrapper | 2 | 0.0 | 3.8 | low-medium / local SDK | 3 | false | [paste-time-unverified] Native packaging path; requires Apple dev spike. Future live refresh required before dispatch. |
| V21 | [evaluation-candidate] Voxtral Mini 4B Realtime | Lane-2d | streaming ASR/audio LLM | 3 | 0.0 | 3.7 | medium / model-runtime risk | 2 | false | [paste-time-unverified] Higher memory and emerging runtime risk. Future live refresh required before dispatch. |
| V22 | [evaluation-candidate] Apple Foundation Models | Lane-2d/Lane-5 | on-device model framework | 2 | 0.0 | 3.4 | low-medium / on-device privacy | 3 | false | [paste-time-unverified] No live refresh here; availability/API constraints need check. Future live refresh required before dispatch. |
| V23 | [evaluation-candidate] Paraformer / FunASR | Lane-2d | Chinese ASR option | 2 | 0.0 | 3.8 | low-medium / local model | 3 | false | [paste-time-unverified] Good Chinese fit; model/runtime validation needed. Future live refresh required before dispatch. |
| V24 | [evaluation-candidate] 通义听悟 | Lane-2d | commercial Chinese ASR | 3 | 180.0 | 4.0 | medium / cloud ASR CN | 4 | false | [paste-time-unverified] Cloud processing, cost, privacy, ToS require review. Future live refresh required before dispatch. |
| V25 | [evaluation-candidate] 讯飞听见 / iFlytek ASR | Lane-2d | commercial Chinese ASR | 3 | 220.0 | 4.0 | medium / cloud ASR CN | 4 | false | [paste-time-unverified] Cloud processing, data residency, cost require review. Future live refresh required before dispatch. |
| V26 | [evaluation-candidate] Apify XHS Scraper | Lane-2/XHS outlook | commercial XHS scraper | 5 | 300.0 | 3.4 | high / XHS anti-scraping | 3 | false | [paste-time-unverified] No official API and anti-scraping pressure. Future live refresh required before dispatch. |
| V27 | [evaluation-candidate] Bright Data XHS | Lane-2/XHS outlook | commercial XHS proxy/scraper | 5 | 600.0 | 3.7 | high / proxy + anti-scraping | 3 | false | [paste-time-unverified] Residential proxy reliance increases risk. Future live refresh required before dispatch. |
| V28 | [evaluation-candidate] MediaCrawler | Lane-2/XHS outlook | open-source XHS crawler | 5 | 0.0 | 3.0 | high / anti-scraping | 2 | false | [paste-time-unverified] Open-source crawler likely brittle and ToS-sensitive. Future live refresh required before dispatch. |
| V29 | [evaluation-candidate] ScraperAPI | Lane-2/XHS outlook | generic web unlocker | 4 | 350.0 | 3.1 | medium-high / generic proxy | 3 | false | [paste-time-unverified] Platform ToS and proxy-risk need live review. Future live refresh required before dispatch. |
| V30 | [evaluation-candidate] Playwright | Lane-3 | browser automation framework | 2 | 0.0 | 4.8 | low-medium / localhost visual only | 5 | false | [paste-time-unverified] Technically strong; must avoid default execution. Future live refresh required before dispatch. |
| V31 | [evaluation-candidate] Selenium | Lane-3 | legacy browser automation | 2 | 0.0 | 4.0 | low-medium / localhost visual only | 4 | false | [paste-time-unverified] Stable but heavier/flakier. Future live refresh required before dispatch. |
| V32 | [evaluation-candidate] Puppeteer | Lane-3 | Chrome automation | 2 | 0.0 | 4.2 | low-medium / localhost visual only | 4 | false | [paste-time-unverified] Chrome-centric but mature. Future live refresh required before dispatch. |
| V33 | [evaluation-candidate] Stagehand | Lane-3 | AI browser action layer | 3 | 120.0 | 3.6 | medium / agentic action risk | 2 | false | [paste-time-unverified] Agentic action risk and vendor dependency. Future live refresh required before dispatch. |
| V34 | [evaluation-candidate] browser-use | Lane-3 | agentic browser automation | 4 | 80.0 | 3.5 | medium-high / agentic action risk | 2 | false | [paste-time-unverified] Agentic autonomy raises action-overreach risk. Future live refresh required before dispatch. |
| V35 | [evaluation-candidate] Claude computer use | Lane-3 | AI computer/browser control | 4 | 200.0 | 3.6 | medium-high / computer-use risk | 2 | false | [paste-time-unverified] Powerful but high operator-control risk. Future live refresh required before dispatch. |
| V36 | [evaluation-candidate] Alembic | Lane-4 | Python migration tool | 2 | 0.0 | 4.5 | low-medium / migration governance | 4 | false | [paste-time-unverified] Mature; risk is governance not tool. Future live refresh required before dispatch. |
| V37 | [evaluation-candidate] Diesel migrations | Lane-4 | Rust migration tool | 2 | 0.0 | 3.7 | low-medium / stack fit risk | 3 | false | [paste-time-unverified] Mature; stack mismatch possible. Future live refresh required before dispatch. |
| V38 | [evaluation-candidate] sqlx migrate | Lane-4 | Rust/SQLx migration tool | 2 | 0.0 | 3.7 | low-medium / stack fit risk | 3 | false | [paste-time-unverified] Mature; stack mismatch possible. Future live refresh required before dispatch. |
| V39 | [evaluation-candidate] SQLite FTS5 | Lane-5 | local-first search index | 1 | 0.0 | 3.8 | low / local-only | 5 | false | [paste-time-unverified] Local and mature; ranking quality limited. Future live refresh required before dispatch. |
| V40 | [evaluation-candidate] Local embeddings + MCP | Lane-5 | local-first signal stack | 2 | 0.0 | 4.0 | low-medium / local model | 4 | false | [paste-time-unverified] Private but model quality/storage needs spike. Future live refresh required before dispatch. |

## §3 Matrix interpretation / 如何读分

[scoring-candidate] Lane-2 has the highest variance. Local ASR engines score better on sandboxability because they can be tested on synthetic audio without platform calls, while Bilibili/XHS scrapers score worse because they are platform-pressure sensitive and can drift or trigger anti-abuse controls.

[scoring-candidate] Lane-3 browser frameworks have strong technical quality but only when the target is localhost and the browser profile is isolated. Agentic action frameworks receive lower sandboxability because the failure mode is no longer just “test flake”; it can become unintended action execution.

[scoring-candidate] Lane-4 migration tools are technically mature, but the main risk is governance: accidental production migration, incompatible schema authority, or a generated migration file outside explicit user approval. A mature migration tool can still be dangerous inside the wrong dispatch boundary.

[scoring-candidate] Lane-5 local-first tools have low direct cost and good privacy posture, but quality depends on evidence grounding. A signal workbench score without segment/claim/quote provenance is not trustworthy, even if the ranking algorithm appears useful.

## §4 Vendor-neutral decision frame

[decision-candidate] For every lane, choose a vendor only after four gates: local sandbox proof, legal/ToS refresh, cost refresh, and human verdict. This supplement deliberately avoids “default vendor” language.

[decision-candidate] Vendor diversification matters most in Bilibili/XHS capture. It matters less for local SQLite/FTS because local-first infrastructure is less subject to third-party API drift.

[decision-candidate] The safest first measurement is not vendor quality; it is sandboxability. A vendor that cannot be safely tested without touching production, secrets, or real user data should be deferred even if the expected quality is high.

## §5 Required future live-refresh query list

[live-refresh-required] Future operator should search at least: Bilibili cease-and-desist follow-up, BiliFix availability, bilibili-API-collect maintainer notices, Apify Bilibili pricing, Bright Data Bilibili pricing, yt-dlp release/CVE advisories, yt-dlp legal DMCA/EU status, ffmpeg security advisories, Whisper large-v3-turbo release/benchmarks, faster-whisper release notes, WhisperKit releases, mlx-whisper releases, whisper.cpp releases, Parakeet v3/TDT release notes, parakeet.cpp release notes, FluidAudio SDK releases, Voxtral Mini realtime docs, Apple Foundation Models updates, XHS official API status, Apify XHS pricing, Bright Data XHS pricing, MediaCrawler maintenance status, Playwright releases, Selenium releases, Puppeteer releases, Stagehand releases, browser-use releases, Temporal durable execution releases, Paraformer/FunASR releases, 通义听悟 pricing, and iFlytek ASR pricing.

[live-refresh-required] A future refresh should add exact URL, publication date, access date, price page snapshot, license, ToS excerpt, CVE/advisory status, and benchmark context. Without those, this matrix remains score-candidate only.

## §6 Scoring caveats

[limitation] Cost estimates are rough planning envelopes. Commercial scraping/ASR prices can change, may include minimum subscription, and may depend on region, proxy bandwidth, concurrency, data retention, or usage tier.

[limitation] Quality scores are expected utility scores, not benchmark claims. Because live benchmark refresh is unavailable, this file does not assert current WER, latency, release date, or CVE state beyond the project prompt evidence.

[limitation] Legal posture is not legal advice. It is a product-risk label for deciding whether a future dispatch needs counsel review or more conservative vendor diversification.


## §7 Per-vendor follow-up notes

### V01 BBDown -info

[follow-up-candidate] `BBDown -info` is scored for `Lane-2a` as `Bilibili metadata CLI`. The current numeric row is a planning estimate only; live release, price, ToS, CVE, and benchmark evidence were not refreshed in this execution.

[follow-up-candidate] Risk rationale: CN platform pressure; media-adjacent; parser drift risk. This creates a review priority of `urgent legal/runtime review`.

[follow-up-candidate] Cost/quality posture: estimated cost per 1k captures is `0.0` USD envelope and quality score is `3.6`. These values should be recalculated after future web evidence refresh and before dispatch drafting.

[follow-up-candidate] Sandbox posture: sandboxability score `3` means the future spike should start with synthetic fixtures and no real platform call. No row is an adoption decision.

### V02 BiliFix vxbilibili.com

[follow-up-candidate] `BiliFix vxbilibili.com` is scored for `Lane-2a` as `oEmbed / link preview shim`. The current numeric row is a planning estimate only; live release, price, ToS, CVE, and benchmark evidence were not refreshed in this execution.

[follow-up-candidate] Risk rationale: Third-party metadata shim; availability and ToS uncertain. This creates a review priority of `conservative review`.

[follow-up-candidate] Cost/quality posture: estimated cost per 1k captures is `0.0` USD envelope and quality score is `2.7`. These values should be recalculated after future web evidence refresh and before dispatch drafting.

[follow-up-candidate] Sandbox posture: sandboxability score `4` means the future spike should be able to start with local/temp fixtures and read-only preflight. No row is an adoption decision.

### V03 bilibili-API-collect

[follow-up-candidate] `bilibili-API-collect` is scored for `Lane-2a` as `API documentation reference`. The current numeric row is a planning estimate only; live release, price, ToS, CVE, and benchmark evidence were not refreshed in this execution.

[follow-up-candidate] Risk rationale: Known warning-letter pressure in prompt evidence. This creates a review priority of `urgent legal/runtime review`.

[follow-up-candidate] Cost/quality posture: estimated cost per 1k captures is `0.0` USD envelope and quality score is `3.2`. These values should be recalculated after future web evidence refresh and before dispatch drafting.

[follow-up-candidate] Sandbox posture: sandboxability score `2` means the future spike should start with synthetic fixtures and no real platform call. No row is an adoption decision.

### V04 bilibili-embed

[follow-up-candidate] `bilibili-embed` is scored for `Lane-2a` as `embed metadata reference`. The current numeric row is a planning estimate only; live release, price, ToS, CVE, and benchmark evidence were not refreshed in this execution.

[follow-up-candidate] Risk rationale: Maintainer notes platform API drift. This creates a review priority of `conservative review`.

[follow-up-candidate] Cost/quality posture: estimated cost per 1k captures is `0.0` USD envelope and quality score is `2.4`. These values should be recalculated after future web evidence refresh and before dispatch drafting.

[follow-up-candidate] Sandbox posture: sandboxability score `3` means the future spike should start with synthetic fixtures and no real platform call. No row is an adoption decision.

### V05 Apify Bilibili Search MCP

[follow-up-candidate] `Apify Bilibili Search MCP` is scored for `Lane-2a` as `commercial metadata scraper`. The current numeric row is a planning estimate only; live release, price, ToS, CVE, and benchmark evidence were not refreshed in this execution.

[follow-up-candidate] Risk rationale: Commercial scraper ToS and pricing require live refresh. This creates a review priority of `conservative review`.

[follow-up-candidate] Cost/quality posture: estimated cost per 1k captures is `250.0` USD envelope and quality score is `3.4`. These values should be recalculated after future web evidence refresh and before dispatch drafting.

[follow-up-candidate] Sandbox posture: sandboxability score `4` means the future spike should be able to start with local/temp fixtures and read-only preflight. No row is an adoption decision.

### V06 Apify Bilibili Downloader

[follow-up-candidate] `Apify Bilibili Downloader` is scored for `Lane-2a` as `commercial downloader`. The current numeric row is a planning estimate only; live release, price, ToS, CVE, and benchmark evidence were not refreshed in this execution.

[follow-up-candidate] Risk rationale: Downloader framing increases media-rights risk. This creates a review priority of `urgent legal/runtime review`.

[follow-up-candidate] Cost/quality posture: estimated cost per 1k captures is `350.0` USD envelope and quality score is `3.8`. These values should be recalculated after future web evidence refresh and before dispatch drafting.

[follow-up-candidate] Sandbox posture: sandboxability score `2` means the future spike should start with synthetic fixtures and no real platform call. No row is an adoption decision.

### V07 Bright Data Web Unlocker Bilibili

[follow-up-candidate] `Bright Data Web Unlocker Bilibili` is scored for `Lane-2a` as `commercial proxy/unlocker`. The current numeric row is a planning estimate only; live release, price, ToS, CVE, and benchmark evidence were not refreshed in this execution.

[follow-up-candidate] Risk rationale: Proxy usage can conflict with platform anti-abuse policy. This creates a review priority of `urgent legal/runtime review`.

[follow-up-candidate] Cost/quality posture: estimated cost per 1k captures is `500.0` USD envelope and quality score is `3.6`. These values should be recalculated after future web evidence refresh and before dispatch drafting.

[follow-up-candidate] Sandbox posture: sandboxability score `3` means the future spike should start with synthetic fixtures and no real platform call. No row is an adoption decision.

### V08 LangChain Bilibili integration

[follow-up-candidate] `LangChain Bilibili integration` is scored for `Lane-2a` as `transcript integration via cookies`. The current numeric row is a planning estimate only; live release, price, ToS, CVE, and benchmark evidence were not refreshed in this execution.

[follow-up-candidate] Risk rationale: Cookie sidecar and transcript access risks. This creates a review priority of `conservative review`.

[follow-up-candidate] Cost/quality posture: estimated cost per 1k captures is `20.0` USD envelope and quality score is `3.0`. These values should be recalculated after future web evidence refresh and before dispatch drafting.

[follow-up-candidate] Sandbox posture: sandboxability score `2` means the future spike should start with synthetic fixtures and no real platform call. No row is an adoption decision.

### V09 Bilibili MCP Server

[follow-up-candidate] `Bilibili MCP Server` is scored for `Lane-2a` as `MCP search/info wrapper`. The current numeric row is a planning estimate only; live release, price, ToS, CVE, and benchmark evidence were not refreshed in this execution.

[follow-up-candidate] Risk rationale: Wrapper inherits platform/API drift. This creates a review priority of `conservative review`.

[follow-up-candidate] Cost/quality posture: estimated cost per 1k captures is `0.0` USD envelope and quality score is `2.8`. These values should be recalculated after future web evidence refresh and before dispatch drafting.

[follow-up-candidate] Sandbox posture: sandboxability score `3` means the future spike should start with synthetic fixtures and no real platform call. No row is an adoption decision.

### V10 yt-dlp metadata-only

[follow-up-candidate] `yt-dlp metadata-only` is scored for `Lane-2b` as `metadata extraction with skip_download`. The current numeric row is a planning estimate only; live release, price, ToS, CVE, and benchmark evidence were not refreshed in this execution.

[follow-up-candidate] Risk rationale: Generally safer than media download but must refresh legal/CVE status. This creates a review priority of `conservative review`.

[follow-up-candidate] Cost/quality posture: estimated cost per 1k captures is `0.0` USD envelope and quality score is `4.0`. These values should be recalculated after future web evidence refresh and before dispatch drafting.

[follow-up-candidate] Sandbox posture: sandboxability score `4` means the future spike should be able to start with local/temp fixtures and read-only preflight. No row is an adoption decision.

### V11 yt-dlp with Bright Data unlocker

[follow-up-candidate] `yt-dlp with Bright Data unlocker` is scored for `Lane-2b` as `region-locked metadata path`. The current numeric row is a planning estimate only; live release, price, ToS, CVE, and benchmark evidence were not refreshed in this execution.

[follow-up-candidate] Risk rationale: Proxy + region workflow raises legal/ToS complexity. This creates a review priority of `urgent legal/runtime review`.

[follow-up-candidate] Cost/quality posture: estimated cost per 1k captures is `500.0` USD envelope and quality score is `4.1`. These values should be recalculated after future web evidence refresh and before dispatch drafting.

[follow-up-candidate] Sandbox posture: sandboxability score `2` means the future spike should start with synthetic fixtures and no real platform call. No row is an adoption decision.

### V12 ffmpeg

[follow-up-candidate] `ffmpeg` is scored for `Lane-2c` as `audio normalization/extraction toolchain`. The current numeric row is a planning estimate only; live release, price, ToS, CVE, and benchmark evidence were not refreshed in this execution.

[follow-up-candidate] Risk rationale: Technically mature; legal risk depends on source media rights. This creates a review priority of `conservative review`.

[follow-up-candidate] Cost/quality posture: estimated cost per 1k captures is `0.0` USD envelope and quality score is `4.8`. These values should be recalculated after future web evidence refresh and before dispatch drafting.

[follow-up-candidate] Sandbox posture: sandboxability score `5` means the future spike should be able to start with local/temp fixtures and read-only preflight. No row is an adoption decision.

### V13 OpenAI Whisper large-v3-turbo

[follow-up-candidate] `OpenAI Whisper large-v3-turbo` is scored for `Lane-2d` as `ASR engine`. The current numeric row is a planning estimate only; live release, price, ToS, CVE, and benchmark evidence were not refreshed in this execution.

[follow-up-candidate] Risk rationale: Model use safer; transcript hallucination and resource cost remain. This creates a review priority of `standard sandbox review`.

[follow-up-candidate] Cost/quality posture: estimated cost per 1k captures is `0.0` USD envelope and quality score is `4.3`. These values should be recalculated after future web evidence refresh and before dispatch drafting.

[follow-up-candidate] Sandbox posture: sandboxability score `4` means the future spike should be able to start with local/temp fixtures and read-only preflight. No row is an adoption decision.

### V14 faster-whisper

[follow-up-candidate] `faster-whisper` is scored for `Lane-2d` as `CTranslate2 Whisper runtime`. The current numeric row is a planning estimate only; live release, price, ToS, CVE, and benchmark evidence were not refreshed in this execution.

[follow-up-candidate] Risk rationale: Mature local runtime; model cache and GPU behavior need spike. This creates a review priority of `standard sandbox review`.

[follow-up-candidate] Cost/quality posture: estimated cost per 1k captures is `0.0` USD envelope and quality score is `4.4`. These values should be recalculated after future web evidence refresh and before dispatch drafting.

[follow-up-candidate] Sandbox posture: sandboxability score `5` means the future spike should be able to start with local/temp fixtures and read-only preflight. No row is an adoption decision.

### V15 WhisperKit

[follow-up-candidate] `WhisperKit` is scored for `Lane-2d` as `CoreML/Apple Silicon Whisper`. The current numeric row is a planning estimate only; live release, price, ToS, CVE, and benchmark evidence were not refreshed in this execution.

[follow-up-candidate] Risk rationale: Apple-specific; packaging drift needs validation. This creates a review priority of `standard sandbox review`.

[follow-up-candidate] Cost/quality posture: estimated cost per 1k captures is `0.0` USD envelope and quality score is `4.1`. These values should be recalculated after future web evidence refresh and before dispatch drafting.

[follow-up-candidate] Sandbox posture: sandboxability score `4` means the future spike should be able to start with local/temp fixtures and read-only preflight. No row is an adoption decision.

### V16 mlx-whisper

[follow-up-candidate] `mlx-whisper` is scored for `Lane-2d` as `MLX Apple runtime`. The current numeric row is a planning estimate only; live release, price, ToS, CVE, and benchmark evidence were not refreshed in this execution.

[follow-up-candidate] Risk rationale: Apple Silicon quality/speed candidate; memory profile unknown here. This creates a review priority of `standard sandbox review`.

[follow-up-candidate] Cost/quality posture: estimated cost per 1k captures is `0.0` USD envelope and quality score is `4.0`. These values should be recalculated after future web evidence refresh and before dispatch drafting.

[follow-up-candidate] Sandbox posture: sandboxability score `4` means the future spike should be able to start with local/temp fixtures and read-only preflight. No row is an adoption decision.

### V17 whisper.cpp

[follow-up-candidate] `whisper.cpp` is scored for `Lane-2d` as `portable C/C++ Whisper`. The current numeric row is a planning estimate only; live release, price, ToS, CVE, and benchmark evidence were not refreshed in this execution.

[follow-up-candidate] Risk rationale: Mature, low-dependency path; quality depends model quantization. This creates a review priority of `standard sandbox review`.

[follow-up-candidate] Cost/quality posture: estimated cost per 1k captures is `0.0` USD envelope and quality score is `3.9`. These values should be recalculated after future web evidence refresh and before dispatch drafting.

[follow-up-candidate] Sandbox posture: sandboxability score `5` means the future spike should be able to start with local/temp fixtures and read-only preflight. No row is an adoption decision.

### V18 NVIDIA Parakeet v3 / TDT 0.6B

[follow-up-candidate] `NVIDIA Parakeet v3 / TDT 0.6B` is scored for `Lane-2d` as `ASR engine`. The current numeric row is a planning estimate only; live release, price, ToS, CVE, and benchmark evidence were not refreshed in this execution.

[follow-up-candidate] Risk rationale: Prompt evidence suggests strong ASR; local memory and ecosystem uncertainty. This creates a review priority of `standard sandbox review`.

[follow-up-candidate] Cost/quality posture: estimated cost per 1k captures is `0.0` USD envelope and quality score is `4.2`. These values should be recalculated after future web evidence refresh and before dispatch drafting.

[follow-up-candidate] Sandbox posture: sandboxability score `3` means the future spike should start with synthetic fixtures and no real platform call. No row is an adoption decision.

### V19 parakeet-mlx / parakeet.cpp

[follow-up-candidate] `parakeet-mlx / parakeet.cpp` is scored for `Lane-2d` as `Apple native Parakeet path`. The current numeric row is a planning estimate only; live release, price, ToS, CVE, and benchmark evidence were not refreshed in this execution.

[follow-up-candidate] Risk rationale: Promising but needs actual local benchmark. This creates a review priority of `standard sandbox review`.

[follow-up-candidate] Cost/quality posture: estimated cost per 1k captures is `0.0` USD envelope and quality score is `4.0`. These values should be recalculated after future web evidence refresh and before dispatch drafting.

[follow-up-candidate] Sandbox posture: sandboxability score `3` means the future spike should start with synthetic fixtures and no real platform call. No row is an adoption decision.

### V20 FluidAudio Swift SDK

[follow-up-candidate] `FluidAudio Swift SDK` is scored for `Lane-2d` as `CoreML/Neural Engine ASR wrapper`. The current numeric row is a planning estimate only; live release, price, ToS, CVE, and benchmark evidence were not refreshed in this execution.

[follow-up-candidate] Risk rationale: Native packaging path; requires Apple dev spike. This creates a review priority of `standard sandbox review`.

[follow-up-candidate] Cost/quality posture: estimated cost per 1k captures is `0.0` USD envelope and quality score is `3.8`. These values should be recalculated after future web evidence refresh and before dispatch drafting.

[follow-up-candidate] Sandbox posture: sandboxability score `3` means the future spike should start with synthetic fixtures and no real platform call. No row is an adoption decision.

### V21 Voxtral Mini 4B Realtime

[follow-up-candidate] `Voxtral Mini 4B Realtime` is scored for `Lane-2d` as `streaming ASR/audio LLM`. The current numeric row is a planning estimate only; live release, price, ToS, CVE, and benchmark evidence were not refreshed in this execution.

[follow-up-candidate] Risk rationale: Higher memory and emerging runtime risk. This creates a review priority of `conservative review`.

[follow-up-candidate] Cost/quality posture: estimated cost per 1k captures is `0.0` USD envelope and quality score is `3.7`. These values should be recalculated after future web evidence refresh and before dispatch drafting.

[follow-up-candidate] Sandbox posture: sandboxability score `2` means the future spike should start with synthetic fixtures and no real platform call. No row is an adoption decision.

### V22 Apple Foundation Models

[follow-up-candidate] `Apple Foundation Models` is scored for `Lane-2d/Lane-5` as `on-device model framework`. The current numeric row is a planning estimate only; live release, price, ToS, CVE, and benchmark evidence were not refreshed in this execution.

[follow-up-candidate] Risk rationale: No live refresh here; availability/API constraints need check. This creates a review priority of `standard sandbox review`.

[follow-up-candidate] Cost/quality posture: estimated cost per 1k captures is `0.0` USD envelope and quality score is `3.4`. These values should be recalculated after future web evidence refresh and before dispatch drafting.

[follow-up-candidate] Sandbox posture: sandboxability score `3` means the future spike should start with synthetic fixtures and no real platform call. No row is an adoption decision.

### V23 Paraformer / FunASR

[follow-up-candidate] `Paraformer / FunASR` is scored for `Lane-2d` as `Chinese ASR option`. The current numeric row is a planning estimate only; live release, price, ToS, CVE, and benchmark evidence were not refreshed in this execution.

[follow-up-candidate] Risk rationale: Good Chinese fit; model/runtime validation needed. This creates a review priority of `standard sandbox review`.

[follow-up-candidate] Cost/quality posture: estimated cost per 1k captures is `0.0` USD envelope and quality score is `3.8`. These values should be recalculated after future web evidence refresh and before dispatch drafting.

[follow-up-candidate] Sandbox posture: sandboxability score `3` means the future spike should start with synthetic fixtures and no real platform call. No row is an adoption decision.

### V24 通义听悟

[follow-up-candidate] `通义听悟` is scored for `Lane-2d` as `commercial Chinese ASR`. The current numeric row is a planning estimate only; live release, price, ToS, CVE, and benchmark evidence were not refreshed in this execution.

[follow-up-candidate] Risk rationale: Cloud processing, cost, privacy, ToS require review. This creates a review priority of `conservative review`.

[follow-up-candidate] Cost/quality posture: estimated cost per 1k captures is `180.0` USD envelope and quality score is `4.0`. These values should be recalculated after future web evidence refresh and before dispatch drafting.

[follow-up-candidate] Sandbox posture: sandboxability score `4` means the future spike should be able to start with local/temp fixtures and read-only preflight. No row is an adoption decision.

### V25 讯飞听见 / iFlytek ASR

[follow-up-candidate] `讯飞听见 / iFlytek ASR` is scored for `Lane-2d` as `commercial Chinese ASR`. The current numeric row is a planning estimate only; live release, price, ToS, CVE, and benchmark evidence were not refreshed in this execution.

[follow-up-candidate] Risk rationale: Cloud processing, data residency, cost require review. This creates a review priority of `conservative review`.

[follow-up-candidate] Cost/quality posture: estimated cost per 1k captures is `220.0` USD envelope and quality score is `4.0`. These values should be recalculated after future web evidence refresh and before dispatch drafting.

[follow-up-candidate] Sandbox posture: sandboxability score `4` means the future spike should be able to start with local/temp fixtures and read-only preflight. No row is an adoption decision.

### V26 Apify XHS Scraper

[follow-up-candidate] `Apify XHS Scraper` is scored for `Lane-2/XHS outlook` as `commercial XHS scraper`. The current numeric row is a planning estimate only; live release, price, ToS, CVE, and benchmark evidence were not refreshed in this execution.

[follow-up-candidate] Risk rationale: No official API and anti-scraping pressure. This creates a review priority of `urgent legal/runtime review`.

[follow-up-candidate] Cost/quality posture: estimated cost per 1k captures is `300.0` USD envelope and quality score is `3.4`. These values should be recalculated after future web evidence refresh and before dispatch drafting.

[follow-up-candidate] Sandbox posture: sandboxability score `3` means the future spike should start with synthetic fixtures and no real platform call. No row is an adoption decision.

### V27 Bright Data XHS

[follow-up-candidate] `Bright Data XHS` is scored for `Lane-2/XHS outlook` as `commercial XHS proxy/scraper`. The current numeric row is a planning estimate only; live release, price, ToS, CVE, and benchmark evidence were not refreshed in this execution.

[follow-up-candidate] Risk rationale: Residential proxy reliance increases risk. This creates a review priority of `urgent legal/runtime review`.

[follow-up-candidate] Cost/quality posture: estimated cost per 1k captures is `600.0` USD envelope and quality score is `3.7`. These values should be recalculated after future web evidence refresh and before dispatch drafting.

[follow-up-candidate] Sandbox posture: sandboxability score `3` means the future spike should start with synthetic fixtures and no real platform call. No row is an adoption decision.

### V28 MediaCrawler

[follow-up-candidate] `MediaCrawler` is scored for `Lane-2/XHS outlook` as `open-source XHS crawler`. The current numeric row is a planning estimate only; live release, price, ToS, CVE, and benchmark evidence were not refreshed in this execution.

[follow-up-candidate] Risk rationale: Open-source crawler likely brittle and ToS-sensitive. This creates a review priority of `urgent legal/runtime review`.

[follow-up-candidate] Cost/quality posture: estimated cost per 1k captures is `0.0` USD envelope and quality score is `3.0`. These values should be recalculated after future web evidence refresh and before dispatch drafting.

[follow-up-candidate] Sandbox posture: sandboxability score `2` means the future spike should start with synthetic fixtures and no real platform call. No row is an adoption decision.

### V29 ScraperAPI

[follow-up-candidate] `ScraperAPI` is scored for `Lane-2/XHS outlook` as `generic web unlocker`. The current numeric row is a planning estimate only; live release, price, ToS, CVE, and benchmark evidence were not refreshed in this execution.

[follow-up-candidate] Risk rationale: Platform ToS and proxy-risk need live review. This creates a review priority of `conservative review`.

[follow-up-candidate] Cost/quality posture: estimated cost per 1k captures is `350.0` USD envelope and quality score is `3.1`. These values should be recalculated after future web evidence refresh and before dispatch drafting.

[follow-up-candidate] Sandbox posture: sandboxability score `3` means the future spike should start with synthetic fixtures and no real platform call. No row is an adoption decision.

### V30 Playwright

[follow-up-candidate] `Playwright` is scored for `Lane-3` as `browser automation framework`. The current numeric row is a planning estimate only; live release, price, ToS, CVE, and benchmark evidence were not refreshed in this execution.

[follow-up-candidate] Risk rationale: Technically strong; must avoid default execution. This creates a review priority of `standard sandbox review`.

[follow-up-candidate] Cost/quality posture: estimated cost per 1k captures is `0.0` USD envelope and quality score is `4.8`. These values should be recalculated after future web evidence refresh and before dispatch drafting.

[follow-up-candidate] Sandbox posture: sandboxability score `5` means the future spike should be able to start with local/temp fixtures and read-only preflight. No row is an adoption decision.

### V31 Selenium

[follow-up-candidate] `Selenium` is scored for `Lane-3` as `legacy browser automation`. The current numeric row is a planning estimate only; live release, price, ToS, CVE, and benchmark evidence were not refreshed in this execution.

[follow-up-candidate] Risk rationale: Stable but heavier/flakier. This creates a review priority of `standard sandbox review`.

[follow-up-candidate] Cost/quality posture: estimated cost per 1k captures is `0.0` USD envelope and quality score is `4.0`. These values should be recalculated after future web evidence refresh and before dispatch drafting.

[follow-up-candidate] Sandbox posture: sandboxability score `4` means the future spike should be able to start with local/temp fixtures and read-only preflight. No row is an adoption decision.

### V32 Puppeteer

[follow-up-candidate] `Puppeteer` is scored for `Lane-3` as `Chrome automation`. The current numeric row is a planning estimate only; live release, price, ToS, CVE, and benchmark evidence were not refreshed in this execution.

[follow-up-candidate] Risk rationale: Chrome-centric but mature. This creates a review priority of `standard sandbox review`.

[follow-up-candidate] Cost/quality posture: estimated cost per 1k captures is `0.0` USD envelope and quality score is `4.2`. These values should be recalculated after future web evidence refresh and before dispatch drafting.

[follow-up-candidate] Sandbox posture: sandboxability score `4` means the future spike should be able to start with local/temp fixtures and read-only preflight. No row is an adoption decision.

### V33 Stagehand

[follow-up-candidate] `Stagehand` is scored for `Lane-3` as `AI browser action layer`. The current numeric row is a planning estimate only; live release, price, ToS, CVE, and benchmark evidence were not refreshed in this execution.

[follow-up-candidate] Risk rationale: Agentic action risk and vendor dependency. This creates a review priority of `conservative review`.

[follow-up-candidate] Cost/quality posture: estimated cost per 1k captures is `120.0` USD envelope and quality score is `3.6`. These values should be recalculated after future web evidence refresh and before dispatch drafting.

[follow-up-candidate] Sandbox posture: sandboxability score `2` means the future spike should start with synthetic fixtures and no real platform call. No row is an adoption decision.

### V34 browser-use

[follow-up-candidate] `browser-use` is scored for `Lane-3` as `agentic browser automation`. The current numeric row is a planning estimate only; live release, price, ToS, CVE, and benchmark evidence were not refreshed in this execution.

[follow-up-candidate] Risk rationale: Agentic autonomy raises action-overreach risk. This creates a review priority of `conservative review`.

[follow-up-candidate] Cost/quality posture: estimated cost per 1k captures is `80.0` USD envelope and quality score is `3.5`. These values should be recalculated after future web evidence refresh and before dispatch drafting.

[follow-up-candidate] Sandbox posture: sandboxability score `2` means the future spike should start with synthetic fixtures and no real platform call. No row is an adoption decision.

### V35 Claude computer use

[follow-up-candidate] `Claude computer use` is scored for `Lane-3` as `AI computer/browser control`. The current numeric row is a planning estimate only; live release, price, ToS, CVE, and benchmark evidence were not refreshed in this execution.

[follow-up-candidate] Risk rationale: Powerful but high operator-control risk. This creates a review priority of `conservative review`.

[follow-up-candidate] Cost/quality posture: estimated cost per 1k captures is `200.0` USD envelope and quality score is `3.6`. These values should be recalculated after future web evidence refresh and before dispatch drafting.

[follow-up-candidate] Sandbox posture: sandboxability score `2` means the future spike should start with synthetic fixtures and no real platform call. No row is an adoption decision.

### V36 Alembic

[follow-up-candidate] `Alembic` is scored for `Lane-4` as `Python migration tool`. The current numeric row is a planning estimate only; live release, price, ToS, CVE, and benchmark evidence were not refreshed in this execution.

[follow-up-candidate] Risk rationale: Mature; risk is governance not tool. This creates a review priority of `standard sandbox review`.

[follow-up-candidate] Cost/quality posture: estimated cost per 1k captures is `0.0` USD envelope and quality score is `4.5`. These values should be recalculated after future web evidence refresh and before dispatch drafting.

[follow-up-candidate] Sandbox posture: sandboxability score `4` means the future spike should be able to start with local/temp fixtures and read-only preflight. No row is an adoption decision.

### V37 Diesel migrations

[follow-up-candidate] `Diesel migrations` is scored for `Lane-4` as `Rust migration tool`. The current numeric row is a planning estimate only; live release, price, ToS, CVE, and benchmark evidence were not refreshed in this execution.

[follow-up-candidate] Risk rationale: Mature; stack mismatch possible. This creates a review priority of `standard sandbox review`.

[follow-up-candidate] Cost/quality posture: estimated cost per 1k captures is `0.0` USD envelope and quality score is `3.7`. These values should be recalculated after future web evidence refresh and before dispatch drafting.

[follow-up-candidate] Sandbox posture: sandboxability score `3` means the future spike should start with synthetic fixtures and no real platform call. No row is an adoption decision.

### V38 sqlx migrate

[follow-up-candidate] `sqlx migrate` is scored for `Lane-4` as `Rust/SQLx migration tool`. The current numeric row is a planning estimate only; live release, price, ToS, CVE, and benchmark evidence were not refreshed in this execution.

[follow-up-candidate] Risk rationale: Mature; stack mismatch possible. This creates a review priority of `standard sandbox review`.

[follow-up-candidate] Cost/quality posture: estimated cost per 1k captures is `0.0` USD envelope and quality score is `3.7`. These values should be recalculated after future web evidence refresh and before dispatch drafting.

[follow-up-candidate] Sandbox posture: sandboxability score `3` means the future spike should start with synthetic fixtures and no real platform call. No row is an adoption decision.

### V39 SQLite FTS5

[follow-up-candidate] `SQLite FTS5` is scored for `Lane-5` as `local-first search index`. The current numeric row is a planning estimate only; live release, price, ToS, CVE, and benchmark evidence were not refreshed in this execution.

[follow-up-candidate] Risk rationale: Local and mature; ranking quality limited. This creates a review priority of `standard sandbox review`.

[follow-up-candidate] Cost/quality posture: estimated cost per 1k captures is `0.0` USD envelope and quality score is `3.8`. These values should be recalculated after future web evidence refresh and before dispatch drafting.

[follow-up-candidate] Sandbox posture: sandboxability score `5` means the future spike should be able to start with local/temp fixtures and read-only preflight. No row is an adoption decision.

### V40 Local embeddings + MCP

[follow-up-candidate] `Local embeddings + MCP` is scored for `Lane-5` as `local-first signal stack`. The current numeric row is a planning estimate only; live release, price, ToS, CVE, and benchmark evidence were not refreshed in this execution.

[follow-up-candidate] Risk rationale: Private but model quality/storage needs spike. This creates a review priority of `standard sandbox review`.

[follow-up-candidate] Cost/quality posture: estimated cost per 1k captures is `0.0` USD envelope and quality score is `4.0`. These values should be recalculated after future web evidence refresh and before dispatch drafting.

[follow-up-candidate] Sandbox posture: sandboxability score `4` means the future spike should be able to start with local/temp fixtures and read-only preflight. No row is an adoption decision.

## §8 Candidate scoring formulas

[scoring-candidate] A future operator may compute `triage_priority = quality_score + sandboxability_score - risk_score - min(cost_per_1k_capture_usd_est / 250, 3)`. This formula is intentionally conservative because it penalizes risk and cost before rewarding quality.

[scoring-candidate] A vendor should require heavy review when `risk_score >= 4` or `sandboxability_score <= 2`, even if quality is high. This catches Bilibili/XHS scrapers, proxy unlockers, media downloaders, and agentic browser tools.

[scoring-candidate] A vendor can be considered low-friction for a sandbox only when `risk_score <= 2`, `sandboxability_score >= 4`, and the spike can run without secrets, model downloads, production writes, or external domains.

[boundary] The formula is a review helper, not an execution policy. It cannot override human gates in the overflow registry.

