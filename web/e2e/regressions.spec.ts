/** Regressions for the independent review findings on f04d912 (CR = code review, DR = design review). */
import AxeBuilder from "@axe-core/playwright";
import type { Page } from "@playwright/test";
import { expect, focused, ready, test } from "./helpers";

const primary = (page: Page, name: string) =>
  page.getByRole("navigation", { name: "Primary" }).getByRole("link", { name });

test("CR1 Back works after the skip link", async ({ page }) => {
  await ready(page, "/explore");
  await page.locator("main input").fill("glass");
  await page.getByRole("link", { name: "Skip to content" }).focus();
  await page.keyboard.press("Enter");
  await expect(page.locator("#main-content")).toBeFocused();
  await page.getByRole("link", { name: "Glass study H" }).click();
  await expect(page.locator("h1")).toHaveText("Glass study H");
  await page.goBack();
  await expect(page.locator("h1")).toHaveText("Explore mock fragrances");
  await expect(page.locator("main input")).toHaveValue("glass");
});

test("CR1 Back works after an on-page About link, and same-page fragments take focus", async ({ page }) => {
  await ready(page, "/about");
  await page.getByRole("navigation", { name: "On this page" }).getByRole("link", { name: "The scent notebook" }).click();
  await expect(page).toHaveURL(/#journal$/);
  await expect.poll(() => focused(page)).toBe("journal");
  await page.getByRole("contentinfo").getByRole("link", { name: "Mock scope" }).click();
  await expect.poll(() => focused(page)).toBe("scope");
  await expect(page.locator("#scope")).toBeInViewport();
  await primary(page, "Notes").click();
  await expect(page.locator("h1")).toHaveText("Notes");
  await page.goBack();
  await expect(page.locator("h1")).toHaveText("A notebook that says what it does not know.");
});

for (const [start, heading] of [["/explore?utm=1", "Explore mock fragrances"], ["/about?x=1", "A notebook that says what it does not know."]] as const) {
  test(`CR2 Back works after query keys were stripped from ${start}`, async ({ page }) => {
    await ready(page, start);
    await expect(page).toHaveURL(start.split("?")[0]!);
    await primary(page, "Notes").click();
    await expect(page.locator("h1")).toHaveText("Notes");
    await page.goBack();
    await expect(page.locator("h1")).toHaveText(heading);
    await expect(page).toHaveURL(start.split("?")[0]!);
  });
}

test("CR3 a malformed slug is a 404 with the response headers", async ({ request }) => {
  const response = await request.get("http://localhost:3000/perfume/%E0%A4%A");
  expect(response.status()).toBe(404);
  expect(response.headers()["x-robots-tag"]).toContain("noindex");
});

for (const path of ["/studies/nope", "/studies/nope.svg", "/icon.svgx"]) {
  test(`CR4 ${path} 404 carries the nonce policy`, async ({ request }) => {
    const response = await request.get(path);
    expect(response.status()).toBe(404);
    const nonce = /'nonce-([^']+)'/.exec(response.headers()["content-security-policy"] ?? "")?.[1];
    expect(nonce).toBeTruthy();
    expect(response.headers()["cache-control"]).toContain("no-store");
    for (const tag of (await response.text()).match(/<script\b[^>]*>/g) ?? []) expect(tag).toContain(`nonce="${nonce}"`);
  });
}

for (const name of ["Search mock catalogue", "Profile unavailable in this mock"]) {
  test(`CR5/DR2 focus returns to "${name}" when the click did not focus it`, async ({ page }) => {
    await ready(page, "/");
    const button = page.getByRole("button", { name });
    await button.evaluate((el) => (el as HTMLElement).click());
    await expect(page.getByRole("dialog")).toBeVisible();
    await page.keyboard.press("Escape");
    await expect(button).toBeFocused();
  });
}

test("CR6 Notes filters survive Back", async ({ page }) => {
  await ready(page, "/notes");
  await page.getByLabel("Family", { exact: true }).selectOption("mock-family-soft");
  await page.locator("main input").fill("wax");
  await page.locator("[data-note='mock-note-006'] a", { hasText: "Browse" }).click();
  await expect(page.locator("[data-entry]")).toHaveCount(6);
  await page.goBack();
  await expect(page.locator("main input")).toHaveValue("wax");
  await expect(page.getByLabel("Family", { exact: true })).toHaveValue("mock-family-soft");
  await expect.poll(() => focused(page)).toBe("browse-mock-note-006");
});

test("CR6 an entry inside a disclosure regains focus without a false message", async ({ page }) => {
  await ready(page, "/notes");
  await page.locator("[data-note='mock-note-001'] summary").click();
  await page.locator("[data-note='mock-note-001'] details a", { hasText: "Paper study B" }).click();
  await expect(page.locator("h1")).toHaveText("Paper study B");
  await page.goBack();
  await expect.poll(() => focused(page)).toBe("listed-mock-note-001-paper-study-b");
  await expect(page.getByText("no longer in this list")).toHaveCount(0);
});

test("CR7 two Explore visits keep separate state", async ({ page }) => {
  await ready(page, "/explore");
  await page.locator("main input").fill("glass");
  await page.getByRole("link", { name: "Glass study G" }).click();
  await expect(page.locator("h1")).toHaveText("Glass study G");
  await page.getByRole("navigation", { name: "Breadcrumb" }).getByRole("link", { name: "Explore" }).click();
  await expect(page.locator("main input")).toHaveValue("");
  await page.goBack();
  await expect(page.locator("h1")).toHaveText("Glass study G");
  await page.goBack();
  await expect(page.locator("main input")).toHaveValue("glass");
  await expect.poll(() => focused(page)).toBe("entry-glass-study-g");
  await page.goForward();
  await expect(page.locator("h1")).toHaveText("Glass study G");
  await page.goForward();
  await expect(page.locator("main input")).toHaveValue("");
});

test("CR11 the pending state clears when a slow transition is abandoned", async ({ page }) => {
  await page.route(/_rsc=/, async (r) => {
    await new Promise((done) => setTimeout(done, 1500));
    await r.continue().catch(() => undefined);
  });
  await ready(page, "/explore");
  await primary(page, "Notes").click();
  await expect(page.locator("[data-route-pending]")).toHaveText("Opening the next page");
  await primary(page, "Explore").click();
  await expect(page.locator("[data-route-pending]")).toHaveText("", { timeout: 800 });
  await expect(page.locator("main")).not.toHaveAttribute("aria-busy", "true");
});

test("CR12 Clear all resets sort, and a fresh same-path visit resets the query", async ({ page }) => {
  await ready(page, "/explore?family=mock-family-soft");
  await page.locator("main input").fill("linen");
  const sort = page.locator("main").getByLabel("Sort", { exact: true });
  await sort.selectOption("name-desc");
  await page.getByRole("button", { name: "Clear all" }).click();
  await expect(sort).toHaveValue("name-asc");
  await sort.selectOption("name-desc");
  await expect(page.getByRole("button", { name: "Clear all" })).toBeVisible();
  await page.locator("main").getByLabel("Family", { exact: true }).selectOption("mock-family-deep");
  await page.locator("main input").fill("stone");
  await primary(page, "Explore").click();
  await expect(page).toHaveURL(/\/explore$/);
  await expect(page.locator("main input")).toHaveValue("");
  await expect(page.locator("[data-entry]")).toHaveCount(12);
});

test("CR10 a render failure offers a Retry that recovers", async ({ page, problems }) => {
  await ready(page, "/explore");
  await page.evaluate(() => {
    const original = Object.getOwnPropertyDescriptor(Intl.Collator.prototype, "compare")!;
    Object.assign(window, { restoreCollator: () => Object.defineProperty(Intl.Collator.prototype, "compare", original) });
    Object.defineProperty(Intl.Collator.prototype, "compare", { configurable: true, get: () => { throw new Error("probe"); } });
  });
  await page.locator("main input").fill("stone");
  await expect(page.getByRole("heading", { name: "This page could not be shown" })).toBeVisible();
  await expect(page.getByRole("link", { name: "Return to Explore" })).toBeVisible();
  expect(await page.locator("main").innerText()).not.toContain("probe");
  await page.evaluate(() => (window as unknown as { restoreCollator: () => void }).restoreCollator());
  await page.getByRole("button", { name: "Retry" }).click();
  await expect(page.locator("[data-entry]")).toHaveCount(12);
  problems.length = 0;
});

for (const [width, height, names] of [
  [375, 812, ["Menu", "Search mock catalogue", "Profile unavailable in this mock"]],
  [320, 640, ["Menu", "Search mock catalogue", "Profile unavailable in this mock"]],
  [1024, 768, ["Search mock catalogue", "Profile unavailable in this mock"]],
] as const) {
  test(`DR1 dialogs stay inside the visible area at ${width}`, async ({ page }) => {
    await page.setViewportSize({ width, height });
    await page.emulateMedia({ reducedMotion: "reduce" });
    await ready(page, "/");
    for (const name of names) {
      await page.getByRole("button", { name }).click();
      const box = await page.getByRole("dialog").evaluate((panel) => {
        const limit = document.documentElement.clientWidth - (window.innerWidth - document.body.getBoundingClientRect().right);
        const inner = [...panel.querySelectorAll("*")].map((el) => el.getBoundingClientRect().right);
        return { panel: panel.getBoundingClientRect().right, inner: Math.max(...inner), limit: Math.min(limit, document.body.getBoundingClientRect().right) };
      });
      expect(box.panel, name).toBeLessThanOrEqual(box.limit + 0.5);
      expect(box.inner, name).toBeLessThanOrEqual(box.panel + 0.5);
      const results = await new AxeBuilder({ page }).withTags(["wcag2a", "wcag2aa", "wcag21a", "wcag21aa"]).analyze();
      expect(results.violations.map((v) => v.id), name).toEqual([]);
      await page.keyboard.press("Escape");
      await expect(page.getByRole("dialog")).toHaveCount(0);
    }
  });
}

test("Menu traps Tab in both directions", async ({ page }) => {
  await page.setViewportSize({ width: 375, height: 700 });
  await ready(page, "/");
  await page.getByRole("button", { name: "Menu" }).click();
  for (let i = 0; i < 16; i += 1) {
    await page.keyboard.press(i < 8 ? "Tab" : "Shift+Tab");
    expect(await page.evaluate(() => !!document.activeElement?.closest("[role='dialog']"))).toBe(true);
  }
});

test("DR4 an unsupplied note relationship is not reported as zero", async ({ page }) => {
  await ready(page, "/explore?note=mock-note-009");
  await expect(page.getByText("Relationship not supplied for Vesk in this mock")).toBeVisible();
  await expect(page.locator("main")).not.toContainText("0 mock studies");
  await page.getByRole("button", { name: "Clear filters" }).click();
  await expect(page.locator("[data-entry]")).toHaveCount(12);
});

test("DR5 an unavailable visual is not captioned as a visual study", async ({ page }) => {
  await page.goto("/perfume/paper-study-a");
  await expect(page.locator("[data-visual-fallback]")).toBeVisible();
  await expect(page.getByText("Synthetic visual study")).toHaveCount(0);
  await page.goto("/perfume/paper-study-b");
  await expect(page.getByText("Synthetic visual study")).toBeVisible();
});

test("DR7 every folio layer says it belongs to the mock and labels its drawing", async ({ page }) => {
  await page.goto("/");
  const layers = page.locator(".folio-layer");
  await expect(layers).toHaveCount(3);
  for (const layer of await layers.all()) {
    await expect(layer).toContainText(/in this mock/i);
    await expect(layer).toContainText(/illustrative drawing/i);
  }
});

test("DR8 Notes group letters are headings and groups are not landmarks", async ({ page }) => {
  await page.goto("/notes");
  await expect(page.locator("main").getByRole("heading", { level: 3 })).toHaveText(["I", "L", "M", "O", "Q", "S", "T", "V"]);
  await expect(page.locator("main").getByRole("heading", { level: 4 })).toHaveCount(9);
  await expect(page.locator("main").getByRole("region")).toHaveCount(0);
});

test("DR11 paired controls align at tablet width", async ({ page }) => {
  await page.setViewportSize({ width: 768, height: 900 });
  await ready(page, "/notes");
  const tops = await page.locator("main input, main select").evaluateAll((els) => els.map((e) => Math.round(e.getBoundingClientRect().top)));
  expect(new Set(tops).size).toBe(1);
});
