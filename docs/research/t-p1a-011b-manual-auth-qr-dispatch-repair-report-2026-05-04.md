# T-P1A-011B Manual-Auth QR Dispatch Repair Report — 2026-05-04

> 状态：`dispatch-repair complete / gate still not authorized for execution`。
> 作用：记录 `07-dispatch-t-p1a-011b-manual-auth-qr-local-only-gate.md` 的修订原因、repo 侧经验教训级联，以及仍然未批准的边界。

## 1. Why This Repair Was Needed

`T-P1A-011` 的 preflight compatibility repair 完成后，新的高风险坑不在 `--version`，而在 manual-auth 本地副作用：

- `BBDown 1.6.3` 的 `--version` 不能单独当 root-less preflight 语义。
- `BBDown login` 可能把 `qrcode.png` 写到当前工作目录。
- `BBDown.data` / `BBDownTV.data` 可能写到 executable 同目录。

因此，原始 07 dispatch 如果不把 executable 位置和 cwd 位置写死为 repo 外 local-only boundary，就容易在执行时把 auth material 留进 repo 或可跟踪目录。

## 2. Authorization Summary

本轮 user 授权内容：

- 允许直接修复 `Downloads` 目录中的 07 dispatch 文本
- 允许把经验教训级联写回 ScoutFlow 相关 authority / contract 文件
- 不等于授权执行 `T-P1A-011B` manual-auth QR local-only gate
- 不等于授权真实 `BBDown -info`
- 不等于授权 media / ffmpeg / ASR / receipt / capture state

## 3. Repo-Side Lessons Written Back

已级联到以下 repo 文件：

- `docs/task-index.md`
- `docs/current.md`
- `docs/specs/contracts-index.md`
- `docs/specs/raw-response-redaction.md`
- `docs/archive/SRD-v1.2-amendment-2026-05-03.md`
- `docs/archive/PRD-v1.2-amendment-2026-05-03.md`

写回的核心 lesson：

1. manual-auth gate 不能在 repo 内 executable 上执行，否则 `BBDown.data` 有落入 repo 的风险。
2. manual-auth gate 不能在 repo cwd 上执行，否则 `qrcode.png` 有落入 repo 的风险。
3. `BBDown.data` / `BBDownTV.data` / `qrcode.png` / terminal QR block 都视为 sensitive auth material，不是 evidence。
4. 即使 user 在本机扫码，report 里也只能写抽象描述，如 `local BBDown auth store outside Git`。

## 4. External Dispatch Repair

已修订外部文件：

```text
/Users/wanglei/Downloads/scoutflow-dispatch-prompts-2026-05-03/07-dispatch-t-p1a-011b-manual-auth-qr-local-only-gate.md
```

修订后的 07 dispatch 重点包括：

- 加入更准确的显式授权短语
- 写明 `T-P1A-011` preflight compatibility repair 已完成
- 写明 `BBDown 1.6.3` manual-auth 的两个副作用：`qrcode.png` at cwd, `BBDown.data` next to executable
- 强制 external executable path + temp cwd outside repo
- 显式禁止 `--debug`
- 把 repo 内 executable / auth store / QR image 视为 stop-the-line

## 5. Still Not Approved

- `T-P1A-011B` execution itself
- real `BBDown -info`
- media download
- ffmpeg
- ASR
- receipt / artifact ledger
- capture state advancement
- browser profile reading
- command-string credentials
