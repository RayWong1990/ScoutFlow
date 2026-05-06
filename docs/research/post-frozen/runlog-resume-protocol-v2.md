---
title: Runlog and resume protocol v2
status: candidate / research / not-authority
created_at: 2026-05-06
related_dispatch: PF-GLOBAL-05
---

# Runlog and resume protocol v2

## interruption_classes

| class | meaning | default_action |
|---|---|---|
| `slot_local` | single dispatch or validation issue inside one slot | repair locally and continue |
| `control_plane` | `gh pr create/view/merge` or push flow broke | repair branch/PR state from GitHub truth |
| `ledger` | merge succeeded but runlog/checkpoint did not finish | rebuild receipt from live PR state |

## checkpoint_minimum

```yaml
run_id: required
baseline_sha: required
cursor_dispatch: required
cursor_branch: required
state: running | pushing | pushed_pending_merge | merged | complete
merged_prs: list
interruption_count:
  slot_local: int
  control_plane: int
  ledger: int
last_verified_at: iso8601
```

## resume_steps

1. `git fetch origin --prune`
2. Re-check `origin/main` and current branch head.
3. Reconcile checkpoint with live GitHub PR state.
4. Prefer GitHub truth over local guess if the two disagree.
5. Update checkpoint before the next push attempt.

## guardrails

- Never resume from a checkpoint that lacks `baseline_sha`.
- Never treat `auto-merge enabled` as `already merged`.
- Never write final report before verifying the merged PR list against GitHub.

## verdict

- `T-PASS` means the protocol is usable as a candidate runbook.
