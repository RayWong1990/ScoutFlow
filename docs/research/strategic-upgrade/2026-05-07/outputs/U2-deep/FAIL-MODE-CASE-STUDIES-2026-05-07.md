---
title: FAIL MODE CASE STUDIES Deep Supplement 2026-05-07
status: candidate / fail_mode_case_studies / not-authority
authority: not-authority
execution_approval: not-approved
runtime_approval: not-approved
migration_approval: not-approved
created_at: 2026-05-07
supplements: cloud-output-U2-phase-2-unlock-playbook-2026-05-07.zip
claim_label_policy: paragraph-level labels; command lines explicitly marked command-candidate
---

# FAIL-MODE-CASE-STUDIES-2026-05-07

## §0 Source anchors / 输入锚点

[canonical-project-evidence] Overflow registry v0 keeps all five lanes in Hold and defines separate human gates: `true_write_approval`, `explicit_runtime_approval`, `visual_verdict`, `explicit_migration_approval`, and `usefulness_verdict`.

[canonical-project-evidence] T-P1A-021 says BBDown live metadata probe is only a future bounded dispatch; raw stdout, credentials, QR, auth sidecar, and URL parameters must stay local-only, and `PlatformResult` must not be emitted when preflight fails.

[canonical-project-evidence] T-P1A-022 says `audio_transcript`, ASR, ffmpeg, worker runtime, model download, and generated transcript artifacts remain blocked; future ASR must preserve raw evidence, segment provenance, timestamp integrity, and human review state.

[canonical-project-evidence] T-P1A-023 says every normalized claim / quote / topic must cite transcript segment provenance; LLM output without segment provenance is an untrusted draft, not a ScoutFlow knowledge artifact.

[canonical-project-evidence] T-P1A-025 says DB vNext is candidate-only, `artifact_assets` remains file authority, new structured tables must index / project artifacts rather than replace the ledger, and migration files remain out of scope.

[canonical-project-evidence] `services/api/scoutflow_api/bridge/config.py` returns `write_enabled=False` both when `SCOUTFLOW_VAULT_ROOT` is absent and when preview is available. This supplement preserves that invariant.

[limitation] Live web browsing is unavailable in this execution environment. The vendor refresh requested by the deep prompt is therefore not represented as live-verified evidence. All vendor status/cost scores are marked `[scoring-candidate]` or `[paste-time-unverified]` and require future live refresh before any dispatch.

## §1 Case-study status

[case-policy] These are triggerable fail-mode case studies, not claims that the failures occurred in the current repo. They are “real” in the sense that each has a concrete input, trigger, detection signal, rollback step, and time cost that a future spike can reproduce in a sandbox.

[boundary] A fail-mode case does not authorize running the failing tool against real platforms, real RAW, or production DB. The case proves audit coverage, not unlock readiness.

## L1-FM-01 — path escape through crafted title

[case-candidate] Lane: `true_vault_write`. This case is designed to be reproducible in `/tmp/scoutflow-u2-deep/true_vault_write` without production writes.

[input] Synthetic capture title contains `../../outside.md` or absolute path-like fragments.

[trigger] Renderer joins title-derived filename without normalization.

[failure-phenomenon] Preview appears to target a path outside sandbox RAW mirror.

[detect-signal] `Path.resolve()` parent check fails; command C10/C11 report BLOCKED.

[rollback-step] Stop spike, keep write_enabled=False, delete sandbox, open amendment noting path sanitizer gap.

[time-cost-estimate] Expected one-dev handling time: 0.5-1 day. This includes reproducing the symptom, preserving the evidence packet, writing an amendment note, and rerunning the relevant negative test.

[audit-question] Can an auditor identify the failure from command logs alone, without trusting the operator's narrative?

## L1-FM-02 — frontmatter invalid but preview still writes

[case-candidate] Lane: `true_vault_write`. This case is designed to be reproducible in `/tmp/scoutflow-u2-deep/true_vault_write` without production writes.

[input] Capture metadata lacks title/status/tags or includes newline injection.

[trigger] Frontmatter generator does not validate four-field RAW mode before render.

[failure-phenomenon] Rendered markdown has malformed YAML or unsafe body-leading delimiters.

[detect-signal] Validator command C12 fails or YAML parser rejects packet.

[rollback-step] Do not promote; add frontmatter validator and negative fixture before audit.

[time-cost-estimate] Expected one-dev handling time: 0.5 day. This includes reproducing the symptom, preserving the evidence packet, writing an amendment note, and rerunning the relevant negative test.

[audit-question] Can an auditor identify the failure from command logs alone, without trusting the operator's narrative?

## L1-FM-03 — dry-run response drifts toward committed state

[case-candidate] Lane: `true_vault_write`. This case is designed to be reproducible in `/tmp/scoutflow-u2-deep/true_vault_write` without production writes.

[input] Future bridge commit route returns ambiguous `committed` or omits `dry_run`.

[trigger] Handler drift or schema change weakens dry-run contract.

[failure-phenomenon] Reviewer cannot tell whether a real write occurred.

[detect-signal] Dry-run contract validator command C16 fails.

[rollback-step] Freeze bridge route, restore explicit false fields, add schema regression test.

[time-cost-estimate] Expected one-dev handling time: 1 day. This includes reproducing the symptom, preserving the evidence packet, writing an amendment note, and rerunning the relevant negative test.

[audit-question] Can an auditor identify the failure from command logs alone, without trusting the operator's narrative?

## L2-FM-01 — BBDown parser drift

[case-candidate] Lane: `runtime_tools`. This case is designed to be reproducible in `/tmp/scoutflow-u2-deep/runtime_tools` without production writes.

[input] One user-approved Bilibili URL returns changed stdout layout.

[trigger] Bilibili output/API fields change; parser expects old title/duration fields.

[failure-phenomenon] Metadata job fails or emits partial/incorrect `PlatformResult`.

[detect-signal] Parser drift synthetic detector returns `parser_drift`; required fields absent.

[rollback-step] Halt probe queue, keep raw stdout local-only, update parser in separate dispatch.

[time-cost-estimate] Expected one-dev handling time: 1-2 days. This includes reproducing the symptom, preserving the evidence packet, writing an amendment note, and rerunning the relevant negative test.

[audit-question] Can an auditor identify the failure from command logs alone, without trusting the operator's narrative?

## L2-FM-02 — cookie or token leakage in evidence

[case-candidate] Lane: `runtime_tools`. This case is designed to be reproducible in `/tmp/scoutflow-u2-deep/runtime_tools` without production writes.

[input] BBDown/LangChain/MCP path emits auth headers or cookie-adjacent strings.

[trigger] Debug flag, raw stdout capture, or unredacted log enters packet.

[failure-phenomenon] Git-tracked evidence contains `SESSDATA`, `bili_jct`, Authorization, or Cookie.

[detect-signal] Credential scanner command detects secret patterns.

[rollback-step] Invalidate packet, rotate token if real, delete leaked artifact, amend ledger.

[time-cost-estimate] Expected one-dev handling time: 0.5-2 days. This includes reproducing the symptom, preserving the evidence packet, writing an amendment note, and rerunning the relevant negative test.

[audit-question] Can an auditor identify the failure from command logs alone, without trusting the operator's narrative?

## L2-FM-03 — ASR OOM or hallucination produces unusable transcript

[case-candidate] Lane: `runtime_tools`. This case is designed to be reproducible in `/tmp/scoutflow-u2-deep/runtime_tools` without production writes.

[input] Long audio or large model on small memory machine; weak audio section.

[trigger] ASR model exceeds memory or predicts text not spoken.

[failure-phenomenon] Transcript has repeated phrases, low confidence, or timestamp instability.

[detect-signal] Segment validator detects invalid timestamps; human review marks hallucination suspected.

[rollback-step] Fall back to smaller model or mark `needs_check`; never normalize unsupported claims.

[time-cost-estimate] Expected one-dev handling time: 1-3 days. This includes reproducing the symptom, preserving the evidence packet, writing an amendment note, and rerunning the relevant negative test.

[audit-question] Can an auditor identify the failure from command logs alone, without trusting the operator's narrative?

## L3-FM-01 — browser profile leaks cookies

[case-candidate] Lane: `browser_automation`. This case is designed to be reproducible in `/tmp/scoutflow-u2-deep/browser_automation` without production writes.

[input] Automation uses a real browser profile instead of temp isolated profile.

[trigger] Profile path not scoped to sandbox or persistent user profile reused.

[failure-phenomenon] Screenshots or traces include logged-in state or private data.

[detect-signal] Reviewer sees profile path outside sandbox; trace contains cookie/session clues.

[rollback-step] Delete profile copy, invalidate evidence, rotate affected credentials if real.

[time-cost-estimate] Expected one-dev handling time: 0.5-1 day. This includes reproducing the symptom, preserving the evidence packet, writing an amendment note, and rerunning the relevant negative test.

[audit-question] Can an auditor identify the failure from command logs alone, without trusting the operator's narrative?

## L3-FM-02 — external network egress

[case-candidate] Lane: `browser_automation`. This case is designed to be reproducible in `/tmp/scoutflow-u2-deep/browser_automation` without production writes.

[input] Visual smoke page loads external platform URL during screenshot.

[trigger] Test target or asset points to Bilibili/XHS/YouTube rather than localhost.

[failure-phenomenon] Browser makes external request, creating ToS/network side effects.

[detect-signal] URL scan and trace network log show non-localhost domain.

[rollback-step] Reject visual packet, enforce denylist, rerun only synthetic/localhost fixture.

[time-cost-estimate] Expected one-dev handling time: 0.5 day. This includes reproducing the symptom, preserving the evidence packet, writing an amendment note, and rerunning the relevant negative test.

[audit-question] Can an auditor identify the failure from command logs alone, without trusting the operator's narrative?

## L3-FM-03 — visual threshold hides regression

[case-candidate] Lane: `browser_automation`. This case is designed to be reproducible in `/tmp/scoutflow-u2-deep/browser_automation` without production writes.

[input] Pixel diff threshold too loose or text assertion absent.

[trigger] Screenshot diff accepts UI with missing Trust Trace / wrong state label.

[failure-phenomenon] Human believes UAT passed although important text disappeared.

[detect-signal] Text assertion schema missing or reviewer checklist unchecked.

[rollback-step] Set text assertions mandatory, rerun screenshot packet, keep visual verdict pending.

[time-cost-estimate] Expected one-dev handling time: 0.5-1 day. This includes reproducing the symptom, preserving the evidence packet, writing an amendment note, and rerunning the relevant negative test.

[audit-question] Can an auditor identify the failure from command logs alone, without trusting the operator's narrative?

## L4-FM-01 — production migration file accidentally generated

[case-candidate] Lane: `dbvnext_migration`. This case is designed to be reproducible in `/tmp/scoutflow-u2-deep/dbvnext_migration` without production writes.

[input] Operator runs migration generator inside repo path.

[trigger] Alembic/sqlx/diesel creates file under `services/api/migrations/**`.

[failure-phenomenon] Git status shows new migration file before explicit approval.

[detect-signal] Forbidden path post-check command reports changed path.

[rollback-step] Delete generated file, keep audit note, restart spike in temp DB only.

[time-cost-estimate] Expected one-dev handling time: 0.25-0.5 day. This includes reproducing the symptom, preserving the evidence packet, writing an amendment note, and rerunning the relevant negative test.

[audit-question] Can an auditor identify the failure from command logs alone, without trusting the operator's narrative?

## L4-FM-02 — idempotency replay conflict ignored

[case-candidate] Lane: `dbvnext_migration`. This case is designed to be reproducible in `/tmp/scoutflow-u2-deep/dbvnext_migration` without production writes.

[input] Same transcript artifact replay inserts duplicate segment row.

[trigger] DB design lacks deterministic unique key or conflict handling.

[failure-phenomenon] Replay creates duplicate rows or silently overwrites text.

[detect-signal] Idempotency replay command writes conflict log or row count mismatch.

[rollback-step] Add unique key / replay comparison; keep migration candidate on Hold.

[time-cost-estimate] Expected one-dev handling time: 1 day. This includes reproducing the symptom, preserving the evidence packet, writing an amendment note, and rerunning the relevant negative test.

[audit-question] Can an auditor identify the failure from command logs alone, without trusting the operator's narrative?

## L4-FM-03 — supersession hides wrong current doc

[case-candidate] Lane: `dbvnext_migration`. This case is designed to be reproducible in `/tmp/scoutflow-u2-deep/dbvnext_migration` without production writes.

[input] New normalized doc supersedes prior doc incorrectly.

[trigger] Query uses latest timestamp instead of explicit supersession relation.

[failure-phenomenon] UI or downstream pulls wrong artifact version.

[detect-signal] Current-doc query returns multiple or wrong rows after synthetic supersession.

[rollback-step] Fix explicit supersedes relation and hide superseded rows by view, not delete.

[time-cost-estimate] Expected one-dev handling time: 1-2 days. This includes reproducing the symptom, preserving the evidence packet, writing an amendment note, and rerunning the relevant negative test.

[audit-question] Can an auditor identify the failure from command logs alone, without trusting the operator's narrative?

## L5-FM-01 — unsupported topic recommendation

[case-candidate] Lane: `signal_workbench`. This case is designed to be reproducible in `/tmp/scoutflow-u2-deep/signal_workbench` without production writes.

[input] Topic candidate has no supporting claims/quotes/segments.

[trigger] LLM or scoring harness invents angle from weak source.

[failure-phenomenon] Workbench suggests follow/park/reject without evidence.

[detect-signal] Provenance validator or weak-support detector flags empty support.

[rollback-step] Downgrade to `needs_human_verdict`, reject unsupported recommendation.

[time-cost-estimate] Expected one-dev handling time: 0.5 day. This includes reproducing the symptom, preserving the evidence packet, writing an amendment note, and rerunning the relevant negative test.

[audit-question] Can an auditor identify the failure from command logs alone, without trusting the operator's narrative?

## L5-FM-02 — score conflates user preference with evidence quality

[case-candidate] Lane: `signal_workbench`. This case is designed to be reproducible in `/tmp/scoutflow-u2-deep/signal_workbench` without production writes.

[input] Scoring combines creator fit and evidence density without explanation.

[trigger] Weights are hidden; high score looks authoritative.

[failure-phenomenon] User cannot audit why topic was recommended.

[detect-signal] Score basis missing or risk thresholds absent.

[rollback-step] Split dimensions, show score_basis, require human usefulness verdict.

[time-cost-estimate] Expected one-dev handling time: 1 day. This includes reproducing the symptom, preserving the evidence packet, writing an amendment note, and rerunning the relevant negative test.

[audit-question] Can an auditor identify the failure from command logs alone, without trusting the operator's narrative?

## L5-FM-03 — downstream coupling breaks local-first assumption

[case-candidate] Lane: `signal_workbench`. This case is designed to be reproducible in `/tmp/scoutflow-u2-deep/signal_workbench` without production writes.

[input] Signal output imports ContentFlow/DiloFlow code or expects their schema.

[trigger] Workbench becomes dependent on sibling project availability.

[failure-phenomenon] ScoutFlow spike cannot run standalone; handoff path brittle.

[detect-signal] Non-coupling note absent; import scan finds sibling path dependency.

[rollback-step] Replace with JSON handoff shape, no imports, no direct coupling.

[time-cost-estimate] Expected one-dev handling time: 0.5-1 day. This includes reproducing the symptom, preserving the evidence packet, writing an amendment note, and rerunning the relevant negative test.

[audit-question] Can an auditor identify the failure from command logs alone, without trusting the operator's narrative?

## §2 Cross-case patterns

[pattern-candidate] The most common pattern is “candidate evidence becomes implicit approval”. This appears in Lane-1 dry-run drift, Lane-2 metadata/media conflation, Lane-3 visual threshold overconfidence, Lane-4 migration generation, and Lane-5 recommendation authority drift.

[pattern-candidate] The second pattern is “unreviewed generated text becomes source of truth”. ASR hallucination, LLM unsupported claims, and signal recommendations all need provenance checks before they become user-facing artifacts.

[pattern-candidate] The third pattern is “sandbox leakage”. Path escape, cookie leakage, browser profile reuse, production migration generation, and sibling-project coupling are all variations of the same control failure: the spike is no longer contained.

## §3 Fail-mode regression suite shape

[command-candidate] A future regression suite can map each case to a single negative fixture. Lane-1 tests use path strings. Lane-2 tests use synthetic stdout and JSONL segments. Lane-3 tests use synthetic screenshots and trace manifests. Lane-4 tests use temp SQLite constraints and replay. Lane-5 tests use unsupported topic JSONL.

[boundary] The regression suite should remain in `docs/research/spike/<lane>/<spike-id>/` or a repo-external temp folder until the user opens a dedicated implementation dispatch.


## §4 Case-to-command mapping

| Case | Primary command group | Negative fixture | Audit severity |
|---|---|---|---|
| L1-FM-01 | [mapping-candidate] true_vault_write commands | path escape through crafted title | HIGH |
| L1-FM-02 | [mapping-candidate] true_vault_write commands | frontmatter invalid but preview still writes | MEDIUM |
| L1-FM-03 | [mapping-candidate] true_vault_write commands | dry-run response drifts toward committed state | MEDIUM |
| L2-FM-01 | [mapping-candidate] runtime_tools commands | BBDown parser drift | MEDIUM |
| L2-FM-02 | [mapping-candidate] runtime_tools commands | cookie or token leakage in evidence | HIGH |
| L2-FM-03 | [mapping-candidate] runtime_tools commands | ASR OOM or hallucination produces unusable transcript | MEDIUM |
| L3-FM-01 | [mapping-candidate] browser_automation commands | browser profile leaks cookies | HIGH |
| L3-FM-02 | [mapping-candidate] browser_automation commands | external network egress | MEDIUM |
| L3-FM-03 | [mapping-candidate] browser_automation commands | visual threshold hides regression | MEDIUM |
| L4-FM-01 | [mapping-candidate] dbvnext_migration commands | production migration file accidentally generated | HIGH |
| L4-FM-02 | [mapping-candidate] dbvnext_migration commands | idempotency replay conflict ignored | MEDIUM |
| L4-FM-03 | [mapping-candidate] dbvnext_migration commands | supersession hides wrong current doc | MEDIUM |
| L5-FM-01 | [mapping-candidate] signal_workbench commands | unsupported topic recommendation | MEDIUM |
| L5-FM-02 | [mapping-candidate] signal_workbench commands | score conflates user preference with evidence quality | MEDIUM |
| L5-FM-03 | [mapping-candidate] signal_workbench commands | downstream coupling breaks local-first assumption | MEDIUM |

## §5 Detailed regression expectations

### Regression expectation for L1-FM-01

[regression-candidate] The future regression should include one positive control and one negative control for `path escape through crafted title`. The positive control demonstrates normal candidate behavior; the negative control demonstrates that the detector fails closed.

[regression-candidate] The test fixture should be small enough to live in a spike packet, not a production test suite, until the relevant lane gets a dedicated implementation dispatch. This prevents research fixtures from silently becoming authority.

[regression-candidate] The case should be considered covered only when the detect signal is machine-readable, the rollback step is written, and the reviewer can inspect the log without executing the risky operation again.

[metric-candidate] Candidate metric for `L1-FM-01`: time to detection should be under 10 minutes during audit replay, and time to rollback should match the estimated one-dev envelope of 0.5-1 day. If replay takes longer, the packet is too hard to audit.

### Regression expectation for L1-FM-02

[regression-candidate] The future regression should include one positive control and one negative control for `frontmatter invalid but preview still writes`. The positive control demonstrates normal candidate behavior; the negative control demonstrates that the detector fails closed.

[regression-candidate] The test fixture should be small enough to live in a spike packet, not a production test suite, until the relevant lane gets a dedicated implementation dispatch. This prevents research fixtures from silently becoming authority.

[regression-candidate] The case should be considered covered only when the detect signal is machine-readable, the rollback step is written, and the reviewer can inspect the log without executing the risky operation again.

[metric-candidate] Candidate metric for `L1-FM-02`: time to detection should be under 10 minutes during audit replay, and time to rollback should match the estimated one-dev envelope of 0.5 day. If replay takes longer, the packet is too hard to audit.

### Regression expectation for L1-FM-03

[regression-candidate] The future regression should include one positive control and one negative control for `dry-run response drifts toward committed state`. The positive control demonstrates normal candidate behavior; the negative control demonstrates that the detector fails closed.

[regression-candidate] The test fixture should be small enough to live in a spike packet, not a production test suite, until the relevant lane gets a dedicated implementation dispatch. This prevents research fixtures from silently becoming authority.

[regression-candidate] The case should be considered covered only when the detect signal is machine-readable, the rollback step is written, and the reviewer can inspect the log without executing the risky operation again.

[metric-candidate] Candidate metric for `L1-FM-03`: time to detection should be under 10 minutes during audit replay, and time to rollback should match the estimated one-dev envelope of 1 day. If replay takes longer, the packet is too hard to audit.

### Regression expectation for L2-FM-01

[regression-candidate] The future regression should include one positive control and one negative control for `BBDown parser drift`. The positive control demonstrates normal candidate behavior; the negative control demonstrates that the detector fails closed.

[regression-candidate] The test fixture should be small enough to live in a spike packet, not a production test suite, until the relevant lane gets a dedicated implementation dispatch. This prevents research fixtures from silently becoming authority.

[regression-candidate] The case should be considered covered only when the detect signal is machine-readable, the rollback step is written, and the reviewer can inspect the log without executing the risky operation again.

[metric-candidate] Candidate metric for `L2-FM-01`: time to detection should be under 10 minutes during audit replay, and time to rollback should match the estimated one-dev envelope of 1-2 days. If replay takes longer, the packet is too hard to audit.

### Regression expectation for L2-FM-02

[regression-candidate] The future regression should include one positive control and one negative control for `cookie or token leakage in evidence`. The positive control demonstrates normal candidate behavior; the negative control demonstrates that the detector fails closed.

[regression-candidate] The test fixture should be small enough to live in a spike packet, not a production test suite, until the relevant lane gets a dedicated implementation dispatch. This prevents research fixtures from silently becoming authority.

[regression-candidate] The case should be considered covered only when the detect signal is machine-readable, the rollback step is written, and the reviewer can inspect the log without executing the risky operation again.

[metric-candidate] Candidate metric for `L2-FM-02`: time to detection should be under 10 minutes during audit replay, and time to rollback should match the estimated one-dev envelope of 0.5-2 days. If replay takes longer, the packet is too hard to audit.

### Regression expectation for L2-FM-03

[regression-candidate] The future regression should include one positive control and one negative control for `ASR OOM or hallucination produces unusable transcript`. The positive control demonstrates normal candidate behavior; the negative control demonstrates that the detector fails closed.

[regression-candidate] The test fixture should be small enough to live in a spike packet, not a production test suite, until the relevant lane gets a dedicated implementation dispatch. This prevents research fixtures from silently becoming authority.

[regression-candidate] The case should be considered covered only when the detect signal is machine-readable, the rollback step is written, and the reviewer can inspect the log without executing the risky operation again.

[metric-candidate] Candidate metric for `L2-FM-03`: time to detection should be under 10 minutes during audit replay, and time to rollback should match the estimated one-dev envelope of 1-3 days. If replay takes longer, the packet is too hard to audit.

### Regression expectation for L3-FM-01

[regression-candidate] The future regression should include one positive control and one negative control for `browser profile leaks cookies`. The positive control demonstrates normal candidate behavior; the negative control demonstrates that the detector fails closed.

[regression-candidate] The test fixture should be small enough to live in a spike packet, not a production test suite, until the relevant lane gets a dedicated implementation dispatch. This prevents research fixtures from silently becoming authority.

[regression-candidate] The case should be considered covered only when the detect signal is machine-readable, the rollback step is written, and the reviewer can inspect the log without executing the risky operation again.

[metric-candidate] Candidate metric for `L3-FM-01`: time to detection should be under 10 minutes during audit replay, and time to rollback should match the estimated one-dev envelope of 0.5-1 day. If replay takes longer, the packet is too hard to audit.

### Regression expectation for L3-FM-02

[regression-candidate] The future regression should include one positive control and one negative control for `external network egress`. The positive control demonstrates normal candidate behavior; the negative control demonstrates that the detector fails closed.

[regression-candidate] The test fixture should be small enough to live in a spike packet, not a production test suite, until the relevant lane gets a dedicated implementation dispatch. This prevents research fixtures from silently becoming authority.

[regression-candidate] The case should be considered covered only when the detect signal is machine-readable, the rollback step is written, and the reviewer can inspect the log without executing the risky operation again.

[metric-candidate] Candidate metric for `L3-FM-02`: time to detection should be under 10 minutes during audit replay, and time to rollback should match the estimated one-dev envelope of 0.5 day. If replay takes longer, the packet is too hard to audit.

### Regression expectation for L3-FM-03

[regression-candidate] The future regression should include one positive control and one negative control for `visual threshold hides regression`. The positive control demonstrates normal candidate behavior; the negative control demonstrates that the detector fails closed.

[regression-candidate] The test fixture should be small enough to live in a spike packet, not a production test suite, until the relevant lane gets a dedicated implementation dispatch. This prevents research fixtures from silently becoming authority.

[regression-candidate] The case should be considered covered only when the detect signal is machine-readable, the rollback step is written, and the reviewer can inspect the log without executing the risky operation again.

[metric-candidate] Candidate metric for `L3-FM-03`: time to detection should be under 10 minutes during audit replay, and time to rollback should match the estimated one-dev envelope of 0.5-1 day. If replay takes longer, the packet is too hard to audit.

### Regression expectation for L4-FM-01

[regression-candidate] The future regression should include one positive control and one negative control for `production migration file accidentally generated`. The positive control demonstrates normal candidate behavior; the negative control demonstrates that the detector fails closed.

[regression-candidate] The test fixture should be small enough to live in a spike packet, not a production test suite, until the relevant lane gets a dedicated implementation dispatch. This prevents research fixtures from silently becoming authority.

[regression-candidate] The case should be considered covered only when the detect signal is machine-readable, the rollback step is written, and the reviewer can inspect the log without executing the risky operation again.

[metric-candidate] Candidate metric for `L4-FM-01`: time to detection should be under 10 minutes during audit replay, and time to rollback should match the estimated one-dev envelope of 0.25-0.5 day. If replay takes longer, the packet is too hard to audit.

### Regression expectation for L4-FM-02

[regression-candidate] The future regression should include one positive control and one negative control for `idempotency replay conflict ignored`. The positive control demonstrates normal candidate behavior; the negative control demonstrates that the detector fails closed.

[regression-candidate] The test fixture should be small enough to live in a spike packet, not a production test suite, until the relevant lane gets a dedicated implementation dispatch. This prevents research fixtures from silently becoming authority.

[regression-candidate] The case should be considered covered only when the detect signal is machine-readable, the rollback step is written, and the reviewer can inspect the log without executing the risky operation again.

[metric-candidate] Candidate metric for `L4-FM-02`: time to detection should be under 10 minutes during audit replay, and time to rollback should match the estimated one-dev envelope of 1 day. If replay takes longer, the packet is too hard to audit.

### Regression expectation for L4-FM-03

[regression-candidate] The future regression should include one positive control and one negative control for `supersession hides wrong current doc`. The positive control demonstrates normal candidate behavior; the negative control demonstrates that the detector fails closed.

[regression-candidate] The test fixture should be small enough to live in a spike packet, not a production test suite, until the relevant lane gets a dedicated implementation dispatch. This prevents research fixtures from silently becoming authority.

[regression-candidate] The case should be considered covered only when the detect signal is machine-readable, the rollback step is written, and the reviewer can inspect the log without executing the risky operation again.

[metric-candidate] Candidate metric for `L4-FM-03`: time to detection should be under 10 minutes during audit replay, and time to rollback should match the estimated one-dev envelope of 1-2 days. If replay takes longer, the packet is too hard to audit.

### Regression expectation for L5-FM-01

[regression-candidate] The future regression should include one positive control and one negative control for `unsupported topic recommendation`. The positive control demonstrates normal candidate behavior; the negative control demonstrates that the detector fails closed.

[regression-candidate] The test fixture should be small enough to live in a spike packet, not a production test suite, until the relevant lane gets a dedicated implementation dispatch. This prevents research fixtures from silently becoming authority.

[regression-candidate] The case should be considered covered only when the detect signal is machine-readable, the rollback step is written, and the reviewer can inspect the log without executing the risky operation again.

[metric-candidate] Candidate metric for `L5-FM-01`: time to detection should be under 10 minutes during audit replay, and time to rollback should match the estimated one-dev envelope of 0.5 day. If replay takes longer, the packet is too hard to audit.

### Regression expectation for L5-FM-02

[regression-candidate] The future regression should include one positive control and one negative control for `score conflates user preference with evidence quality`. The positive control demonstrates normal candidate behavior; the negative control demonstrates that the detector fails closed.

[regression-candidate] The test fixture should be small enough to live in a spike packet, not a production test suite, until the relevant lane gets a dedicated implementation dispatch. This prevents research fixtures from silently becoming authority.

[regression-candidate] The case should be considered covered only when the detect signal is machine-readable, the rollback step is written, and the reviewer can inspect the log without executing the risky operation again.

[metric-candidate] Candidate metric for `L5-FM-02`: time to detection should be under 10 minutes during audit replay, and time to rollback should match the estimated one-dev envelope of 1 day. If replay takes longer, the packet is too hard to audit.

### Regression expectation for L5-FM-03

[regression-candidate] The future regression should include one positive control and one negative control for `downstream coupling breaks local-first assumption`. The positive control demonstrates normal candidate behavior; the negative control demonstrates that the detector fails closed.

[regression-candidate] The test fixture should be small enough to live in a spike packet, not a production test suite, until the relevant lane gets a dedicated implementation dispatch. This prevents research fixtures from silently becoming authority.

[regression-candidate] The case should be considered covered only when the detect signal is machine-readable, the rollback step is written, and the reviewer can inspect the log without executing the risky operation again.

[metric-candidate] Candidate metric for `L5-FM-03`: time to detection should be under 10 minutes during audit replay, and time to rollback should match the estimated one-dev envelope of 0.5-1 day. If replay takes longer, the packet is too hard to audit.

## §6 Fail-mode severity notes

[risk-candidate] CRITICAL escalation should be reserved for real secret leakage, real RAW contamination, real production migration, or real external platform calls outside approval. The cases here mostly stay MEDIUM/HIGH because they are sandbox reproductions.

[risk-candidate] A future implementation dispatch should turn the most important negative fixtures into automated tests only after paths and schemas are approved. Until then, they are audit packet content.

[risk-candidate] The fail-mode file should be cross-checked against the previous 45-risk register. The register is broad; this supplement makes 15 of those risks operationally reproducible.

