---
title: STEP0 Localhost Preview Dispatch Template
status: candidate / research / not-authority
created_at: 2026-05-06
---

# STEP0 Localhost Preview Dispatch Template

> Use this template for the shortest meaningful localhost loop:
> `manual_url -> create capture -> vault preview markdown -> copy/download`

## 1. Scope

This template is for `preview-only localhost loop`.

It is allowed to connect:

- H5 URL input
- `POST /captures/discover`
- Bridge router mount
- `GET /captures/{capture_id}/vault-preview`
- markdown display
- copy / download `.md`

It is not allowed to unlock:

- true vault write
- BBDown live
- ASR
- `audio_transcript`
- browser automation
- migrations

## 2. Specialized dispatch header

```text
# Dispatch <NN> - <Task ID> <Title>
> Task ID: <T-P1A-NNN>
> Owner Tool: Codex Desktop single writer
> Mode: code-bearing
> Depends On: <none or predecessor>
> Source: preview-only localhost loop
> Dispatch Class: proof_mainline
> Cluster: PF-localhost-preview
> Open After State: successor_entry_ready
> Proof Kind: preview_only
> Human Gate: none
```

## 3. Required behavior checklist

- If backend task:
  - mount missing route group or expose missing API boundary
  - preserve `write_disabled`
  - preserve current blocked lanes
- If frontend task:
  - use real API call, not placeholder state
  - keep blocked language explicit
  - do not imply write/commit happened
- If UX task:
  - support visible preview text
  - support copy
  - support download `.md`

## 4. Minimal pass bar

```text
open localhost
  -> paste bilibili manual_url
  -> click create capture
  -> receive capture_id
  -> fetch vault-preview
  -> render markdown preview
  -> copy or download markdown
```

## 5. Shared stop-lines

- any attempt to enable true write
- any attempt to unlock runtime tools
- any attempt to smuggle browser automation into the mainline
- any change to `services/api/migrations/**`

