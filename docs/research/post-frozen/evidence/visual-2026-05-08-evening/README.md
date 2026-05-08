---
status: reference storage
authority: not-authority
applicable_round: master 手顺 v3 Round 4 (战友 localhost V-PASS) + Round 5 (Opus-3 visual re-audit input)
artifact_role: manual-helper / docs-only / candidate
not_approval:
  - not browser automation approval
  - not Playwright/Selenium/Puppeteer install approval
  - not runtime approval
  - not true write approval
---

# Visual Evidence Packet — 2026-05-08 Evening Sub-wave

## 目的

战友在 Lane A merged 后 (Round 4), 按 9 步 manual script 跑 localhost, 把 notes + screenshot (可选) 放入本目录, 供 Opus-3 (Round 5) 视觉再审 + 未来 V-PASS receipt.

⭐ Manual only. 不准引入 Playwright / Selenium / Puppeteer / 任何 browser automation. `browser_automation` 仍是 5 overflow Hold 之一.

## 9 步 manual script (按 Opus-2 §5 + GPT Pro C LOCALHOST-REVIEW-POINTS)

跑前条件:
- Lane D code-bearing PR + Lane A T-P1A-160 PR 都 merged
- 本地 ScoutFlow main 已拉最新, `pnpm --dir apps/capture-station test/lint/typecheck/build` 全过
- 战友手动启动 dev server (`pnpm --dir apps/capture-station dev`)
- 浏览器手开 localhost (Chrome / Firefox / Safari 任一)

### 9 步 (战友逐项检查 + 写 notes + 可选截图):

1. 打开当前 branch 的 AppShellOverview/single-flow 入口, 输入 1 个真实 Bilibili canonical URL, 看 `创建采集` 从 idle → ready → success 的切换是否符合 Lane D 9 态 token (empty/loading/disabled/blocked/preview/committed/failed/partial/skipped).
2. 创建 capture 后, **不切页**, 同屏内确认能否说明 `discover / metadata_fetch / trust_trace / preview / write gate`. 若仍需跨 surface 拼真相 → fail (VT-P1-01 未修).
3. 打开 Trust Trace surface, 检查 idle / route error / 下游 blocked 三种状态. 顶部 badge **绝不能** 因为 route 成功就显示蓝色 ready (VT-P0-01 验证).
4. 打开 Vault Preview surface, 检查 `preview_pending / preview_loaded / preview_disabled / route_error`. 任何 preview-only 都不能出现 success green 或 committed-like cue (VT-P0-03 验证).
5. 打开 Vault Commit surface, 检查 `Run dry-run check` 与 `Commit to vault (disabled)`. `committed=false` 绝不能被绿色成功 footer 包装 (VT-P0-03 验证).
6. 打开 Topic Card Vault 和 Capture Plan, 检查"真实写入仍 blocked"是否被画成 blocked (HoldBanner), 而不是 pending / loading (VT-P0-02 验证).
7. 检查是否存在真正的 RewriteOutputV1 preview surface (`features/rewrite-output/`). 若不存在 → 直接 fail (VT-P1-02 未修).
8. 用长 transcript / 长 safe field / 长 path 做一轮极端输入, 确认不会把 Trust Trace 或 Preview 面板撑爆.
9. 用 mock 3-item 和 mock 10-item batch fixture (若 Codex-Bat-Prep spec 已落); 因为 Storybook 推迟, 此步可仅核验 `batch-manifest-v1-contracts-candidate.md` doc 中 5 final state vocab 在 UI 中是否有占位词或 placeholder (本波 batch row UI 推迟, 是 Phase 3 dispatch 范围).

每步写 1-3 句 notes 到 `round-4/notes.md` (复制 `round-4/notes.md.template` 起手), 标 PASS / WITH_AMENDMENTS / FAIL.

可选: 截图放 `round-4/screenshots/` (文件名 `<step>-<surface>-<state>.png`). 截图必须**不含**真 cookie / token / 私 URL / 私人内容.

## Verdict 写法

跑完 9 步后, 战友复制 `VERDICT-TEMPLATE.md` 到 `round-4/verdict.md` 填:

- `V-PASS` — 9 步全 PASS, 无 blocking 视觉/证据 issue.
- `V-PASS_WITH_AMENDMENTS` — 9 步部分 amendments, 但可在 merge 前修.
- `V-PARTIAL` — 有用但不够作 P3A 证明.
- `V-REJECT` — 不能作 P3A proof.

⭐ Round 5 Opus-3 verdict 必须 V-PASS-CLEAR 才 closeout (master 手顺 v3 §3.5). WITH_AMENDMENTS 自动进 hotfix round.

## 禁忌 (verbatim from GPT Pro C LOCALHOST-REVIEW-POINTS §7)

跑 review 时立即停 if:

- localhost 要求 live external platform 执行
- UI claim commit success
- UI hide write-disabled state
- UI claim transcript / rewrite success without transcript handoff
- 浏览器 automation flow 被提议
- 截图泄露 secret / 私 URL / token-bearing URL

## 不批准

- 不批准 browser automation
- 不批准 Playwright / Selenium / Puppeteer 引入
- 不批准 runtime / true write / migration / DB queue
