/** Regressions for the S2 refinement pass. Each one failed on 94820c2 before its correction, except the
 * UX12 guard, which S3 made sensitive to its own removal. The redirect origin test is in headers.spec.ts
 * and the visible-scrollbar half of UX2 is in scrollbar.spec.ts. */
import type { Page } from "@playwright/test";
import { expect, ORIGIN, ready, test } from "./helpers";

const box = (page: Page, selector: string) =>
  page.locator(selector).first().evaluate((el) => {
    const { top, bottom, left, right, width, height } = el.getBoundingClientRect();
    return { top, bottom, left, right, width, height };
  });

test("UX1 a late stylesheet does not animate the page in from browser defaults", async ({ page }) => {
  await page.route(/_next\/static\/.*\.css/, async (r) => {
    await new Promise((done) => setTimeout(done, 700));
    await r.continue();
  });
  await page.addInitScript(() => {
    const log: string[] = [];
    Object.assign(window, { transitions: log });
    document.addEventListener("transitionrun", (e) => log.push(`${e.propertyName} ${(e.target as Element).tagName}`), true);
  });
  await ready(page, "/");
  await page.waitForTimeout(500);
  expect(await page.evaluate(() => (window as unknown as { transitions: string[] }).transitions)).toEqual([]);
  // Feedback still animates once the page is ready.
  await page.getByRole("link", { name: "Explore mock catalogue" }).hover();
  await expect
    .poll(() => page.evaluate(() => (window as unknown as { transitions: string[] }).transitions.length))
    .toBeGreaterThan(0);
});

for (const path of ["/", "/perfume/nope"]) {
  test(`UX2 opening a dialog does not move the page (${path})`, async ({ page, problems }) => {
    await ready(page, path);
    const before = await box(page, "[data-header-nav]");
    await page.getByRole("button", { name: "Search mock catalogue" }).click();
    await expect(page.getByRole("dialog")).toBeVisible();
    expect((await box(page, "[data-header-nav]")).left).toBeCloseTo(before.left, 1);
    await page.keyboard.press("Escape");
    expect((await box(page, "[data-header-nav]")).left).toBeCloseTo(before.left, 1);
    problems.splice(0, problems.length, ...problems.filter((p) => !/status of 404/.test(p)));
  });
}

test("UX3 the current-page weight does not move the navigation labels", async ({ page }) => {
  const seen = new Set<string>();
  for (const path of ["/", "/explore", "/notes", "/about"]) {
    await ready(page, path);
    const lefts = await page
      .locator("[data-header-nav] a")
      .evaluateAll((els) => els.map((e) => e.getBoundingClientRect().left.toFixed(1)));
    seen.add(lefts.join(" "));
  }
  expect([...seen]).toHaveLength(1);
});

test("UX4 a malformed address shows the unavailable view", async ({ request, page, problems }) => {
  const path = `${ORIGIN}/perfume/%E0%A4%A`;
  const response = await request.get(path);
  expect(response.status()).toBe(404);
  expect(response.headers()["cache-control"]).toContain("no-store");
  expect(response.headers()["x-robots-tag"]).toContain("noindex");
  const nonce = /script-src 'self' 'nonce-([^']+)'/.exec(response.headers()["content-security-policy"] ?? "")?.[1];
  const html = await response.text();
  expect(html).toContain("This page is unavailable");
  for (const tag of html.match(/<script\b[^>]*>/g) ?? []) expect(tag).toContain(`nonce="${nonce}"`);
  await page.goto(path);
  await expect(page.locator("[data-state='unavailable'] h1")).toBeVisible();
  await page.getByRole("link", { name: "Return to the mock catalogue" }).click();
  await expect(page.locator("h1")).toHaveText("Explore mock fragrances");
  problems.splice(0, problems.length, ...problems.filter((p) => !/status of 404/.test(p)));
});

for (const [path, target] of [["/explore/", "/explore"], ["/about/?x=1", "/about?x=1"], ["/perfume/paper-study-b/", "/perfume/paper-study-b"]] as const) {
  test(`UX5 ${path} redirects locally with noindex and no-store`, async ({ request }) => {
    const response = await request.get(path, { maxRedirects: 0 });
    expect(response.status()).toBe(308);
    const location = response.headers()["location"]!;
    expect(new URL(location, ORIGIN).href).toBe(`${ORIGIN}${target}`);
    expect(response.headers()["x-robots-tag"]).toContain("noindex");
    expect(response.headers()["cache-control"]).toContain("no-store");
    expect(response.headers()["content-security-policy"]).toContain("default-src 'self'");
  });
}

test("UX6 an unavailable filter is not counted as zero studies", async ({ page }) => {
  await ready(page, "/explore?family=x");
  await expect(page.locator("main [data-count]")).toHaveText("Filter unavailable");
  await expect(page.locator("main")).not.toContainText("0 mock studies");
});

for (const [width, height] of [[1440, 900], [375, 812]] as const) {
  test(`UX7 the footer closes a short page at ${width}`, async ({ page, problems }) => {
    await page.setViewportSize({ width, height });
    await ready(page, "/perfume/nope");
    const footer = await box(page, "footer");
    expect(Math.abs(footer.bottom - height)).toBeLessThanOrEqual(1);
    expect(await page.evaluate(() => document.documentElement.scrollHeight)).toBe(height);
    problems.splice(0, problems.length, ...problems.filter((p) => !/status of 404/.test(p)));
  });
}

test("UX8 the hero keeps Featured in the first view and takes its full padding when there is room", async ({ page }) => {
  const measure = async (width: number, height: number) => {
    await page.setViewportSize({ width, height });
    await ready(page, "/");
    return page.evaluate(() => {
      const style = getComputedStyle(document.querySelector("[data-hero]")!);
      const heading = document.querySelector("#featured-heading")!.getBoundingClientRect();
      return { top: style.paddingTop, bottom: style.paddingBottom, heading: heading.bottom, view: innerHeight };
    });
  };
  const compact = await measure(1440, 900);
  expect(compact.heading).toBeLessThanOrEqual(compact.view);
  expect(parseFloat(compact.bottom)).toBeGreaterThanOrEqual(40);
  for (const [w, h] of [[1440, 1080], [1920, 1200]] as const) {
    const full = await measure(w, h);
    expect([full.top, full.bottom], `${w}x${h}`).toEqual(["80px", "80px"]);
    expect(full.heading, `${w}x${h}`).toBeLessThanOrEqual(full.view);
  }
});

test("UX9 Featured is a level grid on desktop and leaves no orphan on two columns", async ({ page }) => {
  await page.setViewportSize({ width: 1440, height: 900 });
  await ready(page, "/");
  const tops = await page
    .locator("[aria-labelledby='featured-heading'] li")
    .evaluateAll((els) => els.map((e) => Math.round(e.getBoundingClientRect().top)));
  expect(new Set(tops).size).toBe(1);
  for (const width of [768, 640, 520]) {
    await page.setViewportSize({ width, height: 1024 });
    await ready(page, "/");
    const list = await box(page, "[aria-labelledby='featured-heading'] ul");
    const last = page.locator("[aria-labelledby='featured-heading'] li").last();
    const item = await last.evaluate((e) => e.getBoundingClientRect().width);
    expect(Math.abs(item - list.width), String(width)).toBeLessThanOrEqual(1);
    const parts = await last.evaluate((e) => {
      const visual = e.querySelector("img")!.getBoundingClientRect();
      const title = e.querySelector("h3")!.getBoundingClientRect();
      const meta = [...e.querySelectorAll("p")].at(-1)!.getBoundingClientRect();
      return {
        ratio: visual.width / visual.height,
        beside: title.left >= visual.right && meta.left >= visual.right,
        inside: title.top >= visual.top && meta.bottom <= visual.bottom + 1,
      };
    });
    expect(parts.ratio, String(width)).toBeCloseTo(0.8, 1);
    expect(parts.beside && parts.inside, String(width)).toBe(true);
    await expect(last.getByRole("link", { name: "Stone study J", exact: true })).toBeVisible();
  }
});

test("UX10 note descriptions share one column on Detail", async ({ page }) => {
  await page.setViewportSize({ width: 1440, height: 900 });
  await ready(page, "/perfume/stone-study-j");
  const lefts = await page
    .locator("[data-layer='base'] li > span")
    .evaluateAll((els) => els.map((e) => Math.round(e.getBoundingClientRect().left)));
  expect(lefts.length).toBe(3);
  expect(new Set(lefts).size).toBe(1);
});

test("UX11 the Detail name starts level with its visual on desktop", async ({ page }) => {
  for (const [width, height] of [[1440, 900], [1024, 768]] as const) {
    await page.setViewportSize({ width, height });
    await ready(page, "/perfume/paper-study-b");
    const visual = await box(page, "main figure img");
    const marker = await box(page, "[data-mock-marker]");
    expect(Math.abs(marker.top - visual.top)).toBeLessThanOrEqual(8);
    expect((await box(page, "main h1")).bottom).toBeLessThan(height);
  }
});

test("UX13 forced colors still mark only the current page in the navigation", async ({ page }) => {
  await page.emulateMedia({ forcedColors: "active" });
  await ready(page, "/explore");
  const borders = await page
    .locator("[data-header-nav] .nav-label, [data-header-nav] a > span")
    .evaluateAll((els) => els.map((e) => getComputedStyle(e).borderBottomColor));
  const canvas = await page.evaluate(() => getComputedStyle(document.body).backgroundColor);
  expect(borders.map((c) => c !== canvas)).toEqual([false, true, false, false]);
});

test("UX12 a malformed fragment does not break navigation", async ({ page }) => {
  await ready(page, "/about#%E0%A4%A");
  // A same-page link is decoded in the click handler; an unguarded decode is a page error here.
  await page.evaluate(() => {
    const link = document.createElement("a");
    link.href = "#%E0%A4%A";
    link.textContent = "Malformed fragment";
    document.querySelector("main h1")!.after(link);
  });
  await page.getByRole("link", { name: "Malformed fragment" }).click();
  await page.getByRole("navigation", { name: "Primary" }).getByRole("link", { name: "Notes" }).click();
  await expect(page.locator("h1")).toBeFocused();
  await page.goBack();
  await expect(page.locator("h1")).toHaveText("A notebook that says what it does not know.");
});
