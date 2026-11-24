/**
 * Response classes, sent as exact request targets. Two groups stay separate on purpose: responses that
 * pass through src/proxy.ts, and known exceptions that the framework or Node answers before it runs.
 */
import { expect, ORIGIN, raw, test } from "./helpers";

type Headers = Awaited<ReturnType<typeof raw>>["headers"];
const policy = (headers: Headers) => ({
  csp: headers["content-security-policy"] !== undefined,
  noindex: /noindex/.test(String(headers["x-robots-tag"] ?? "")),
  nosniff: headers["x-content-type-options"] === "nosniff",
  noStore: /no-store/.test(headers["cache-control"] ?? ""),
});
const FULL = { csp: true, noindex: true, nosniff: true, noStore: true };
const NONE = { csp: false, noindex: false, nosniff: false, noStore: false };

test.describe("responses produced through the proxy", () => {
  for (const [target, location] of [
    ["/explore/", "/explore"],
    ["/example.test/", "/example.test"],
    ["/%5Cexample.test/", "/%5Cexample.test"],
    ["/%2F%2Fexample.test/", "/%2F%2Fexample.test"],
    ["/about/?next=%2F%2Fexample.test%2F", "/about?next=%2F%2Fexample.test%2F"],
  ] as const) {
    test(`UX5 ${target} redirects once, on this origin, with every header`, async () => {
      const response = await raw("GET", target);
      expect(response.status).toBe(308);
      expect(response.headers.location).toBe(location);
      expect(new URL(location, ORIGIN).origin).toBe(ORIGIN);
      expect(policy(response.headers)).toEqual(FULL);
    });
  }

  for (const query of [
    "y=%20z",
    "y=+z&p=%2B&y=2&e=",
    "t=%E0%B8%81%E0%B8%A5",
    "family=mock-family-soft&note=mock-note-002",
    "m=%26%3D%23",
  ]) {
    test(`a redirect keeps the meaning of ?${query}`, async () => {
      const { status, headers } = await raw("GET", `/explore/?${query}`);
      expect(status).toBe(308);
      const sent = new URLSearchParams(query);
      const kept = new URL(String(headers.location), ORIGIN).searchParams;
      // Escapes may change form and repeated keys may be grouped; the app reads each key's values in order.
      expect([...new Set(kept.keys())].sort()).toEqual([...new Set(sent.keys())].sort());
      for (const key of sent.keys()) expect(kept.getAll(key), key).toEqual(sent.getAll(key));
    });
  }

  for (const [target, status] of [
    ["/", 200],
    ["/explore", 200],
    ["/perfume/paper-study-a", 200],
    ["/notes", 200],
    ["/about", 200],
    ["/perfume/nope", 404],
    ["/nope", 404],
    ["/perfume/%E0%A4%A", 404],
    ["/%E0%A4%A/", 404],
    ["/%2f%2fexample.test", 404],
    ["/studies/absent.svg", 404],
    ["/_next/data/x", 404],
    ["/_next/image?url=x", 404],
    [`/explore?family=${"a".repeat(7000)}`, 200],
  ] as const) {
    test(`${target.slice(0, 40)} is ${status} with every header`, async () => {
      const response = await raw("GET", target);
      expect(response.status).toBe(status);
      expect(policy(response.headers)).toEqual(FULL);
    });
  }

  test("owned images carry the policy and are the only cacheable proxied class", async () => {
    for (const target of ["/studies/hero.svg", "/icon.svg"]) {
      const response = await raw("GET", target);
      expect(response.status).toBe(200);
      expect(policy(response.headers)).toEqual({ ...FULL, noStore: false });
    }
  });

  for (const method of ["POST", "PUT", "PATCH", "DELETE", "OPTIONS"]) {
    test(`${method} is refused without a body and changes nothing`, async () => {
      // Scripts carry the nonce and per-render framework values, which differ between any two reads.
      const text = async (path: string) =>
        (await raw("GET", path)).body.replace(/<script\b[\s\S]*?<\/script>/g, "").replace(/nonce="[^"]*"/g, "");
      const paths = ["/", "/explore", "/perfume/paper-study-a", "/notes"];
      const before = await Promise.all(paths.map(text));
      expect(before.every((html) => html.includes("<h1"))).toBe(true);
      for (const target of [...paths, "/explore/", "/nope", "/explore?family=mock-family-soft", "/studies/hero.svg"]) {
        const response = await raw(method, target);
        expect(response.status, target).toBe(405);
        expect(response.headers.allow, target).toBe("GET, HEAD");
        expect(response.body, target).toBe("");
        expect(policy(response.headers), target).toEqual({ ...FULL, noStore: !target.startsWith("/studies/") });
        expect(response.headers["set-cookie"], target).toBeUndefined();
      }
      expect(await Promise.all(paths.map(text))).toEqual(before);
    });
  }

  test("HEAD answers like GET without a body", async () => {
    const response = await raw("HEAD", "/explore");
    expect(response.status).toBe(200);
    expect(response.body).toBe("");
    expect(policy(response.headers)).toEqual(FULL);
  });
});

/**
 * KNOWN LIMITATION, not a pass: these responses never reach src/proxy.ts, and most never reach the
 * next.config.ts headers. The missing headers are asserted so that a change in the framework or in Node
 * is noticed and the records are corrected. Nothing here may be reported as universal header coverage.
 */
test.describe("known exceptions answered before the proxy", () => {
  for (const [target, location, final] of [
    ["//example.test/", "/example.test/", 404],
    ["///example.test//", "/example.test/", 404],
    ["/\\example.test/", "/example.test/", 404],
    ["/about//", "/about/", 200],
    ["//explore", "/explore", 200],
  ] as const) {
    test(`framework repeated-slash redirect ${target} stays on this origin but has no headers`, async () => {
      const first = await raw("GET", target);
      expect(first.status).toBe(308);
      expect(first.headers.location).toBe(location);
      expect(new URL(location, ORIGIN).origin).toBe(ORIGIN);
      expect(policy(first.headers)).toEqual(NONE);
      // Every later hop, and the page that is finally shown, do carry them.
      let hop = first;
      for (let i = 0; i < 3 && hop.headers.location; i += 1) {
        hop = await raw("GET", hop.headers.location);
        expect(policy(hop.headers)).toEqual(FULL);
      }
      expect(hop.status).toBe(final);
    });
  }

  test("an absolute-form target is answered with the sender's own target", async () => {
    // Browsers send this form only to a configured forward proxy, never to this server.
    const response = await raw("GET", "http://example.test/explore/");
    expect(response.status).toBe(308);
    expect(response.headers.location).toBe("http://example.test/explore/");
    expect(policy(response.headers)).toEqual(NONE);
  });

  test("a request line above Node's header limit is a bare 431", async () => {
    const response = await raw("GET", `/explore?family=${"a".repeat(20_000)}`);
    expect(response.status).toBe(431);
    expect(response.body).toBe("");
    expect(policy(response.headers)).toEqual(NONE);
  });

  test("TRACE and the asterisk target are a framework 500 without page content", async () => {
    for (const [method, target] of [["TRACE", "/explore"], ["GET", "*"]] as const) {
      const response = await raw(method, target);
      expect(response.status).toBe(500);
      expect(response.body).toBe("Internal Server Error");
      expect(policy(response.headers)).toEqual({ ...NONE, noStore: true });
    }
  });

  test("hashed framework assets carry noindex and nosniff but no policy or no-store", async () => {
    const page = await raw("GET", "/");
    const asset = /\/_next\/static\/[^"]+\.js/.exec(page.body)![0];
    const response = await raw("GET", asset);
    expect(response.status).toBe(200);
    expect(policy(response.headers)).toEqual({ csp: false, noindex: true, nosniff: true, noStore: false });
  });
});
