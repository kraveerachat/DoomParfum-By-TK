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

/** The request headers the proxy forwards, and where it rewrote the request (null when it did not). */
const forwarded = (path: string, headers: Record<string, string> = {}) => {
  const response = proxy(new NextRequest(`${ORIGIN}${path}`, { headers }));
  const rewrite = response.headers.get("x-middleware-rewrite");
  return {
    status: response.status,
    locale: response.headers.get("x-middleware-request-x-doomparfum-locale"),
    rewrite: rewrite ? new URL(rewrite).pathname : null,
  };
};

test("S9: the 404 locale comes from the path only, never from a client header", () => {
  const spoof = { "x-doomparfum-locale": "th", "accept-language": "th-TH,th;q=0.9" };
  for (const [path, locale] of [
    ["/nope", "en"],
    ["/en", "en"],
    ["/TH", "en"],
    ["/thx", "en"],
    ["/perfume/nope", "en"],
    ["/th", "th"],
    ["/th/nope", "th"],
    ["/th/perfume/nope", "th"],
    ["/%E0%B8", "en"],
    ["/th/%E0%B8", "th"],
  ] as const) {
    assert.equal(forwarded(path, spoof).locale, locale, path);
    assert.equal(forwarded(path, { "x-doomparfum-locale": locale === "th" ? "en" : "th" }).locale, locale, path);
  }
});

test("S9: malformed addresses and unknown slugs go to the global 404, known pages do not", () => {
  // Before S9 these reached notFound() in a page: the framework error document, no lang, empty without scripting.
  for (const [path, target] of [
    ["/perfume/nope", "/_unavailable"],
    ["/perfume/Paper-Study-A", "/_unavailable"],
    ["/perfume/%E0%A4%A", "/_unavailable"],
    ["/%E0%B8", "/_unavailable"],
    ["/TH/%E0%B8", "/_unavailable"],
    ["/th/perfume/nope", "/th/_unavailable"],
    ["/th/%E0%B8", "/th/_unavailable"],
  ] as const) {
    assert.deepEqual([forwarded(path).status, forwarded(path).rewrite], [200, target], path);
  }
  for (const path of ["/", "/explore", "/notes", "/about", "/perfume/paper-study-a", "/perfume/paper%2Dstudy-a", "/th", "/th/perfume/glass-study-i", "/nope", "/perfume/nope/x"]) {
    assert.equal(forwarded(path).rewrite, null, path);
  }
  // A trailing slash is still redirected first, so an unknown slug with one is redirected, then answered.
  assert.equal(forwarded("/perfume/nope/").status, 308);
});

test("the production policy has no development exception", () => {
  const csp = call("/").headers.get("content-security-policy") ?? "";
  assert.doesNotMatch(csp, /unsafe-|strict-dynamic|https?:|wss?:|\*/);
});
