---
title: PF-C1 Canary URL Pack
status: candidate / proof-prep / not-authority
created_at: 2026-05-06
related_dispatch: PF-C1-01
proof_kind: real_url_preview
human_gate: URL_selection
---

# PF-C1 Canary URL Pack

## Purpose

Lock the three user-selected canary URLs for `PF-C1` so downstream proof work stays bounded and does not expand into bulk URL sampling.

## Canonicalization Rule

- Strip query strings such as `spm_id_from` and `vd_source`.
- Keep only the canonical bilibili video URL.
- Do not add search-result URLs, short links, or a second expansion pool in this dispatch.

## Locked Canary Set

| Slot | Class | Original URL | Canonical URL | Why this slot exists |
| --- | --- | --- | --- | --- |
| `URL-1` | `ordinary` | `https://www.bilibili.com/video/BV16ooQBsEah/?spm_id_from=333.337.search-card.all.click` | `https://www.bilibili.com/video/BV16ooQBsEah/` | Normal-density baseline. Used to check whether the preview-to-topic-card path is useful even when the source is not obviously premium. |
| `URL-2` | `edge` | `https://www.bilibili.com/video/BV1zhoUB1Ebg/?spm_id_from=333.337.search-card.all.click&vd_source=4be6ac946264764a925966c890c00b25` | `https://www.bilibili.com/video/BV1zhoUB1Ebg/` | Edge-case probe. Used to surface weak metadata, noisy preview shape, or over-objectification risk. |
| `URL-3` | `high-signal` | `https://www.bilibili.com/video/BV1A196BpESQ/?spm_id_from=333.337.search-card.all.click&vd_source=4be6ac946264764a925966c890c00b25` | `https://www.bilibili.com/video/BV1A196BpESQ/` | Follow-worthy candidate. Used to test whether the topic-card-lite form can preserve obvious human usefulness without claiming product proof too early. |

## Boundary

- This file records a bounded canary pack only.
- It does not prove runtime approval, RAW handoff, visual quality, true vault write, or C1 usefulness verdict.
- `PF-C1-11` may introduce at most two replacement URLs later, but only if `PF-C1-10` records `partial`.
