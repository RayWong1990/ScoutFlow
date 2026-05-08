import { describe, expect, it } from "vitest";

import { STATE_COPY_ZH, STATE_TOKEN_VAR_MAP } from "./state-tokens";

describe("state-tokens", () => {
  it("exports the nine-state Chinese vocabulary", () => {
    expect(Object.keys(STATE_COPY_ZH)).toHaveLength(9);
    expect(STATE_COPY_ZH.blocked).toContain("Hold");
    expect(STATE_COPY_ZH.preview).toContain("预览");
  });

  it("defines the expected CSS custom properties", () => {
    expect(STATE_TOKEN_VAR_MAP.empty.bg).toBe("--state-empty-bg");
    expect(STATE_TOKEN_VAR_MAP.loading.border).toBe("--state-loading-border");
    expect(STATE_TOKEN_VAR_MAP.committed.bg).toBe("--state-committed-bg");
    expect(STATE_TOKEN_VAR_MAP.skipped.borderStyle).toBe("--state-skipped-border-style");
  });
});
