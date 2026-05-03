# T-P1A-011B BBDown Manual-Auth QR Local-Only Report — 2026-05-04

> 状态：`complete / local-only auth gate closed`。
> 文件名沿用 07 dispatch 指定日期；本次实际执行时间为 `2026-05-04`（Asia/Shanghai）。
> 本报告是 redacted local-only auth report，不是 runtime approval，不是 `-info` probe report，不是 media / ffmpeg / ASR approval。

## 1. Scope

本次只执行 `T-P1A-011B manual-auth QR local-only gate`。

执行边界：

- 使用 repo 外 local-only executable
- 使用 repo 外临时 cwd 展示 QR
- 只执行 BBDown help/login 相关动作
- 不执行 `BBDown -info`
- 不下载 media
- 不运行 ffmpeg / ASR
- 不读取 browser profile
- 不调用 `/jobs/{job_id}/complete`
- 不创建 receipt / artifact ledger
- 不推进 capture state

## 2. Local-Only Preconditions

执行前已确认：

- repo-local executable 风险已规避：`yes`
- repo-local cwd 风险已规避：`yes`
- auth-sidecar 预期落点在 tracked repo 外：`yes`
- operator 不需要粘贴 cookie / token：`yes`

安全抽象描述：

- executable location: `external local-only BBDown executable outside Git`
- auth storage location: `local BBDown auth store outside Git`
- QR display location: `temporary local-only cwd outside Git`

## 3. QR Gate Result

```text
qr_displayed_locally=true
user_scan_completed=true
auth_result=completed
repo_local_executable_or_cwd_risk_avoided=true
```

安全确认要点：

- 本地 QR 图像已生成并展示给 user
- user 已完成扫码
- safe tool output 显示扫码成功并随后显示登录成功
- 当前临时 QR cwd 已清空；未留下 `qrcode.png`
- auth-sidecar 已落在 repo 外 local-only auth store

## 4. Sensitive Material Handling

未进入 Git / PR / logs / tracked artifacts 的内容：

- QR image
- terminal QR block
- cookie/token values
- authorization header
- browser profile
- raw auth-sidecar contents
- auth-sidecar precise filesystem path

本报告只保留抽象事实，不保留可复用凭据或可复扫材料。

## 5. Boundary Confirmation

- `BBDown -info` executed: `no`
- platform boundary reached for probe: `no`
- `PlatformResult` emitted: `no`
- media download: `no`
- ffmpeg run: `no`
- ASR run: `no`
- browser profile read: `no`
- receipt created: `no`
- artifact ledger written: `no`
- capture state advanced: `no`

## 6. Interpretation

`T-P1A-011B` 只证明：

- 本地 QR manual-auth gate 可以在 repo 外 local-only boundary 内安全完成
- `BBDown.data` / `qrcode.png` 的落点风险可以通过 external executable + temp cwd 控制住

`T-P1A-011B` 不证明：

- no-auth probe 成功
- `BBDown -info` 成功
- metadata parser success
- `PlatformResult` classification
- media / ffmpeg / ASR runtime approval

## 7. Next Gate

后续若要继续，仍需 user 明确授权下一 gate。当前最自然的后续是：

- 一个新的 `-info` gate，明确允许在 local-only auth state 已存在的前提下做单次 metadata probe

仍未批准：

- real `BBDown -info`
- media download
- ffmpeg
- ASR
- `audio_transcript`
- receipt / artifact ledger
- capture state advancement
