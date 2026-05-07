---
status: candidate / signal_sample_data / not-authority
authority: not-authority
execution_approval: not-approved
runtime_approval: not-approved
migration_approval: not-approved
created_at: 2026-05-07
supplement_for: cloud-output-U3-entity-v0-contracts-2026-05-07.zip
---
# ENTITY-Signal-v0-sample-data-2026-05-07

[canonical] Purpose: this supplementary file expands the previous entity contract with reviewable fixture-style sample instances. It does not promote any entity to DB authority, does not approve a migration, and does not add runtime endpoints.
[candidate] Data honesty note: live web browsing is unavailable in this execution environment. The Bilibili URLs below are carried from existing PF-C1 evidence context and from the user-provided prompt lineage; author names and rich platform metadata are deliberately marked `UNKNOWN_NOT_LIVE_VERIFIED` rather than fabricated.
[candidate] Sample design rule: each sample is fully populated at the contract level because every required field has a value, even when that value is an explicit unknown, blocked, or not-live-verified state. This keeps the IR testable without inventing truth.
[candidate] Review use: these samples are intended for local fixture review, OpenAPI examples, referential integrity tests, and migration worked examples. They should not be copied into SQLite or RAW as real knowledge objects.

## §1 Depth gaps found in previous ZIP

[candidate] Gap 1: Samples were too few to exercise duplicate dedupe, broken reference, AI-generated observation, and cross-platform observation in one matrix.
[candidate] Gap 2: Validation state and source author uncertainty were described but not stress-tested with explicit unknown values.
[candidate] Gap 3: The anti-second-inbox rule existed at concept level, but sample rows did not show how a derived signal avoids re-emitting capture state.

## §2 Sample instances

### Sample 01 — Signal

[candidate] Sample 01 exercises Signal relations using `BV16ooQBsEah`. URL shape is carried as a platform URL, but author and rich metadata remain not-live-verified.
```yaml
id: "sig_01HR7S6A7F3Z9N2X4M8Q1V0A01"
entity_kind: "Signal"
schema_version: "signal.v0.candidate"
source_capture_id: "cap_u3_01_sEah"
platform: "bilibili"
platform_item_id: "BV16ooQBsEah"
canonical_url: "https://www.bilibili.com/video/BV16ooQBsEah/"
canonical_url_verification_state: "carried_from_existing_evidence_not_live_checked"
source_author_display_name: "UNKNOWN_NOT_LIVE_VERIFIED"
source_author_verification_state: "not_live_verified_in_this_environment"
observation_kind: "preview_usefulness"
observation_text: "ordinary sample signal 1: metadata-only preview can be observed, but semantic richness remains unverified until enrichment or human review."
observation_value: "needs_edit"
observation_unit: "review_label"
observed_at: "2026-05-07T00:00:00+08:00"
evidence_refs:
  - "pf-c1-url-ordinary"
  - "topic-card-lite-preview"
  - "human-verdict-needs-edit"
dedupe_key: "bilibili:BV16ooQBsEah:signal:1"
duplicate_policy: "merge_same_capture_same_observation_kind"
lifecycle_state: "observed"
claim_label_map:
  canonical_fields:
    - "id"
    - "source_capture_id"
    - "canonical_url"
  candidate_fields:
    - "observation_kind"
    - "observation_text"
  tentative_fields:
    - "source_author_display_name"
    - "observation_value"
broken_reference_state: "ok_if_capture_exists_else_broken_reference"
anti_second_inbox_check: "does_not_copy_capture_state; stores only derived observation"
notes: "Candidate fixture only; not an artifact_assets row and not a RAW note."
```
[candidate] Audit note 01: this sample intentionally uses explicit unknown/blocked states where live platform evidence is missing, preserving truthfulness while still making validators deterministic.
### Sample 02 — Signal

[candidate] Sample 02 exercises Signal relations using `BV1zhoUB1Ebg`. URL shape is carried as a platform URL, but author and rich metadata remain not-live-verified.
```yaml
id: "sig_01HR7S6A7F3Z9N2X4M8Q1V0A02"
entity_kind: "Signal"
schema_version: "signal.v0.candidate"
source_capture_id: "cap_u3_02_1Ebg"
platform: "bilibili"
platform_item_id: "BV1zhoUB1Ebg"
canonical_url: "https://www.bilibili.com/video/BV1zhoUB1Ebg/"
canonical_url_verification_state: "carried_from_existing_evidence_not_live_checked"
source_author_display_name: "UNKNOWN_NOT_LIVE_VERIFIED"
source_author_verification_state: "not_live_verified_in_this_environment"
observation_kind: "false_positive_risk"
observation_text: "edge sample signal 2: metadata-only preview can be observed, but semantic richness remains unverified until enrichment or human review."
observation_value: "counter_evidence_visible"
observation_unit: "review_label"
observed_at: "2026-05-07T00:00:00+08:00"
evidence_refs:
  - "pf-c1-url-edge"
  - "topic-card-lite-preview"
  - "human-verdict-needs-edit"
dedupe_key: "bilibili:BV1zhoUB1Ebg:signal:2"
duplicate_policy: "merge_same_capture_same_observation_kind"
lifecycle_state: "validated"
claim_label_map:
  canonical_fields:
    - "id"
    - "source_capture_id"
    - "canonical_url"
  candidate_fields:
    - "observation_kind"
    - "observation_text"
  tentative_fields:
    - "source_author_display_name"
    - "observation_value"
broken_reference_state: "ok_if_capture_exists_else_broken_reference"
anti_second_inbox_check: "does_not_copy_capture_state; stores only derived observation"
notes: "Candidate fixture only; not an artifact_assets row and not a RAW note."
```
[candidate] Audit note 02: this sample intentionally uses explicit unknown/blocked states where live platform evidence is missing, preserving truthfulness while still making validators deterministic.
### Sample 03 — Signal

[candidate] Sample 03 exercises Signal relations using `BV1A196BpESQ`. URL shape is carried as a platform URL, but author and rich metadata remain not-live-verified.
```yaml
id: "sig_01HR7S6A7F3Z9N2X4M8Q1V0A03"
entity_kind: "Signal"
schema_version: "signal.v0.candidate"
source_capture_id: "cap_u3_03_pESQ"
platform: "bilibili"
platform_item_id: "BV1A196BpESQ"
canonical_url: "https://www.bilibili.com/video/BV1A196BpESQ/"
canonical_url_verification_state: "carried_from_existing_evidence_not_live_checked"
source_author_display_name: "UNKNOWN_NOT_LIVE_VERIFIED"
source_author_verification_state: "not_live_verified_in_this_environment"
observation_kind: "cross_platform_reference"
observation_text: "high_signal sample signal 3: metadata-only preview can be observed, but semantic richness remains unverified until enrichment or human review."
observation_value: "scope_required"
observation_unit: "review_label"
observed_at: "2026-05-07T00:00:00+08:00"
evidence_refs:
  - "pf-c1-url-high_signal"
  - "topic-card-lite-preview"
  - "human-verdict-needs-edit"
dedupe_key: "bilibili:BV1A196BpESQ:signal:3"
duplicate_policy: "merge_same_capture_same_observation_kind"
lifecycle_state: "conflicted"
claim_label_map:
  canonical_fields:
    - "id"
    - "source_capture_id"
    - "canonical_url"
  candidate_fields:
    - "observation_kind"
    - "observation_text"
  tentative_fields:
    - "source_author_display_name"
    - "observation_value"
broken_reference_state: "ok_if_capture_exists_else_broken_reference"
anti_second_inbox_check: "does_not_copy_capture_state; stores only derived observation"
notes: "Candidate fixture only; not an artifact_assets row and not a RAW note."
```
[candidate] Audit note 03: this sample intentionally uses explicit unknown/blocked states where live platform evidence is missing, preserving truthfulness while still making validators deterministic.
### Sample 04 — Signal

[candidate] Sample 04 exercises Signal relations using `BV16ooQBsEah`. URL shape is carried as a platform URL, but author and rich metadata remain not-live-verified.
```yaml
id: "sig_01HR7S6A7F3Z9N2X4M8Q1V0A04"
entity_kind: "Signal"
schema_version: "signal.v0.candidate"
source_capture_id: "cap_u3_04_sEah"
platform: "bilibili"
platform_item_id: "BV16ooQBsEah"
canonical_url: "https://www.bilibili.com/video/BV16ooQBsEah/"
canonical_url_verification_state: "carried_from_existing_evidence_not_live_checked"
source_author_display_name: "UNKNOWN_NOT_LIVE_VERIFIED"
source_author_verification_state: "not_live_verified_in_this_environment"
observation_kind: "ai_generated_boundary"
observation_text: "ordinary sample signal 4: metadata-only preview can be observed, but semantic richness remains unverified until enrichment or human review."
observation_value: "not_human_validated"
observation_unit: "review_label"
observed_at: "2026-05-07T00:00:00+08:00"
evidence_refs:
  - "pf-c1-url-ordinary"
  - "topic-card-lite-preview"
  - "human-verdict-needs-edit"
dedupe_key: "bilibili:BV16ooQBsEah:signal:4"
duplicate_policy: "merge_same_capture_same_observation_kind"
lifecycle_state: "archived"
claim_label_map:
  canonical_fields:
    - "id"
    - "source_capture_id"
    - "canonical_url"
  candidate_fields:
    - "observation_kind"
    - "observation_text"
  tentative_fields:
    - "source_author_display_name"
    - "observation_value"
broken_reference_state: "ok_if_capture_exists_else_broken_reference"
anti_second_inbox_check: "does_not_copy_capture_state; stores only derived observation"
notes: "Candidate fixture only; not an artifact_assets row and not a RAW note."
```
[candidate] Audit note 04: this sample intentionally uses explicit unknown/blocked states where live platform evidence is missing, preserving truthfulness while still making validators deterministic.
### Sample 05 — Signal

[candidate] Sample 05 exercises Signal relations using `BV1zhoUB1Ebg`. URL shape is carried as a platform URL, but author and rich metadata remain not-live-verified.
```yaml
id: "sig_01HR7S6A7F3Z9N2X4M8Q1V0A05"
entity_kind: "Signal"
schema_version: "signal.v0.candidate"
source_capture_id: "cap_u3_05_1Ebg"
platform: "bilibili"
platform_item_id: "BV1zhoUB1Ebg"
canonical_url: "https://www.bilibili.com/video/BV1zhoUB1Ebg/"
canonical_url_verification_state: "carried_from_existing_evidence_not_live_checked"
source_author_display_name: "UNKNOWN_NOT_LIVE_VERIFIED"
source_author_verification_state: "not_live_verified_in_this_environment"
observation_kind: "metadata_presence"
observation_text: "edge sample signal 5: metadata-only preview can be observed, but semantic richness remains unverified until enrichment or human review."
observation_value: "present"
observation_unit: "review_label"
observed_at: "2026-05-07T00:00:00+08:00"
evidence_refs:
  - "pf-c1-url-edge"
  - "topic-card-lite-preview"
  - "human-verdict-needs-edit"
dedupe_key: "bilibili:BV1zhoUB1Ebg:signal:0"
duplicate_policy: "merge_same_capture_same_observation_kind"
lifecycle_state: "draft"
claim_label_map:
  canonical_fields:
    - "id"
    - "source_capture_id"
    - "canonical_url"
  candidate_fields:
    - "observation_kind"
    - "observation_text"
  tentative_fields:
    - "source_author_display_name"
    - "observation_value"
broken_reference_state: "ok_if_capture_exists_else_broken_reference"
anti_second_inbox_check: "does_not_copy_capture_state; stores only derived observation"
notes: "Candidate fixture only; not an artifact_assets row and not a RAW note."
```
[candidate] Audit note 05: this sample intentionally uses explicit unknown/blocked states where live platform evidence is missing, preserving truthfulness while still making validators deterministic.
### Sample 06 — Signal

[candidate] Sample 06 exercises Signal relations using `BV1A196BpESQ`. URL shape is carried as a platform URL, but author and rich metadata remain not-live-verified.
```yaml
id: "sig_01HR7S6A7F3Z9N2X4M8Q1V0A06"
entity_kind: "Signal"
schema_version: "signal.v0.candidate"
source_capture_id: "cap_u3_06_pESQ"
platform: "bilibili"
platform_item_id: "BV1A196BpESQ"
canonical_url: "https://www.bilibili.com/video/BV1A196BpESQ/"
canonical_url_verification_state: "carried_from_existing_evidence_not_live_checked"
source_author_display_name: "UNKNOWN_NOT_LIVE_VERIFIED"
source_author_verification_state: "not_live_verified_in_this_environment"
observation_kind: "preview_usefulness"
observation_text: "high_signal sample signal 6: metadata-only preview can be observed, but semantic richness remains unverified until enrichment or human review."
observation_value: "needs_edit"
observation_unit: "review_label"
observed_at: "2026-05-07T00:00:00+08:00"
evidence_refs:
  - "pf-c1-url-high_signal"
  - "topic-card-lite-preview"
  - "human-verdict-needs-edit"
dedupe_key: "bilibili:BV1A196BpESQ:signal:1"
duplicate_policy: "merge_same_capture_same_observation_kind"
lifecycle_state: "observed"
claim_label_map:
  canonical_fields:
    - "id"
    - "source_capture_id"
    - "canonical_url"
  candidate_fields:
    - "observation_kind"
    - "observation_text"
  tentative_fields:
    - "source_author_display_name"
    - "observation_value"
broken_reference_state: "ok_if_capture_exists_else_broken_reference"
anti_second_inbox_check: "does_not_copy_capture_state; stores only derived observation"
notes: "Candidate fixture only; not an artifact_assets row and not a RAW note."
```
[candidate] Audit note 06: this sample intentionally uses explicit unknown/blocked states where live platform evidence is missing, preserving truthfulness while still making validators deterministic.
### Sample 07 — Signal

[candidate] Sample 07 exercises Signal relations using `BV16ooQBsEah`. URL shape is carried as a platform URL, but author and rich metadata remain not-live-verified.
```yaml
id: "sig_01HR7S6A7F3Z9N2X4M8Q1V0A07"
entity_kind: "Signal"
schema_version: "signal.v0.candidate"
source_capture_id: "cap_u3_07_sEah"
platform: "bilibili"
platform_item_id: "BV16ooQBsEah"
canonical_url: "https://www.bilibili.com/video/BV16ooQBsEah/"
canonical_url_verification_state: "carried_from_existing_evidence_not_live_checked"
source_author_display_name: "UNKNOWN_NOT_LIVE_VERIFIED"
source_author_verification_state: "not_live_verified_in_this_environment"
observation_kind: "false_positive_risk"
observation_text: "ordinary sample signal 7: metadata-only preview can be observed, but semantic richness remains unverified until enrichment or human review."
observation_value: "counter_evidence_visible"
observation_unit: "review_label"
observed_at: "2026-05-07T00:00:00+08:00"
evidence_refs:
  - "pf-c1-url-ordinary"
  - "topic-card-lite-preview"
  - "human-verdict-needs-edit"
dedupe_key: "bilibili:BV16ooQBsEah:signal:2"
duplicate_policy: "merge_same_capture_same_observation_kind"
lifecycle_state: "validated"
claim_label_map:
  canonical_fields:
    - "id"
    - "source_capture_id"
    - "canonical_url"
  candidate_fields:
    - "observation_kind"
    - "observation_text"
  tentative_fields:
    - "source_author_display_name"
    - "observation_value"
broken_reference_state: "ok_if_capture_exists_else_broken_reference"
anti_second_inbox_check: "does_not_copy_capture_state; stores only derived observation"
notes: "Candidate fixture only; not an artifact_assets row and not a RAW note."
```
[candidate] Audit note 07: this sample intentionally uses explicit unknown/blocked states where live platform evidence is missing, preserving truthfulness while still making validators deterministic.
### Sample 08 — Signal

[candidate] Sample 08 exercises Signal relations using `BV1zhoUB1Ebg`. URL shape is carried as a platform URL, but author and rich metadata remain not-live-verified.
```yaml
id: "sig_01HR7S6A7F3Z9N2X4M8Q1V0A08"
entity_kind: "Signal"
schema_version: "signal.v0.candidate"
source_capture_id: "cap_u3_08_1Ebg"
platform: "bilibili"
platform_item_id: "BV1zhoUB1Ebg"
canonical_url: "https://www.bilibili.com/video/BV1zhoUB1Ebg/"
canonical_url_verification_state: "carried_from_existing_evidence_not_live_checked"
source_author_display_name: "UNKNOWN_NOT_LIVE_VERIFIED"
source_author_verification_state: "not_live_verified_in_this_environment"
observation_kind: "cross_platform_reference"
observation_text: "edge sample signal 8: metadata-only preview can be observed, but semantic richness remains unverified until enrichment or human review."
observation_value: "scope_required"
observation_unit: "review_label"
observed_at: "2026-05-07T00:00:00+08:00"
evidence_refs:
  - "pf-c1-url-edge"
  - "topic-card-lite-preview"
  - "human-verdict-needs-edit"
dedupe_key: "bilibili:BV1zhoUB1Ebg:signal:3"
duplicate_policy: "merge_same_capture_same_observation_kind"
lifecycle_state: "conflicted"
claim_label_map:
  canonical_fields:
    - "id"
    - "source_capture_id"
    - "canonical_url"
  candidate_fields:
    - "observation_kind"
    - "observation_text"
  tentative_fields:
    - "source_author_display_name"
    - "observation_value"
broken_reference_state: "ok_if_capture_exists_else_broken_reference"
anti_second_inbox_check: "does_not_copy_capture_state; stores only derived observation"
notes: "Candidate fixture only; not an artifact_assets row and not a RAW note."
```
[candidate] Audit note 08: this sample intentionally uses explicit unknown/blocked states where live platform evidence is missing, preserving truthfulness while still making validators deterministic.
### Sample 09 — Signal

[candidate] Sample 09 exercises Signal relations using `BV1A196BpESQ`. URL shape is carried as a platform URL, but author and rich metadata remain not-live-verified.
```yaml
id: "sig_01HR7S6A7F3Z9N2X4M8Q1V0A09"
entity_kind: "Signal"
schema_version: "signal.v0.candidate"
source_capture_id: "cap_u3_09_pESQ"
platform: "bilibili"
platform_item_id: "BV1A196BpESQ"
canonical_url: "https://www.bilibili.com/video/BV1A196BpESQ/"
canonical_url_verification_state: "carried_from_existing_evidence_not_live_checked"
source_author_display_name: "UNKNOWN_NOT_LIVE_VERIFIED"
source_author_verification_state: "not_live_verified_in_this_environment"
observation_kind: "ai_generated_boundary"
observation_text: "high_signal sample signal 9: metadata-only preview can be observed, but semantic richness remains unverified until enrichment or human review."
observation_value: "not_human_validated"
observation_unit: "review_label"
observed_at: "2026-05-07T00:00:00+08:00"
evidence_refs:
  - "pf-c1-url-high_signal"
  - "topic-card-lite-preview"
  - "human-verdict-needs-edit"
dedupe_key: "bilibili:BV1A196BpESQ:signal:4"
duplicate_policy: "merge_same_capture_same_observation_kind"
lifecycle_state: "archived"
claim_label_map:
  canonical_fields:
    - "id"
    - "source_capture_id"
    - "canonical_url"
  candidate_fields:
    - "observation_kind"
    - "observation_text"
  tentative_fields:
    - "source_author_display_name"
    - "observation_value"
broken_reference_state: "ok_if_capture_exists_else_broken_reference"
anti_second_inbox_check: "does_not_copy_capture_state; stores only derived observation"
notes: "Candidate fixture only; not an artifact_assets row and not a RAW note."
```
[candidate] Audit note 09: this sample intentionally uses explicit unknown/blocked states where live platform evidence is missing, preserving truthfulness while still making validators deterministic.
### Sample 10 — Signal

[candidate] Sample 10 exercises Signal relations using `BV16ooQBsEah`. URL shape is carried as a platform URL, but author and rich metadata remain not-live-verified.
```yaml
id: "sig_01HR7S6A7F3Z9N2X4M8Q1V0A10"
entity_kind: "Signal"
schema_version: "signal.v0.candidate"
source_capture_id: "cap_u3_10_sEah"
platform: "bilibili"
platform_item_id: "BV16ooQBsEah"
canonical_url: "https://www.bilibili.com/video/BV16ooQBsEah/"
canonical_url_verification_state: "carried_from_existing_evidence_not_live_checked"
source_author_display_name: "UNKNOWN_NOT_LIVE_VERIFIED"
source_author_verification_state: "not_live_verified_in_this_environment"
observation_kind: "metadata_presence"
observation_text: "ordinary sample signal 10: metadata-only preview can be observed, but semantic richness remains unverified until enrichment or human review."
observation_value: "present"
observation_unit: "review_label"
observed_at: "2026-05-07T00:00:00+08:00"
evidence_refs:
  - "pf-c1-url-ordinary"
  - "topic-card-lite-preview"
  - "human-verdict-needs-edit"
dedupe_key: "bilibili:BV16ooQBsEah:signal:0"
duplicate_policy: "merge_same_capture_same_observation_kind"
lifecycle_state: "draft"
claim_label_map:
  canonical_fields:
    - "id"
    - "source_capture_id"
    - "canonical_url"
  candidate_fields:
    - "observation_kind"
    - "observation_text"
  tentative_fields:
    - "source_author_display_name"
    - "observation_value"
broken_reference_state: "ok_if_capture_exists_else_broken_reference"
anti_second_inbox_check: "does_not_copy_capture_state; stores only derived observation"
notes: "Candidate fixture only; not an artifact_assets row and not a RAW note."
```
[candidate] Audit note 10: this sample intentionally uses explicit unknown/blocked states where live platform evidence is missing, preserving truthfulness while still making validators deterministic.

## §3 Fixture validation checklist

[candidate] Every sample has an id shaped as a stable candidate identifier.
[candidate] Every sample carries capture linkage or explains why it cannot become capture authority.
[candidate] Every sample preserves LP-001: no recommendation, keyword, RAW gap, playlist, account, or comment expansion is turned into direct capture.
[candidate] Every sample marks author metadata as not live verified.
[candidate] Every sample includes a lifecycle state and a claim_label_map.


## §4 Reviewer scenarios for second-pass audit

[candidate] Scenario 01: The reviewer should inspect the Signal sample as a fixture for observation primitive boundaries, duplicate grouping, source metadata uncertainty, and anti-second-inbox behavior. The pass condition is not that the sample looks semantically rich; the pass condition is that the sample can survive a skeptical audit without pretending that live metadata, author identity, runtime capture, RAW intake, or DiloFlow execution has been verified. When the sample uses `UNKNOWN_NOT_LIVE_VERIFIED`, that value is a successful honesty marker rather than an incomplete field.
[tentative] Scenario 01 failure mode: if a future agent replaces explicit unknowns with guessed author names, guessed follower counts, guessed title quality, or guessed platform state, the fixture should fail even if the rest of the JSON shape validates. This rule is especially important because sample data can quietly become seed data; the supplement blocks that drift by repeating not-authority frontmatter and candidate-only notes.
[candidate] Scenario 02: The reviewer should inspect the Signal sample as a fixture for observation primitive boundaries, duplicate grouping, source metadata uncertainty, and anti-second-inbox behavior. The pass condition is not that the sample looks semantically rich; the pass condition is that the sample can survive a skeptical audit without pretending that live metadata, author identity, runtime capture, RAW intake, or DiloFlow execution has been verified. When the sample uses `UNKNOWN_NOT_LIVE_VERIFIED`, that value is a successful honesty marker rather than an incomplete field.
[tentative] Scenario 02 failure mode: if a future agent replaces explicit unknowns with guessed author names, guessed follower counts, guessed title quality, or guessed platform state, the fixture should fail even if the rest of the JSON shape validates. This rule is especially important because sample data can quietly become seed data; the supplement blocks that drift by repeating not-authority frontmatter and candidate-only notes.
[candidate] Scenario 03: The reviewer should inspect the Signal sample as a fixture for observation primitive boundaries, duplicate grouping, source metadata uncertainty, and anti-second-inbox behavior. The pass condition is not that the sample looks semantically rich; the pass condition is that the sample can survive a skeptical audit without pretending that live metadata, author identity, runtime capture, RAW intake, or DiloFlow execution has been verified. When the sample uses `UNKNOWN_NOT_LIVE_VERIFIED`, that value is a successful honesty marker rather than an incomplete field.
[tentative] Scenario 03 failure mode: if a future agent replaces explicit unknowns with guessed author names, guessed follower counts, guessed title quality, or guessed platform state, the fixture should fail even if the rest of the JSON shape validates. This rule is especially important because sample data can quietly become seed data; the supplement blocks that drift by repeating not-authority frontmatter and candidate-only notes.
[candidate] Scenario 04: The reviewer should inspect the Signal sample as a fixture for observation primitive boundaries, duplicate grouping, source metadata uncertainty, and anti-second-inbox behavior. The pass condition is not that the sample looks semantically rich; the pass condition is that the sample can survive a skeptical audit without pretending that live metadata, author identity, runtime capture, RAW intake, or DiloFlow execution has been verified. When the sample uses `UNKNOWN_NOT_LIVE_VERIFIED`, that value is a successful honesty marker rather than an incomplete field.
[tentative] Scenario 04 failure mode: if a future agent replaces explicit unknowns with guessed author names, guessed follower counts, guessed title quality, or guessed platform state, the fixture should fail even if the rest of the JSON shape validates. This rule is especially important because sample data can quietly become seed data; the supplement blocks that drift by repeating not-authority frontmatter and candidate-only notes.
[candidate] Scenario 05: The reviewer should inspect the Signal sample as a fixture for observation primitive boundaries, duplicate grouping, source metadata uncertainty, and anti-second-inbox behavior. The pass condition is not that the sample looks semantically rich; the pass condition is that the sample can survive a skeptical audit without pretending that live metadata, author identity, runtime capture, RAW intake, or DiloFlow execution has been verified. When the sample uses `UNKNOWN_NOT_LIVE_VERIFIED`, that value is a successful honesty marker rather than an incomplete field.
[tentative] Scenario 05 failure mode: if a future agent replaces explicit unknowns with guessed author names, guessed follower counts, guessed title quality, or guessed platform state, the fixture should fail even if the rest of the JSON shape validates. This rule is especially important because sample data can quietly become seed data; the supplement blocks that drift by repeating not-authority frontmatter and candidate-only notes.
[candidate] Scenario 06: The reviewer should inspect the Signal sample as a fixture for observation primitive boundaries, duplicate grouping, source metadata uncertainty, and anti-second-inbox behavior. The pass condition is not that the sample looks semantically rich; the pass condition is that the sample can survive a skeptical audit without pretending that live metadata, author identity, runtime capture, RAW intake, or DiloFlow execution has been verified. When the sample uses `UNKNOWN_NOT_LIVE_VERIFIED`, that value is a successful honesty marker rather than an incomplete field.
[tentative] Scenario 06 failure mode: if a future agent replaces explicit unknowns with guessed author names, guessed follower counts, guessed title quality, or guessed platform state, the fixture should fail even if the rest of the JSON shape validates. This rule is especially important because sample data can quietly become seed data; the supplement blocks that drift by repeating not-authority frontmatter and candidate-only notes.
[candidate] Scenario 07: The reviewer should inspect the Signal sample as a fixture for observation primitive boundaries, duplicate grouping, source metadata uncertainty, and anti-second-inbox behavior. The pass condition is not that the sample looks semantically rich; the pass condition is that the sample can survive a skeptical audit without pretending that live metadata, author identity, runtime capture, RAW intake, or DiloFlow execution has been verified. When the sample uses `UNKNOWN_NOT_LIVE_VERIFIED`, that value is a successful honesty marker rather than an incomplete field.
[tentative] Scenario 07 failure mode: if a future agent replaces explicit unknowns with guessed author names, guessed follower counts, guessed title quality, or guessed platform state, the fixture should fail even if the rest of the JSON shape validates. This rule is especially important because sample data can quietly become seed data; the supplement blocks that drift by repeating not-authority frontmatter and candidate-only notes.
[candidate] Scenario 08: The reviewer should inspect the Signal sample as a fixture for observation primitive boundaries, duplicate grouping, source metadata uncertainty, and anti-second-inbox behavior. The pass condition is not that the sample looks semantically rich; the pass condition is that the sample can survive a skeptical audit without pretending that live metadata, author identity, runtime capture, RAW intake, or DiloFlow execution has been verified. When the sample uses `UNKNOWN_NOT_LIVE_VERIFIED`, that value is a successful honesty marker rather than an incomplete field.
[tentative] Scenario 08 failure mode: if a future agent replaces explicit unknowns with guessed author names, guessed follower counts, guessed title quality, or guessed platform state, the fixture should fail even if the rest of the JSON shape validates. This rule is especially important because sample data can quietly become seed data; the supplement blocks that drift by repeating not-authority frontmatter and candidate-only notes.
[candidate] Scenario 09: The reviewer should inspect the Signal sample as a fixture for observation primitive boundaries, duplicate grouping, source metadata uncertainty, and anti-second-inbox behavior. The pass condition is not that the sample looks semantically rich; the pass condition is that the sample can survive a skeptical audit without pretending that live metadata, author identity, runtime capture, RAW intake, or DiloFlow execution has been verified. When the sample uses `UNKNOWN_NOT_LIVE_VERIFIED`, that value is a successful honesty marker rather than an incomplete field.
[tentative] Scenario 09 failure mode: if a future agent replaces explicit unknowns with guessed author names, guessed follower counts, guessed title quality, or guessed platform state, the fixture should fail even if the rest of the JSON shape validates. This rule is especially important because sample data can quietly become seed data; the supplement blocks that drift by repeating not-authority frontmatter and candidate-only notes.
[candidate] Scenario 10: The reviewer should inspect the Signal sample as a fixture for observation primitive boundaries, duplicate grouping, source metadata uncertainty, and anti-second-inbox behavior. The pass condition is not that the sample looks semantically rich; the pass condition is that the sample can survive a skeptical audit without pretending that live metadata, author identity, runtime capture, RAW intake, or DiloFlow execution has been verified. When the sample uses `UNKNOWN_NOT_LIVE_VERIFIED`, that value is a successful honesty marker rather than an incomplete field.
[tentative] Scenario 10 failure mode: if a future agent replaces explicit unknowns with guessed author names, guessed follower counts, guessed title quality, or guessed platform state, the fixture should fail even if the rest of the JSON shape validates. This rule is especially important because sample data can quietly become seed data; the supplement blocks that drift by repeating not-authority frontmatter and candidate-only notes.
[candidate] Scenario 11: The reviewer should inspect the Signal sample as a fixture for observation primitive boundaries, duplicate grouping, source metadata uncertainty, and anti-second-inbox behavior. The pass condition is not that the sample looks semantically rich; the pass condition is that the sample can survive a skeptical audit without pretending that live metadata, author identity, runtime capture, RAW intake, or DiloFlow execution has been verified. When the sample uses `UNKNOWN_NOT_LIVE_VERIFIED`, that value is a successful honesty marker rather than an incomplete field.
[tentative] Scenario 11 failure mode: if a future agent replaces explicit unknowns with guessed author names, guessed follower counts, guessed title quality, or guessed platform state, the fixture should fail even if the rest of the JSON shape validates. This rule is especially important because sample data can quietly become seed data; the supplement blocks that drift by repeating not-authority frontmatter and candidate-only notes.
[candidate] Scenario 12: The reviewer should inspect the Signal sample as a fixture for observation primitive boundaries, duplicate grouping, source metadata uncertainty, and anti-second-inbox behavior. The pass condition is not that the sample looks semantically rich; the pass condition is that the sample can survive a skeptical audit without pretending that live metadata, author identity, runtime capture, RAW intake, or DiloFlow execution has been verified. When the sample uses `UNKNOWN_NOT_LIVE_VERIFIED`, that value is a successful honesty marker rather than an incomplete field.
[tentative] Scenario 12 failure mode: if a future agent replaces explicit unknowns with guessed author names, guessed follower counts, guessed title quality, or guessed platform state, the fixture should fail even if the rest of the JSON shape validates. This rule is especially important because sample data can quietly become seed data; the supplement blocks that drift by repeating not-authority frontmatter and candidate-only notes.

## §5 Field-level audit expansion

[candidate] Field `id` must be read as a fixture contract field. The reviewer should ask three questions: is the field populated, is its claim label clear, and does the value avoid smuggling runtime or authority approval? For Signal, a populated field can still be an explicit `not-approved`, `not_live_verified_in_this_environment`, `blocked_runtime`, or `candidate_only` value; those values are preferable to attractive but unverifiable details.
[candidate] Field `schema_version` must be read as a fixture contract field. The reviewer should ask three questions: is the field populated, is its claim label clear, and does the value avoid smuggling runtime or authority approval? For Signal, a populated field can still be an explicit `not-approved`, `not_live_verified_in_this_environment`, `blocked_runtime`, or `candidate_only` value; those values are preferable to attractive but unverifiable details.
[candidate] Field `source_capture_id` must be read as a fixture contract field. The reviewer should ask three questions: is the field populated, is its claim label clear, and does the value avoid smuggling runtime or authority approval? For Signal, a populated field can still be an explicit `not-approved`, `not_live_verified_in_this_environment`, `blocked_runtime`, or `candidate_only` value; those values are preferable to attractive but unverifiable details.
[candidate] Field `canonical_url` must be read as a fixture contract field. The reviewer should ask three questions: is the field populated, is its claim label clear, and does the value avoid smuggling runtime or authority approval? For Signal, a populated field can still be an explicit `not-approved`, `not_live_verified_in_this_environment`, `blocked_runtime`, or `candidate_only` value; those values are preferable to attractive but unverifiable details.
[candidate] Field `platform_item_id` must be read as a fixture contract field. The reviewer should ask three questions: is the field populated, is its claim label clear, and does the value avoid smuggling runtime or authority approval? For Signal, a populated field can still be an explicit `not-approved`, `not_live_verified_in_this_environment`, `blocked_runtime`, or `candidate_only` value; those values are preferable to attractive but unverifiable details.
[candidate] Field `lifecycle_state` must be read as a fixture contract field. The reviewer should ask three questions: is the field populated, is its claim label clear, and does the value avoid smuggling runtime or authority approval? For Signal, a populated field can still be an explicit `not-approved`, `not_live_verified_in_this_environment`, `blocked_runtime`, or `candidate_only` value; those values are preferable to attractive but unverifiable details.
[candidate] Field `claim_label_map` must be read as a fixture contract field. The reviewer should ask three questions: is the field populated, is its claim label clear, and does the value avoid smuggling runtime or authority approval? For Signal, a populated field can still be an explicit `not-approved`, `not_live_verified_in_this_environment`, `blocked_runtime`, or `candidate_only` value; those values are preferable to attractive but unverifiable details.
[candidate] Field `evidence_refs` must be read as a fixture contract field. The reviewer should ask three questions: is the field populated, is its claim label clear, and does the value avoid smuggling runtime or authority approval? For Signal, a populated field can still be an explicit `not-approved`, `not_live_verified_in_this_environment`, `blocked_runtime`, or `candidate_only` value; those values are preferable to attractive but unverifiable details.
[candidate] Field `verification_state` must be read as a fixture contract field. The reviewer should ask three questions: is the field populated, is its claim label clear, and does the value avoid smuggling runtime or authority approval? For Signal, a populated field can still be an explicit `not-approved`, `not_live_verified_in_this_environment`, `blocked_runtime`, or `candidate_only` value; those values are preferable to attractive but unverifiable details.
[candidate] Field `notes` must be read as a fixture contract field. The reviewer should ask three questions: is the field populated, is its claim label clear, and does the value avoid smuggling runtime or authority approval? For Signal, a populated field can still be an explicit `not-approved`, `not_live_verified_in_this_environment`, `blocked_runtime`, or `candidate_only` value; those values are preferable to attractive but unverifiable details.

## §6 Downstream fixture-use guidance

[candidate] U1 SRD-v3 outline drafting: use Signal samples as bounded design input only. A consumer may copy the field names into a checklist, but should not copy the instances into an authority database. The safe reuse pattern is fixture → audit question → amendment text, not fixture → migration → runtime.
[candidate] U2 Lane-4/5 unlock discussion: use Signal samples as bounded design input only. A consumer may copy the field names into a checklist, but should not copy the instances into an authority database. The safe reuse pattern is fixture → audit question → amendment text, not fixture → migration → runtime.
[candidate] PF-C1 topic-card preview regression review: use Signal samples as bounded design input only. A consumer may copy the field names into a checklist, but should not copy the instances into an authority database. The safe reuse pattern is fixture → audit question → amendment text, not fixture → migration → runtime.
[candidate] PF-C2 RAW handoff negative testing: use Signal samples as bounded design input only. A consumer may copy the field names into a checklist, but should not copy the instances into an authority database. The safe reuse pattern is fixture → audit question → amendment text, not fixture → migration → runtime.
[candidate] future C4 dispatch UI projection sketch: use Signal samples as bounded design input only. A consumer may copy the field names into a checklist, but should not copy the instances into an authority database. The safe reuse pattern is fixture → audit question → amendment text, not fixture → migration → runtime.
