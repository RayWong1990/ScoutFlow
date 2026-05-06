# 当前裁决

## 最前置结论

实现 localhost 粘 URL、点按钮、看到转换后的 markdown、可复制/下载，最短仍需：

| 层级 | 任务包 | dispatch | 裁决 |
|---|---:|---:|---|
| preview-only localhost loop | 2-3 | 8-13 | 当前最短主线 |
| + real URL topic-card proof + RAW handoff proof | 4-5 | 15-23 | 产品飞轮 proof |
| + screenshot/human visual verdict + controlled hardening | 5-7 | 20-30 | 强视觉与稳定化 |

## 核心判断

- Authority sync after PR #193/#194 is not the main blocker anymore.
- The blocker is wiring: Bridge router mount + H5 createCapture + preview fetch + copy/download.
- PF-C0/O1 must be thin and precede code-bearing work.
- PF-localhost-preview is the shortest and most valuable mainline.
