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
    });
  }
}

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
