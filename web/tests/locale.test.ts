import assert from "node:assert/strict";
import { readFileSync } from "node:fs";
import { join } from "node:path";
import { test } from "node:test";
import { filterEntries, filterNotes } from "../src/catalogue/search.ts";
import { fixtures } from "../src/fixtures/data.ts";
import { thaiOverlay } from "../src/fixtures/th.ts";
import { validateOverlay } from "../src/fixtures/validate-overlay.ts";
import { buildCatalogue } from "../src/fixtures/view-model.ts";
import { hasThai, localeOf, localize, logicalPath, textLang } from "../src/i18n/locale.ts";
import { en, th } from "../src/i18n/messages.ts";

const NONE = { family: null, note: null } as const;

test("locale paths: English keeps V1 paths, Thai lives under /th only", () => {
  assert.equal(localeOf("/"), "en");
  assert.equal(localeOf("/explore"), "en");
  assert.equal(localeOf("/th"), "th");
  assert.equal(localeOf("/th/perfume/paper-study-a"), "th");
  assert.equal(localeOf("/TH"), "en");
  assert.equal(localeOf("/thx"), "en");
  assert.equal(logicalPath("/th"), "/");
  assert.equal(logicalPath("/th/notes"), "/notes");
  assert.equal(localize("en", "/about#journal"), "/about#journal");
  assert.equal(localize("th", "/"), "/th");
  assert.equal(localize("th", "/explore?note=mock-note-001"), "/th/explore?note=mock-note-001");
  assert.equal(localize("th", "/about#credits"), "/th/about#credits");
  assert.equal(localize("th", "#purpose"), "#purpose");
  assert.equal(textLang("Paper study A", "th"), "en");
  assert.equal(textLang("แบบศึกษา", "en"), "th");
  assert.equal(textLang("Paper study A", "en"), undefined);
});

test("V02: both dictionaries have the same keys and no empty text", () => {
  const walk = (a: unknown, b: unknown, path: string): void => {
    if (typeof a === "string") {
      assert.equal(typeof b, "string", path);
      assert.ok((b as string).trim() !== "", `${path} is empty in Thai`);
      return;
    }
    const ka = Object.keys(a as object).sort();
    assert.deepEqual(Object.keys(b as object).sort(), ka, path);
    for (const k of ka) walk((a as Record<string, unknown>)[k], (b as Record<string, unknown>)[k], `${path}.${k}`);
  };
  walk(en, th, "messages");
});

test("V02: Thai interface text is Thai, apart from names, short codes and placeholders", () => {
  const latinAllowed = new Set(["site.name", "language.enShort", "language.enName", "language.thShort", "explore.sortAsc", "explore.sortDesc"]);
  const walk = (v: unknown, path: string): void => {
    if (typeof v === "string") {
      if (!latinAllowed.has(path)) assert.ok(hasThai(v), `${path} has no Thai: ${v}`);
      return;
    }
    for (const [k, x] of Object.entries(v as object)) walk(x, path ? `${path}.${k}` : k);
  };
  walk(th, "");
});

test("V04: the Thai overlay is valid and only translates existing prose", () => {
  assert.deepEqual(validateOverlay(thaiOverlay, fixtures), []);
});

// eslint-disable-next-line @typescript-eslint/no-explicit-any -- negative controls need to break the types
type Loose = any;
const broken = (change: (o: Loose) => void) => {
  const copy: Loose = structuredClone(thaiOverlay);
  change(copy);
  return validateOverlay(copy, fixtures);
};
const rejects = (name: string, change: (o: Loose) => void, expected: RegExp) =>
  test(`V04 overlay rejects ${name}`, () => {
    const errors = broken(change);
    assert.ok(errors.some((e) => expected.test(e)), `expected ${expected}, got: ${errors.join(" | ") || "no errors"}`);
  });
rejects("an unknown fixture id", (o) => (o.notes["mock-note-999"] = { descriptor: { th: "ใหม่", review: "draft" } }), /unknown fixture id/);
rejects("a new name", (o) => (o.notes["mock-note-001"].label = { th: "ไอเวรล", review: "draft" }), /"label" is not allowed/);
rejects("text for an unknown field", (o) => (o.perfumes["mock-perfume-006"] = { description: { th: "คำบรรยาย", review: "draft" } }), /source field is unknown/);
rejects("over-long text", (o) => (o.notes["mock-note-001"].descriptor.th = "ก".repeat(201)), /exceeds 200/);
rejects("markup", (o) => (o.notes["mock-note-001"].descriptor.th = "ขอบ <b>เย็น</b>"), /markup or a URL/);
rejects("a URL", (o) => (o.notes["mock-note-001"].descriptor.th = "ดูที่ https://example.test"), /markup or a URL/);
// The shipped texts carry the Owner's review record (S6), so the control removes it as well.
rejects("a reviewed mark without a review record", (o) => {
  o.notes["mock-note-001"].descriptor.review = "reviewed";
  delete o.notes["mock-note-001"].descriptor.reviewRecord;
}, /review record/);
rejects("non-Thai text", (o) => (o.notes["mock-note-001"].descriptor.th = "Cool edge"), /must be Thai/);
rejects("a changed paragraph count", (o) => o.articles["mock-article-001"].body.th.pop(), /paragraphs/);
rejects("a relationship field", (o) => (o.perfumes["mock-perfume-002"].top = ["mock-note-001"]), /"top" is not allowed/);

test("V06: English results do not change with the Thai overlay", () => {
  const v1 = buildCatalogue(fixtures);
  const v11 = buildCatalogue(fixtures, "en", thaiOverlay);
  for (const q of ["", "paper", "fictional", "ink", "study", "a", "late", "unknown", "empty"]) {
    assert.deepEqual(filterEntries(v11.entries, q, NONE).map((e) => e.id), filterEntries(v1.entries, q, NONE).map((e) => e.id), q);
    assert.deepEqual(filterNotes(v11.notes, q, null).map((n) => n.id), filterNotes(v1.notes, q, null).map((n) => n.id), q);
  }
});

test("V06: on English pages a Thai query adds exactly the records whose reviewed Thai text matches (4.5)", () => {
  const v1 = buildCatalogue(fixtures);
  const v11 = buildCatalogue(fixtures, "en", thaiOverlay);
  const ids = (xs: readonly { id: string }[]) => xs.map((x) => x.id).sort();
  // Every shipped overlay text is Owner-reviewed (S6), so each one takes part for a Thai query.
  assert.ok(v11.entries.every((e) => e.extra.every((t) => /[฀-๿]/.test(t))));
  for (const q of ["ไม่", "แบบ", "หมึก", "ฮาร์ตโน้ต", "ก้อนหิน"]) {
    const base = ids(filterEntries(v1.entries, q, NONE));
    const expected = v11.entries.filter((e) => base.includes(e.id) || e.extra.some((t) => t.includes(q))).map((e) => e.id);
    assert.deepEqual(ids(filterEntries(v11.entries, q, NONE)), expected, q);
    const baseNotes = ids(filterNotes(v1.notes, q, null));
    const expectedNotes = v11.notes.filter((n) => baseNotes.includes(n.id) || n.extra.some((t) => t.includes(q))).map((n) => n.id);
    assert.deepEqual(ids(filterNotes(v11.notes, q, null)), expectedNotes, q);
  }
  // The reviewed path is live: Paper study C is found from an English page by its Thai description.
  assert.ok(ids(filterEntries(v11.entries, "หมึกยามดึก", NONE)).includes("mock-perfume-003"));
  assert.ok(!ids(filterEntries(v1.entries, "หมึกยามดึก", NONE)).includes("mock-perfume-003"));
});

test("V06: production builds the English view with the overlay (reviewed text can become searchable)", () => {
  const source = readFileSync(join(import.meta.dirname, "../src/server/catalogue.ts"), "utf8");
  assert.match(source, /export const catalogue = buildCatalogue\(fixtureSet, "en", overlay\)/);
});

test("V06: a reviewed Thai text joins English search only for a Thai query", () => {
  const overlay = structuredClone(thaiOverlay) as Loose;
  overlay.perfumes["mock-perfume-003"].description = { th: "หน้ากระดาษสมมติที่เขียนด้วยหมึกยามดึก", review: "reviewed", reviewRecord: "test" };
  const view = buildCatalogue(fixtures, "en", overlay);
  assert.deepEqual(filterEntries(view.entries, "หมึก", NONE).map((e) => e.slug), ["paper-study-c"]);
  assert.ok(!filterEntries(view.entries, "late ink", NONE).some((e) => e.extra.length && e.slug !== "paper-study-c"));
});

test("V06: Thai pages search the shown Thai text and the English source", () => {
  const view = buildCatalogue(fixtures, "th", thaiOverlay);
  assert.deepEqual(filterEntries(view.entries, "หมึกยามดึก", NONE).map((e) => e.slug), ["paper-study-c"]);
  assert.deepEqual(filterEntries(view.entries, "late ink", NONE).map((e) => e.slug), ["paper-study-c"]);
  assert.deepEqual(filterEntries(view.entries, "Paper study A", NONE).map((e) => e.slug), ["paper-study-a"]);
  assert.deepEqual(filterNotes(view.notes, "หินชนวน", null).map((n) => n.label), ["Quellis"]);
  // Names, IDs, relationships and order are those of the English catalogue.
  const enView = buildCatalogue(fixtures);
  assert.deepEqual(filterEntries(view.entries, "", NONE).map((e) => e.id), filterEntries(enView.entries, "", NONE).map((e) => e.id));
  assert.deepEqual(view.notes.map((n) => [n.id, n.label, n.membership?.length ?? null]), enView.notes.map((n) => [n.id, n.label, n.membership?.length ?? null]));
});

test("V06: Thai and combining-mark queries stay within the 120 code point limit and match literally", () => {
  const view = buildCatalogue(fixtures, "th", thaiOverlay);
  assert.deepEqual(filterEntries(view.entries, "ก".repeat(500), NONE), []);
  assert.deepEqual(filterEntries(view.entries, "(.*)", NONE), []);
  assert.ok(filterEntries(view.entries, "ที่สิบสอง", NONE).some((e) => e.slug === "paper-study-l"));
});
