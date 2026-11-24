import { expect, ORIGIN, ready, ROUTES, test } from "./helpers";

const FORBIDDEN = /paper-study|mock-perfume-0|mock-note-0|Ivrel|Luthmere|mock atelier/;

test.describe("A06 isolation, cache and network", () => {
  for (const { path } of [...ROUTES, { path: "/perfume/nope" }]) {
    test(`${path} headers: nonce CSP, no-store, noindex`, async ({ request }) => {
      const first = await request.get(path);
      const second = await request.get(path);
      const h = first.headers();
      const csp = h["content-security-policy"] ?? "";
      expect(h["cache-control"]).toContain("no-store");
      expect(h["x-robots-tag"]).toContain("noindex");
      expect(h["x-powered-by"]).toBeUndefined();
      for (const part of ["default-src 'self'", "object-src 'none'", "frame-src 'none'", "frame-ancestors 'none'", "form-action 'none'", "base-uri 'self'", "connect-src 'self'", "font-src 'self'", "img-src 'self'", "worker-src 'none'"]) {
        expect(csp).toContain(part);
      }
      expect(csp).not.toMatch(/unsafe-inline|unsafe-eval|strict-dynamic|https?:|ws:|\*/);
      const nonce = /script-src 'self' 'nonce-([^']+)'/.exec(csp)?.[1];
      expect(nonce).toBeTruthy();
      expect(second.headers()["content-security-policy"]).not.toContain(nonce!);
      const html = await first.text();
      for (const tag of html.match(/<script\b[^>]*>/g) ?? []) expect(tag).toContain(`nonce="${nonce}"`);
      expect(html).not.toMatch(/\sstyle="/);
      expect(html).not.toMatch(/<style(?![^>]*nonce)/);
    });

    test(`${path} RSC response is no-store`, async ({ request }) => {
      const response = await request.get(`${path}?_rsc=probe`, { headers: { RSC: "1" } });
      expect(response.headers()["content-type"]).toContain("text/x-component");
      expect(response.headers()["cache-control"]).toContain("no-store");
      expect(response.headers()["x-robots-tag"]).toContain("noindex");
    });
  }

  test("a full session stays same-origin, writes no storage and registers no worker", async ({ page, context }) => {
    const requests: { url: string; method: string }[] = [];
    page.on("request", (r) => requests.push({ url: r.url(), method: r.method() }));
    await ready(page, "/");
    await page.getByRole("button", { name: "Search mock catalogue" }).click();
    await page.getByRole("dialog").getByRole("textbox").fill("glass");
    await page.keyboard.press("Escape");
    await page.getByRole("button", { name: "Profile unavailable in this mock" }).click();
    await page.keyboard.press("Escape");
    for (const name of ["Explore", "Notes", "About", "Home"]) {
      await page.getByRole("navigation", { name: "Primary" }).getByRole("link", { name }).click();
      await expect(page.locator("h1")).toBeFocused();
    }
    await page.getByRole("link", { name: "Soft study" }).click();
    await page.locator("main").getByLabel("Note", { exact: true }).selectOption("mock-note-002");
    await page.locator("main input").fill("linen");
    await page.getByRole("link", { name: "Linen study E" }).click();
    await expect(page.locator("h1")).toHaveText("Linen study E");

    for (const r of requests) {
      expect(new URL(r.url).origin).toBe(ORIGIN);
      expect(r.method).toBe("GET");
      expect(decodeURIComponent(r.url)).not.toMatch(/glass(?!-)|q=|query/);
    }
    const stored = await page.evaluate(async () => ({
      local: localStorage.length,
      session: sessionStorage.length,
      databases: (await indexedDB.databases()).length,
      caches: (await caches.keys()).length,
      workers: (await navigator.serviceWorker.getRegistrations()).length,
      cookies: document.cookie,
    }));
    expect(stored).toEqual({ local: 0, session: 0, databases: 0, caches: 0, workers: 0, cookies: "" });
    expect(await context.cookies()).toEqual([]);
  });

  test("immutable assets carry no fixture payload", async ({ page, request }) => {
    const assets = new Map<string, string>();
    for (const { path } of ROUTES) {
      const urls: string[] = [];
      const collect = (r: { url: () => string }) => {
        if (r.url().includes("/_next/static/") && /\.(js|css)(\?|$)/.test(r.url())) urls.push(r.url());
      };
      page.on("request", collect);
      await ready(page, path);
      page.off("request", collect);
      for (const url of urls) {
        if (!assets.has(url)) assets.set(url, await (await request.get(url)).text());
      }
    }
    expect(assets.size).toBeGreaterThan(3);
    for (const [url, text] of assets) {
      expect(text.length, url).toBeGreaterThan(100);
      expect(FORBIDDEN.test(text), url).toBe(false);
    }
  });

  test("the app exposes no extra endpoint and ignores writes", async ({ request }) => {
    for (const path of ["/api", "/api/health", "/robots.txt", "/sitemap.xml", "/sw.js", "/manifest.json", "/_next/image?url=%2Fstudies%2Fhero.svg&w=640&q=75"]) {
      expect((await request.get(path)).status(), path).toBe(404);
    }
    const post = await request.post("/explore", { form: { q: "probe-value" } });
    expect(post.headers()["cache-control"]).toContain("no-store");
    expect(await post.text()).not.toContain("probe-value");
  });
});

test.describe("A12 performance and motion", () => {
  for (const { path } of ROUTES) {
    test(`${path} initial JS and layout shift within budget`, async ({ page }, info) => {
      let bytes = 0;
      const session = await page.context().newCDPSession(page);
      await session.send("Network.enable");
      const scripts = new Set<string>();
      session.on("Network.responseReceived", (e) => {
        if (e.type === "Script") scripts.add(e.requestId);
      });
      session.on("Network.loadingFinished", (e) => {
        if (scripts.has(e.requestId)) bytes += e.encodedDataLength;
      });
      await page.addInitScript(() => {
        Object.assign(window, { cls: 0 });
        new PerformanceObserver((list) => {
          for (const entry of list.getEntries() as unknown as { value: number; hadRecentInput: boolean }[]) {
            if (!entry.hadRecentInput) (window as unknown as { cls: number }).cls += entry.value;
          }
        }).observe({ type: "layout-shift", buffered: true });
      });
      await ready(page, path);
      await page.evaluate(async () => {
        for (let y = 0; y < document.body.scrollHeight; y += 500) {
          scrollTo(0, y);
          await new Promise((r) => setTimeout(r, 60));
        }
      });
      const cls = await page.evaluate(() => (window as unknown as { cls: number }).cls);
      info.annotations.push({ type: "metric", description: `js=${(bytes / 1024).toFixed(1)}KiB cls=${cls.toFixed(4)}` });
      expect(bytes).toBeLessThanOrEqual(200 * 1024);
      expect(bytes).toBeGreaterThan(0);
      expect(cls).toBeLessThanOrEqual(0.1);
    });
  }

  test("a slow transition states that it is opening and then clears", async ({ page }) => {
    await page.route(/_rsc=/, async (r) => {
      await new Promise((done) => setTimeout(done, 900));
      await r.continue();
    });
    await ready(page, "/");
    await page.getByRole("navigation", { name: "Primary" }).getByRole("link", { name: "Notes" }).click();
    await expect(page.locator("[data-route-pending]")).toHaveText("Opening the next page");
    await expect(page.locator("main")).toHaveAttribute("aria-busy", "true");
    await expect(page.locator("h1")).toHaveText("A personal atlas of scent.");
    await expect(page.locator("h1")).toHaveText("Notes");
    await expect(page.locator("[data-route-pending]")).toHaveText("");
    await expect(page.locator("main")).not.toHaveAttribute("aria-busy", "true");
    await expect(page.locator("h1")).toBeFocused();
  });

  test("reduced motion removes panel and folio movement", async ({ page }) => {
    await page.emulateMedia({ reducedMotion: "reduce" });
    await ready(page, "/");
    await expect(page.locator("[data-armed]")).toHaveCount(0);
    await page.getByRole("button", { name: "Profile unavailable in this mock" }).click();
    const running = await page.evaluate(() => document.getAnimations().filter((a) => a.effect!.getComputedTiming().duration as number > 1).length);
    expect(running).toBe(0);
    await page.keyboard.press("Escape");
    await expect(page.locator("[data-panel-copy]")).toHaveCount(0);
  });

  test("with motion, folio layers settle once and end fully visible", async ({ page }) => {
    await ready(page, "/");
    await expect(page.locator("[data-armed]")).toHaveCount(3);
    await page.locator("#folio-heading").scrollIntoViewIfNeeded();
    for (let i = 0; i < 8; i += 1) await page.mouse.wheel(0, 300).then(() => page.waitForTimeout(80));
    await expect(page.locator("[data-armed]")).toHaveCount(0);
    await page.waitForTimeout(300);
    for (const li of await page.locator(".folio-layer").all()) await expect(li).toHaveCSS("opacity", "1");
  });

  for (const width of [375, 320]) {
    test(`without scripting the four routes stay reachable from the header at ${width}`, async ({ browser }) => {
      const context = await browser.newContext({ javaScriptEnabled: false, viewport: { width, height: 800 }, baseURL: ORIGIN });
      const page = await context.newPage();
      await page.goto("/explore");
      const nav = page.getByRole("navigation", { name: "Primary" });
      await expect(nav.getByRole("link")).toHaveText(["Home", "Explore", "Notes", "About"]);
      await expect(nav.getByRole("link", { name: "Explore" })).toHaveAttribute("aria-current", "page");
      // The drawer cannot open without scripting, so its trigger is not offered.
      await expect(page.getByRole("button", { name: "Menu" })).toHaveCount(0);
      for (const link of await nav.getByRole("link").all()) {
        const size = (await link.boundingBox())!;
        expect(Math.min(size.width, size.height)).toBeGreaterThanOrEqual(43.5);
        expect(size.x + size.width).toBeLessThanOrEqual(width);
      }
      const brand = (await page.locator("[data-header-brand]").boundingBox())!;
      expect((await nav.boundingBox())!.y).toBeGreaterThanOrEqual(brand.y + brand.height);
      for (const [name, path] of [["Notes", "/notes"], ["About", "/about"], ["Home", "/"], ["Explore", "/explore"]] as const) {
        await nav.getByRole("link", { name }).focus();
        await page.keyboard.press("Enter");
        await expect(page).toHaveURL(`${ORIGIN}${path}`);
      }
      await context.close();
    });
  }

  test("without scripting the content is still complete", async ({ browser }) => {
    const context = await browser.newContext({ javaScriptEnabled: false });
    const page = await context.newPage();
    for (const { path } of ROUTES) {
      await page.goto(`${ORIGIN}${path}`);
      await expect(page.locator("h1")).toBeVisible();
    }
    await page.goto(`${ORIGIN}/explore`);
    await expect(page.locator("[data-entry]").first()).toBeVisible();
    await context.close();
  });
});
