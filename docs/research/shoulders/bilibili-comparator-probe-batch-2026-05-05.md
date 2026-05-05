---
title: ScoutFlow Bilibili Comparator Probe Batch
date: 2026-05-05
type: shoulder-probe-batch
status: candidate / research-only / not-authority / not-runtime-approval
wave: 3B
related_task: T-P1A-052
---

# ScoutFlow Bilibili Comparator Probe Batch

## Scope

- This dispatch probes the first low-risk Bilibili comparator shoulder after the scan lane locked `BBDown` as the primary route.
- Comparator work here is limited to field discovery, parser-drift contrast, and reference-only fallback analysis.
- This report does not approve runtime replacement, Python import, media download, or credential-bearing flows.

## Inputs

- The scan lane locked the comparator role as `field discovery + parser drift monitoring + reference fallback`, not a `BBDown` replacement lane ([docs/research/shoulders/bilibili-comparator-scan-2026-05-04.md:L13-L23](docs/research/shoulders/bilibili-comparator-scan-2026-05-04.md), [docs/research/shoulders/bilibili-comparator-scan-2026-05-04.md:L36-L40](docs/research/shoulders/bilibili-comparator-scan-2026-05-04.md)).
- The current BBDown baseline exposed five minimum metadata fields that any comparator must be judged against: `platform_item_id`, `title`, `duration_seconds`, `page_count`, and `selected_page` ([docs/research/t-p1a-011c-bbdown-auth-present-info-probe-report-2026-05-04.md:L34-L44](docs/research/t-p1a-011c-bbdown-auth-present-info-probe-report-2026-05-04.md)).
- The clone plan and tracked mirror show `yt-dlp` as the only live comparator clone in the first cap-4 batch, while `Nemo2011/bilibili-api` stays reserve-only ([docs/research/shoulders/clone-plan-2026-05-05.md:L24-L31](docs/research/shoulders/clone-plan-2026-05-05.md), [docs/research/shoulders/referencerepo-index-2026-05-05.md:L15-L21](docs/research/shoulders/referencerepo-index-2026-05-05.md)).
- The earlier Wave 3B probe already surfaced the strongest `yt-dlp` field-ceiling evidence ([docs/research/shoulders/shoulders-probe-batch-1-2026-05-05.md:L85-L104](docs/research/shoulders/shoulders-probe-batch-1-2026-05-05.md)).

## Batch verdict

| shoulder | decision | integration proposal | confidence | next_action |
|---|---|---|---:|---|
| `BILIBILI-COMPARATOR / yt-dlp` | continue | `reference_only comparator` | 0.88 | keep as field-ceiling and drift-contrast baseline |

## Probe findings

### shoulder BILIBILI-COMPARATOR / yt-dlp

Decision: keep `yt-dlp` as the primary Bilibili comparator shoulder for field ceiling and multi-part drift explanation, without turning it into the main ScoutFlow runtime route.

Why:

- The scan lane already ranked `yt-dlp` as the strongest low-risk comparator because it is active, license-light, and rich in structured extractor output ([docs/research/shoulders/bilibili-comparator-scan-2026-05-04.md:L52-L60](docs/research/shoulders/bilibili-comparator-scan-2026-05-04.md), [docs/research/shoulders/bilibili-comparator-scan-2026-05-04.md:L64-L104](docs/research/shoulders/bilibili-comparator-scan-2026-05-04.md)).
- The tracked mirror confirms the local-only clone exists at `referencerepo/bilibili/yt-dlp/` with commit `35684c1171dd` ([docs/research/shoulders/referencerepo-index-2026-05-05.md:L19-L21](docs/research/shoulders/referencerepo-index-2026-05-05.md)).
- The local extractor uses `/x/player/pagelist` and builds playlist-like multi-part entries, which maps directly to ScoutFlow's `page_count` / `selected_page` questions ([referencerepo/bilibili/yt-dlp/yt_dlp/extractor/bilibili.py:L701-L714](referencerepo/bilibili/yt-dlp/yt_dlp/extractor/bilibili.py:L701-L714), [referencerepo/bilibili/yt-dlp/yt_dlp/extractor/bilibili.py:L720-L723](referencerepo/bilibili/yt-dlp/yt_dlp/extractor/bilibili.py:L720-L723)).
- The same extractor emits `tags`, `view_count`, `comment_count`, `chapters`, `subtitles`, and `extract_comments(aid)`, so it is the best single shoulder in this batch for understanding what sits above BBDown's current minimum metadata plane ([referencerepo/bilibili/yt-dlp/yt_dlp/extractor/bilibili.py:L733-L747](referencerepo/bilibili/yt-dlp/yt_dlp/extractor/bilibili.py:L733-L747), [referencerepo/bilibili/yt-dlp/yt_dlp/extractor/bilibili.py:L825-L831](referencerepo/bilibili/yt-dlp/yt_dlp/extractor/bilibili.py:L825-L831), [referencerepo/bilibili/yt-dlp/README.md:L1348-L1356](referencerepo/bilibili/yt-dlp/README.md:L1348-L1356)).
- That extra surface is useful precisely because BBDown's live proof path is still narrower and centered on metadata-only capture evidence, not because ScoutFlow should swap routes now ([docs/research/t-p1a-011c-bbdown-auth-present-info-probe-report-2026-05-04.md:L24-L44](docs/research/t-p1a-011c-bbdown-auth-present-info-probe-report-2026-05-04.md), [docs/research/t-p1a-011c-bbdown-auth-present-info-probe-report-2026-05-04.md:L77-L89](docs/research/t-p1a-011c-bbdown-auth-present-info-probe-report-2026-05-04.md)).

Carry-forward:

- Keep `yt-dlp` as the first comparator probe result and long-term field-ceiling reference.
- Use it to explain parser drift or missing fields, not to bypass the current `BBDown locked` route.

## Reserve note

- `Nemo2011/bilibili-api` remains reserve-only in this batch because the tracked mirror still marks it `pending`, not cloned ([docs/research/shoulders/referencerepo-index-2026-05-05.md:L20-L21](docs/research/shoulders/referencerepo-index-2026-05-05.md)).
- The scan lane keeps `Nemo2011/bilibili-api` in the pool as a richer site-native semantic comparator, but only under `reference_only` and `subprocess only` assumptions because of GPL and credential-surface concerns ([docs/research/shoulders/bilibili-comparator-scan-2026-05-04.md:L106-L149](docs/research/shoulders/bilibili-comparator-scan-2026-05-04.md)).

## Result

This batch keeps the Bilibili comparator conclusion narrow and defensible:

- `yt-dlp` is the live comparator shoulder
- `Nemo2011` stays reserve-only
- the comparator lane serves BBDown contrast, not replacement
