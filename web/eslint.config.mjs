import { defineConfig, globalIgnores } from "eslint/config";
import nextVitals from "eslint-config-next/core-web-vitals";
import nextTs from "eslint-config-next/typescript";

export default defineConfig([
  ...nextVitals,
  ...nextTs,
  globalIgnores([".next/**", "next-env.d.ts", "test-results/**", "playwright-report/**", ".artifacts/**"]),
  {
    rules: {
      // Visuals are same-origin static SVG studies; the image optimizer is disabled on purpose.
      "@next/next/no-img-element": "off",
      // Mock boundary: the app never reaches into the repository's other workstreams.
      "no-restricted-imports": ["error", {
        patterns: [{ group: ["**/database/**", "**/matching_math/**"], message: "web/ must stay isolated from database/ and matching_math/." }],
      }],
      "no-restricted-globals": ["error", "fetch", "XMLHttpRequest", "WebSocket", "EventSource", "localStorage", "sessionStorage", "indexedDB", "caches"],
    },
  },
  { files: ["e2e/**", "scripts/**", "tests/**"], rules: { "no-restricted-globals": "off" } },
]);
