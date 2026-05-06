---
title: PR #226 / #228 Dual-Coverage Topology Note
status: candidate / receipt-amendment / not-authority
created_at: 2026-05-06
related_dispatches: [PF-LP-06, PF-LP-07, PF-LP-08, PF-LP-11, PF-LP-15]
---

# PR #226 / #228 双覆盖 Topology

## 关系

- `#226` (merged `04a25c3`): initial LP-06/07 preview shell + URL bar bridge
- `#228` (merged `bd1f382`): super-set re-land of LP-06/07 preview shell + extended LP-08/11/15 panel/test/placeholder

## 性质判定

- `#228` 是 replacement / re-land + extension，不是增量 PR
- LP-06/07 final truth source = `#228` (`bd1f382`)
- `#226` 保留为 historical traceability，但 final-state code 由 `#228` 覆盖

## 文件级覆盖关系

- `apps/capture-station/src/layout/FourPanelShell.tsx`: `#226` land -> `#228` 重写并扩展
- `apps/capture-station/src/features/url-bar/UrlBar.tsx`: `#226` 修改 -> `#228` 扩展
- `apps/capture-station/src/features/vault-preview/VaultPreviewPanel.{tsx,test.tsx}`: 仅 `#228` land（LP-08/11）
- `apps/capture-station/src/lib/api-client.test.ts`: 仅 `#228` land（LP-14 coverage）
- `apps/capture-station/src/layout/pf-lp-06-07-dispatch-scope-note.md`: `#228` 写入 scope note，承认双 land
- `apps/capture-station/src/features/vault-preview/pf-lp-08-11-15-dispatch-scope-note.md`: `#228` 写入

## 后续 dispatch 的 truth source 选择

读 LP-06/07 当前实现 -> 读 `bd1f382` (`#228` final state)，不读 `04a25c3` (`#226`)。

## 为什么不 rollback #226

- `#226` 已 merged 进 `main`，rollback 会破坏 git 历史完整性
- `#228` 已是 final-state truth；`#226` historical-only
- 3 窗口外审结论集中在 receipt / traceability，不在 code 风险
