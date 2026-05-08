import { render, screen } from "@testing-library/react";
import { describe, expect, it } from "vitest";

import Button from "./Button";
import { deriveVaultActionButtonVariant } from "./derive";

describe("Button", () => {
  it("supports preview-only tone without using success cue", () => {
    render(<Button variant="preview-only">Preview only</Button>);
    expect(screen.getByRole("button", { name: "Preview only" }).className).toMatch(/preview-only/);
  });

  it("derives blocked/preview-only/success from vault action truth", () => {
    expect(deriveVaultActionButtonVariant({ committed: false, writeEnabled: false, dryRun: true })).toBe("blocked");
    expect(deriveVaultActionButtonVariant({ committed: false, writeEnabled: true, dryRun: true })).toBe("preview-only");
    expect(deriveVaultActionButtonVariant({ committed: true, writeEnabled: true, dryRun: false })).toBe("success");
  });
});
