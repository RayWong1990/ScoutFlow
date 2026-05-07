---
status: candidate / not-authority / not-runtime-approval
created_for: Cloud Prompt U4 Visual Asset Spine
requested_date: 2026-05-07
generated_in_session_date: 2026-05-06
write_enabled: false
claim_scope: spec-only; no production code modification; no dispatch authorization
---

# CROSS-MODULE CONTRACT — U4 visual asset spine

> claim label: ≥95% for internal contract shape; no production API or database migration approval.

## 1. Contract purpose

The U4 spine exists because four asset classes are only useful when they can reference each other. A visual image without its prompt cannot be regenerated. A prompt without its pattern cannot be improved systematically. A pattern without example assets becomes folklore. Tokens without consumer records become a style wish. This contract defines the minimal local-first wiring that lets one prosumer user run a high-throughput visual agent fleet without drifting into enterprise DAM or production authority changes.


## Source Register / 证据边界

- PRD-v2/SRD-v2 的稳定事实：ScoutFlow 是 single-user、local-first、SQLite + FS + state words 的 authority-first 工作台；当前不得自动批准 SaaS、多用户、runtime 扩张、media/ASR、browser automation、vault true write 或 migration。
- Capture Station 的已读事实：`apps/capture-station/package.json` 是 React 18 + Vite 5，未把 Tailwind/shadcn/Panda/Radix/React Flow/TanStack/Lucide 写成已批准依赖；现有 H5 代码使用深海蓝 palette、inline style、URL Bar + Vault Preview/Dry Run + Live Metadata + Capture Scope + Trust Trace 的工作台结构。
- Visual docs 的已读事实：`design-brief.md` 固定 4 面板扫描顺序；`five-gate-checklist.md` 要求 5 gate 全过才可称 visual pass；`trust-trace-graph-spec.md` 固定 `capture -> capture_state -> metadata_job -> probe_evidence -> receipt_ledger -> media_audio -> audit` 节点链。
- 本地缺口：容器内没有 `~/workspace/ScoutFlow`、没有 `~/.claude/rules/aesthetic-first-principles.md`、没有 PF-V 实际 `INDEX.csv`，因此相关内容均标为 `needs_local_refresh`。
- Live web 缺口：本运行环境禁用实时网页浏览；任何 vendor / 2026 工具状态只能列为待验证 URL 种子，不得写成已访问事实。

## 2. Entity relationship summary

```text
prompt_template.prompt_id
  -> visual_asset.prompt_id
  -> prompt_template_usage.consumer_id

pattern_library.pattern_letter
  -> visual_asset.pattern_tag
  -> pattern_artifact_links.asset_id

design-tokens.json
  -> token_visual assets
  -> prompt_template parameter schema
  -> pattern_library references

5-Gate audit
  -> visual_asset.five_gate_audit_passed
  -> visual_asset.state locked guard
```

## 3. Foreign-key posture

Because these are sidecar modules and may be stored in separate SQLite files, strict SQLite foreign keys across files are optional. The contract therefore has two layers:

1. **Hard FK when co-located**: if `u4_assets.sqlite` stores all tables, use normal references.
2. **Soft FK when modular**: if each module has its own DB, run contract audit queries before `locked`, `handoff`, or `phase close`.

The recommended single-user implementation is a single sidecar DB first, with namespaces implemented as table prefixes. Split DBs only if file size or maintenance demands it.

## 4. Required link fields

| Source | Field | Target | Required when | Failure behavior |
|---|---|---|---|---|
| visual_assets | `prompt_id` | prompt_templates.prompt_id | generated or prompt-derived assets | candidate allowed, locked blocked if missing |
| visual_assets | `pattern_tag` | pattern_entries.pattern_letter | PF-V Pattern A-J assets | null allowed, mismatch blocked |
| pattern_artifact_links | `asset_id` | visual_assets.asset_id | example/counterexample links | missing asset blocks active pattern |
| prompt_template_usage | consumer_id | visual_asset / pattern / audit id | prompt used by a module | missing usage is warning |
| token_visual asset | prompt_id | token extraction prompt | generated token visuals | locked blocked if missing |
| visual_gate_audits | asset_id | visual_assets.asset_id | any gate audit | missing audit blocks `five_gate_audit_passed=1` |

## 5. Cross-module queries

### 5.1 Asset with prompt and pattern

```sql
SELECT
  v.asset_id,
  v.kind,
  v.state,
  v.phase,
  v.file_path,
  p.prompt_id,
  p.title AS prompt_title,
  p.version AS prompt_version,
  pe.pattern_letter,
  pe.slug AS pattern_slug
FROM visual_assets v
LEFT JOIN prompt_templates p ON p.prompt_id = v.prompt_id
LEFT JOIN pattern_entries pe ON pe.pattern_letter = v.pattern_tag
WHERE v.asset_id = :asset_id;
```

### 5.2 Lock readiness

```sql
SELECT
  v.asset_id,
  CASE WHEN v.prompt_id IS NOT NULL AND p.prompt_id IS NULL THEN 'missing_prompt' END AS prompt_issue,
  CASE WHEN v.pattern_tag IS NOT NULL AND pe.pattern_letter IS NULL THEN 'missing_pattern' END AS pattern_issue,
  CASE WHEN v.five_gate_audit_passed <> 1 THEN 'missing_5_gate_pass' END AS gate_issue
FROM visual_assets v
LEFT JOIN prompt_templates p ON p.prompt_id = v.prompt_id
LEFT JOIN pattern_entries pe ON pe.pattern_letter = v.pattern_tag
WHERE v.asset_id = :asset_id;
```

A result with any issue blocks `state='locked'`.

### 5.3 Phase reuse shortlist

```sql
SELECT
  v.asset_id, v.kind, v.phase AS source_phase, v.pattern_tag,
  pe.slug, p.title, v.quality_score, v.file_path
FROM visual_assets v
LEFT JOIN pattern_entries pe ON pe.pattern_letter = v.pattern_tag
LEFT JOIN prompt_templates p ON p.prompt_id = v.prompt_id
WHERE v.state='locked'
  AND v.phase <> :target_phase
  AND v.five_gate_audit_passed=1
ORDER BY v.quality_score DESC, v.created_at DESC
LIMIT 50;
```

## 6. Contract state transitions

```text
asset created
  -> prompt linked or marked unknown
  -> pattern linked or null
  -> thumbnail/phash generated
  -> 5-Gate audit attempted
  -> if all pass, set five_gate_audit_passed=1
  -> lock readiness query
  -> locked or refined/deprecated
```

No module can bypass the `locked` guard. A prompt can have high quality; a pattern can have high success rate; a token can match palette; none of these alone make an image locked.

## 7. Error taxonomy

| error | severity | meaning | action |
|---|---|---|---|
| `missing_prompt` | major | generated asset has no prompt registry row | backfill prompt or keep candidate |
| `missing_pattern` | major | pattern_tag cannot resolve | add placeholder pattern or clear tag |
| `gate_fail` | major | one or more 5-Gates failed | repair or deprecated |
| `hash_mismatch` | critical | file changed after registration | stop and re-register |
| `token_drift` | warning/major | generated CSS or asset uses non-token value | record drift, do not auto patch |
| `dispatch_auth_leak` | critical | dispatch prompt reads like authorization | block handoff |

## 8. Single-writer rule

U4 follows the ScoutFlow single-writer instinct: one local process writes the sidecar DB at a time. Readers can run concurrently. The simplest lock is a SQLite immediate transaction plus a `.lock` file for long thumbnail jobs. Multi-user merge conflict handling is deliberately out of scope.

## 9. Acceptance checklist

- Every module can operate alone, but lock/handoff requires contract audit.
- Contract audit is read-only except for explicit state transition commands.
- Cross-module links use stable IDs, not filenames or titles.
- Separate DB mode is allowed but audited as soft FK.
- The contract does not authorize production code, runtime, migration, or vault write.


## 10. Recommended unified DB bootstrap order

If implemented as one local DB, create tables in this order:

```text
1. prompt_templates
2. prompt_template_runs
3. prompt_template_usage
4. pattern_entries
5. pattern_artifact_links
6. pattern_domain_stats
7. visual_assets
8. visual_asset_events
9. visual_asset_phase_use
10. visual_gate_audits
```

`visual_assets` can be created before prompt/pattern tables if soft-FK mode is used, but the contract audit is simpler when prompt and pattern rows already exist. Seed placeholders before importing PF-V assets to avoid immediate missing-link noise.

## 11. Contract audit stdout

```yaml
U4_CONTRACT_AUDIT_COMPLETE: true
asset_id: va_...
checks:
  sha_current: pass
  prompt_link: warning_missing_placeholder_body
  pattern_link: pass_placeholder_definition
  five_gate: fail_gate_3
  token_drift: not_applicable
lock_ready: false
recommended_next_action: "repair gate 3 or keep refined"
```

The audit should distinguish `warning` from `fail`. Placeholder prompt body is a warning for candidate/refined states; missing 5-Gate pass is a fail for lock.

## 12. Transaction model

For the single-user case, use SQLite transactions rather than building a service. Long operations like thumbnail generation should select candidate rows, then update one row per transaction. This avoids locking the DB for minutes. State transitions should use `BEGIN IMMEDIATE` so two terminals cannot lock/deprecate the same asset simultaneously.

```sql
BEGIN IMMEDIATE;
SELECT state, sha256, five_gate_audit_passed FROM visual_assets WHERE asset_id=:id;
-- verify guard conditions in Python
UPDATE visual_assets SET state='locked' WHERE asset_id=:id;
INSERT INTO visual_asset_events (...);
COMMIT;
```

## 13. Boundary against ScoutFlow production API

U4 is intentionally not added to ScoutFlow's Thin API in this candidate. The reason is not that an API would be bad; it is that adding API endpoints would imply production surface area, tests, routes, and authority review. The sidecar DB lets the visual spine mature without disturbing Phase 1A capture constraints. If U4 is later promoted, the API should expose read-only projections first: `GET /visual-assets`, `GET /prompts`, `GET /patterns`, and only later guarded writes.

## 14. Phase closeout query

At the end of a visual phase, run:

```sql
SELECT state, COUNT(*) AS n
FROM visual_assets
WHERE phase=:phase
GROUP BY state;
```

Then run:

```sql
SELECT pattern_tag, COUNT(*) AS locked_count
FROM visual_assets
WHERE phase=:phase AND state='locked'
GROUP BY pattern_tag
ORDER BY locked_count DESC;
```

This produces a compact handoff: how many candidates were generated, how many refined, how many locked, and which patterns actually produced durable assets.


## 15. Handoff packet contract

A locked visual asset should be exportable as a small handoff packet:

```yaml
asset_id: va_...
file_path: visual-assets/gpt_image_2/...
sha256: <hash>
phase: PF-V-S14
state: locked
prompt:
  prompt_id: pt_s14_v0
  version: v0
pattern:
  letter: H
  slug: 5-gate-repair-loop
tokens:
  design_tokens_version: candidate-2026-05-07
gate_audit:
  audit_id: ga_...
  overall_pass: true
reuse:
  allowed_as: reference
  forbidden_as: production proof
```

This packet is the bridge between local creative iteration and future planning. It is intentionally not a dispatch authorization and not a product proof.

## 16. Contract report for phase close

A phase close report should combine all modules:

| metric | source |
|---|---|
| assets generated/refined/locked/deprecated | visual_assets |
| prompts used and superseded | prompt_templates + usage |
| patterns used and success rates | pattern_entries |
| token drift warnings | design token report |
| gate failures by gate number | visual_gate_audits |
| missing local/live evidence | README/LIVE-WEB file |

The report makes it possible to decide whether the next phase should generate more images, repair gate failures, consolidate tokens, or backfill prompt bodies.

## 17. Cross-module anti-corruption rules

- `quality_score` cannot update `five_gate_audit_passed`.
- `pattern success_rate` cannot update asset state.
- `prompt output_quality_score` cannot make a prompt default if boundary lint fails.
- `design-tokens.json` cannot edit React files.
- `visual_asset.locked` cannot approve runtime, migration, vault write, or capture state.

These rules are simple, but they prevent most semantic overreach.


## 18. Contract invariants

The contract has five invariants:

```text
1. A locked visual asset must have a current sha256 match.
2. A locked visual asset must have an explicit all-pass 5-Gate audit.
3. A generated visual asset should link to a prompt or carry a missing-prompt warning.
4. A pattern-tagged asset should resolve to a pattern entry or carry a placeholder warning.
5. No sidecar state can approve ScoutFlow runtime, vault write, migration, or production code.
```

These invariants are simple enough to run before every phase handoff. They also make the package auditable by a future agent without requiring full project context.

## 19. Contract versioning

Start with `u4_contract_version=1`. If a future promotion adds API endpoints, vector search, or production token import, increment the version. Do not mutate v1 semantics retroactively. Historical assets should remain interpretable under the contract version that locked them.


## Appendix B — contract validation checklist

每次 spine DB 变更后运行一个轻量 validator，而不是引入复杂 migration framework。validator 至少检查：`visual_assets.prompt_id` 存在或为空；非空 `pattern_tag` 能在 pattern_library 中找到同 letter；`pattern_library.example_artifacts` 中的 asset_id 均存在；`prompt_templates.superseded_by` 不形成环；`design_token_usages.token_name` 在 `design-tokens.json` 中存在；`locked` visual asset 必须有 `sha256`、dimensions、file_path、5_gate_audit_passed=true。

失败输出必须 machine-readable：

```yaml
CONTRACT_VALIDATION_PASS: false
errors:
  - code: missing_prompt_fk
    table: visual_assets
    id: va_20260507_0101
  - code: token_usage_unknown
    token: color.accent.unknown
```

这个 validator 不写 DB；它只给操作者一个清楚的修复队列。修复仍通过各模块 CRUD，避免一个“全局修复脚本”变成第二 authority writer。


## Appendix C — failure isolation examples

若 thumbnail cron 失败，只有 `visual_assets.thumbnail_status` 进入 `pending` 或 `failed_tool_missing`，prompt_template、pattern_library、design_token 不受影响。若 prompt lineage 缺 body，visual_asset 仍可通过 `prompt_stub` 关联，不阻塞 hash 与 5-Gate。若 design token JSON 校验失败，只冻结 token rebuild，不回滚已存在 asset。这个隔离策略符合 single-writer discipline：每个模块的失败边界清楚，操作者可以逐项修复，而不是让一个缺失 prompt 或一个无效 token 使整个视觉资产库不可查询。
