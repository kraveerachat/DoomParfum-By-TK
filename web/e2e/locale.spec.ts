/** Frontend V1.1 (DPT-PLAN-013): two languages, sticky header, language selector, heading focus. */
import type { Page } from "@playwright/test";
import { expect, noOverflow, ORIGIN, raw, ready, test } from "./helpers";

const PAIRS = [
  ["/", "/th", "Home · DoomParfum By TK", "หน้าแรก · DoomParfum By TK"],
  ["/explore", "/th/explore", "Explore mock fragrances · DoomParfum By TK", "สำรวจน้ำหอมจำลอง · DoomParfum By TK"],
  ["/perfume/paper-study-a", "/th/perfume/paper-study-a", "Paper study A · Mock study · DoomParfum By TK", "Paper study A · แบบศึกษาจำลอง · DoomParfum By TK"],
  ["/notes", "/th/notes", "Notes · DoomParfum By TK", "โน้ตกลิ่น · DoomParfum By TK"],
  ["/about", "/th/about", "About · DoomParfum By TK", "เกี่ยวกับ · DoomParfum By TK"],
] as const;

test.describe("V01 ten routes and their 404s", () => {
  for (const [enPath, thPath, enTitle, thTitle] of PAIRS) {
    for (const [path, lang, title, notice] of [
      [enPath, "en", enTitle, "Synthetic mock study."],
      [thPath, "th", thTitle, "แบบศึกษาจำลอง"],
    ] as const) {
      test(`${path} is ${lang} from the server, with title, one h1 and the mock notice`, async ({ page }) => {
        const response = await raw("GET", path);
        expect(response.status).toBe(200);
        expect(response.body).toContain(`<html lang="${lang}"`);
        expect(response.headers["content-security-policy"]).toContain("nonce-");
        expect(response.headers["cache-control"]).toContain("no-store");
        await ready(page, path);
        await expect(page).toHaveTitle(title);
        await expect(page.locator("h1")).toHaveCount(1);
        await expect(page.locator("[data-synthetic-notice]")).toContainText(notice);
      });
    }
  }

  for (const [path, heading] of [
    ["/en", "This page is unavailable"],
    ["/en/explore", "This page is unavailable"],
    ["/TH", "This page is unavailable"],
    ["/fr", "This page is unavailable"],
    ["/th/nope", "ไม่พบหน้านี้"],
    ["/th/perfume/nope", "ไม่พบหน้านี้"],
  ] as const) {
    test(`${path} is a real 404 in its language`, async ({ page, problems }) => {
      const response = await raw("GET", path);
      expect(response.status).toBe(404);
      expect(response.headers["x-robots-tag"]).toContain("noindex");
      expect(response.headers["content-security-policy"]).toContain("nonce-");
      await page.goto(path);
      await expect(page.locator("[data-state='unavailable'] h1")).toHaveText(heading);
      problems.splice(0, problems.length, ...problems.filter((p) => !/status of 404/.test(p)));
    });
  }
});

/** Every visible text node and accessible name on a Thai page is Thai, marked English, or a name or numeral. */
const strayLatin = (page: Page) =>
  page.evaluate(() => {
    const ok = /^(?:[\s\d.,·:;!?/()–—+−×→←'"“”‘’|-]*|[IVX]+)$/;
    const allowed = new Set(["DOOMPARFUM", "BY TK", "TH", "EN", "English", "A–Z", "Z–A"]);
    const bad: string[] = [];
    const walker = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT);
    for (let node = walker.nextNode(); node; node = walker.nextNode()) {
      const text = node.textContent?.trim() ?? "";
      const el = node.parentElement;
      if (!text || !el || /[฀-๿]/.test(text) || ok.test(text) || allowed.has(text)) continue;
      if (el.closest("[lang]:not(html)")?.getAttribute("lang") === "en") continue;
      if (el.closest("script, style, noscript, template")) continue;
      bad.push(text.slice(0, 60));
    }
    for (const el of document.querySelectorAll("[aria-label]")) {
      const name = el.getAttribute("aria-label") ?? "";
      if (!/[฀-๿]/.test(name)) bad.push(`aria-label: ${name}`);
    }
    return bad;
  });

test.describe("V02 translation coverage", () => {
  for (const path of ["/th", "/th/explore", "/th/perfume/paper-study-c", "/th/perfume/glass-study-i", "/th/notes", "/th/about", "/th/nope"]) {
    test(`${path} has no unmarked English`, async ({ page, problems }) => {
      await ready(page, path);
      expect(await strayLatin(page)).toEqual([]);
      problems.splice(0, problems.length, ...problems.filter((p) => !/status of 404/.test(p)));
    });
  }

  test("dialogs and the drawer are Thai on Thai pages", async ({ page }) => {
    await page.setViewportSize({ width: 390, height: 844 });
    await ready(page, "/th/explore");
    for (const name of ["เมนู", "ค้นหาแคตตาล็อกจำลอง", "โปรไฟล์ยังไม่เปิดใช้ในการจำลองนี้"]) {
      await page.getByRole("button", { name, exact: true }).click();
      await expect(page.getByRole("dialog")).toBeVisible();
      expect(await strayLatin(page)).toEqual([]);
      await page.keyboard.press("Escape");
      await expect(page.getByRole("dialog")).toHaveCount(0);
    }
  });
});

const langHref = (page: Page, lang: "th" | "en") => page.locator(`header a[hreflang="${lang}"]:visible`).first().getAttribute("href");

test.describe("V05 language switch", () => {
  test("keeps the page, slug, recognized filters and the fragment, both ways", async ({ page }) => {
    await ready(page, "/explore?family=mock-family-soft&note=mock-note-002");
    expect(await langHref(page, "th")).toBe("/th/explore?family=mock-family-soft&note=mock-note-002");
    await ready(page, "/explore?family=floral&note=mock-note-002");
    expect(await langHref(page, "th")).toBe("/th/explore?note=mock-note-002");
    await ready(page, "/perfume/paper-study-c");
    expect(await langHref(page, "th")).toBe("/th/perfume/paper-study-c");
    await ready(page, "/about#credits");
    expect(await langHref(page, "th")).toBe("/th/about#credits");
    await ready(page, "/th/notes");
    expect(await langHref(page, "en")).toBe("/notes");
    await ready(page, "/th");
    expect(await langHref(page, "en")).toBe("/");
  });

  test("is a document navigation that works and writes no cookie or storage", async ({ page, context }) => {
    await ready(page, "/perfume/paper-study-c");
    await page.locator('header a[hreflang="th"]:visible').first().click();
    await expect(page).toHaveURL(`${ORIGIN}/th/perfume/paper-study-c`);
    await expect(page.locator("html")).toHaveAttribute("lang", "th");
    expect(await context.cookies()).toEqual([]);
    expect(await page.evaluate(() => localStorage.length + sessionStorage.length)).toBe(0);
  });

  test("works without scripting", async ({ browser }) => {
    const context = await browser.newContext({ javaScriptEnabled: false });
    const page = await context.newPage();
    await page.goto(`${ORIGIN}/notes`);
    await page.locator('footer a[hreflang="th"]').click();
    await expect(page).toHaveURL(`${ORIGIN}/th/notes`);
    await expect(page.locator("h1")).toHaveText("โน้ตกลิ่น");
    await context.close();
  });

  for (const path of ["/th", "/th/explore", "/th/perfume/paper-study-b", "/th/notes", "/th/about"]) {
    test(`${path}: every internal link stays in Thai except the English language link`, async ({ page }) => {
      await page.goto(path);
      const hrefs = await page.locator("a[href^='/']").evaluateAll((els) => els.map((e) => [e.getAttribute("href"), e.getAttribute("hreflang")]));
      const leaving = hrefs.filter(([href, lang]) => !(href === "/th" || href!.startsWith("/th/") || href!.startsWith("/th?") || href!.startsWith("/th#")) && lang !== "en");
      expect(leaving).toEqual([]);
    });
  }
});

test.describe("V06 search in Thai", () => {
  test("Thai pages find studies by Thai text and by the English source", async ({ page }) => {
    await ready(page, "/th/explore");
    const input = page.getByRole("textbox", { name: "ค้นหาแคตตาล็อกจำลอง" });
    await input.fill("หมึกยามดึก");
    await expect(page.locator("[data-entry]")).toHaveCount(1);
    await input.fill("late ink");
    await expect(page.locator("[data-entry]")).toHaveCount(1);
    await input.fill("ไม่มีคำนี้เลย");
    await expect(page.getByText("ไม่มีแบบศึกษาจำลองที่ตรงกับตัวกรองนี้")).toBeVisible();
  });

  test("English pages are not widened by draft Thai text", async ({ page }) => {
    await ready(page, "/explore");
    await page.getByRole("textbox", { name: "Search mock catalogue" }).fill("หมึก");
    await expect(page.locator("[data-entry]")).toHaveCount(0);
  });
});

test.describe("V07 sticky header", () => {
  for (const width of [1440, 390]) {
    test(`stays at the top while scrolling at ${width}, opaque, below dialogs`, async ({ page }) => {
      await page.setViewportSize({ width, height: 900 });
      await ready(page, "/about");
      await page.evaluate(() => scrollTo(0, 1500));
      const header = await page.locator("header").evaluate((el) => {
        const s = getComputedStyle(el);
        return { top: el.getBoundingClientRect().top, position: s.position, bg: s.backgroundColor, z: s.zIndex };
      });
      expect(header).toEqual({ top: 0, position: "sticky", bg: "rgb(247, 245, 240)", z: "20" });
    });
  }

  test("a fragment target and the skip link target are not hidden under it", async ({ page }) => {
    await page.goto("/about#credits");
    await page.waitForTimeout(300);
    const [bottom, top] = await page.evaluate(() => [
      document.querySelector("header")!.getBoundingClientRect().bottom,
      document.getElementById("credits")!.getBoundingClientRect().top,
    ]);
    expect(top).toBeGreaterThanOrEqual(bottom);
  });

  test("focusing a header control never scrolls the page", async ({ page }) => {
    await ready(page, "/about");
    await page.evaluate(() => scrollTo(0, 800));
    await page.getByRole("button", { name: "Search mock catalogue" }).focus();
    expect(await page.evaluate(() => scrollY)).toBe(800);
  });

  test("is static on a short viewport", async ({ page }) => {
    await page.setViewportSize({ width: 812, height: 375 });
    await ready(page, "/about");
    expect(await page.locator("header").evaluate((el) => getComputedStyle(el).position)).toBe("static");
  });
});

test.describe("V08 navigation centre with the language selector", () => {
  for (const path of ["/", "/th"]) {
    for (const width of [1024, 1280, 1440, 1920]) {
      test(`${path} at ${width}`, async ({ page }) => {
        await page.setViewportSize({ width, height: 900 });
        await ready(page, path);
        const offset = await page.evaluate(() => {
          const grid = document.querySelector("[data-header-grid]")!.getBoundingClientRect();
          const nav = document.querySelector("[data-header-nav]")!.getBoundingClientRect();
          return Math.abs(nav.left + nav.width / 2 - (grid.left + grid.width / 2));
        });
        expect(offset).toBeLessThanOrEqual(1);
      });
    }
  }
});

test.describe("V09 language control at every width", () => {
  for (const [label, width, css] of [
    ["320", 320, ""],
    ["390", 390, ""],
    ["768", 768, ""],
    ["200% text at 375", 375, "html{font-size:200%}"],
  ] as const) {
    test(label, async ({ page }) => {
      await page.setViewportSize({ width, height: 800 });
      await ready(page, "/explore");
      if (css) {
        // Adopted sheets, as in A08: the nonce policy refuses an inline style element.
        await page.evaluate((text) => {
          const sheet = new CSSStyleSheet();
          sheet.replaceSync(text);
          document.adoptedStyleSheets = [sheet];
        }, css);
        await page.waitForTimeout(100);
      }
      const link = page.locator('header a[hreflang="th"]:visible');
      await expect(link).toHaveCount(1);
      const box = (await link.boundingBox())!;
      expect(box.width).toBeGreaterThanOrEqual(44);
      expect(box.height).toBeGreaterThanOrEqual(44);
      await expect(link).toHaveAccessibleName(/^TH\s*ภาษาไทย$/);
      expect((await noOverflow(page)).scroll).toBe(0);
    });
  }
});

test.describe("V13 heading focus follows how the navigation started", () => {
  const ring = (page: Page) => page.locator("main h1").evaluate((el) => document.activeElement === el && getComputedStyle(el).outlineStyle !== "none");

  test("pointer navigation: no ring on the heading, even after a later key press", async ({ page }) => {
    await ready(page, "/");
    await page.getByRole("navigation", { name: "Primary" }).getByRole("link", { name: "About" }).click();
    await expect(page.locator("main h1")).toBeFocused();
    expect(await ring(page)).toBe(false);
    await page.keyboard.press("Shift");
    expect(await ring(page)).toBe(false);
    await page.keyboard.press("Tab");
    expect(await page.evaluate(() => getComputedStyle(document.activeElement!).outlineStyle)).toBe("solid");
  });

  test("keyboard navigation: the heading shows the ring", async ({ page }) => {
    await ready(page, "/");
    await page.getByRole("navigation", { name: "Primary" }).getByRole("link", { name: "About" }).focus();
    await page.keyboard.press("Enter");
    await expect(page.locator("main h1")).toBeFocused();
    expect(await ring(page)).toBe(true);
  });
});
