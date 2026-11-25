import assert from "node:assert/strict";
import { readdirSync } from "node:fs";
import { join } from "node:path";
import { test } from "node:test";
import { fixtures } from "../src/fixtures/data.ts";
import { assertFixtures, LIMITS, validateFixtures, VISUAL_IDS } from "../src/fixtures/validate.ts";
import { buildCatalogue } from "../src/fixtures/view-model.ts";

// eslint-disable-next-line @typescript-eslint/no-explicit-any -- negative controls need to break the types
type Loose = any;
const broken = (change: (set: Loose) => void): string[] => {
  const copy: Loose = structuredClone(fixtures);
  change(copy);
  return validateFixtures(copy);
};
const rejects = (name: string, change: (set: Loose) => void, expected: RegExp) =>
  test(`rejects ${name}`, () => {
    const errors = broken(change);
    assert.ok(errors.some((e) => expected.test(e)), `expected ${expected}, got: ${errors.join(" | ") || "no errors"}`);
  });

test("authored fixtures are valid and within the contract limits", () => {
  assert.deepEqual(validateFixtures(fixtures), []);
  for (const key of Object.keys(LIMITS) as (keyof typeof LIMITS)[]) assert.ok(fixtures[key].length <= LIMITS[key]);
});

rejects("synthetic false", (s) => (s.perfumes[0].synthetic = false), /synthetic must be literal true/);
rejects("synthetic missing", (s) => delete s.notes[0].synthetic, /"synthetic" is missing/);
rejects("a price", (s) => (s.perfumes[0].price = 10), /"price" is not allowed/);
rejects("a score", (s) => (s.perfumes[0].score = 0.9), /"score" is not allowed/);
rejects("a review", (s) => (s.perfumes[0].review = "x"), /"review" is not allowed/);
rejects("an external source", (s) => (s.perfumes[0].sourceUrl = "https://example.test"), /"sourceUrl" is not allowed/);
rejects("a source inside provenance", (s) => (s.perfumes[0].provenance = { ...s.perfumes[0].provenance, url: "x" }), /"url" is not allowed/);
rejects("missing provenance", (s) => delete s.perfumes[0].provenance, /provenance/);
rejects("a foreign provenance kind", (s) => (s.perfumes[0].provenance = { ...s.perfumes[0].provenance, kind: "import" }), /provenance\.kind/);
rejects("foreign rights", (s) => (s.perfumes[0].rights = "licensed"), /rights must be/);
rejects("a duplicate slug", (s) => (s.perfumes[1].slug = s.perfumes[0].slug), /perfumes\.slug: duplicate/);
rejects("a duplicate id", (s) => (s.perfumes[1].id = s.perfumes[0].id), /perfumes\.id: duplicate/);
rejects("an unsafe slug", (s) => (s.perfumes[0].slug = "../Paper"), /slug: is invalid/);
rejects("an unknown note reference", (s) => (s.perfumes[1].top = { state: "known", value: ["mock-note-999"] }), /unknown reference/);
rejects("a repeated note in a layer", (s) => (s.perfumes[1].top.value = ["mock-note-001", "mock-note-001"]), /duplicate/);
rejects("an unknown family reference", (s) => (s.perfumes[0].family = { state: "known", value: "floral" }), /unknown reference/);
rejects("unsafe HTML", (s) => (s.perfumes[0].name = "<img src=x onerror=alert(1)>"), /markup or a URL/);
rejects("a URL in text", (s) => (s.notes[0].descriptor = "see https://example.test"), /markup or a URL/);
rejects("oversized text", (s) => (s.perfumes[0].description = { state: "known", value: "x".repeat(601) }), /exceeds 600/);
rejects("oversized name in code points", (s) => (s.perfumes[0].name = "ก".repeat(121)), /exceeds 120/);
rejects("a remote visual", (s) => (s.perfumes[1].visual = { state: "known", value: "https://example.test/a.png" }), /owned local study/);
rejects("an unknown visual state", (s) => (s.perfumes[1].visual = { state: "unknown" }), /known or unavailable/);
rejects("null in place of unknown", (s) => (s.perfumes[0].heart = null), /field state object/);
rejects("an unknown field that carries a value", (s) => (s.perfumes[0].heart = { state: "unknown", value: [] }), /"value" is not allowed/);
rejects("a house that is not visibly mock", (s) => (s.perfumes[0].houseLabel = "Maison"), /visibly mock/);
rejects("too many studies", (s) => s.perfumes.push({ ...s.perfumes[0], id: "mock-perfume-013", slug: "paper-study-m" }), /more than 12/);
rejects("a duplicate article id", (s) => (s.articles[1].id = s.articles[0].id), /articles\.id: duplicate/);
rejects("an article anchor owned by the page", (s) => (s.articles[0].anchor = "journal"), /anchor: is invalid/);
rejects("a product-like slug", (s) => (s.perfumes[0].slug = "eau-no-five"), /slug: is invalid/);
rejects("a product-like name", (s) => (s.perfumes[0].name = "Eau No Five"), /visibly a study/);
rejects("a bare domain", (s) => (s.notes[0].descriptor = "see example.com"), /markup or a URL/);
rejects("a mail link", (s) => (s.notes[0].descriptor = "mailto:a"), /markup or a URL/);
rejects("a bidirectional override", (s) => (s.notes[0].descriptor = "a‮b"), /markup or a URL/);
rejects("a hole in a list", (s) => delete s.notes[8], /must be an object/);
rejects("an unknown featured slug", (s) => s.featured.push("nope"), /unknown reference/);

test("a failing set throws instead of dropping records", () => {
  assert.throws(() => assertFixtures({ ...fixtures, perfumes: [{}] }), /rejected/);
});

test("Paper study A keeps known, unknown, empty and unavailable apart", () => {
  const record = fixtures.perfumes.find((p) => p.slug === "paper-study-a");
  assert.deepEqual(record?.top, { state: "known", value: ["mock-note-001"] });
  assert.deepEqual(record?.heart, { state: "unknown" });
  assert.deepEqual(record?.base, { state: "known", value: [] });
  assert.deepEqual(record?.generalNotes, { state: "unknown" });
  assert.deepEqual(record?.visual, { state: "unavailable" });
});

test("membership is explicit and an unsupplied relationship is not zero", () => {
  const view = buildCatalogue(fixtures);
  assert.equal(view.notes.find((n) => n.id === "mock-note-009")?.membership, null);
  const f = view.entries.find((e) => e.slug === "linen-study-f");
  assert.deepEqual(f?.noteIds, ["mock-note-006", "mock-note-008"], "general notes only; no inferred layers");
  const listed = view.notes.find((n) => n.id === "mock-note-006")?.membership?.find((m) => m.slug === "linen-study-f");
  assert.deepEqual(listed?.places, ["General notes"]);
});

test("every referenced study exists as an owned local file", () => {
  const files = new Set(readdirSync(join(import.meta.dirname, "../public/studies")));
  for (const id of VISUAL_IDS) assert.ok(files.has(`${id}.svg`), id);
});
