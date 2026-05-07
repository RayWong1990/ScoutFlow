---
title: MODULE-state-library-spec-2026-05-07
status: candidate / not-authority / not-production-approval
claim_label: ≥95% candidate-spec confidence
request_date_label: 2026-05-07
generated_at_actual: 2026-05-06
write_enabled: false
boundary: spec-only; no apps/** mutation; no screenshots generated
---

# MODULE-state-library-spec-2026-05-07

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


## 1. Mission framing

ScoutFlow capture-station 的视觉空间不是 “一个页面”，而是八个 surface 在六类视觉状态中的组合：`empty / loading / partial / full / error / amend`。U7 的重点不是生成新 UI，也不是替 PF-V 直接补图，而是把 PF-V 正在产出的状态图、未来截图和 5-Gate 审计结果注册成可查询、可复用、可追踪的 state-library。这样后续任何人问 “URL Bar 的 loading state 有没有截图证据、contrast 有没有测、human gate 谁审过” 时，不需要翻聊天记录或手动搜文件夹，可以直接按 `state_id` 查询。

当前 repo 已经有多个真实状态入口，但它们分散在组件内部：UrlBar 使用 React state 管理输入、提交中和错误；FourPanelShell 管理 `previewState`；TrustTraceGraph 和 CaptureScopePanel 用数组常量表达 blocked/ready/candidate；TopicCard Preview/Vault 已经有 data model。问题是这些状态尚未被注册为统一库，也没有与 visual_asset / screenshot / human-review queue 绑定。State-library 的正确抽象应当处在 “组件之外、证据之上”：它记录状态定义、props fixture、组件 route、截图 FK、5-Gate 状态、phase 和 claim label；它不直接声明 production component 必须怎么实现。

## 2. Core principles

1. **Candidate-only**：state-library 是 registration 和 audit surface，不改变 apps/**，不替代 `docs/current.md` 或 task ledger。
2. **State first, screenshot later**：先登记 48 个 canonical state，截图由 PF-V P2 或后续授权 dispatch 产出后再 attach。
3. **Props are evidence fixtures**：`props_json` 是可复现 fixture，不是强制 production API；现有组件还没有导出全部控制点时，允许使用 harness adapter。
4. **Human gate cannot be bypassed**：Gate 1 visual hierarchy 与 Gate 5 visual weight 只能有 machine-assist score，最终必须排队给人审。
5. **A11Y requires measurement**：contrast 不能只写 “符合 WCAG”；必须记录 foreground/background、ratio、阈值和 pass/fail。
6. **No runtime unlock by screenshot**：截图 evidence 只证明视觉状态，不证明 BBDown live、ffmpeg、ASR、browser automation、vault commit 或 migration 解锁。

## 3. SQLite schema candidate

下面 DDL 以 SQLite 为主。它刻意不假设 U4 `visual_asset` 已经存在于当前数据库；如果 U4 表已存在，则 `screenshot_asset_id` FK 激活；如果尚未存在，则先作为 nullable text + deferred validation。

```sql
PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS state_library (
  state_id TEXT PRIMARY KEY,
  panel_name TEXT NOT NULL CHECK (panel_name IN (
    'url_bar','live_meta','capture_scope','trust_trace',
    'topic_card_preview','topic_card_vault','four_panel_shell','main_nav'
  )),
  state_name TEXT NOT NULL CHECK (state_name IN (
    'empty','loading','partial','full','error','amend','custom'
  )),
  variant_name TEXT NOT NULL DEFAULT 'base',
  component_route TEXT NOT NULL,
  component_export TEXT NOT NULL,
  source_component_path TEXT NOT NULL,
  props_json TEXT NOT NULL CHECK (json_valid(props_json)),
  viewport TEXT NOT NULL DEFAULT 'desktop-1360x900',
  screenshot_asset_id TEXT NULL,
  screenshot_path TEXT NULL,
  screenshot_sha256 TEXT NULL,
  five_gate_status TEXT NOT NULL DEFAULT 'not_run' CHECK (five_gate_status IN (
    'not_run','auto_pass','auto_fail','human_pending','human_pass','human_fail','blocked'
  )),
  evidence_status TEXT NOT NULL DEFAULT 'deferred_visual_evidence' CHECK (evidence_status IN (
    'deferred_visual_evidence','screenshot_attached','stale','invalidated'
  )),
  phase TEXT NOT NULL DEFAULT 'PF-V-P2',
  claim_label TEXT NOT NULL DEFAULT 'candidate_not_authority',
  created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
  notes TEXT NOT NULL DEFAULT '',
  UNIQUE(panel_name, state_name, variant_name, viewport)
);

CREATE INDEX IF NOT EXISTS idx_state_library_panel_state
  ON state_library(panel_name, state_name);
CREATE INDEX IF NOT EXISTS idx_state_library_gate
  ON state_library(five_gate_status, evidence_status);

CREATE TABLE IF NOT EXISTS state_screenshot_evidence (
  evidence_id TEXT PRIMARY KEY,
  state_id TEXT NOT NULL REFERENCES state_library(state_id) ON DELETE CASCADE,
  visual_asset_id TEXT NULL,
  screenshot_path TEXT NOT NULL,
  screenshot_sha256 TEXT NOT NULL,
  viewport TEXT NOT NULL,
  generated_by TEXT NOT NULL,
  generated_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
  source_dispatch TEXT NULL,
  pfv_step TEXT NULL,
  evidence_claim TEXT NOT NULL DEFAULT 'screenshot_only_not_visual_approval'
);

CREATE TABLE IF NOT EXISTS state_gate_audit (
  audit_id TEXT PRIMARY KEY,
  state_id TEXT NOT NULL REFERENCES state_library(state_id) ON DELETE CASCADE,
  audit_run_id TEXT NOT NULL,
  gate_1_hierarchy_status TEXT NOT NULL DEFAULT 'human_pending',
  gate_2_spacing_status TEXT NOT NULL DEFAULT 'not_run',
  gate_3_occlusion_status TEXT NOT NULL DEFAULT 'not_run',
  gate_4_typography_status TEXT NOT NULL DEFAULT 'not_run',
  gate_5_weight_status TEXT NOT NULL DEFAULT 'human_pending',
  machine_report_json TEXT NOT NULL CHECK (json_valid(machine_report_json)),
  human_reviewer TEXT NULL,
  human_reviewed_at TEXT NULL,
  final_status TEXT NOT NULL DEFAULT 'human_pending',
  notes TEXT NOT NULL DEFAULT ''
);
```

## 4. Canonical 48-state matrix

| state_id | panel | state | variant | route/export | intent |
|---|---|---|---|---|---|
| `url_bar.empty.manual_url_required_empty` | `url_bar` | `empty` | `manual_url_required_empty` | `UrlBar` | empty input, no canonical manual URL |
| `url_bar.loading.submit_in_flight` | `url_bar` | `loading` | `submit_in_flight` | `UrlBar` | createCapture promise pending |
| `url_bar.partial.invalid_partial_url` | `url_bar` | `partial` | `invalid_partial_url` | `UrlBar` | non-http draft URL blocks submit |
| `url_bar.full.manual_url_ready` | `url_bar` | `full` | `manual_url_ready` | `UrlBar` | valid http(s) manual URL ready |
| `url_bar.error.create_capture_error` | `url_bar` | `error` | `create_capture_error` | `UrlBar` | rejected createCapture renders role=alert |
| `url_bar.amend.draft_change_resets_preview` | `url_bar` | `amend` | `draft_change_resets_preview` | `UrlBar` | operator edits draft after preview exists |
| `live_meta.empty.no_capture_placeholder` | `live_meta` | `empty` | `no_capture_placeholder` | `LiveMetadataPanel` | no metadata should not imply live probe |
| `live_meta.loading.metadata_probe_pending` | `live_meta` | `loading` | `metadata_probe_pending` | `LiveMetadataPanel` | metadata request pending |
| `live_meta.partial.title_duration_only` | `live_meta` | `partial` | `title_duration_only` | `LiveMetadataPanel` | safe partial metadata only |
| `live_meta.full.safe_metadata_complete` | `live_meta` | `full` | `safe_metadata_complete` | `LiveMetadataPanel` | all safe rows present |
| `live_meta.error.metadata_probe_error` | `live_meta` | `error` | `metadata_probe_error` | `LiveMetadataPanel` | blocked or failed metadata probe |
| `live_meta.amend.metadata_corrected_title` | `live_meta` | `amend` | `metadata_corrected_title` | `LiveMetadataPanel` | safe amend without runtime unlock |
| `capture_scope.empty.no_scope_rows` | `capture_scope` | `empty` | `no_scope_rows` | `CaptureScopePanel` | scope not yet evaluated |
| `capture_scope.loading.scope_rules_loading` | `capture_scope` | `loading` | `scope_rules_loading` | `CaptureScopePanel` | scope rules loading |
| `capture_scope.partial.allowed_only_visible` | `capture_scope` | `partial` | `allowed_only_visible` | `CaptureScopePanel` | allowed path visible but blocked lanes summarized |
| `capture_scope.full.allowed_blocked_candidate_all` | `capture_scope` | `full` | `allowed_blocked_candidate_all` | `CaptureScopePanel` | full current scope truth |
| `capture_scope.error.scope_contradiction` | `capture_scope` | `error` | `scope_contradiction` | `CaptureScopePanel` | scope rule contradiction |
| `capture_scope.amend.rule_note_amended` | `capture_scope` | `amend` | `rule_note_amended` | `CaptureScopePanel` | wording correction |
| `trust_trace.empty.no_trace_nodes` | `trust_trace` | `empty` | `no_trace_nodes` | `TrustTraceGraph` | no trace yet |
| `trust_trace.loading.receipt_pending_chain` | `trust_trace` | `loading` | `receipt_pending_chain` | `TrustTraceGraph` | receipt graph pending |
| `trust_trace.partial.capture_metadata_ready` | `trust_trace` | `partial` | `capture_metadata_ready` | `TrustTraceGraph` | core trace ready, ledger pending |
| `trust_trace.full.ready_pending_blocked_visible` | `trust_trace` | `full` | `ready_pending_blocked_visible` | `TrustTraceGraph` | ready + pending + blocked all explicit |
| `trust_trace.error.trace_mismatch_error` | `trust_trace` | `error` | `trace_mismatch_error` | `TrustTraceGraph` | provenance mismatch blocks trust trace |
| `trust_trace.amend.receipt_note_amended` | `trust_trace` | `amend` | `receipt_note_amended` | `TrustTraceGraph` | manual audit note appended |
| `topic_card_preview.empty.no_preview_card` | `topic_card_preview` | `empty` | `no_preview_card` | `TopicCardPreviewCandidate` | no preview transform output |
| `topic_card_preview.loading.transform_pending` | `topic_card_preview` | `loading` | `transform_pending` | `TopicCardPreviewCandidate` | preview card transform pending |
| `topic_card_preview.partial.mapped_missing_frontmatter` | `topic_card_preview` | `partial` | `mapped_missing_frontmatter` | `TopicCardPreviewCandidate` | mapped but missing/partial frontmatter |
| `topic_card_preview.full.reviewed_handoff_candidate` | `topic_card_preview` | `full` | `reviewed_handoff_candidate` | `TopicCardPreviewCandidate` | ready for handoff, still needs human verdict |
| `topic_card_preview.error.transform_warning_error` | `topic_card_preview` | `error` | `transform_warning_error` | `TopicCardPreviewCandidate` | transform warnings shown as visible counter-evidence |
| `topic_card_preview.amend.review_step_amended` | `topic_card_preview` | `amend` | `review_step_amended` | `TopicCardPreviewCandidate` | reviewer changes state after card edit |
| `topic_card_vault.empty.no_markdown_candidate` | `topic_card_vault` | `empty` | `no_markdown_candidate` | `TopicCardVaultCandidate` | no vault markdown candidate |
| `topic_card_vault.loading.markdown_render_pending` | `topic_card_vault` | `loading` | `markdown_render_pending` | `TopicCardVaultCandidate` | markdown companion rendering |
| `topic_card_vault.partial.markdown_without_verdict` | `topic_card_vault` | `partial` | `markdown_without_verdict` | `TopicCardVaultCandidate` | markdown present, human verdict missing |
| `topic_card_vault.full.markdown_evidence_balance_full` | `topic_card_vault` | `full` | `markdown_evidence_balance_full` | `TopicCardVaultCandidate` | all evidence lanes visible; still no commit |
| `topic_card_vault.error.unsafe_target_path_error` | `topic_card_vault` | `error` | `unsafe_target_path_error` | `TopicCardVaultCandidate` | path policy violation |
| `topic_card_vault.amend.frontmatter_amended` | `topic_card_vault` | `amend` | `frontmatter_amended` | `TopicCardVaultCandidate` | markdown preview amended |
| `four_panel_shell.empty.initial_idle_shell` | `four_panel_shell` | `empty` | `initial_idle_shell` | `FourPanelShell` | initial shell with URL bar and idle preview |
| `four_panel_shell.loading.preview_loading_after_capture` | `four_panel_shell` | `loading` | `preview_loading_after_capture` | `FourPanelShell` | loadPreview pending after capture created |
| `four_panel_shell.partial.core_panels_ready_preview_pending` | `four_panel_shell` | `partial` | `core_panels_ready_preview_pending` | `FourPanelShell` | core layout ready while preview pending |
| `four_panel_shell.full.preview_ready_shell` | `four_panel_shell` | `full` | `preview_ready_shell` | `FourPanelShell` | preview ready and panels visible |
| `four_panel_shell.error.preview_error_shell` | `four_panel_shell` | `error` | `preview_error_shell` | `FourPanelShell` | preview route error |
| `four_panel_shell.amend.draft_change_reset_shell` | `four_panel_shell` | `amend` | `draft_change_reset_shell` | `FourPanelShell` | draft amended, preview reset |
| `main_nav.empty.no_active_route` | `main_nav` | `empty` | `no_active_route` | `RoutePanelNav(candidate)` | no navigation selection yet |
| `main_nav.loading.route_resolving` | `main_nav` | `loading` | `route_resolving` | `RoutePanelNav(candidate)` | routing item resolving |
| `main_nav.partial.core_four_panel_nav` | `main_nav` | `partial` | `core_four_panel_nav` | `RoutePanelNav(candidate)` | panels.ts currently lists four core panel specs |
| `main_nav.full.eight_panel_nav_full` | `main_nav` | `full` | `eight_panel_nav_full` | `RoutePanelNav(candidate)` | state-library nav can show all eight registered panels |
| `main_nav.error.unknown_route_error` | `main_nav` | `error` | `unknown_route_error` | `RoutePanelNav(candidate)` | unknown panel route fallback |
| `main_nav.amend.nav_order_label_amended` | `main_nav` | `amend` | `nav_order_label_amended` | `RoutePanelNav(candidate)` | nav label/order amended |

## 5. State to component routing

The state-library browser should resolve one state in four steps:

```text
state_id -> state_library row -> component_route/component_export -> harness props_json -> render in isolated frame
```

Candidate route map:

```ts
export const STATE_COMPONENT_ROUTES = {
  url_bar: { path: '../features/url-bar/UrlBar.tsx', exportName: 'default' },
  live_meta: { path: '../features/live-metadata/LiveMetadataPanel.tsx', exportName: 'default' },
  capture_scope: { path: '../features/capture-scope/CaptureScopePanel.tsx', exportName: 'default' },
  trust_trace: { path: '../features/trust-trace/TrustTraceGraph.tsx', exportName: 'default' },
  topic_card_preview: { path: '../features/topic-card-preview/TopicCardPreviewCandidate.tsx', exportName: 'default' },
  topic_card_vault: { path: '../features/topic-card-vault/TopicCardVaultCandidate.tsx', exportName: 'default' },
  four_panel_shell: { path: '../layout/FourPanelShell.tsx', exportName: 'default' },
  main_nav: { path: '../layout/panels.ts', exportName: 'PANEL_SPECS' }
} as const;
```

现有组件中只有 TopicCard Preview/Vault 明确接受 `data` prop；UrlBar 接受 API callbacks 但不接受 initial value；FourPanelShell 接受 API callbacks 但不接受 initial `previewState`；LiveMetadata/CaptureScope/TrustTrace 目前是 fixture 常量。U7 不应强迫 production 组件马上改 props。建议先加 **state harness adapter**：在 Storybook-style 浏览器里包一层测试用 wrapper，通过 fake callback、mock promise、或 future `__fixture` adapter 来模拟视觉状态；production component 暂不改。

## 6. Storybook-style browser UI candidate, ≤300 React lines

```tsx
import React, { useMemo, useState } from 'react';
import states from './state-library.generated.json';
import UrlBar from '../features/url-bar/UrlBar';
import LiveMetadataPanel from '../features/live-metadata/LiveMetadataPanel';
import CaptureScopePanel from '../features/capture-scope/CaptureScopePanel';
import TrustTraceGraph from '../features/trust-trace/TrustTraceGraph';
import TopicCardPreviewCandidate from '../features/topic-card-preview/TopicCardPreviewCandidate';
import TopicCardVaultCandidate from '../features/topic-card-vault/TopicCardVaultCandidate';
import FourPanelShell from '../layout/FourPanelShell';

const components = {
  url_bar: UrlBar,
  live_meta: LiveMetadataPanel,
  capture_scope: CaptureScopePanel,
  trust_trace: TrustTraceGraph,
  topic_card_preview: TopicCardPreviewCandidate,
  topic_card_vault: TopicCardVaultCandidate,
  four_panel_shell: FourPanelShell,
  main_nav: StateLibraryNavPreview,
};

function StateLibraryNavPreview({ data }) {
  return <nav aria-label="State library navigation">{data.items.map((id) => <button key={id}>{id}</button>)}</nav>;
}

function makeHarnessProps(row) {
  const props = JSON.parse(row.props_json || '{}');
  if (row.panel_name === 'url_bar') {
    return {
      createCapture: async () => {
        if (row.state_name === 'error') throw new Error(props.errorMessage || 'Create capture failed.');
        await new Promise((r) => setTimeout(r, row.state_name === 'loading' ? 2000 : 0));
        return { capture_id: 'cap_fixture', platform_item_id: 'BV_fixture', canonical_url: props.value };
      },
      onCaptureCreated: () => undefined,
      onDraftChange: () => undefined,
    };
  }
  if (row.panel_name === 'topic_card_preview' || row.panel_name === 'topic_card_vault') {
    return { data: props.data || props };
  }
  if (row.panel_name === 'four_panel_shell') {
    return {
      createCapture: async () => ({ capture_id: props.captureId || 'cap_fixture' }),
      loadPreview: async () => {
        if (row.state_name === 'error') throw new Error(props.previewError?.message || 'Preview request failed.');
        return props.preview || { capture_id: 'cap_fixture', target_path: '/tmp/a.md', frontmatter: {}, warnings: [], body_markdown: '# fixture' };
      },
    };
  }
  return props;
}

export default function StateLibraryBrowser() {
  const [panel, setPanel] = useState('url_bar');
  const [stateId, setStateId] = useState(states[0].state_id);
  const visible = useMemo(() => states.filter((s) => s.panel_name === panel), [panel]);
  const row = states.find((s) => s.state_id === stateId) || visible[0];
  const Component = components[row.panel_name];
  return (
    <main className="state-library-browser">
      <aside>
        {Object.keys(components).map((p) => <button onClick={() => setPanel(p)} key={p}>{p}</button>)}
      </aside>
      <section>
        <select value={row.state_id} onChange={(e) => setStateId(e.target.value)}>
          {visible.map((s) => <option key={s.state_id} value={s.state_id}>{s.state_name} / {s.variant_name}</option>)}
        </select>
        <div data-state-id={row.state_id} data-panel={row.panel_name} className="preview-frame">
          <Component {...makeHarnessProps(row)} />
        </div>
        <pre>{JSON.stringify(row, null, 2)}</pre>
      </section>
    </main>
  );
}
```

## 7. Registration workflow

1. **Extract state intent** from component/test/docs: create `state_id`, `panel_name`, `state_name`, `variant_name`, source path, route, and props fixture.
2. **Insert row without screenshot**: `evidence_status='deferred_visual_evidence'`, `five_gate_status='not_run'`.
3. **PF-V attaches screenshot**: screenshot file enters visual_asset first, then state row receives `screenshot_asset_id`, `screenshot_path`, `screenshot_sha256`.
4. **Automation audit runs**: Gate 2/3/4 plus assistive Gate 1/5 metrics write `state_gate_audit.machine_report_json`.
5. **Human review**: visual hierarchy and visual weight get human verdict; final row status changes to `human_pass` only when required fields exist.
6. **Query and reuse**: H5, poster, PPT, future DiloFlow, and DAM can query by panel/state/phase without duplicating screenshot metadata.

## 8. Query examples

```sql
-- states lacking screenshots
SELECT state_id, panel_name, state_name, variant_name
FROM state_library
WHERE evidence_status = 'deferred_visual_evidence'
ORDER BY panel_name, state_name;

-- states whose auto gate passed but human gate is pending
SELECT l.state_id, a.audit_id, a.gate_1_hierarchy_status, a.gate_5_weight_status
FROM state_library l
JOIN state_gate_audit a USING(state_id)
WHERE a.final_status = 'human_pending';

-- PF-V S04 URL Bar states
SELECT state_id, screenshot_path, five_gate_status
FROM state_library
WHERE panel_name = 'url_bar' AND phase LIKE 'PF-V%';
```

## 9. Acceptance criteria

- At least 48 canonical rows registered, exactly eight panels × six canonical states.
- Each row has a route, component export, source path, props_json, viewport, claim label, and no implicit production approval.
- Screenshot fields are nullable before PF-V attachment, but once attached must carry sha256 and visual_asset link.
- State browser can filter by panel, state, variant, gate status, and evidence status.
- Browser UI stays small: ≤300 React lines; Python/SQL exporter stays within the single-user budget.
- Main navigation remains marked as candidate/inferred until a dedicated component or route map is promoted.

## 10. Notes for future implementation

The cleanest implementation is not to install full Storybook immediately. Use a tiny local browser first because U7 is a register/audit lane, not a component-doc platform adoption. Storybook/Chromatic can be adopted later if package policy and CI budget permit it. The state-library schema is deliberately compatible with Storybook stories: each row can produce a story id, and each story id can map back to `state_id`. That means no rework if the project later chooses Storybook.


## 11. Seed-row generation pattern

The registry should be generated from a deterministic seed list, not typed manually in SQLite. Manual SQL entry invites drift: one row will use `live_metadata` while another uses `live_meta`; one row will call a state `failed` while another uses `error`; one screenshot will omit the viewport. The seed generator should own all canonical spelling and produce both SQL rows and browser JSON.

Recommended seed source shape:

```json
{
  "panel_name": "url_bar",
  "state_name": "error",
  "variant_name": "create_capture_error",
  "component_route": "../features/url-bar/UrlBar.tsx",
  "component_export": "default",
  "source_component_path": "apps/capture-station/src/features/url-bar/UrlBar.tsx",
  "props_json": {
    "value": "https://www.bilibili.com/video/BV_error",
    "errorMessage": "Create capture failed.",
    "expected_status": "manual_url ready"
  },
  "viewport": "desktop-1360x900",
  "phase": "PF-V-P2",
  "claim_label": "candidate_not_authority"
}
```

A single seed row can be expanded into three rows if PF-V wants desktop/tablet/mobile evidence. The canonical `state_id` should remain stable with viewport as a separate field, or become viewport-qualified only in screenshot evidence. I recommend keeping `state_id` viewport-neutral because it is the semantic identity; screenshot evidence and audit reports are viewport-specific.

## 12. Harness adapter rules

Harness adapters are allowed only in the state-library browser and audit runner. They must not silently drift from component truth. For every adapter, record:

- which production component path it wraps;
- which props are native component props;
- which props are harness-only simulation knobs;
- which state transitions are simulated by fake promises or callback interception;
- whether the current component source can truly render the requested state.

Example for UrlBar: the component accepts `createCapture`, `onCaptureCreated`, and `onDraftChange`, but not `initialValue`. A harness can simulate error by injecting `createCapture` that rejects after the user clicks. It cannot truly show an empty initial field without either user-event setup or a controlled initial wrapper. Therefore the row should say `fixture_control=interaction_driven`, not `fixture_control=native_prop`. This distinction prevents state-library from becoming a fantasy catalog.

For LiveMetadataPanel, CaptureScopePanel and TrustTraceGraph, current code is mostly static. The first U7 browser may render only current full-ish state and use adapter mock panels for other states. That is acceptable if the adapter screenshot is labeled `adapter_rendered`, not `production_rendered`. Later implementation dispatches can add props to production components if desired.

## 13. State identity governance

State ids should never depend on English display copy. Copy changes frequently; state meaning should not. Use stable slugs:

```text
panel.state.variant
url_bar.full.manual_url_ready
capture_scope.error.scope_contradiction
trust_trace.partial.capture_metadata_ready
topic_card_vault.error.unsafe_target_path_error
```

If display copy changes from “manual_url ready” to “ready for metadata capture”, the `state_id` should remain `url_bar.full.manual_url_ready`. If product semantics change, create a new variant and mark the old one stale. Do not rename old state ids casually because screenshot links, audit reports and PF-V evidence would break.

## 14. State-library browser behavior requirements

A useful browser is not just a gallery. It should show four panes:

1. rendered state frame;
2. metadata table for the selected row;
3. screenshot/audit evidence summary;
4. copyable handoff snippet for PF-V or human review.

Minimum controls:

- panel filter;
- state filter;
- variant search;
- viewport selector;
- evidence status filter;
- gate status filter;
- “show stale only” toggle;
- “copy state_id” button;
- “open screenshot path” link if evidence exists;
- “open human review queue item” link if pending.

The UI can still fit under 300 lines if it avoids elaborate styling. It should use the same dark shell palette only enough to be legible; it should not become a new product surface.

## 15. Invalidation contract

A state row can be valid while its screenshot is stale. Distinguish these cases:

| Case | state row | screenshot evidence | gate audit |
|---|---|---|---|
| new state, no screenshot | valid | deferred | not_run |
| screenshot attached, component unchanged | valid | attached | machine/human status applies |
| component changed after screenshot | valid | stale | blocked until refresh |
| state semantics changed | superseded | stale/invalid | blocked |
| screenshot hash mismatch | valid | invalidated | blocked |
| human review failed | valid | attached failed evidence | human_fail |

This state machine avoids a subtle but serious error: deleting the state when only the screenshot is stale. The semantic state remains a requirement even when visual evidence must be regenerated.

## 16. Composite shell rows

`four_panel_shell` states are composite. A shell screenshot is not a replacement for child-panel screenshots because a child may pass inside the shell but fail in isolation, or vice versa. Add optional `composite_children_json` in a v1.1 schema:

```sql
ALTER TABLE state_library ADD COLUMN composite_children_json TEXT NOT NULL DEFAULT '[]';
```

For example:

```json
[
  "url_bar.full.manual_url_ready",
  "live_meta.full.safe_metadata_complete",
  "capture_scope.full.allowed_blocked_candidate_all",
  "trust_trace.full.ready_pending_blocked_visible"
]
```

The audit runner should audit composite rows but also verify that all child state ids exist. Human reviewers should see both the shell screenshot and child screenshots if available.

## 17. Why not make Storybook the first step

Storybook is attractive, but in this project the first problem is not “lack of component docs”; it is “lack of state evidence registry”. Installing and configuring Storybook may be right later, but it adds package decisions and CI surface. U7 can keep the architecture Storybook-compatible by generating stories from state rows later:

```ts
export const ManualUrlReady = makeStateStory('url_bar.full.manual_url_ready');
```

That path lets U7 start with SQLite + JSON + tiny browser and graduate to Storybook only after the state taxonomy proves useful.

## 18. Minimum operator checklist

Before a state row is accepted:

- state id slug is stable and canonical;
- panel name is one of the eight allowed panels;
- state name is one of the six canonical states or `custom` with a reason;
- variant name explains the stress condition;
- props_json is valid JSON;
- source component path exists or is marked adapter/inferred;
- screenshot is not required yet, but evidence status is explicit;
- no row claims visual approval before 5-Gate and human review.
