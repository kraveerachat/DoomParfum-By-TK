/**
 * Strict validator for the synthetic fixture contract (DPT-PLAN-012, Luxury_Mock_Fixture_Contract).
 * Unknown keys are rejected, so price, score, review, seller and source fields cannot enter.
 */
import type { FixtureSet } from "./types.ts";

export const LIMITS = { perfumes: 12, notes: 9, families: 3, accords: 4, articles: 2 } as const;
export const VISUAL_IDS = [
  "glass-g", "glass-h", "glass-i", "linen-d", "linen-e", "linen-f",
  "paper-b", "paper-c", "paper-l", "stone-j", "stone-k",
] as const;

const MARK_KEYS = ["synthetic", "rights", "provenance"];
const KEYS = {
  family: ["id", "label", "descriptor", ...MARK_KEYS],
  accord: ["id", "label", ...MARK_KEYS],
  note: ["id", "label", "descriptor", "family", ...MARK_KEYS],
  perfume: [
    "id", "slug", "name", "houseLabel", "description", "family", "top", "heart", "base",
    "generalNotes", "accords", "visual", ...MARK_KEYS,
  ],
  article: ["id", "anchor", "title", "excerpt", "body", ...MARK_KEYS],
  set: ["families", "accords", "notes", "perfumes", "articles", "featured"],
  provenance: ["kind", "fixtureVersion", "authoredFor"],
} as const;

const SLUG = /^[a-z0-9]+(?:-[a-z0-9]+)*$/;
const UNSAFE = /[<>]|https?:|data:|javascript:|\/\//i;

type Obj = Record<string, unknown>;
const isObj = (v: unknown): v is Obj => typeof v === "object" && v !== null && !Array.isArray(v);

export function validateFixtures(input: unknown): string[] {
  const errors: string[] = [];
  const fail = (path: string, message: string): void => {
    errors.push(`${path}: ${message}`);
  };

  const exactKeys = (path: string, value: Obj, allowed: readonly string[]): void => {
    for (const key of Object.keys(value)) if (!allowed.includes(key)) fail(path, `field "${key}" is not allowed`);
    for (const key of allowed) if (!(key in value)) fail(path, `field "${key}" is missing`);
  };
  const text = (path: string, value: unknown, max: number): void => {
    if (typeof value !== "string" || value.trim() === "") return fail(path, "must be non-empty text");
    if (Array.from(value).length > max) fail(path, `exceeds ${max} code points`);
    if (UNSAFE.test(value)) fail(path, "contains markup or a URL");
  };
  const marked = (path: string, value: Obj): void => {
    if (value.synthetic !== true) fail(path, "synthetic must be literal true");
    if (value.rights !== "project_owned_synthetic") fail(path, "rights must be project_owned_synthetic");
    if (!isObj(value.provenance)) return fail(path, "provenance is missing");
    exactKeys(`${path}.provenance`, value.provenance, KEYS.provenance);
    if (value.provenance.kind !== "locally_authored_fixture") {
      fail(path, "provenance.kind must be locally_authored_fixture");
    }
    text(`${path}.provenance.fixtureVersion`, value.provenance.fixtureVersion, 20);
    text(`${path}.provenance.authoredFor`, value.provenance.authoredFor, 40);
  };
  const field = (path: string, value: unknown, check: (path: string, v: unknown) => void): void => {
    if (!isObj(value)) return fail(path, "must be a field state object");
    if (value.state === "unknown") return exactKeys(path, value, ["state"]);
    if (value.state !== "known") return fail(path, "state must be known or unknown");
    exactKeys(path, value, ["state", "value"]);
    check(path, value.value);
  };
  const list = (name: keyof typeof LIMITS, value: unknown): Obj[] => {
    if (!Array.isArray(value)) {
      fail(name, "must be a list");
      return [];
    }
    if (value.length > LIMITS[name]) fail(name, `has more than ${LIMITS[name]} records`);
    return value.filter((v, i): v is Obj => {
      if (!isObj(v)) fail(`${name}[${i}]`, "must be an object");
      return isObj(v);
    });
  };
  const unique = (name: string, values: readonly unknown[]): Set<unknown> => {
    const seen = new Set<unknown>();
    for (const v of values) {
      if (seen.has(v)) fail(name, `duplicate "${String(v)}"`);
      seen.add(v);
    }
    return seen;
  };
  const idPattern = (path: string, value: unknown, pattern: RegExp): void => {
    if (typeof value !== "string" || !pattern.test(value)) fail(path, "has an invalid id");
  };
  const ref = (pool: Set<unknown>) => (path: string, value: unknown): void => {
    if (typeof value !== "string" || !pool.has(value)) fail(path, `unknown reference "${String(value)}"`);
  };
  const refs = (pool: Set<unknown>) => (path: string, value: unknown): void => {
    if (!Array.isArray(value)) return fail(path, "must be a list");
    unique(path, value);
    for (const v of value) ref(pool)(path, v);
  };

  if (!isObj(input)) return ["fixtures: must be an object"];
  exactKeys("fixtures", input, KEYS.set);

  const families = list("families", input.families);
  const accords = list("accords", input.accords);
  const notes = list("notes", input.notes);
  const perfumes = list("perfumes", input.perfumes);
  const articles = list("articles", input.articles);
  const familyIds = unique("families.id", families.map((f) => f.id));
  const accordIds = unique("accords.id", accords.map((a) => a.id));
  const noteIds = unique("notes.id", notes.map((n) => n.id));
  unique("perfumes.id", perfumes.map((p) => p.id));
  const slugs = unique("perfumes.slug", perfumes.map((p) => p.slug));
  unique("articles.anchor", articles.map((a) => a.anchor));

  families.forEach((f, i) => {
    const p = `families[${i}]`;
    exactKeys(p, f, KEYS.family);
    marked(p, f);
    idPattern(p, f.id, /^mock-family-[a-z]+$/);
    text(`${p}.label`, f.label, 60);
    text(`${p}.descriptor`, f.descriptor, 200);
  });
  accords.forEach((a, i) => {
    const p = `accords[${i}]`;
    exactKeys(p, a, KEYS.accord);
    marked(p, a);
    idPattern(p, a.id, /^mock-accord-\d{3}$/);
    text(`${p}.label`, a.label, 60);
  });
  notes.forEach((n, i) => {
    const p = `notes[${i}]`;
    exactKeys(p, n, KEYS.note);
    marked(p, n);
    idPattern(p, n.id, /^mock-note-\d{3}$/);
    text(`${p}.label`, n.label, 60);
    text(`${p}.descriptor`, n.descriptor, 200);
    field(`${p}.family`, n.family, ref(familyIds));
  });
  perfumes.forEach((f, i) => {
    const p = `perfumes[${i}]`;
    exactKeys(p, f, KEYS.perfume);
    marked(p, f);
    idPattern(p, f.id, /^mock-perfume-\d{3}$/);
    if (typeof f.slug !== "string" || f.slug.length > 80 || !SLUG.test(f.slug)) fail(`${p}.slug`, "is invalid");
    text(`${p}.name`, f.name, 120);
    text(`${p}.houseLabel`, f.houseLabel, 120);
    if (typeof f.houseLabel === "string" && !/\bmock\b/i.test(f.houseLabel)) {
      fail(`${p}.houseLabel`, "must be visibly mock");
    }
    field(`${p}.description`, f.description, (path, v) => text(path, v, 600));
    field(`${p}.family`, f.family, ref(familyIds));
    for (const layer of ["top", "heart", "base", "generalNotes"] as const) {
      field(`${p}.${layer}`, f[layer], refs(noteIds));
    }
    field(`${p}.accords`, f.accords, refs(accordIds));
    if (isObj(f.visual) && f.visual.state === "unavailable") exactKeys(`${p}.visual`, f.visual, ["state"]);
    else if (isObj(f.visual) && f.visual.state === "unknown") fail(`${p}.visual`, "must be known or unavailable");
    else {
      field(`${p}.visual`, f.visual, (path, v) => {
        if (!(VISUAL_IDS as readonly unknown[]).includes(v)) fail(path, "must be an owned local study id");
      });
    }
  });
  articles.forEach((a, i) => {
    const p = `articles[${i}]`;
    exactKeys(p, a, KEYS.article);
    marked(p, a);
    idPattern(p, a.id, /^mock-article-\d{3}$/);
    if (typeof a.anchor !== "string" || !SLUG.test(a.anchor)) fail(`${p}.anchor`, "is invalid");
    text(`${p}.title`, a.title, 120);
    text(`${p}.excerpt`, a.excerpt, 240);
    if (!Array.isArray(a.body) || a.body.length === 0) fail(`${p}.body`, "must be a non-empty list");
    else a.body.forEach((t, j) => text(`${p}.body[${j}]`, t, 900));
  });
  if (!Array.isArray(input.featured)) fail("featured", "must be a list");
  else {
    unique("featured", input.featured);
    for (const s of input.featured) ref(slugs)("featured", s);
  }

  return errors;
}

export function assertFixtures(input: unknown): FixtureSet {
  const errors = validateFixtures(input);
  if (errors.length) throw new Error(`Synthetic fixtures rejected:\n- ${errors.join("\n- ")}`);
  return input as FixtureSet;
}
