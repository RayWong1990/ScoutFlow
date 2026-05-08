import type { HoldBannerProps } from "./HoldBanner";

export type HoldKey =
  | "true_vault_write"
  | "runtime_tools"
  | "browser_automation"
  | "dbvnext_migration"
  | "full_signal_workbench"
  | "audio_transcript"
  | "source_linkage";

export const DEFAULT_HOLDS: Record<HoldKey, HoldBannerProps> = {
  true_vault_write: {
    holdId: "HOLD-TRUE-WRITE",
    title: "True write 保持关闭",
    reason: "write_enabled=False 仍是硬真相，当前只允许 dry-run / preview。",
    unlockPath: "需要 Lane C gate readiness + user explicit approval。",
  },
  runtime_tools: {
    holdId: "HOLD-RUNTIME-TOOLS",
    title: "Runtime tools 未解禁",
    reason: "外部 runtime 工具仍在候选 readiness 阶段，不允许 UI 假装可运行。",
    unlockPath: "等待 Lane B readiness 证据和后续显式授权。",
  },
  browser_automation: {
    holdId: "HOLD-BROWSER-AUTO",
    title: "Browser automation 保持阻止",
    reason: "浏览器自动化仍被主线红线拦住，不允许从 capture-station 侧暗示可点通。",
    unlockPath: "必须新 dispatch + user gate。",
  },
  dbvnext_migration: {
    holdId: "HOLD-DBVNEXT",
    title: "DB vNext 仍是 candidate-only",
    reason: "migration readiness 未获批，任何 committed cue 都会越权。",
    unlockPath: "等待独立 migration dispatch 和外审。",
  },
  full_signal_workbench: {
    holdId: "HOLD-SIGNAL-WORKBENCH",
    title: "Full-signal workbench 未开放",
    reason: "当前只保留 metadata-only / trust-trace bounded readback。",
    unlockPath: "需要后续 product lane 明确 promote。",
  },
  audio_transcript: {
    holdId: "HOLD-AUDIO-TRANSCRIPT",
    title: "ASR / transcript 仍 blocked",
    reason: "audio_transcript runtime 还没进入可执行窗口。",
    unlockPath: "等待单独 runtime lane 和显式 user gate。",
  },
  source_linkage: {
    holdId: "HOLD-SOURCE-LINKAGE",
    title: "Source linkage 证据未齐",
    reason: "source_task_id / source_report_path 不完整时，不能上升为 success cue。",
    unlockPath: "等 trust-trace source linkage 回填后再升级状态。",
  },
};
