---
title: ScoutFlow Bilibili Comparator Clone Local-only Mirror
date: 2026-05-05
type: shoulder-clone-mirror
status: candidate / research-only / tracked-mirror-only / not-runtime-approval
wave: 3B
related_task: T-P1A-063
---

# ScoutFlow Bilibili Comparator Clone Local-only Mirror

## Scope

- This dispatch mirrors the live Bilibili comparator clone into the canonical local-only metadata surface.
- The result keeps `yt-dlp` as a comparator-only donor and does not reopen runtime, media download, or GPL reserve decisions.
- `referencerepo/**` remains untracked.

## Inputs

- The Bilibili comparator probe already locked `yt-dlp` as the live comparator shoulder and kept `Nemo2011/bilibili-api` as reserve-only ([docs/research/shoulders/bilibili-comparator-probe-batch-2026-05-05.md:L19-L27](docs/research/shoulders/bilibili-comparator-probe-batch-2026-05-05.md), [docs/research/shoulders/bilibili-comparator-probe-batch-2026-05-05.md:L31-L56](docs/research/shoulders/bilibili-comparator-probe-batch-2026-05-05.md)).
- Dispatch 84 repaired the referencerepo structure mirror and carried `capture/YT-DLP` forward as the canonical local-only alias ([docs/research/shoulders/referencerepo-structure-plan-2026-05-05.md:L27-L40](docs/research/shoulders/referencerepo-structure-plan-2026-05-05.md), [docs/research/shoulders/referencerepo-index-2026-05-05.md:L16-L18](docs/research/shoulders/referencerepo-index-2026-05-05.md)).

## Mirror decision

| canonical alias | actual local path | commit | size | metadata result |
|---|---|---|---:|---|
| `YT-DLP` | `/Users/wanglei/workspace/scoutflow-T-P1A-044/referencerepo/bilibili/yt-dlp` | `35684c1171dd` | `18M` | `_SCOUTFLOW_META.local.md` created |

## Why this stays comparator-only

- The existing probe already framed `yt-dlp` as the best field-ceiling and drift-contrast donor, not as a replacement for the locked BBDown route ([docs/research/shoulders/bilibili-comparator-probe-batch-2026-05-05.md:L31-L56](docs/research/shoulders/bilibili-comparator-probe-batch-2026-05-05.md)).
- The tracked mirror confirms the clone is real, small enough for the `<100MB` local-only budget, and already part of the first cap-4 probe wave ([docs/research/shoulders/referencerepo-index-2026-05-05.md:L16-L18](docs/research/shoulders/referencerepo-index-2026-05-05.md)).
- The reserve GPL shoulder remains intentionally un-cloned, so this dispatch does not blur `reference_only comparator` with broader route approval.

## Local-only metadata truth

The local-only file created by this dispatch is:

- `referencerepo/capture/YT-DLP/_SCOUTFLOW_META.local.md`

It records:

- `canonical_alias = YT-DLP`
- the real source path under `.../referencerepo/bilibili/yt-dlp`
- `tracked_in_git = false`
- a note that the donor is comparator-only and the GPL reserve remains outside this mirror file

## Result

Dispatch 88 keeps the comparator mirror narrow:

- `YT-DLP` now has a real local-only metadata anchor
- the donor remains comparator-only
- the GPL reserve still stays out of the live mirror
- no runtime approval is implied
