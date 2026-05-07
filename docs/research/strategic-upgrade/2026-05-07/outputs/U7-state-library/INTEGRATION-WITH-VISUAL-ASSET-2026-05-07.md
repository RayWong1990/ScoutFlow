---
title: INTEGRATION-WITH-VISUAL-ASSET-2026-05-07
status: candidate / not-authority / not-production-approval
claim_label: ≥95% candidate-spec confidence
request_date_label: 2026-05-07
generated_at_actual: 2026-05-06
write_enabled: false
boundary: spec-only; no apps/** mutation; no screenshots generated
---

# INTEGRATION-WITH-VISUAL-ASSET-2026-05-07

> 口径：本文件是 U7 candidate spec，不是 authority，不批准 runtime、frontend implementation、package install、browser automation、migration、vault true write 或 production 修改。文件名沿用用户 prompt 的 2026-05-07；实际生成环境日期为 2026-05-06。所有 “state” 都是可注册、可审计、可迁移的视觉状态，不等同于当前组件已经有完整可控 props。


## 1. Integration goal

U7 should become the bridge between state definitions and U4 visual assets. The current failure mode to avoid is simple: a screenshot file exists somewhere, but nobody can tell which panel/state it proves, whether the screenshot is stale, whether contrast was measured, or whether human review happened. The integration contract should make three things impossible:

1. treating a screenshot as visual approval;
2. approving a state without a screenshot asset id;
3. passing subjective 5-Gate gates without human review.

Because the exact U4 schema is not available in this environment, this file defines a compatibility layer rather than a destructive migration. It can be implemented either as nullable fields on `visual_asset` or as a join table. The join-table path is safer because it does not require immediate schema mutation.

## 2. Preferred join-table contract

```sql
CREATE TABLE IF NOT EXISTS visual_asset_state_link (
  link_id TEXT PRIMARY KEY,
  visual_asset_id TEXT NOT NULL,
  state_id TEXT NOT NULL REFERENCES state_library(state_id) ON DELETE CASCADE,
  relation TEXT NOT NULL DEFAULT 'screenshot_evidence' CHECK (relation IN (
    'screenshot_evidence','reference_inspiration','failed_state_evidence','audit_report_attachment'
  )),
  viewport TEXT NOT NULL,
  asset_sha256 TEXT NOT NULL,
  linked_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
  linked_by TEXT NOT NULL DEFAULT 'PF-V-or-local-dispatch',
  UNIQUE(visual_asset_id, state_id, viewport, relation)
);
```

If U4 already has `visual_asset(asset_id)` then `visual_asset_id` becomes FK. If not, the table can still validate state linkage and later backfill the FK. This is better than hard-coding screenshot paths into state_library only.

## 3. Optional visual_asset field extension

If the project chooses direct fields, add them conservatively:

```sql
ALTER TABLE visual_asset ADD COLUMN state_id TEXT NULL;
ALTER TABLE visual_asset ADD COLUMN five_gate_audit_passed INTEGER NOT NULL DEFAULT 0;
ALTER TABLE visual_asset ADD COLUMN five_gate_audit_id TEXT NULL;
ALTER TABLE visual_asset ADD COLUMN human_review_required INTEGER NOT NULL DEFAULT 1;
ALTER TABLE visual_asset ADD COLUMN audit_status TEXT NOT NULL DEFAULT 'not_run';
```

Field meanings:

| Field | Meaning | Do not use it to claim |
|---|---|---|
| `state_id` | Which U7 state this screenshot depicts | production component approval |
| `five_gate_audit_passed` | all required machine and human gates passed | runtime approval or authority promotion |
| `five_gate_audit_id` | pointer to `state_gate_audit` row | screenshot freshness unless hash matches |
| `human_review_required` | subjective gate required | automation failure by itself |
| `audit_status` | `not_run / machine_failed / human_pending / human_passed / human_failed` | final product readiness |

## 4. State machine alignment

The state transitions should be explicit:

```text
state_library row created
  -> screenshot deferred
  -> visual_asset created by PF-V or authorized screenshot dispatch
  -> visual_asset_state_link inserted
  -> machine audit run
  -> machine pass/fail/warn
  -> human queue opened for Gate 1 and Gate 5
  -> human pass/fail/revise
  -> state_library.five_gate_status updated
```

A screenshot can be valuable even if it fails. For example, an error state that shows text clipping is a failed-state evidence asset; it should remain linked for regression and audit. Do not delete failed screenshots just to keep dashboards green.

## 5. U5 dispatch ledger alignment

U5 dispatch ledger should record three separate events:

1. `state_registered`: U7 row created, no screenshot yet.
2. `screenshot_attached`: visual_asset linked with sha256 and viewport.
3. `gate_audit_completed`: machine + human result recorded.

Candidate event payload:

```json
{
  "event_kind": "screenshot_attached",
  "dispatch_id": "PF-V-P2-S04",
  "state_id": "url_bar.error.create_capture_error",
  "visual_asset_id": "va_20260507_001",
  "viewport": "desktop-1360x900",
  "sha256": "...",
  "boundary": "screenshot_only_not_visual_approval"
}
```

The ledger event should never say “approved” unless it is specifically the human/audit completion event and all required gates passed.

## 6. U6 visual-DAM alignment

U6 visual-DAM can treat state_library as a taxonomy source. DAM folders/tags should not invent another panel naming system. Recommended DAM facets:

- `panel_name`
- `state_name`
- `variant_name`
- `viewport`
- `phase`
- `gate_status`
- `human_review_status`
- `asset_kind=screenshot|audit_report|reference`

This lets DAM answer questions like: “show all mobile error-state screenshots that failed contrast” or “show all topic-card-vault full-state assets whose human weight review is pending”. DAM should keep assets; U7 keeps state truth; U5 keeps dispatch chronology.

## 7. Freshness and invalidation

Every screenshot link must carry source component path and preferably source commit/ref. If a component source changes, linked screenshots become `stale` unless a content-hash diff proves unaffected. Minimal invalidation rule:

```text
if source_component_path changed after screenshot_generated_at:
  evidence_status = 'stale'
  five_gate_status = 'blocked'
  require screenshot refresh or human stale-approval note
```

For main_nav, freshness is stricter because current nav is inferred. Any future explicit nav component should invalidate the adapter screenshot set.

## 8. Cross-cluster reuse

The same link model supports PF-V H5, future PPT/poster assets, DiloFlow visual experiments, and visual regression reports. A poster or PPT slide may link to a state as `reference_inspiration`, but only screenshot assets rendered from the component should use `screenshot_evidence`. This distinction matters because an attractive design reference is not proof that the H5 state is legible or implemented.

## 9. Acceptance criteria

- Every screenshot asset maps to exactly one `state_id` for screenshot evidence, or multiple only when explicitly marked composite.
- Every state with `five_gate_status='human_pass'` has at least one screenshot link and a completed audit row.
- Failed screenshots remain discoverable.
- U5 ledger records state registration, screenshot attachment and gate completion as separate events.
- U6 DAM uses U7 taxonomy rather than free-form names.
- No integration step writes apps/** or claims runtime unlock.


## 10. Composite and multi-asset handling

Some screenshots depict more than one state. FourPanelShell is the obvious case, but a future state-library browser screenshot might show navigation and a panel together. Do not force these into a single ambiguous state id. Use one primary link and additional secondary links:

```sql
CREATE TABLE IF NOT EXISTS visual_asset_state_composite_child (
  child_link_id TEXT PRIMARY KEY,
  visual_asset_id TEXT NOT NULL,
  parent_state_id TEXT NOT NULL REFERENCES state_library(state_id),
  child_state_id TEXT NOT NULL REFERENCES state_library(state_id),
  child_role TEXT NOT NULL DEFAULT 'visible_child_panel'
);
```

The primary state answers “what screenshot is this?” The child links answer “which registered states appear inside it?” Audit reports can then decide whether a shell failure is caused by the shell grid or by a child panel.

## 11. Rollback and stale evidence handling

If a screenshot was attached to the wrong state, do not delete historical evidence unless it contains sensitive material. Mark the link invalidated:

```sql
ALTER TABLE visual_asset_state_link ADD COLUMN link_status TEXT NOT NULL DEFAULT 'active';
ALTER TABLE visual_asset_state_link ADD COLUMN invalidation_reason TEXT NOT NULL DEFAULT '';
```

Valid statuses: `active`, `stale`, `wrong_state`, `hash_mismatch`, `sensitive_removed`, `superseded`. This preserves audit history and avoids rewriting the past. If sensitive material appears in a screenshot, remove or quarantine the asset according to project policy, then leave a redacted ledger event; do not keep sensitive screenshots in DAM.

## 12. Conflict resolution

Potential conflicts and resolutions:

| Conflict | Resolution |
|---|---|
| PF-V names screenshot `live_metadata` but U7 uses `live_meta` | alias in ingest; canonical row remains `live_meta` |
| U4 visual_asset already has another taxonomy | add join table rather than renaming U4 fields |
| DAM wants folder names by project | keep DAM folder names, add U7 facets/tags |
| Human reviewer fails a screenshot after machine pass | final status becomes `human_fail`; visual_asset remains failed evidence |
| Component changes after human pass | mark evidence stale and require refresh |
| One screenshot covers multiple viewports through responsive fullPage | split by viewport if possible; otherwise mark viewport `mixed` and do not use for pass |

## 13. Minimal API surface

A future implementation can expose a small read-only API for tools:

```http
GET /state-library/states?panel=url_bar&status=human_pending
GET /state-library/states/{state_id}
GET /state-library/states/{state_id}/assets
GET /state-library/human-review-queue
```

Write endpoints should remain local/dispatch-gated:

```http
POST /state-library/states/{state_id}/assets
POST /state-library/audit-runs
POST /state-library/human-review-queue/{queue_id}/verdict
```

Do not add these routes to production API without a separate architecture decision. They can be local tooling first.

## 14. Test cases for integration

1. Create `url_bar.full.manual_url_ready` without screenshot; expect `deferred_visual_evidence`.
2. Attach screenshot with sha256; expect link row and evidence status `screenshot_attached`.
3. Run machine audit that fails muted label contrast; expect `machine_failed` and no human pass allowed.
4. Run machine pass and open human queue; expect `human_pending`.
5. Human passes Gate 1 and fails Gate 5; expect final `human_fail`.
6. Component source changes; expect stale evidence and blocked audit status.
7. Composite shell screenshot links four child states; expect query by child returns shell asset.

## 15. Why join-table first is safer

Directly altering U4 may be faster, but U4 might already have its own state machine. A join table lets U7 deliver value without taking ownership of U4. If U4 later accepts U7 fields, the join table can be migrated. Until then, state-library can remain a reversible overlay. This matches the project’s current caution: research/spec surfaces should not become final authority or schema changes without a dispatch.


## 16. Example lifecycle record

A complete lifecycle for one screenshot should look like this:

```yaml
state_id: url_bar.error.create_capture_error
state_registered:
  at: 2026-05-07T00:00:00Z
  by: U7 seed
  evidence_status: deferred_visual_evidence
screenshot_attached:
  visual_asset_id: va_url_bar_error_desktop_001
  sha256: <digest>
  viewport: desktop-1360x900
  claim: screenshot_only_not_visual_approval
machine_audit:
  gate_2: pass
  gate_3: pass
  gate_4: fail
  reason: muted panel label ratio 4.11 below 4.5
human_queue:
  gate_1: not_open_until_machine_fix
  gate_5: not_open_until_machine_fix
final:
  status: machine_failed
```

This record is better than a screenshot filename because it tells the operator exactly why the state is not approved.

## 17. Human verdict data shape

Human review should be structured enough to audit later:

```json
{
  "queue_id": "hq_001",
  "state_id": "topic_card_vault.full.markdown_evidence_balance_full",
  "gate_name": "gate_5_visual_weight",
  "verdict": "revise",
  "reviewer": "RW",
  "reviewed_at": "2026-05-07T10:20:00+08:00",
  "review_note": "markdown block dominates; write_disabled badge is visible but too weak",
  "required_change": "increase boundary badge prominence or reduce markdown preview height"
}
```

A free-form comment in chat is not enough. Store the verdict where state and asset records can query it.

## 18. Security and privacy posture

Visual assets can leak local paths, URLs, or operator context. U7 should enforce:

- no credentials, cookies, tokens or QR/auth screenshots;
- no raw stdout/stderr embedded in images;
- local filesystem paths only if already safe and expected, otherwise redact or use fixture paths;
- no browser profile screenshots;
- no live platform media thumbnails unless separately approved.

This is especially important because visual-DAM makes assets easier to browse and share.


## 19. Query examples for U4/U7 operators

```sql
-- assets waiting for human review
SELECT l.state_id, q.gate_name, q.priority, vas.visual_asset_id
FROM human_visual_review_queue q
JOIN state_library l ON l.state_id = q.state_id
JOIN visual_asset_state_link vas ON vas.state_id = l.state_id
WHERE q.verdict = 'pending';

-- stale assets by component path
SELECT l.source_component_path, COUNT(*) AS stale_count
FROM state_library l
JOIN visual_asset_state_link vas ON vas.state_id = l.state_id
WHERE vas.link_status = 'stale'
GROUP BY l.source_component_path;

-- screenshots that passed machine gates but not human gates
SELECT l.state_id, a.audit_id, a.final_status
FROM state_library l
JOIN state_gate_audit a ON a.state_id = l.state_id
WHERE a.final_status = 'human_pending';
```

These queries should be in the operator README once U4/U7 are implemented.

## 20. Integration acceptance nuance

A visual_asset can be “good storage” and still “bad visual quality”. U4 should answer whether the asset exists, is hashed, classified and safe. U7 should answer whether it proves a state and passed gate review. Keeping those responsibilities separate prevents DAM from becoming an accidental quality authority.
