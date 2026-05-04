# T-P1A-011F Dispatch 08/09 Patch Report — 2026-05-04

> 状态：`complete / repo-side patch report`。
> 说明：patched prompt files 位于 repo 外下载包，不属于本次 GitHub PR；本报告只记录修补后的依赖口径与边界。

## 1. Original Stale Dependency

原始问题是 Dispatch 08 把成功证据前提写成：

```text
successful T-P1A-011 redacted metadata evidence
```

这与当前 GitHub truth 冲突，因为：

- `T-P1A-011` remained blocked
- `T-P1A-011C` is the successful auth-present metadata evidence source

## 2. Corrected Dependency

patched Dispatch 08 现在应以以下链条为前提：

```text
T-P1A-011D second retro triage complete
T-P1A-011E minimal retro skeleton complete, unless user explicitly waived it
T-P1A-011F dispatch 08/09 prompt patch complete
T-P1A-011G sidecar review PASS or PASS_WITH_FIXES, unless user explicitly skips sidecar review
T-P1A-011C auth-present redacted metadata evidence with platform_result=ok
```

## 3. Numbering Policy

```text
T-P1A-012 and T-P1A-013 stay reserved for Dispatch 08 and Dispatch 09.
```

任何 pre-08 retro / remediation 都继续占用 `T-P1A-011D/E/F/G/H`。

## 4. Dispatch 08 Patch Summary

外部 working file：

- `/Users/wanglei/Downloads/scoutflow-dispatch-7x-to-09-patched-pack/08-dispatch-t-p1a-012-metadata-receipt-ledger-wiring-PATCHED.md`

修补后重点：

- success evidence 改为 `T-P1A-011C`
- 明写 `T-P1A-011` blocked no-auth probe 不是 success evidence source
- 强化 boundary：no live BBDown / no `BBDown -info` / no auth reuse / no media/audio artifacts
- 指定 evidence source file：`docs/research/t-p1a-011c-bbdown-auth-present-info-probe-report-2026-05-04.md`
- 要求产物只能是 safe metadata evidence，不保留 raw stdout/stderr、signed URL、cookie、local auth path、QR image

## 5. Dispatch 09 Patch Summary

外部 working file：

- `/Users/wanglei/Downloads/scoutflow-dispatch-7x-to-09-patched-pack/09-dispatch-t-p1a-013-explore-trust-trace-minimal-PATCHED.md`

修补后重点：

- 依赖改为 `T-P1A-011F` + `T-P1A-012` + `T-P1A-012R`，或 user 明确授权 docs-only mock mode
- 明写 layering：`probe evidence != receipt ledger != capture state != media/audio readiness`
- 收紧 UI/API 词汇：receipt 不得早于 receipt ledger 存在
- 明写不得从 metadata success 推导出 `audio_transcript` readiness
- 继续禁止 raw stdout/stderr、cookie、token、signed URL、local auth path、QR image

## 6. External Patch Pack Status

当前下载包内已经存在 patched copies：

- `README-dispatch-7x-to-09-patched-pack.md`
- `08-dispatch-t-p1a-012-metadata-receipt-ledger-wiring-PATCHED.md`
- `09-dispatch-t-p1a-013-explore-trust-trace-minimal-PATCHED.md`

本任务逐项核对这些外部文件与当前 repo truth 的一致性，保留它们作为后续运行 Dispatch 08/09 的 working input。

## 7. Runtime Confirmation

本任务没有执行：

- BBDown
- receipt writing
- artifact ledger
- capture state advancement
- media / ffmpeg / ASR

这是 prompt repair / prompt verification，不是 runtime。
