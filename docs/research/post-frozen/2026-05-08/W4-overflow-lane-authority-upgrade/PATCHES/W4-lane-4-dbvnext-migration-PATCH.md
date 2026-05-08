---
title: W4 Lane 4 (dbvnext_migration) Patch — §0.5 B-lane sanity lane-specific
status: candidate / patch
authority: not-authority
created_by: gpt-pro
parent_cluster: W4
parent_lane: dbvnext_migration
created_at: 2026-05-08
upstream_finding: "audit catch — 5 lane §0.5 B-lane sanity / §5.7 amend_trigger paragraph clone, lane 4 缺 lane-specific verify"
disclaimer: 真态数字以 GitHub live main HEAD 为准; 撰写时刻数字仅为历史参考。
prerequisite_check: drift_detected
main_head_drift: "GitHub live main HEAD = 45e88d4; START-HERE 已刷新到 45e88d4 语境；docs/current.md 与 docs/decision-log.md 的主锚仍停在 e18d45a"
active_product_count: "0/3 (refreshed at §0.5 Check)"
authority_writer_count: "0/1 (refreshed at §0.5 Check)"
wave_state: "WAVE_6_CANDIDATE_OPEN / NOT_EXECUTION_APPROVED"
write_enabled: false
memory_batch_count: 17
deliverable_type: patch
target_replacement_section:
  - "§0.5 B-lane sanity row"

---
# Lane 4 Patch — dbvnext_migration

> State: candidate / patch / not-authority / not runtime approval / not migration approval / not lane unlock.

## §0.5 Prerequisite Check

| Check | Live readback | Result |
|---|---|---|
| GitHub / origin/main | `45e88d4` / PR #257 merge commit | 本 patch 的 prerequisite truth 以此为准 |
| docs/00-START-HERE.md | `last_refreshed_from_main_sha: 45e88d4`; auto anchor chain = `45e88d4 ← 3cbe79e ← ca8593a` | START-HERE 已刷新到 45e88d4 语境 |
| docs/current.md | reports `main = e18d45a`, Active `0/3`, Authority writer `0/1`, `WAVE_6_CANDIDATE_OPEN / NOT_EXECUTION_APPROVED`, `write_enabled=False` | main-head drift remains in `current.md`; authority counts match |
| docs/task-index.md | Active table empty, Review empty, Backlog empty; product lane `0/3`, authority writer `0/1` | matches prompt authority state |
| docs/decision-log.md | current authority file reachable; top rebase record still anchors `origin/main = e18d45a`; repo search confirms PR #246/D-017 references exist on main | decision history usable; main-head drift remains in decision-log wording |
| docs/memory/INDEX.md | `batch_count: 17`, 7 lessons + 5 feedback + 5 patterns | matches prompt |
| GitHub commit chronological | latest returned commit is `45e88d4` / PR #257 W4-B Step0 convergence merge | drift vs `current.md` / `decision-log.md` anchor `e18d45a` |

**prerequisite_check = `partial_refresh_applied`**. Main-head truth in this packet is `45e88d4`. `docs/00-START-HERE.md` has been refreshed into that context, while `docs/current.md` and `docs/decision-log.md` still narrate `e18d45a` as their last authority-rebase anchor. This patch records the post-refresh truth for Codex / CC0 intake without widening lane scope.

## §0.5 B-lane sanity — lane-specific replacement

| Sanity item | Lane 4 live-specific check | Required readback before any lane work |
|---|---|---|
| Migration baseline | Current migration baseline has `001_phase1a_capture_creation.sql` and `002_phase1a_jobs_receipt.sql` only in the prompt/live readback scope | Do not create, rename, reorder, squash, or “repair” migration files in this patch |
| Current adopted path | `services/api/scoutflow_api/storage.py::_init_schema()` 按文件名顺序读取 `services/api/migrations/*.sql`; live scope 内仍只有 001/002 | 本轮 adopted path 明确记录为 manual SQL + storage.py loader; 不新增 SQL, 不修改 loader |
| Forbidden path | `services/api/migrations/**` is explicitly forbidden in current authority unless a new dispatch + user authorization + separate PR + external audit exists | Lane 4 patch may write candidate upgrade rules only; no SQL migration body |
| Alembic 工具状态 | ⚠️ 假锚点修正 (CC0 post-audit fix): `services/api/alembic.ini` 在 ScoutFlow live 真态**未实例化** (verify: `find ScoutFlow -name 'alembic*' → 0 hit`). 这是历史建议里的假前置，不是当前执行基线。 | 本轮只允许把 Alembic 记录为 deferred candidate / historical suggestion；若未来要引入，必须另立 toolchain 评估与 migration PR，不能作为 lane 4 spec 先决条件 |
| DTO freeze | `PlatformResult`, `WorkerReceipt`, and Trust Trace DTO are locked and cannot be mutated as convenience for DB vNext | Any DTO collision stops and routes to separate design/audit |
| Referential integrity | DB vNext must preserve capture/job/artifact relationships and idempotency; current schema has capture, artifact_assets, jobs, job_events | Future migration must prove RI and rollback before land |
| Upgrade path | Master spec §16.2 path G is the legal route: explicit migration dispatch + dry-run evidence + rollback plan + external audit | Lane 4 cannot self-unlock by patching clone text |

### Lane 4 B-lane sanity verdict

Lane 4 begins `candidate / migration_forbidden / requires explicit dbvnext_migration gate`.
Its current adopted path remains manual SQL + `storage.py` loader.
Alembic stays deferred candidate only.
It may prepare a migration-readiness checklist, schema-drift detector, rollback criteria, and DTO-collision matrix. It may not write SQL, require Alembic, or alter Pydantic/DTO shapes in this patch.

## §5.7 amend_and_proceed

Lane 4 §5.7 is intentionally **not replaced** by this patch. The upstream finding says Lane 4 §5.7 is already lane-specific around schema drift, referential-integrity failure, rollback uncertainty, and DTO collision. CC0 should keep that section and only replace the cloned §0.5 sanity row.

## Self-flag

1. ⚠️ I verified the two baseline migration filenames from live reachable files, but I did not inspect `services/api/alembic.ini` because it was not necessary for this patch body; Codex should verify locally before any future migration lane.
2. ⚠️ Lane 4 §5.7 is deliberately left unchanged per task instruction; this file is a partial patch by design.
3. ⚠️ “Path G” label is prompt/master-spec-derived and should be exact-checked by CC0 before final land.
