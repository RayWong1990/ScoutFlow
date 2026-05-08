---
title: Batch Manifest V1 Contracts (candidate)
status: candidate north-star
authority: not-authority
applicable_phase: master roadmap §Phase 3 (3 URL smoke) and §Phase 3.5 (10 URL friction)
ingest_basis: GPT Pro pack D 01/02/08 + APPENDIX-A/B (raw PARA)
not_approval:
  - not batch execution approval
  - not true-write approval
  - not runtime approval
  - not ASR approval
  - not scheduler approval
  - not worker approval
  - not DB queue approval
  - not Storybook UI approval
  - not browser automation approval
created_at: 2026-05-08
---

# Batch Manifest V1 Contracts (candidate)

> State: candidate / docs-only / not-authority / not-batch-execution-approval.

## 1. Purpose

This file is a schema-and-boundary spec for future batch manifests only. It is a citeable source for future Phase 3 and Phase 3.5 dispatches. It is not a batch runner contract, scheduler object, worker registry, DB queue contract, migration proposal, runtime route decision, browser lane, Storybook plan, or true-write lane.

## 2. Source Anchors

- `docs/current.md`
- `docs/task-index.md`
- `docs/BATCH-TRANSCRIPTION-MASTER-ROADMAP-2026-05-08.md`
- `/Users/wanglei/Downloads/research0508/SCOUTFLOW-GPTPRO-D-BATCH-SMOKE-FRICTION-OPS-2026-05-08.zip`

## 3. Batch Type Boundaries

| Batch type | Role | Scope ceiling | Boundary sentence |
|---|---|---|---|
| `3a_preview_smoke` | preview smoke | same 3 URLs, preview only | `3 URL is smoke only.` |
| `3b_true_write_smoke` | true-write smoke | same 3 URLs as 3A | `Same payload as 3A verified or blocked.` |
| `10a_preview_friction` | preview friction | same 10 URLs, preview only | `10 URL is friction only.` |
| `10b_true_write_friction` | true-write friction | same 10 URLs as 10A | `No full-platform-ready claim.` |

All four stay candidate-only. None of them changes `write_enabled=False`, `runtime_tools`, `true_vault_write`, `browser_automation`, `dbvnext_migration`, or `full_signal_workbench`.

## 4. ItemRunManifestV1 Schema

### 4.1 Item final-state vocabulary

| State | Meaning | Can be final | Continue condition |
|---|---|---|---|
| `closed_ok` | item reached the current run endpoint | yes | evidence is present and boundaries stay intact |
| `closed_recorded_failure` | item failed but failure is classified | yes | failure class is filled and evidence is readable |
| `closed_duplicate` | item deduped against same-run or prior evidence | yes | duplicate basis is explicit |
| `closed_skipped` | item skipped before risky action by explicit rule | yes | skip reason is explicit |
| `batch_stop_line` | item hit stop-line and no further processing should continue | yes | batch verdict must surface the stop-line |

### 4.2 Item fields

| Field | Required? | Allowed values / shape | Evidence requirement | No-go condition |
|---|---:|---|---|---|
| `batch_id` | yes | stable batch string | matches parent batch manifest | batch ID drift inside same run |
| `item_id` | yes | stable string unique within batch | appears in item and batch manifests | duplicate `item_id` without `closed_duplicate` |
| `batch_type` | yes | exact four batch types only | matches dispatch and parent batch manifest | invented fifth type |
| `operator` | yes | human or Codex executor label | readable owner identity | anonymous executor with no trace |
| `created_at` | yes | ISO-8601 | creation timestamp is preserved | missing creation time |
| `updated_at` | yes | ISO-8601 | update timestamp moves on state change | stale or blank timestamp |
| `final_state` | yes | one of 5 item final states | matches actual item outcome | blank, `pending`, or vague success wording |
| `source_url` | yes | canonical URL or explicit redacted placeholder | URL hash or safe reference; no raw secrets | signed params, cookie, token, or credential-bearing URL |
| `source_family` | yes | `bilibili` / `youtube` / `xhs` / `rss` / `pdf` / `image` / `research` / `unknown` | operator classification or source receipt | tactical route presented as long-term source promotion |
| `source_receipt` | yes for reachable source; otherwise explicit blocked form | safe receipt link, safe summary, or `blocked:<reason>` | tied to `source_url` and redacted | raw stdout/stderr or unsafe source dump |
| `transcript_handoff` | yes or explicit blocked form | `present:<link>` / `blocked:transcript_missing` / `not_in_scope` | runtime/ASR candidate must point to safe handoff; preview-only blocked item may store reason only | transcript implied ready without evidence |
| `rewrite_output` | yes for preview-ready item; otherwise explicit blocked form | `present:<link>` / `blocked:rewrite_unsupported` / `not_in_scope` | preview link or rewrite hash | unsupported rewrite used as if evidence-backed |
| `preview_hash` | yes for preview runs | stable hash or `blocked:<reason>` | same value reused for same-payload verification | true-write path proceeds without matching preview hash |
| `true_write_hash` | required only for true-write path; otherwise explicit waiting/blocked form | stable hash / `waiting_user_gate` / `blocked:<reason>` / `not_in_scope` | committed artifact hash plus write evidence when present | filled as committed without gate and write receipt |
| `failure_class` | yes when `final_state` is not `closed_ok` | one of failure classes in §6 | one-line reason plus detection point | unclassified failure with item closed as if clear |
| `evidence_links` | yes for every non-skipped item | safe local/GitHub/receipt links | at least one readable evidence pointer | raw stdout/stderr, cookie, token, signed URL, or private profile data |
| `cost_row` | yes | row link or inline row ID | runtime seconds, manual minutes, retry count, or cost note | no operator-load trace in friction run |
| `operator_note` | optional but recommended | one sentence | human-observable friction or ambiguity | long narrative replacing evidence |
| `remaining_hold` | yes | current holds that remain unchanged | still-active hold list is explicit | item phrasing implies unlock of runtime/write/browser/DB/full-signal |

### 4.3 Minimal filled item example

| Field | Example |
|---|---|
| `batch_id` | `BATCH-3A-2026-05-08` |
| `item_id` | `BATCH-3A-2026-05-08-ITEM-01` |
| `batch_type` | `3a_preview_smoke` |
| `operator` | `codex-local` |
| `created_at` | `2026-05-08T12:00:00Z` |
| `updated_at` | `2026-05-08T12:07:00Z` |
| `final_state` | `closed_recorded_failure` |
| `source_url` | `https://example.invalid/source-01` |
| `source_family` | `bilibili` |
| `source_receipt` | `present:safe-source-receipt-01.md` |
| `transcript_handoff` | `blocked:transcript_missing` |
| `rewrite_output` | `blocked:rewrite_unsupported` |
| `preview_hash` | `blocked:transcript_missing` |
| `true_write_hash` | `not_in_scope` |
| `failure_class` | `transcript_missing` |
| `evidence_links` | `safe-source-receipt-01.md` |
| `cost_row` | `COST-ROW-01` |
| `operator_note` | `Preview blocked honestly; no write attempted.` |
| `remaining_hold` | `runtime_tools, true_vault_write, browser_automation, dbvnext_migration, full_signal_workbench` |

## 5. Run-State Vocabulary

| State | Use |
|---|---|
| `preview_ready` | preview run has enough filled fields to move into human review |
| `preview_blocked` | preview run cannot proceed and the blocker is classified |
| `true_write_waiting_user_gate` | same-payload true-write candidate is ready but user gate is absent |
| `true_write_committed` | true-write evidence and receipts exist for that exact payload |
| `true_write_blocked` | true-write path is blocked by gate, hash, secret, path, atomic-write, or rollback issue |
| `friction_report_complete` | friction findings are complete enough to inform the next decision |

## 6. Failure Classes

Use short operational classes. Do not expand this into a heavy enterprise taxonomy.

| Class | Meaning | Continue? |
|---|---|---|
| `none` | no failure | yes |
| `duplicate_same_batch` | same URL/payload already represented in this batch | yes, close duplicate |
| `source_route_blocked` | source cannot be handled under current route | yes if classified |
| `transcript_missing` | transcript or handoff is absent/incomplete | yes for preview friction; write path stays blocked |
| `rewrite_unsupported` | rewrite lacks transcript/source backing | yes if recorded; do not write |
| `preview_write_hash_mismatch` | same-payload check failed | no; stop-line |
| `secret_scan_fail` | secret or raw output leakage risk | no; stop-line |
| `vault_path_collision` | naming or containment conflict detected | no for true-write path |
| `user_gate_missing` | explicit user gate is absent | yes as waiting/blocked; no write |
| `db_friction` | receipt/path/lookup friction suggests DB architecture decision is needed | yes; record only |
| `operator_fatigue` | manual load is too high for current batch shape | yes; record only |
| `receipt_unreadable` | evidence is too noisy to audit | yes; record only |
| `stop_line_other` | any unlisted stop-line | no; stop-line |

## 7. BatchRunManifestV1 Schema

### 7.1 Batch fields

| Field | Required? | Allowed values / shape | Evidence requirement | No-go condition |
|---|---:|---|---|---|
| `batch_id` | yes | stable batch string | appears in every item manifest | batch ID changes mid-run |
| `batch_type` | yes | exact four batch types only | matches dispatch and closeout template | invented “full batch proof” type |
| `run_state` | yes | one of 6 run states from §5 | matches item outcomes and batch verdict | vague `complete` wording |
| `item_count` | yes | `3` or `10` | equals item manifest count before dedupe closeout | missing or extra item |
| `logical_slots` | yes | `1`, `2`, or explicit `3` for `10a_preview_friction` / `10b_true_write_friction` only | operator note explains slot use | slot count described as worker architecture |
| `input_urls` | yes | list length equals `item_count` before dedupe | canonical list or redacted labels | raw credential-bearing URLs in tracked docs |
| `item_manifests` | yes | one pointer per input item | every input item reaches one final state | orphan item or missing final state |
| `dedupe_summary` | yes | table or object matching §8 | duplicate handling is explicit | silent duplicate drop |
| `cost_summary` | yes | aggregate matching §9 | lightweight cost rows are preserved | no operator-load capture |
| `stop_lines_hit` | yes | list or `none` | maps to §11 matrix | stop-line hidden as normal failure |
| `remaining_holds` | yes | hold block matching §10 | current authority readback is visible | omitted hold implies unlock |
| `final_verdict` | yes | run state plus one-line reason | tied to item states and batch type rule | claims global readiness or general runtime truth |

### 7.2 Final verdict rules per batch type

| Batch | Allowed final run state | Required statement |
|---|---|---|
| `3a_preview_smoke` | `preview_ready` / `preview_blocked` | `3 URL is smoke only.` |
| `3b_true_write_smoke` | `true_write_waiting_user_gate` / `true_write_committed` / `true_write_blocked` | `Same payload as 3A verified or blocked.` |
| `10a_preview_friction` | `preview_ready` / `preview_blocked` / `friction_report_complete` | `10 URL is friction only.` |
| `10b_true_write_friction` | `true_write_waiting_user_gate` / `true_write_committed` / `true_write_blocked` / `friction_report_complete` | `No full-platform-ready claim.` |

## 8. Dedupe Summary Shape

| Dedupe class | Count | Items | Action |
|---|---:|---|---|
| same URL + same payload | `<N>` | `<item_ids>` | `closed_duplicate` |
| same URL + changed payload | `<N>` | `<item_ids>` | keep both, note payload delta |
| prior-run same preview hash | `<N>` | `<item_ids>` | close duplicate or require same-payload verification |
| no duplicate | `<N>` | `<item_ids>` | continue |

## 9. Cost Summary Shape

| Metric | Total | Worst item | Operator note |
|---|---:|---|---|
| runtime seconds | `<N>` | `<item_id>` | `<note>` |
| ASR seconds | `<N or not_in_scope>` | `<item_id>` | `<note>` |
| rewrite estimated tokens | `<N or not_in_scope>` | `<item_id>` | `<note>` |
| manual operator minutes | `<N>` | `<item_id>` | `<note>` |
| retry count | `<N>` | `<item_id>` | `<note>` |

## 10. Remaining Holds Block

Always paste this block in future batch closeout and strike only with future authority evidence.

| Hold | Status after this batch | Evidence |
|---|---|---|
| `runtime_tools` | still Hold unless separate runtime dispatch says otherwise | `<link>` |
| `true_vault_write` | still Hold unless explicit true-write gate and write receipt exist | `<link>` |
| `browser_automation` | still Hold | `<link>` |
| `dbvnext_migration` | still Hold until DB implementation dispatch | `<link>` |
| `full_signal_workbench` | still Hold until lane 1/2/4 dependency verdict plus proof-pair canary | `<link>` |

## 11. Stop-Line and Escalation Matrix

| Stop-line / issue | Detection | Immediate action | Who reviews | Allowed next step | Forbidden next step |
|---|---|---|---|---|---|
| credential/raw stdout leak | secret scan, raw stdout/stderr pattern, cookie/token/signed param seen | halt batch, quarantine evidence, do not commit | human + Opus audit | redact/delete unsafe packet; rerun from safe receipt if allowed | track raw output, continue batch, write vault |
| runtime route mismatch | source route differs from dispatch or unplanned dual-route appears | stop affected item; classify route drift | Codex + human | narrow route decision or dispatch amendment | declare runtime ready or run fallback live without gate |
| transcript missing | `TranscriptHandoffV1` missing or incomplete | record item failure; block rewrite/write if dependent | human | close `closed_recorded_failure` or retry once if gate says so | fabricate transcript or claim rewrite-ready |
| rewrite unsupported | rewrite lacks transcript/source backing | block write; record rewrite failure | human + Opus if risk is high | revise rewrite template or mark item failure | write unsupported note to vault |
| preview/write hash mismatch | preview hash differs from pre-write payload | stop item and batch true-write path | Codex + human | rerun preview or request new same-payload gate | write changed payload |
| vault path collision | containment or naming uniqueness check finds conflict | stop item before write | human + Opus audit | disambiguate by explicit policy or mark failure | overwrite, auto-rename silently, imply commit success |
| secret scan fail | scanner fails or cannot run | stop true-write; preview may close blocked if safe | human + Opus audit | repair scan or evidence path | bypass scan |
| user V-PASS missing | no human V-PASS for preview or no true-write gate for write | close as waiting or blocked | user | obtain explicit gate | treat preview as write gate |
| DB friction exceeds threshold | repeated receipt/path lookup noise appears in 10A/10B | record friction; recommend DB architecture study | human + Opus critique | candidate DB architecture study | migration implementation without dispatch |
| unclassified failure | item failed but no failure class is assigned | halt closeout claim | Codex + human | classify item or mark `batch_stop_line` | call batch clear |
| browser automation appears | Playwright/Selenium/browser profile/network trace appears outside scope | halt batch | human + Opus audit | remove scope or open separate browser lane | use screenshots/traces as batch proof |
| scheduler/worker/DB queue appears | queue backend, worker architecture, scheduler design, or DB queue implementation enters scope | halt template or run | human | return to manifest-only batch | promote scheduler/platform path |

## 12. Record-and-Continue Examples

| Issue | Continue condition |
|---|---|
| duplicate URL | item marked `closed_duplicate` |
| source route unavailable | failure classified and no raw output tracked |
| transcript missing in preview friction | item marked `closed_recorded_failure`; no write attempted |
| manual minutes high | cost row filled and top bottleneck recorded |
| receipt too long | receipt readability friction recorded |

## 13. Escalation Levels

| Level | Meaning | Action |
|---|---|---|
| `record` | safe friction | continue batch |
| `item_block` | item cannot proceed but batch can still close truthfully | close item with final state |
| `batch_stop_line` | safety or integrity boundary hit | stop run and review |
| `dispatch_amendment_needed` | scope is unclear or route drift changed the meaning of the run | do not continue until dispatch is amended |

## 14. Human Operator Checklist

### Before any batch

- read current authority snapshot
- confirm batch type is exactly `3a_preview_smoke`, `3b_true_write_smoke`, `10a_preview_friction`, or `10b_true_write_friction`
- confirm URL count is exactly `3` or `10`
- confirm preview precedes true-write
- confirm all remaining holds are understood
- confirm no scheduler / worker / DB queue scope
- confirm browser automation stays out of scope

### For `3a_preview_smoke`

- all 3 items have manifests
- every item has final state
- preview hashes are present or honestly blocked
- failures are classified
- no true-write is attempted
- closeout stays short enough to review

### For `3b_true_write_smoke`

- `3a_preview_smoke` closeout is available
- URLs are identical to `3a_preview_smoke`
- payload hashes are identical
- explicit user gate exists for that exact batch
- secret scan passed
- path containment passed
- rollback/cleanup receipt is present
- report avoids broad true-write wording

### For `10a_preview_friction`

- all 10 items have final states
- friction, not success, is the focus
- top 5 bottlenecks are filled
- bottlenecks are classified as DB / UI / receipt / runtime / source route
- operator fatigue is recorded
- receipt readability is recorded
- DB migration is not triggered

### For `10b_true_write_friction`

- `10a_preview_friction` report is complete
- URLs and payloads are identical to `10a_preview_friction`
- explicit user gate exists for that exact 10 URL set
- path collisions are recorded
- rollback/cleanup findings are recorded
- report avoids full-platform-ready wording

### Final operator sentence template

`I reviewed <BATCH-ID> and accept that this batch is <smoke/friction> only, with remaining Holds still active.`

## 15. Batch Quality Rubric

### Score scale

| Score | Meaning |
|---:|---|
| 0 | missing or unsafe |
| 1 | present but too vague |
| 2 | usable with minor gaps |
| 3 | clear, minimal, auditable |

### Rubric dimensions

| Dimension | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| item final states | missing states | some states vague | all states present | all states present and match evidence |
| preview/write boundary | mixed | stated but weak | mostly clear | impossible to confuse |
| same-payload verification | absent | manual claim only | hash table present | hash table plus blocked mismatch handling |
| cost/operator load | absent | partial | rows complete | rows reveal actionable friction |
| dedupe/idempotency | absent | narrative | table present | table plus item final states |
| stop-line handling | hidden | mixed with failures | matrix used | stop-lines plus allowed/forbidden next steps |
| receipt readability | too noisy | narrative-heavy | readable | one-page or table-first |
| remaining Holds | omitted | partial | listed | listed with evidence and no-unlock wording |
| solo-dev fit | enterprise bloat | too many fields | manageable | minimal and directly runnable |
| overclaim control | overclaims | some strong wording | mostly bounded | no runtime/platform/vault generalization |

### Suggested thresholds

| Run | Minimum useful score | Notes |
|---|---:|---|
| `3a_preview_smoke` | 22/30 | smoke can be partial if failure is known |
| `3b_true_write_smoke` | 25/30 | true-write needs stronger boundary proof |
| `10a_preview_friction` | 24/30 | friction value matters more than all-ok |
| `10b_true_write_friction` | 27/30 | true-write friction needs strict evidence |

### Automatic rubric fail

- any item lacks final state
- true-write proceeds without user gate
- raw stdout/stderr or credentials are tracked
- preview/write hash mismatch is ignored
- stop-line is hidden as normal failure
- remaining Holds are omitted
- `3a_preview_smoke` is written as real batch proof
- `10a_preview_friction` or `10b_true_write_friction` is written as full-platform readiness

## 16. Boundary Notes

- This file does not authorize any batch execution.
- This file does not authorize scheduler, worker, DB queue, browser automation, runtime tools, ASR, or migration.
- This file does not turn any candidate batch type into a go-live path.
- Any future Phase 3 or Phase 3.5 dispatch must cite this file and still require explicit user gate where write is involved.

## 17. Future Use Notes

Future Phase 3 dispatches can cite this file in four places only: item schema, batch schema, stop-line vocabulary, and closeout checklist/rubric. They must still read live authority first, preserve all remaining Holds, and keep `preview != write`, `candidate != authority`, and `smoke/friction != platform proof`.
