export type HoldBannerPreset = {
  holdId: string;
  title: string;
  reason: string;
  unlockPath: string;
};

export const DEFAULT_HOLD_BANNERS: HoldBannerPreset[] = [
  {
    holdId: "HOLD-TRUE-WRITE",
    title: "True write remains blocked",
    reason: "write_enabled=false，预览与 committed 仍必须严格分离。",
    unlockPath: "单独 true_vault_write gate + human approval",
  },
  {
    holdId: "HOLD-RUNTIME",
    title: "Runtime tools remain blocked",
    reason: "BBDown / yt-dlp / ffmpeg / ASR live execution 本轮不解禁。",
    unlockPath: "runtime_tools lane gate readiness + explicit runtime approval",
  },
  {
    holdId: "HOLD-BROWSER",
    title: "Browser automation remains blocked",
    reason: "不允许 Playwright / Selenium / Puppeteer / browser automation 偷渡。",
    unlockPath: "独立 browser_automation gate",
  },
  {
    holdId: "HOLD-DBVNEXT",
    title: "DB vNext migration remains blocked",
    reason: "本轮只允许 candidate architecture，不允许 migration drill 或 schema execution。",
    unlockPath: "dbvnext_migration gate + dedicated PR",
  },
  {
    holdId: "HOLD-FULL-SIGNAL",
    title: "Full signal workbench remains blocked",
    reason: "当前只允许 bounded visual/runtime preparation，不允许全量工作台解禁。",
    unlockPath: "future full_signal_workbench gate",
  },
];

