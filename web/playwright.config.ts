import { defineConfig } from "@playwright/test";

// Runs against the Docker preview on the fixed loopback URL. E2E_ORIGIN names another loopback
// origin, so a candidate build can be tested without stopping the preview.
export default defineConfig({
  testDir: "./e2e",
  outputDir: "./test-results",
  fullyParallel: true,
  workers: 4,
  retries: 0,
  reporter: [["list"], ["json", { outputFile: ".artifacts/e2e.json" }]],
  use: { baseURL: process.env.E2E_ORIGIN ?? "http://localhost:3000", channel: "chrome", viewport: { width: 1280, height: 900 } },
});
