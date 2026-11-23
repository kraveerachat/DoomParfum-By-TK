import assert from "node:assert/strict";
import { test } from "node:test";
import { clipQuery, exploreHref, filterEntries, filterNotes, matchesText, parseQuery, sortEntries } from "../src/catalogue/search.ts";
import { fixtures } from "../src/fixtures/data.ts";
import { buildCatalogue } from "../src/fixtures/view-model.ts";

const view = buildCatalogue(fixtures);
const NONE = { family: null, note: null };
const slugs = (query: string, filters: { family: string | null; note: string | null } = NONE) =>
  filterEntries(view.entries, query, filters).map((e) => e.slug).sort();
const allowed = { families: new Set(view.families.map((f) => f.id)), notes: new Set(view.notes.map((n) => n.id)) };
const parse = (q: string) => parseQuery(new URLSearchParams(q), allowed);

test("a blank query lists every study", () => {
  assert.equal(slugs("").length, 12);
  assert.equal(slugs("   ").length, 12);
});

test("case and Unicode form do not matter", () => {
  assert.deepEqual(slugs("gLaSs STUDY h"), ["glass-study-h"]);
  assert.deepEqual(slugs("Ｇｌａｓｓ study h"), ["glass-study-h"]);
  assert.deepEqual(slugs("กระดาษ"), ["paper-study-l"]);
});

test("a missing description contributes no match", () => {
  assert.ok(!slugs("fictional").includes("linen-study-f"));
});

test("HTML-looking and regex-looking text is literal", () => {
  for (const q of ["<script>alert(1)</script>", ".*", "(", "[a-z]", "\\"]) assert.deepEqual(slugs(q), [], q);
  assert.equal(matchesText(".*", ["a.*b"]), true);
});

test("the query limit is 120 code points, not UTF-16 units", () => {
  assert.equal(Array.from(clipQuery("🜁".repeat(130))).length, 120);
  assert.equal(clipQuery("a".repeat(120)).length, 120);
  assert.equal(clipQuery("a".repeat(121)).length, 120);
  assert.equal(matchesText("a".repeat(121), ["a".repeat(120)]), true);
});

test("family and note combine with AND", () => {
  const family = slugs("", { family: "mock-family-deep", note: null });
  assert.deepEqual(family, ["paper-study-c", "stone-study-j", "stone-study-k"]);
  assert.deepEqual(slugs("", { family: "mock-family-deep", note: "mock-note-008" }), ["stone-study-j", "stone-study-k"]);
  assert.deepEqual(slugs("surface", { family: "mock-family-deep", note: "mock-note-008" }), ["stone-study-j"]);
  assert.deepEqual(slugs("", { family: "mock-family-bright", note: "mock-note-007" }), []);
});

test("unknown membership never matches", () => {
  assert.deepEqual(slugs("", { family: null, note: "mock-note-009" }), []);
  for (const f of view.families) assert.ok(!slugs("", { family: f.id, note: null }).includes("glass-study-i"));
});

test("sorting is deterministic with an id tie-break", () => {
  const twin = view.entries.slice(0, 1).map((e) => ({ ...e, id: "mock-perfume-000" }));
  const [first] = sortEntries([...view.entries.slice(0, 1), ...twin], "name-asc");
  assert.equal(first?.id, "mock-perfume-000");
  const names = (s: "name-asc" | "name-desc") => sortEntries(view.entries, s).map((e) => e.name);
  assert.equal(names("name-asc")[0], "Glass study G");
  assert.deepEqual(names("name-desc"), names("name-asc").reverse());
});

test("URL filters accept only allowlisted single values", () => {
  assert.deepEqual(parse("family=mock-family-soft&note=mock-note-001"), {
    filters: { family: "mock-family-soft", note: "mock-note-001" }, invalid: false, unsupported: false,
  });
  assert.equal(parse("family=floral").invalid, true);
  assert.equal(parse("family=").invalid, true);
  assert.equal(parse("note=mock-note-001&note=mock-note-002").invalid, true);
  assert.equal(parse("note=__proto__").invalid, true);
  assert.deepEqual([parse("q=x").unsupported, parse("q=x").invalid], [true, false]);
});

test("explore links carry ids only", () => {
  assert.equal(exploreHref(NONE), "/explore");
  assert.equal(exploreHref({ family: "mock-family-soft", note: "mock-note-001" }), "/explore?family=mock-family-soft&note=mock-note-001");
});

test("note search covers labels and descriptors", () => {
  assert.deepEqual(filterNotes(view.notes, "ink", null).map((n) => n.label), ["Ondrith"]);
  assert.deepEqual(filterNotes(view.notes, "", "mock-family-soft").map((n) => n.label), ["Oskane", "Sendrel"]);
  assert.deepEqual(filterNotes(view.notes, "zzz", null), []);
});
