---
status: candidate / not-authority / not-runtime-approval
created_for: Cloud Prompt U4 Visual Asset Spine
requested_date: 2026-05-07
generated_in_session_date: 2026-05-06
write_enabled: false
claim_scope: spec-only; no production code modification; no dispatch authorization
---

# PF-V INTEGRATION MAP — INDEX.csv ↔ U4 modules

> claim label: ≥95% for migration strategy; actual PF-V CSV rows/headers are `needs_local_refresh` because the file was not present in this container.

## 1. Integration purpose

PF-V is already operating as a visual asset ecosystem: GPT-Image-2 reverse H5, approximately 160-180 images, 18+ GPT Pro sessions, S00-S18 prompt system, Pattern A-J, and an `INDEX.csv` with 19 tracking columns. U4 should not tell PF-V to slow down; it should make the resulting asset pile legible, searchable, reusable, and auditable.


## Source Register / 证据边界

- PRD-v2/SRD-v2 的稳定事实：ScoutFlow 是 single-user、local-first、SQLite + FS + state words 的 authority-first 工作台；当前不得自动批准 SaaS、多用户、runtime 扩张、media/ASR、browser automation、vault true write 或 migration。
- Capture Station 的已读事实：`apps/capture-station/package.json` 是 React 18 + Vite 5，未把 Tailwind/shadcn/Panda/Radix/React Flow/TanStack/Lucide 写成已批准依赖；现有 H5 代码使用深海蓝 palette、inline style、URL Bar + Vault Preview/Dry Run + Live Metadata + Capture Scope + Trust Trace 的工作台结构。
- Visual docs 的已读事实：`design-brief.md` 固定 4 面板扫描顺序；`five-gate-checklist.md` 要求 5 gate 全过才可称 visual pass；`trust-trace-graph-spec.md` 固定 `capture -> capture_state -> metadata_job -> probe_evidence -> receipt_ledger -> media_audio -> audit` 节点链。
- 本地缺口：容器内没有 `~/workspace/ScoutFlow`、没有 `~/.claude/rules/aesthetic-first-principles.md`、没有 PF-V 实际 `INDEX.csv`，因此相关内容均标为 `needs_local_refresh`。
- Live web 缺口：本运行环境禁用实时网页浏览；任何 vendor / 2026 工具状态只能列为待验证 URL 种子，不得写成已访问事实。

## 2. Import philosophy

The importer must be **header-driven**. It should not hard-code a 19-column order because the actual CSV was not available. It should accept aliases, print the resolved mapping, and fail closed when a required field cannot be found.

Required minimal fields:

| required concept | accepted aliases | target |
|---|---|---|
| file path | `file`, `file_path`, `path`, `output_path`, `image_path` | visual_assets.file_path |
| phase/session | `phase`, `run`, `session`, `sxx`, `wave` | visual_assets.phase |
| kind/source | `kind`, `asset_kind`, `source`, `source_type` | visual_assets.kind |

Optional fields:

| optional concept | target | default |
|---|---|---|
| prompt/session id | visual_assets.prompt_id + prompt usage | null / placeholder |
| pattern A-J | visual_assets.pattern_tag | null |
| parent | visual_assets.parent_asset_id | null |
| state | visual_assets.state | candidate |
| score/pass | quality_score / five_gate_audit_passed | null / 0 |
| width/height | width/height | compute |
| sha/pHash | sha256/perceptual_hash | compute |
| notes | notes | empty |

## 3. Candidate 19-column normalization

The following table is a likely normalization target, not a claim that PF-V uses these exact headers.

| # | normalized column | maps to | module |
|---:|---|---|---|
| 1 | `index_id` | import event payload | visual_asset_events |
| 2 | `file_path` | `visual_assets.file_path` | visual_asset |
| 3 | `asset_kind` | `visual_assets.kind` | visual_asset |
| 4 | `phase` | `visual_assets.phase` | visual_asset |
| 5 | `session` | prompt seed / run label | prompt_template |
| 6 | `prompt_id` | `visual_assets.prompt_id` | prompt_template |
| 7 | `prompt_version` | prompt_templates.version | prompt_template |
| 8 | `pattern_letter` | `visual_assets.pattern_tag` | pattern_library |
| 9 | `parent_asset` | `visual_assets.parent_asset_id` | visual_asset |
| 10 | `state` | `visual_assets.state` | visual_asset |
| 11 | `quality_score` | `visual_assets.quality_score` | visual_asset |
| 12 | `gate_1` | visual_gate_audits | 5-Gate |
| 13 | `gate_2` | visual_gate_audits | 5-Gate |
| 14 | `gate_3` | visual_gate_audits | 5-Gate |
| 15 | `gate_4` | visual_gate_audits | 5-Gate |
| 16 | `gate_5` | visual_gate_audits | 5-Gate |
| 17 | `decision` | state/event notes | visual_asset_events |
| 18 | `reuse_target` | visual_asset_phase_use | visual_asset |
| 19 | `notes` | visual_assets.notes | visual_asset |

## 4. Dry-run output contract

```yaml
PFV_IMPORT_DRY_RUN: true
csv_path: <path>
rows_seen: <n>
rows_importable: <n>
rows_blocked: <n>
resolved_columns:
  file_path: <header>
  phase: <header>
  kind: <header-or-inferred>
  prompt_id: <header-or-null>
  pattern_tag: <header-or-null>
blocked_reasons:
  missing_file_path: <n>
  missing_file_on_disk: <n>
  invalid_kind: <n>
  invalid_pattern_tag: <n>
will_write: false
```

## 5. Import pseudocode

```python
ALIASES = {
  'file_path': ['file_path','path','output_path','image_path','file'],
  'phase': ['phase','run','session','wave','sxx'],
  'kind': ['kind','asset_kind','source','source_type'],
  'prompt_id': ['prompt_id','prompt','session_prompt','s_prompt'],
  'pattern_tag': ['pattern','pattern_tag','pattern_letter','a_j'],
}

def resolve(headers):
    lower = {h.lower().strip(): h for h in headers}
    out = {}
    for target, aliases in ALIASES.items():
        out[target] = next((lower[a] for a in aliases if a in lower), None)
    if not out['file_path'] or not out['phase']:
        raise SystemExit('PF-V import requires file_path and phase')
    return out

def normalize_kind(raw, path):
    r = (raw or '').lower()
    if r in {'raw_screenshot','gpt_image_2','svg','mockup','icon','illustration','token_visual'}:
        return r
    if str(path).endswith('.svg'): return 'svg'
    if 'token' in r: return 'token_visual'
    if 'gpt' in r or 'image' in r: return 'gpt_image_2'
    return 'mockup'
```

## 6. Migration steps

1. Run `pfv-import --dry-run INDEX.csv`.
2. Review resolved header mapping and blocked reasons.
3. Seed missing prompt placeholders S00-S18 only; do not invent bodies.
4. Seed Pattern A-J placeholders only; do not invent definitions if PF-V has actual ones.
5. Import assets as `candidate` unless the CSV carries explicit all-gate pass evidence.
6. Generate thumbnails/pHash after import.
7. Run contract audit and print lock candidates.
8. Only then transition selected rows to `refined` or `locked`.

## 7. Mapping to prompt_template

S00-S18 can be represented as prompt templates even before bodies are available. The importer should link rows by session label:

```text
S00 -> pt_s00_v0
S01 -> pt_s01_v0
...
S18 -> pt_s18_v0
```

If the CSV has prompt bodies, import them. If not, set `template_body='[needs_body_backfill]'` and `claim_label='needs_body_backfill'`.

## 8. Mapping to pattern_library

Pattern letters A-J are legal as tags if they match `^[A-J]$`. If actual names are missing, link to placeholder rows. If actual names are later provided, update `pattern_entries.description` and preserve asset links.

## 9. Mapping to 5-Gate

If the CSV has five columns with pass/fail, create one `visual_gate_audits` row per asset with `audit_source='pfv_index_csv'`. If any gate is unknown, `five_gate_audit_passed` remains 0.

## 10. Acceptance checklist

- Importer never assumes exact 19-column order.
- Unknown quality cannot become `locked`.
- Missing files block insert or create a dry-run warning; no phantom asset rows.
- S00-S18 and A-J are linked as placeholders when bodies/definitions are unavailable.
- Reuse targets populate `visual_asset_phase_use`, not ad-hoc notes only.


## 11. Example dry-run mapping

If PF-V provides a row like:

```csv
file_path,session,kind,pattern,decision,gate_1,gate_2,gate_3,gate_4,gate_5,notes
outputs/S07/e_trace_04.png,S07,gpt_image_2,E,refined,pass,pass,fail,pass,pass,"toast overlaps mobile node"
```

The importer should produce:

```yaml
asset:
  kind: gpt_image_2
  state: refined
  phase: PF-V-S07
  prompt_id: pt_s07_v0
  pattern_tag: E
  five_gate_audit_passed: 0
  notes: "toast overlaps mobile node"
gate_audit:
  source: pfv_index_csv
  gate_1: true
  gate_2: true
  gate_3: false
  gate_4: true
  gate_5: true
lock_ready: false
```

The critical behavior is preserving the failure. A four-out-of-five image can be valuable, but it is not locked.

## 12. Staging import protocol

```text
mkdir -p visual-assets/import-staging/PF-V-20260507
copy or symlink INDEX.csv into staging
run pfv-import --dry-run
review YAML stdout
run pfv-import --write --state-default candidate
run thumbs --missing-only
run contract-audit --phase PF-V-20260507
export phase-report.md
```

The importer should support `--state-default candidate` even if the CSV has a decision column. This is a safe mode for first import. After reviewing gate rows, the user can selectively promote refined/locked assets.

## 13. Rollback policy

Every import batch should have an `import_batch_id` in event payloads. If a batch is wrong, rollback can delete rows created by the batch while preserving files:

```sql
SELECT asset_id FROM visual_asset_events
WHERE event_kind='created'
  AND json_extract(event_payload_json, '$.import_batch_id')=:batch;
```

Then delete those asset rows inside a transaction. If prompt placeholders or pattern placeholders were created in the same batch, mark them deprecated rather than deleting if other assets now reference them.

## 14. Phase report shape

```yaml
PFV_PHASE_REPORT: true
phase: PF-V-S07
rows_imported: 38
assets_by_state:
  candidate: 21
  refined: 14
  locked: 0
  deprecated: 3
patterns_seen: [A, C, E, H]
prompt_sessions_seen: [S07]
gate_failures:
  gate_1: 2
  gate_2: 4
  gate_3: 11
  gate_4: 1
  gate_5: 5
recommended_actions:
  - "Run Pattern H repair loop on gate_3 mobile occlusion failures."
  - "Do not lock any S07 asset until at least one all-gate pass exists."
```

This report is what makes the PF-V import useful for later planning rather than just cataloging files.


## 15. Handling 160-180 images

The importer should be comfortable with hundreds of images but not optimize for millions. A single transaction per batch is fine for inserts. Thumbnail generation can happen after import because it is slower and more failure-prone. Recommended order:

```text
insert metadata rows -> commit -> generate thumbs/pHash row by row -> run gate/contract audit
```

If 20 files fail thumbnail generation, the metadata rows still exist and can be inspected. Do not make image processing failure erase lineage.

## 16. Session grouping

PF-V sessions S00-S18 can be grouped into phases even if the exact phase names differ:

| session band | likely role | phase label fallback |
|---|---|---|
| S00-S02 | bootstrap / direction | PF-V-bootstrap |
| S03-S06 | pattern exploration | PF-V-pattern-explore |
| S07-S10 | panel and graph refinement | PF-V-panel-refine |
| S11-S14 | token/code/lock review | PF-V-consolidation |
| S15-S18 | final audit/handoff | PF-V-handoff |

This grouping is only a fallback. If `INDEX.csv` has exact phase labels, those win.

## 17. Import quality gates

Rows should be blocked or downgraded when:

| issue | behavior |
|---|---|
| missing file | block insert in write mode |
| invalid pattern letter | insert with `pattern_tag=NULL` and warning, or block if strict |
| state says locked but gates missing | downgrade to refined/candidate and warn |
| prompt session unknown | link to placeholder `pt_unknown_v0` only if user allows |
| file extension unsupported | insert only if kind is SVG or metadata-only, no thumbnail |

The importer must prefer a noisy safe import over a quiet misleading import.

## 18. Backfill completion target

A PF-V integration is “complete enough” when:

```yaml
rows_imported: >= actual PF-V rows intended for retention
missing_files: 0
unknown_prompt_bodies: allowed_but_counted
pattern_placeholders: allowed_but_counted
locked_assets_without_5_gate: 0
phase_report_written: true
```

This target acknowledges that prompt bodies and pattern definitions may lag behind asset import while preserving lock honesty.


## 19. Human-in-the-loop checkpoints

PF-V import should require human checkpoints at three moments:

1. Header mapping review before write.
2. Gate failure summary before lock transitions.
3. Phase report review before next-session prompt generation.

These checkpoints are not bureaucracy; they are guardrails against letting a fast AI image pipeline silently promote weak or mislabeled assets. A single user can perform each checkpoint quickly if stdout is clear.

## 20. Integration with future S19+

If PF-V continues beyond S18, new sessions should not require schema changes. Use the same prompt seed pattern: `pt_s19_v0`, `pt_s20_v0`, and so on. Pattern tags may extend beyond J only after the current A-J set is audited. New sessions should inherit the same import policy: unknown body allowed, unknown gate pass not allowed.


## Appendix C — INDEX.csv reconciliation protocol

PF-V 当前 INDEX.csv 是事实运转源，但不是最终 authority。迁移时先生成 reconciliation report：总行数、可解析行数、缺失 prompt/session 的行、缺失文件路径的行、重复 sha256、重复 perceptual_hash、无法映射的 Pattern A-J。report 只输出，不写入，直到操作者确认本地路径和另窗口 prompt body 已收齐。

建议 report 字段：

```csv
index_row, proposed_asset_id, file_path_status, prompt_status, pattern_status, hash_status, action
12, va_pfv_0012, exists, prompt_stub, pattern_ok, new_hash, insert_candidate
13, va_pfv_0013, missing_file, prompt_stub, pattern_ok, no_hash, hold
```

迁移优先级：先 locked/refined 资产，再 candidate，再 gen；先有文件和 hash 的行，再补 prompt-only 记录。对于 160-180 张图，第一轮目标不是完美迁移，而是把可复用资产和 lineage 先纳入查询面。S00-S18 和 Run-1~Run-5 的 dispatch prompt 允许先建 stub，以免 visual_asset 因 FK 缺失无法入库；stub 必须带 `needs_body_backfill=true`。

### Cross-phase reuse example

U4 后续若要找“适合 Capture Station right graph 的高可信样式”，查询条件可以是：`pattern_tag in ('C','F','I') AND five_gate_audit_passed=1 AND phase in ('PF-V','U4') AND state in ('refined','locked')`。这比翻文件夹快，也保留了为什么这张图可复用的解释。


## Appendix D — non-destructive migration rule

PF-V 文件夹原结构不应在 U4 迁移中被整理、重命名或删除。visual_asset 表只登记路径与 hash；若需要更干净的资产目录，另建 `assets/visual-spine/` copy，并把原始路径放进 `source_file_path`。这样另窗口仍可继续跑 S00-S18，不会因为 U4 catalog 改动而断链。迁移脚本默认 `--dry-run`，只有显式 `--commit` 才写 DB。
