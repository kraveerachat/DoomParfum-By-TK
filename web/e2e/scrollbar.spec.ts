/**
 * Scroll lock with real scrollbars. Headless Chrome hides scrollbars by default, which hides a missing
 * gutter too, so this file runs in a browser that shows them and asserts that state first.
 */
import type { Page } from "@playwright/test";
import { expect, ready, test } from "./helpers";

test.use({ launchOptions: { ignoreDefaultArgs: ["--hide-scrollbars"] } });

const scrollbar = (page: Page) => page.evaluate(() => innerWidth - document.documentElement.clientWidth);
const lefts = (page: Page) =>
  page
    .locator("[data-header-brand], [data-header-nav], [data-header-utils], main h1, footer li")
    .evaluateAll((els) => els.map((e) => Math.round(e.getBoundingClientRect().left * 10) / 10));
const lock = (page: Page) =>
  page.evaluate(() => {
    const root = document.documentElement;
    return { value: root.getAttribute("data-overlay"), overflow: getComputedStyle(root).overflowY };
  });
/** Small enough to leave the header controls whole, so the click itself does not scroll. */
const START = 16;
const wheel = async (page: Page) => {
  await page.mouse.move(8, 400);
  await page.mouse.wheel(0, 300);
  await page.waitForTimeout(250);
  return page.evaluate(() => scrollY);
};

for (const [path, shown] of [["/", true], ["/perfume/nope", false]] as const) {
  for (const width of [1440, 1280, 768]) {
    test(`UX2 ${path} at ${width} does not move when a dialog opens or closes`, async ({ page, problems }) => {
      await page.setViewportSize({ width, height: 900 });
      await ready(page, path);
      expect((await scrollbar(page)) > 0).toBe(shown);
      const before = await lefts(page);
      for (const name of ["Search mock catalogue", "Profile unavailable in this mock"]) {
        await page.getByRole("button", { name }).click();
        await expect(page.getByRole("dialog")).toBeVisible();
        expect(await lock(page)).toEqual({ value: shown ? "gutter" : "", overflow: "hidden" });
        expect(await lefts(page)).toEqual(before);
        await page.keyboard.press("Escape");
        await expect(page.getByRole("dialog")).toHaveCount(0);
        expect(await lefts(page)).toEqual(before);
      }
      problems.splice(0, problems.length, ...problems.filter((p) => !/status of 404/.test(p)));
    });
  }
}

for (const [label, close] of [
  ["Escape", (page: Page) => page.keyboard.press("Escape")],
  ["Close", (page: Page) => page.getByRole("button", { name: "Close" }).click()],
  ["the scrim", (page: Page) => page.mouse.click(8, 880)],
] as const) {
  test(`the lock holds the page, and ${label} releases it with focus and position restored`, async ({ page }) => {
    await ready(page, "/");
    await page.evaluate((y) => scrollTo(0, y), START);
    const trigger = page.getByRole("button", { name: "Profile unavailable in this mock" });
    await trigger.click();
    await expect(page.getByRole("dialog")).toBeVisible();
    await expect(page.locator("body > div[inert]")).toHaveCount(1);
    expect(await lock(page)).toEqual({ value: "gutter", overflow: "hidden" });
    expect(await wheel(page)).toBe(START);
    await close(page);
    await expect(page.getByRole("dialog")).toHaveCount(0);
    await expect(page.locator("body > div[inert]")).toHaveCount(0);
    const after = await lock(page);
    expect(after.value).toBeNull();
    expect(after.overflow).not.toBe("hidden");
    await expect(trigger).toBeFocused();
    expect(await page.evaluate(() => scrollY)).toBe(START);
    expect(await wheel(page)).toBeGreaterThan(START);
  });
}

test("Back releases the lock and restores the earlier entry", async ({ page }) => {
  await ready(page, "/");
  await page.getByRole("navigation", { name: "Primary" }).getByRole("link", { name: "Notes" }).click();
  await expect(page.locator("h1")).toBeFocused();
  await page.getByRole("button", { name: "Search mock catalogue" }).click();
  await expect(page.getByRole("dialog")).toBeVisible();
  expect((await lock(page)).value).toBe("gutter");
  await page.goBack();
  await expect(page.getByRole("dialog")).toHaveCount(0);
  await expect(page.locator("h1")).toHaveText("A personal atlas of scent.");
  await expect(page.getByRole("navigation", { name: "Primary" }).getByRole("link", { name: "Notes" })).toBeFocused();
  const after = await lock(page);
  expect(after.value).toBeNull();
  expect(after.overflow).not.toBe("hidden");
  expect(await wheel(page)).toBeGreaterThan(0);
});
