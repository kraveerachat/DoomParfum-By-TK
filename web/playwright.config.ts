import { defineConfig } from "@playwright/test";

// Runs against the Docker preview already listening on the fixed loopback URL.
export default defineConfig({
  testDir: "./e2e",
  outputDir: "./test-results",
  fullyParallel: true,
  workers: 4,
  retries: 0,
  reporter: [["list"], ["json", { outputFile: ".artifacts/e2e.json" }]],
  use: { baseURL: "http://localhost:3000", channel: "chrome", viewport: { width: 1280, height: 900 } },
});
