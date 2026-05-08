---
title: W4 Lane 3 (browser_automation) Patch — §0.5 B-lane sanity + §5.7 amend_trigger lane-specific
status: candidate / patch
authority: not-authority
created_by: gpt-pro
parent_cluster: W4
parent_lane: browser_automation
created_at: 2026-05-08
upstream_finding: "audit catch — 5 lane §0.5 B-lane sanity / §5.7 amend_trigger paragraph clone, lane 3 缺 lane-specific verify"
disclaimer: 真态数字以 GitHub live main HEAD 为准; 撰写时刻数字仅为历史参考。
prerequisite_check: drift_detected
main_head_drift: "docs/current.md reports c802de4; GitHub chronological latest merge readback is 6dd27d7 / PR #245 W2D memory graph (撰写时刻历史参考, GitHub live 以 §0.5 Check 为准)"
active_product_count: "0/3 (refreshed at §0.5 Check)"
authority_writer_count: "0/1 (refreshed at §0.5 Check)"
wave_state: "WAVE_6_CANDIDATE_OPEN / NOT_EXECUTION_APPROVED"
write_enabled: false
memory_batch_count: 17
deliverable_type: patch
target_replacement_section:
  - "§0.5 B-lane sanity row"
  - "§5.7 amend_and_proceed pattern"

---
# Lane 3 Patch — browser_automation

> State: candidate / patch / not-authority / not runtime approval / not migration approval / not lane unlock.

## §0.5 Prerequisite Check

| Check | Live readback | Result |
|---|---|---|
| docs/current.md | reports `main = c802de4`, Active `0/3`, Authority writer `0/1`, `WAVE_6_CANDIDATE_OPEN / NOT_EXECUTION_APPROVED`, `write_enabled=False` | drift on main-head only; authority counts match |
| docs/task-index.md | Active table empty, Review empty, Backlog empty; product lane `0/3`, authority writer `0/1` | matches prompt authority state |
| docs/decision-log.md | current authority file reachable; tail is tool-truncated, but repo search confirms PR #246/D-017 references exist on main | partial tail visibility; no authority-count drift detected |
| docs/memory/INDEX.md | `batch_count: 17`, 7 lessons + 5 feedback + 5 patterns | matches prompt |
| GitHub commit chronological | latest returned commit is `6dd27d7` / PR #245 W2D memory graph, after PR #248 / PR #247 chronologically | drift vs current.md anchor `c802de4` |

**prerequisite_check = `drift_detected`**. Main-head truth in this packet is: docs authority anchor still says `c802de4`, while GitHub chronological latest merge is `6dd27d7` (撰写时刻历史参考, GitHub live 以 §0.5 Check 为准). This packet does not write authority and does not repair that drift; it only records it for Codex / CC0 intake.

## §0.5 B-lane sanity — lane-specific replacement

| Sanity item | Lane 3 live-specific check | Required readback before any lane work |
|---|---|---|
| Dependency truth | capture-station package surface has React/Vite/Vitest stack and no Playwright / Selenium / Puppeteer dependency in current package.json | Do not add browser automation packages in this patch; any addition requires separate explicit lane gate |
| Use-case truth | Prompt context says Lane 3 currently has no concrete use case; it is a reserved schema/gate, not an implementation need | Default verdict should be abstain/defer until a concrete user story exists |
| Platform ToS risk | Bilibili / 抖音 / 小红书 browser automation is generally high-risk due to bot/captcha/rate-limit patterns | Require platform-specific legal/risk readback before any browser session design |
| Current authority | browser_automation is one of 5 overflow Hold lanes and remains blocked | Do not present screenshots, browser runs, or headless execution as available proof |
| Upgrade path | Master spec §16.2 path F is the legal route: concrete use case + explicit user gate + separate PR + external audit | Lane 3 cannot be bootstrapped by W2C visual need alone |
| Evidence posture | Visual/screenshot evidence is allowed only when separately approved and redacted; absence must be explicit | No fake V-PASS or hidden screenshot gap |

### Lane 3 B-lane sanity verdict

Lane 3 should be marked `candidate / abstain_until_use_case / requires Hermes pre-review`. The default action is to defer, not to build. If a future need appears, it must be framed as a concrete one-sentence use case and pre-reviewed before package/runtime decisions.

### Suggested §1.4 lane trade-off replacement

`Lane 3 remains intentionally deferred until a concrete browser-automation use case appears. Generic visual review, screenshot convenience, or “nice to have” browsing is insufficient. Once a use case exists, run Hermes pre-review for ToS / bot / captcha / rate-limit risk before any Codex implementation prompt.`

## §5.7 amend_and_proceed — lane-specific replacement

### Amend trigger matrix

| Trigger | Lane-specific detection | Required action | Hard stop reason |
|---|---|---|---|
| Use case absent | lane prompt lacks exact site/action/user value or only says “browser automation capability” | STOP with abstain verdict; do not implement | no actionable consumer within 24h means over-engineering |
| ToS / anti-bot drift | platform terms, robots, captcha, rate-limit, auth-wall, or anti-scraping signal changes | STOP; require platform risk refresh + Hermes review | legal/platform posture determines whether lane can exist |
| Bot license ambiguity | package/tool license or headless-bot interpretation is uncertain | STOP; write license ambiguity receipt | dependency/license uncertainty cannot be patched mid-lane |
| Captcha / rate-limit spike | any probe hits captcha, account lock, IP throttle, or repeated 429/403 | STOP; no retry loop; record safe summary only | repeated probes raise risk and may contaminate accounts |
| Credential/profile contamination | browser profile, cookies, local storage, session tokens, or auth sidecars enter repo/evidence | STOP; quarantine; redaction review | credential material is never evidence |
| Visual evidence overclaim | screenshot gap is rewritten as terminal V-PASS or product UI approval | STOP; correct claim labels before continuation | visual proof cannot be fabricated by wording |

### Amend rule

Lane 3 should not use amend-and-proceed for runtime/browser risk. It may only amend documentation to say “deferred / no use case / not approved.” Any actual browser automation requires explicit user gate plus cross-vendor audit.

### Receipt requirements

- Receipt path: `docs/research/post-frozen/W4/lane-3/receipts/<timestamp>-browser-automation-abstain-or-trigger.md`.
- Required fields: concrete use case, platform, action, risk trigger, credential exposure status, captcha/rate-limit status, reviewer needed.
- Forbidden fields: browser profile path, cookie/localStorage/session content, screenshots containing private data, raw browser logs.

## Self-flag

1. ⚠️ I intentionally recommend abstain/defer for Lane 3 because the prompt says there is no current use case.
2. ⚠️ ToS risk language is conservative and should be refreshed by Hermes or human review before any real browser lane.
3. ⚠️ This patch does not say screenshot automation is impossible; it says it is not approved by W2C/W4 clone repair.
