---
status: candidate / openapi_golden_fragment / not-authority
authority: not-authority
execution_approval: not-approved
runtime_approval: not-approved
migration_approval: not-approved
created_at: 2026-05-07
supplement_for: cloud-output-U3-entity-v0-contracts-2026-05-07.zip
---
# OPENAPI-GOLDEN-FRAGMENT-2026-05-07

[canonical] This is an OpenAPI 3.1 golden fragment for candidate IR review only. It is not registered in FastAPI, not exposed by ScoutFlow, and not an approval to add endpoints.
[candidate] The fragment uses explicit `x-scoutflow-candidate-only: true`, `x-runtime-approval: not-approved`, and `x-migration-approval: not-approved` markers so readers cannot confuse it with an implemented API.
[candidate] Paths are named under `/candidate-ir/*` to make non-runtime status visible. Real current routes remain the Phase 1A capture, job receipt, trust trace, and bridge preview surfaces.
```yaml
openapi: 3.1.0
info:
  title: ScoutFlow Entity Candidate IR Golden Fragment
  version: 0.0.0-candidate
  summary: Candidate-only fragment for Signal, Hypothesis, CapturePlan, and TopicCard.
  description: >-
    This fragment is a design artifact. It must not be mounted, generated into a client,
    or treated as an exposed endpoint without a future amendment and implementation lane.
x-scoutflow-candidate-only: true
x-runtime-approval: not-approved
x-migration-approval: not-approved
servers:
  - url: http://127.0.0.1:0
    description: non-routable placeholder server for candidate docs only
paths:
  /candidate-ir/signals:
    get:
      operationId: listSignalCandidatesNotImplemented
      summary: Candidate list of Signal IR objects; not implemented.
      x-scoutflow-candidate-only: true
      responses:
        '200':
          description: Candidate fixture list.
          content:
            application/json:
              schema:
                type: object
                required: [items, candidate_only]
                properties:
                  candidate_only: { type: boolean, const: true }
                  items:
                    type: array
                    items: { $ref: '#/components/schemas/SignalV0Candidate' }
    post:
      operationId: createSignalCandidateNotImplemented
      summary: Candidate create shape; not an exposed endpoint.
      x-scoutflow-candidate-only: true
      requestBody:
        required: true
        content:
          application/json:
            schema: { $ref: '#/components/schemas/SignalV0Candidate' }
      responses:
        '202': { description: Candidate accepted in fixture review only }
  /candidate-ir/signals/{signal_id}:
    parameters:
      - name: signal_id
        in: path
        required: true
        schema: { type: string, minLength: 1 }
    get:
      operationId: getSignalCandidateNotImplemented
      summary: Candidate read shape; not implemented.
      x-scoutflow-candidate-only: true
      responses:
        '200':
          description: Candidate Signal object.
          content: { application/json: { schema: { $ref: '#/components/schemas/SignalV0Candidate' } } }
    patch:
      operationId: archiveSignalCandidateNotImplemented
      summary: Candidate archive/project action; delete is intentionally absent.
      x-scoutflow-candidate-only: true
      responses:
        '202': { description: Candidate lifecycle transition preview only }
  /candidate-ir/hypotheses:
    get:
      operationId: listHypothesisCandidatesNotImplemented
      x-scoutflow-candidate-only: true
      responses:
        '200':
          description: Candidate fixture list.
          content: { application/json: { schema: { type: object, properties: { candidate_only: { type: boolean, const: true }, items: { type: array, items: { $ref: '#/components/schemas/HypothesisV0Candidate' } } } } } }
    post:
      operationId: createHypothesisCandidateNotImplemented
      x-scoutflow-candidate-only: true
      requestBody:
        required: true
        content: { application/json: { schema: { $ref: '#/components/schemas/HypothesisV0Candidate' } } }
      responses:
        '202': { description: Candidate fixture create only }
  /candidate-ir/hypotheses/{hypothesis_id}:
    parameters:
      - { name: hypothesis_id, in: path, required: true, schema: { type: string, minLength: 1 } }
    get:
      operationId: getHypothesisCandidateNotImplemented
      x-scoutflow-candidate-only: true
      responses:
        '200': { description: Candidate object, content: { application/json: { schema: { $ref: '#/components/schemas/HypothesisV0Candidate' } } } }
    patch:
      operationId: verdictHypothesisCandidateNotImplemented
      x-scoutflow-candidate-only: true
      responses:
        '202': { description: Candidate verdict preview; may suspend linked plans in fixture only }
  /candidate-ir/capture-plans:
    get:
      operationId: listCapturePlanCandidatesNotImplemented
      x-scoutflow-candidate-only: true
      responses:
        '200': { description: Candidate fixture list, content: { application/json: { schema: { type: object, properties: { candidate_only: { type: boolean, const: true }, items: { type: array, items: { $ref: '#/components/schemas/CapturePlanV0Candidate' } } } } } } }
    post:
      operationId: createCapturePlanCandidateNotImplemented
      summary: Candidate plan shape only; must not emit capture jobs.
      x-scoutflow-candidate-only: true
      requestBody:
        required: true
        content: { application/json: { schema: { $ref: '#/components/schemas/CapturePlanV0Candidate' } } }
      responses:
        '202': { description: Candidate fixture create only }
  /candidate-ir/capture-plans/{capture_plan_id}:
    parameters:
      - { name: capture_plan_id, in: path, required: true, schema: { type: string, minLength: 1 } }
    get:
      operationId: getCapturePlanCandidateNotImplemented
      x-scoutflow-candidate-only: true
      responses:
        '200': { description: Candidate object, content: { application/json: { schema: { $ref: '#/components/schemas/CapturePlanV0Candidate' } } } }
    patch:
      operationId: suspendCapturePlanCandidateNotImplemented
      summary: Candidate lifecycle patch; not a scheduler endpoint.
      x-scoutflow-candidate-only: true
      responses:
        '202': { description: Candidate lifecycle transition only }
  /candidate-ir/topic-cards:
    get:
      operationId: listTopicCardCandidatesNotImplemented
      x-scoutflow-candidate-only: true
      responses:
        '200': { description: Candidate fixture list, content: { application/json: { schema: { type: object, properties: { candidate_only: { type: boolean, const: true }, items: { type: array, items: { $ref: '#/components/schemas/TopicCardV1Candidate' } } } } } } }
    post:
      operationId: createTopicCardCandidateNotImplemented
      summary: Candidate TopicCard v1 shape; not RAW write, not DiloFlow execution.
      x-scoutflow-candidate-only: true
      requestBody:
        required: true
        content: { application/json: { schema: { $ref: '#/components/schemas/TopicCardV1Candidate' } } }
      responses:
        '202': { description: Candidate fixture create only }
  /candidate-ir/topic-cards/{topic_card_id}:
    parameters:
      - { name: topic_card_id, in: path, required: true, schema: { type: string, minLength: 1 } }
    get:
      operationId: getTopicCardCandidateNotImplemented
      x-scoutflow-candidate-only: true
      responses:
        '200': { description: Candidate object, content: { application/json: { schema: { $ref: '#/components/schemas/TopicCardV1Candidate' } } } }
    patch:
      operationId: archiveTopicCardCandidateNotImplemented
      summary: Candidate lifecycle patch; delete is intentionally absent.
      x-scoutflow-candidate-only: true
      responses:
        '202': { description: Candidate lifecycle transition only }
components:
  schemas:
    CandidateMeta:
      type: object
      required: [candidate_only, authority, runtime_approval, migration_approval]
      properties:
        candidate_only: { type: boolean, const: true }
        authority: { type: string, const: not-authority }
        runtime_approval: { type: string, const: not-approved }
        migration_approval: { type: string, const: not-approved }
    ClaimLabelMap:
      type: object
      properties:
        canonical_fields: { type: array, items: { type: string } }
        candidate_fields: { type: array, items: { type: string } }
        tentative_fields: { type: array, items: { type: string } }
      additionalProperties: false
    SignalV0Candidate:
      type: object
      required: [id, entity_kind, schema_version, source_capture_id, canonical_url, observation_kind, observation_text, lifecycle_state, claim_label_map, candidate_meta]
      additionalProperties: false
      properties:
        id: { type: string, pattern: '^sig_[A-Z0-9]{26}$' }
        entity_kind: { type: string, const: Signal }
        schema_version: { type: string, const: signal.v0.candidate }
        source_capture_id: { type: string, minLength: 1 }
        platform: { type: string, enum: [bilibili, xhs, youtube, cross_platform, unknown] }
        platform_item_id: { type: string }
        canonical_url: { type: string, format: uri }
        source_author_display_name: { type: string }
        source_author_verification_state: { type: string, enum: [live_verified, not_live_verified_in_this_environment, unknown] }
        observation_kind: { type: string }
        observation_text: { type: string, minLength: 1 }
        observation_value: { type: string }
        evidence_refs: { type: array, items: { type: string } }
        lifecycle_state: { type: string, enum: [draft, observed, validated, conflicted, broken_reference, archived] }
        claim_label_map: { $ref: '#/components/schemas/ClaimLabelMap' }
        candidate_meta: { $ref: '#/components/schemas/CandidateMeta' }
      examples:
        - id: sig_01HR7S6A7F3Z9N2X4M8Q1V0A01
          entity_kind: Signal
          schema_version: signal.v0.candidate
          source_capture_id: cap_u3_01_sEah
          platform: bilibili
          platform_item_id: BV16ooQBsEah
          canonical_url: https://www.bilibili.com/video/BV16ooQBsEah/
          source_author_display_name: UNKNOWN_NOT_LIVE_VERIFIED
          source_author_verification_state: not_live_verified_in_this_environment
          observation_kind: preview_usefulness
          observation_text: metadata-only preview is present but needs edit
          observation_value: needs_edit
          evidence_refs: [pf-c1-url-ordinary, human-verdict-needs-edit]
          lifecycle_state: observed
          claim_label_map: { canonical_fields: [id, source_capture_id, canonical_url], candidate_fields: [observation_kind, observation_text], tentative_fields: [source_author_display_name] }
          candidate_meta: { candidate_only: true, authority: not-authority, runtime_approval: not-approved, migration_approval: not-approved }
    HypothesisV0Candidate:
      type: object
      required: [id, entity_kind, schema_version, claim_text, support_signal_ids, counter_signal_ids, user_verdict, lifecycle_state, candidate_meta]
      additionalProperties: false
      properties:
        id: { type: string, pattern: '^hyp_[A-Z0-9]{26}$' }
        entity_kind: { type: string, const: Hypothesis }
        schema_version: { type: string, const: hypothesis.v0.candidate }
        title: { type: string }
        claim_text: { type: string, minLength: 1 }
        testability: { type: string }
        source_capture_ids: { type: array, items: { type: string } }
        support_signal_ids: { type: array, items: { type: string } }
        counter_signal_ids: { type: array, items: { type: string } }
        neutral_signal_ids: { type: array, items: { type: string } }
        user_verdict: { type: string, enum: [pending, needs_edit, follow, reject, park] }
        lifecycle_state: { type: string, enum: [draft, under_review, accepted_for_plan, rejected, archived, needs_repair] }
        candidate_meta: { $ref: '#/components/schemas/CandidateMeta' }
      examples:
        - id: hyp_01HR7S6A7F3Z9N2X4M8Q1V0A01
          entity_kind: Hypothesis
          schema_version: hypothesis.v0.candidate
          title: Preview usefulness requires evidence balance
          claim_text: Topic-card usefulness is plausible only if support and counter signals remain visible.
          testability: human verdict plus edit-cost log
          source_capture_ids: [cap_u3_01_sEah]
          support_signal_ids: [sig_01HR7S6A7F3Z9N2X4M8Q1V0A01]
          counter_signal_ids: [sig_01HR7S6A7F3Z9N2X4M8Q1V0A02]
          neutral_signal_ids: []
          user_verdict: needs_edit
          lifecycle_state: under_review
          candidate_meta: { candidate_only: true, authority: not-authority, runtime_approval: not-approved, migration_approval: not-approved }
    CapturePlanV0Candidate:
      type: object
      required: [id, entity_kind, schema_version, source_hypothesis_ids, planned_urls, enrichment_level, runtime_gate_state, lifecycle_state, candidate_meta]
      additionalProperties: false
      properties:
        id: { type: string, pattern: '^plan_[A-Z0-9]{26}$' }
        entity_kind: { type: string, const: CapturePlan }
        schema_version: { type: string, const: capture_plan.v0.candidate }
        plan_title: { type: string }
        source_hypothesis_ids: { type: array, items: { type: string } }
        source_signal_ids: { type: array, items: { type: string } }
        planned_urls:
          type: array
          items:
            type: object
            required: [platform, url, source_kind, allowed_preset]
            properties:
              platform: { type: string }
              url: { type: string, format: uri }
              source_kind: { type: string }
              allowed_preset: { type: string, const: metadata_only }
        enrichment_level: { type: string, enum: [metadata_only] }
        blocked_enrichments: { type: array, items: { type: string } }
        runtime_gate_state: { type: string, const: not-approved }
        lifecycle_state: { type: string, enum: [draft, scoped, approved_candidate, suspended, blocked_runtime, archived] }
        candidate_meta: { $ref: '#/components/schemas/CandidateMeta' }
      examples:
        - id: plan_01HR7S6A7F3Z9N2X4M8Q1V0A01
          entity_kind: CapturePlan
          schema_version: capture_plan.v0.candidate
          plan_title: bounded metadata follow-up
          source_hypothesis_ids: [hyp_01HR7S6A7F3Z9N2X4M8Q1V0A01]
          source_signal_ids: [sig_01HR7S6A7F3Z9N2X4M8Q1V0A01]
          planned_urls: [{ platform: bilibili, url: https://www.bilibili.com/video/BV16ooQBsEah/, source_kind: manual_url, allowed_preset: metadata_only }]
          enrichment_level: metadata_only
          blocked_enrichments: [audio_transcript, comments, danmaku, media_download]
          runtime_gate_state: not-approved
          lifecycle_state: scoped
          candidate_meta: { candidate_only: true, authority: not-authority, runtime_approval: not-approved, migration_approval: not-approved }
    TopicCardV1Candidate:
      type: object
      required: [id, entity_kind, schema_version, title, platform_item_id, canonical_url, capture_id, export_posture, target_path, signal_refs, hypothesis_refs, lifecycle_state, candidate_meta]
      additionalProperties: false
      properties:
        id: { type: string, pattern: '^card_[A-Z0-9]{26}$' }
        entity_kind: { type: string, const: TopicCard }
        schema_version: { type: string, const: topic_card.v1.candidate }
        title: { type: string, minLength: 1 }
        platform_item_id: { type: string, minLength: 1 }
        canonical_url: { type: string, format: uri }
        capture_id: { type: string, minLength: 1 }
        export_posture: { type: string, enum: [local_only, handoff_candidate] }
        target_path: { type: string, minLength: 1 }
        signal_refs: { type: array, items: { type: string } }
        hypothesis_refs: { type: array, items: { type: string } }
        capture_plan_refs: { type: array, items: { type: string } }
        evidence_balance: { type: object, additionalProperties: true }
        raw_handoff:
          type: object
          properties:
            posture: { type: string, enum: [candidate_only] }
            true_write: { type: string, const: not-approved }
        diloflow_handoff:
          type: object
          properties:
            posture: { type: string }
            execution: { type: string, const: not-approved }
        lifecycle_state: { type: string, enum: [draft, reviewable, handoff_candidate, returned_for_edit, archived] }
        candidate_meta: { $ref: '#/components/schemas/CandidateMeta' }
      examples:
        - id: card_01HR7S6A7F3Z9N2X4M8Q1V0A01
          entity_kind: TopicCard
          schema_version: topic_card.v1.candidate
          title: ScoutFlow BV16ooQBsEah review card
          platform_item_id: BV16ooQBsEah
          canonical_url: https://www.bilibili.com/video/BV16ooQBsEah/
          capture_id: cap_u3_01_sEah
          export_posture: handoff_candidate
          target_path: /tmp/scoutflow-vault/00-Inbox/topic-card-cap_u3_01_sEah.md
          signal_refs: [sig_01HR7S6A7F3Z9N2X4M8Q1V0A01]
          hypothesis_refs: [hyp_01HR7S6A7F3Z9N2X4M8Q1V0A01]
          capture_plan_refs: [plan_01HR7S6A7F3Z9N2X4M8Q1V0A01]
          evidence_balance: { support: capture truth preserved, counter: author and semantic richness not live verified }
          raw_handoff: { posture: candidate_only, true_write: not-approved }
          diloflow_handoff: { posture: script_seed_input_candidate, execution: not-approved }
          lifecycle_state: reviewable
          candidate_meta: { candidate_only: true, authority: not-authority, runtime_approval: not-approved, migration_approval: not-approved }
```

## §2 Endpoint count and redline summary

[candidate] 16 candidate operations are drafted: list/create/read/patch for 4 entities.
[candidate] All operations are named `NotImplemented` to prevent client-generation confusion.
[candidate] Delete operations are intentionally absent; archive/suspend/project are the safer lifecycle actions.
[candidate] The fragment should be used as an egress contract anchor for U1/U2 discussion only, not as a production route map.


## §3 Schema-consumer guidance

[candidate] Signal OpenAPI guidance 1: a consumer should treat the schema as a golden fragment for fixture validation and cross-project vocabulary alignment. It should not generate a client that calls `/candidate-ir/*`, because those paths are intentionally non-routable. The useful output is a shared expectation about required fields, lifecycle states, claim labels, and candidate_meta markers.
[candidate] Signal OpenAPI guidance 2: a consumer should treat the schema as a golden fragment for fixture validation and cross-project vocabulary alignment. It should not generate a client that calls `/candidate-ir/*`, because those paths are intentionally non-routable. The useful output is a shared expectation about required fields, lifecycle states, claim labels, and candidate_meta markers.
[candidate] Signal OpenAPI guidance 3: a consumer should treat the schema as a golden fragment for fixture validation and cross-project vocabulary alignment. It should not generate a client that calls `/candidate-ir/*`, because those paths are intentionally non-routable. The useful output is a shared expectation about required fields, lifecycle states, claim labels, and candidate_meta markers.
[candidate] Signal OpenAPI guidance 4: a consumer should treat the schema as a golden fragment for fixture validation and cross-project vocabulary alignment. It should not generate a client that calls `/candidate-ir/*`, because those paths are intentionally non-routable. The useful output is a shared expectation about required fields, lifecycle states, claim labels, and candidate_meta markers.
[candidate] Signal OpenAPI guidance 5: a consumer should treat the schema as a golden fragment for fixture validation and cross-project vocabulary alignment. It should not generate a client that calls `/candidate-ir/*`, because those paths are intentionally non-routable. The useful output is a shared expectation about required fields, lifecycle states, claim labels, and candidate_meta markers.
[candidate] Signal OpenAPI guidance 6: a consumer should treat the schema as a golden fragment for fixture validation and cross-project vocabulary alignment. It should not generate a client that calls `/candidate-ir/*`, because those paths are intentionally non-routable. The useful output is a shared expectation about required fields, lifecycle states, claim labels, and candidate_meta markers.
[candidate] Signal OpenAPI guidance 7: a consumer should treat the schema as a golden fragment for fixture validation and cross-project vocabulary alignment. It should not generate a client that calls `/candidate-ir/*`, because those paths are intentionally non-routable. The useful output is a shared expectation about required fields, lifecycle states, claim labels, and candidate_meta markers.
[candidate] Signal OpenAPI guidance 8: a consumer should treat the schema as a golden fragment for fixture validation and cross-project vocabulary alignment. It should not generate a client that calls `/candidate-ir/*`, because those paths are intentionally non-routable. The useful output is a shared expectation about required fields, lifecycle states, claim labels, and candidate_meta markers.
[candidate] Hypothesis OpenAPI guidance 1: a consumer should treat the schema as a golden fragment for fixture validation and cross-project vocabulary alignment. It should not generate a client that calls `/candidate-ir/*`, because those paths are intentionally non-routable. The useful output is a shared expectation about required fields, lifecycle states, claim labels, and candidate_meta markers.
[candidate] Hypothesis OpenAPI guidance 2: a consumer should treat the schema as a golden fragment for fixture validation and cross-project vocabulary alignment. It should not generate a client that calls `/candidate-ir/*`, because those paths are intentionally non-routable. The useful output is a shared expectation about required fields, lifecycle states, claim labels, and candidate_meta markers.
[candidate] Hypothesis OpenAPI guidance 3: a consumer should treat the schema as a golden fragment for fixture validation and cross-project vocabulary alignment. It should not generate a client that calls `/candidate-ir/*`, because those paths are intentionally non-routable. The useful output is a shared expectation about required fields, lifecycle states, claim labels, and candidate_meta markers.
[candidate] Hypothesis OpenAPI guidance 4: a consumer should treat the schema as a golden fragment for fixture validation and cross-project vocabulary alignment. It should not generate a client that calls `/candidate-ir/*`, because those paths are intentionally non-routable. The useful output is a shared expectation about required fields, lifecycle states, claim labels, and candidate_meta markers.
[candidate] Hypothesis OpenAPI guidance 5: a consumer should treat the schema as a golden fragment for fixture validation and cross-project vocabulary alignment. It should not generate a client that calls `/candidate-ir/*`, because those paths are intentionally non-routable. The useful output is a shared expectation about required fields, lifecycle states, claim labels, and candidate_meta markers.
[candidate] Hypothesis OpenAPI guidance 6: a consumer should treat the schema as a golden fragment for fixture validation and cross-project vocabulary alignment. It should not generate a client that calls `/candidate-ir/*`, because those paths are intentionally non-routable. The useful output is a shared expectation about required fields, lifecycle states, claim labels, and candidate_meta markers.
[candidate] Hypothesis OpenAPI guidance 7: a consumer should treat the schema as a golden fragment for fixture validation and cross-project vocabulary alignment. It should not generate a client that calls `/candidate-ir/*`, because those paths are intentionally non-routable. The useful output is a shared expectation about required fields, lifecycle states, claim labels, and candidate_meta markers.
[candidate] Hypothesis OpenAPI guidance 8: a consumer should treat the schema as a golden fragment for fixture validation and cross-project vocabulary alignment. It should not generate a client that calls `/candidate-ir/*`, because those paths are intentionally non-routable. The useful output is a shared expectation about required fields, lifecycle states, claim labels, and candidate_meta markers.
[candidate] CapturePlan OpenAPI guidance 1: a consumer should treat the schema as a golden fragment for fixture validation and cross-project vocabulary alignment. It should not generate a client that calls `/candidate-ir/*`, because those paths are intentionally non-routable. The useful output is a shared expectation about required fields, lifecycle states, claim labels, and candidate_meta markers.
[candidate] CapturePlan OpenAPI guidance 2: a consumer should treat the schema as a golden fragment for fixture validation and cross-project vocabulary alignment. It should not generate a client that calls `/candidate-ir/*`, because those paths are intentionally non-routable. The useful output is a shared expectation about required fields, lifecycle states, claim labels, and candidate_meta markers.
[candidate] CapturePlan OpenAPI guidance 3: a consumer should treat the schema as a golden fragment for fixture validation and cross-project vocabulary alignment. It should not generate a client that calls `/candidate-ir/*`, because those paths are intentionally non-routable. The useful output is a shared expectation about required fields, lifecycle states, claim labels, and candidate_meta markers.
[candidate] CapturePlan OpenAPI guidance 4: a consumer should treat the schema as a golden fragment for fixture validation and cross-project vocabulary alignment. It should not generate a client that calls `/candidate-ir/*`, because those paths are intentionally non-routable. The useful output is a shared expectation about required fields, lifecycle states, claim labels, and candidate_meta markers.
[candidate] CapturePlan OpenAPI guidance 5: a consumer should treat the schema as a golden fragment for fixture validation and cross-project vocabulary alignment. It should not generate a client that calls `/candidate-ir/*`, because those paths are intentionally non-routable. The useful output is a shared expectation about required fields, lifecycle states, claim labels, and candidate_meta markers.
[candidate] CapturePlan OpenAPI guidance 6: a consumer should treat the schema as a golden fragment for fixture validation and cross-project vocabulary alignment. It should not generate a client that calls `/candidate-ir/*`, because those paths are intentionally non-routable. The useful output is a shared expectation about required fields, lifecycle states, claim labels, and candidate_meta markers.
[candidate] CapturePlan OpenAPI guidance 7: a consumer should treat the schema as a golden fragment for fixture validation and cross-project vocabulary alignment. It should not generate a client that calls `/candidate-ir/*`, because those paths are intentionally non-routable. The useful output is a shared expectation about required fields, lifecycle states, claim labels, and candidate_meta markers.
[candidate] CapturePlan OpenAPI guidance 8: a consumer should treat the schema as a golden fragment for fixture validation and cross-project vocabulary alignment. It should not generate a client that calls `/candidate-ir/*`, because those paths are intentionally non-routable. The useful output is a shared expectation about required fields, lifecycle states, claim labels, and candidate_meta markers.
[candidate] TopicCard OpenAPI guidance 1: a consumer should treat the schema as a golden fragment for fixture validation and cross-project vocabulary alignment. It should not generate a client that calls `/candidate-ir/*`, because those paths are intentionally non-routable. The useful output is a shared expectation about required fields, lifecycle states, claim labels, and candidate_meta markers.
[candidate] TopicCard OpenAPI guidance 2: a consumer should treat the schema as a golden fragment for fixture validation and cross-project vocabulary alignment. It should not generate a client that calls `/candidate-ir/*`, because those paths are intentionally non-routable. The useful output is a shared expectation about required fields, lifecycle states, claim labels, and candidate_meta markers.
[candidate] TopicCard OpenAPI guidance 3: a consumer should treat the schema as a golden fragment for fixture validation and cross-project vocabulary alignment. It should not generate a client that calls `/candidate-ir/*`, because those paths are intentionally non-routable. The useful output is a shared expectation about required fields, lifecycle states, claim labels, and candidate_meta markers.
[candidate] TopicCard OpenAPI guidance 4: a consumer should treat the schema as a golden fragment for fixture validation and cross-project vocabulary alignment. It should not generate a client that calls `/candidate-ir/*`, because those paths are intentionally non-routable. The useful output is a shared expectation about required fields, lifecycle states, claim labels, and candidate_meta markers.
[candidate] TopicCard OpenAPI guidance 5: a consumer should treat the schema as a golden fragment for fixture validation and cross-project vocabulary alignment. It should not generate a client that calls `/candidate-ir/*`, because those paths are intentionally non-routable. The useful output is a shared expectation about required fields, lifecycle states, claim labels, and candidate_meta markers.
[candidate] TopicCard OpenAPI guidance 6: a consumer should treat the schema as a golden fragment for fixture validation and cross-project vocabulary alignment. It should not generate a client that calls `/candidate-ir/*`, because those paths are intentionally non-routable. The useful output is a shared expectation about required fields, lifecycle states, claim labels, and candidate_meta markers.
[candidate] TopicCard OpenAPI guidance 7: a consumer should treat the schema as a golden fragment for fixture validation and cross-project vocabulary alignment. It should not generate a client that calls `/candidate-ir/*`, because those paths are intentionally non-routable. The useful output is a shared expectation about required fields, lifecycle states, claim labels, and candidate_meta markers.
[candidate] TopicCard OpenAPI guidance 8: a consumer should treat the schema as a golden fragment for fixture validation and cross-project vocabulary alignment. It should not generate a client that calls `/candidate-ir/*`, because those paths are intentionally non-routable. The useful output is a shared expectation about required fields, lifecycle states, claim labels, and candidate_meta markers.

## §4 Negative OpenAPI examples

[candidate] Negative example `Missing candidate_meta`: reject the example because not-authority/runtime/migration boundaries are not machine-visible. This negative test is part of the golden-fragment contract because the main danger is not schema invalidity; it is overclaiming execution, migration, or source truth.
[candidate] Negative example `POST /candidate-ir/capture-plans treated as scheduler`: reject because candidate path is not runtime and no job may be emitted. This negative test is part of the golden-fragment contract because the main danger is not schema invalidity; it is overclaiming execution, migration, or source truth.
[candidate] Negative example `TopicCard raw_handoff true_write=true`: reject because RAW true write is not approved. This negative test is part of the golden-fragment contract because the main danger is not schema invalidity; it is overclaiming execution, migration, or source truth.
[candidate] Negative example `DiloFlow execution approved`: reject because DiloFlow consumption is candidate-only. This negative test is part of the golden-fragment contract because the main danger is not schema invalidity; it is overclaiming execution, migration, or source truth.
[candidate] Negative example `Delete operation added`: reject because delete is excluded; archive/suspend are the lifecycle operations. This negative test is part of the golden-fragment contract because the main danger is not schema invalidity; it is overclaiming execution, migration, or source truth.
[candidate] Negative example `OpenAPI server set to live 127.0.0.1 port`: reject because fragment should not imply mounted endpoint. This negative test is part of the golden-fragment contract because the main danger is not schema invalidity; it is overclaiming execution, migration, or source truth.
[candidate] Negative example `Author metadata marked live_verified without evidence`: reject because live verification was not performed. This negative test is part of the golden-fragment contract because the main danger is not schema invalidity; it is overclaiming execution, migration, or source truth.
[candidate] Negative example `CapturePlan enrichment_level includes audio_transcript`: reject because audio_transcript remains blocked. This negative test is part of the golden-fragment contract because the main danger is not schema invalidity; it is overclaiming execution, migration, or source truth.


## §5 OpenAPI fragment implementation redline scan

[candidate] OpenAPI redline scan 01: if this fragment appears in generated client code, route registration, tests that hit a live server, or an API documentation page for users, the consuming lane has crossed the boundary. The only safe locations are research docs, fixture validators, and handoff notes that preserve `candidate_only=true` and `runtime_approval=not-approved`.
[tentative] OpenAPI repair 01: convert any tempting implementation detail into a non-routable example. For example, replace a real server URL with `http://127.0.0.1:0`, keep operationIds ending in `NotImplemented`, and make every response description say fixture or candidate. This makes the schema useful for alignment while preventing accidental endpoint exposure.
[candidate] OpenAPI redline scan 02: if this fragment appears in generated client code, route registration, tests that hit a live server, or an API documentation page for users, the consuming lane has crossed the boundary. The only safe locations are research docs, fixture validators, and handoff notes that preserve `candidate_only=true` and `runtime_approval=not-approved`.
[tentative] OpenAPI repair 02: convert any tempting implementation detail into a non-routable example. For example, replace a real server URL with `http://127.0.0.1:0`, keep operationIds ending in `NotImplemented`, and make every response description say fixture or candidate. This makes the schema useful for alignment while preventing accidental endpoint exposure.
[candidate] OpenAPI redline scan 03: if this fragment appears in generated client code, route registration, tests that hit a live server, or an API documentation page for users, the consuming lane has crossed the boundary. The only safe locations are research docs, fixture validators, and handoff notes that preserve `candidate_only=true` and `runtime_approval=not-approved`.
[tentative] OpenAPI repair 03: convert any tempting implementation detail into a non-routable example. For example, replace a real server URL with `http://127.0.0.1:0`, keep operationIds ending in `NotImplemented`, and make every response description say fixture or candidate. This makes the schema useful for alignment while preventing accidental endpoint exposure.
[candidate] OpenAPI redline scan 04: if this fragment appears in generated client code, route registration, tests that hit a live server, or an API documentation page for users, the consuming lane has crossed the boundary. The only safe locations are research docs, fixture validators, and handoff notes that preserve `candidate_only=true` and `runtime_approval=not-approved`.
[tentative] OpenAPI repair 04: convert any tempting implementation detail into a non-routable example. For example, replace a real server URL with `http://127.0.0.1:0`, keep operationIds ending in `NotImplemented`, and make every response description say fixture or candidate. This makes the schema useful for alignment while preventing accidental endpoint exposure.
[candidate] OpenAPI redline scan 05: if this fragment appears in generated client code, route registration, tests that hit a live server, or an API documentation page for users, the consuming lane has crossed the boundary. The only safe locations are research docs, fixture validators, and handoff notes that preserve `candidate_only=true` and `runtime_approval=not-approved`.
[tentative] OpenAPI repair 05: convert any tempting implementation detail into a non-routable example. For example, replace a real server URL with `http://127.0.0.1:0`, keep operationIds ending in `NotImplemented`, and make every response description say fixture or candidate. This makes the schema useful for alignment while preventing accidental endpoint exposure.
[candidate] OpenAPI redline scan 06: if this fragment appears in generated client code, route registration, tests that hit a live server, or an API documentation page for users, the consuming lane has crossed the boundary. The only safe locations are research docs, fixture validators, and handoff notes that preserve `candidate_only=true` and `runtime_approval=not-approved`.
[tentative] OpenAPI repair 06: convert any tempting implementation detail into a non-routable example. For example, replace a real server URL with `http://127.0.0.1:0`, keep operationIds ending in `NotImplemented`, and make every response description say fixture or candidate. This makes the schema useful for alignment while preventing accidental endpoint exposure.
[candidate] OpenAPI redline scan 07: if this fragment appears in generated client code, route registration, tests that hit a live server, or an API documentation page for users, the consuming lane has crossed the boundary. The only safe locations are research docs, fixture validators, and handoff notes that preserve `candidate_only=true` and `runtime_approval=not-approved`.
[tentative] OpenAPI repair 07: convert any tempting implementation detail into a non-routable example. For example, replace a real server URL with `http://127.0.0.1:0`, keep operationIds ending in `NotImplemented`, and make every response description say fixture or candidate. This makes the schema useful for alignment while preventing accidental endpoint exposure.
[candidate] OpenAPI redline scan 08: if this fragment appears in generated client code, route registration, tests that hit a live server, or an API documentation page for users, the consuming lane has crossed the boundary. The only safe locations are research docs, fixture validators, and handoff notes that preserve `candidate_only=true` and `runtime_approval=not-approved`.
[tentative] OpenAPI repair 08: convert any tempting implementation detail into a non-routable example. For example, replace a real server URL with `http://127.0.0.1:0`, keep operationIds ending in `NotImplemented`, and make every response description say fixture or candidate. This makes the schema useful for alignment while preventing accidental endpoint exposure.
[candidate] OpenAPI redline scan 09: if this fragment appears in generated client code, route registration, tests that hit a live server, or an API documentation page for users, the consuming lane has crossed the boundary. The only safe locations are research docs, fixture validators, and handoff notes that preserve `candidate_only=true` and `runtime_approval=not-approved`.
[tentative] OpenAPI repair 09: convert any tempting implementation detail into a non-routable example. For example, replace a real server URL with `http://127.0.0.1:0`, keep operationIds ending in `NotImplemented`, and make every response description say fixture or candidate. This makes the schema useful for alignment while preventing accidental endpoint exposure.
[candidate] OpenAPI redline scan 10: if this fragment appears in generated client code, route registration, tests that hit a live server, or an API documentation page for users, the consuming lane has crossed the boundary. The only safe locations are research docs, fixture validators, and handoff notes that preserve `candidate_only=true` and `runtime_approval=not-approved`.
[tentative] OpenAPI repair 10: convert any tempting implementation detail into a non-routable example. For example, replace a real server URL with `http://127.0.0.1:0`, keep operationIds ending in `NotImplemented`, and make every response description say fixture or candidate. This makes the schema useful for alignment while preventing accidental endpoint exposure.
[candidate] OpenAPI redline scan 11: if this fragment appears in generated client code, route registration, tests that hit a live server, or an API documentation page for users, the consuming lane has crossed the boundary. The only safe locations are research docs, fixture validators, and handoff notes that preserve `candidate_only=true` and `runtime_approval=not-approved`.
[tentative] OpenAPI repair 11: convert any tempting implementation detail into a non-routable example. For example, replace a real server URL with `http://127.0.0.1:0`, keep operationIds ending in `NotImplemented`, and make every response description say fixture or candidate. This makes the schema useful for alignment while preventing accidental endpoint exposure.
[candidate] OpenAPI redline scan 12: if this fragment appears in generated client code, route registration, tests that hit a live server, or an API documentation page for users, the consuming lane has crossed the boundary. The only safe locations are research docs, fixture validators, and handoff notes that preserve `candidate_only=true` and `runtime_approval=not-approved`.
[tentative] OpenAPI repair 12: convert any tempting implementation detail into a non-routable example. For example, replace a real server URL with `http://127.0.0.1:0`, keep operationIds ending in `NotImplemented`, and make every response description say fixture or candidate. This makes the schema useful for alignment while preventing accidental endpoint exposure.
[candidate] OpenAPI redline scan 13: if this fragment appears in generated client code, route registration, tests that hit a live server, or an API documentation page for users, the consuming lane has crossed the boundary. The only safe locations are research docs, fixture validators, and handoff notes that preserve `candidate_only=true` and `runtime_approval=not-approved`.
[tentative] OpenAPI repair 13: convert any tempting implementation detail into a non-routable example. For example, replace a real server URL with `http://127.0.0.1:0`, keep operationIds ending in `NotImplemented`, and make every response description say fixture or candidate. This makes the schema useful for alignment while preventing accidental endpoint exposure.
[candidate] OpenAPI redline scan 14: if this fragment appears in generated client code, route registration, tests that hit a live server, or an API documentation page for users, the consuming lane has crossed the boundary. The only safe locations are research docs, fixture validators, and handoff notes that preserve `candidate_only=true` and `runtime_approval=not-approved`.
[tentative] OpenAPI repair 14: convert any tempting implementation detail into a non-routable example. For example, replace a real server URL with `http://127.0.0.1:0`, keep operationIds ending in `NotImplemented`, and make every response description say fixture or candidate. This makes the schema useful for alignment while preventing accidental endpoint exposure.
