/**
 * Original fictional content authored for IMP-WEB-01. No record describes a real
 * fragrance, house, ingredient, price, review or formula.
 */
import type { Field, FixtureSet, PerfumeFixture } from "./types.ts";

const mark = {
  synthetic: true,
  rights: "project_owned_synthetic",
  provenance: { kind: "locally_authored_fixture", fixtureVersion: "1.0.0", authoredFor: "IMP-WEB-01" },
} as const;

const known = <T>(value: T) => ({ state: "known", value }) as const;
const unknown = { state: "unknown" } as const;
const pad = (i: number) => String(i).padStart(3, "0");
const n = (...ids: number[]): Field<readonly string[]> => known(ids.map((i) => `mock-note-${pad(i)}`));
const a = (...ids: number[]): Field<readonly string[]> => known(ids.map((i) => `mock-accord-${pad(i)}`));

const BRIGHT = known("mock-family-bright");
const SOFT = known("mock-family-soft");
const DEEP = known("mock-family-deep");
const HOUSE = "DoomParfum mock atelier";

type Draft = Omit<PerfumeFixture, "id" | "synthetic" | "rights" | "provenance" | "houseLabel">;

const drafts: readonly Draft[] = [
  {
    slug: "paper-study-a",
    name: "Paper study A",
    description: known(
      "A fictional record kept deliberately incomplete. Its heart was never supplied, and its base was authored as empty. The two read differently on purpose.",
    ),
    family: BRIGHT,
    top: n(1),
    heart: unknown,
    base: n(),
    generalNotes: unknown,
    accords: unknown,
    visual: { state: "unavailable" },
  },
  {
    slug: "paper-study-b",
    name: "Paper study B",
    description: known("A fictional sheet folded once, written as a quiet opening that settles without hurry."),
    family: SOFT,
    top: n(1, 3),
    heart: n(6),
    base: n(4),
    generalNotes: n(),
    accords: a(1),
    visual: known("paper-b"),
  },
  {
    slug: "paper-study-c",
    name: "Paper study C",
    description: known("A fictional page of late ink. Most of its weight was authored into the last layer."),
    family: DEEP,
    top: n(5),
    heart: n(7),
    base: n(7, 4),
    generalNotes: unknown,
    accords: a(3),
    visual: known("paper-c"),
  },
  {
    slug: "linen-study-d",
    name: "Linen study D",
    description: known("Fictional cloth in morning light: one thread at the start, one at the end, and room between them."),
    family: SOFT,
    top: n(2),
    heart: n(6, 2),
    base: n(8),
    generalNotes: n(6),
    accords: a(1, 2),
    visual: known("linen-d"),
  },
  {
    slug: "linen-study-e",
    name: "Linen study E",
    description: known(
      "A fictional weave recorded at three distances. Every layer was supplied, so this is the plainest record to read first.",
    ),
    family: SOFT,
    top: n(3, 2),
    heart: n(6, 8),
    base: n(4),
    generalNotes: n(2),
    accords: a(2),
    visual: known("linen-e"),
  },
  {
    slug: "linen-study-f",
    name: "Linen study F",
    description: unknown,
    family: SOFT,
    top: unknown,
    heart: unknown,
    base: unknown,
    generalNotes: n(6, 8),
    accords: unknown,
    visual: known("linen-f"),
  },
  {
    slug: "glass-study-g",
    name: "Glass study G",
    description: known("A fictional pane seen edge-on. Bright at the rim, then almost nothing."),
    family: BRIGHT,
    top: n(3, 1),
    heart: n(5),
    base: n(),
    generalNotes: n(),
    accords: a(4),
    visual: known("glass-g"),
  },
  {
    slug: "glass-study-h",
    name: "Glass study H",
    description: known("Fictional light through two curved surfaces, arriving in order: rim, slate, wax."),
    family: BRIGHT,
    top: n(3),
    heart: n(5, 1),
    base: n(6),
    generalNotes: n(3),
    accords: a(4, 1),
    visual: known("glass-h"),
  },
  {
    slug: "glass-study-i",
    name: "Glass study I",
    description: known(
      "A fictional study whose family was never assigned. It stays in the catalogue with its family shown as unknown.",
    ),
    family: unknown,
    top: n(5),
    heart: n(3),
    base: unknown,
    generalNotes: unknown,
    accords: a(),
    visual: known("glass-i"),
  },
  {
    slug: "stone-study-j",
    name: "Stone study J",
    description: known(
      "Fictional strata, read from the surface down. The base carries three labels and is the longest list in this mock.",
    ),
    family: DEEP,
    top: n(5),
    heart: n(8, 4),
    base: n(7, 4, 8),
    generalNotes: n(7),
    accords: a(3, 2),
    visual: known("stone-j"),
  },
  {
    slug: "stone-study-k",
    name: "Stone study K",
    description: known(
      "A fictional boulder with a long and slightly impractical description, kept here so that wrapping, zooming and larger text can be checked against something more demanding than a single tidy line. It names no real material and makes no claim about wear.",
    ),
    family: DEEP,
    top: n(),
    heart: n(7),
    base: n(4, 8),
    generalNotes: unknown,
    accords: a(3),
    visual: known("stone-k"),
  },
  {
    slug: "paper-study-l",
    name: "แบบศึกษากระดาษ ลำดับที่สิบสอง",
    description: known(
      "แบบศึกษาสมมติสำหรับตรวจสอบการแสดงผลอักษรไทย การตัดบรรทัด และวรรณยุกต์ ไม่ใช่น้ำหอมจริงและไม่มีข้อมูลผลิตภัณฑ์จริง",
    ),
    family: SOFT,
    top: n(1),
    heart: n(2),
    base: n(6),
    generalNotes: n(),
    accords: a(1),
    visual: known("paper-l"),
  },
];

export const fixtures: FixtureSet = {
  families: [
    { id: "mock-family-bright", label: "Bright study", descriptor: "Edges, rims and thin light.", ...mark },
    { id: "mock-family-soft", label: "Soft study", descriptor: "Folds, threads and slow curves.", ...mark },
    { id: "mock-family-deep", label: "Deep study", descriptor: "Strata, weight and late ink.", ...mark },
  ],
  accords: [
    { id: "mock-accord-001", label: "Folded quiet", ...mark },
    { id: "mock-accord-002", label: "Open weave", ...mark },
    { id: "mock-accord-003", label: "Settled weight", ...mark },
    { id: "mock-accord-004", label: "Clear edge", ...mark },
  ],
  notes: [
    { id: "mock-note-001", label: "Ivrel", descriptor: "The cool edge of a cut sheet.", family: BRIGHT, ...mark },
    { id: "mock-note-002", label: "Oskane", descriptor: "A dry thread pulled straight.", family: SOFT, ...mark },
    { id: "mock-note-003", label: "Tavren", descriptor: "A bright rim, seen edge-on.", family: BRIGHT, ...mark },
    { id: "mock-note-004", label: "Marovane", descriptor: "Warm dust on a high shelf.", family: DEEP, ...mark },
    { id: "mock-note-005", label: "Quellis", descriptor: "Wet slate before noon.", family: BRIGHT, ...mark },
    { id: "mock-note-006", label: "Sendrel", descriptor: "Soft wax, barely marked.", family: SOFT, ...mark },
    { id: "mock-note-007", label: "Ondrith", descriptor: "Late ink, not yet dry.", family: DEEP, ...mark },
    { id: "mock-note-008", label: "Luthmere", descriptor: "A pale trace left in a room.", family: unknown, ...mark },
    { id: "mock-note-009", label: "Vesk", descriptor: "A label with no supplied relationships.", family: unknown, ...mark },
  ],
  perfumes: drafts.map((d, i) => ({ id: `mock-perfume-${pad(i + 1)}`, houseLabel: HOUSE, ...d, ...mark })),
  articles: [
    {
      id: "mock-article-001",
      anchor: "journal-reading-a-layer",
      title: "Reading a layer",
      excerpt: "Top, heart and base are an order of reading. They are not a recipe.",
      body: [
        "Every record in this mock can carry three layers. Top is what was written first, heart is what was written to stay, and base is what was written to remain. The order describes reading, in the way chapters do.",
        "A layer holds labels, never amounts. Nothing here says how much of anything exists, how long it lasts or what it is made of. When a record lists one label and another lists three, the second list is longer and that is all it means.",
        "General notes sit apart from the layers. They belong to the whole record and are never moved up or down to fill a gap.",
      ],
      ...mark,
    },
    {
      id: "mock-article-002",
      anchor: "journal-empty-is-not-unknown",
      title: "Empty is not unknown",
      excerpt: "Two records can look equally bare and mean opposite things.",
      body: [
        "Paper study A has a heart that was never supplied and a base that was authored as empty. The first is a question nobody has answered. The second is an answer.",
        "Catalogues often flatten the two into one blank space, and a reader then fills that space with a guess. This notebook keeps them apart: one says it was not supplied, the other says it has no entries.",
        "The same care applies to a family, a description or a picture. When something is missing, the page says what is missing and leaves it there.",
      ],
      ...mark,
    },
  ],
  featured: ["glass-study-h", "linen-study-e", "stone-study-j"],
};
