---
title: PF-V-P2-MIGRATION-PATH-2026-05-07
status: candidate / not-authority / not-production-approval
claim_label: ≥95% candidate-spec confidence
request_date_label: 2026-05-07
generated_at_actual: 2026-05-06
write_enabled: false
boundary: spec-only; no apps/** mutation; no screenshots generated
---

# PF-V-P2-MIGRATION-PATH-2026-05-07

> 口径：本文件是 U7 candidate spec，不是 authority，不批准 runtime、frontend implementation、package install、browser automation、migration、vault true write 或 production 修改。文件名沿用用户 prompt 的 2026-05-07；实际生成环境日期为 2026-05-06。所有 “state” 都是可注册、可审计、可迁移的视觉状态，不等同于当前组件已经有完整可控 props。


## 1. Migration thesis

PF-V P2 is already producing state-oriented visual material, but without U7 it remains file-folder evidence. The migration path should not interrupt PF-V image production. It should wrap PF-V outputs in a state registry after the fact, then progressively move PF-V toward generating state-library rows at source.

The prompt names PF-V S04 URL Bar with roughly ten states, S05 Live Metadata with roughly ten variants, and S06-S09 each with five to ten states. U7’s canonical inventory is 48 states; PF-V can exceed that count through variants. The mapping is many-to-one at the canonical state level and one-to-one at the variant level.

## 2. Inputs expected from PF-V

Minimal file contract:

```text
PF-V-P2/
  INDEX.csv
  S04-url-bar/
    desktop/url_bar_full_manual_url_ready.png
    desktop/url_bar_error_create_capture_error.png
  S05-live-metadata/
  S06-capture-scope/
  S07-trust-trace/
  S08-topic-card-preview/
  S09-topic-card-vault/
```

Minimum `INDEX.csv` columns:

| Column | Required | Meaning |
|---|---:|---|
| `pfv_step` | yes | S04/S05/... |
| `panel_name` | yes | U7 canonical panel name |
| `state_name` | yes | empty/loading/partial/full/error/amend/custom |
| `variant_name` | yes | stable slug |
| `viewport` | yes | desktop/tablet/mobile dimensions |
| `screenshot_path` | yes | relative file path |
| `source_component_path` | yes | TSX or adapter source |
| `notes` | no | human-readable context |

## 3. Mapping table

| PF-V step | U7 panel | Canonical destination | Notes |
|---|---|---|---|
| S04 URL Bar | `url_bar` | six canonical states plus variants | S04’s ten states should map into value/submit/error/amend families |
| S05 Live Metadata | `live_meta` | six canonical states plus variants | variants likely cover row density, auth-present fixture, missing fields |
| S06 Capture Scope | `capture_scope` | six canonical states | ensure blocked and candidate lanes are visible |
| S07 Trust Trace | `trust_trace` | six canonical states | ready/pending/blocked graph variants |
| S08 Topic Card Preview | `topic_card_preview` | six canonical states | long title/metrics/review step overflow are variants |
| S09 Topic Card Vault | `topic_card_vault` | six canonical states | markdown/path/frontmatter variants |
| PF-V Shell pass | `four_panel_shell` | six canonical states | composite screenshots should declare child state ids |
| PF-V Navigation pass | `main_nav` | six canonical states | until production nav lands, use state-library adapter |

## 4. Migration phases

### Phase A — register without moving assets

Read PF-V `INDEX.csv`, create missing `state_library` rows, and link screenshot paths as external references. Do not copy files yet. This minimizes risk and lets U7 validate taxonomy quickly.

### Phase B — sha256 and visual_asset attachment

For every screenshot path, compute sha256 and create/attach U4 visual_asset. Update `state_screenshot_evidence`. If the screenshot file is missing, keep the state row but mark `evidence_status='deferred_visual_evidence'`.

### Phase C — audit queue generation

Run Gate 2/3/4 automation. All rows with screenshot evidence enter human queue for Gate 1 and Gate 5. Rows without screenshots remain `not_run`.

### Phase D — PF-V native generation

After the registry is stable, PF-V should generate from `state_library` rows instead of handmade lists. PF-V reads states, renders state browser, writes screenshot, computes hash, and posts back asset id.

## 5. CSV ingest pseudocode

```python
import csv, hashlib, json, sqlite3
from pathlib import Path

PANEL_ALLOW = {'url_bar','live_meta','capture_scope','trust_trace','topic_card_preview','topic_card_vault','four_panel_shell','main_nav'}
STATE_ALLOW = {'empty','loading','partial','full','error','amend','custom'}

def state_id(row):
    return f"{row['panel_name']}.{row['state_name']}.{row['variant_name']}"

def sha256(path):
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b''):
            h.update(chunk)
    return h.hexdigest()

conn = sqlite3.connect('state-library.sqlite')
for row in csv.DictReader(open('INDEX.csv', newline='')):
    assert row['panel_name'] in PANEL_ALLOW
    assert row['state_name'] in STATE_ALLOW
    sid = state_id(row)
    props = json.dumps({'pfv_step': row['pfv_step'], 'variant_name': row['variant_name']})
    conn.execute('''
      INSERT INTO state_library(state_id,panel_name,state_name,variant_name,component_route,component_export,source_component_path,props_json,viewport,phase)
      VALUES(?,?,?,?,?,?,?,?,?,?)
      ON CONFLICT(state_id) DO UPDATE SET updated_at=CURRENT_TIMESTAMP
    ''', (sid,row['panel_name'],row['state_name'],row['variant_name'],row['source_component_path'],'default',row['source_component_path'],props,row['viewport'],'PF-V-P2'))
    p = Path(row['screenshot_path'])
    if p.exists():
        digest = sha256(p)
        conn.execute('UPDATE state_library SET screenshot_path=?, screenshot_sha256=?, evidence_status=? WHERE state_id=?',
                     (str(p), digest, 'screenshot_attached', sid))
conn.commit()
```

## 6. Handling mismatches

| Mismatch | Action |
|---|---|
| PF-V state name not in canonical six | register as `custom`, add mapping note |
| Screenshot path missing | keep state row, mark deferred evidence |
| Panel name differs, e.g. `live_metadata` | normalize to `live_meta`, record source alias |
| Duplicate screenshot for same state/viewport | preserve latest as active, keep older as historical visual_asset |
| Composite shell screenshot | link shell state and child state ids through `composite_children_json` extension |
| Main nav screenshot without production component | link to adapter and mark confidence medium |

## 7. Non-conflict with PF-V

PF-V remains the image lane. U7 does not tell PF-V what to draw beyond the registered state intent and audit requirements. PF-V can continue producing more than 48 screenshots; U7 will register them as variants. The only hard requirement is that each screenshot becomes queryable and auditable.

## 8. Recommended migration order

1. Register canonical 48 rows from this spec.
2. Ingest S04 URL Bar first because source state is best understood and error/loading are concrete.
3. Ingest S08/S09 Topic Card Preview/Vault next because data props make fixture generation clean.
4. Ingest S06/S07 static panels with adapter notes.
5. Ingest S05 Live Metadata with strong warning against live-runtime implication.
6. Add shell composite states after child states exist.
7. Add main_nav last because current component evidence is weakest.

## 9. Acceptance criteria

- PF-V `INDEX.csv` can be transformed into U7 rows without changing PF-V screenshots.
- Each screenshot has sha256 and state_id.
- S04-S09 variants are not collapsed or lost; they map to canonical state + variant.
- Missing evidence is explicit rather than hidden.
- Migration does not write apps/**, does not run browser automation unless separately approved, and does not claim visual approval before 5-Gate + human review.


## 10. Concrete S04 URL Bar mapping

PF-V S04’s ten-state set can map as follows:

| PF-V likely state | U7 canonical | variant |
|---|---|---|
| blank input | `empty` | `manual_url_required_empty` |
| focused blank | `empty` | `focused_empty` |
| invalid partial | `partial` | `invalid_partial_url` |
| sample filled | `full` | `sample_bv_ready` |
| long valid URL | `full` | `long_url_ready` |
| submit pending | `loading` | `submit_in_flight` |
| API success before preview | `full` | `capture_created` |
| API error | `error` | `create_capture_error` |
| long error | `error` | `long_error_message` |
| draft edited after preview | `amend` | `draft_change_resets_preview` |

This keeps the prompt’s “S04 has 10 states” compatible with U7’s canonical six states. U7 does not throw away PF-V detail; it stores detail as variants.

## 11. Concrete S05 Live Metadata mapping

Likely S05 variants:

| PF-V likely variant | U7 canonical | Migration note |
|---|---|---|
| no capture | `empty` | no metadata rows |
| skeleton rows | `loading` | do not imply BBDown live |
| title only | `partial` | safe partial |
| title + duration | `partial` | record missing fields |
| full safe metadata | `full` | evidence source required |
| auth-present fixture | `full` | badge must say fixture/source |
| probe blocked | `error` | blocked message |
| missing field warning | `error` or `partial` | depends on severity |
| title corrected | `amend` | rows_version v2 |
| page selection changed | `amend` | selected_page changed |

## 12. S06-S09 mapping discipline

S06/S07 are static-ish components, so PF-V screenshots may be more conceptual than production-rendered. Record `fixture_control=adapter_rendered` until production props exist. S08/S09 are cleaner because data props exist; register these as `production_rendered` if the screenshot uses the actual component with data prop. The distinction will help later code review prioritize which components need refactoring.

## 13. Migration dry-run output

Every ingest should produce a markdown summary:

```text
PF-V-P2 ingest dry-run
rows_read: 72
state_rows_created: 48
state_rows_updated: 24
screenshots_found: 68
screenshots_missing: 4
aliases_used:
  live_metadata -> live_meta: 10
machine_audit_enqueued: 68
human_queue_enqueued: 136
blocked:
  main_nav.full.eight_panel_nav_full: screenshot missing
```

This summary should be attached to the dispatch ledger. It should not be interpreted as visual approval.

## 14. Alias map

Use an explicit alias map rather than fuzzy matching:

```python
PANEL_ALIAS = {
  'url-bar': 'url_bar',
  'url_bar': 'url_bar',
  'live-metadata': 'live_meta',
  'live_metadata': 'live_meta',
  'capture-scope': 'capture_scope',
  'trust-trace': 'trust_trace',
  'topic-card-preview': 'topic_card_preview',
  'topic-card-vault': 'topic_card_vault',
  'four-panel-shell': 'four_panel_shell',
  'main-nav': 'main_nav',
}
```

Fuzzy matching is risky because `vault-preview` and `topic-card-vault` are semantically different. If an unknown alias appears, stop the ingest and write a defer note.

## 15. Screenshot path policy

PF-V screenshot paths should be relative to a known root and must not include user home secrets or raw local-only material. Store:

- relative path;
- sha256;
- viewport;
- source PF-V step;
- generated_at if available;
- source component path;
- state id.

Do not store raw stdout or browser logs that may contain secrets. If screenshots contain local filesystem paths, confirm they are safe or redact.

## 16. Human review handoff after migration

After ingest, produce a human queue grouped by panel and severity:

1. machine failures first, because they block pass;
2. error states second, because they often have color/occlusion risk;
3. topic-card-vault markdown-dense states third;
4. shell composite states fourth;
5. full states last if machine pass.

Reviewers should not be asked to review screenshots with missing state metadata. A screenshot without state id is not ready for human gate.

## 17. Migration acceptance detail

The migration is complete only when every PF-V screenshot either:

- maps to an active U7 state row;
- maps to a custom state with reason;
- is marked out-of-scope with reason;
- or is missing/invalid and listed in the dry-run report.

No silent leftovers. A folder full of screenshots without registry rows is exactly the problem U7 is meant to solve.


## 18. Migration validation commands

Candidate commands for a local authorized run:

```bash
python tools/u7_ingest_pfv_index.py \
  --index PF-V-P2/INDEX.csv \
  --screenshot-root PF-V-P2 \
  --db .u7/state-library.sqlite \
  --dry-run

python tools/u7_ingest_pfv_index.py \
  --index PF-V-P2/INDEX.csv \
  --screenshot-root PF-V-P2 \
  --db .u7/state-library.sqlite \
  --write

python tools/u7_report_coverage.py \
  --db .u7/state-library.sqlite \
  --out .u7/pfv-p2-coverage.md
```

The first command should be the default. The `--write` command requires dispatch permission because it changes local registry state.

## 19. Coverage report fields

The coverage report should include:

- total rows by panel/state;
- screenshots attached vs deferred;
- missing canonical states;
- custom states requiring review;
- stale assets;
- machine audit counts;
- human queue counts;
- screenshots with no matching row;
- rows with no source component path;
- rows using adapter/inferred route.

This report becomes the practical bridge between PF-V and U7. It lets the user see not only “how many images exist” but “which states are actually evidenced and reviewable”.

## 20. Stop conditions

Stop the migration rather than guessing if:

- `INDEX.csv` is missing required columns;
- panel alias is unknown;
- screenshot path points outside the allowed screenshot root;
- hash calculation fails;
- a screenshot appears to contain credentials or auth material;
- PF-V state claims runtime unlock not approved by current authority;
- a row attempts to map media download/ASR/browser automation to an active state.

Write a defer note with the exact blocker. A partial, truthful ingest is better than a broad, false import.


## 21. Custom states policy

PF-V may discover states not in the canonical six. Examples: `blocked`, `success`, `reviewed`, `stale`, `unsupported_mobile`. Do not reject them blindly. Register them as `state_name='custom'` with `variant_name` carrying the discovered state, then decide whether they fold into canonical six later.

```json
{
  "panel_name": "topic_card_preview",
  "state_name": "custom",
  "variant_name": "reviewed_but_human_failed",
  "notes": "PF-V found a state after human review failed visual weight"
}
```

A monthly or wave closeout can normalize custom states. Immediate ingestion should prioritize not losing evidence.

## 22. State-library generated PF-V worklist

Once U7 rows exist, PF-V can consume a worklist:

```csv
state_id,panel_name,state_name,variant_name,viewport,priority,required_boundary_copy
url_bar.error.create_capture_error,url_bar,error,create_capture_error,desktop-1360x900,P0,manual_url ready
capture_scope.full.allowed_blocked_candidate_all,capture_scope,full,allowed_blocked_candidate_all,desktop-1360x900,P0,audio_transcript blocked
```

This flips the workflow: instead of PF-V inventing screenshot names and U7 trying to interpret them, U7 declares the evidence backlog and PF-V fills it.

## 23. Priority order for missing screenshots

If PF-V cannot produce every screenshot quickly, prioritize:

1. error and blocked states;
2. full states with boundary copy;
3. loading states that may imply completion;
4. amend/reset states;
5. empty states;
6. decorative nav variants.

Negative states are more important because they prevent product overclaim.
