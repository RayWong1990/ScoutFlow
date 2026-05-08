export const CAPTURE_SURFACE_STATES = [
  "empty",
  "loading",
  "disabled",
  "blocked",
  "preview",
  "committed",
  "failed",
  "partial",
  "skipped",
] as const;

export const STATE_TOKEN_VARIABLES = [
  "--state-empty-bg",
  "--state-loading-bg",
  "--state-disabled-bg",
  "--state-blocked-bg",
  "--state-preview-bg",
  "--state-committed-bg",
  "--state-failed-bg",
  "--state-partial-bg",
  "--state-skipped-bg",
] as const;

export type CaptureSurfaceState = (typeof CAPTURE_SURFACE_STATES)[number];

export const STATE_COPY_ZH: Record<CaptureSurfaceState, string> = {
  empty: "等待输入 / 尚无预览",
  loading: "正在读取 / 正在生成",
  disabled: "当前未解禁 / 需要新 dispatch",
  blocked: "已阻止：详见 Hold 原因",
  preview: "预览已生成，尚未写入",
  committed: "已写入 raw inbox",
  failed: "失败已记录：source/ASR/rewrite/write",
  partial: "部分完成：详见拆分",
  skipped: "已跳过：详见原因",
};

export const STATE_ICON_NAME: Record<CaptureSurfaceState, string> = {
  empty: "empty",
  loading: "loading",
  disabled: "locked",
  blocked: "blocked",
  preview: "focus",
  committed: "success",
  failed: "error",
  partial: "warning",
  skipped: "empty",
};
