import { render, screen } from "@testing-library/react";
import { describe, expect, it } from "vitest";

import Button from "./Button";
import { deriveButtonVariant } from "./derive";

describe("Button", () => {
  it("downgrades dry-run committed=false flows into preview-only tone", () => {
    const variant = deriveButtonVariant({
      committed: false,
      writeEnabled: false,
      dryRun: true,
    });

    render(<Button variant={variant}>committed=false</Button>);

    expect(screen.getByRole("button").getAttribute("data-variant")).toBe("preview-only");
  });

  it("keeps explicit success alias from rendering as committed green", () => {
    render(<Button variant="success">legacy success</Button>);

    expect(screen.getByRole("button").getAttribute("data-variant")).toBe("preview-only");
  });
});
