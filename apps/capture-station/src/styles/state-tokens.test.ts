import { describe, expect, it } from "vitest";

import { CAPTURE_SURFACE_STATES, STATE_COPY_ZH, STATE_TOKEN_VARIABLES } from "./state-tokens";

describe("state-tokens", () => {
  it("exports the nine-state vocabulary with Chinese-first copy", () => {
    expect(CAPTURE_SURFACE_STATES).toHaveLength(9);
    expect(STATE_COPY_ZH.preview).toContain("尚未写入");
    expect(STATE_COPY_ZH.blocked).toContain("已阻止");
  });

  it("tracks the corresponding state token variable set", () => {
    expect(STATE_TOKEN_VARIABLES).toContain("--state-preview-bg");
    expect(STATE_TOKEN_VARIABLES).toContain("--state-committed-bg");
    expect(STATE_TOKEN_VARIABLES).toContain("--state-blocked-bg");
  });
});
