---
name: runtime-approval-drift
description: metadata probe / parser repair / bounded H5 evidence 不自动批准 live runtime / media download / ffmpeg / ASR
type: project
source_atlas_node: L-RUNTIME-APPROVAL-DRIFT
cross_vendor_readers: [cc0, cc1, codex, gpt-pro, hermes]
risk_if_forgotten: critical
cross_session_count: 14
status: current authority
---

# Runtime approval drift

metadata-only probe / parser fix / H5 静态壳 / Bridge preview / Vault preview 等任何 bounded evidence **不自动**解禁 live runtime (BBDown live / yt-dlp / ffmpeg / ASR / browser automation / vault true-write / DB migration / frontend hot-fix). 5 overflow lane 永远独立 gate.

**Why:** ScoutFlow `bridge/config.py:24,36` 硬编 `write_enabled=False`, 5 overflow lane (true_vault_write / runtime_tools / browser_automation / dbvnext_migration / full_signal_workbench) 全 Hold. 历史多次出现 "B2 preflight 关闭 → 推断 frontend 已批" / "PRD-v2.1 promoted → 推断 BBDown live 已批" 的滑坡.

**How to apply:** 任何 lane 启动前显式 readback `docs/current.md` "当前禁止" 段. PR / dispatch / commander prompt 必须明文区分 "metadata probe" vs "runtime exec". 见到 commander prompt 隐含 runtime 操作 (启动 ffmpeg / 跑 ASR / 真写 vault) 立刻 reject + 走 authority 升级 PR.
