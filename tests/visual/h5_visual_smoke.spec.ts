import { expect, test } from "@playwright/test";

const baseURL = process.env.CAPTURE_STATION_BASE_URL;

test.describe("capture station visual smoke", () => {
  test.skip(!baseURL, "CAPTURE_STATION_BASE_URL is required; browser automation remains separately gated.");

  test("renders the current four-panel shell", async ({ page }) => {
    await page.goto(baseURL!);

    await expect(page.getByText("Capture Station")).toBeVisible();
    await expect(page.getByTestId("panel-url-bar")).toBeVisible();
    await expect(page.getByTestId("panel-live-metadata")).toBeVisible();
    await expect(page.getByTestId("panel-capture-scope")).toBeVisible();
    await expect(page.getByTestId("panel-trust-trace")).toBeVisible();
  });
});
