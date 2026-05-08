import { render, screen } from "@testing-library/react";
import { describe, expect, it } from "vitest";

import HoldBanner from "./HoldBanner";
import { DEFAULT_HOLD_BANNERS } from "./holds";

describe("HoldBanner", () => {
  it("keeps hold reason and unlock path always visible", () => {
    const hold = DEFAULT_HOLD_BANNERS[0];
    render(<HoldBanner {...hold} />);

    expect(screen.getByText(hold.reason)).toBeTruthy();
    expect(screen.getByText((_, node) => node?.textContent === `解锁路径：${hold.unlockPath}`)).toBeTruthy();
    expect(screen.getByRole("status", { name: /HOLD-TRUE-WRITE hold/i })).toBeTruthy();
  });
});
