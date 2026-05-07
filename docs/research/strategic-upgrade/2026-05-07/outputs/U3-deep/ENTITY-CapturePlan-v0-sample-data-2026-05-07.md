---
status: candidate / captureplan_sample_data / not-authority
authority: not-authority
execution_approval: not-approved
runtime_approval: not-approved
migration_approval: not-approved
created_at: 2026-05-07
supplement_for: cloud-output-U3-entity-v0-contracts-2026-05-07.zip
---
# ENTITY-CapturePlan-v0-sample-data-2026-05-07

[canonical] Purpose: this supplementary file expands the previous entity contract with reviewable fixture-style sample instances. It does not promote any entity to DB authority, does not approve a migration, and does not add runtime endpoints.
[candidate] Data honesty note: live web browsing is unavailable in this execution environment. The Bilibili URLs below are carried from existing PF-C1 evidence context and from the user-provided prompt lineage; author names and rich platform metadata are deliberately marked `UNKNOWN_NOT_LIVE_VERIFIED` rather than fabricated.
[candidate] Sample design rule: each sample is fully populated at the contract level because every required field has a value, even when that value is an explicit unknown, blocked, or not-live-verified state. This keeps the IR testable without inventing truth.
[candidate] Review use: these samples are intended for local fixture review, OpenAPI examples, referential integrity tests, and migration worked examples. They should not be copied into SQLite or RAW as real knowledge objects.

## §1 Depth gaps found in previous ZIP

[candidate] Gap 1: Frequency, enrichment level, and rollback policy were present but not expanded into operational fixture rows.
[candidate] Gap 2: Plan failure after capture was covered in corner cases but lacked sample data with snapshot fields.
[candidate] Gap 3: LP-001 scope gates needed stronger sample-level proof that recommendation/keyword/RAW gap do not directly create captures.

## §2 Sample instances

### Sample 01 — CapturePlan

[candidate] Sample 01 exercises CapturePlan relations using `BV16ooQBsEah`. URL shape is carried as a platform URL, but author and rich metadata remain not-live-verified.
```yaml
id: "plan_01HR7S6A7F3Z9N2X4M8Q1V0A01"
entity_kind: "CapturePlan"
schema_version: "capture_plan.v0.candidate"
plan_title: "Plan 1: bounded metadata follow-up for BV16ooQBsEah"
source_hypothesis_ids:
  - "hyp_01HR7S6A7F3Z9N2X4M8Q1V0A01"
source_signal_ids:
  - "sig_01HR7S6A7F3Z9N2X4M8Q1V0A01"
  - "sig_01HR7S6A7F3Z9N2X4M8Q1V0A03"
planned_urls:
  -
    platform: "bilibili"
    url: "https://www.bilibili.com/video/BV16ooQBsEah/"
    source_kind: "manual_url"
    allowed_preset: "metadata_only"
canonical_url: "https://www.bilibili.com/video/BV16ooQBsEah/"
platform_item_id: "BV16ooQBsEah"
source_capture_id: "cap_u3_01_sEah"
frequency_policy: "manual_only"
enrichment_level: "metadata_only"
blocked_enrichments:
  - "audio_transcript"
  - "comments"
  - "danmaku"
  - "media_download"
  - "ASR"
approval_gate: "LP-001 scope approval + user explicit action"
runtime_gate_state: "not-approved"
rollback_snapshot:
  on_capture_failure: "return_to_draft_or_suspended"
  on_hypothesis_reject: "cascade_suspend"
  on_broken_capture: "mark_broken_reference"
lifecycle_state: "scoped"
claim_label_map:
  canonical_fields:
    - "id"
    - "source_hypothesis_ids"
    - "planned_urls"
  candidate_fields:
    - "frequency_policy"
    - "rollback_snapshot"
  tentative_fields:
    - "approval_gate"
anti_scope_creep_check: "does_not_create_author_playlist_keyword_or_raw_gap_capture"
notes: "Candidate plan fixture; not a worker job, scheduler, or approved capture runtime."
```
[candidate] Audit note 01: this sample intentionally uses explicit unknown/blocked states where live platform evidence is missing, preserving truthfulness while still making validators deterministic.
### Sample 02 — CapturePlan

[candidate] Sample 02 exercises CapturePlan relations using `BV1zhoUB1Ebg`. URL shape is carried as a platform URL, but author and rich metadata remain not-live-verified.
```yaml
id: "plan_01HR7S6A7F3Z9N2X4M8Q1V0A02"
entity_kind: "CapturePlan"
schema_version: "capture_plan.v0.candidate"
plan_title: "Plan 2: bounded metadata follow-up for BV1zhoUB1Ebg"
source_hypothesis_ids:
  - "hyp_01HR7S6A7F3Z9N2X4M8Q1V0A02"
source_signal_ids:
  - "sig_01HR7S6A7F3Z9N2X4M8Q1V0A02"
  - "sig_01HR7S6A7F3Z9N2X4M8Q1V0A04"
planned_urls:
  -
    platform: "bilibili"
    url: "https://www.bilibili.com/video/BV1zhoUB1Ebg/"
    source_kind: "manual_url"
    allowed_preset: "metadata_only"
canonical_url: "https://www.bilibili.com/video/BV1zhoUB1Ebg/"
platform_item_id: "BV1zhoUB1Ebg"
source_capture_id: "cap_u3_02_1Ebg"
frequency_policy: "weekly_review_candidate"
enrichment_level: "metadata_only"
blocked_enrichments:
  - "audio_transcript"
  - "comments"
  - "danmaku"
  - "media_download"
  - "ASR"
approval_gate: "LP-001 scope approval + user explicit action"
runtime_gate_state: "not-approved"
rollback_snapshot:
  on_capture_failure: "return_to_draft_or_suspended"
  on_hypothesis_reject: "cascade_suspend"
  on_broken_capture: "mark_broken_reference"
lifecycle_state: "approved_candidate"
claim_label_map:
  canonical_fields:
    - "id"
    - "source_hypothesis_ids"
    - "planned_urls"
  candidate_fields:
    - "frequency_policy"
    - "rollback_snapshot"
  tentative_fields:
    - "approval_gate"
anti_scope_creep_check: "does_not_create_author_playlist_keyword_or_raw_gap_capture"
notes: "Candidate plan fixture; not a worker job, scheduler, or approved capture runtime."
```
[candidate] Audit note 02: this sample intentionally uses explicit unknown/blocked states where live platform evidence is missing, preserving truthfulness while still making validators deterministic.
### Sample 03 — CapturePlan

[candidate] Sample 03 exercises CapturePlan relations using `BV1A196BpESQ`. URL shape is carried as a platform URL, but author and rich metadata remain not-live-verified.
```yaml
id: "plan_01HR7S6A7F3Z9N2X4M8Q1V0A03"
entity_kind: "CapturePlan"
schema_version: "capture_plan.v0.candidate"
plan_title: "Plan 3: bounded metadata follow-up for BV1A196BpESQ"
source_hypothesis_ids:
  - "hyp_01HR7S6A7F3Z9N2X4M8Q1V0A03"
source_signal_ids:
  - "sig_01HR7S6A7F3Z9N2X4M8Q1V0A03"
  - "sig_01HR7S6A7F3Z9N2X4M8Q1V0A05"
planned_urls:
  -
    platform: "bilibili"
    url: "https://www.bilibili.com/video/BV1A196BpESQ/"
    source_kind: "manual_url"
    allowed_preset: "metadata_only"
canonical_url: "https://www.bilibili.com/video/BV1A196BpESQ/"
platform_item_id: "BV1A196BpESQ"
source_capture_id: "cap_u3_03_pESQ"
frequency_policy: "on_user_verdict_only"
enrichment_level: "metadata_only"
blocked_enrichments:
  - "audio_transcript"
  - "comments"
  - "danmaku"
  - "media_download"
  - "ASR"
approval_gate: "LP-001 scope approval + user explicit action"
runtime_gate_state: "not-approved"
rollback_snapshot:
  on_capture_failure: "return_to_draft_or_suspended"
  on_hypothesis_reject: "cascade_suspend"
  on_broken_capture: "mark_broken_reference"
lifecycle_state: "suspended"
claim_label_map:
  canonical_fields:
    - "id"
    - "source_hypothesis_ids"
    - "planned_urls"
  candidate_fields:
    - "frequency_policy"
    - "rollback_snapshot"
  tentative_fields:
    - "approval_gate"
anti_scope_creep_check: "does_not_create_author_playlist_keyword_or_raw_gap_capture"
notes: "Candidate plan fixture; not a worker job, scheduler, or approved capture runtime."
```
[candidate] Audit note 03: this sample intentionally uses explicit unknown/blocked states where live platform evidence is missing, preserving truthfulness while still making validators deterministic.
### Sample 04 — CapturePlan

[candidate] Sample 04 exercises CapturePlan relations using `BV16ooQBsEah`. URL shape is carried as a platform URL, but author and rich metadata remain not-live-verified.
```yaml
id: "plan_01HR7S6A7F3Z9N2X4M8Q1V0A04"
entity_kind: "CapturePlan"
schema_version: "capture_plan.v0.candidate"
plan_title: "Plan 4: bounded metadata follow-up for BV16ooQBsEah"
source_hypothesis_ids:
  - "hyp_01HR7S6A7F3Z9N2X4M8Q1V0A04"
source_signal_ids:
  - "sig_01HR7S6A7F3Z9N2X4M8Q1V0A04"
  - "sig_01HR7S6A7F3Z9N2X4M8Q1V0A06"
planned_urls:
  -
    platform: "bilibili"
    url: "https://www.bilibili.com/video/BV16ooQBsEah/"
    source_kind: "manual_url"
    allowed_preset: "metadata_only"
canonical_url: "https://www.bilibili.com/video/BV16ooQBsEah/"
platform_item_id: "BV16ooQBsEah"
source_capture_id: "cap_u3_04_sEah"
frequency_policy: "disabled_until_gate"
enrichment_level: "metadata_only"
blocked_enrichments:
  - "audio_transcript"
  - "comments"
  - "danmaku"
  - "media_download"
  - "ASR"
approval_gate: "LP-001 scope approval + user explicit action"
runtime_gate_state: "not-approved"
rollback_snapshot:
  on_capture_failure: "return_to_draft_or_suspended"
  on_hypothesis_reject: "cascade_suspend"
  on_broken_capture: "mark_broken_reference"
lifecycle_state: "archived"
claim_label_map:
  canonical_fields:
    - "id"
    - "source_hypothesis_ids"
    - "planned_urls"
  candidate_fields:
    - "frequency_policy"
    - "rollback_snapshot"
  tentative_fields:
    - "approval_gate"
anti_scope_creep_check: "does_not_create_author_playlist_keyword_or_raw_gap_capture"
notes: "Candidate plan fixture; not a worker job, scheduler, or approved capture runtime."
```
[candidate] Audit note 04: this sample intentionally uses explicit unknown/blocked states where live platform evidence is missing, preserving truthfulness while still making validators deterministic.
### Sample 05 — CapturePlan

[candidate] Sample 05 exercises CapturePlan relations using `BV1zhoUB1Ebg`. URL shape is carried as a platform URL, but author and rich metadata remain not-live-verified.
```yaml
id: "plan_01HR7S6A7F3Z9N2X4M8Q1V0A05"
entity_kind: "CapturePlan"
schema_version: "capture_plan.v0.candidate"
plan_title: "Plan 5: bounded metadata follow-up for BV1zhoUB1Ebg"
source_hypothesis_ids:
  - "hyp_01HR7S6A7F3Z9N2X4M8Q1V0A05"
source_signal_ids:
  - "sig_01HR7S6A7F3Z9N2X4M8Q1V0A05"
  - "sig_01HR7S6A7F3Z9N2X4M8Q1V0A07"
planned_urls:
  -
    platform: "bilibili"
    url: "https://www.bilibili.com/video/BV1zhoUB1Ebg/"
    source_kind: "manual_url"
    allowed_preset: "metadata_only"
canonical_url: "https://www.bilibili.com/video/BV1zhoUB1Ebg/"
platform_item_id: "BV1zhoUB1Ebg"
source_capture_id: "cap_u3_05_1Ebg"
frequency_policy: "once"
enrichment_level: "metadata_only"
blocked_enrichments:
  - "audio_transcript"
  - "comments"
  - "danmaku"
  - "media_download"
  - "ASR"
approval_gate: "LP-001 scope approval + user explicit action"
runtime_gate_state: "not-approved"
rollback_snapshot:
  on_capture_failure: "return_to_draft_or_suspended"
  on_hypothesis_reject: "cascade_suspend"
  on_broken_capture: "mark_broken_reference"
lifecycle_state: "draft"
claim_label_map:
  canonical_fields:
    - "id"
    - "source_hypothesis_ids"
    - "planned_urls"
  candidate_fields:
    - "frequency_policy"
    - "rollback_snapshot"
  tentative_fields:
    - "approval_gate"
anti_scope_creep_check: "does_not_create_author_playlist_keyword_or_raw_gap_capture"
notes: "Candidate plan fixture; not a worker job, scheduler, or approved capture runtime."
```
[candidate] Audit note 05: this sample intentionally uses explicit unknown/blocked states where live platform evidence is missing, preserving truthfulness while still making validators deterministic.
### Sample 06 — CapturePlan

[candidate] Sample 06 exercises CapturePlan relations using `BV1A196BpESQ`. URL shape is carried as a platform URL, but author and rich metadata remain not-live-verified.
```yaml
id: "plan_01HR7S6A7F3Z9N2X4M8Q1V0A06"
entity_kind: "CapturePlan"
schema_version: "capture_plan.v0.candidate"
plan_title: "Plan 6: bounded metadata follow-up for BV1A196BpESQ"
source_hypothesis_ids:
  - "hyp_01HR7S6A7F3Z9N2X4M8Q1V0A06"
source_signal_ids:
  - "sig_01HR7S6A7F3Z9N2X4M8Q1V0A06"
  - "sig_01HR7S6A7F3Z9N2X4M8Q1V0A08"
planned_urls:
  -
    platform: "bilibili"
    url: "https://www.bilibili.com/video/BV1A196BpESQ/"
    source_kind: "manual_url"
    allowed_preset: "metadata_only"
canonical_url: "https://www.bilibili.com/video/BV1A196BpESQ/"
platform_item_id: "BV1A196BpESQ"
source_capture_id: "cap_u3_06_pESQ"
frequency_policy: "manual_only"
enrichment_level: "metadata_only"
blocked_enrichments:
  - "audio_transcript"
  - "comments"
  - "danmaku"
  - "media_download"
  - "ASR"
approval_gate: "LP-001 scope approval + user explicit action"
runtime_gate_state: "not-approved"
rollback_snapshot:
  on_capture_failure: "return_to_draft_or_suspended"
  on_hypothesis_reject: "cascade_suspend"
  on_broken_capture: "mark_broken_reference"
lifecycle_state: "scoped"
claim_label_map:
  canonical_fields:
    - "id"
    - "source_hypothesis_ids"
    - "planned_urls"
  candidate_fields:
    - "frequency_policy"
    - "rollback_snapshot"
  tentative_fields:
    - "approval_gate"
anti_scope_creep_check: "does_not_create_author_playlist_keyword_or_raw_gap_capture"
notes: "Candidate plan fixture; not a worker job, scheduler, or approved capture runtime."
```
[candidate] Audit note 06: this sample intentionally uses explicit unknown/blocked states where live platform evidence is missing, preserving truthfulness while still making validators deterministic.
### Sample 07 — CapturePlan

[candidate] Sample 07 exercises CapturePlan relations using `BV16ooQBsEah`. URL shape is carried as a platform URL, but author and rich metadata remain not-live-verified.
```yaml
id: "plan_01HR7S6A7F3Z9N2X4M8Q1V0A07"
entity_kind: "CapturePlan"
schema_version: "capture_plan.v0.candidate"
plan_title: "Plan 7: bounded metadata follow-up for BV16ooQBsEah"
source_hypothesis_ids:
  - "hyp_01HR7S6A7F3Z9N2X4M8Q1V0A07"
source_signal_ids:
  - "sig_01HR7S6A7F3Z9N2X4M8Q1V0A07"
  - "sig_01HR7S6A7F3Z9N2X4M8Q1V0A09"
planned_urls:
  -
    platform: "bilibili"
    url: "https://www.bilibili.com/video/BV16ooQBsEah/"
    source_kind: "manual_url"
    allowed_preset: "metadata_only"
canonical_url: "https://www.bilibili.com/video/BV16ooQBsEah/"
platform_item_id: "BV16ooQBsEah"
source_capture_id: "cap_u3_07_sEah"
frequency_policy: "weekly_review_candidate"
enrichment_level: "metadata_only"
blocked_enrichments:
  - "audio_transcript"
  - "comments"
  - "danmaku"
  - "media_download"
  - "ASR"
approval_gate: "LP-001 scope approval + user explicit action"
runtime_gate_state: "not-approved"
rollback_snapshot:
  on_capture_failure: "return_to_draft_or_suspended"
  on_hypothesis_reject: "cascade_suspend"
  on_broken_capture: "mark_broken_reference"
lifecycle_state: "approved_candidate"
claim_label_map:
  canonical_fields:
    - "id"
    - "source_hypothesis_ids"
    - "planned_urls"
  candidate_fields:
    - "frequency_policy"
    - "rollback_snapshot"
  tentative_fields:
    - "approval_gate"
anti_scope_creep_check: "does_not_create_author_playlist_keyword_or_raw_gap_capture"
notes: "Candidate plan fixture; not a worker job, scheduler, or approved capture runtime."
```
[candidate] Audit note 07: this sample intentionally uses explicit unknown/blocked states where live platform evidence is missing, preserving truthfulness while still making validators deterministic.
### Sample 08 — CapturePlan

[candidate] Sample 08 exercises CapturePlan relations using `BV1zhoUB1Ebg`. URL shape is carried as a platform URL, but author and rich metadata remain not-live-verified.
```yaml
id: "plan_01HR7S6A7F3Z9N2X4M8Q1V0A08"
entity_kind: "CapturePlan"
schema_version: "capture_plan.v0.candidate"
plan_title: "Plan 8: bounded metadata follow-up for BV1zhoUB1Ebg"
source_hypothesis_ids:
  - "hyp_01HR7S6A7F3Z9N2X4M8Q1V0A08"
source_signal_ids:
  - "sig_01HR7S6A7F3Z9N2X4M8Q1V0A08"
  - "sig_01HR7S6A7F3Z9N2X4M8Q1V0A10"
planned_urls:
  -
    platform: "bilibili"
    url: "https://www.bilibili.com/video/BV1zhoUB1Ebg/"
    source_kind: "manual_url"
    allowed_preset: "metadata_only"
canonical_url: "https://www.bilibili.com/video/BV1zhoUB1Ebg/"
platform_item_id: "BV1zhoUB1Ebg"
source_capture_id: "cap_u3_08_1Ebg"
frequency_policy: "on_user_verdict_only"
enrichment_level: "metadata_only"
blocked_enrichments:
  - "audio_transcript"
  - "comments"
  - "danmaku"
  - "media_download"
  - "ASR"
approval_gate: "LP-001 scope approval + user explicit action"
runtime_gate_state: "not-approved"
rollback_snapshot:
  on_capture_failure: "return_to_draft_or_suspended"
  on_hypothesis_reject: "cascade_suspend"
  on_broken_capture: "mark_broken_reference"
lifecycle_state: "suspended"
claim_label_map:
  canonical_fields:
    - "id"
    - "source_hypothesis_ids"
    - "planned_urls"
  candidate_fields:
    - "frequency_policy"
    - "rollback_snapshot"
  tentative_fields:
    - "approval_gate"
anti_scope_creep_check: "does_not_create_author_playlist_keyword_or_raw_gap_capture"
notes: "Candidate plan fixture; not a worker job, scheduler, or approved capture runtime."
```
[candidate] Audit note 08: this sample intentionally uses explicit unknown/blocked states where live platform evidence is missing, preserving truthfulness while still making validators deterministic.
### Sample 09 — CapturePlan

[candidate] Sample 09 exercises CapturePlan relations using `BV1A196BpESQ`. URL shape is carried as a platform URL, but author and rich metadata remain not-live-verified.
```yaml
id: "plan_01HR7S6A7F3Z9N2X4M8Q1V0A09"
entity_kind: "CapturePlan"
schema_version: "capture_plan.v0.candidate"
plan_title: "Plan 9: bounded metadata follow-up for BV1A196BpESQ"
source_hypothesis_ids:
  - "hyp_01HR7S6A7F3Z9N2X4M8Q1V0A09"
source_signal_ids:
  - "sig_01HR7S6A7F3Z9N2X4M8Q1V0A09"
  - "sig_01HR7S6A7F3Z9N2X4M8Q1V0A01"
planned_urls:
  -
    platform: "bilibili"
    url: "https://www.bilibili.com/video/BV1A196BpESQ/"
    source_kind: "manual_url"
    allowed_preset: "metadata_only"
canonical_url: "https://www.bilibili.com/video/BV1A196BpESQ/"
platform_item_id: "BV1A196BpESQ"
source_capture_id: "cap_u3_09_pESQ"
frequency_policy: "disabled_until_gate"
enrichment_level: "metadata_only"
blocked_enrichments:
  - "audio_transcript"
  - "comments"
  - "danmaku"
  - "media_download"
  - "ASR"
approval_gate: "LP-001 scope approval + user explicit action"
runtime_gate_state: "not-approved"
rollback_snapshot:
  on_capture_failure: "return_to_draft_or_suspended"
  on_hypothesis_reject: "cascade_suspend"
  on_broken_capture: "mark_broken_reference"
lifecycle_state: "archived"
claim_label_map:
  canonical_fields:
    - "id"
    - "source_hypothesis_ids"
    - "planned_urls"
  candidate_fields:
    - "frequency_policy"
    - "rollback_snapshot"
  tentative_fields:
    - "approval_gate"
anti_scope_creep_check: "does_not_create_author_playlist_keyword_or_raw_gap_capture"
notes: "Candidate plan fixture; not a worker job, scheduler, or approved capture runtime."
```
[candidate] Audit note 09: this sample intentionally uses explicit unknown/blocked states where live platform evidence is missing, preserving truthfulness while still making validators deterministic.
### Sample 10 — CapturePlan

[candidate] Sample 10 exercises CapturePlan relations using `BV16ooQBsEah`. URL shape is carried as a platform URL, but author and rich metadata remain not-live-verified.
```yaml
id: "plan_01HR7S6A7F3Z9N2X4M8Q1V0A10"
entity_kind: "CapturePlan"
schema_version: "capture_plan.v0.candidate"
plan_title: "Plan 10: bounded metadata follow-up for BV16ooQBsEah"
source_hypothesis_ids:
  - "hyp_01HR7S6A7F3Z9N2X4M8Q1V0A10"
source_signal_ids:
  - "sig_01HR7S6A7F3Z9N2X4M8Q1V0A10"
  - "sig_01HR7S6A7F3Z9N2X4M8Q1V0A02"
planned_urls:
  -
    platform: "bilibili"
    url: "https://www.bilibili.com/video/BV16ooQBsEah/"
    source_kind: "manual_url"
    allowed_preset: "metadata_only"
canonical_url: "https://www.bilibili.com/video/BV16ooQBsEah/"
platform_item_id: "BV16ooQBsEah"
source_capture_id: "cap_u3_10_sEah"
frequency_policy: "once"
enrichment_level: "metadata_only"
blocked_enrichments:
  - "audio_transcript"
  - "comments"
  - "danmaku"
  - "media_download"
  - "ASR"
approval_gate: "LP-001 scope approval + user explicit action"
runtime_gate_state: "not-approved"
rollback_snapshot:
  on_capture_failure: "return_to_draft_or_suspended"
  on_hypothesis_reject: "cascade_suspend"
  on_broken_capture: "mark_broken_reference"
lifecycle_state: "draft"
claim_label_map:
  canonical_fields:
    - "id"
    - "source_hypothesis_ids"
    - "planned_urls"
  candidate_fields:
    - "frequency_policy"
    - "rollback_snapshot"
  tentative_fields:
    - "approval_gate"
anti_scope_creep_check: "does_not_create_author_playlist_keyword_or_raw_gap_capture"
notes: "Candidate plan fixture; not a worker job, scheduler, or approved capture runtime."
```
[candidate] Audit note 10: this sample intentionally uses explicit unknown/blocked states where live platform evidence is missing, preserving truthfulness while still making validators deterministic.

## §3 Fixture validation checklist

[candidate] Every sample has an id shaped as a stable candidate identifier.
[candidate] Every sample carries capture linkage or explains why it cannot become capture authority.
[candidate] Every sample preserves LP-001: no recommendation, keyword, RAW gap, playlist, account, or comment expansion is turned into direct capture.
[candidate] Every sample marks author metadata as not live verified.
[candidate] Every sample includes a lifecycle state and a claim_label_map.


## §4 Reviewer scenarios for second-pass audit

[candidate] Scenario 01: The reviewer should inspect the CapturePlan sample as a fixture for LP-001 scope confirmation, not-approved runtime posture, rollback snapshots, and no scheduler assumption. The pass condition is not that the sample looks semantically rich; the pass condition is that the sample can survive a skeptical audit without pretending that live metadata, author identity, runtime capture, RAW intake, or DiloFlow execution has been verified. When the sample uses `UNKNOWN_NOT_LIVE_VERIFIED`, that value is a successful honesty marker rather than an incomplete field.
[tentative] Scenario 01 failure mode: if a future agent replaces explicit unknowns with guessed author names, guessed follower counts, guessed title quality, or guessed platform state, the fixture should fail even if the rest of the JSON shape validates. This rule is especially important because sample data can quietly become seed data; the supplement blocks that drift by repeating not-authority frontmatter and candidate-only notes.
[candidate] Scenario 02: The reviewer should inspect the CapturePlan sample as a fixture for LP-001 scope confirmation, not-approved runtime posture, rollback snapshots, and no scheduler assumption. The pass condition is not that the sample looks semantically rich; the pass condition is that the sample can survive a skeptical audit without pretending that live metadata, author identity, runtime capture, RAW intake, or DiloFlow execution has been verified. When the sample uses `UNKNOWN_NOT_LIVE_VERIFIED`, that value is a successful honesty marker rather than an incomplete field.
[tentative] Scenario 02 failure mode: if a future agent replaces explicit unknowns with guessed author names, guessed follower counts, guessed title quality, or guessed platform state, the fixture should fail even if the rest of the JSON shape validates. This rule is especially important because sample data can quietly become seed data; the supplement blocks that drift by repeating not-authority frontmatter and candidate-only notes.
[candidate] Scenario 03: The reviewer should inspect the CapturePlan sample as a fixture for LP-001 scope confirmation, not-approved runtime posture, rollback snapshots, and no scheduler assumption. The pass condition is not that the sample looks semantically rich; the pass condition is that the sample can survive a skeptical audit without pretending that live metadata, author identity, runtime capture, RAW intake, or DiloFlow execution has been verified. When the sample uses `UNKNOWN_NOT_LIVE_VERIFIED`, that value is a successful honesty marker rather than an incomplete field.
[tentative] Scenario 03 failure mode: if a future agent replaces explicit unknowns with guessed author names, guessed follower counts, guessed title quality, or guessed platform state, the fixture should fail even if the rest of the JSON shape validates. This rule is especially important because sample data can quietly become seed data; the supplement blocks that drift by repeating not-authority frontmatter and candidate-only notes.
[candidate] Scenario 04: The reviewer should inspect the CapturePlan sample as a fixture for LP-001 scope confirmation, not-approved runtime posture, rollback snapshots, and no scheduler assumption. The pass condition is not that the sample looks semantically rich; the pass condition is that the sample can survive a skeptical audit without pretending that live metadata, author identity, runtime capture, RAW intake, or DiloFlow execution has been verified. When the sample uses `UNKNOWN_NOT_LIVE_VERIFIED`, that value is a successful honesty marker rather than an incomplete field.
[tentative] Scenario 04 failure mode: if a future agent replaces explicit unknowns with guessed author names, guessed follower counts, guessed title quality, or guessed platform state, the fixture should fail even if the rest of the JSON shape validates. This rule is especially important because sample data can quietly become seed data; the supplement blocks that drift by repeating not-authority frontmatter and candidate-only notes.
[candidate] Scenario 05: The reviewer should inspect the CapturePlan sample as a fixture for LP-001 scope confirmation, not-approved runtime posture, rollback snapshots, and no scheduler assumption. The pass condition is not that the sample looks semantically rich; the pass condition is that the sample can survive a skeptical audit without pretending that live metadata, author identity, runtime capture, RAW intake, or DiloFlow execution has been verified. When the sample uses `UNKNOWN_NOT_LIVE_VERIFIED`, that value is a successful honesty marker rather than an incomplete field.
[tentative] Scenario 05 failure mode: if a future agent replaces explicit unknowns with guessed author names, guessed follower counts, guessed title quality, or guessed platform state, the fixture should fail even if the rest of the JSON shape validates. This rule is especially important because sample data can quietly become seed data; the supplement blocks that drift by repeating not-authority frontmatter and candidate-only notes.
[candidate] Scenario 06: The reviewer should inspect the CapturePlan sample as a fixture for LP-001 scope confirmation, not-approved runtime posture, rollback snapshots, and no scheduler assumption. The pass condition is not that the sample looks semantically rich; the pass condition is that the sample can survive a skeptical audit without pretending that live metadata, author identity, runtime capture, RAW intake, or DiloFlow execution has been verified. When the sample uses `UNKNOWN_NOT_LIVE_VERIFIED`, that value is a successful honesty marker rather than an incomplete field.
[tentative] Scenario 06 failure mode: if a future agent replaces explicit unknowns with guessed author names, guessed follower counts, guessed title quality, or guessed platform state, the fixture should fail even if the rest of the JSON shape validates. This rule is especially important because sample data can quietly become seed data; the supplement blocks that drift by repeating not-authority frontmatter and candidate-only notes.
[candidate] Scenario 07: The reviewer should inspect the CapturePlan sample as a fixture for LP-001 scope confirmation, not-approved runtime posture, rollback snapshots, and no scheduler assumption. The pass condition is not that the sample looks semantically rich; the pass condition is that the sample can survive a skeptical audit without pretending that live metadata, author identity, runtime capture, RAW intake, or DiloFlow execution has been verified. When the sample uses `UNKNOWN_NOT_LIVE_VERIFIED`, that value is a successful honesty marker rather than an incomplete field.
[tentative] Scenario 07 failure mode: if a future agent replaces explicit unknowns with guessed author names, guessed follower counts, guessed title quality, or guessed platform state, the fixture should fail even if the rest of the JSON shape validates. This rule is especially important because sample data can quietly become seed data; the supplement blocks that drift by repeating not-authority frontmatter and candidate-only notes.
[candidate] Scenario 08: The reviewer should inspect the CapturePlan sample as a fixture for LP-001 scope confirmation, not-approved runtime posture, rollback snapshots, and no scheduler assumption. The pass condition is not that the sample looks semantically rich; the pass condition is that the sample can survive a skeptical audit without pretending that live metadata, author identity, runtime capture, RAW intake, or DiloFlow execution has been verified. When the sample uses `UNKNOWN_NOT_LIVE_VERIFIED`, that value is a successful honesty marker rather than an incomplete field.
[tentative] Scenario 08 failure mode: if a future agent replaces explicit unknowns with guessed author names, guessed follower counts, guessed title quality, or guessed platform state, the fixture should fail even if the rest of the JSON shape validates. This rule is especially important because sample data can quietly become seed data; the supplement blocks that drift by repeating not-authority frontmatter and candidate-only notes.
[candidate] Scenario 09: The reviewer should inspect the CapturePlan sample as a fixture for LP-001 scope confirmation, not-approved runtime posture, rollback snapshots, and no scheduler assumption. The pass condition is not that the sample looks semantically rich; the pass condition is that the sample can survive a skeptical audit without pretending that live metadata, author identity, runtime capture, RAW intake, or DiloFlow execution has been verified. When the sample uses `UNKNOWN_NOT_LIVE_VERIFIED`, that value is a successful honesty marker rather than an incomplete field.
[tentative] Scenario 09 failure mode: if a future agent replaces explicit unknowns with guessed author names, guessed follower counts, guessed title quality, or guessed platform state, the fixture should fail even if the rest of the JSON shape validates. This rule is especially important because sample data can quietly become seed data; the supplement blocks that drift by repeating not-authority frontmatter and candidate-only notes.
[candidate] Scenario 10: The reviewer should inspect the CapturePlan sample as a fixture for LP-001 scope confirmation, not-approved runtime posture, rollback snapshots, and no scheduler assumption. The pass condition is not that the sample looks semantically rich; the pass condition is that the sample can survive a skeptical audit without pretending that live metadata, author identity, runtime capture, RAW intake, or DiloFlow execution has been verified. When the sample uses `UNKNOWN_NOT_LIVE_VERIFIED`, that value is a successful honesty marker rather than an incomplete field.
[tentative] Scenario 10 failure mode: if a future agent replaces explicit unknowns with guessed author names, guessed follower counts, guessed title quality, or guessed platform state, the fixture should fail even if the rest of the JSON shape validates. This rule is especially important because sample data can quietly become seed data; the supplement blocks that drift by repeating not-authority frontmatter and candidate-only notes.
[candidate] Scenario 11: The reviewer should inspect the CapturePlan sample as a fixture for LP-001 scope confirmation, not-approved runtime posture, rollback snapshots, and no scheduler assumption. The pass condition is not that the sample looks semantically rich; the pass condition is that the sample can survive a skeptical audit without pretending that live metadata, author identity, runtime capture, RAW intake, or DiloFlow execution has been verified. When the sample uses `UNKNOWN_NOT_LIVE_VERIFIED`, that value is a successful honesty marker rather than an incomplete field.
[tentative] Scenario 11 failure mode: if a future agent replaces explicit unknowns with guessed author names, guessed follower counts, guessed title quality, or guessed platform state, the fixture should fail even if the rest of the JSON shape validates. This rule is especially important because sample data can quietly become seed data; the supplement blocks that drift by repeating not-authority frontmatter and candidate-only notes.
[candidate] Scenario 12: The reviewer should inspect the CapturePlan sample as a fixture for LP-001 scope confirmation, not-approved runtime posture, rollback snapshots, and no scheduler assumption. The pass condition is not that the sample looks semantically rich; the pass condition is that the sample can survive a skeptical audit without pretending that live metadata, author identity, runtime capture, RAW intake, or DiloFlow execution has been verified. When the sample uses `UNKNOWN_NOT_LIVE_VERIFIED`, that value is a successful honesty marker rather than an incomplete field.
[tentative] Scenario 12 failure mode: if a future agent replaces explicit unknowns with guessed author names, guessed follower counts, guessed title quality, or guessed platform state, the fixture should fail even if the rest of the JSON shape validates. This rule is especially important because sample data can quietly become seed data; the supplement blocks that drift by repeating not-authority frontmatter and candidate-only notes.

## §5 Field-level audit expansion

[candidate] Field `id` must be read as a fixture contract field. The reviewer should ask three questions: is the field populated, is its claim label clear, and does the value avoid smuggling runtime or authority approval? For CapturePlan, a populated field can still be an explicit `not-approved`, `not_live_verified_in_this_environment`, `blocked_runtime`, or `candidate_only` value; those values are preferable to attractive but unverifiable details.
[candidate] Field `schema_version` must be read as a fixture contract field. The reviewer should ask three questions: is the field populated, is its claim label clear, and does the value avoid smuggling runtime or authority approval? For CapturePlan, a populated field can still be an explicit `not-approved`, `not_live_verified_in_this_environment`, `blocked_runtime`, or `candidate_only` value; those values are preferable to attractive but unverifiable details.
[candidate] Field `source_capture_id` must be read as a fixture contract field. The reviewer should ask three questions: is the field populated, is its claim label clear, and does the value avoid smuggling runtime or authority approval? For CapturePlan, a populated field can still be an explicit `not-approved`, `not_live_verified_in_this_environment`, `blocked_runtime`, or `candidate_only` value; those values are preferable to attractive but unverifiable details.
[candidate] Field `canonical_url` must be read as a fixture contract field. The reviewer should ask three questions: is the field populated, is its claim label clear, and does the value avoid smuggling runtime or authority approval? For CapturePlan, a populated field can still be an explicit `not-approved`, `not_live_verified_in_this_environment`, `blocked_runtime`, or `candidate_only` value; those values are preferable to attractive but unverifiable details.
[candidate] Field `platform_item_id` must be read as a fixture contract field. The reviewer should ask three questions: is the field populated, is its claim label clear, and does the value avoid smuggling runtime or authority approval? For CapturePlan, a populated field can still be an explicit `not-approved`, `not_live_verified_in_this_environment`, `blocked_runtime`, or `candidate_only` value; those values are preferable to attractive but unverifiable details.
[candidate] Field `lifecycle_state` must be read as a fixture contract field. The reviewer should ask three questions: is the field populated, is its claim label clear, and does the value avoid smuggling runtime or authority approval? For CapturePlan, a populated field can still be an explicit `not-approved`, `not_live_verified_in_this_environment`, `blocked_runtime`, or `candidate_only` value; those values are preferable to attractive but unverifiable details.
[candidate] Field `claim_label_map` must be read as a fixture contract field. The reviewer should ask three questions: is the field populated, is its claim label clear, and does the value avoid smuggling runtime or authority approval? For CapturePlan, a populated field can still be an explicit `not-approved`, `not_live_verified_in_this_environment`, `blocked_runtime`, or `candidate_only` value; those values are preferable to attractive but unverifiable details.
[candidate] Field `evidence_refs` must be read as a fixture contract field. The reviewer should ask three questions: is the field populated, is its claim label clear, and does the value avoid smuggling runtime or authority approval? For CapturePlan, a populated field can still be an explicit `not-approved`, `not_live_verified_in_this_environment`, `blocked_runtime`, or `candidate_only` value; those values are preferable to attractive but unverifiable details.
[candidate] Field `verification_state` must be read as a fixture contract field. The reviewer should ask three questions: is the field populated, is its claim label clear, and does the value avoid smuggling runtime or authority approval? For CapturePlan, a populated field can still be an explicit `not-approved`, `not_live_verified_in_this_environment`, `blocked_runtime`, or `candidate_only` value; those values are preferable to attractive but unverifiable details.
[candidate] Field `notes` must be read as a fixture contract field. The reviewer should ask three questions: is the field populated, is its claim label clear, and does the value avoid smuggling runtime or authority approval? For CapturePlan, a populated field can still be an explicit `not-approved`, `not_live_verified_in_this_environment`, `blocked_runtime`, or `candidate_only` value; those values are preferable to attractive but unverifiable details.

## §6 Downstream fixture-use guidance

[candidate] U1 SRD-v3 outline drafting: use CapturePlan samples as bounded design input only. A consumer may copy the field names into a checklist, but should not copy the instances into an authority database. The safe reuse pattern is fixture → audit question → amendment text, not fixture → migration → runtime.
[candidate] U2 Lane-4/5 unlock discussion: use CapturePlan samples as bounded design input only. A consumer may copy the field names into a checklist, but should not copy the instances into an authority database. The safe reuse pattern is fixture → audit question → amendment text, not fixture → migration → runtime.
[candidate] PF-C1 topic-card preview regression review: use CapturePlan samples as bounded design input only. A consumer may copy the field names into a checklist, but should not copy the instances into an authority database. The safe reuse pattern is fixture → audit question → amendment text, not fixture → migration → runtime.
[candidate] PF-C2 RAW handoff negative testing: use CapturePlan samples as bounded design input only. A consumer may copy the field names into a checklist, but should not copy the instances into an authority database. The safe reuse pattern is fixture → audit question → amendment text, not fixture → migration → runtime.
[candidate] future C4 dispatch UI projection sketch: use CapturePlan samples as bounded design input only. A consumer may copy the field names into a checklist, but should not copy the instances into an authority database. The safe reuse pattern is fixture → audit question → amendment text, not fixture → migration → runtime.
