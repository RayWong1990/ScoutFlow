---
name: api-as-write-boundary
description: Bridge / Thin API 是唯一 write channel; 不允许 frontend 直 worker / 直 vault
type: project
source_atlas_node: P-API-AS-WRITE-BOUNDARY
cross_vendor_readers: [cc0, cc1, codex, gpt-pro, hermes]
memory_role: cross-vendor instinct source
status: reference storage
---

# Bridge / Thin API as the only write channel

ScoutFlow 4-layer 架构 (L0 Authority / L1 Workers / L2 Thin API / L3 Console) 严格走 Thin API (Bridge) 作为唯一 write boundary. Console (frontend) 不直接调 Workers (BBDown / yt-dlp / ffmpeg / ASR), 不直接写 Vault. 一切 write 经 Bridge route, Bridge 守 5 routes 表锁 + write_enabled=False 边界.

**Why:** SRD-v2 + SRD-v3 h5-bridge promoted 锁的 4-layer architecture 第一性. 任何 "frontend 直 BBDown / Console 直 vault" = 破坏 Trust Trace + 失去 audit 路径 + 撞 5 overflow lane Hold.

**How to apply:** PR review 时 grep `apps/capture-station/**` 是否调任何 worker / vault module. 任一命中 reject. commander prompt 必含 "frontend 仅调 Bridge route, 不直 worker". 新增 surface 必走 Bridge route mapping, 不绕道.
