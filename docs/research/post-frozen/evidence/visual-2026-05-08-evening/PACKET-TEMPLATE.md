---
status: reference storage
session_id: <YYYY-MM-DD-HHMM>
operator: <name>
round: 4
applicable_window: Codex-264 Lane A T-P1A-160 + Codex-267 Lane D code-bearing (already merged)
packet_state: in_progress / clear / partial / reject
---

# Manual Visual Evidence Packet — Round 4

## §1 跑前 confirm

- [ ] Lane D code-bearing PR # ___ merged
- [ ] Lane A T-P1A-160 PR # ___ merged
- [ ] `pnpm --dir apps/capture-station test/lint/typecheck/build` 全过
- [ ] dev server 启动 OK
- [ ] 浏览器手开 localhost OK
- [ ] 无 Playwright / browser automation 在跑

## §2 9 步 notes

### Step 1 — URL Bar 9 态 token verify
- 状态: PASS / WITH_AMENDMENTS / FAIL
- notes: ___
- 截图 (可选): ___

### Step 2 — 单屏 workstation flow (VT-P1-01)
- 状态:
- notes:
- 截图:

### Step 3 — Trust Trace badge tone (VT-P0-01)
- 状态:
- notes:
- 截图:

### Step 4 — Vault Preview preview-only tone (VT-P0-03)
- 状态:
- notes:
- 截图:

### Step 5 — Vault Commit committed=false 禁绿 (VT-P0-03)
- 状态:
- notes:
- 截图:

### Step 6 — PromoteGate blocked vs pending (VT-P0-02)
- 状态:
- notes:
- 截图:

### Step 7 — RewriteOutputV1 surface 存在 (VT-P1-02)
- 状态:
- notes:
- 截图:

### Step 8 — 极端输入 panel 不撑爆
- 状态:
- notes:
- 截图:

### Step 9 — Batch row vocab 占位 (本波 Storybook 推迟, 仅 spec doc 验证)
- 状态:
- notes: 本步只核验 `docs/specs/batch-manifest-v1-contracts-candidate.md` 是否落 + UI 是否有 placeholder/不冲突即可
- 截图:

## §3 Final verdict

- [ ] V-PASS
- [ ] V-PASS_WITH_AMENDMENTS (列具体 amendments: ___)
- [ ] V-PARTIAL (列具体不足: ___)
- [ ] V-REJECT (列具体阻塞: ___)

## §4 Remaining Holds

仍 Hold (本 packet 不解禁): write_enabled=False, runtime_tools, true_vault_write, browser_automation, dbvnext_migration, full_signal_workbench.

## §5 Boundary

- 本 packet 不批准 P3A / P3B / Phase 3 / Phase 3.5
- 本 packet 不批准 runtime / true write / migration / browser automation
- 本 packet 仅 Lane A + Lane D code-bearing 视觉真值核验
