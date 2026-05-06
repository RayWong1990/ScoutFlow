# PF-C1-12 — C1 closeout and C2 go/no-go

```yaml
status: candidate_task_draft_not_authority
pack: PF-C1-proof-pair-pack
cluster: PF-C1
dispatch_class: handoff
open_after_state: preview_only_localhost_ready
proof_kind: human_verdict
human_gate: usefulness_verdict
can_parallel: no
serial_gate: human C2 go/no-go
```

## 0. Frozen historical boundary

Dispatch126-176 are frozen historical assets/evidence. Do not reopen, reorder, or re-execute them.

This task may inherit ideas or evidence from frozen historical work, but it must not reopen, reorder, or re-execute old dispatches.

## 1. Goal

Keeps successor work bounded and prevents old candidate truth from becoming execution truth.

## 2. Expected output

`authority surfaces optional`

## 3. Dependencies

- PF-C1-10

## 4. Allowed paths

- `docs/current.md`
- `docs/task-index.md`
- `docs/decision-log.md`
- `docs/specs/contracts-index.md`

## 5. Forbidden paths / claims

- `services/api/migrations/**`
- `workers/**`
- `packages/**`
- `data/**`
- `referencerepo/**`
- `raw credentials`
- `true vault write`

## 6. Blocked claims that remain blocked

- `no_true_vault_write`
- `no_runtime_approval`
- `no_browser_automation`
- `no_migration`
- `no_ASR`
- `no_BBDown_live`

## 7. Enter condition

- The task's `open_after_state` is satisfied.
- The pack's stop-lines are still intact.
- The task does not depend on unapproved runtime, migration, true vault write, or browser automation.

## 8. Pass condition

Only opens C2 when C1 pass or strong partial is accepted by human gate.

## 9. Partial pass condition

- The output exists and is useful, but the named proof_kind or human gate is not yet satisfied.
- The task remains blocked from promoting downstream work until the missing proof is completed.

## 10. Fail condition

- The task claims proof from docs-only output, placeholder data, fixture-only data, dry-run-only data, or checklist-only visual review.
- The task expands scope beyond its allowed paths.
- The task weakens any blocked claim.

## 11. Kill signal

Immediate stop if this task attempts to enable true write, runtime tools, browser automation, migrations, or reopens Dispatch126-176.

## 12. Validation baseline

```bash
python tools/check-docs-redlines.py
python tools/check-secrets-redlines.py
git diff --check
```

Add code-specific tests when the task touches app or service code.

## 13. What this task does NOT prove

- It does not prove RAW handoff unless proof_kind is `raw_intake` or `script_seed`.
- It does not prove visual quality unless proof_kind is `screenshot_visual` and human gate passes.
- It does not approve true vault write, runtime execution, or migrations.
