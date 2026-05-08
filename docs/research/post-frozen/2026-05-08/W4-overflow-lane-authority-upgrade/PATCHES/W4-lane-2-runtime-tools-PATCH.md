---
title: W4 Lane 2 (runtime_tools) Patch — §0.5 B-lane sanity + §5.7 amend_trigger lane-specific
status: candidate / patch
authority: not-authority
created_by: gpt-pro
parent_cluster: W4
parent_lane: runtime_tools
created_at: 2026-05-08
upstream_finding: "audit catch — 5 lane §0.5 B-lane sanity / §5.7 amend_trigger paragraph clone, lane 2 缺 lane-specific verify"
disclaimer: 真态数字以 GitHub live main HEAD 为准; 撰写时刻数字仅为历史参考。
prerequisite_check: drift_detected
main_head_drift: "docs/current.md reports c802de4; GitHub chronological latest merge readback is 45e88d4 / PR #257 W4-B step0 convergence (撰写时刻历史参考, GitHub live 以 §0.5 Check 为准)"
active_product_count: "0/3 (refreshed at §0.5 Check)"
authority_writer_count: "0/1 (refreshed at §0.5 Check)"
wave_state: "WAVE_6_CANDIDATE_OPEN / NOT_EXECUTION_APPROVED"
vault_true_write_flag: false
memory_batch_count: 17
deliverable_type: patch
target_replacement_section:
  - "§0.5 B-lane sanity row"
  - "§5.7 amend_and_proceed pattern"

---
# Lane 2 Patch — runtime_tools spec hardening

> State: candidate / patch / not-authority / not runtime approval / not migration approval / not lane unlock.
>
> Purpose: 把 lane 2 从研究包收口为可执行 spec PR 输入, 同时保留 hypothesis 语气、runtime blocked、以及 same-lane only 边界。

## §0.5 Prerequisite Check

| Check | Live readback | Result |
|---|---|---|
| docs/current.md | reports `main = c802de4`, Active `0/3`, Authority writer `0/1`, `WAVE_6_CANDIDATE_OPEN / NOT_EXECUTION_APPROVED`, vault true-write flag remains false | drift on main-head persists; live main is `45e88d4` |
| docs/task-index.md | Active table empty, Review empty, Backlog empty; product lane `0/3`, authority writer `0/1` | matches prompt authority state |
| docs/decision-log.md | current authority file reachable; tail still centers on W2C closeout and does not encode PR #257 merge state | authority history readable, but live merge truth still needs Git readback |
| docs/memory/INDEX.md | `batch_count: 17`, 7 lessons + 5 feedback + 5 patterns | matches prompt |
| GitHub commit chronological | latest returned commit is `45e88d4` / PR #257 W4-B step0 convergence | drift vs current.md anchor `c802de4` |

**prerequisite_check = `drift_detected`**. Main-head truth in this packet is: docs authority anchor still says `c802de4`, while GitHub chronological latest merge is `45e88d4` (撰写时刻历史参考, GitHub live 以 §0.5 Check 为准). This packet does not write authority trio; it only records the drift for Codex / CC0 intake.

## §0.5 B-lane sanity — lane-specific replacement

| Sanity item | Lane 2 live-specific check | Required readback before any lane work |
|---|---|---|
| Runtime binary truth | BBDown / yt-dlp / ffmpeg / ASR / Whisper.cpp Metal are not repo-approved runtime dependencies in the PR #243 capture-station baseline | Confirm no binary invocation path is present in W2C/W4 candidate output; any local binary proof is repo-external evidence only |
| Legal/vendor risk | BBDown has a 2026-01-28 Bilibili cease-and-desist signal in project memory/prompt context; XHS/抖音/YouTube each need separate risk posture | Treat adapter choice as risk-managed candidate, not “use BBDown by default” |
| Cost/perf estimate | Whisper.cpp Metal on M-series is estimated at 30s-2min per single-file run in prompt context | Require first real probe to record wall-clock, model, input duration, and hardware; do not extrapolate from prompt |
| Preferred first-pass hypotheses | `yt-dlp primary / BBDown fallback` and `Whisper.cpp Metal primary / FunASR fallback` are allowed only as candidate planning hypotheses | Require legal refresh receipt + benchmark receipt before any route lock; if evidence disagrees, downgrade to TODO/hypothesis |
| Current authority | runtime_tools lane is still Hold; `audio_transcript` runtime blocked; vault true-write flag remains unrelated but still a global truth | Do not open runtime_tools via spec text; request explicit user gate and separate PR |
| Upgrade path | Master spec §16.2 path E is the legal route: new dispatch + user explicit authorization + isolated PR + external/cross-vendor audit | Lane 2 may prepare gate criteria but cannot approve itself |
| Evidence safety | Runtime stdout/stderr, raw media, cookies, headers, and sidecars are not tracked evidence | Evidence must be redacted summary + hash/size manifest only |
| Rewrite handoff | downstream rewrite/vault can consume transcript evidence later, but lane 2 只允许写 minimal rewrite plugin registry snapshot | Keep only style/output/fallback metadata; no rewrite runtime, no plugin implementation |

### Lane 2 B-lane sanity verdict

Lane 2 begins in `candidate / blocked / requires explicit runtime_tools gate`. A valid Lane 2 packet can define adapter matrix, preferred first-pass hypotheses, preflight, cost budget, legal risk, minimal rewrite registry, and stop criteria. It cannot execute or approve BBDown, yt-dlp, ffmpeg, ASR, media download, transcript generation, or `audio_transcript` runtime.

## §5.7 amend_and_proceed — lane-specific replacement

### Amend trigger matrix

| Trigger | Lane-specific detection | Required action | Hard stop reason |
|---|---|---|---|
| Vendor legal drift | New cease-and-desist, ToS, rate-limit, auth, or anti-scraping signal appears for Bilibili / 抖音 / 小红书 / YouTube | STOP; update vendor risk table; require CC0 + Hermes/Codex review before any probe | legal/platform drift changes adapter viability, not just implementation details |
| Legal refresh missing | draft proposes a preferred vendor route but has no fresh legal-refresh receipt for the active vendor pair | STOP; add refresh receipt before any route wording gets stronger | no vendor pair may graduate from hypothesis without a fresh legal readback |
| Runtime cost spike | first measured runtime >2x estimate, memory pressure, thermal throttling, or queue stall | STOP; write cost spike receipt; narrow model/input size before continuation | cost blowups can make local prosumer workflow unusable |
| Single-source failure | BBDown-only path fails, auth expires, platform blocks, or source coverage is insufficient | STOP; require source matrix fallback decision before proceeding | vendor diversification is required; no silent single-source lock-in |
| ASR quality drift | transcript WER/semantic quality below threshold, language segmentation wrong, speaker split hallucinated | STOP; classify quality failure; do not amend into “good enough” | bad transcript corrupts downstream rewrite/vault trust chain |
| Benchmark receipt missing | route text starts leaning toward “primary” but no bounded benchmark receipt exists | STOP; restore hypothesis wording; attach receipt schema first | wording cannot outrun evidence |
| Credential / sidecar contamination | auth data, cookie, token, or tool sidecar enters repo/evidence/log path | STOP; quarantine; run redaction review; no continuation | LP-SEC-001 forbids credential material as evidence |
| Unsafe temp-dir / raw stdout | command writes inside repo or raw stdout/stderr is proposed as tracked evidence | STOP; move to repo-external temp dir; reduce evidence to `safe_stdout_excerpt` + manifest only | sandbox leakage voids bounded-canary trust |
| subprocess/orchestrator regression | implementation proposal uses unsafe `subprocess.run` in prohibited orchestrator context | STOP; route to separate safety dispatch | existing tripwire prohibits this pattern |
| Rewrite registry drift | lane 2 draft starts adding rewrite runtime, plugin implementation, or cross-lane promotion logic | STOP; shrink back to minimal registry snapshot | lane 2 may describe handoff metadata only, not reopen rewrite lane |

### Amend rule

Lane 2 may use amend-and-proceed only for documentation wording or non-risk test narrowing. It may **not** amend-through legal drift, cost spike, quality failure, single-source lock-in, or credential contamination. Those become stop-line receipts and require explicit user gate.

### Receipt requirements

- Receipt path: `docs/research/post-frozen/W4/lane-2/receipts/<timestamp>-runtime-tools-trigger.md`.
- Required fields: tool/source, trigger type, measured cost if any, legal/risk note, redaction status, fallback recommendation, reviewer needed.
- Required additions for route-selection cases: `route_hypothesis`, `legal_refresh_status`, `benchmark_receipt_status`, `temp_dir_scope`, `safe_stdout_present`.
- Required additions for transcript handoff cases: `transcript_text`, `language_detected`, `duration_seconds`, `asr_engine`, `asr_model_sha256`, `extraction_seed`, `trust_trace_id`, `source_url`, `capture_date`.
- Forbidden fields: raw media body, cookie/token, raw tool stdout/stderr, browser profile path, secret sidecar.

## Self-flag

1. ⚠️ Runtime cost numbers are prompt-provided estimates; I did not independently verify M-series ASR benchmarks in live repo.
2. ⚠️ Vendor legal drift must be refreshed at execution time; this patch only requires the refresh and stop rule.
3. ⚠️ Lane 2 path E naming comes from the prompt/master-spec reference; CC0 should verify exact §16.2 row label before applying.
4. ⚠️ `yt-dlp primary / BBDown fallback` and `Whisper.cpp Metal primary / FunASR fallback` are spec-writing hypotheses only; this patch does not promote them to authority.
