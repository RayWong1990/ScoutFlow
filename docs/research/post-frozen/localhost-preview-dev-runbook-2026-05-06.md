---
title: Localhost Preview Dev Runbook
status: candidate / shape_only / not-authority
date: 2026-05-06
dispatch_id: PF-LP-12
---

# Localhost Preview Dev Runbook

## backend_start

在仓库根目录启动 API：

```bash
cd /Users/wanglei/workspace/ScoutFlow
PYTHONPATH=services/api uvicorn scoutflow_api.main:create_app --factory --reload --port 8000
```

预期：

- `http://127.0.0.1:8000/docs` 可打开
- `/bridge/health` 返回 `write_enabled=false`
- 不需要 BBDown、yt-dlp、ffmpeg、ASR 或 browser automation

## h5_start

在第二个终端启动 H5：

```bash
cd /Users/wanglei/workspace/ScoutFlow/apps/capture-station
pnpm dev --host 127.0.0.1 --port 5173
```

预期：

- 浏览器打开 `http://127.0.0.1:5173`
- 页面可见 `Manual URL`、`Vault Preview`、`Vault Commit Dry Run`
- 这是 preview-only localhost loop，不构成 runtime approval 或 true write approval

## env_setup

建议在启动 backend 前显式设置：

```bash
export SCOUTFLOW_VAULT_ROOT=/absolute/path/to/obsidian-vault
```

说明：

- 未设置时，preview 路线应 fail-loud，不得暗示已经写入 vault
- 路径必须是本机可访问目录；本 runbook 不批准真实写入，只用于 preview draft
- 如果只想验证 blocked state，可故意不设置 `SCOUTFLOW_VAULT_ROOT`

## manual_evidence_capture

推荐最小手工回路：

1. 在 URL Bar 粘贴一个 Bilibili URL
2. 点击 `Create capture`
3. 观察 preview 状态从 `loading` 进入 `preview loaded` 或 fail-loud error
4. 记录 `capture_id`
5. 点击 `Copy markdown`，确认能粘贴出完整 markdown
6. 点击 `Download .md`，确认文件名形如 `scoutflow-preview-{capture_id}.md`

证据建议写入：

- `docs/research/post-frozen/evidence/PF-LP-16-manual-localhost-run-2026-05-06.md`

最少记录字段：

- `input_url`
- `capture_id`
- `markdown_excerpt_first_3_lines`
- `copy_action`
- `download_action`
- `downloaded_filename`
- `verdict`

## stop_lines

以下情况立即停线，不把结果写成 `PASS` 或 execution approval：

- 需要 Playwright、browser automation、截图脚本才能完成验证
- UI 暗示 true vault write 已发生
- 需要 BBDown live、yt-dlp、ffmpeg、ASR、`audio_transcript`
- 需要修改 `docs/current.md`、`docs/task-index.md`、`docs/decision-log.md`
- 需要触碰 `services/api/migrations/**`、`workers/**`、`packages/**`

结论措辞限制：

- 可写 `T-PASS`、`V-PASS`、`partial`、`FAIL_ENV`
- 不写裸 `PASS`、`DONE`、`已完成`
