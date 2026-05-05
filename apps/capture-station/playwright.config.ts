export default {
  testDir: "../../tests/visual",
  reporter: "list",
  use: {
    headless: true,
    screenshot: "only-on-failure",
  },
} as const;
