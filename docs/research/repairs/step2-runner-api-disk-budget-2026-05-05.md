---
title: STEP2 Runner API Disk Budget Note
status: candidate
authority: not-authority
execution_approval: not-approved
runtime_approval: not-approved
created_at: 2026-05-05
scope: STEP2A item 2A-6
---

# STEP2 Runner API Disk Budget Note

> State: candidate / not authority / not execution approval.

## 1. Short Verdict

Current evidence does not justify a default STEP3 pool ceiling of `20`.

Recommended practical ceiling:

- start at `10`
- if staged rollout still exists, treat `12` as the evidence-backed upper step
- do not write `10 -> 20` as if it were already validated

## 2. Why

The limiting uncertainty is not disk and not GitHub API rate.

The limiting uncertainty is GitHub runner concurrency, plus the cost of managing many worktrees and CI waits in a repo that already has a non-trivial code-bearing path.

## 3. Verified Facts

- repo is private
- actions permissions are enabled
- branch protection endpoint returns `403`, so no usable positive protection evidence was obtained from API
- GitHub API core budget is healthy
- disk free space is healthy
- worktree count is already high

These facts support:

- API budget is not the first bottleneck
- disk is not the first bottleneck
- runner concurrency and worktree management are the real practical constraints

## 4. STEP3 Caveat

For STEP3 wording, prefer:

```text
recommended_pool_ceiling = 10
staged_rollout = 10 first, then consider 12 after health checks
```

Do not claim:

```text
20 is proven-safe
```

## 5. Evidence Paths

- [docs/current.md](/Users/wanglei/workspace/ScoutFlow/docs/current.md:3)
- [docs/task-index.md](/Users/wanglei/workspace/ScoutFlow/docs/task-index.md:3)
- [.github/workflows/docs-check.yml](/Users/wanglei/workspace/ScoutFlow/.github/workflows/docs-check.yml:1)
