import AxeBuilder from "@axe-core/playwright";
import type { Page } from "@playwright/test";
import { expect, focused, noOverflow, ready, ROUTES, test } from "./helpers";

const ALL = [...ROUTES.map((r) => r.path), "/perfume/stone-study-k", "/perfume/paper-study-l", "/explore?note=mock-note-009", "/explore?family=x"];
const axe = (page: Page) => new AxeBuilder({ page }).withTags(["wcag2a", "wcag2aa", "wcag21a", "wcag21aa"]).analyze();

test.describe("A05 keyboard and focus", () => {
  test("skip link is first, visible when focused, and moves into main", async ({ page }) => {
    await ready(page, "/");
    await page.keyboard.press("Tab");
    const skip = page.getByRole("link", { name: "Skip to content" });
    await expect(skip).toBeFocused();
    await expect(skip).toBeInViewport();
    await page.keyboard.press("Enter");
    await expect(page.locator("#main-content")).toBeFocused();
  });

  for (const [trigger, title] of [["Search mock catalogue", "Search"], ["Profile unavailable in this mock", "Profile"]] as const) {
    test(`${title}: opens by keyboard, traps focus, closes with Escape, restores focus`, async ({ page }) => {
      await ready(page, "/explore");
      const button = page.getByRole("button", { name: trigger });
      await button.focus();
      await page.keyboard.press("Enter");
      const dialog = page.getByRole("dialog", { name: title });
      await expect(dialog).toBeVisible();
      await expect(page.locator("body > div[inert]")).toHaveCount(1);
      for (let i = 0; i < 30; i += 1) {
        await page.keyboard.press(i % 7 === 6 ? "Shift+Tab" : "Tab");
        expect(await page.evaluate(() => !!document.activeElement?.closest("[role='dialog']"))).toBe(true);
      }
      await page.keyboard.press("Escape");
      await expect(page.getByRole("dialog")).toHaveCount(0);
      await expect(button).toBeFocused();
      await page.keyboard.press("Space");
      await expect(dialog).toBeVisible();
      await dialog.getByRole("button", { name: "Close" }).click();
      await expect(button).toBeFocused();
    });
  }

  test("Profile explains itself and contains no form", async ({ page }) => {
    await ready(page, "/");
    await page.getByRole("button", { name: "Profile unavailable in this mock" }).click();
    const dialog = page.getByRole("dialog");
    await expect(dialog).toContainText("Profile is not available in this mock. No sign-in or account data is used.");
    await expect(dialog.locator("form, input")).toHaveCount(0);
    await expect(dialog.getByRole("button")).toHaveCount(1);
  });

  test("Menu drawer: Close focused first, scrim closes, links navigate to the h1", async ({ page }) => {
    await page.setViewportSize({ width: 375, height: 700 });
    await ready(page, "/about");
    const menu = page.getByRole("button", { name: "Menu" });
    await menu.click();
    const dialog = page.getByRole("dialog", { name: "Navigation" });
    await expect(dialog.getByRole("button", { name: "Close" })).toBeFocused();
    await expect(dialog.getByRole("link")).toHaveText(["Home", "Explore", "Notes", "About"]);
    await expect(dialog.getByRole("link", { name: "About" })).toHaveAttribute("aria-current", "page");
    await page.waitForTimeout(320);
    await page.mouse.click(370, 400);
    await expect(dialog).toHaveCount(0);
    await expect(menu).toBeFocused();
    await menu.click();
    await dialog.getByRole("link", { name: "About" }).click();
    await expect(dialog).toHaveCount(0);
    await expect(menu).toBeFocused();
    await menu.click();
    await dialog.getByRole("link", { name: "Notes" }).click();
    await expect(page).toHaveURL(/\/notes$/);
    await expect(dialog).toHaveCount(0);
    await expect(page.locator("h1")).toBeFocused();
    await page.goBack();
    await expect(menu).toBeFocused();
    await page.goForward();
    await expect(page).toHaveURL(/\/notes$/);
  });

  test("Back closes an open overlay", async ({ page }) => {
    await ready(page, "/");
    await page.getByRole("navigation", { name: "Primary" }).getByRole("link", { name: "Notes" }).click();
    await expect(page.locator("h1")).toBeFocused();
    await page.getByRole("button", { name: "Search mock catalogue" }).click();
    await expect(page.getByRole("dialog")).toBeVisible();
    await page.goBack();
    await expect(page.getByRole("dialog")).toHaveCount(0);
    await expect(page.locator("html")).not.toHaveAttribute("data-overlay", "");
  });

  test("fragment links focus their section", async ({ page }) => {
    await ready(page, "/");
    await page.locator("[data-focus-key='article-mock-article-002']").click();
    await expect(page).toHaveURL(/#journal-empty-is-not-unknown$/);
    expect(await focused(page)).toBe("journal-empty-is-not-unknown");
    await expect(page.locator("#journal-empty-is-not-unknown")).toBeInViewport();
  });

  test("every focusable control shows a visible focus indicator", async ({ page }) => {
    await ready(page, "/");
    const total = await page.locator("a[href]:visible, button:visible, summary:visible").count();
    for (let i = 0; i < total; i += 1) {
      await page.keyboard.press("Tab");
      const style = await page.evaluate(() => {
        const s = getComputedStyle(document.activeElement!);
        return { style: s.outlineStyle, width: parseFloat(s.outlineWidth), tag: document.activeElement!.outerHTML.slice(0, 80) };
      });
      expect(style.style, style.tag).toBe("solid");
      expect(style.width, style.tag).toBeGreaterThanOrEqual(2);
    }
  });

  test("rapid toggling leaves one correct final state", async ({ page }) => {
    await ready(page, "/");
    for (let i = 0; i < 6; i += 1) {
      await page.getByRole("button", { name: "Search mock catalogue" }).click();
      await page.keyboard.press("Escape");
    }
    await page.getByRole("button", { name: "Profile unavailable in this mock" }).click();
    await expect(page.getByRole("dialog")).toHaveCount(1);
    await page.keyboard.press("Escape");
    await expect(page.getByRole("dialog")).toHaveCount(0);
    await expect(page.getByRole("button", { name: "Profile unavailable in this mock" })).toBeFocused();
    await expect(page.locator("[data-panel-copy]")).toHaveCount(0);
    await page.mouse.wheel(0, 500);
    await expect.poll(() => page.evaluate(() => scrollY)).toBeGreaterThan(100);
  });
});

test.describe("A07 automatable accessibility and contrast", () => {
  for (const path of ALL) {
    test(`axe ${path}`, async ({ page }) => {
      await ready(page, path);
      expect((await axe(page)).violations.map((v) => `${v.id}: ${v.nodes.map((n) => n.target).join(" ")}`)).toEqual([]);
    });
  }
  for (const name of ["Search mock catalogue", "Profile unavailable in this mock"]) {
    test(`axe dialog ${name}`, async ({ page }) => {
      await page.emulateMedia({ reducedMotion: "reduce" });
      await ready(page, "/");
      await page.getByRole("button", { name }).click();
      await page.waitForTimeout(300);
      expect((await axe(page)).violations.map((v) => `${v.id}: ${v.nodes.map((n) => n.target).join(" ")}`)).toEqual([]);
    });
  }
  test("content survives blocked fonts", async ({ page, problems }) => {
    await page.route("**/*.woff2", (r) => r.abort());
    for (const { path } of ROUTES) {
      await ready(page, path);
      await expect(page.locator("h1")).toBeVisible();
      expect(await noOverflow(page)).toEqual({ scroll: 0, bad: [] });
    }
    expect(problems.filter((p) => !/Failed to load resource: net::ERR_FAILED/.test(p))).toEqual([]);
    problems.length = 0;
  });
});

const SPACING = "*{line-height:1.5!important;letter-spacing:.12em!important;word-spacing:.16em!important}p{margin-bottom:2em!important}";
// Injected through CSSOM so that the page's own policy stays untouched.
const restyle = (page: Page, css: string) =>
  page.evaluate((text) => {
    const sheet = new CSSStyleSheet();
    sheet.replaceSync(text);
    document.adoptedStyleSheets = [sheet];
  }, css);

test.describe("A08 reflow", () => {
  for (const [width, height] of [[320, 640], [375, 812], [640, 900], [768, 1024], [1024, 768], [1280, 900], [1440, 900], [812, 375]] as const) {
    test(`${width}x${height} and 44px targets`, async ({ page }) => {
      await page.setViewportSize({ width, height });
      for (const path of ALL) {
        await ready(page, path);
        expect(await noOverflow(page), path).toEqual({ scroll: 0, bad: [] });
        const small = await page.locator("button:visible, select:visible, summary:visible, input:visible, a[href]:visible").evaluateAll((els) =>
          els
            .filter((el) => !el.matches("a[href='#main-content'], [aria-label='Breadcrumb'] li:last-child a"))
            .map((el) => ({ t: el.outerHTML.slice(0, 90), w: el.getBoundingClientRect().width, h: el.getBoundingClientRect().height }))
            .filter((b) => b.h < 43.5 || b.w < 43.5),
        );
        expect(small, path).toEqual([]);
      }
    });
  }

  for (const [label, width, css] of [
    ["200% text at 1280", 1280, "html{font-size:200%}"],
    ["200% text at 375", 375, "html{font-size:200%}"],
    ["200% text at 320", 320, "html{font-size:200%}"],
    ["400% zoom of 1280 (320 CSS px)", 320, "html{font-size:100%}"],
    ["text spacing at 320", 320, SPACING],
    ["text spacing at 1280", 1280, SPACING],
  ] as const) {
    test(label, async ({ page }) => {
      await page.setViewportSize({ width, height: 800 });
      for (const path of ALL) {
        await ready(page, path);
        await restyle(page, css);
        await page.waitForTimeout(50);
        expect(await noOverflow(page), path).toEqual({ scroll: 0, bad: [] });
        for (const name of ["Search mock catalogue", "Profile unavailable in this mock"]) {
          await expect(page.getByRole("button", { name })).toBeInViewport();
        }
      }
    });
  }

  test("drawer and search stay operable in a short landscape viewport", async ({ page }) => {
    await page.setViewportSize({ width: 812, height: 375 });
    await ready(page, "/");
    await page.getByRole("button", { name: "Menu" }).click();
    const dialog = page.getByRole("dialog");
    await expect(dialog.getByRole("button", { name: "Close" })).toBeInViewport();
    await dialog.getByRole("link", { name: "About" }).scrollIntoViewIfNeeded();
    await expect(dialog.getByRole("link", { name: "About" })).toBeInViewport();
    await page.keyboard.press("Escape");
    await page.getByRole("button", { name: "Search mock catalogue" }).click();
    await page.waitForTimeout(300);
    await expect(dialog.getByRole("button", { name: "Close" })).toBeInViewport();
    await expect(dialog.getByRole("textbox")).toBeInViewport();
  });

  test("Thai headings use Thai metrics", async ({ page }) => {
    await ready(page, "/perfume/paper-study-l");
    const h1 = await page.locator("h1").evaluate((el) => {
      const s = getComputedStyle(el);
      return { lang: el.getAttribute("lang"), spacing: s.letterSpacing, ratio: parseFloat(s.lineHeight) / parseFloat(s.fontSize), face: s.fontFamily };
    });
    expect(h1.lang).toBe("th");
    expect(h1.spacing).toBe("normal");
    expect(h1.ratio).toBeGreaterThanOrEqual(1.35);
    expect(h1.face).toMatch(/^"?Noto Sans Thai/);
  });
});

test.describe("A09 header geometry", () => {
  for (const width of [1024, 1280, 1440]) {
    test(`navigation is centred at ${width}`, async ({ page }) => {
      await page.setViewportSize({ width, height: 900 });
      await ready(page, "/");
      const measure = () =>
        page.evaluate(() => {
          const box = (s: string) => document.querySelector(s)!.getBoundingClientRect();
          const grid = box("[data-header-grid]");
          const nav = box("[data-header-nav]");
          const brand = box("[data-header-brand]");
          const utils = box("[data-header-utils]");
          const tracks = getComputedStyle(document.querySelector("[data-header-grid]")!).gridTemplateColumns.split(" ").map(parseFloat);
          return {
            offset: Math.abs(nav.left + nav.width / 2 - (grid.left + grid.width / 2)),
            tracks: Math.abs(tracks[0]! - tracks[2]!),
            clear: nav.left - brand.right >= 0 && utils.left - nav.right >= 0,
            height: document.querySelector("header")!.getBoundingClientRect().height,
          };
        });
      const check = async () => {
        const m = await measure();
        expect(m.offset).toBeLessThanOrEqual(1);
        expect(m.tracks).toBeLessThanOrEqual(1);
        expect(m.clear).toBe(true);
        expect(m.height).toBeGreaterThanOrEqual(88);
      };
      await check();
      for (const [left, right] of [[150, 96], [240, 96], [150, 144], [240, 144]]) {
        await restyle(page, `[data-header-brand]{width:${left}px}[data-header-utils]{width:${right}px}`);
        await check();
      }
      await restyle(page, "html{font-size:200%}");
      await expect(page.locator("[data-header-nav]")).toBeHidden();
      await expect(page.getByRole("button", { name: "Menu" })).toBeVisible();
    });
  }
  test("the narrow header replaces the primary row below 1024", async ({ page }) => {
    await page.setViewportSize({ width: 1023, height: 800 });
    await ready(page, "/");
    await expect(page.locator("[data-header-nav]")).toBeHidden();
    await expect(page.getByRole("button", { name: "Menu" })).toBeVisible();
  });
});
