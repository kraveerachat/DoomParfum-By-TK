import { expect, ready, test } from "./helpers";

// IMP-WEB-02 S3: alignment defects found in the Impeccable critique of the CP5 candidate.

for (const width of [1440, 390, 320]) {
  for (const path of ["/perfume/paper-study-a", "/th/perfume/paper-study-c"]) {
    test(`T3 record sheet values start on one column (${path}, ${width})`, async ({ page }) => {
      await page.setViewportSize({ width, height: 900 });
      await ready(page, path);
      const starts = await page.locator("[data-record-sheet] dd").evaluateAll((dds) => dds.map((dd) => Math.round(dd.getBoundingClientRect().left)));
      expect(starts).toHaveLength(6);
      expect(new Set(starts).size).toBe(1);
      const room = await page.locator("[data-record-sheet] dd").first().evaluate((dd) => dd.getBoundingClientRect().width);
      expect(room).toBeGreaterThan(120);
      // Two columns where they fit; a label above its value on the smallest phones.
      const beside = await page.locator("[data-record-sheet] > div").first().evaluate((row) => {
        return row.querySelector("dd")!.getBoundingClientRect().left > row.querySelector("dt")!.getBoundingClientRect().right;
      });
      expect(beside).toBe(width > 320);
    });
  }
}

test("T3 record sheet stacks under 200% text at 320 without sideways scroll", async ({ page }) => {
  await page.setViewportSize({ width: 320, height: 800 });
  await ready(page, "/perfume/stone-study-k");
  await page.evaluate(() => document.documentElement.style.setProperty("font-size", "200%"));
  const [stacked, scroll] = await page.evaluate(() => {
    const row = document.querySelectorAll("[data-record-sheet] > div")[3]!;
    const dt = row.querySelector("dt")!.getBoundingClientRect();
    const dd = row.querySelector("dd")!.getBoundingClientRect();
    return [dd.top >= dt.bottom - 1, document.documentElement.scrollWidth - document.documentElement.clientWidth] as const;
  });
  expect(stacked).toBe(true);
  expect(scroll).toBe(0);
});

for (const path of ["/", "/th"]) {
  test(`footer language names start on the footer column (${path})`, async ({ page }) => {
    await ready(page, path);
    const [links, lang] = await page.evaluate(() => [
      Math.round(document.querySelector("footer ul a")!.getBoundingClientRect().left),
      Math.round(document.querySelector("footer .lang-footer .lang-label")!.getBoundingClientRect().left),
    ]);
    expect(lang).toBe(links);
  });
}
