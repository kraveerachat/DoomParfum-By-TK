import { type Page } from "@playwright/test";
import { expect, ready, test } from "./helpers";

// IMP-WEB-02 S3: every navigation path named in the Owner's Notes outline report (CP4 item 11).
// A ring is drawn only when the user's own last input was the keyboard.

/** True when the focused element (not the body) draws an outline. */
const activeRing = (page: Page) =>
  page.evaluate(() => {
    const el = document.activeElement;
    return !!el && el !== document.body && getComputedStyle(el).outlineStyle !== "none";
  });
const headingRing = (page: Page) =>
  page.locator("main h1").evaluate((el) => document.activeElement === el && getComputedStyle(el).outlineStyle !== "none");

test.describe("S3 Notes heading focus on every navigation path", () => {
  test("pointer to Notes, then ordinary keys and screenshot shortcuts: no ring", async ({ page }) => {
    await ready(page, "/");
    await page.getByRole("navigation", { name: "Primary" }).getByRole("link", { name: "Notes" }).click();
    await expect(page.locator("main h1")).toBeFocused();
    for (const key of ["Shift", "a", "Control", "Meta", "PrintScreen", "Control+Shift+S", "Shift+Meta+S"]) {
      await page.keyboard.press(key);
      expect(await headingRing(page), key).toBe(false);
    }
  });

  // Headless and headed Chrome both keep the heading's pointer state here even on the CP4 build, so this
  // does not reproduce an OS screenshot shortcut; locale.spec V13 (synthetic blur) is the test that does.
  test("pointer to Notes, switching to another tab and back: no ring", async ({ page, context }) => {
    await ready(page, "/");
    await page.getByRole("navigation", { name: "Primary" }).getByRole("link", { name: "Notes" }).click();
    await expect(page.locator("main h1")).toBeFocused();
    const other = await context.newPage();
    await other.bringToFront();
    await page.bringToFront();
    await page.keyboard.press("PrintScreen");
    expect(await headingRing(page)).toBe(false);
    await other.close();
  });

  test("Thai: pointer to Notes draws no ring, keyboard to Notes does", async ({ page }) => {
    await ready(page, "/th");
    const nav = page.getByRole("navigation", { name: "เมนูหลัก" });
    await nav.getByRole("link", { name: "โน้ตกลิ่น" }).click();
    await expect(page).toHaveURL(/\/th\/notes$/);
    await expect(page.locator("main h1")).toBeFocused();
    await page.keyboard.press("Shift");
    expect(await headingRing(page)).toBe(false);

    await ready(page, "/th");
    await nav.getByRole("link", { name: "โน้ตกลิ่น" }).focus();
    await page.keyboard.press("Enter");
    await expect(page.locator("main h1")).toBeFocused();
    expect(await headingRing(page)).toBe(true);
  });

  test("keyboard to Notes: the heading shows the ring", async ({ page }) => {
    await ready(page, "/");
    await page.getByRole("navigation", { name: "Primary" }).getByRole("link", { name: "Notes" }).focus();
    await page.keyboard.press("Enter");
    await expect(page.locator("main h1")).toBeFocused();
    expect(await headingRing(page)).toBe(true);
  });

  test("pointer navigation, then Back and Forward: no ring appears", async ({ page }) => {
    await ready(page, "/");
    await page.getByRole("navigation", { name: "Primary" }).getByRole("link", { name: "Notes" }).click();
    await expect(page.locator("main h1")).toBeFocused();
    await page.goBack();
    await expect(page).toHaveURL(/\/$/);
    await page.waitForTimeout(300);
    expect(await activeRing(page)).toBe(false);
    await page.goForward();
    await expect(page).toHaveURL(/\/notes$/);
    await page.waitForTimeout(300);
    expect(await activeRing(page)).toBe(false);
    await page.keyboard.press("Shift");
    expect(await headingRing(page)).toBe(false);
  });

  for (const how of ["pointer", "keyboard"] as const) {
    test(`language switch on Notes by ${how}: the new page draws no heading ring`, async ({ page }) => {
      await ready(page, "/notes");
      const link = page.locator("header [data-document-nav]:visible").first();
      if (how === "pointer") await link.click();
      else {
        await link.focus();
        await page.keyboard.press("Enter");
      }
      await expect(page).toHaveURL(/\/th\/notes$/);
      await page.waitForLoadState("load");
      expect(await headingRing(page)).toBe(false);
      expect(await activeRing(page)).toBe(false);
    });
  }

  test("alphabet jump link by keyboard focuses its group with a ring", async ({ page }) => {
    await ready(page, "/notes");
    await page.locator(".letter-link").nth(1).focus();
    await page.keyboard.press("Enter");
    const heading = page.locator("main h3[id^='notes-']").nth(1);
    await expect(heading).toBeFocused();
    expect(await heading.evaluate((el) => getComputedStyle(el).outlineStyle)).toBe("solid");
  });

  test("a note link from a perfume entry by pointer lands without a ring", async ({ page }) => {
    await ready(page, "/perfume/paper-study-a");
    await page.locator("main a[href^='/notes']").first().click();
    await expect(page).toHaveURL(/\/notes/);
    await page.waitForTimeout(300);
    await page.keyboard.press("Shift");
    expect(await activeRing(page)).toBe(false);
  });

  test("mobile drawer to Notes by pointer: no ring on the heading", async ({ page }) => {
    await page.setViewportSize({ width: 390, height: 844 });
    await ready(page, "/");
    await page.locator("header button[aria-haspopup='dialog']").filter({ hasNotText: /search|profile/i }).first().click();
    const dialog = page.getByRole("dialog");
    await dialog.getByRole("link", { name: "Notes" }).click();
    await expect(page.locator("main h1")).toBeFocused();
    await page.keyboard.press("Shift");
    expect(await headingRing(page)).toBe(false);
  });

  test("Search dialog closed by pointer returns focus without a ring; by Escape with one", async ({ page }) => {
    await ready(page, "/notes");
    const trigger = page.getByRole("button", { name: "Search mock catalogue" });
    await trigger.click();
    await page.getByRole("dialog").getByRole("button", { name: /close/i }).click();
    await expect(trigger).toBeFocused();
    expect(await activeRing(page)).toBe(false);

    await trigger.focus();
    await page.keyboard.press("Enter");
    await expect(page.getByRole("dialog")).toBeVisible();
    await page.keyboard.press("Escape");
    await expect(trigger).toBeFocused();
    expect(await activeRing(page)).toBe(true);
  });
});
