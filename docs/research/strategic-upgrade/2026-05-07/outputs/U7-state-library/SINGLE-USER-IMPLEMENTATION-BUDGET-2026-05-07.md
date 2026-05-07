---
title: SINGLE-USER-IMPLEMENTATION-BUDGET-2026-05-07
status: candidate / not-authority / not-production-approval
claim_label: ≥95% candidate-spec confidence
request_date_label: 2026-05-07
generated_at_actual: 2026-05-06
write_enabled: false
boundary: spec-only; no apps/** mutation; no screenshots generated
---

# SINGLE-USER-IMPLEMENTATION-BUDGET-2026-05-07

> 口径：本文件是 U7 candidate spec，不是 authority，不批准 runtime、frontend implementation、package install、browser automation、migration、vault true write 或 production 修改。文件名沿用用户 prompt 的 2026-05-07；实际生成环境日期为 2026-05-06。所有 “state” 都是可注册、可审计、可迁移的视觉状态，不等同于当前组件已经有完整可控 props。


## 1. Budget target

U7 must fit a single-user implementation budget: ≤900 total implementation lines and ≤1.5 weeks. The budget below assumes no production apps/** mutation in the spec phase. Actual code lands later only with a separate dispatch.

## 2. Proposed LOC budget

| Component | LOC target | Notes |
|---|---:|---|
| SQLite DDL + seed exporter | 90 | schema, indexes, seed rows, no ORM |
| Python ingest/audit helpers | 420 | CSV ingest, sha256, contrast math, report writer |
| Playwright audit script | 170 | render states, screenshot, collect DOM metrics |
| Tiny React state browser | 270 | filter/select/render state fixtures |
| README/checklist glue | 40 | operator instructions |
| Total | 890 | within ≤900 LOC |

This is tight but realistic if the first implementation avoids full Storybook, hosted visual regression, token pipeline, and complex dashboarding. The core trick is to keep `state_library` rows as data and reuse one browser route for all states.

## 3. Day budget

| Day | Work | Output |
|---:|---|---|
| 0.5 | Read repo state and confirm dispatch boundaries | final implementation plan |
| 1.0 | Create SQLite schema and seed canonical 48 rows | `state-library.sqlite` seeded |
| 1.0 | Build tiny state browser | local route renders states |
| 1.0 | Build PF-V INDEX.csv ingest and screenshot linker | screenshot paths/sha256 linked |
| 1.0 | Build contrast + DOM metrics collector | Gate 4 reports |
| 1.0 | Add spacing/occlusion checks and report schema | Gate 2/3 partial automation |
| 0.5 | Add human review queue | Gate 1/5 queue |
| 1.0 | Run local dry-run on subset and fix false positives | tested subset |
| 0.5 | Documentation, stdout and handoff | operator-ready package |
| 1.0 buffer | source drift, missing PF-V data, viewport surprises | risk reserve |

Total: about 8.5 working days, which fits 1.5 calendar weeks for a focused single-user lane if PF-V screenshots/INDEX are available. If PF-V INDEX is missing, add 1–2 days for manual mapping.

## 4. Scope exclusions that protect budget

Do not include these in U7 v1:

- Storybook installation or hosted Chromatic setup;
- Percy/Loki/Backstop evaluation beyond the live-refresh report;
- production component refactor to expose all state props;
- CI workflow changes;
- package-manager adoption;
- screenshot generation for all 48 states;
- migration of visual_asset schema if U4 is not ready;
- token pipeline or Figma integration;
- dashboard analytics beyond a simple browser table;
- runtime capture, BBDown, ASR, ffmpeg, browser login or vault writes.

## 5. Risk and mitigation

| Risk | Impact | Mitigation |
|---|---|---|
| Components lack fixture props | state browser cannot control all states | use harness wrappers first; refactor later under dispatch |
| Main nav component absent | lower confidence for nav states | mark `main_nav` inferred and route via adapter |
| Strict 8dp grid causes false positives | noisy Gate 2 | use macro 8dp + micro 4dp tokens with warnings |
| Contrast finds muted label failures | Gate 4 fails many states | fix token or record explicit exemption; do not waive silently |
| PF-V screenshot names differ | ingest mismatch | maintain alias map and require INDEX.csv |
| Human review backlog | status stuck at pending | queue by priority; allow failed evidence to remain linked |
| Live web unavailable | evidence report incomplete | keep downgraded file until browser-enabled refresh |

## 6. Minimal implementation order

1. Seed canonical 48 states.
2. Build browser route from seed JSON.
3. Add screenshot linker but do not require screenshots.
4. Add contrast validator and run on two states.
5. Add spacing/occlusion metrics.
6. Add human queue.
7. Only then connect PF-V bulk import.

## 7. Single-user operating mode

The package should be usable by one operator without a large CI platform. Local commands should be few:

```bash
python tools/u7_seed_state_library.py --db state-library.sqlite
npm run dev --workspace apps/capture-station
python tools/u7_ingest_pfv_index.py --index PF-V-P2/INDEX.csv --db state-library.sqlite
python tools/u7_gate_audit.py --db state-library.sqlite --state url_bar.full.manual_url_ready
```

The first implementation can be docs/spec only; the next dispatch can choose whether the scripts live under `tools/` or a visual prototype folder. Keep package policy and apps/** restrictions intact.


## 8. What “≤900 LOC” includes and excludes

Included:

- seed data and schema exporter;
- PF-V CSV ingest;
- sha256 calculation;
- contrast math;
- DOM metric collection wrapper;
- simple React browser;
- markdown summary exporter.

Excluded:

- generated state JSON rows;
- generated markdown reports;
- screenshots;
- SQL migration files if a later dispatch decides schema ownership separately;
- tests beyond a minimal handful of math/ingest tests.

Counting generated rows as LOC would punish the project for having a complete state matrix. Count only maintained implementation code.

## 9. Minimal test budget

Even a small implementation needs tests:

| Test | LOC | Purpose |
|---|---:|---|
| contrast math | 30 | protect ratios and thresholds |
| state id generation | 20 | stable slugs |
| CSV alias mapping | 30 | prevent panel drift |
| missing screenshot handling | 30 | deferred evidence path |
| human queue status rule | 40 | no auto-pass subjective gates |
| total | 150 | can fit inside Python helper budget if concise |

If LOC pressure becomes severe, keep contrast and human queue tests first. Those are the highest-trust boundaries.

## 10. Implementation slices

Slice 1: **Registry only**. Seed 48 rows, query them, export JSON. No browser, no screenshots.

Slice 2: **Browser render**. Add React browser and route state rows to components/adapters.

Slice 3: **PF-V ingest**. Link existing screenshots, compute sha256, mark missing evidence.

Slice 4: **Machine audit**. Contrast, spacing and occlusion reports.

Slice 5: **Human review**. Queue, review template and final status calculation.

Each slice is useful alone. If time runs out, stop after the latest slice and report exactly what is missing.

## 11. Budget pressure warning signs

- Adding full Storybook before proving tiny browser.
- Adding a token pipeline before fixing the obvious muted contrast risk.
- Trying to refactor all components to accept fixture props in v1.
- Building a dashboard when a table and filters are enough.
- Running every viewport and every screenshot before validating two states.
- Attempting U4 schema mutation without knowing current U4 DDL.

These moves are not bad in the long term, but they break the 1.5-week target.

## 12. Single-user success metric

Success is not “a perfect visual QA platform”. Success is:

```text
Given a state_id,
I can render or locate its screenshot,
see whether objective gates passed,
see whether human hierarchy/weight review is pending or done,
and know exactly which boundary claims are still blocked.
```

That is enough to improve PF-V immediately without turning U7 into a large product.


## 13. Review checkpoints

Set three checkpoints:

1. **Registry checkpoint**: 48 rows exist; no screenshots required.
2. **Evidence checkpoint**: PF-V screenshots link to rows with sha256.
3. **Quality checkpoint**: Gate 4 reports exist and human queue is populated.

Each checkpoint can be reviewed independently. This prevents a single large “done/not done” cliff.

## 14. Budget fallback plan

If the budget gets cut further, keep only:

- SQLite schema;
- canonical 48 seed rows;
- PF-V ingest dry-run;
- contrast math;
- human review queue scaffold.

Drop spacing/occlusion automation temporarily. Gate 2 and Gate 3 can be manual checklist until the next dispatch. Do not drop contrast or human gate separation because those are core trust requirements.

## 15. Maintenance cost

After v1, maintenance should be light:

- add new state row when a component gains a state;
- refresh screenshots when source changes;
- re-run audit after token/layout changes;
- clear human queue after PF-V batches;
- update live-web evidence only when adopting a new vendor/tool.

This fits a single-user workflow because most actions are row/report updates, not platform administration.


## 16. Definition of done for v1

V1 is done when:

- 48 canonical rows are queryable;
- at least one state per panel can be rendered or marked with honest adapter/inferred status;
- PF-V ingest dry-run can parse INDEX.csv;
- contrast validator can identify the known muted-label failure;
- human queue prevents Gate 1/Gate 5 auto-pass;
- README stdout reports any missing live web or screenshot evidence.

V1 is not required to have all screenshots, all human reviews or full CI.

## 17. Expected cost if Storybook is adopted early

Early Storybook adoption likely adds setup, config, story generation, addon decisions and visual regression integration. That can easily consume 2–4 extra days before any state evidence improves. Therefore Storybook should be a v1.5/v2 option unless the user explicitly prioritizes component-doc platforming over lean state registration.
