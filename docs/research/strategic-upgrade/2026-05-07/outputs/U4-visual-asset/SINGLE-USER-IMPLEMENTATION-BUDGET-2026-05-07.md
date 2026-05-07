---
status: candidate / not-authority / not-runtime-approval
created_for: Cloud Prompt U4 Visual Asset Spine
requested_date: 2026-05-07
generated_in_session_date: 2026-05-06
write_enabled: false
claim_scope: spec-only; no production code modification; no dispatch authorization
---

# SINGLE-USER IMPLEMENTATION BUDGET — U4 visual asset spine

> claim label: ≥95% for feasibility estimate under local-first, single-user assumptions; cost excludes paid model usage already happening in PF-V.

## 1. Budget stance

This is a prosumer local-first spine. It should be buildable by one developer in less than a week because it avoids enterprise features: no user management, no cloud media store, no async job queue, no SaaS permission model, no shared review workflow, no browser automation, no production app changes. The implementation budget targets small Python scripts, one SQLite sidecar DB, one cron entry, and one token watch script.


## Source Register / 证据边界

- PRD-v2/SRD-v2 的稳定事实：ScoutFlow 是 single-user、local-first、SQLite + FS + state words 的 authority-first 工作台；当前不得自动批准 SaaS、多用户、runtime 扩张、media/ASR、browser automation、vault true write 或 migration。
- Capture Station 的已读事实：`apps/capture-station/package.json` 是 React 18 + Vite 5，未把 Tailwind/shadcn/Panda/Radix/React Flow/TanStack/Lucide 写成已批准依赖；现有 H5 代码使用深海蓝 palette、inline style、URL Bar + Vault Preview/Dry Run + Live Metadata + Capture Scope + Trust Trace 的工作台结构。
- Visual docs 的已读事实：`design-brief.md` 固定 4 面板扫描顺序；`five-gate-checklist.md` 要求 5 gate 全过才可称 visual pass；`trust-trace-graph-spec.md` 固定 `capture -> capture_state -> metadata_job -> probe_evidence -> receipt_ledger -> media_audio -> audit` 节点链。
- 本地缺口：容器内没有 `~/workspace/ScoutFlow`、没有 `~/.claude/rules/aesthetic-first-principles.md`、没有 PF-V 实际 `INDEX.csv`，因此相关内容均标为 `needs_local_refresh`。
- Live web 缺口：本运行环境禁用实时网页浏览；任何 vendor / 2026 工具状态只能列为待验证 URL 种子，不得写成已访问事实。

## 2. Proposed file map

```text
tools/u4_visual_assets.py          ~240 LOC
tools/u4_prompt_templates.py       ~220 LOC
tools/u4_design_tokens.py          ~180 LOC
tools/u4_pattern_library.py        ~210 LOC
tools/u4_gate_audit.py             ~240 LOC
tools/u4_contract_audit.py         ~160 LOC
visual-assets/schema.sql           ~120 LOC
visual-assets/design-tokens.json   data file
README-u4-local.md                 docs
cron/watch shell snippets          ~40 LOC
```

Estimated implementation code LOC: **~1,250** including scripts and SQL, below the requested 1,500 LOC ceiling. Each module script stays under 300 LOC by avoiding frameworks and avoiding a production API service.

## 3. Development day estimate

| day | work | output | risk |
|---:|---|---|---|
| 0.5 | create schema + DB bootstrap | `u4_assets.sqlite`, schema smoke test | low |
| 1.0 | visual_asset CRUD + thumbnail/pHash | add/list/transition/cron | medium due image formats |
| 0.75 | prompt_template registry + lineage | put/supersede/tree/backfill placeholders | low |
| 0.75 | pattern_library registry | A-J seed/link/use stats | low |
| 0.5 | design token JSON + CSS generator | watch/build CSS outside app | low |
| 0.75 | 5-Gate audit hook + lock guard | audit rows + state guard | medium due visual heuristics |
| 0.75 | PF-V CSV import + contract audit | header introspection + dry-run report | medium due missing actual CSV |
| 0.5 | README + tests | smoke tests + truthful stdout | low |

Total: **4.75 to 5.5 focused dev days**. With interruptions and PF-V backfill surprises, keep a one-week calendar budget.

## 4. Runtime and tool cost

| item | required | estimated direct cost |
|---|---:|---:|
| Python 3 + SQLite | yes | $0 |
| Pillow | yes for thumbnails | $0 open-source dependency |
| imagehash | optional; can inline dHash | $0 |
| cron / launchd | optional | $0 |
| Style Dictionary | optional future | $0 if not installed now |
| GPT/Image/API calls | not required by spine scripts | variable, outside this budget |
| local disk | yes | depends on image volume |

The sidecar spine itself should cost **$0 infrastructure**. Model costs are attributable to PF-V generation, not to the registry implementation.

## 5. Minimal tests

```text
python tools/u4_visual_assets.py init
python tools/u4_visual_assets.py add --kind raw_screenshot --phase PF-V --file sample.png
python tools/u4_visual_assets.py transition --asset-id va_x --state locked  # expected fail before 5-Gate
python tools/u4_prompt_templates.py seed-s00-s18 --placeholder-only
python tools/u4_pattern_library.py seed-a-j --placeholder-only
python tools/u4_design_tokens.py build-css
python tools/u4_contract_audit.py lock-ready --asset-id va_x
```

## 6. Key risk controls

- **Enterprise DAM drift**: no roles, collections, approvals, CDN, cloud sync, brand portal, AI search, or team commenting.
- **YAGNI underbuild**: despite being small, the DB records hash, pHash, prompt, pattern, phase, state, and 5-Gate result; this prevents asset chaos.
- **Production boundary**: scripts write under `visual-assets/` and never edit `apps/capture-station/**`.
- **PF-V uncertainty**: importers run `--dry-run` first and print header mapping before insert.
- **Visual pass honesty**: 5-Gate audit is explicit and blocks `locked`; render pass and visual pass are separate.

## 7. One-week implementation sequence

### Step 1 — Sidecar schema

Create `visual-assets/u4_assets.sqlite` with all tables. Run inserts in a transaction. Use `PRAGMA user_version=1`. Keep schema migrations manual and small.

### Step 2 — Asset intake

Implement `add`, `list`, `show`, `transition`, `thumbs`, `reuse`. The first win is being able to add any PNG/JPEG/SVG and see prompt/pattern/phase fields.

### Step 3 — Prompt and pattern seeds

Seed prompt placeholders and pattern placeholders. The placeholders are intentionally honest: they allow linking while warning that bodies/definitions need backfill.

### Step 4 — Token generator

Store the JSON. Generate CSS into `visual-assets/generated/`. Do not import it into React. Use it for drift reports and prompt injection.

### Step 5 — Gate audit

Implement a CLI that accepts either structured manual audit JSON or heuristic checks. Locking requires all five gates pass. Heuristics may produce warnings, but only explicit pass rows set `five_gate_audit_passed=1`.

### Step 6 — PF-V importer

The importer accepts `INDEX.csv`, normalizes headers, prints a mapping, and supports `--dry-run`. It should import unknown rows as `candidate`, not `locked`.

## 8. Acceptance budget summary

- Code: ≤1,500 LOC total; each module ≤300 LOC.
- Time: ≤1 week calendar; 4.75-5.5 focused days.
- Infra: $0 local sidecar; no hosted service.
- Dependencies: Python stdlib + Pillow; optional imagehash.
- Writes: sidecar only; no production app, services, vault, or authority write.


## 9. Test matrix

| test | command shape | expected result |
|---|---|---|
| schema smoke | `u4 init && sqlite3 .schema` | all tables present, foreign_keys on |
| invalid enum | `add --kind bad_kind` | nonzero exit, no row inserted |
| missing file | `add --file missing.png` | nonzero exit, reason printed |
| duplicate sha | add same file twice | existing row warning or duplicate block |
| lock without gate | `transition --state locked` | fail with gate reason |
| prompt lineage | `prompt lineage pt_s00_v0` | tree output |
| pattern mismatch | asset tag E + linked pattern F | contract audit fail |
| token build | edit JSON then build | generated CSS updated outside app |
| PF-V dry run | `pfv-import --dry-run INDEX.csv` | mapping printed, no writes |
| live web gap | evidence file generated | `live_verified_vendor_count=0` |

## 10. Dependency budget detail

Pillow is the only non-stdlib dependency worth accepting in v0 because thumbnails and dimensions are central to the asset spine. `imagehash` is convenient but optional; a small dHash can be implemented in ~25 LOC using Pillow grayscale/resize. Avoid pandas for the importer unless the CSV becomes messy enough to justify it. The standard `csv` module is sufficient for header-driven mapping.

## 11. Maintenance budget

After initial implementation, expected weekly maintenance should be low:

| activity | frequency | time |
|---|---:|---:|
| import PF-V rows | per visual phase | 10-20 min |
| review lock candidates | per phase close | 30-60 min |
| token drift report | after H5 style work | 5-10 min |
| pattern stats review | weekly during PF-V | 10 min |
| DB backup | weekly | 2 min |

The registry should therefore save time after the first 1-2 phases by reducing repeated image generation and prompt archaeology.

## 12. Backup policy

Because this is local-first, backup is simple but important:

```text
visual-assets/u4_assets.sqlite
visual-assets/design-tokens.json
visual-assets/thumbs/
visual-assets/**/*.png|jpg|svg|webp
```

Back up the DB and files together. A DB without files loses visual truth; files without DB lose lineage. A simple zip snapshot per phase is enough for v0.

## 13. De-scope triggers

If implementation time exceeds one week, cut in this order:

1. Drop optional `pattern_domain_stats` and compute stats on demand.
2. Drop watch mode; keep one-shot token CSS build.
3. Drop pHash and keep sha256 + dimensions first.
4. Drop prompt run cost tracking.
5. Keep 5-Gate lock guard no matter what.

The last point is important: a visual spine without gate honesty would recreate the same confusion the module is meant to fix.


## 14. Why one DB first

A single SQLite file reduces implementation time and avoids cross-database consistency problems. The modules are conceptual modules; they do not need separate storage on day one. If file size or backup policy later demands separation, split after the contract audit has proven stable. Starting split would add friction without helping the single-user workflow.

## 15. Example implementation milestone stdout

```yaml
U4_LOCAL_SPINE_BOOTSTRAP_COMPLETE: true
schema_version: 1
tables_created: 10
scripts_loc_estimate: 1250
sidecar_root: visual-assets/
production_paths_modified: []
next_command: "python tools/u4_visual_assets.py add --file <image> --kind gpt_image_2 --phase PF-V"
```

Every script should print a similar concise result. The user is running high-throughput agent work; stdout clarity matters more than a polished UI for v0.

## 16. Budget realism check

The risky part is not SQLite. The risky part is messy human artifacts: inconsistent filenames, missing prompt bodies, CSV header drift, and ambiguous visual pass claims. The budget remains realistic because the v0 response to ambiguity is not to solve everything; it is to mark placeholders, fail closed, and keep assets in `candidate` until evidence improves. That is cheaper and safer than building broad automation.


## 17. Time-saving payoff

The payoff is not a prettier database. The payoff is avoiding repeated reconstruction. Without U4, each new visual phase asks: which prompt made this, which image passed, which token values were used, which pattern failed, and whether a screenshot was truly reviewed. With U4, those answers are one query away. That saves the most time when the user is running multiple AI agents and many image variants in parallel.

## 18. When to stop building

Stop v0 once add/list/reuse/lock-audit/import-token-build all work. Do not build a UI, embedding search, cloud sync, or DAM-like collection manager until the sidecar proves daily value. The first milestone is operational memory, not polish.


## Appendix A — minimal dependency posture

预算约束不仅是代码行数，也是依赖数量。推荐依赖上限：Python 标准库 + Pillow + imagehash + jsonschema。SQLite 用 stdlib `sqlite3`；CLI 用 `argparse`；cron 用系统 cron 或一个显式 `make visual-cron-once`。不引入 SQLAlchemy、Celery、FastAPI、Redis、S3 SDK 或多用户认证，因为这些都会把 U4 从 prosumer spine 推向 enterprise DAM。

若机器上没有 Pillow/imagehash，脚本应仍能注册 asset，只把 thumbnail/pHash 状态写成 `pending_tool_missing`。这样视觉资产骨架不会因一个本地图像库缺失而停摆。


## Appendix B — cost ceiling note

除 GPT/Image 调用本身外，U4 spine 的本地实现成本应接近零：SQLite、cron、argparse、JSON schema、Pillow/imagehash 都可在本机运行。真正的预算风险来自反复生成图、反复人工审计、以及把工具升级成协作 SaaS。预算控制点不是少建表，而是避免引入上传、权限、团队分享和云存储。
