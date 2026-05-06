---
title: PF-LP-16 Manual Localhost Run Evidence
status: candidate / user_uat_1_evidence / synthetic_partial
date: 2026-05-06
verdict: partial
synthetic_result: works
missing_proof: real_browser_visual_uat
---

# UAT-1 Manual Run Evidence

## Setup

- backend: synthetic uvicorn on `127.0.0.1:8000` with temp db / artifacts / vault rooted under `/tmp/scoutflow-synth-uat-f4M6s2`
- h5: JSDOM-only verification via `pnpm test -- VaultPreviewPanel UrlBar`
- browser: not_started (`curl` + `pnpm test` only; no Playwright / Selenium / Puppeteer / real browser)

## Run trace

- input_url: https://www.bilibili.com/video/BV1WQ9YBNEk6/?spm_id_from=333.1387.homepage.video_card.click&vd_source=4be6ac946264764a925966c890c00b25
- canonicalized_note: BV path canonical form is `https://www.bilibili.com/video/BV1WQ9YBNEk6`; synthetic run kept the original query string in stored preview input
- capture_id: 01KQYEXWJYZ9X8FW7TGD1QW0XP
- markdown_excerpt_lines: 23
- markdown_excerpt_first_3_lines: |
    # ScoutFlow BV1WQ9YBNEk6
    
    ## Capture
- copy_action: success
- download_action: success
- downloaded_filename: scoutflow-preview-01KQYEXWJYZ9X8FW7TGD1QW0XP.md

## Verification notes

- `curl -s http://127.0.0.1:8000/healthz | grep ok` returned `{"status":"ok"}`
- `POST /captures/discover` returned `capture_id=01KQYEXWJYZ9X8FW7TGD1QW0XP`
- `GET /captures/01KQYEXWJYZ9X8FW7TGD1QW0XP/vault-preview` returned a 23-line markdown preview
- `pnpm test -- VaultPreviewPanel UrlBar` passed `22/22`; copy/download actions are classified from the green JSDOM assertions rather than a real browser click

## verdict

- verdict: partial
- synthetic_result: works (`curl` backend probe + JSDOM `22/22` assertions green)
- missing_proof: real_browser_visual_uat (no Playwright / Selenium / Puppeteer / real browser by user authorization)

## blockers

- blockers:
  - real_browser_visual_uat_not_run
