export type CaptureSurfaceState =
  | "empty"
  | "loading"
  | "disabled"
  | "blocked"
  | "preview"
  | "committed"
  | "failed"
  | "partial"
  | "skipped";

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

export const STATE_TOKEN_VAR_MAP: Record<
  CaptureSurfaceState,
  { bg: string; fg: string; border: string; borderStyle?: string }
> = {
  empty: {
    bg: "--state-empty-bg",
    fg: "--state-empty-fg",
    border: "--state-empty-border",
  },
  loading: {
    bg: "--state-loading-bg",
    fg: "--state-loading-fg",
    border: "--state-loading-border",
  },
  disabled: {
    bg: "--state-disabled-bg",
    fg: "--state-disabled-fg",
    border: "--state-disabled-border",
  },
  blocked: {
    bg: "--state-blocked-bg",
    fg: "--state-blocked-fg",
    border: "--state-blocked-border",
  },
  preview: {
    bg: "--state-preview-bg",
    fg: "--state-preview-fg",
    border: "--state-preview-border",
  },
  committed: {
    bg: "--state-committed-bg",
    fg: "--state-committed-fg",
    border: "--state-committed-border",
  },
  failed: {
    bg: "--state-failed-bg",
    fg: "--state-failed-fg",
    border: "--state-failed-border",
  },
  partial: {
    bg: "--state-partial-bg",
    fg: "--state-partial-fg",
    border: "--state-partial-border",
  },
  skipped: {
    bg: "--state-skipped-bg",
    fg: "--state-skipped-fg",
    border: "--state-skipped-border",
    borderStyle: "--state-skipped-border-style",
  },
};

const captureSurfaceStates = new Set<CaptureSurfaceState>(Object.keys(STATE_COPY_ZH) as CaptureSurfaceState[]);

export function isCaptureSurfaceState(value: string): value is CaptureSurfaceState {
  return captureSurfaceStates.has(value as CaptureSurfaceState);
}
