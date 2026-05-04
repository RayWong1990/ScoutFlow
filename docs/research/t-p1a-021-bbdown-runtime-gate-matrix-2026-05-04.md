# T-P1A-021 BBDown Runtime Gate Matrix — Research Note
> Status: **research / candidate** — not authority; not runtime approval; not implementation approval.
> Date: 2026-05-04
> Depends on: T-P1A-017 merged (Wave 2 ledger open)
> Prior evidence base: T-P1A-003 / T-P1A-009 / T-P1A-011 / T-P1A-011B / T-P1A-011C

---

## 1. Scope

Produce a candidate gate matrix for future bounded live BBDown `-info` metadata probes.
No BBDown execution in this task. No product code change. No authority change.

The gate matrix maps each observable probe outcome to a safe system response,
covering: what enters the receipt ledger, what stays local-only, and what triggers
which downstream job state transition.

---

## 2. ToolPreflightResult Gate

Checked before any platform call. Failure here means `PlatformResult` is **never emitted**.

| ToolPreflightResult | Meaning | System Action | Receipt Ledger |
|---|---|---|---|
| `executable_found` | BBDown binary present, version parseable | Proceed to platform probe | No entry yet |
| `executable_not_found` | Binary absent from configured PATH / explicit path | Job status → `failed`; blocker = `bbdown_not_found` | No receipt; no platform_result |
| `subprocess_error` | Binary present but version check subprocess crashed | Job status → `failed`; blocker = `bbdown_subprocess_error` | No receipt; no platform_result |

**Invariant**: `platform_result` field MUST remain `null` / not emitted when `ToolPreflightResult ≠ executable_found`. Writing any `PlatformResult` value for a preflight failure is a contract violation.

---

## 3. PlatformResult Gate Matrix

Emitted only after `ToolPreflightResult = executable_found` and BBDown `-info` is invoked.

### 3.1 Success Path

| PlatformResult | Signal | Safe Job Outcome | Receipt Entry | Evidence to `docs/research/` |
|---|---|---|---|---|
| `ok` | Parsed title + duration + page_count returned | `succeeded`; metadata written to receipt | `artifact_kind = safe_metadata_evidence` with redacted excerpt | Redacted stdout summary only (no raw stdout, no URL, no auth token) |

### 3.2 Auth / Access States

| PlatformResult | BBDown Signal | Safe Job Outcome | Receipt Entry | Brainstorm Note |
|---|---|---|---|---|
| `auth_required` | BBDown exits with login-required message or empty info for login-gated content | `failed`; reason = `auth_required` | No metadata receipt; blocker recorded | **Early-degradation candidate**: for `metadata_only` path, auth_required on a public video is unexpected — may indicate URL is actually member-only; worth surfacing as UX signal rather than hard fail |
| `vip_required` | BBDown signals premium-only content | `failed`; reason = `vip_required` | No metadata receipt; blocker recorded | `metadata_only` probe can still return title/duration on some VIP content via `-info`; should be validated before treating as full fail |
| `forbidden` | HTTP 403 or access explicitly denied | `failed`; reason = `forbidden` | No metadata receipt | Hard fail; no retry |
| `region_blocked` | Content not available in probe runtime region | `failed`; reason = `region_blocked` | No metadata receipt | Probe region must be declared in `safe_execution_preconditions`; no VPN/proxy allowed in repo context |

### 3.3 Content / Parser States

| PlatformResult | BBDown Signal | Safe Job Outcome | Receipt Entry | Notes |
|---|---|---|---|---|
| `not_found` | BBDown reports video not found / deleted / private | `failed`; reason = `not_found` | No metadata receipt | Capture should be marked `unavailable_source`; no retry |
| `unavailable` | Video exists but temporarily unavailable | `failed`; reason = `unavailable` | No metadata receipt | Retry may be appropriate after user-configured interval |
| `parser_drift` | BBDown stdout format changed; current parser cannot extract required fields | `failed`; reason = `parser_drift` | No metadata receipt; parser_drift event logged | **High priority for T-P1A-019**: `orchestration/` layer must detect parser_drift and halt further probes until parser repaired |

### 3.4 Network / Rate States

| PlatformResult | BBDown Signal | Safe Job Outcome | Receipt Entry | Retry Policy (candidate) |
|---|---|---|---|---|
| `network_error` | DNS / connection failure; BBDown never reached Bilibili API | `failed`; reason = `network_error` | No metadata receipt | Retry up to N times with exponential backoff; N and interval = user-configured or system default (see §5 brainstorm question) |
| `timeout` | BBDown subprocess exceeded configured wall-clock limit | `failed`; reason = `timeout` | No metadata receipt | Retry allowed; timeout threshold configurable |
| `rate_limited` | Bilibili API returns 412 / rate-limit response | `failed`; reason = `rate_limited` | No metadata receipt | Mandatory backoff before retry; never immediate retry; see §5 brainstorm question |
| `unknown_error` | BBDown exit code non-zero; unrecognized stderr pattern | `failed`; reason = `unknown_error` | No metadata receipt; raw exit code logged locally (not in ledger) | Investigate before retry |

---

## 4. Safe Execution Preconditions

These preconditions must all be satisfied before any live `-info` probe is approved in a future dispatch. They are **not currently approved**; this section is design input only.

| Precondition | Requirement | Rationale |
|---|---|---|
| Temp CWD | Probe must run in a repo-external temp directory (e.g. `tempfile.mkdtemp()`) | Prevents accidental write of BBDown cache / temp files into repo |
| No `--debug` flag | `--debug` must never be passed | `--debug` emits full HTTP headers which may contain session tokens |
| No media download flags | `--audio-only`, `--video-only`, `--download-danmaku`, `-p` page range for download must not be passed | `-info` only; no media pipeline |
| Max stdout excerpt | Only first N lines of stdout admitted to evidence (N ≤ 50 recommended) | Prevents raw response leakage |
| No raw stdout in ledger | Full BBDown stdout must stay local-only; only structured extracted fields enter `receipt_ledger` | Receipt ledger is Git-tracked; raw stdout may contain session-adjacent signals |
| Redaction before evidence | Title, URL, aid extracted; raw stdout discarded after extraction | Matches existing T-P1A-011C / T-P1A-012 redaction protocol |
| Configured probe timeout | Wall-clock timeout (e.g. 30s) applied to BBDown subprocess | Prevents hung subprocess blocking job queue |
| No VPN / proxy injection | Probe runs in native runtime region | Region-blocked results must reflect actual deployment region |
| Auth sidecar stays local | Cookie / token file path is passed via env / config; never written to repo or receipt | Matches T-P1A-011B auth gate |

---

## 5. Evidence Routing Rules

| Evidence Type | May Enter `docs/research/**` | May Enter Receipt Ledger | Must Stay Local-Only |
|---|---|---|---|
| Redacted metadata excerpt (title, duration, page_count, aid) | Yes — after manual redaction review | Yes — as `safe_metadata_evidence` artifact | — |
| `platform_result` value | Yes | Yes | — |
| `tool_preflight_result` + version | Yes | Yes | — |
| Raw BBDown stdout | No | No | Yes — temp dir, deleted after extraction |
| BBDown stderr / exit code | Summary only (no tokens) | No | Raw stays local |
| Cookie / token path | No | No | Yes |
| Session QR / auth state | No | No | Yes |
| Full Bilibili URL (with user-specific params) | No | Canonicalized form only | Raw with params stays local |

---

## 6. Future Dispatch Proposal — Single URL Bounded Live Probe

> This section is a **candidate dispatch design**, not an approved task.
> Approval requires explicit user gate + separate dispatch file.

**Proposed task**: `T-P1A-021A` (or later lane) — Single URL bounded live `-info` probe

**Scope constraints**:
- One URL only; URL must be user-provided, not inferred from corpus
- Auth state: may use existing local-only auth sidecar (T-P1A-011B baseline)
- Output: `platform_result` + redacted metadata excerpt → receipt ledger
- No media, no ffmpeg, no ASR, no `audio_transcript`

**Pre-conditions gate** (all must be true before dispatch):
1. `ToolPreflightResult = executable_found` (T-P1A-010A / T-P1A-011C baseline)
2. `T-P1A-019` orchestration layer exists and can receive probe results
3. Parser regression test passes (T-P1A-011C parser baseline)
4. Conflict domain table allows probe to write into orchestration layer (T-P1A-019 owns that domain)
5. User explicit gate: "approve single URL bounded live probe for T-P1A-021A"

**Proposed gate matrix sequence**:
```
ToolPreflightResult check
  → executable_not_found / subprocess_error → STOP, log blocker
  → executable_found
      → BBDown -info <url> (temp CWD, no debug, timeout=30s)
          → stdout excerpt extracted (≤50 lines)
          → redaction pass
          → PlatformResult classification
              → ok → receipt_ledger write (safe_metadata_evidence)
              → auth_required / vip_required / region_blocked → log, no receipt
              → parser_drift → STOP, log parser_drift event, halt probe queue
              → network_error / timeout / rate_limited → log, backoff, retry policy
              → not_found / unavailable / unknown_error → log, no receipt
```

---

## 7. Brainstorm Questions (per Dispatch 21 §8)

These are open questions for user + design review. Not decisions.

**Q1: auth_required / vip_required / region_blocked — early degradation?**

For `metadata_only` path, these three states may be more nuanced than a hard fail:
- `auth_required` on a supposedly public URL may indicate the video was recently made members-only → surface as `capture_state = source_changed` rather than `job_failed`?
- `vip_required`: some VIP content still returns title/duration in `-info` without auth. Should we distinguish `vip_required_no_metadata` vs `vip_required_partial_metadata`?
- `region_blocked`: hard fail for the probe, but the capture record itself might still be valid for a different runtime region. Worth preserving the capture record vs discarding?

**Q2: single URL bounded probe — user mental model?**

Two possible framings:
- "试一次看能不能" (opportunistic / exploratory): user pastes URL, system tries once, reports result. Low ceremony, no retry, result is informational.
- "正式探查" (formal probe): user explicitly initiates a metadata fetch job with retry semantics, SLA expectations, receipt issuance.

The current job queue model (`POST /jobs/`) maps better to the "正式探查" model.
The "试一次" model maps to a future synchronous preview endpoint (not yet designed).
Recommend: Wave 2 implements the "正式探查" model first (job queue); "试一次" can be a Phase 2 UX addition.

**Q3: rate_limited retry — user-configured or default backoff?**

Bilibili rate limiting is per-IP and per-cookie. Options:
- Default backoff: system applies 60s → 120s → 300s exponential backoff (simple, no user config needed)
- User-configured: user sets `probe_retry_interval_seconds` in capture config (flexible, more UX surface)
- No retry: rate_limited = permanent fail for this job; user re-submits manually

Recommendation (candidate): default backoff with configurable max_retries (default=3); rate_limited after max_retries → `job_failed` with `reason=rate_limited_exhausted`. Avoids needing a new config surface while being reasonable for most cases.

---

## 8. Boundary Confirmation

- No BBDown execution in this task.
- No product code modified.
- No authority document modified (PRD-v2 / SRD-v2 / LP / spec contracts unchanged).
- No credentials, QR, auth sidecar, or raw stdout documented.
- No runtime approval granted. This note is `research / candidate` status.
- No no-auth success asserted without future evidence.

---

## 9. References

| Source | Key finding |
|---|---|
| T-P1A-003 | BBDown `-info` confirmed for metadata-only; failure/stderr → `platform_result` draft mapping |
| T-P1A-009 | `executable_not_found` → `platform_result` not emitted; redaction protocol established |
| T-P1A-011 | `subprocess_error` → `platform_result` not emitted; two-layer separation confirmed |
| T-P1A-011B | Auth sidecar local-only gate; QR never enters repo |
| T-P1A-011C | `executable_found` + `platform_result=ok` baseline; parser repair (BBDown 1.6.3 output format) |
| T-P1A-012 | `safe_metadata_evidence` artifact kind; `metadata_probe_receipt_bridge` protocol |
