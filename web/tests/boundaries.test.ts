import assert from "node:assert/strict";
import { readdirSync, readFileSync } from "node:fs";
import { join, relative } from "node:path";
import { test } from "node:test";

const root = join(import.meta.dirname, "../src");
const files = readdirSync(root, { recursive: true, withFileTypes: true })
  .filter((f) => f.isFile() && /\.(ts|tsx|css)$/.test(f.name))
  .map((f) => join(f.parentPath, f.name));
const sources = files.map((f) => ({ name: relative(root, f).replaceAll("\\", "/"), text: readFileSync(f, "utf8") }));
const hits = (pattern: RegExp, except: readonly string[] = []) =>
  sources.filter((s) => !except.includes(s.name) && pattern.test(s.text)).map((s) => s.name);

test("no import leaves web/src for the database, matching or vault workstreams", () => {
  assert.deepEqual(hits(/from\s+["'][^"']*(database|matching_math|Structure DB)/), []);
  assert.deepEqual(hits(/from\s+["'](?:\.\.\/){3,}/), []);
});

test("no network, storage, cookie, worker or environment access in application code", () => {
  assert.deepEqual(hits(/\b(fetch|XMLHttpRequest|WebSocket|EventSource|sendBeacon)\s*\(/), []);
  assert.deepEqual(hits(/\b(localStorage|sessionStorage|indexedDB|serviceWorker|document\.cookie)\b/), []);
  assert.deepEqual(hits(/process\.env/, ["proxy.ts"]), []);
  assert.deepEqual(hits(/["']use server["']/), []);
});

test("no external URL in application code", () => {
  // proxy.ts names the loopback dev WebSocket; validate.ts holds the URL rejection pattern.
  assert.deepEqual(hits(/https?:\/\/|wss?:\/\//, ["proxy.ts"]), []);
});

test("fixture data is imported by the server module only", () => {
  assert.deepEqual(hits(/fixtures\/data/), ["server/catalogue.ts"]);
  const clientFiles = sources.filter((s) => /^["']use client["']/.test(s.text));
  assert.ok(clientFiles.length > 5);
  for (const s of clientFiles) assert.doesNotMatch(s.text, /server\/catalogue/, s.name);
});

test("no inline style attribute that the nonce policy would reject, and no raw HTML", () => {
  assert.deepEqual(hits(/\sstyle=\{/), []);
  assert.deepEqual(hits(/dangerouslySetInnerHTML/), []);
});

test("no score, price or rating vocabulary reaches the interface", () => {
  assert.deepEqual(hits(/\b(similarity|match score|% match|rating|best[- ]seller|add to cart|checkout)\b/i), []);
});

test("colors come from tokens", () => {
  assert.deepEqual(hits(/#[0-9a-f]{6}\b/i, ["app/globals.css", "app/layout.tsx"]), []);
});
