---
title: ScoutFlow Wave 3B Shoulders Probe Batch 1
date: 2026-05-05
type: shoulder-probe-batch
status: candidate / research-only / not-authority / not-runtime-approval
wave: 3B
related_task: T-P1A-044
---

# ScoutFlow Wave 3B Shoulders Probe Batch 1

If total shoulders to probe > 4, split into PR69 + PR69b.

## Scope

- This PR probes exactly 4 shoulders from the Wave 3B clone plan.
- All source reads come from local-only shallow clones under `referencerepo/**`.
- No runtime approval, no dependency approval, no tracked clone metadata beyond the tracked mirror.

## Batch verdict

| shoulder | decision | integration proposal | confidence | next_action |
|---|---|---|---:|---|
| `REDNOTE-XHS / iFurySt/RedNote-MCP` | continue | `reference_only -> clone_to_reference -> deeper auth/output probe` | 0.84 | keep as primary XHS read-path baseline |
| `REDNOTE-XHS / ShellyDeng08/rednote-analyzer-mcp` | continue with caution | `reference_only -> clone_to_reference -> isolate discovery from generation` | 0.79 | keep as Python-native contrast; do not inherit generation scope blindly |
| `CONSOLE-CLI / satnaing/shadcn-admin` | continue | `reference_only -> UI/layout clone reference` | 0.82 | keep as first browser H5 console/layout donor |
| `BILIBILI-COMPARATOR / yt-dlp` | continue | `reference_only comparator` | 0.88 | keep as primary comparator for page list + subtitles + chapters + comments field ceiling |

## Why only these four

- The Wave 3B clone plan set a hard cap of four shoulders for this first probe batch.
- `Nemo2011/bilibili-api` and `Kiranism/tanstack-start-dashboard` stay reserve-only to avoid blowing the PR69 cap.
- `OBSIDIAN-FRONTMATTER` stays in the scan/spec lane, not the clone/probe lane.

## Probe findings

### shoulder REDNOTE-XHS / iFurySt/RedNote-MCP

Decision: keep as the primary XHS read-path reference, but hold it at `reference_only` until a later lane proves ScoutFlow can tolerate the login + cookie persistence boundary.

Why:

- The README makes login bootstrap explicit and writes cookies to `~/.mcp/rednote/cookies.json`, which is useful operationally but immediately raises a boundary question for ScoutFlow (`referencerepo/xhs/rednote-mcp-ifuryst/README.md:L25-L26`, `referencerepo/xhs/rednote-mcp-ifuryst/README.md:L67-L72`).
- The manifest confirms a Node/TypeScript CLI package with MCP SDK, Playwright, Commander, Winston, and Zod; that is a credible MCP server/tool surface, but it is still a browser-driven stack rather than a thin pure-HTTP reader (`referencerepo/xhs/rednote-mcp-ifuryst/package.json:L7-L15`, `referencerepo/xhs/rednote-mcp-ifuryst/package.json:L22-L33`, `referencerepo/xhs/rednote-mcp-ifuryst/package.json:L52-L56`).
- The CLI registers search/content/comments tools and returns note/comment fields in text payloads, so the read surface is concrete enough for later shape comparison (`referencerepo/xhs/rednote-mcp-ifuryst/src/cli.ts:L35-L52`, `referencerepo/xhs/rednote-mcp-ifuryst/src/cli.ts:L61-L79`, `referencerepo/xhs/rednote-mcp-ifuryst/src/cli.ts:L89-L105`).
- The auth manager hardcodes the cookie path and creates `~/.mcp/rednote/`, which is workable for a local MCP tool but not something ScoutFlow should silently inherit into tracked/runtime defaults (`referencerepo/xhs/rednote-mcp-ifuryst/src/auth/authManager.ts:L23-L43`).

Carry-forward:

- Keep this repo as the primary XHS read-path reference.
- Future probe should focus on output normalization and auth isolation, not on publish/write features.

### shoulder REDNOTE-XHS / ShellyDeng08/rednote-analyzer-mcp

Decision: keep as the Python-native contrast repo, but split discovery/read-path value from its heavier analysis/generation framing before any adaptation talk.

Why:

- The README and package metadata position it as an MCP server that can search, analyze, and generate RedNote content, which is broader than ScoutFlow's current capture boundary (`referencerepo/xhs/rednote-analyzer-mcp/README.md:L1-L13`, `referencerepo/xhs/rednote-analyzer-mcp/pyproject.toml:L1-L10`, `referencerepo/xhs/rednote-analyzer-mcp/pyproject.toml:L52-L67`).
- The project is Python `>=3.11`, MIT-licensed, and exports both `rednote-analyzer-mcp` and `rednote-login`, so it fits ScoutFlow's language better than the TypeScript winner while still carrying a real login/runtime story (`referencerepo/xhs/rednote-analyzer-mcp/pyproject.toml:L9-L10`, `referencerepo/xhs/rednote-analyzer-mcp/pyproject.toml:L52-L67`).
- The server uses a module-level singleton adapter, supports both `mock` and `playwright`, and explicitly documents the Playwright/browser extra; that is useful for boundary design because ScoutFlow can separate mock/read contracts from live browser fetch later (`referencerepo/xhs/rednote-analyzer-mcp/src/rednote_analyzer_mcp/server.py:L20-L33`, `referencerepo/xhs/rednote-analyzer-mcp/src/rednote_analyzer_mcp/server.py:L36-L63`).
- The Playwright adapter sets a cookie path under `~/.rednote-mcp/cookies.json` and builds in rate limiting (`MIN_REQUEST_INTERVAL_MS`, `MAX_REQUESTS_PER_MINUTE`), which is operationally mature but again too broad to inherit unfiltered (`referencerepo/xhs/rednote-analyzer-mcp/src/rednote_analyzer_mcp/adapters/playwright.py:L42-L49`, `referencerepo/xhs/rednote-analyzer-mcp/src/rednote_analyzer_mcp/adapters/playwright.py:L55-L57`).

Carry-forward:

- Keep it as the Python-native contrast repo.
- Future XHS adapter discussion should explicitly strip out generation/analysis scope and judge only discovery/note-detail/comment surfaces.

### shoulder CONSOLE-CLI / satnaing/shadcn-admin

Decision: keep as the first browser H5 console/layout donor, but treat it as a component/layout reference rather than a full information architecture template.

Why:

- The README states the project is a Shadcn + Vite admin dashboard and explicitly says it is not a starter template, which makes it a strong UI/component donor rather than a prescriptive app shell (`referencerepo/console/shadcn-admin/README.md:L1-L11`).
- Its tech stack locks the exact combination ScoutFlow wanted to probe: Vite, Shadcn, TanStack Router, and a modern component-heavy dashboard surface (`referencerepo/console/shadcn-admin/README.md:L61-L75`).
- The manifest confirms React Query, TanStack Router, React Table, Recharts, Lucide, and Zustand are all in play; that gives ScoutFlow a realistic browser H5 stack sample instead of a marketing demo (`referencerepo/console/shadcn-admin/package.json:L42-L65`).
- `src/main.tsx` shows a concrete `QueryClient` + `createRouter` + `RouterProvider` boot path, which is exactly the kind of app-shell signal the Wave 3B design lanes needed (`referencerepo/console/shadcn-admin/src/main.tsx:L21-L38`, `referencerepo/console/shadcn-admin/src/main.tsx:L51-L80`, `referencerepo/console/shadcn-admin/src/main.tsx:L90-L105`).

Carry-forward:

- Keep it as the primary local-only console clone.
- Do not inherit its sidebar-first IA or auth shell wholesale; borrow component/layout/data patterns only.

### shoulder BILIBILI-COMPARATOR / yt-dlp

Decision: keep as the primary comparator repo for field ceiling and multi-part/media-shape drift detection, without turning it into the primary runtime path.

Why:

- The extractor uses `/x/player/pagelist` and turns multi-part anthologies into playlist-like entries, which is directly relevant to ScoutFlow's `page_count/selected_page` concerns (`referencerepo/bilibili/yt-dlp/yt_dlp/extractor/bilibili.py:L701-L714`, `referencerepo/bilibili/yt-dlp/yt_dlp/extractor/bilibili.py:L720-L723`).
- The same extractor fills `tags`, `view_count`, and `comment_count` in metadata, so it is valuable as a field-ceiling comparator rather than just a downloader (`referencerepo/bilibili/yt-dlp/yt_dlp/extractor/bilibili.py:L733-L747`).
- Return values explicitly include `chapters`, `subtitles`, and `extract_comments(aid)`, which makes it the best single probe in this batch for understanding “what extra structured fields exist beyond BBDown's current minimum” (`referencerepo/bilibili/yt-dlp/yt_dlp/extractor/bilibili.py:L825-L831`).
- The general README metadata docs also call out `comment_count` as an extractor-visible field, reinforcing its usefulness as a comparator/reference surface (`referencerepo/bilibili/yt-dlp/README.md:L1348-L1356`).

Carry-forward:

- Keep `yt-dlp` as the first comparator probe result.
- Keep `Nemo2011/bilibili-api` reserve-only for now so the next decision table can compare “generic extractor ceiling” vs “site-native semantic API surface” without bloating PR69.

## Reserve note

- `Nemo2011/bilibili-api` remains reserve because PR69 is capped at four shoulders.
- `Kiranism/tanstack-start-dashboard` remains reserve because `satnaing/shadcn-admin` already supplied the critical browser H5 stack evidence.
