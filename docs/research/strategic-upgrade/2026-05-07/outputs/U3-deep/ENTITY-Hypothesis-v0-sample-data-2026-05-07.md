---
status: candidate / hypothesis_sample_data / not-authority
authority: not-authority
execution_approval: not-approved
runtime_approval: not-approved
migration_approval: not-approved
created_at: 2026-05-07
supplement_for: cloud-output-U3-entity-v0-contracts-2026-05-07.zip
---
# ENTITY-Hypothesis-v0-sample-data-2026-05-07

[canonical] Purpose: this supplementary file expands the previous entity contract with reviewable fixture-style sample instances. It does not promote any entity to DB authority, does not approve a migration, and does not add runtime endpoints.
[candidate] Data honesty note: live web browsing is unavailable in this execution environment. The Bilibili URLs below are carried from existing PF-C1 evidence context and from the user-provided prompt lineage; author names and rich platform metadata are deliberately marked `UNKNOWN_NOT_LIVE_VERIFIED` rather than fabricated.
[candidate] Sample design rule: each sample is fully populated at the contract level because every required field has a value, even when that value is an explicit unknown, blocked, or not-live-verified state. This keeps the IR testable without inventing truth.
[candidate] Review use: these samples are intended for local fixture review, OpenAPI examples, referential integrity tests, and migration worked examples. They should not be copied into SQLite or RAW as real knowledge objects.

## §1 Depth gaps found in previous ZIP

[candidate] Gap 1: Conflict signals were mentioned but not turned into fixture cases with support/counter/neutral evidence arrays.
[candidate] Gap 2: User verdict gates were clear conceptually but not shown as sample history objects.
[candidate] Gap 3: Downstream capture_plan cascade reverts were not attached to realistic hypothesis samples.

## §2 Sample instances

### Sample 01 — Hypothesis

[candidate] Sample 01 exercises Hypothesis relations using `BV16ooQBsEah`. URL shape is carried as a platform URL, but author and rich metadata remain not-live-verified.
```yaml
id: "hyp_01HR7S6A7F3Z9N2X4M8Q1V0A01"
entity_kind: "Hypothesis"
schema_version: "hypothesis.v0.candidate"
title: "H1: ordinary preview usefulness requires evidence balance"
claim_text: "For BV16ooQBsEah, topic-card usefulness is plausible only if support and counter signals remain visible."
testability: "can_be_reviewed_by_human_verdict_and_edit_cost_log"
source_capture_ids:
  - "cap_u3_01_sEah"
support_signal_ids:
  - "sig_01HR7S6A7F3Z9N2X4M8Q1V0A01"
  - "sig_01HR7S6A7F3Z9N2X4M8Q1V0A02"
counter_signal_ids:
  - "sig_01HR7S6A7F3Z9N2X4M8Q1V0A03"
neutral_signal_ids:
  - "sig_01HR7S6A7F3Z9N2X4M8Q1V0A04"
canonical_url_refs:
  - "https://www.bilibili.com/video/BV16ooQBsEah/"
confidence_label: "medium"
user_verdict: "needs_edit"
verdict_history:
  -
    at: "2026-05-07T00:00:00+08:00"
    actor: "single_user"
    verdict: "needs_edit"
    reason: "fixture exercise of state machine"
lifecycle_state: "under_review"
capture_plan_refs:
  - "plan_01HR7S6A7F3Z9N2X4M8Q1V0A01"
conflict_policy: "show_support_and_counter_before_any_plan"
claim_label_map:
  canonical_fields:
    - "id"
    - "source_capture_ids"
  candidate_fields:
    - "claim_text"
    - "support_signal_ids"
    - "counter_signal_ids"
  tentative_fields:
    - "confidence_label"
    - "user_verdict"
cascade_revert_policy: "if rejected, linked plan moves to suspended_pending_user_review"
notes: "Candidate hypothesis fixture; no scoring engine or recommendation runtime approval."
```
[candidate] Audit note 01: this sample intentionally uses explicit unknown/blocked states where live platform evidence is missing, preserving truthfulness while still making validators deterministic.
### Sample 02 — Hypothesis

[candidate] Sample 02 exercises Hypothesis relations using `BV1zhoUB1Ebg`. URL shape is carried as a platform URL, but author and rich metadata remain not-live-verified.
```yaml
id: "hyp_01HR7S6A7F3Z9N2X4M8Q1V0A02"
entity_kind: "Hypothesis"
schema_version: "hypothesis.v0.candidate"
title: "H2: edge preview usefulness requires evidence balance"
claim_text: "For BV1zhoUB1Ebg, topic-card usefulness is plausible only if support and counter signals remain visible."
testability: "can_be_reviewed_by_human_verdict_and_edit_cost_log"
source_capture_ids:
  - "cap_u3_02_1Ebg"
support_signal_ids:
  - "sig_01HR7S6A7F3Z9N2X4M8Q1V0A02"
  - "sig_01HR7S6A7F3Z9N2X4M8Q1V0A03"
counter_signal_ids:
  - "sig_01HR7S6A7F3Z9N2X4M8Q1V0A04"
neutral_signal_ids:
  - "sig_01HR7S6A7F3Z9N2X4M8Q1V0A05"
canonical_url_refs:
  - "https://www.bilibili.com/video/BV1zhoUB1Ebg/"
confidence_label: "medium"
user_verdict: "follow"
verdict_history:
  -
    at: "2026-05-07T00:00:00+08:00"
    actor: "single_user"
    verdict: "follow"
    reason: "fixture exercise of state machine"
lifecycle_state: "accepted_for_plan"
capture_plan_refs:
  - "plan_01HR7S6A7F3Z9N2X4M8Q1V0A02"
conflict_policy: "show_support_and_counter_before_any_plan"
claim_label_map:
  canonical_fields:
    - "id"
    - "source_capture_ids"
  candidate_fields:
    - "claim_text"
    - "support_signal_ids"
    - "counter_signal_ids"
  tentative_fields:
    - "confidence_label"
    - "user_verdict"
cascade_revert_policy: "if rejected, linked plan moves to suspended_pending_user_review"
notes: "Candidate hypothesis fixture; no scoring engine or recommendation runtime approval."
```
[candidate] Audit note 02: this sample intentionally uses explicit unknown/blocked states where live platform evidence is missing, preserving truthfulness while still making validators deterministic.
### Sample 03 — Hypothesis

[candidate] Sample 03 exercises Hypothesis relations using `BV1A196BpESQ`. URL shape is carried as a platform URL, but author and rich metadata remain not-live-verified.
```yaml
id: "hyp_01HR7S6A7F3Z9N2X4M8Q1V0A03"
entity_kind: "Hypothesis"
schema_version: "hypothesis.v0.candidate"
title: "H3: high_signal preview usefulness requires evidence balance"
claim_text: "For BV1A196BpESQ, topic-card usefulness is plausible only if support and counter signals remain visible."
testability: "can_be_reviewed_by_human_verdict_and_edit_cost_log"
source_capture_ids:
  - "cap_u3_03_pESQ"
support_signal_ids:
  - "sig_01HR7S6A7F3Z9N2X4M8Q1V0A03"
  - "sig_01HR7S6A7F3Z9N2X4M8Q1V0A04"
counter_signal_ids:
  - "sig_01HR7S6A7F3Z9N2X4M8Q1V0A05"
neutral_signal_ids:
  - "sig_01HR7S6A7F3Z9N2X4M8Q1V0A06"
canonical_url_refs:
  - "https://www.bilibili.com/video/BV1A196BpESQ/"
confidence_label: "low"
user_verdict: "reject"
verdict_history:
  -
    at: "2026-05-07T00:00:00+08:00"
    actor: "single_user"
    verdict: "reject"
    reason: "fixture exercise of state machine"
lifecycle_state: "rejected"
capture_plan_refs:
  - "plan_01HR7S6A7F3Z9N2X4M8Q1V0A03"
conflict_policy: "show_support_and_counter_before_any_plan"
claim_label_map:
  canonical_fields:
    - "id"
    - "source_capture_ids"
  candidate_fields:
    - "claim_text"
    - "support_signal_ids"
    - "counter_signal_ids"
  tentative_fields:
    - "confidence_label"
    - "user_verdict"
cascade_revert_policy: "if rejected, linked plan moves to suspended_pending_user_review"
notes: "Candidate hypothesis fixture; no scoring engine or recommendation runtime approval."
```
[candidate] Audit note 03: this sample intentionally uses explicit unknown/blocked states where live platform evidence is missing, preserving truthfulness while still making validators deterministic.
### Sample 04 — Hypothesis

[candidate] Sample 04 exercises Hypothesis relations using `BV16ooQBsEah`. URL shape is carried as a platform URL, but author and rich metadata remain not-live-verified.
```yaml
id: "hyp_01HR7S6A7F3Z9N2X4M8Q1V0A04"
entity_kind: "Hypothesis"
schema_version: "hypothesis.v0.candidate"
title: "H4: ordinary preview usefulness requires evidence balance"
claim_text: "For BV16ooQBsEah, topic-card usefulness is plausible only if support and counter signals remain visible."
testability: "can_be_reviewed_by_human_verdict_and_edit_cost_log"
source_capture_ids:
  - "cap_u3_04_sEah"
support_signal_ids:
  - "sig_01HR7S6A7F3Z9N2X4M8Q1V0A04"
  - "sig_01HR7S6A7F3Z9N2X4M8Q1V0A05"
counter_signal_ids:
  - "sig_01HR7S6A7F3Z9N2X4M8Q1V0A06"
neutral_signal_ids:
  - "sig_01HR7S6A7F3Z9N2X4M8Q1V0A07"
canonical_url_refs:
  - "https://www.bilibili.com/video/BV16ooQBsEah/"
confidence_label: "parking_lot"
user_verdict: "park"
verdict_history:
  -
    at: "2026-05-07T00:00:00+08:00"
    actor: "single_user"
    verdict: "park"
    reason: "fixture exercise of state machine"
lifecycle_state: "archived"
capture_plan_refs:
  - "plan_01HR7S6A7F3Z9N2X4M8Q1V0A04"
conflict_policy: "show_support_and_counter_before_any_plan"
claim_label_map:
  canonical_fields:
    - "id"
    - "source_capture_ids"
  candidate_fields:
    - "claim_text"
    - "support_signal_ids"
    - "counter_signal_ids"
  tentative_fields:
    - "confidence_label"
    - "user_verdict"
cascade_revert_policy: "if rejected, linked plan moves to suspended_pending_user_review"
notes: "Candidate hypothesis fixture; no scoring engine or recommendation runtime approval."
```
[candidate] Audit note 04: this sample intentionally uses explicit unknown/blocked states where live platform evidence is missing, preserving truthfulness while still making validators deterministic.
### Sample 05 — Hypothesis

[candidate] Sample 05 exercises Hypothesis relations using `BV1zhoUB1Ebg`. URL shape is carried as a platform URL, but author and rich metadata remain not-live-verified.
```yaml
id: "hyp_01HR7S6A7F3Z9N2X4M8Q1V0A05"
entity_kind: "Hypothesis"
schema_version: "hypothesis.v0.candidate"
title: "H5: edge preview usefulness requires evidence balance"
claim_text: "For BV1zhoUB1Ebg, topic-card usefulness is plausible only if support and counter signals remain visible."
testability: "can_be_reviewed_by_human_verdict_and_edit_cost_log"
source_capture_ids:
  - "cap_u3_05_1Ebg"
support_signal_ids:
  - "sig_01HR7S6A7F3Z9N2X4M8Q1V0A05"
  - "sig_01HR7S6A7F3Z9N2X4M8Q1V0A06"
counter_signal_ids:
  - "sig_01HR7S6A7F3Z9N2X4M8Q1V0A07"
neutral_signal_ids:
  - "sig_01HR7S6A7F3Z9N2X4M8Q1V0A08"
canonical_url_refs:
  - "https://www.bilibili.com/video/BV1zhoUB1Ebg/"
confidence_label: "low"
user_verdict: "pending"
verdict_history:
  -
    at: "2026-05-07T00:00:00+08:00"
    actor: "single_user"
    verdict: "pending"
    reason: "fixture exercise of state machine"
lifecycle_state: "draft"
capture_plan_refs:
  - "plan_01HR7S6A7F3Z9N2X4M8Q1V0A05"
conflict_policy: "show_support_and_counter_before_any_plan"
claim_label_map:
  canonical_fields:
    - "id"
    - "source_capture_ids"
  candidate_fields:
    - "claim_text"
    - "support_signal_ids"
    - "counter_signal_ids"
  tentative_fields:
    - "confidence_label"
    - "user_verdict"
cascade_revert_policy: "if rejected, linked plan moves to suspended_pending_user_review"
notes: "Candidate hypothesis fixture; no scoring engine or recommendation runtime approval."
```
[candidate] Audit note 05: this sample intentionally uses explicit unknown/blocked states where live platform evidence is missing, preserving truthfulness while still making validators deterministic.
### Sample 06 — Hypothesis

[candidate] Sample 06 exercises Hypothesis relations using `BV1A196BpESQ`. URL shape is carried as a platform URL, but author and rich metadata remain not-live-verified.
```yaml
id: "hyp_01HR7S6A7F3Z9N2X4M8Q1V0A06"
entity_kind: "Hypothesis"
schema_version: "hypothesis.v0.candidate"
title: "H6: high_signal preview usefulness requires evidence balance"
claim_text: "For BV1A196BpESQ, topic-card usefulness is plausible only if support and counter signals remain visible."
testability: "can_be_reviewed_by_human_verdict_and_edit_cost_log"
source_capture_ids:
  - "cap_u3_06_pESQ"
support_signal_ids:
  - "sig_01HR7S6A7F3Z9N2X4M8Q1V0A06"
  - "sig_01HR7S6A7F3Z9N2X4M8Q1V0A07"
counter_signal_ids:
  - "sig_01HR7S6A7F3Z9N2X4M8Q1V0A08"
neutral_signal_ids:
  - "sig_01HR7S6A7F3Z9N2X4M8Q1V0A09"
canonical_url_refs:
  - "https://www.bilibili.com/video/BV1A196BpESQ/"
confidence_label: "medium"
user_verdict: "needs_edit"
verdict_history:
  -
    at: "2026-05-07T00:00:00+08:00"
    actor: "single_user"
    verdict: "needs_edit"
    reason: "fixture exercise of state machine"
lifecycle_state: "under_review"
capture_plan_refs:
  - "plan_01HR7S6A7F3Z9N2X4M8Q1V0A06"
conflict_policy: "show_support_and_counter_before_any_plan"
claim_label_map:
  canonical_fields:
    - "id"
    - "source_capture_ids"
  candidate_fields:
    - "claim_text"
    - "support_signal_ids"
    - "counter_signal_ids"
  tentative_fields:
    - "confidence_label"
    - "user_verdict"
cascade_revert_policy: "if rejected, linked plan moves to suspended_pending_user_review"
notes: "Candidate hypothesis fixture; no scoring engine or recommendation runtime approval."
```
[candidate] Audit note 06: this sample intentionally uses explicit unknown/blocked states where live platform evidence is missing, preserving truthfulness while still making validators deterministic.
### Sample 07 — Hypothesis

[candidate] Sample 07 exercises Hypothesis relations using `BV16ooQBsEah`. URL shape is carried as a platform URL, but author and rich metadata remain not-live-verified.
```yaml
id: "hyp_01HR7S6A7F3Z9N2X4M8Q1V0A07"
entity_kind: "Hypothesis"
schema_version: "hypothesis.v0.candidate"
title: "H7: ordinary preview usefulness requires evidence balance"
claim_text: "For BV16ooQBsEah, topic-card usefulness is plausible only if support and counter signals remain visible."
testability: "can_be_reviewed_by_human_verdict_and_edit_cost_log"
source_capture_ids:
  - "cap_u3_07_sEah"
support_signal_ids:
  - "sig_01HR7S6A7F3Z9N2X4M8Q1V0A07"
  - "sig_01HR7S6A7F3Z9N2X4M8Q1V0A08"
counter_signal_ids:
  - "sig_01HR7S6A7F3Z9N2X4M8Q1V0A09"
neutral_signal_ids:
  - "sig_01HR7S6A7F3Z9N2X4M8Q1V0A10"
canonical_url_refs:
  - "https://www.bilibili.com/video/BV16ooQBsEah/"
confidence_label: "medium"
user_verdict: "follow"
verdict_history:
  -
    at: "2026-05-07T00:00:00+08:00"
    actor: "single_user"
    verdict: "follow"
    reason: "fixture exercise of state machine"
lifecycle_state: "accepted_for_plan"
capture_plan_refs:
  - "plan_01HR7S6A7F3Z9N2X4M8Q1V0A07"
conflict_policy: "show_support_and_counter_before_any_plan"
claim_label_map:
  canonical_fields:
    - "id"
    - "source_capture_ids"
  candidate_fields:
    - "claim_text"
    - "support_signal_ids"
    - "counter_signal_ids"
  tentative_fields:
    - "confidence_label"
    - "user_verdict"
cascade_revert_policy: "if rejected, linked plan moves to suspended_pending_user_review"
notes: "Candidate hypothesis fixture; no scoring engine or recommendation runtime approval."
```
[candidate] Audit note 07: this sample intentionally uses explicit unknown/blocked states where live platform evidence is missing, preserving truthfulness while still making validators deterministic.
### Sample 08 — Hypothesis

[candidate] Sample 08 exercises Hypothesis relations using `BV1zhoUB1Ebg`. URL shape is carried as a platform URL, but author and rich metadata remain not-live-verified.
```yaml
id: "hyp_01HR7S6A7F3Z9N2X4M8Q1V0A08"
entity_kind: "Hypothesis"
schema_version: "hypothesis.v0.candidate"
title: "H8: edge preview usefulness requires evidence balance"
claim_text: "For BV1zhoUB1Ebg, topic-card usefulness is plausible only if support and counter signals remain visible."
testability: "can_be_reviewed_by_human_verdict_and_edit_cost_log"
source_capture_ids:
  - "cap_u3_08_1Ebg"
support_signal_ids:
  - "sig_01HR7S6A7F3Z9N2X4M8Q1V0A08"
  - "sig_01HR7S6A7F3Z9N2X4M8Q1V0A09"
counter_signal_ids:
  - "sig_01HR7S6A7F3Z9N2X4M8Q1V0A10"
neutral_signal_ids:
  - "sig_01HR7S6A7F3Z9N2X4M8Q1V0A01"
canonical_url_refs:
  - "https://www.bilibili.com/video/BV1zhoUB1Ebg/"
confidence_label: "low"
user_verdict: "reject"
verdict_history:
  -
    at: "2026-05-07T00:00:00+08:00"
    actor: "single_user"
    verdict: "reject"
    reason: "fixture exercise of state machine"
lifecycle_state: "rejected"
capture_plan_refs:
  - "plan_01HR7S6A7F3Z9N2X4M8Q1V0A08"
conflict_policy: "show_support_and_counter_before_any_plan"
claim_label_map:
  canonical_fields:
    - "id"
    - "source_capture_ids"
  candidate_fields:
    - "claim_text"
    - "support_signal_ids"
    - "counter_signal_ids"
  tentative_fields:
    - "confidence_label"
    - "user_verdict"
cascade_revert_policy: "if rejected, linked plan moves to suspended_pending_user_review"
notes: "Candidate hypothesis fixture; no scoring engine or recommendation runtime approval."
```
[candidate] Audit note 08: this sample intentionally uses explicit unknown/blocked states where live platform evidence is missing, preserving truthfulness while still making validators deterministic.
### Sample 09 — Hypothesis

[candidate] Sample 09 exercises Hypothesis relations using `BV1A196BpESQ`. URL shape is carried as a platform URL, but author and rich metadata remain not-live-verified.
```yaml
id: "hyp_01HR7S6A7F3Z9N2X4M8Q1V0A09"
entity_kind: "Hypothesis"
schema_version: "hypothesis.v0.candidate"
title: "H9: high_signal preview usefulness requires evidence balance"
claim_text: "For BV1A196BpESQ, topic-card usefulness is plausible only if support and counter signals remain visible."
testability: "can_be_reviewed_by_human_verdict_and_edit_cost_log"
source_capture_ids:
  - "cap_u3_09_pESQ"
support_signal_ids:
  - "sig_01HR7S6A7F3Z9N2X4M8Q1V0A09"
  - "sig_01HR7S6A7F3Z9N2X4M8Q1V0A10"
counter_signal_ids:
  - "sig_01HR7S6A7F3Z9N2X4M8Q1V0A01"
neutral_signal_ids:
  - "sig_01HR7S6A7F3Z9N2X4M8Q1V0A02"
canonical_url_refs:
  - "https://www.bilibili.com/video/BV1A196BpESQ/"
confidence_label: "parking_lot"
user_verdict: "park"
verdict_history:
  -
    at: "2026-05-07T00:00:00+08:00"
    actor: "single_user"
    verdict: "park"
    reason: "fixture exercise of state machine"
lifecycle_state: "archived"
capture_plan_refs:
  - "plan_01HR7S6A7F3Z9N2X4M8Q1V0A09"
conflict_policy: "show_support_and_counter_before_any_plan"
claim_label_map:
  canonical_fields:
    - "id"
    - "source_capture_ids"
  candidate_fields:
    - "claim_text"
    - "support_signal_ids"
    - "counter_signal_ids"
  tentative_fields:
    - "confidence_label"
    - "user_verdict"
cascade_revert_policy: "if rejected, linked plan moves to suspended_pending_user_review"
notes: "Candidate hypothesis fixture; no scoring engine or recommendation runtime approval."
```
[candidate] Audit note 09: this sample intentionally uses explicit unknown/blocked states where live platform evidence is missing, preserving truthfulness while still making validators deterministic.
### Sample 10 — Hypothesis

[candidate] Sample 10 exercises Hypothesis relations using `BV16ooQBsEah`. URL shape is carried as a platform URL, but author and rich metadata remain not-live-verified.
```yaml
id: "hyp_01HR7S6A7F3Z9N2X4M8Q1V0A10"
entity_kind: "Hypothesis"
schema_version: "hypothesis.v0.candidate"
title: "H10: ordinary preview usefulness requires evidence balance"
claim_text: "For BV16ooQBsEah, topic-card usefulness is plausible only if support and counter signals remain visible."
testability: "can_be_reviewed_by_human_verdict_and_edit_cost_log"
source_capture_ids:
  - "cap_u3_10_sEah"
support_signal_ids:
  - "sig_01HR7S6A7F3Z9N2X4M8Q1V0A10"
  - "sig_01HR7S6A7F3Z9N2X4M8Q1V0A01"
counter_signal_ids:
  - "sig_01HR7S6A7F3Z9N2X4M8Q1V0A02"
neutral_signal_ids:
  - "sig_01HR7S6A7F3Z9N2X4M8Q1V0A03"
canonical_url_refs:
  - "https://www.bilibili.com/video/BV16ooQBsEah/"
confidence_label: "low"
user_verdict: "pending"
verdict_history:
  -
    at: "2026-05-07T00:00:00+08:00"
    actor: "single_user"
    verdict: "pending"
    reason: "fixture exercise of state machine"
lifecycle_state: "draft"
capture_plan_refs:
  - "plan_01HR7S6A7F3Z9N2X4M8Q1V0A10"
conflict_policy: "show_support_and_counter_before_any_plan"
claim_label_map:
  canonical_fields:
    - "id"
    - "source_capture_ids"
  candidate_fields:
    - "claim_text"
    - "support_signal_ids"
    - "counter_signal_ids"
  tentative_fields:
    - "confidence_label"
    - "user_verdict"
cascade_revert_policy: "if rejected, linked plan moves to suspended_pending_user_review"
notes: "Candidate hypothesis fixture; no scoring engine or recommendation runtime approval."
```
[candidate] Audit note 10: this sample intentionally uses explicit unknown/blocked states where live platform evidence is missing, preserving truthfulness while still making validators deterministic.

## §3 Fixture validation checklist

[candidate] Every sample has an id shaped as a stable candidate identifier.
[candidate] Every sample carries capture linkage or explains why it cannot become capture authority.
[candidate] Every sample preserves LP-001: no recommendation, keyword, RAW gap, playlist, account, or comment expansion is turned into direct capture.
[candidate] Every sample marks author metadata as not live verified.
[candidate] Every sample includes a lifecycle state and a claim_label_map.


## §4 Reviewer scenarios for second-pass audit

[candidate] Scenario 01: The reviewer should inspect the Hypothesis sample as a fixture for evidence balance, user verdict gates, conflict explanation, and cascade behavior toward CapturePlan. The pass condition is not that the sample looks semantically rich; the pass condition is that the sample can survive a skeptical audit without pretending that live metadata, author identity, runtime capture, RAW intake, or DiloFlow execution has been verified. When the sample uses `UNKNOWN_NOT_LIVE_VERIFIED`, that value is a successful honesty marker rather than an incomplete field.
[tentative] Scenario 01 failure mode: if a future agent replaces explicit unknowns with guessed author names, guessed follower counts, guessed title quality, or guessed platform state, the fixture should fail even if the rest of the JSON shape validates. This rule is especially important because sample data can quietly become seed data; the supplement blocks that drift by repeating not-authority frontmatter and candidate-only notes.
[candidate] Scenario 02: The reviewer should inspect the Hypothesis sample as a fixture for evidence balance, user verdict gates, conflict explanation, and cascade behavior toward CapturePlan. The pass condition is not that the sample looks semantically rich; the pass condition is that the sample can survive a skeptical audit without pretending that live metadata, author identity, runtime capture, RAW intake, or DiloFlow execution has been verified. When the sample uses `UNKNOWN_NOT_LIVE_VERIFIED`, that value is a successful honesty marker rather than an incomplete field.
[tentative] Scenario 02 failure mode: if a future agent replaces explicit unknowns with guessed author names, guessed follower counts, guessed title quality, or guessed platform state, the fixture should fail even if the rest of the JSON shape validates. This rule is especially important because sample data can quietly become seed data; the supplement blocks that drift by repeating not-authority frontmatter and candidate-only notes.
[candidate] Scenario 03: The reviewer should inspect the Hypothesis sample as a fixture for evidence balance, user verdict gates, conflict explanation, and cascade behavior toward CapturePlan. The pass condition is not that the sample looks semantically rich; the pass condition is that the sample can survive a skeptical audit without pretending that live metadata, author identity, runtime capture, RAW intake, or DiloFlow execution has been verified. When the sample uses `UNKNOWN_NOT_LIVE_VERIFIED`, that value is a successful honesty marker rather than an incomplete field.
[tentative] Scenario 03 failure mode: if a future agent replaces explicit unknowns with guessed author names, guessed follower counts, guessed title quality, or guessed platform state, the fixture should fail even if the rest of the JSON shape validates. This rule is especially important because sample data can quietly become seed data; the supplement blocks that drift by repeating not-authority frontmatter and candidate-only notes.
[candidate] Scenario 04: The reviewer should inspect the Hypothesis sample as a fixture for evidence balance, user verdict gates, conflict explanation, and cascade behavior toward CapturePlan. The pass condition is not that the sample looks semantically rich; the pass condition is that the sample can survive a skeptical audit without pretending that live metadata, author identity, runtime capture, RAW intake, or DiloFlow execution has been verified. When the sample uses `UNKNOWN_NOT_LIVE_VERIFIED`, that value is a successful honesty marker rather than an incomplete field.
[tentative] Scenario 04 failure mode: if a future agent replaces explicit unknowns with guessed author names, guessed follower counts, guessed title quality, or guessed platform state, the fixture should fail even if the rest of the JSON shape validates. This rule is especially important because sample data can quietly become seed data; the supplement blocks that drift by repeating not-authority frontmatter and candidate-only notes.
[candidate] Scenario 05: The reviewer should inspect the Hypothesis sample as a fixture for evidence balance, user verdict gates, conflict explanation, and cascade behavior toward CapturePlan. The pass condition is not that the sample looks semantically rich; the pass condition is that the sample can survive a skeptical audit without pretending that live metadata, author identity, runtime capture, RAW intake, or DiloFlow execution has been verified. When the sample uses `UNKNOWN_NOT_LIVE_VERIFIED`, that value is a successful honesty marker rather than an incomplete field.
[tentative] Scenario 05 failure mode: if a future agent replaces explicit unknowns with guessed author names, guessed follower counts, guessed title quality, or guessed platform state, the fixture should fail even if the rest of the JSON shape validates. This rule is especially important because sample data can quietly become seed data; the supplement blocks that drift by repeating not-authority frontmatter and candidate-only notes.
[candidate] Scenario 06: The reviewer should inspect the Hypothesis sample as a fixture for evidence balance, user verdict gates, conflict explanation, and cascade behavior toward CapturePlan. The pass condition is not that the sample looks semantically rich; the pass condition is that the sample can survive a skeptical audit without pretending that live metadata, author identity, runtime capture, RAW intake, or DiloFlow execution has been verified. When the sample uses `UNKNOWN_NOT_LIVE_VERIFIED`, that value is a successful honesty marker rather than an incomplete field.
[tentative] Scenario 06 failure mode: if a future agent replaces explicit unknowns with guessed author names, guessed follower counts, guessed title quality, or guessed platform state, the fixture should fail even if the rest of the JSON shape validates. This rule is especially important because sample data can quietly become seed data; the supplement blocks that drift by repeating not-authority frontmatter and candidate-only notes.
[candidate] Scenario 07: The reviewer should inspect the Hypothesis sample as a fixture for evidence balance, user verdict gates, conflict explanation, and cascade behavior toward CapturePlan. The pass condition is not that the sample looks semantically rich; the pass condition is that the sample can survive a skeptical audit without pretending that live metadata, author identity, runtime capture, RAW intake, or DiloFlow execution has been verified. When the sample uses `UNKNOWN_NOT_LIVE_VERIFIED`, that value is a successful honesty marker rather than an incomplete field.
[tentative] Scenario 07 failure mode: if a future agent replaces explicit unknowns with guessed author names, guessed follower counts, guessed title quality, or guessed platform state, the fixture should fail even if the rest of the JSON shape validates. This rule is especially important because sample data can quietly become seed data; the supplement blocks that drift by repeating not-authority frontmatter and candidate-only notes.
[candidate] Scenario 08: The reviewer should inspect the Hypothesis sample as a fixture for evidence balance, user verdict gates, conflict explanation, and cascade behavior toward CapturePlan. The pass condition is not that the sample looks semantically rich; the pass condition is that the sample can survive a skeptical audit without pretending that live metadata, author identity, runtime capture, RAW intake, or DiloFlow execution has been verified. When the sample uses `UNKNOWN_NOT_LIVE_VERIFIED`, that value is a successful honesty marker rather than an incomplete field.
[tentative] Scenario 08 failure mode: if a future agent replaces explicit unknowns with guessed author names, guessed follower counts, guessed title quality, or guessed platform state, the fixture should fail even if the rest of the JSON shape validates. This rule is especially important because sample data can quietly become seed data; the supplement blocks that drift by repeating not-authority frontmatter and candidate-only notes.
[candidate] Scenario 09: The reviewer should inspect the Hypothesis sample as a fixture for evidence balance, user verdict gates, conflict explanation, and cascade behavior toward CapturePlan. The pass condition is not that the sample looks semantically rich; the pass condition is that the sample can survive a skeptical audit without pretending that live metadata, author identity, runtime capture, RAW intake, or DiloFlow execution has been verified. When the sample uses `UNKNOWN_NOT_LIVE_VERIFIED`, that value is a successful honesty marker rather than an incomplete field.
[tentative] Scenario 09 failure mode: if a future agent replaces explicit unknowns with guessed author names, guessed follower counts, guessed title quality, or guessed platform state, the fixture should fail even if the rest of the JSON shape validates. This rule is especially important because sample data can quietly become seed data; the supplement blocks that drift by repeating not-authority frontmatter and candidate-only notes.
[candidate] Scenario 10: The reviewer should inspect the Hypothesis sample as a fixture for evidence balance, user verdict gates, conflict explanation, and cascade behavior toward CapturePlan. The pass condition is not that the sample looks semantically rich; the pass condition is that the sample can survive a skeptical audit without pretending that live metadata, author identity, runtime capture, RAW intake, or DiloFlow execution has been verified. When the sample uses `UNKNOWN_NOT_LIVE_VERIFIED`, that value is a successful honesty marker rather than an incomplete field.
[tentative] Scenario 10 failure mode: if a future agent replaces explicit unknowns with guessed author names, guessed follower counts, guessed title quality, or guessed platform state, the fixture should fail even if the rest of the JSON shape validates. This rule is especially important because sample data can quietly become seed data; the supplement blocks that drift by repeating not-authority frontmatter and candidate-only notes.
[candidate] Scenario 11: The reviewer should inspect the Hypothesis sample as a fixture for evidence balance, user verdict gates, conflict explanation, and cascade behavior toward CapturePlan. The pass condition is not that the sample looks semantically rich; the pass condition is that the sample can survive a skeptical audit without pretending that live metadata, author identity, runtime capture, RAW intake, or DiloFlow execution has been verified. When the sample uses `UNKNOWN_NOT_LIVE_VERIFIED`, that value is a successful honesty marker rather than an incomplete field.
[tentative] Scenario 11 failure mode: if a future agent replaces explicit unknowns with guessed author names, guessed follower counts, guessed title quality, or guessed platform state, the fixture should fail even if the rest of the JSON shape validates. This rule is especially important because sample data can quietly become seed data; the supplement blocks that drift by repeating not-authority frontmatter and candidate-only notes.
[candidate] Scenario 12: The reviewer should inspect the Hypothesis sample as a fixture for evidence balance, user verdict gates, conflict explanation, and cascade behavior toward CapturePlan. The pass condition is not that the sample looks semantically rich; the pass condition is that the sample can survive a skeptical audit without pretending that live metadata, author identity, runtime capture, RAW intake, or DiloFlow execution has been verified. When the sample uses `UNKNOWN_NOT_LIVE_VERIFIED`, that value is a successful honesty marker rather than an incomplete field.
[tentative] Scenario 12 failure mode: if a future agent replaces explicit unknowns with guessed author names, guessed follower counts, guessed title quality, or guessed platform state, the fixture should fail even if the rest of the JSON shape validates. This rule is especially important because sample data can quietly become seed data; the supplement blocks that drift by repeating not-authority frontmatter and candidate-only notes.

## §5 Field-level audit expansion

[candidate] Field `id` must be read as a fixture contract field. The reviewer should ask three questions: is the field populated, is its claim label clear, and does the value avoid smuggling runtime or authority approval? For Hypothesis, a populated field can still be an explicit `not-approved`, `not_live_verified_in_this_environment`, `blocked_runtime`, or `candidate_only` value; those values are preferable to attractive but unverifiable details.
[candidate] Field `schema_version` must be read as a fixture contract field. The reviewer should ask three questions: is the field populated, is its claim label clear, and does the value avoid smuggling runtime or authority approval? For Hypothesis, a populated field can still be an explicit `not-approved`, `not_live_verified_in_this_environment`, `blocked_runtime`, or `candidate_only` value; those values are preferable to attractive but unverifiable details.
[candidate] Field `source_capture_id` must be read as a fixture contract field. The reviewer should ask three questions: is the field populated, is its claim label clear, and does the value avoid smuggling runtime or authority approval? For Hypothesis, a populated field can still be an explicit `not-approved`, `not_live_verified_in_this_environment`, `blocked_runtime`, or `candidate_only` value; those values are preferable to attractive but unverifiable details.
[candidate] Field `canonical_url` must be read as a fixture contract field. The reviewer should ask three questions: is the field populated, is its claim label clear, and does the value avoid smuggling runtime or authority approval? For Hypothesis, a populated field can still be an explicit `not-approved`, `not_live_verified_in_this_environment`, `blocked_runtime`, or `candidate_only` value; those values are preferable to attractive but unverifiable details.
[candidate] Field `platform_item_id` must be read as a fixture contract field. The reviewer should ask three questions: is the field populated, is its claim label clear, and does the value avoid smuggling runtime or authority approval? For Hypothesis, a populated field can still be an explicit `not-approved`, `not_live_verified_in_this_environment`, `blocked_runtime`, or `candidate_only` value; those values are preferable to attractive but unverifiable details.
[candidate] Field `lifecycle_state` must be read as a fixture contract field. The reviewer should ask three questions: is the field populated, is its claim label clear, and does the value avoid smuggling runtime or authority approval? For Hypothesis, a populated field can still be an explicit `not-approved`, `not_live_verified_in_this_environment`, `blocked_runtime`, or `candidate_only` value; those values are preferable to attractive but unverifiable details.
[candidate] Field `claim_label_map` must be read as a fixture contract field. The reviewer should ask three questions: is the field populated, is its claim label clear, and does the value avoid smuggling runtime or authority approval? For Hypothesis, a populated field can still be an explicit `not-approved`, `not_live_verified_in_this_environment`, `blocked_runtime`, or `candidate_only` value; those values are preferable to attractive but unverifiable details.
[candidate] Field `evidence_refs` must be read as a fixture contract field. The reviewer should ask three questions: is the field populated, is its claim label clear, and does the value avoid smuggling runtime or authority approval? For Hypothesis, a populated field can still be an explicit `not-approved`, `not_live_verified_in_this_environment`, `blocked_runtime`, or `candidate_only` value; those values are preferable to attractive but unverifiable details.
[candidate] Field `verification_state` must be read as a fixture contract field. The reviewer should ask three questions: is the field populated, is its claim label clear, and does the value avoid smuggling runtime or authority approval? For Hypothesis, a populated field can still be an explicit `not-approved`, `not_live_verified_in_this_environment`, `blocked_runtime`, or `candidate_only` value; those values are preferable to attractive but unverifiable details.
[candidate] Field `notes` must be read as a fixture contract field. The reviewer should ask three questions: is the field populated, is its claim label clear, and does the value avoid smuggling runtime or authority approval? For Hypothesis, a populated field can still be an explicit `not-approved`, `not_live_verified_in_this_environment`, `blocked_runtime`, or `candidate_only` value; those values are preferable to attractive but unverifiable details.

## §6 Downstream fixture-use guidance

[candidate] U1 SRD-v3 outline drafting: use Hypothesis samples as bounded design input only. A consumer may copy the field names into a checklist, but should not copy the instances into an authority database. The safe reuse pattern is fixture → audit question → amendment text, not fixture → migration → runtime.
[candidate] U2 Lane-4/5 unlock discussion: use Hypothesis samples as bounded design input only. A consumer may copy the field names into a checklist, but should not copy the instances into an authority database. The safe reuse pattern is fixture → audit question → amendment text, not fixture → migration → runtime.
[candidate] PF-C1 topic-card preview regression review: use Hypothesis samples as bounded design input only. A consumer may copy the field names into a checklist, but should not copy the instances into an authority database. The safe reuse pattern is fixture → audit question → amendment text, not fixture → migration → runtime.
[candidate] PF-C2 RAW handoff negative testing: use Hypothesis samples as bounded design input only. A consumer may copy the field names into a checklist, but should not copy the instances into an authority database. The safe reuse pattern is fixture → audit question → amendment text, not fixture → migration → runtime.
[candidate] future C4 dispatch UI projection sketch: use Hypothesis samples as bounded design input only. A consumer may copy the field names into a checklist, but should not copy the instances into an authority database. The safe reuse pattern is fixture → audit question → amendment text, not fixture → migration → runtime.
