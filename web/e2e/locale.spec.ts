/** Frontend V1.1 (DPT-PLAN-013): two languages, sticky header, language selector, heading focus. */
import type { Page } from "@playwright/test";
import { expect, noOverflow, ORIGIN, raw, ready, test } from "./helpers";

/** Rows of the header grid, counted from the tops of its visible parts relative to the brand. */
const headerRows = (page: Page) =>
  page.evaluate(() => {
    const brand = document.querySelector("[data-header-brand]")!.getBoundingClientRect();
    const parts = Array.from(document.querySelector("[data-header-grid]")!.children)
      .map((part) => part.getBoundingClientRect())
      .filter((box) => box.height > 0);
    return parts.some((box) => box.top >= brand.bottom - 1) ? 2 : 1;
  });

const PAIRS = [
  ["/", "/th", "Home · DoomParfum By TK", "หน้าแรก · DoomParfum By TK"],
  ["/explore", "/th/explore", "Explore mock fragrances · DoomParfum By TK", "สำรวจน้ำหอมจำลอง · DoomParfum By TK"],
  ["/perfume/paper-study-a", "/th/perfume/paper-study-a", "Paper study A · Mock study · DoomParfum By TK", "Paper study A · แบบศึกษาจำลอง · DoomParfum By TK"],
  ["/notes", "/th/notes", "Notes · DoomParfum By TK", "โน้ตกลิ่น · DoomParfum By TK"],
  ["/about", "/th/about", "About · DoomParfum By TK", "เกี่ยวกับเรา · DoomParfum By TK"],
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
    for (const name of ["เมนู", "ค้นหาในแคตตาล็อกจำลอง", "โปรไฟล์ยังไม่เปิดใช้ในฉบับจำลองนี้"]) {
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
    const input = page.getByRole("textbox", { name: "ค้นหาในแคตตาล็อกจำลอง" });
    await input.fill("หมึกยามดึก");
    await expect(page.locator("[data-entry]")).toHaveCount(1);
    await input.fill("late ink");
    await expect(page.locator("[data-entry]")).toHaveCount(1);
    await input.fill("ไม่มีคำนี้เลย");
    await expect(page.getByText("ไม่พบแบบศึกษาที่ตรงกับตัวกรอง")).toBeVisible();
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

  test("a fragment target is not hidden under it", async ({ page }) => {
    await page.goto("/about#credits");
    await page.waitForTimeout(300);
    const [bottom, top] = await page.evaluate(() => [
      document.querySelector("header")!.getBoundingClientRect().bottom,
      document.getElementById("credits")!.getBoundingClientRect().top,
    ]);
    expect(top).toBeGreaterThanOrEqual(bottom);
  });

  test("the skip link target starts below the header", async ({ page }) => {
    await ready(page, "/about");
    await page.evaluate(() => scrollTo(0, 1500));
    await page.keyboard.press("Tab");
    await page.keyboard.press("Enter");
    await expect(page.locator("main#main-content")).toBeFocused();
    const [bottom, top] = await page.evaluate(() => [
      document.querySelector("header")!.getBoundingClientRect().bottom,
      document.getElementById("main-content")!.getBoundingClientRect().top,
    ]);
    expect(top).toBeGreaterThanOrEqual(bottom - 1);
  });

  test("Thai language names are never tracked", async ({ page }) => {
    for (const path of ["/notes", "/th/notes"]) {
      await ready(page, path);
      const spacing = await page.locator("footer [lang='th']").evaluateAll((els) => els.map((el) => getComputedStyle(el).letterSpacing));
      expect(spacing.length).toBeGreaterThan(0);
      for (const s of spacing) expect(s).toBe("normal");
    }
  });

  test("a one-row header stays sticky at 320px", async ({ page }) => {
    await page.setViewportSize({ width: 320, height: 640 });
    await ready(page, "/about");
    expect(await headerRows(page)).toBe(1);
    expect(await page.locator("header").evaluate((el) => getComputedStyle(el).position)).toBe("sticky");
  });

  test("a two-row header is static even when it covers less than a fifth of the viewport (5.1)", async ({ page }) => {
    await page.setViewportSize({ width: 320, height: 1000 });
    await ready(page, "/about");
    await page.evaluate(() => document.documentElement.style.setProperty("font-size", "125%"));
    await expect.poll(() => headerRows(page)).toBe(2);
    const [position, height, offset] = await page.evaluate(() => {
      const header = document.querySelector("header")!;
      return [
        getComputedStyle(header).position,
        header.getBoundingClientRect().height,
        getComputedStyle(document.documentElement).getPropertyValue("--header-h").trim(),
      ] as const;
    });
    expect(height).toBeLessThanOrEqual(200);
    expect(position).toBe("static");
    expect(offset).toBe("0px");
  });

  for (const [width, position] of [[768, "static"], [1280, "sticky"]] as const) {
    test(`without scripting the header is ${position} at ${width}px and a fragment target clears it`, async ({ browser }) => {
      const context = await browser.newContext({ javaScriptEnabled: false, viewport: { width, height: 900 }, baseURL: ORIGIN });
      const page = await context.newPage();
      await page.goto("/about#credits");
      expect(await headerRows(page)).toBe(position === "static" ? 2 : 1);
      expect(await page.locator("header").evaluate((el) => getComputedStyle(el).position)).toBe(position);
      await page.evaluate(() => document.getElementById("credits")!.scrollIntoView());
      const [scrolled, bottom, top] = await page.evaluate(() => [
        scrollY,
        Math.max(0, document.querySelector("header")!.getBoundingClientRect().bottom),
        document.getElementById("credits")!.getBoundingClientRect().top,
      ]);
      expect(scrolled).toBeGreaterThan(0);
      expect(top).toBeGreaterThanOrEqual(bottom);
      await context.close();
    });
  }

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

test.describe("CP4 selections (Owner, 2026-11-26)", () => {
  test("T1: Thai headings render in Fahkwang 300, English headings in Bodoni Moda, body in Noto Sans Thai", async ({ page }) => {
    const fonts: string[] = [];
    page.on("response", (r) => { if (r.url().endsWith(".woff2")) fonts.push(r.url().split("/").pop()!); });
    await ready(page, "/th/notes");
    const h1 = await page.locator("main h1").evaluate((el) => {
      const s = getComputedStyle(el);
      return { family: s.fontFamily, weight: s.fontWeight, spacing: s.letterSpacing, settings: s.fontVariationSettings, ratio: parseFloat(s.lineHeight) / parseFloat(s.fontSize) };
    });
    expect(h1.family).toMatch(/^"?Bodoni Moda"?, "?Fahkwang/);
    expect(h1.weight).toBe("300");
    expect(h1.spacing).toBe("normal");
    expect(h1.settings).toBe("normal");
    expect(h1.ratio).toBeGreaterThanOrEqual(1.45);
    expect(await page.evaluate(() => document.fonts.check('300 50px "Fahkwang"', "โน้ตกลิ่น"))).toBe(true);
    expect(await page.locator("main p").first().evaluate((el) => getComputedStyle(el).fontFamily)).toMatch(/^"?Noto Sans Thai/);
    expect(fonts.some((f) => f.startsWith("fahkwang-thai-300"))).toBe(true);
    // A Latin name on a Thai page keeps Bodoni Moda 400.
    await ready(page, "/th/perfume/paper-study-c");
    const name = await page.locator("main h1").evaluate((el) => [el.getAttribute("lang"), getComputedStyle(el).fontFamily, getComputedStyle(el).fontWeight]);
    expect(name).toEqual(["en", expect.stringMatching(/^"?Bodoni Moda/), "400"]);
  });

  test("T1: an English page without Thai text loads no Thai display font", async ({ page }) => {
    const fonts: string[] = [];
    page.on("response", (r) => { if (r.url().endsWith(".woff2")) fonts.push(r.url().split("/").pop()!); });
    await ready(page, "/about");
    expect(fonts.filter((f) => f.startsWith("fahkwang"))).toEqual([]);
  });

  test("T2: the hero text is centred on the art at 1440", async ({ page }) => {
    await page.setViewportSize({ width: 1440, height: 1000 });
    await ready(page, "/");
    const [text, art] = await page.evaluate(() =>
      ["[data-hero-text]", ".hero-art"].map((s) => {
        const r = document.querySelector(s)!.getBoundingClientRect();
        return r.top + r.height / 2;
      }),
    );
    expect(Math.abs(text! - art!)).toBeLessThanOrEqual(24);
    await expect(page.getByText("Vol. I")).toHaveCount(0);
  });

  test("T3: the record sheet shows the record's own fields with distinct unknown and empty states", async ({ page }) => {
    await ready(page, "/perfume/paper-study-a");
    const sheet = page.locator("[data-record-sheet]");
    await expect(sheet.locator("dt")).toHaveText(["Family", "Top", "Heart", "Base", "General notes", "Accords"]);
    await expect(sheet.locator("dd")).toHaveText(["Bright study", "Ivrel", "Not supplied in this mock", "No entries", "Not supplied in this mock", "Not supplied in this mock"]);
    await expect(sheet.locator("dd[data-field='unknown']").first()).toHaveCSS("font-style", "italic");
    // The same record in the layer section below says the same things.
    await expect(page.locator("[data-layer='heart'] [data-field='unknown']")).toHaveCount(1);
    await expect(page.locator("[data-layer='base'] [data-field='empty']")).toHaveCount(1);
    await ready(page, "/th/perfume/stone-study-j");
    await expect(page.locator("[data-record-sheet] dt")).toHaveText(["ตระกูลกลิ่น", "ท็อปโน้ต", "ฮาร์ตโน้ต", "เบสโน้ต", "โน้ตทั่วไป", "แอคคอร์ด"]);
    await expect(page.locator("[data-record-sheet] dd").nth(3)).toHaveText("Ondrith, Marovane, Luthmere");
  });

  test("T4: the compact toolbar keeps visible labels, full borders and 44px controls on one row", async ({ page }) => {
    await page.setViewportSize({ width: 1280, height: 900 });
    await ready(page, "/explore");
    const fields = await page.locator("#explore-filters .toolbar-field").evaluateAll((els) =>
      els.map((el) => {
        const label = el.querySelector("label")!.getBoundingClientRect();
        const select = el.querySelector("select")!;
        const box = select.getBoundingClientRect();
        return { sameRow: Math.abs(label.top + label.height / 2 - (box.top + box.height / 2)) < 4, height: box.height, border: getComputedStyle(select).borderTopStyle, top: Math.round(box.top) };
      }),
    );
    expect(fields).toHaveLength(3);
    for (const f of fields) expect(f).toMatchObject({ sameRow: true, border: "solid" });
    for (const f of fields) expect(f.height).toBeGreaterThanOrEqual(44);
    expect(new Set(fields.map((f) => f.top)).size).toBe(1);
    await expect(page.getByText("Searches the names, house and descriptions of fictional studies.")).toBeVisible();
  });

  for (const [path, width] of [["/explore", 1440], ["/th/explore", 1440], ["/explore", 1280], ["/th/explore", 1280]] as const) {
    test(`T4: the first catalogue picture starts at or above 560px on ${path} at ${width}x900`, async ({ page }) => {
      await page.setViewportSize({ width, height: 900 });
      await ready(page, path);
      const top = await page.locator("[data-entry] a > :first-child").first().evaluate((el) => el.getBoundingClientRect().top);
      expect(top).toBeLessThanOrEqual(560);
    });
  }

  test("T8: buttons, fields, chips and dialogs are square; icons keep their shapes", async ({ page }) => {
    await ready(page, "/explore?family=mock-family-soft");
    const radii = await page.evaluate(() =>
      [".button-quiet", ".field-control", ".filter-chip", "[data-mock-marker]"].map((s) => {
        const el = document.querySelector(s);
        return el ? getComputedStyle(el).borderTopLeftRadius : "missing";
      }),
    );
    expect(radii.filter((r) => r !== "missing")).toEqual(radii.filter((r) => r !== "missing").map(() => "0px"));
    await page.getByRole("button", { name: "Profile unavailable in this mock" }).click();
    expect(await page.locator("[data-panel]").evaluate((el) => getComputedStyle(el).borderTopLeftRadius)).toBe("0px");
  });

  test("BY TK signature is 11px and stays visible while scrolling", async ({ page }) => {
    await ready(page, "/about");
    await page.evaluate(() => scrollTo(0, 1200));
    const sig = await page.locator("header .text-signature").evaluate((el) => [getComputedStyle(el).fontSize, getComputedStyle(el).opacity, el.getBoundingClientRect().height > 0]);
    expect(sig).toEqual(["11px", "1", true]);
  });
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

  test("pointer navigation to Notes: no ring after the window loses and regains focus (screenshot tool)", async ({ page }) => {
    await ready(page, "/");
    await page.getByRole("navigation", { name: "Primary" }).getByRole("link", { name: "Notes" }).click();
    await expect(page.locator("main h1")).toBeFocused();
    // What a screenshot tool causes: blur on the heading while it stays the active element.
    await page.locator("main h1").evaluate((el) => {
      el.dispatchEvent(new FocusEvent("blur"));
      window.dispatchEvent(new FocusEvent("blur"));
      window.dispatchEvent(new FocusEvent("focus"));
    });
    await page.keyboard.press("PrintScreen");
    await page.keyboard.press("Shift");
    // A non-modifier key makes Chromium re-evaluate :focus-visible, so the check cannot pass vacuously.
    await page.keyboard.press("a");
    expect(await ring(page)).toBe(false);
  });

  test("an alphabet jump link by pointer focuses its group without a ring", async ({ page }) => {
    await ready(page, "/notes");
    await page.locator(".letter-link").nth(1).click();
    const heading = page.locator("main h3[id^='notes-']").nth(1);
    await expect(heading).toBeFocused();
    await page.keyboard.press("Shift");
    expect(await heading.evaluate((el) => getComputedStyle(el).outlineStyle)).toBe("none");
  });

  test("the skip link still shows focus on main for keyboard users", async ({ page }) => {
    await ready(page, "/notes");
    await page.keyboard.press("Tab");
    await page.keyboard.press("Enter");
    await expect(page.locator("main#main-content")).toBeFocused();
    expect(await page.locator("main#main-content").evaluate((el) => getComputedStyle(el).outlineStyle)).toBe("solid");
  });

  test("keyboard navigation: the heading shows the ring", async ({ page }) => {
    await ready(page, "/");
    await page.getByRole("navigation", { name: "Primary" }).getByRole("link", { name: "About" }).focus();
    await page.keyboard.press("Enter");
    await expect(page.locator("main h1")).toBeFocused();
    expect(await ring(page)).toBe(true);
  });
});
