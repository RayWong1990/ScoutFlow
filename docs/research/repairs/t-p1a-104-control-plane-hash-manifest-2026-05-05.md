---
title: T-P1A-104 Control-plane Hash Manifest
date: 2026-05-05
status: research / repair-evidence / hash-manifest-only
related_task: T-P1A-104
supersedes_gap: T-P1A-103 RAW control-plane evidence was local-only and not externally hash-auditable
---

# T-P1A-104 Control-plane Hash Manifest

## Scope

This manifest makes the T-P1A-103 RAW repair package externally auditable without copying RAW file bodies into the ScoutFlow repo.

It records:

- absolute local path
- file existence at verification time
- byte size
- SHA-256 hash
- structural counts for the checkpoint and diff bundle
- local cleanup checks for the temporary T-P1A-103 worktree/branch

It does not store raw stdout/stderr, Hermes config content, cookies, tokens, credential material, or local-only clone contents.

## RAW file hashes

| Artifact | Absolute path | Exists | Bytes | SHA-256 |
|---|---|---:|---:|---|
| final report | `/Users/wanglei/workspace/raw/05-Projects/ScoutFlow/dispatches/REPORT-Wave4-Batch1-Dispatch76-90-CODEX0-2026-05-05.md` | true | 8003 | `ea99775a159da677cc9c0814d3240ef376081207e79e374c9685b3b77be138de` |
| full diff bundle | `/Users/wanglei/workspace/raw/05-Projects/ScoutFlow/dispatches/DIFF-BUNDLE-Wave4-Batch1-Dispatch76-90-2026-05-05.md` | true | 102663 | `4ada350dd5194ecc5a751fd62389a30d641267e92abed7d3aad320d1a44c1d20` |
| local evidence manifest | `/Users/wanglei/workspace/raw/05-Projects/ScoutFlow/dispatches/LOCAL-EVIDENCE-MANIFEST-Wave4-Batch1-Dispatch76-90-2026-05-05.md` | true | 2432 | `2e2a7ff61573b9affef77f727a9969f8659bef0c553ade2e01d6219d07dc5753` |
| archived partial report | `/Users/wanglei/workspace/raw/05-Projects/ScoutFlow/dispatches/archive/REPORT-Wave4-Batch1-Dispatch76-90-CODEX0-2026-05-05.md.partial` | true | 4240 | `531abe1b78166f68680cb84f778eb624e3efe03baa1aa32325424b469e980275` |
| checkpoint | `/Users/wanglei/workspace/raw/05-Projects/ScoutFlow/dispatches/packs/ScoutFlow-PR76-PR125-dispatch-pack-2026-05-05/CHECKPOINT-Wave4-Batch1-Dispatch76-90.json` | true | 13545 | `b3da498ff9f10b63d26a8955e708487761b2d31355ce6a4a4dc7e3533592823d` |

## Structural checks

| Check | Result |
|---|---|
| checkpoint `.run_state` | `completed` |
| checkpoint dispatch rows | `15` |
| checkpoint PR range | `#78` through `#92` |
| checkpoint legacy `commit == head_commit` rows | `15 / 15` |
| diff bundle PR merge sections | `15` |
| stale control-plane phrases | `clear` for `resumed Dispatch 84-90 only`, `baseline family`, and `checkpoint carried forward` |

## Boundary notes

- The full diff bundle is a patch archive. It contains text references to cookie file paths from donor research notes, but not cookie values.
- The local evidence manifest is existence/hash/size oriented and states its own no-secret-copy boundary.
- T-P1A-104 does not make RAW files repo-tracked authority. It gives future auditors a stable hash target for local verification.

## Local cleanup checks

| Check | Result |
|---|---|
| `/Users/wanglei/workspace/ScoutFlow-T-P1A-103` exists | false |
| `git worktree list` contains `T-P1A-103` or `wave4-b1-control-plane` | false |
| `git branch --list '*T-P1A-103*'` returns rows | false |
| root worktree still has unrelated pre-existing dirty files | true; not cleaned by T-P1A-103/T-P1A-104 |

## Reproduction commands

```bash
for f in \
  "/Users/wanglei/workspace/raw/05-Projects/ScoutFlow/dispatches/REPORT-Wave4-Batch1-Dispatch76-90-CODEX0-2026-05-05.md" \
  "/Users/wanglei/workspace/raw/05-Projects/ScoutFlow/dispatches/DIFF-BUNDLE-Wave4-Batch1-Dispatch76-90-2026-05-05.md" \
  "/Users/wanglei/workspace/raw/05-Projects/ScoutFlow/dispatches/LOCAL-EVIDENCE-MANIFEST-Wave4-Batch1-Dispatch76-90-2026-05-05.md" \
  "/Users/wanglei/workspace/raw/05-Projects/ScoutFlow/dispatches/archive/REPORT-Wave4-Batch1-Dispatch76-90-CODEX0-2026-05-05.md.partial" \
  "/Users/wanglei/workspace/raw/05-Projects/ScoutFlow/dispatches/packs/ScoutFlow-PR76-PR125-dispatch-pack-2026-05-05/CHECKPOINT-Wave4-Batch1-Dispatch76-90.json"; do
  test -f "$f" && printf '%s\t%s\t' "$f" "$(wc -c < "$f" | tr -d ' ')" && shasum -a 256 "$f" | awk '{print $1}'
done

jq -r '[.run_state, (.dispatches|length), ([.dispatches[].github_pr]|min), ([.dispatches[].github_pr]|max), ([.dispatches[] | select(.commit == .head_commit)] | length)] | @tsv' \
  /Users/wanglei/workspace/raw/05-Projects/ScoutFlow/dispatches/packs/ScoutFlow-PR76-PR125-dispatch-pack-2026-05-05/CHECKPOINT-Wave4-Batch1-Dispatch76-90.json

rg -c '^## PR #[0-9]+ merge ' \
  /Users/wanglei/workspace/raw/05-Projects/ScoutFlow/dispatches/DIFF-BUNDLE-Wave4-Batch1-Dispatch76-90-2026-05-05.md

git -C /Users/wanglei/workspace/ScoutFlow worktree list | rg 'T-P1A-103|wave4-b1-control-plane' || true
git -C /Users/wanglei/workspace/ScoutFlow branch --list '*T-P1A-103*'
test -d /Users/wanglei/workspace/ScoutFlow-T-P1A-103
```
