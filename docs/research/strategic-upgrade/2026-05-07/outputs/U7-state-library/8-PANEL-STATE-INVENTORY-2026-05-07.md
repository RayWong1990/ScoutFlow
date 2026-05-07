---
title: 8-PANEL-STATE-INVENTORY-2026-05-07
status: candidate / not-authority / not-production-approval
claim_label: ≥95% candidate-spec confidence
request_date_label: 2026-05-07
generated_at_actual: 2026-05-06
write_enabled: false
boundary: spec-only; no apps/** mutation; no screenshots generated
---

# 8-PANEL-STATE-INVENTORY-2026-05-07

> 口径：本文件是 U7 candidate spec，不是 authority，不批准 runtime、frontend implementation、package install、browser automation、migration、vault true write 或 production 修改。文件名沿用用户 prompt 的 2026-05-07；实际生成环境日期为 2026-05-06。所有 “state” 都是可注册、可审计、可迁移的视觉状态，不等同于当前组件已经有完整可控 props。

## Source snapshot used

| Surface | Path / source | Evidence read | Confidence |
|---|---|---|---|
| URL Bar | `apps/capture-station/src/features/url-bar/UrlBar.tsx` | `value`, `isSubmitting`, `errorMessage`, `isManualUrlReady`, sample suggestions, role=alert branch | high |
| Live Metadata | `apps/capture-station/src/features/live-metadata/LiveMetadataPanel.tsx` | static `metadataRows` for platform/probe/evidence/audio_transcript | medium-high; state props absent |
| Capture Scope | `apps/capture-station/src/features/capture-scope/CaptureScopePanel.tsx` | `scopeRows` with allowed / blocked / candidate and status colors | high |
| Trust Trace | `apps/capture-station/src/features/trust-trace/TrustTraceGraph.tsx` | `nodes` with ready / pending / blocked projection graph | high |
| Topic Card Preview | `apps/capture-station/src/features/topic-card-preview/TopicCardPreviewCandidate.tsx` + `topicCardLite.ts` | data model, review steps, metrics, counterNote | high |
| Topic Card Vault | `apps/capture-station/src/features/topic-card-vault/TopicCardVaultCandidate.tsx` + data file | write_disabled gate, evidence balance, markdown preview | high |
| Four Panel Shell | `apps/capture-station/src/layout/FourPanelShell.tsx` | `captureId`, `previewState` idle/loading/error/ready and reset flow | high |
| Main Navigation | `apps/capture-station/src/layout/panels.ts` + shell header | `PANEL_SPECS` lists four core panels; eight-panel nav is candidate state-library route | medium; explicit nav component not found |


## 1. Inventory purpose

This file is the concrete 8 panel × 6 state inventory. It deliberately distinguishes **observed source implementation** from **candidate visual state registration**. Some source components already expose state through local React state or typed props. Others are currently static fixtures and need harness-only adapters before screenshots can be generated. That is acceptable: U7 is the state registry and quality automation spec; PF-V P2 remains the image production lane.

## 2. Observed implementation summary

| Panel | Observed implementation | Current gap for state-library |
|---|---|---|
| URL Bar | local state supports value, submit pending, error branch and ready/blocked status | needs initial fixture injection in harness |
| Live Metadata | static rows show safe metadata placeholders and audio_transcript blocked | needs fixture prop or wrapper for loading/error/partial states |
| Capture Scope | static rows include allowed, blocked and candidate scope lanes | needs wrapper for empty/loading/error/amend states |
| Trust Trace | static nodes include ready, pending and blocked projection states | needs wrapper for alternative node arrays |
| Topic Card Preview | typed data prop supports mapped/reviewed, export posture and review steps | easiest to register with props_json |
| Topic Card Vault | typed data prop supports markdown preview/evidence/gate | easiest to register with props_json |
| Four Panel Shell | local `captureId` and `previewState` idle/loading/error/ready; reset on draft change | needs mock callbacks and perhaps harness-controlled initial state |
| Main Navigation | no dedicated component found; `PANEL_SPECS` has four core panels and shell header acts as nav context | candidate nav adapter must be explicit and marked inferred |

## 3. Canonical table

| state_id | panel label | state | variant | component/harness | props_json example | visual intent |
|---|---|---|---|---|---|---|
| `url_bar.empty.manual_url_required_empty` | `URL Bar` | `empty` | `manual_url_required_empty` | `UrlBar` | `{"value":"","isSubmitting":false,"errorMessage":null,"expected_status":"manual_url required","button_disabled":true}` | empty input, no canonical manual URL |
| `url_bar.loading.submit_in_flight` | `URL Bar` | `loading` | `submit_in_flight` | `UrlBar` | `{"value":"https://www.bilibili.com/video/BV1AB411c7mD","isSubmitting":true,"errorMessage":null,"expected_status":"submitting capture...","button_disabled":true}` | createCapture promise pending |
| `url_bar.partial.invalid_partial_url` | `URL Bar` | `partial` | `invalid_partial_url` | `UrlBar` | `{"value":"www.bilibili.com/video/BV_partial","isSubmitting":false,"errorMessage":null,"expected_status":"manual_url required","button_disabled":true}` | non-http draft URL blocks submit |
| `url_bar.full.manual_url_ready` | `URL Bar` | `full` | `manual_url_ready` | `UrlBar` | `{"value":"https://www.bilibili.com/video/BV1AB411c7mD","isSubmitting":false,"errorMessage":null,"expected_status":"manual_url ready","button_disabled":false}` | valid http(s) manual URL ready |
| `url_bar.error.create_capture_error` | `URL Bar` | `error` | `create_capture_error` | `UrlBar` | `{"value":"https://www.bilibili.com/video/BV_error","isSubmitting":false,"errorMessage":"Create capture failed.","expected_status":"manual_url ready","button_disabled":false}` | rejected createCapture renders role=alert |
| `url_bar.amend.draft_change_resets_preview` | `URL Bar` | `amend` | `draft_change_resets_preview` | `UrlBar` | `{"value":"https://www.bilibili.com/video/BV_amend","isSubmitting":false,"errorMessage":null,"onDraftChange":"resetPreviewDraft"}` | operator edits draft after preview exists |
| `live_meta.empty.no_capture_placeholder` | `Live Metadata` | `empty` | `no_capture_placeholder` | `LiveMetadataPanel` | `{"capture_id":null,"rows":[],"badge":"fixture only","safe_fields_visible":false}` | no metadata should not imply live probe |
| `live_meta.loading.metadata_probe_pending` | `Live Metadata` | `loading` | `metadata_probe_pending` | `LiveMetadataPanel` | `{"capture_id":"cap_001","probeState":"loading","rows":[{"label":"Platform","value":"pending"}]}` | metadata request pending |
| `live_meta.partial.title_duration_only` | `Live Metadata` | `partial` | `title_duration_only` | `LiveMetadataPanel` | `{"capture_id":"cap_001","rows":[{"label":"Platform","value":"bilibili"},{"label":"duration","value":"11:20"}],"missing":["page_count","selected_page"]}` | safe partial metadata only |
| `live_meta.full.safe_metadata_complete` | `Live Metadata` | `full` | `safe_metadata_complete` | `LiveMetadataPanel` | `{"capture_id":"cap_001","rows":[{"label":"Platform","value":"bilibili"},{"label":"Probe mode","value":"auth-present fixture"},{"label":"Evidence task","value":"T-P1A-011C"},{"label":"audio_transcript","value":"blocked"}]}` | all safe rows present |
| `live_meta.error.metadata_probe_error` | `Live Metadata` | `error` | `metadata_probe_error` | `LiveMetadataPanel` | `{"capture_id":"cap_001","probeState":"error","errorMessage":"metadata probe blocked"}` | blocked or failed metadata probe |
| `live_meta.amend.metadata_corrected_title` | `Live Metadata` | `amend` | `metadata_corrected_title` | `LiveMetadataPanel` | `{"capture_id":"cap_001","amendment":"title corrected after reviewer note","rows_version":"v2"}` | safe amend without runtime unlock |
| `capture_scope.empty.no_scope_rows` | `Capture Scope` | `empty` | `no_scope_rows` | `CaptureScopePanel` | `{"scopeRows":[],"operator_can_capture":false}` | scope not yet evaluated |
| `capture_scope.loading.scope_rules_loading` | `Capture Scope` | `loading` | `scope_rules_loading` | `CaptureScopePanel` | `{"scopeState":"loading","pendingRules":["manual_url","metadata_only"]}` | scope rules loading |
| `capture_scope.partial.allowed_only_visible` | `Capture Scope` | `partial` | `allowed_only_visible` | `CaptureScopePanel` | `{"scopeRows":[{"label":"manual_url / metadata_only","status":"allowed"}],"blockedCollapsed":true}` | allowed path visible but blocked lanes summarized |
| `capture_scope.full.allowed_blocked_candidate_all` | `Capture Scope` | `full` | `allowed_blocked_candidate_all` | `CaptureScopePanel` | `{"scopeRows":[{"label":"manual_url / metadata_only","status":"allowed"},{"label":"recommendation / keyword / RAW gap","status":"blocked"},{"label":"audio_transcript","status":"blocked"},{"label":"DB vNext / migration dry-run","status":"candidate"}]}` | full current scope truth |
| `capture_scope.error.scope_contradiction` | `Capture Scope` | `error` | `scope_contradiction` | `CaptureScopePanel` | `{"scopeError":"source_kind recommendation attempted direct capture","blocked_reason":"manual_url_only"}` | scope rule contradiction |
| `capture_scope.amend.rule_note_amended` | `Capture Scope` | `amend` | `rule_note_amended` | `CaptureScopePanel` | `{"scopeRows_version":"v2","amendedRow":"DB vNext / migration dry-run","note":"requires separate dispatch"}` | wording correction |
| `trust_trace.empty.no_trace_nodes` | `Trust Trace` | `empty` | `no_trace_nodes` | `TrustTraceGraph` | `{"nodes":[],"projection_only":true}` | no trace yet |
| `trust_trace.loading.receipt_pending_chain` | `Trust Trace` | `loading` | `receipt_pending_chain` | `TrustTraceGraph` | `{"nodes":[{"id":"capture","state":"pending"},{"id":"metadata-job","state":"pending"}]}` | receipt graph pending |
| `trust_trace.partial.capture_metadata_ready` | `Trust Trace` | `partial` | `capture_metadata_ready` | `TrustTraceGraph` | `{"nodes":[{"id":"capture","state":"ready"},{"id":"metadata-job","state":"ready"},{"id":"receipt-ledger","state":"pending"}]}` | core trace ready, ledger pending |
| `trust_trace.full.ready_pending_blocked_visible` | `Trust Trace` | `full` | `ready_pending_blocked_visible` | `TrustTraceGraph` | `{"nodes":[{"id":"capture","state":"ready"},{"id":"metadata-job","state":"ready"},{"id":"probe-evidence","state":"ready"},{"id":"receipt-ledger","state":"pending"},{"id":"media-audio","state":"blocked"}]}` | ready + pending + blocked all explicit |
| `trust_trace.error.trace_mismatch_error` | `Trust Trace` | `error` | `trace_mismatch_error` | `TrustTraceGraph` | `{"traceError":"probe platform_item_id mismatch","nodes":[{"id":"capture","state":"ready"},{"id":"probe-evidence","state":"blocked"}]}` | provenance mismatch blocks trust trace |
| `trust_trace.amend.receipt_note_amended` | `Trust Trace` | `amend` | `receipt_note_amended` | `TrustTraceGraph` | `{"amendedNode":"receipt-ledger","state":"pending","reviewer_note":"awaiting visual_asset link"}` | manual audit note appended |
| `topic_card_preview.empty.no_preview_card` | `Topic Card Preview` | `empty` | `no_preview_card` | `TopicCardPreviewCandidate` | `{"data":null,"reviewState":null,"exportPosture":null}` | no preview transform output |
| `topic_card_preview.loading.transform_pending` | `Topic Card Preview` | `loading` | `transform_pending` | `TopicCardPreviewCandidate` | `{"transformState":"loading","captureId":"cap_001"}` | preview card transform pending |
| `topic_card_preview.partial.mapped_missing_frontmatter` | `Topic Card Preview` | `partial` | `mapped_missing_frontmatter` | `TopicCardPreviewCandidate` | `{"reviewState":"mapped","exportPosture":"local_only","frontmatterStatus":"pending","metrics":["source_kind","capture_mode"]}` | mapped but missing/partial frontmatter |
| `topic_card_preview.full.reviewed_handoff_candidate` | `Topic Card Preview` | `full` | `reviewed_handoff_candidate` | `TopicCardPreviewCandidate` | `{"reviewState":"reviewed","exportPosture":"handoff_candidate","reviewSteps":[{"label":"preview generated","state":"ready"},{"label":"topic-card review","state":"ready"},{"label":"human usefulness verdict","state":"needs_review"}]}` | ready for handoff, still needs human verdict |
| `topic_card_preview.error.transform_warning_error` | `Topic Card Preview` | `error` | `transform_warning_error` | `TopicCardPreviewCandidate` | `{"reviewState":"mapped","warnings":["title missing","target_path unsafe"],"counterNote":"preview_only=true"}` | transform warnings shown as visible counter-evidence |
| `topic_card_preview.amend.review_step_amended` | `Topic Card Preview` | `amend` | `review_step_amended` | `TopicCardPreviewCandidate` | `{"reviewState":"reviewed","amendment":"human usefulness verdict returned to needs_review"}` | reviewer changes state after card edit |
| `topic_card_vault.empty.no_markdown_candidate` | `Topic Card Vault` | `empty` | `no_markdown_candidate` | `TopicCardVaultCandidate` | `{"data":null,"gate":"write_disabled","markdownPreview":""}` | no vault markdown candidate |
| `topic_card_vault.loading.markdown_render_pending` | `Topic Card Vault` | `loading` | `markdown_render_pending` | `TopicCardVaultCandidate` | `{"renderState":"loading","gate":"write_disabled"}` | markdown companion rendering |
| `topic_card_vault.partial.markdown_without_verdict` | `Topic Card Vault` | `partial` | `markdown_without_verdict` | `TopicCardVaultCandidate` | `{"gate":"write_disabled","targetPath":"/tmp/scoutflow-vault/00-Inbox/topic-card-cap_placeholder.md","evidence":[{"label":"capture truth","stance":"support"}]}` | markdown present, human verdict missing |
| `topic_card_vault.full.markdown_evidence_balance_full` | `Topic Card Vault` | `full` | `markdown_evidence_balance_full` | `TopicCardVaultCandidate` | `{"gate":"write_disabled","exportPosture":"handoff_candidate","evidence":["support","process","counter"],"markdownPreview":"# ScoutFlow topic-card candidate"}` | all evidence lanes visible; still no commit |
| `topic_card_vault.error.unsafe_target_path_error` | `Topic Card Vault` | `error` | `unsafe_target_path_error` | `TopicCardVaultCandidate` | `{"gate":"write_disabled","errorMessage":"target_path outside 00-Inbox","targetPath":"../bad.md"}` | path policy violation |
| `topic_card_vault.amend.frontmatter_amended` | `Topic Card Vault` | `amend` | `frontmatter_amended` | `TopicCardVaultCandidate` | `{"gate":"write_disabled","amendment":"frontmatter status corrected","markdownPreviewVersion":"v2"}` | markdown preview amended |
| `four_panel_shell.empty.initial_idle_shell` | `Four Panel Shell` | `empty` | `initial_idle_shell` | `FourPanelShell` | `{"captureId":null,"previewState":"idle","preview":null,"previewError":null}` | initial shell with URL bar and idle preview |
| `four_panel_shell.loading.preview_loading_after_capture` | `Four Panel Shell` | `loading` | `preview_loading_after_capture` | `FourPanelShell` | `{"captureId":"cap_001","previewState":"loading","preview":null,"previewError":null}` | loadPreview pending after capture created |
| `four_panel_shell.partial.core_panels_ready_preview_pending` | `Four Panel Shell` | `partial` | `core_panels_ready_preview_pending` | `FourPanelShell` | `{"captureId":"cap_001","previewState":"loading","corePanels":["url_bar","live_meta","capture_scope","trust_trace"]}` | core layout ready while preview pending |
| `four_panel_shell.full.preview_ready_shell` | `Four Panel Shell` | `full` | `preview_ready_shell` | `FourPanelShell` | `{"captureId":"cap_001","previewState":"ready","preview":{"capture_id":"cap_001","target_path":"/tmp/scoutflow-vault/00-Inbox/a.md"},"previewError":null}` | preview ready and panels visible |
| `four_panel_shell.error.preview_error_shell` | `Four Panel Shell` | `error` | `preview_error_shell` | `FourPanelShell` | `{"captureId":"cap_001","previewState":"error","preview":null,"previewError":{"code":"preview_error","message":"Preview request failed."}}` | preview route error |
| `four_panel_shell.amend.draft_change_reset_shell` | `Four Panel Shell` | `amend` | `draft_change_reset_shell` | `FourPanelShell` | `{"captureId":null,"previewState":"idle","resetReason":"UrlBar onDraftChange"}` | draft amended, preview reset |
| `main_nav.empty.no_active_route` | `Main Navigation` | `empty` | `no_active_route` | `RoutePanelNav(candidate)` | `{"activePanel":null,"items":[],"routeState":"idle"}` | no navigation selection yet |
| `main_nav.loading.route_resolving` | `Main Navigation` | `loading` | `route_resolving` | `RoutePanelNav(candidate)` | `{"routeState":"loading","activePanel":"url_bar","items":["url_bar"]}` | routing item resolving |
| `main_nav.partial.core_four_panel_nav` | `Main Navigation` | `partial` | `core_four_panel_nav` | `RoutePanelNav(candidate)` | `{"activePanel":"url_bar","items":["url_bar","live_meta","capture_scope","trust_trace"],"source":"PANEL_SPECS"}` | panels.ts currently lists four core panel specs |
| `main_nav.full.eight_panel_nav_full` | `Main Navigation` | `full` | `eight_panel_nav_full` | `RoutePanelNav(candidate)` | `{"activePanel":"topic_card_preview","items":["url_bar","live_meta","capture_scope","trust_trace","topic_card_preview","topic_card_vault","four_panel_shell","main_nav"],"source":"state_library"}` | state-library nav can show all eight registered panels |
| `main_nav.error.unknown_route_error` | `Main Navigation` | `error` | `unknown_route_error` | `RoutePanelNav(candidate)` | `{"routeState":"error","requestedPanel":"bad_panel","fallbackPanel":"url_bar"}` | unknown panel route fallback |
| `main_nav.amend.nav_order_label_amended` | `Main Navigation` | `amend` | `nav_order_label_amended` | `RoutePanelNav(candidate)` | `{"routeState":"ready","amendment":"renamed live_meta label and reordered topic card lanes"}` | nav label/order amended |

## 4. Panel-by-panel notes

### URL Bar

The URL Bar deserves more than six variants in PF-V because it has user-input nuance: blank value, non-http value, valid URL, two sample chips, pending submit, failed submit, successful submit, and amend/reset. The six canonical states are therefore a **minimum index**, not the full screenshot backlog. S04 can keep its ten-state set; U7 maps those ten into canonical state families plus variants such as `long_url`, `sample_chip_active`, `submit_disabled`, and `api_reject_long_message`. The important design point is that the button must not imply recommendation/keyword capture. The status text must remain visible: `manual_url ready`, `manual_url required`, or `submitting capture...`.

### Live Metadata

The current panel is safe because it says fixture-only and explicitly says audio_transcript is blocked. The state-library should preserve that safety when adding richer states. A loading state should not say “BBDown running” unless a separate runtime gate proves it. A full state may show title, duration, page count and selected page only if the evidence source is recorded. An error state should be explicit: blocked, missing auth, or probe failure. An amend state should show a corrected metadata field without claiming new runtime.

### Capture Scope

This panel is the visual redline surface. In the full state, allowed, blocked and candidate rows must all be visible together. Hiding blocked lanes produces a product lie: the operator may infer that future runtime is absent rather than intentionally blocked. Error state should be used for attempts to create capture from recommendation, keyword, RAW gap, audio_transcript, browser automation, or media download. Amend state should be common because scope wording evolves; amendments must never silently unlock state words.

### Trust Trace

Trust Trace is projection-only. It can show ready/pending/blocked but cannot create authority. The full state should include at least one blocked node to preserve boundary visibility. Error state is especially important for provenance mismatch. For example, URL-derived BV id and probe platform id mismatch should be visible as trust failure rather than a quiet warning.

### Topic Card Preview

The preview data model is already friendly to state-library because it accepts a data prop. Partial/full/error/amend can be generated by changing `reviewState`, `exportPosture`, `metrics`, `reviewSteps`, `counterNote`, and frontmatter status. The preview’s footer text is a boundary asset: it says preview exposes reviewable structure only and does not call topic-card APIs or change the shell. Keep that line in screenshots.

### Topic Card Vault

Vault candidate is not a vault commit. The full state must still show `write_disabled`; otherwise visual weight may imply an approved commit lane. Partial state should show markdown without human verdict. Error state should focus on path/frontmatter safety, not renderer aesthetics alone. The markdown preview block has high density; Gate 5 should prioritize it for human visual-weight review.

### Four Panel Shell

FourPanelShell is the composite state carrier. It already has idle/loading/error/ready preview states, and the amend state occurs when UrlBar draft changes and resets preview. In state-library, shell states should not be used to hide failures in child panels: a shell screenshot must declare which child states it is composing. For example `four_panel_shell.full.preview_ready_shell` should carry child references: `url_bar.full`, `vault_preview.full`, `live_meta.full`, `capture_scope.full`, `trust_trace.full`.

### Main Navigation

No dedicated main navigation component was found in the available evidence. The closest source is `PANEL_SPECS`, currently listing four core panels, plus the shell header. U7 should not pretend an eight-item nav exists in production. Instead, register `main_nav` as a candidate adapter that renders state-library routes. Its purpose is not production navigation; its purpose is a browsable index for state review. When a future nav component lands, the route can be switched while preserving existing state ids.

## 5. Variant backlog beyond 48

PF-V’s S04/S05/S06-S09 variants can be registered as `variant_name` values under the canonical state. Suggested variants:

- `long_title`, `long_url`, `long_target_path`, `long_error_message`
- `tags_overflow`, `markdown_overflow`, `metrics_three_columns`, `evidence_many_rows`
- `mobile_single_column`, `tablet_two_column`, `desktop_shell`
- `blocked_lane_dominant`, `candidate_badge_visible`, `human_pending_badge`
- `contrast_muted_label`, `error_alert_dense`, `review_steps_overflow`

Do not multiply canonical states just because a viewport changes. Use `viewport` and `variant_name` together. Canonical state answers **what condition is represented**; viewport/variant answer **how that condition is stressed**.


## 6. Coverage interpretation

The 48 rows are the semantic floor. They do not mean PF-V should stop at 48 screenshots. In practice, URL Bar alone can justify ten or more screenshots because input length, sample chip behavior, disabled button styling and error text length all affect visual quality. The state-library solves this by making `state_name` canonical and `variant_name` expandable. A PF-V image called `url_bar_error_long_api_message_mobile` should not create a new canonical state; it should register as `panel=url_bar`, `state=error`, `variant=long_api_message`, `viewport=mobile-390x844`.

## 7. Evidence confidence tiers

Use the following confidence tiers when registering rows:

| Tier | Meaning | Example |
|---|---|---|
| `production_rendered` | current production component can render the state through native props or real interactions | TopicCard Preview full via `data` prop |
| `interaction_rendered` | current component can render after user-event or fake API callback | UrlBar error via rejected `createCapture` |
| `adapter_rendered` | state requires a harness wrapper because component is static | Live Metadata loading |
| `inferred_route` | no dedicated component found; route is candidate adapter | Main Navigation full eight-panel nav |

This tier should live in `props_json` or a future `fixture_control` column. It helps reviewers understand whether a screenshot proves production behavior or only state intent.

## 8. PF-V variant examples by panel

| Panel | Variant candidates |
|---|---|
| URL Bar | `long_url`, `empty_focus`, `sample_chip_click`, `api_error_long`, `loading_disabled_button` |
| Live Metadata | `long_title`, `missing_duration`, `auth_present_fixture`, `probe_blocked`, `audio_transcript_blocked_visible` |
| Capture Scope | `many_blocked_lanes`, `candidate_db_vnext`, `manual_url_only`, `scope_contradiction`, `blocked_lane_collapsed_risk` |
| Trust Trace | `five_nodes`, `long_node_title`, `provenance_mismatch`, `receipt_pending`, `media_audio_blocked` |
| Topic Card Preview | `long_hypothesis`, `metrics_overflow`, `review_steps_dense`, `counter_note_long`, `frontmatter_pending` |
| Topic Card Vault | `markdown_long`, `target_path_long`, `unsafe_path_error`, `evidence_many_rows`, `write_disabled_badge` |
| Four Panel Shell | `desktop_three_columns`, `tablet_wrap`, `mobile_overflow`, `preview_error`, `draft_reset` |
| Main Navigation | `four_core_only`, `eight_full`, `unknown_route`, `active_topic_card`, `label_amend` |

## 9. Required props_json discipline

The props examples in this file are intentionally concise. Implementation rows should include enough fixture data to reproduce the state without reading external notes. Required fields:

- `fixture_control`: `production_rendered`, `interaction_rendered`, `adapter_rendered`, or `inferred_route`;
- `state_intent`: one-sentence reason this visual state exists;
- `boundary_copy_required`: list of phrases that must remain visible, such as `write_disabled` or `manual_url_only`;
- `expected_primary_status`: the status badge/text expected in the screenshot;
- `negative_assertions`: claims the screen must not imply, such as `no_vault_commit` or `no_audio_transcript_runtime`.

Example:

```json
{
  "fixture_control": "interaction_rendered",
  "state_intent": "createCapture rejects and UrlBar shows role=alert",
  "boundary_copy_required": ["manual_url ready"],
  "expected_primary_status": "error alert visible",
  "negative_assertions": ["no recommendation capture", "no runtime unlock"]
}
```

## 10. Inventory acceptance

This inventory should be considered accepted when all 48 canonical rows exist and every row has a props fixture with at least one negative assertion. The negative assertion matters because ScoutFlow’s UI problem is not merely missing states; it is also accidental overclaim. A state screenshot can be visually polished and still fail if it implies an unapproved path.


## 11. State total verification

The inventory total is:

```text
8 panels × 6 canonical states = 48 state rows
```

Panels: `url_bar`, `live_meta`, `capture_scope`, `trust_trace`, `topic_card_preview`, `topic_card_vault`, `four_panel_shell`, `main_nav`.

States: `empty`, `loading`, `partial`, `full`, `error`, `amend`.

The average state count per panel is exactly 6. Custom variants do not change this average; they increase screenshot evidence count.

## 12. Required negative examples

For each panel, at least one screenshot should intentionally show a blocked or not-ready condition. A library containing only polished full states is misleading. Minimum negative coverage:

- URL Bar: invalid partial URL and createCapture error.
- Live Metadata: metadata probe blocked.
- Capture Scope: forbidden source kind or audio_transcript blocked.
- Trust Trace: provenance mismatch or media-audio blocked.
- Topic Card Preview: missing human usefulness verdict.
- Topic Card Vault: unsafe target path or write_disabled badge.
- Four Panel Shell: preview error state.
- Main Navigation: unknown route fallback.

This negative coverage reinforces ScoutFlow’s boundary-first product posture.
