import assert from "node:assert/strict";
import { registerHooks } from "node:module";
import { test } from "node:test";

// The package has no export map, so plain Node needs the file name that the bundler resolves itself.
registerHooks({
  resolve: (specifier, context, next) => next(specifier === "next/server" ? "next/server.js" : specifier, context),
});
const { NextRequest } = await import("next/server");
const { proxy } = await import("../src/proxy.ts");

const ORIGIN = "http://localhost:3000";
const call = (path: string, method = "GET") => proxy(new NextRequest(`${ORIGIN}${path}`, { method }));
const covered = (response: Response) => {
  assert.match(response.headers.get("content-security-policy") ?? "", /^default-src 'self'; script-src 'self' 'nonce-[^']+';/);
  assert.equal(response.headers.get("x-robots-tag"), "noindex, nofollow");
};

test("a redirect written by the proxy cannot leave this origin, whatever reaches it", () => {
  // The framework collapses repeated slashes first, so these paths only reach the proxy if it stops doing so.
  for (const path of ["//example.test/", "///example.test//", "/\\example.test/", "/\\\\example.test//", "//example.test:80/a/", "//"]) {
    const response = call(path);
    const location = response.headers.get("location");
    assert.equal(response.status, 308, path);
    assert.ok(location, path);
    const target = new URL(location, ORIGIN);
    assert.equal(target.origin, ORIGIN, path);
    assert.ok(!/^[/\\]{2}/.test(target.pathname), path);
    covered(response);
  }
});

test("only reads are answered", () => {
  for (const method of ["POST", "PUT", "PATCH", "DELETE", "OPTIONS"]) {
    for (const path of ["/", "/explore", "/explore/", "/perfume/%E0%A4%A", "/studies/hero.svg"]) {
      const response = call(path, method);
      assert.equal(response.status, 405, `${method} ${path}`);
      assert.equal(response.headers.get("allow"), "GET, HEAD");
      assert.equal(response.body, null);
      covered(response);
    }
  }
  for (const method of ["GET", "HEAD"]) assert.equal(call("/explore", method).status, 200);
});

test("every kind of answer carries the policy, and only owned files may be cached", () => {
  for (const path of ["/", "/explore/", "/perfume/%E0%A4%A", "/_next/image?url=x", "/nope", "/studies/hero.svg", "/icon.svg"]) {
    const response = call(path);
    covered(response);
    const owned = path.startsWith("/studies/") || path === "/icon.svg";
    assert.equal(response.headers.get("cache-control"), owned ? null : "private, no-store, max-age=0", path);
  }
});

test("the production policy has no development exception", () => {
  const csp = call("/").headers.get("content-security-policy") ?? "";
  assert.doesNotMatch(csp, /unsafe-|strict-dynamic|https?:|wss?:|\*/);
});
