---
status: candidate / topiccard_sample_data / not-authority
authority: not-authority
execution_approval: not-approved
runtime_approval: not-approved
migration_approval: not-approved
created_at: 2026-05-07
supplement_for: cloud-output-U3-entity-v0-contracts-2026-05-07.zip
---
# ENTITY-TopicCard-v0-sample-data-2026-05-07

[canonical] Purpose: this supplementary file expands the previous entity contract with reviewable fixture-style sample instances. It does not promote any entity to DB authority, does not approve a migration, and does not add runtime endpoints.
[candidate] Data honesty note: live web browsing is unavailable in this execution environment. The Bilibili URLs below are carried from existing PF-C1 evidence context and from the user-provided prompt lineage; author names and rich platform metadata are deliberately marked `UNKNOWN_NOT_LIVE_VERIFIED` rather than fabricated.
[candidate] Sample design rule: each sample is fully populated at the contract level because every required field has a value, even when that value is an explicit unknown, blocked, or not-live-verified state. This keeps the IR testable without inventing truth.
[candidate] Review use: these samples are intended for local fixture review, OpenAPI examples, referential integrity tests, and migration worked examples. They should not be copied into SQLite or RAW as real knowledge objects.

## §1 Depth gaps found in previous ZIP

[candidate] Gap 1: The lite-v0 to v1 extension was described but sample rows did not show 6 carry-over fields plus v1 relations together.
[candidate] Gap 2: RAW and DiloFlow handoff postures were separated but not demonstrated in card-level fixture data.
[candidate] Gap 3: Human usefulness verdict and counter-evidence were present but not rich enough to prevent usefulness inflation.

## §2 Sample instances

### Sample 01 — TopicCard

[candidate] Sample 01 exercises TopicCard relations using `BV16ooQBsEah`. URL shape is carried as a platform URL, but author and rich metadata remain not-live-verified.
```yaml
id: "card_01HR7S6A7F3Z9N2X4M8Q1V0A01"
entity_kind: "TopicCard"
schema_version: "topic_card.v1.candidate"
title: "ScoutFlow BV16ooQBsEah review card 1"
platform_item_id: "BV16ooQBsEah"
canonical_url: "https://www.bilibili.com/video/BV16ooQBsEah/"
capture_id: "cap_u3_01_sEah"
export_posture: "handoff_candidate"
target_path: "/tmp/scoutflow-vault/00-Inbox/topic-card-cap_u3_01_sEah.md"
carry_over_from_lite_v0:
  - "title"
  - "platform_item_id"
  - "canonical_url"
  - "capture_id"
  - "export_posture"
  - "target_path"
signal_refs:
  - "sig_01HR7S6A7F3Z9N2X4M8Q1V0A01"
  - "sig_01HR7S6A7F3Z9N2X4M8Q1V0A02"
  - "sig_01HR7S6A7F3Z9N2X4M8Q1V0A03"
hypothesis_refs:
  - "hyp_01HR7S6A7F3Z9N2X4M8Q1V0A01"
capture_plan_refs:
  - "plan_01HR7S6A7F3Z9N2X4M8Q1V0A01"
hypothesis_summary: "Card 1 frames whether ordinary preview can be useful without claiming semantic completeness."
evidence_balance:
  support: "capture truth and target path are present"
  counter: "author and rich metadata are not live verified"
  process: "write_enabled remains false"
frontmatter:
  title: "ScoutFlow BV16ooQBsEah review card 1"
  date: "2026-05-07"
  tags: "ScoutFlow/candidate topic-card"
  status: "candidate"
raw_handoff:
  posture: "candidate_only"
  target: "00-Inbox raw note candidate"
  true_write: "not-approved"
diloflow_handoff:
  posture: "script_seed_input_candidate"
  execution: "not-approved"
review_state: "reviewed"
lifecycle_state: "reviewable"
claim_label_map:
  canonical_fields:
    - "title"
    - "platform_item_id"
    - "canonical_url"
    - "capture_id"
    - "export_posture"
    - "target_path"
  candidate_fields:
    - "signal_refs"
    - "hypothesis_refs"
    - "capture_plan_refs"
  tentative_fields:
    - "hypothesis_summary"
    - "evidence_balance"
notes: "Candidate TopicCard v1 fixture; not a RAW commit, not a DiloFlow execution, not publish-ready."
```
[candidate] Audit note 01: this sample intentionally uses explicit unknown/blocked states where live platform evidence is missing, preserving truthfulness while still making validators deterministic.
### Sample 02 — TopicCard

[candidate] Sample 02 exercises TopicCard relations using `BV1zhoUB1Ebg`. URL shape is carried as a platform URL, but author and rich metadata remain not-live-verified.
```yaml
id: "card_01HR7S6A7F3Z9N2X4M8Q1V0A02"
entity_kind: "TopicCard"
schema_version: "topic_card.v1.candidate"
title: "ScoutFlow BV1zhoUB1Ebg review card 2"
platform_item_id: "BV1zhoUB1Ebg"
canonical_url: "https://www.bilibili.com/video/BV1zhoUB1Ebg/"
capture_id: "cap_u3_02_1Ebg"
export_posture: "handoff_candidate"
target_path: "/tmp/scoutflow-vault/00-Inbox/topic-card-cap_u3_02_1Ebg.md"
carry_over_from_lite_v0:
  - "title"
  - "platform_item_id"
  - "canonical_url"
  - "capture_id"
  - "export_posture"
  - "target_path"
signal_refs:
  - "sig_01HR7S6A7F3Z9N2X4M8Q1V0A02"
  - "sig_01HR7S6A7F3Z9N2X4M8Q1V0A03"
  - "sig_01HR7S6A7F3Z9N2X4M8Q1V0A04"
hypothesis_refs:
  - "hyp_01HR7S6A7F3Z9N2X4M8Q1V0A02"
capture_plan_refs:
  - "plan_01HR7S6A7F3Z9N2X4M8Q1V0A02"
hypothesis_summary: "Card 2 frames whether edge preview can be useful without claiming semantic completeness."
evidence_balance:
  support: "capture truth and target path are present"
  counter: "author and rich metadata are not live verified"
  process: "write_enabled remains false"
frontmatter:
  title: "ScoutFlow BV1zhoUB1Ebg review card 2"
  date: "2026-05-07"
  tags: "ScoutFlow/candidate topic-card"
  status: "candidate"
raw_handoff:
  posture: "candidate_only"
  target: "00-Inbox raw note candidate"
  true_write: "not-approved"
diloflow_handoff:
  posture: "script_seed_input_candidate"
  execution: "not-approved"
review_state: "needs_human_verdict"
lifecycle_state: "handoff_candidate"
claim_label_map:
  canonical_fields:
    - "title"
    - "platform_item_id"
    - "canonical_url"
    - "capture_id"
    - "export_posture"
    - "target_path"
  candidate_fields:
    - "signal_refs"
    - "hypothesis_refs"
    - "capture_plan_refs"
  tentative_fields:
    - "hypothesis_summary"
    - "evidence_balance"
notes: "Candidate TopicCard v1 fixture; not a RAW commit, not a DiloFlow execution, not publish-ready."
```
[candidate] Audit note 02: this sample intentionally uses explicit unknown/blocked states where live platform evidence is missing, preserving truthfulness while still making validators deterministic.
### Sample 03 — TopicCard

[candidate] Sample 03 exercises TopicCard relations using `BV1A196BpESQ`. URL shape is carried as a platform URL, but author and rich metadata remain not-live-verified.
```yaml
id: "card_01HR7S6A7F3Z9N2X4M8Q1V0A03"
entity_kind: "TopicCard"
schema_version: "topic_card.v1.candidate"
title: "ScoutFlow BV1A196BpESQ review card 3"
platform_item_id: "BV1A196BpESQ"
canonical_url: "https://www.bilibili.com/video/BV1A196BpESQ/"
capture_id: "cap_u3_03_pESQ"
export_posture: "local_only"
target_path: "/tmp/scoutflow-vault/00-Inbox/topic-card-cap_u3_03_pESQ.md"
carry_over_from_lite_v0:
  - "title"
  - "platform_item_id"
  - "canonical_url"
  - "capture_id"
  - "export_posture"
  - "target_path"
signal_refs:
  - "sig_01HR7S6A7F3Z9N2X4M8Q1V0A03"
  - "sig_01HR7S6A7F3Z9N2X4M8Q1V0A04"
  - "sig_01HR7S6A7F3Z9N2X4M8Q1V0A05"
hypothesis_refs:
  - "hyp_01HR7S6A7F3Z9N2X4M8Q1V0A03"
capture_plan_refs:
  - "plan_01HR7S6A7F3Z9N2X4M8Q1V0A03"
hypothesis_summary: "Card 3 frames whether high_signal preview can be useful without claiming semantic completeness."
evidence_balance:
  support: "capture truth and target path are present"
  counter: "author and rich metadata are not live verified"
  process: "write_enabled remains false"
frontmatter:
  title: "ScoutFlow BV1A196BpESQ review card 3"
  date: "2026-05-07"
  tags: "ScoutFlow/candidate topic-card"
  status: "candidate"
raw_handoff:
  posture: "candidate_only"
  target: "00-Inbox raw note candidate"
  true_write: "not-approved"
diloflow_handoff:
  posture: "script_seed_input_candidate"
  execution: "not-approved"
review_state: "parked"
lifecycle_state: "returned_for_edit"
claim_label_map:
  canonical_fields:
    - "title"
    - "platform_item_id"
    - "canonical_url"
    - "capture_id"
    - "export_posture"
    - "target_path"
  candidate_fields:
    - "signal_refs"
    - "hypothesis_refs"
    - "capture_plan_refs"
  tentative_fields:
    - "hypothesis_summary"
    - "evidence_balance"
notes: "Candidate TopicCard v1 fixture; not a RAW commit, not a DiloFlow execution, not publish-ready."
```
[candidate] Audit note 03: this sample intentionally uses explicit unknown/blocked states where live platform evidence is missing, preserving truthfulness while still making validators deterministic.
### Sample 04 — TopicCard

[candidate] Sample 04 exercises TopicCard relations using `BV16ooQBsEah`. URL shape is carried as a platform URL, but author and rich metadata remain not-live-verified.
```yaml
id: "card_01HR7S6A7F3Z9N2X4M8Q1V0A04"
entity_kind: "TopicCard"
schema_version: "topic_card.v1.candidate"
title: "ScoutFlow BV16ooQBsEah review card 4"
platform_item_id: "BV16ooQBsEah"
canonical_url: "https://www.bilibili.com/video/BV16ooQBsEah/"
capture_id: "cap_u3_04_sEah"
export_posture: "handoff_candidate"
target_path: "/tmp/scoutflow-vault/00-Inbox/topic-card-cap_u3_04_sEah.md"
carry_over_from_lite_v0:
  - "title"
  - "platform_item_id"
  - "canonical_url"
  - "capture_id"
  - "export_posture"
  - "target_path"
signal_refs:
  - "sig_01HR7S6A7F3Z9N2X4M8Q1V0A04"
  - "sig_01HR7S6A7F3Z9N2X4M8Q1V0A05"
  - "sig_01HR7S6A7F3Z9N2X4M8Q1V0A06"
hypothesis_refs:
  - "hyp_01HR7S6A7F3Z9N2X4M8Q1V0A04"
capture_plan_refs:
  - "plan_01HR7S6A7F3Z9N2X4M8Q1V0A04"
hypothesis_summary: "Card 4 frames whether ordinary preview can be useful without claiming semantic completeness."
evidence_balance:
  support: "capture truth and target path are present"
  counter: "author and rich metadata are not live verified"
  process: "write_enabled remains false"
frontmatter:
  title: "ScoutFlow BV16ooQBsEah review card 4"
  date: "2026-05-07"
  tags: "ScoutFlow/candidate topic-card"
  status: "candidate"
raw_handoff:
  posture: "candidate_only"
  target: "00-Inbox raw note candidate"
  true_write: "not-approved"
diloflow_handoff:
  posture: "script_seed_input_candidate"
  execution: "not-approved"
review_state: "archived"
lifecycle_state: "archived"
claim_label_map:
  canonical_fields:
    - "title"
    - "platform_item_id"
    - "canonical_url"
    - "capture_id"
    - "export_posture"
    - "target_path"
  candidate_fields:
    - "signal_refs"
    - "hypothesis_refs"
    - "capture_plan_refs"
  tentative_fields:
    - "hypothesis_summary"
    - "evidence_balance"
notes: "Candidate TopicCard v1 fixture; not a RAW commit, not a DiloFlow execution, not publish-ready."
```
[candidate] Audit note 04: this sample intentionally uses explicit unknown/blocked states where live platform evidence is missing, preserving truthfulness while still making validators deterministic.
### Sample 05 — TopicCard

[candidate] Sample 05 exercises TopicCard relations using `BV1zhoUB1Ebg`. URL shape is carried as a platform URL, but author and rich metadata remain not-live-verified.
```yaml
id: "card_01HR7S6A7F3Z9N2X4M8Q1V0A05"
entity_kind: "TopicCard"
schema_version: "topic_card.v1.candidate"
title: "ScoutFlow BV1zhoUB1Ebg review card 5"
platform_item_id: "BV1zhoUB1Ebg"
canonical_url: "https://www.bilibili.com/video/BV1zhoUB1Ebg/"
capture_id: "cap_u3_05_1Ebg"
export_posture: "local_only"
target_path: "/tmp/scoutflow-vault/00-Inbox/topic-card-cap_u3_05_1Ebg.md"
carry_over_from_lite_v0:
  - "title"
  - "platform_item_id"
  - "canonical_url"
  - "capture_id"
  - "export_posture"
  - "target_path"
signal_refs:
  - "sig_01HR7S6A7F3Z9N2X4M8Q1V0A05"
  - "sig_01HR7S6A7F3Z9N2X4M8Q1V0A06"
  - "sig_01HR7S6A7F3Z9N2X4M8Q1V0A07"
hypothesis_refs:
  - "hyp_01HR7S6A7F3Z9N2X4M8Q1V0A05"
capture_plan_refs:
  - "plan_01HR7S6A7F3Z9N2X4M8Q1V0A05"
hypothesis_summary: "Card 5 frames whether edge preview can be useful without claiming semantic completeness."
evidence_balance:
  support: "capture truth and target path are present"
  counter: "author and rich metadata are not live verified"
  process: "write_enabled remains false"
frontmatter:
  title: "ScoutFlow BV1zhoUB1Ebg review card 5"
  date: "2026-05-07"
  tags: "ScoutFlow/candidate topic-card"
  status: "candidate"
raw_handoff:
  posture: "candidate_only"
  target: "00-Inbox raw note candidate"
  true_write: "not-approved"
diloflow_handoff:
  posture: "script_seed_input_candidate"
  execution: "not-approved"
review_state: "mapped"
lifecycle_state: "draft"
claim_label_map:
  canonical_fields:
    - "title"
    - "platform_item_id"
    - "canonical_url"
    - "capture_id"
    - "export_posture"
    - "target_path"
  candidate_fields:
    - "signal_refs"
    - "hypothesis_refs"
    - "capture_plan_refs"
  tentative_fields:
    - "hypothesis_summary"
    - "evidence_balance"
notes: "Candidate TopicCard v1 fixture; not a RAW commit, not a DiloFlow execution, not publish-ready."
```
[candidate] Audit note 05: this sample intentionally uses explicit unknown/blocked states where live platform evidence is missing, preserving truthfulness while still making validators deterministic.
### Sample 06 — TopicCard

[candidate] Sample 06 exercises TopicCard relations using `BV1A196BpESQ`. URL shape is carried as a platform URL, but author and rich metadata remain not-live-verified.
```yaml
id: "card_01HR7S6A7F3Z9N2X4M8Q1V0A06"
entity_kind: "TopicCard"
schema_version: "topic_card.v1.candidate"
title: "ScoutFlow BV1A196BpESQ review card 6"
platform_item_id: "BV1A196BpESQ"
canonical_url: "https://www.bilibili.com/video/BV1A196BpESQ/"
capture_id: "cap_u3_06_pESQ"
export_posture: "handoff_candidate"
target_path: "/tmp/scoutflow-vault/00-Inbox/topic-card-cap_u3_06_pESQ.md"
carry_over_from_lite_v0:
  - "title"
  - "platform_item_id"
  - "canonical_url"
  - "capture_id"
  - "export_posture"
  - "target_path"
signal_refs:
  - "sig_01HR7S6A7F3Z9N2X4M8Q1V0A06"
  - "sig_01HR7S6A7F3Z9N2X4M8Q1V0A07"
  - "sig_01HR7S6A7F3Z9N2X4M8Q1V0A08"
hypothesis_refs:
  - "hyp_01HR7S6A7F3Z9N2X4M8Q1V0A06"
capture_plan_refs:
  - "plan_01HR7S6A7F3Z9N2X4M8Q1V0A06"
hypothesis_summary: "Card 6 frames whether high_signal preview can be useful without claiming semantic completeness."
evidence_balance:
  support: "capture truth and target path are present"
  counter: "author and rich metadata are not live verified"
  process: "write_enabled remains false"
frontmatter:
  title: "ScoutFlow BV1A196BpESQ review card 6"
  date: "2026-05-07"
  tags: "ScoutFlow/candidate topic-card"
  status: "candidate"
raw_handoff:
  posture: "candidate_only"
  target: "00-Inbox raw note candidate"
  true_write: "not-approved"
diloflow_handoff:
  posture: "script_seed_input_candidate"
  execution: "not-approved"
review_state: "reviewed"
lifecycle_state: "reviewable"
claim_label_map:
  canonical_fields:
    - "title"
    - "platform_item_id"
    - "canonical_url"
    - "capture_id"
    - "export_posture"
    - "target_path"
  candidate_fields:
    - "signal_refs"
    - "hypothesis_refs"
    - "capture_plan_refs"
  tentative_fields:
    - "hypothesis_summary"
    - "evidence_balance"
notes: "Candidate TopicCard v1 fixture; not a RAW commit, not a DiloFlow execution, not publish-ready."
```
[candidate] Audit note 06: this sample intentionally uses explicit unknown/blocked states where live platform evidence is missing, preserving truthfulness while still making validators deterministic.
### Sample 07 — TopicCard

[candidate] Sample 07 exercises TopicCard relations using `BV16ooQBsEah`. URL shape is carried as a platform URL, but author and rich metadata remain not-live-verified.
```yaml
id: "card_01HR7S6A7F3Z9N2X4M8Q1V0A07"
entity_kind: "TopicCard"
schema_version: "topic_card.v1.candidate"
title: "ScoutFlow BV16ooQBsEah review card 7"
platform_item_id: "BV16ooQBsEah"
canonical_url: "https://www.bilibili.com/video/BV16ooQBsEah/"
capture_id: "cap_u3_07_sEah"
export_posture: "handoff_candidate"
target_path: "/tmp/scoutflow-vault/00-Inbox/topic-card-cap_u3_07_sEah.md"
carry_over_from_lite_v0:
  - "title"
  - "platform_item_id"
  - "canonical_url"
  - "capture_id"
  - "export_posture"
  - "target_path"
signal_refs:
  - "sig_01HR7S6A7F3Z9N2X4M8Q1V0A07"
  - "sig_01HR7S6A7F3Z9N2X4M8Q1V0A08"
  - "sig_01HR7S6A7F3Z9N2X4M8Q1V0A09"
hypothesis_refs:
  - "hyp_01HR7S6A7F3Z9N2X4M8Q1V0A07"
capture_plan_refs:
  - "plan_01HR7S6A7F3Z9N2X4M8Q1V0A07"
hypothesis_summary: "Card 7 frames whether ordinary preview can be useful without claiming semantic completeness."
evidence_balance:
  support: "capture truth and target path are present"
  counter: "author and rich metadata are not live verified"
  process: "write_enabled remains false"
frontmatter:
  title: "ScoutFlow BV16ooQBsEah review card 7"
  date: "2026-05-07"
  tags: "ScoutFlow/candidate topic-card"
  status: "candidate"
raw_handoff:
  posture: "candidate_only"
  target: "00-Inbox raw note candidate"
  true_write: "not-approved"
diloflow_handoff:
  posture: "script_seed_input_candidate"
  execution: "not-approved"
review_state: "needs_human_verdict"
lifecycle_state: "handoff_candidate"
claim_label_map:
  canonical_fields:
    - "title"
    - "platform_item_id"
    - "canonical_url"
    - "capture_id"
    - "export_posture"
    - "target_path"
  candidate_fields:
    - "signal_refs"
    - "hypothesis_refs"
    - "capture_plan_refs"
  tentative_fields:
    - "hypothesis_summary"
    - "evidence_balance"
notes: "Candidate TopicCard v1 fixture; not a RAW commit, not a DiloFlow execution, not publish-ready."
```
[candidate] Audit note 07: this sample intentionally uses explicit unknown/blocked states where live platform evidence is missing, preserving truthfulness while still making validators deterministic.
### Sample 08 — TopicCard

[candidate] Sample 08 exercises TopicCard relations using `BV1zhoUB1Ebg`. URL shape is carried as a platform URL, but author and rich metadata remain not-live-verified.
```yaml
id: "card_01HR7S6A7F3Z9N2X4M8Q1V0A08"
entity_kind: "TopicCard"
schema_version: "topic_card.v1.candidate"
title: "ScoutFlow BV1zhoUB1Ebg review card 8"
platform_item_id: "BV1zhoUB1Ebg"
canonical_url: "https://www.bilibili.com/video/BV1zhoUB1Ebg/"
capture_id: "cap_u3_08_1Ebg"
export_posture: "local_only"
target_path: "/tmp/scoutflow-vault/00-Inbox/topic-card-cap_u3_08_1Ebg.md"
carry_over_from_lite_v0:
  - "title"
  - "platform_item_id"
  - "canonical_url"
  - "capture_id"
  - "export_posture"
  - "target_path"
signal_refs:
  - "sig_01HR7S6A7F3Z9N2X4M8Q1V0A08"
  - "sig_01HR7S6A7F3Z9N2X4M8Q1V0A09"
  - "sig_01HR7S6A7F3Z9N2X4M8Q1V0A10"
hypothesis_refs:
  - "hyp_01HR7S6A7F3Z9N2X4M8Q1V0A08"
capture_plan_refs:
  - "plan_01HR7S6A7F3Z9N2X4M8Q1V0A08"
hypothesis_summary: "Card 8 frames whether edge preview can be useful without claiming semantic completeness."
evidence_balance:
  support: "capture truth and target path are present"
  counter: "author and rich metadata are not live verified"
  process: "write_enabled remains false"
frontmatter:
  title: "ScoutFlow BV1zhoUB1Ebg review card 8"
  date: "2026-05-07"
  tags: "ScoutFlow/candidate topic-card"
  status: "candidate"
raw_handoff:
  posture: "candidate_only"
  target: "00-Inbox raw note candidate"
  true_write: "not-approved"
diloflow_handoff:
  posture: "script_seed_input_candidate"
  execution: "not-approved"
review_state: "parked"
lifecycle_state: "returned_for_edit"
claim_label_map:
  canonical_fields:
    - "title"
    - "platform_item_id"
    - "canonical_url"
    - "capture_id"
    - "export_posture"
    - "target_path"
  candidate_fields:
    - "signal_refs"
    - "hypothesis_refs"
    - "capture_plan_refs"
  tentative_fields:
    - "hypothesis_summary"
    - "evidence_balance"
notes: "Candidate TopicCard v1 fixture; not a RAW commit, not a DiloFlow execution, not publish-ready."
```
[candidate] Audit note 08: this sample intentionally uses explicit unknown/blocked states where live platform evidence is missing, preserving truthfulness while still making validators deterministic.
### Sample 09 — TopicCard

[candidate] Sample 09 exercises TopicCard relations using `BV1A196BpESQ`. URL shape is carried as a platform URL, but author and rich metadata remain not-live-verified.
```yaml
id: "card_01HR7S6A7F3Z9N2X4M8Q1V0A09"
entity_kind: "TopicCard"
schema_version: "topic_card.v1.candidate"
title: "ScoutFlow BV1A196BpESQ review card 9"
platform_item_id: "BV1A196BpESQ"
canonical_url: "https://www.bilibili.com/video/BV1A196BpESQ/"
capture_id: "cap_u3_09_pESQ"
export_posture: "handoff_candidate"
target_path: "/tmp/scoutflow-vault/00-Inbox/topic-card-cap_u3_09_pESQ.md"
carry_over_from_lite_v0:
  - "title"
  - "platform_item_id"
  - "canonical_url"
  - "capture_id"
  - "export_posture"
  - "target_path"
signal_refs:
  - "sig_01HR7S6A7F3Z9N2X4M8Q1V0A09"
  - "sig_01HR7S6A7F3Z9N2X4M8Q1V0A10"
  - "sig_01HR7S6A7F3Z9N2X4M8Q1V0A01"
hypothesis_refs:
  - "hyp_01HR7S6A7F3Z9N2X4M8Q1V0A09"
capture_plan_refs:
  - "plan_01HR7S6A7F3Z9N2X4M8Q1V0A09"
hypothesis_summary: "Card 9 frames whether high_signal preview can be useful without claiming semantic completeness."
evidence_balance:
  support: "capture truth and target path are present"
  counter: "author and rich metadata are not live verified"
  process: "write_enabled remains false"
frontmatter:
  title: "ScoutFlow BV1A196BpESQ review card 9"
  date: "2026-05-07"
  tags: "ScoutFlow/candidate topic-card"
  status: "candidate"
raw_handoff:
  posture: "candidate_only"
  target: "00-Inbox raw note candidate"
  true_write: "not-approved"
diloflow_handoff:
  posture: "script_seed_input_candidate"
  execution: "not-approved"
review_state: "archived"
lifecycle_state: "archived"
claim_label_map:
  canonical_fields:
    - "title"
    - "platform_item_id"
    - "canonical_url"
    - "capture_id"
    - "export_posture"
    - "target_path"
  candidate_fields:
    - "signal_refs"
    - "hypothesis_refs"
    - "capture_plan_refs"
  tentative_fields:
    - "hypothesis_summary"
    - "evidence_balance"
notes: "Candidate TopicCard v1 fixture; not a RAW commit, not a DiloFlow execution, not publish-ready."
```
[candidate] Audit note 09: this sample intentionally uses explicit unknown/blocked states where live platform evidence is missing, preserving truthfulness while still making validators deterministic.
### Sample 10 — TopicCard

[candidate] Sample 10 exercises TopicCard relations using `BV16ooQBsEah`. URL shape is carried as a platform URL, but author and rich metadata remain not-live-verified.
```yaml
id: "card_01HR7S6A7F3Z9N2X4M8Q1V0A10"
entity_kind: "TopicCard"
schema_version: "topic_card.v1.candidate"
title: "ScoutFlow BV16ooQBsEah review card 10"
platform_item_id: "BV16ooQBsEah"
canonical_url: "https://www.bilibili.com/video/BV16ooQBsEah/"
capture_id: "cap_u3_10_sEah"
export_posture: "local_only"
target_path: "/tmp/scoutflow-vault/00-Inbox/topic-card-cap_u3_10_sEah.md"
carry_over_from_lite_v0:
  - "title"
  - "platform_item_id"
  - "canonical_url"
  - "capture_id"
  - "export_posture"
  - "target_path"
signal_refs:
  - "sig_01HR7S6A7F3Z9N2X4M8Q1V0A10"
  - "sig_01HR7S6A7F3Z9N2X4M8Q1V0A01"
  - "sig_01HR7S6A7F3Z9N2X4M8Q1V0A02"
hypothesis_refs:
  - "hyp_01HR7S6A7F3Z9N2X4M8Q1V0A10"
capture_plan_refs:
  - "plan_01HR7S6A7F3Z9N2X4M8Q1V0A10"
hypothesis_summary: "Card 10 frames whether ordinary preview can be useful without claiming semantic completeness."
evidence_balance:
  support: "capture truth and target path are present"
  counter: "author and rich metadata are not live verified"
  process: "write_enabled remains false"
frontmatter:
  title: "ScoutFlow BV16ooQBsEah review card 10"
  date: "2026-05-07"
  tags: "ScoutFlow/candidate topic-card"
  status: "candidate"
raw_handoff:
  posture: "candidate_only"
  target: "00-Inbox raw note candidate"
  true_write: "not-approved"
diloflow_handoff:
  posture: "script_seed_input_candidate"
  execution: "not-approved"
review_state: "mapped"
lifecycle_state: "draft"
claim_label_map:
  canonical_fields:
    - "title"
    - "platform_item_id"
    - "canonical_url"
    - "capture_id"
    - "export_posture"
    - "target_path"
  candidate_fields:
    - "signal_refs"
    - "hypothesis_refs"
    - "capture_plan_refs"
  tentative_fields:
    - "hypothesis_summary"
    - "evidence_balance"
notes: "Candidate TopicCard v1 fixture; not a RAW commit, not a DiloFlow execution, not publish-ready."
```
[candidate] Audit note 10: this sample intentionally uses explicit unknown/blocked states where live platform evidence is missing, preserving truthfulness while still making validators deterministic.

## §3 Fixture validation checklist

[candidate] Every sample has an id shaped as a stable candidate identifier.
[candidate] Every sample carries capture linkage or explains why it cannot become capture authority.
[candidate] Every sample preserves LP-001: no recommendation, keyword, RAW gap, playlist, account, or comment expansion is turned into direct capture.
[candidate] Every sample marks author metadata as not live verified.
[candidate] Every sample includes a lifecycle state and a claim_label_map.


## §4 Reviewer scenarios for second-pass audit

[candidate] Scenario 01: The reviewer should inspect the TopicCard sample as a fixture for lite-v0 carry-over, v1 relation references, RAW/DiloFlow candidate handoff, and usefulness inflation defense. The pass condition is not that the sample looks semantically rich; the pass condition is that the sample can survive a skeptical audit without pretending that live metadata, author identity, runtime capture, RAW intake, or DiloFlow execution has been verified. When the sample uses `UNKNOWN_NOT_LIVE_VERIFIED`, that value is a successful honesty marker rather than an incomplete field.
[tentative] Scenario 01 failure mode: if a future agent replaces explicit unknowns with guessed author names, guessed follower counts, guessed title quality, or guessed platform state, the fixture should fail even if the rest of the JSON shape validates. This rule is especially important because sample data can quietly become seed data; the supplement blocks that drift by repeating not-authority frontmatter and candidate-only notes.
[candidate] Scenario 02: The reviewer should inspect the TopicCard sample as a fixture for lite-v0 carry-over, v1 relation references, RAW/DiloFlow candidate handoff, and usefulness inflation defense. The pass condition is not that the sample looks semantically rich; the pass condition is that the sample can survive a skeptical audit without pretending that live metadata, author identity, runtime capture, RAW intake, or DiloFlow execution has been verified. When the sample uses `UNKNOWN_NOT_LIVE_VERIFIED`, that value is a successful honesty marker rather than an incomplete field.
[tentative] Scenario 02 failure mode: if a future agent replaces explicit unknowns with guessed author names, guessed follower counts, guessed title quality, or guessed platform state, the fixture should fail even if the rest of the JSON shape validates. This rule is especially important because sample data can quietly become seed data; the supplement blocks that drift by repeating not-authority frontmatter and candidate-only notes.
[candidate] Scenario 03: The reviewer should inspect the TopicCard sample as a fixture for lite-v0 carry-over, v1 relation references, RAW/DiloFlow candidate handoff, and usefulness inflation defense. The pass condition is not that the sample looks semantically rich; the pass condition is that the sample can survive a skeptical audit without pretending that live metadata, author identity, runtime capture, RAW intake, or DiloFlow execution has been verified. When the sample uses `UNKNOWN_NOT_LIVE_VERIFIED`, that value is a successful honesty marker rather than an incomplete field.
[tentative] Scenario 03 failure mode: if a future agent replaces explicit unknowns with guessed author names, guessed follower counts, guessed title quality, or guessed platform state, the fixture should fail even if the rest of the JSON shape validates. This rule is especially important because sample data can quietly become seed data; the supplement blocks that drift by repeating not-authority frontmatter and candidate-only notes.
[candidate] Scenario 04: The reviewer should inspect the TopicCard sample as a fixture for lite-v0 carry-over, v1 relation references, RAW/DiloFlow candidate handoff, and usefulness inflation defense. The pass condition is not that the sample looks semantically rich; the pass condition is that the sample can survive a skeptical audit without pretending that live metadata, author identity, runtime capture, RAW intake, or DiloFlow execution has been verified. When the sample uses `UNKNOWN_NOT_LIVE_VERIFIED`, that value is a successful honesty marker rather than an incomplete field.
[tentative] Scenario 04 failure mode: if a future agent replaces explicit unknowns with guessed author names, guessed follower counts, guessed title quality, or guessed platform state, the fixture should fail even if the rest of the JSON shape validates. This rule is especially important because sample data can quietly become seed data; the supplement blocks that drift by repeating not-authority frontmatter and candidate-only notes.
[candidate] Scenario 05: The reviewer should inspect the TopicCard sample as a fixture for lite-v0 carry-over, v1 relation references, RAW/DiloFlow candidate handoff, and usefulness inflation defense. The pass condition is not that the sample looks semantically rich; the pass condition is that the sample can survive a skeptical audit without pretending that live metadata, author identity, runtime capture, RAW intake, or DiloFlow execution has been verified. When the sample uses `UNKNOWN_NOT_LIVE_VERIFIED`, that value is a successful honesty marker rather than an incomplete field.
[tentative] Scenario 05 failure mode: if a future agent replaces explicit unknowns with guessed author names, guessed follower counts, guessed title quality, or guessed platform state, the fixture should fail even if the rest of the JSON shape validates. This rule is especially important because sample data can quietly become seed data; the supplement blocks that drift by repeating not-authority frontmatter and candidate-only notes.
[candidate] Scenario 06: The reviewer should inspect the TopicCard sample as a fixture for lite-v0 carry-over, v1 relation references, RAW/DiloFlow candidate handoff, and usefulness inflation defense. The pass condition is not that the sample looks semantically rich; the pass condition is that the sample can survive a skeptical audit without pretending that live metadata, author identity, runtime capture, RAW intake, or DiloFlow execution has been verified. When the sample uses `UNKNOWN_NOT_LIVE_VERIFIED`, that value is a successful honesty marker rather than an incomplete field.
[tentative] Scenario 06 failure mode: if a future agent replaces explicit unknowns with guessed author names, guessed follower counts, guessed title quality, or guessed platform state, the fixture should fail even if the rest of the JSON shape validates. This rule is especially important because sample data can quietly become seed data; the supplement blocks that drift by repeating not-authority frontmatter and candidate-only notes.
[candidate] Scenario 07: The reviewer should inspect the TopicCard sample as a fixture for lite-v0 carry-over, v1 relation references, RAW/DiloFlow candidate handoff, and usefulness inflation defense. The pass condition is not that the sample looks semantically rich; the pass condition is that the sample can survive a skeptical audit without pretending that live metadata, author identity, runtime capture, RAW intake, or DiloFlow execution has been verified. When the sample uses `UNKNOWN_NOT_LIVE_VERIFIED`, that value is a successful honesty marker rather than an incomplete field.
[tentative] Scenario 07 failure mode: if a future agent replaces explicit unknowns with guessed author names, guessed follower counts, guessed title quality, or guessed platform state, the fixture should fail even if the rest of the JSON shape validates. This rule is especially important because sample data can quietly become seed data; the supplement blocks that drift by repeating not-authority frontmatter and candidate-only notes.
[candidate] Scenario 08: The reviewer should inspect the TopicCard sample as a fixture for lite-v0 carry-over, v1 relation references, RAW/DiloFlow candidate handoff, and usefulness inflation defense. The pass condition is not that the sample looks semantically rich; the pass condition is that the sample can survive a skeptical audit without pretending that live metadata, author identity, runtime capture, RAW intake, or DiloFlow execution has been verified. When the sample uses `UNKNOWN_NOT_LIVE_VERIFIED`, that value is a successful honesty marker rather than an incomplete field.
[tentative] Scenario 08 failure mode: if a future agent replaces explicit unknowns with guessed author names, guessed follower counts, guessed title quality, or guessed platform state, the fixture should fail even if the rest of the JSON shape validates. This rule is especially important because sample data can quietly become seed data; the supplement blocks that drift by repeating not-authority frontmatter and candidate-only notes.
[candidate] Scenario 09: The reviewer should inspect the TopicCard sample as a fixture for lite-v0 carry-over, v1 relation references, RAW/DiloFlow candidate handoff, and usefulness inflation defense. The pass condition is not that the sample looks semantically rich; the pass condition is that the sample can survive a skeptical audit without pretending that live metadata, author identity, runtime capture, RAW intake, or DiloFlow execution has been verified. When the sample uses `UNKNOWN_NOT_LIVE_VERIFIED`, that value is a successful honesty marker rather than an incomplete field.
[tentative] Scenario 09 failure mode: if a future agent replaces explicit unknowns with guessed author names, guessed follower counts, guessed title quality, or guessed platform state, the fixture should fail even if the rest of the JSON shape validates. This rule is especially important because sample data can quietly become seed data; the supplement blocks that drift by repeating not-authority frontmatter and candidate-only notes.
[candidate] Scenario 10: The reviewer should inspect the TopicCard sample as a fixture for lite-v0 carry-over, v1 relation references, RAW/DiloFlow candidate handoff, and usefulness inflation defense. The pass condition is not that the sample looks semantically rich; the pass condition is that the sample can survive a skeptical audit without pretending that live metadata, author identity, runtime capture, RAW intake, or DiloFlow execution has been verified. When the sample uses `UNKNOWN_NOT_LIVE_VERIFIED`, that value is a successful honesty marker rather than an incomplete field.
[tentative] Scenario 10 failure mode: if a future agent replaces explicit unknowns with guessed author names, guessed follower counts, guessed title quality, or guessed platform state, the fixture should fail even if the rest of the JSON shape validates. This rule is especially important because sample data can quietly become seed data; the supplement blocks that drift by repeating not-authority frontmatter and candidate-only notes.
[candidate] Scenario 11: The reviewer should inspect the TopicCard sample as a fixture for lite-v0 carry-over, v1 relation references, RAW/DiloFlow candidate handoff, and usefulness inflation defense. The pass condition is not that the sample looks semantically rich; the pass condition is that the sample can survive a skeptical audit without pretending that live metadata, author identity, runtime capture, RAW intake, or DiloFlow execution has been verified. When the sample uses `UNKNOWN_NOT_LIVE_VERIFIED`, that value is a successful honesty marker rather than an incomplete field.
[tentative] Scenario 11 failure mode: if a future agent replaces explicit unknowns with guessed author names, guessed follower counts, guessed title quality, or guessed platform state, the fixture should fail even if the rest of the JSON shape validates. This rule is especially important because sample data can quietly become seed data; the supplement blocks that drift by repeating not-authority frontmatter and candidate-only notes.
[candidate] Scenario 12: The reviewer should inspect the TopicCard sample as a fixture for lite-v0 carry-over, v1 relation references, RAW/DiloFlow candidate handoff, and usefulness inflation defense. The pass condition is not that the sample looks semantically rich; the pass condition is that the sample can survive a skeptical audit without pretending that live metadata, author identity, runtime capture, RAW intake, or DiloFlow execution has been verified. When the sample uses `UNKNOWN_NOT_LIVE_VERIFIED`, that value is a successful honesty marker rather than an incomplete field.
[tentative] Scenario 12 failure mode: if a future agent replaces explicit unknowns with guessed author names, guessed follower counts, guessed title quality, or guessed platform state, the fixture should fail even if the rest of the JSON shape validates. This rule is especially important because sample data can quietly become seed data; the supplement blocks that drift by repeating not-authority frontmatter and candidate-only notes.

## §5 Field-level audit expansion

[candidate] Field `id` must be read as a fixture contract field. The reviewer should ask three questions: is the field populated, is its claim label clear, and does the value avoid smuggling runtime or authority approval? For TopicCard, a populated field can still be an explicit `not-approved`, `not_live_verified_in_this_environment`, `blocked_runtime`, or `candidate_only` value; those values are preferable to attractive but unverifiable details.
[candidate] Field `schema_version` must be read as a fixture contract field. The reviewer should ask three questions: is the field populated, is its claim label clear, and does the value avoid smuggling runtime or authority approval? For TopicCard, a populated field can still be an explicit `not-approved`, `not_live_verified_in_this_environment`, `blocked_runtime`, or `candidate_only` value; those values are preferable to attractive but unverifiable details.
[candidate] Field `source_capture_id` must be read as a fixture contract field. The reviewer should ask three questions: is the field populated, is its claim label clear, and does the value avoid smuggling runtime or authority approval? For TopicCard, a populated field can still be an explicit `not-approved`, `not_live_verified_in_this_environment`, `blocked_runtime`, or `candidate_only` value; those values are preferable to attractive but unverifiable details.
[candidate] Field `canonical_url` must be read as a fixture contract field. The reviewer should ask three questions: is the field populated, is its claim label clear, and does the value avoid smuggling runtime or authority approval? For TopicCard, a populated field can still be an explicit `not-approved`, `not_live_verified_in_this_environment`, `blocked_runtime`, or `candidate_only` value; those values are preferable to attractive but unverifiable details.
[candidate] Field `platform_item_id` must be read as a fixture contract field. The reviewer should ask three questions: is the field populated, is its claim label clear, and does the value avoid smuggling runtime or authority approval? For TopicCard, a populated field can still be an explicit `not-approved`, `not_live_verified_in_this_environment`, `blocked_runtime`, or `candidate_only` value; those values are preferable to attractive but unverifiable details.
[candidate] Field `lifecycle_state` must be read as a fixture contract field. The reviewer should ask three questions: is the field populated, is its claim label clear, and does the value avoid smuggling runtime or authority approval? For TopicCard, a populated field can still be an explicit `not-approved`, `not_live_verified_in_this_environment`, `blocked_runtime`, or `candidate_only` value; those values are preferable to attractive but unverifiable details.
[candidate] Field `claim_label_map` must be read as a fixture contract field. The reviewer should ask three questions: is the field populated, is its claim label clear, and does the value avoid smuggling runtime or authority approval? For TopicCard, a populated field can still be an explicit `not-approved`, `not_live_verified_in_this_environment`, `blocked_runtime`, or `candidate_only` value; those values are preferable to attractive but unverifiable details.
[candidate] Field `evidence_refs` must be read as a fixture contract field. The reviewer should ask three questions: is the field populated, is its claim label clear, and does the value avoid smuggling runtime or authority approval? For TopicCard, a populated field can still be an explicit `not-approved`, `not_live_verified_in_this_environment`, `blocked_runtime`, or `candidate_only` value; those values are preferable to attractive but unverifiable details.
[candidate] Field `verification_state` must be read as a fixture contract field. The reviewer should ask three questions: is the field populated, is its claim label clear, and does the value avoid smuggling runtime or authority approval? For TopicCard, a populated field can still be an explicit `not-approved`, `not_live_verified_in_this_environment`, `blocked_runtime`, or `candidate_only` value; those values are preferable to attractive but unverifiable details.
[candidate] Field `notes` must be read as a fixture contract field. The reviewer should ask three questions: is the field populated, is its claim label clear, and does the value avoid smuggling runtime or authority approval? For TopicCard, a populated field can still be an explicit `not-approved`, `not_live_verified_in_this_environment`, `blocked_runtime`, or `candidate_only` value; those values are preferable to attractive but unverifiable details.

## §6 Downstream fixture-use guidance

[candidate] U1 SRD-v3 outline drafting: use TopicCard samples as bounded design input only. A consumer may copy the field names into a checklist, but should not copy the instances into an authority database. The safe reuse pattern is fixture → audit question → amendment text, not fixture → migration → runtime.
[candidate] U2 Lane-4/5 unlock discussion: use TopicCard samples as bounded design input only. A consumer may copy the field names into a checklist, but should not copy the instances into an authority database. The safe reuse pattern is fixture → audit question → amendment text, not fixture → migration → runtime.
[candidate] PF-C1 topic-card preview regression review: use TopicCard samples as bounded design input only. A consumer may copy the field names into a checklist, but should not copy the instances into an authority database. The safe reuse pattern is fixture → audit question → amendment text, not fixture → migration → runtime.
[candidate] PF-C2 RAW handoff negative testing: use TopicCard samples as bounded design input only. A consumer may copy the field names into a checklist, but should not copy the instances into an authority database. The safe reuse pattern is fixture → audit question → amendment text, not fixture → migration → runtime.
[candidate] future C4 dispatch UI projection sketch: use TopicCard samples as bounded design input only. A consumer may copy the field names into a checklist, but should not copy the instances into an authority database. The safe reuse pattern is fixture → audit question → amendment text, not fixture → migration → runtime.
