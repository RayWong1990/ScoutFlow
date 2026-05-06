---
title: Commander prompt near-term mainline
status: candidate / research / not-authority
created_at: 2026-05-06
related_dispatch: PF-GLOBAL-02
---

# Commander prompt near-term mainline

## purpose

- Give a future single-writer window one paste-ready frame for the `20-30` near-term mainline budget.
- Keep the prompt anchored on [near-term-execution-matrix-2026-05-06.md](/Users/wanglei/workspace/ScoutFlow/docs/research/post-frozen/near-term-execution-matrix-2026-05-06.md:1), not on stale chat memory.

## paste_ready_slots

| slot | expected_value |
|---|---|
| `baseline_sha` | fresh `origin/main` at paste time |
| `near_term_cap` | `21` under the current matrix |
| `allowed_clusters` | `PF-C0/PF-O1 repaired forms + PF-LP current chain` |
| `blocked_clusters` | `PF-C2`, `PF-C3`, `PF-C4`, `PF-GLOBAL` unless explicitly promoted |
| `blocked_claims` | runtime, true write, migration, browser automation |

## prompt_skeleton

```text
你是 ScoutFlow 单写者，只执行 near-term mainline。
先做 live preflight: git fetch origin --prune, git rev-parse origin/main, cat docs/current.md, cat near-term-execution-matrix-2026-05-06.md。
只从 matrix 中读取 status=near_term_run1 或 near_term_run2 的 dispatch。
任何 reservoir / overflow / later_authority 行默认不进入。
每个 dispatch 只承认 T-PASS | partial | FAIL_ENV | REJECT_AS_X。
一旦发现 docs-only output 被写成 runtime proof, 立即停线。
```

## do_not_say

- Do not say `the pack is ready by default`.
- Do not say `preview proof equals runtime approval`.
- Do not say `PF-GLOBAL support files are automatically near-term`.

## verdict

- This document drafts a future commander prompt shape only.
- `T-PASS` does not open a new execution wave by itself.
