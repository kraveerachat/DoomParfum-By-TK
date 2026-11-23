import { expect, ready, ROUTES, test } from "./helpers";

test.describe("A01 routes and navigation", () => {
  for (const { path, title } of ROUTES) {
    test(`${path} has one h1, its title and noindex`, async ({ page }) => {
      const response = await page.goto(path);
      expect(response?.status()).toBe(200);
      await expect(page).toHaveTitle(title);
      await expect(page.locator("h1")).toHaveCount(1);
      await expect(page.locator("main#main-content")).toHaveCount(1);
      await expect(page.locator("meta[name='robots']")).toHaveAttribute("content", /noindex/);
      await expect(page.locator("footer")).toBeVisible();
    });
  }

  for (const path of ["/perfume/nope", "/perfume/Paper-Study-A", "/perfume/paper-study-a/x", "/login", "/journal"]) {
    test(`${path} is a real 404 with the unavailable view`, async ({ request, page, problems }) => {
      const response = await request.get(path);
      expect(response.status()).toBe(404);
      expect(response.headers()["x-robots-tag"]).toContain("noindex");
      await page.goto(path);
      await expect(page.locator("[data-state='unavailable'] h1")).toBeVisible();
      await expect(page.getByRole("link", { name: "Return to the mock catalogue" })).toBeVisible();
      await expect(page.locator("header")).toBeVisible();
      // The browser itself logs the 404 document; nothing else may be logged.
      expect(problems.filter((p) => !/status of 404/.test(p))).toEqual([]);
      problems.length = 0;
    });
  }

  test("invalid URL filters are explained, never reinterpreted", async ({ page }) => {
    for (const q of ["family=floral", "note=mock-note-999", "family=mock-family-soft&family=mock-family-deep", "note="]) {
      await ready(page, `/explore?${q}`);
      await expect(page.getByText("This filter is unavailable")).toBeVisible();
      await expect(page.locator("[data-entry]")).toHaveCount(0);
    }
    await page.getByRole("button", { name: "Reset filters" }).click();
    await expect(page).toHaveURL(/\/explore$/);
    await expect(page.locator("[data-entry]")).toHaveCount(12);
  });

  test("unsupported query keys are removed", async ({ page }) => {
    await ready(page, "/explore?q=secret&family=mock-family-soft&utm=1");
    await expect(page).toHaveURL(/\/explore\?family=mock-family-soft$/);
    await ready(page, "/about?x=1");
    await expect(page).toHaveURL(/\/about$/);
  });

  test("every internal link resolves and no dead fragment exists", async ({ page, request }) => {
    const seen = new Set<string>();
    for (const path of [...ROUTES.map((r) => r.path), "/perfume/linen-study-e"]) {
      await page.goto(path);
      for (const href of await page.locator("a[href]").evaluateAll((els) => els.map((e) => (e as HTMLAnchorElement).href))) {
        seen.add(href);
      }
    }
    const pages = new Map<string, string>();
    for (const href of seen) {
      const url = new URL(href);
      expect(url.origin).toBe("http://localhost:3000");
      const key = url.pathname + url.search;
      if (!pages.has(key)) {
        const response = await request.get(key);
        expect(response.status(), key).toBe(200);
        pages.set(key, await response.text());
      }
      if (url.hash) expect(pages.get(key)).toContain(`id="${url.hash.slice(1)}"`);
    }
  });

  test("one activation reaches Explore, one more a fixture, one more a note's studies", async ({ page }) => {
    await ready(page, "/");
    await page.getByRole("link", { name: "Explore mock catalogue" }).click();
    await expect(page).toHaveURL(/\/explore$/);
    await page.getByRole("link", { name: "Linen study E" }).click();
    await expect(page).toHaveURL(/\/perfume\/linen-study-e$/);
    await page.locator("[data-layer='heart'] a").first().click();
    await expect(page).toHaveURL(/\/explore\?note=mock-note-006$/);
    await expect(page.locator("[data-entry]")).toHaveCount(6);
  });
});

test.describe("A02 fixture truth", () => {
  test("every entry and every detail is visibly mock", async ({ page }) => {
    await ready(page, "/explore");
    const entries = page.locator("[data-entry]");
    await expect(entries).toHaveCount(12);
    for (const entry of await entries.all()) await expect(entry.getByText("Mock", { exact: true })).toBeVisible();
    const slugs = await entries.evaluateAll((els) => els.map((e) => (e as HTMLElement).dataset.entry));
    for (const slug of slugs) {
      await page.goto(`/perfume/${slug}`);
      await expect(page.locator("[data-mock-marker]")).toBeVisible();
      await expect(page.locator("[data-synthetic-notice]")).toBeVisible();
    }
  });

  test("Paper study A shows known, unknown, empty and unavailable as four different things", async ({ page }) => {
    await page.goto("/perfume/paper-study-a");
    await expect(page.locator("[data-layer='top'] [data-field='known']")).toContainText("Ivrel");
    await expect(page.locator("[data-layer='heart'] [data-field='unknown']")).toHaveText("Not supplied in this mock");
    await expect(page.locator("[data-layer='base'] [data-field='empty']")).toHaveText("No entries in this mock layer");
    await expect(page.locator("[data-layer='generalNotes'] [data-field='unknown']")).toBeVisible();
    await expect(page.locator("[data-visual-fallback]")).toContainText("Visual unavailable in this mock");
  });

  test("an unknown family and description are stated", async ({ page }) => {
    await page.goto("/perfume/glass-study-i");
    await expect(page.locator("dd [data-field='unknown']")).toHaveText("Unknown");
    await page.goto("/perfume/linen-study-f");
    await expect(page.getByText("Description not supplied in this mock")).toBeVisible();
  });

  test("a broken visual falls back without losing its title", async ({ page, problems }) => {
    await page.route("**/studies/glass-h.svg", (r) => r.abort());
    await ready(page, "/perfume/glass-study-h");
    await expect(page.locator("[data-visual-fallback]")).toBeVisible();
    await expect(page.locator("h1")).toHaveText("Glass study H");
    expect(problems.filter((p) => !/Failed to load resource/.test(p))).toEqual([]);
    problems.length = 0;
  });
});

test.describe("A03 search and filters", () => {
  test("Explore search and filters give exact ids and counts and keep focus", async ({ page }) => {
    await ready(page, "/explore");
    const input = page.getByLabel("Search mock catalogue", { exact: true }).locator("visible=true").last();
    const box = page.locator("main input");
    await expect(input).toBeVisible();
    const slugs = () => page.locator("[data-entry]").evaluateAll((els) => els.map((e) => (e as HTMLElement).dataset.entry));
    const requests: string[] = [];
    page.on("request", (r) => requests.push(r.url()));

    await box.fill("  STONE ");
    expect(await slugs()).toEqual(["stone-study-j", "stone-study-k"]);
    await expect(page.locator("main [data-count]")).toHaveText("2 mock studies");
    await expect(box).toBeFocused();
    await box.fill("กระดาษ");
    expect(await slugs()).toEqual(["paper-study-l"]);
    await box.fill("<img src=x onerror=alert(1)>");
    await expect(page.locator("[data-state='no-results']")).toBeVisible();
    await page.getByRole("button", { name: "Clear filters" }).click();
    await expect(box).toBeFocused();
    expect(await slugs()).toHaveLength(12);

    const note = page.locator("main").getByLabel("Note", { exact: true });
    await page.locator("main").getByLabel("Family", { exact: true }).selectOption("mock-family-deep");
    await note.selectOption("mock-note-008");
    expect(await slugs()).toEqual(["stone-study-j", "stone-study-k"]);
    await expect(page).toHaveURL("/explore?family=mock-family-deep&note=mock-note-008");
    await page.getByRole("button", { name: /remove note filter/ }).click();
    await expect(note).toBeFocused();
    expect(await slugs()).toEqual(["paper-study-c", "stone-study-j", "stone-study-k"]);
    await page.locator("main").getByLabel("Sort", { exact: true }).selectOption("name-desc");
    expect(await slugs()).toEqual(["stone-study-k", "stone-study-j", "paper-study-c"]);
    await page.getByRole("button", { name: "Clear all" }).click();
    await expect(page).toHaveURL(/\/explore$/);

    expect(requests.filter((u) => !/\/(studies|_next\/static|icon\.svg)/.test(u))).toEqual([]);
    expect(page.url()).not.toContain("STONE");
  });

  test("the query stops at 120 code points", async ({ page }) => {
    await ready(page, "/explore");
    const box = page.locator("main input");
    await box.fill("🜁".repeat(130));
    expect(Array.from(await box.inputValue())).toHaveLength(120);
  });

  test("the count is announced once after typing settles", async ({ page }) => {
    await ready(page, "/explore");
    await page.evaluate(() => {
      const node = document.querySelector("main [data-count-status]")!;
      const log: string[] = [];
      Object.assign(window, { announced: log });
      new MutationObserver(() => log.push(node.textContent ?? "")).observe(node, { childList: true, characterData: true, subtree: true });
    });
    await page.locator("main input").pressSequentially("stone", { delay: 40 });
    await page.waitForTimeout(900);
    expect(await page.evaluate(() => (window as unknown as { announced: string[] }).announced)).toEqual(["2 mock studies"]);
  });

  test("Search dialog uses the same semantics", async ({ page }) => {
    await ready(page, "/about");
    await page.getByRole("button", { name: "Search mock catalogue" }).click();
    const dialog = page.getByRole("dialog");
    await expect(dialog.getByRole("textbox")).toBeFocused();
    await expect(dialog.getByRole("listitem")).toHaveCount(12);
    await dialog.getByRole("textbox").fill("zzz");
    await expect(dialog.getByText("No mock fragrances found")).toBeVisible();
    await expect(dialog.getByRole("textbox")).toHaveValue("zzz");
    await dialog.getByRole("button", { name: "Clear search" }).click();
    await expect(dialog.getByRole("textbox")).toBeFocused();
    await dialog.getByRole("textbox").fill("glass study h");
    await dialog.getByRole("link", { name: /Glass study H/ }).click();
    await expect(page).toHaveURL(/glass-study-h$/);
    await expect(page.getByRole("dialog")).toHaveCount(0);
    await expect(page.locator("h1")).toBeFocused();
  });

  test("Back restores query, filters, scroll and the opened entry; reload resets the query", async ({ page }) => {
    await ready(page, "/explore?family=mock-family-soft");
    await page.locator("main input").fill("study");
    await page.setViewportSize({ width: 375, height: 700 });
    const link = page.getByRole("link", { name: "Linen study F" });
    await link.scrollIntoViewIfNeeded();
    const before = await page.evaluate(() => scrollY);
    await link.click();
    await expect(page.locator("h1")).toHaveText("Linen study F");
    await page.goBack();
    await expect(page.locator("main input")).toHaveValue("study");
    await expect(page).toHaveURL(/family=mock-family-soft$/);
    await expect(link).toBeFocused();
    expect(Math.abs((await page.evaluate(() => scrollY)) - before)).toBeLessThan(3);
    await page.reload();
    await expect(page.locator("main input")).toHaveValue("");
    await expect(page).toHaveURL(/family=mock-family-soft$/);
  });

  test("a fresh visit to Explore does not inherit an old query", async ({ page }) => {
    await ready(page, "/explore");
    await page.locator("main input").fill("zzz");
    await page.getByRole("navigation", { name: "Primary" }).getByRole("link", { name: "Notes" }).click();
    await page.locator("[data-note='mock-note-001'] a", { hasText: "Browse" }).click();
    await expect(page.locator("[data-entry]")).toHaveCount(5);
    await expect(page.locator("main input")).toHaveValue("");
  });
});

test.describe("A04 layers and notes", () => {
  test("layers, general notes and accords stay separate", async ({ page }) => {
    await page.goto("/perfume/stone-study-j");
    await expect(page.locator("[data-layer='base'] a")).toHaveCount(3);
    await expect(page.locator("[data-layer='generalNotes'] a")).toHaveCount(1);
    await expect(page.locator("[data-layer='accords'] a")).toHaveCount(0);
    await expect(page.locator("[data-layer='accords'] li")).toHaveText(["Settled weight", "Open weave"]);
    expect(await page.locator("main").innerText()).not.toMatch(/%|\bscore|similar|confidence|\bprice|฿|\$/i);
  });

  test("note links reach exactly the stated number of studies", async ({ page }) => {
    await page.goto("/notes");
    const rows = await page.locator("[data-note]").evaluateAll((els) =>
      els.map((el) => {
        const a = [...el.querySelectorAll("a")].find((x) => x.textContent?.startsWith("Browse"));
        return { id: (el as HTMLElement).dataset.note, href: a?.getAttribute("href"), count: Number(a?.textContent?.match(/\d+/)?.[0]) };
      }),
    );
    expect(rows).toHaveLength(9);
    for (const row of rows) {
      if (!row.href) continue;
      await page.goto(row.href);
      await expect(page.locator("[data-entry]")).toHaveCount(row.count);
    }
    expect(rows.filter((r) => !r.href).map((r) => r.id)).toEqual(["mock-note-009"]);
    await page.goto("/notes");
    await expect(page.locator("[data-note='mock-note-009']")).toContainText("Relationship not supplied");
  });

  test("note search, family and empty reset", async ({ page }) => {
    await ready(page, "/notes");
    await page.getByLabel("Family", { exact: true }).selectOption("mock-family-soft");
    await expect(page.locator("[data-note]")).toHaveCount(2);
    await page.locator("main input").fill("nothing");
    await page.getByRole("button", { name: "Show all notes" }).click();
    await expect(page.locator("[data-note]")).toHaveCount(9);
    await expect(page.locator("main input")).toBeFocused();
  });
});
