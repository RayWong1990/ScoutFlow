# Localhost 最短闭环估算

| 目标层级 | 任务包数 | dispatch 数 | 关键能力 | 不该提前做的东西 |
|---|---:|---:|---|---|
| preview-only localhost loop | 2-3 | 8-13 | bridge router mount; createCapture API; URLBar submit; vault preview fetch; markdown display; copy/download; manual run proof | true vault write; BBDown live; ASR; browser automation; migrations; full Signal Workbench |
| preview-only + real URL topic-card proof + RAW handoff proof | 4-5 | 15-23 | 3 URL canary; topic-card-lite; human usefulness verdict; RAW note candidate; manual handoff; intake/script seed proof | ranking engine; capture-plan full object; true write; automated RAW intake |
| above + screenshot/human visual verdict + controlled hardening | 5-7 | 20-30 | screenshot set; human visual verdict; frontend bootstrap repair; targeted bridge/error hardening | Playwright execution by default; browser automation; phase 2 runtime |

## Why not fewer

The current live repo already has partial pieces, but they are disconnected: API bridge router is not mounted, H5 Create capture is static, preview panel is placeholder-first, and copy/download is absent.

## Why not more now

More scope before A-tier pass increases debt: over-objectification, preview false closure, second inbox, and runtime creep.
