/**
 * Validator for the Thai overlay (DPT-PLAN-013 4.3, Luxury_Mock_Fixture_Contract amendment). The overlay
 * may only translate existing prose: unknown IDs, new keys (names, notes, relationships), text for a
 * field whose state is unknown, markup, URLs, over-long text and a "reviewed" mark without a review
 * record are rejected.
 */
import type { FixtureSet, ThaiOverlay } from "./types.ts";
import { isObj, UNSAFE, type Obj } from "./validate.ts";

const hasThai = (text: string) => /[฀-๿]/.test(text);

export function validateOverlay(input: unknown, fixtures: FixtureSet): string[] {
  const errors: string[] = [];
  const fail = (path: string, message: string): void => {
    errors.push(`overlay.${path}: ${message}`);
  };
  const exactKeys = (path: string, value: Obj, allowed: readonly string[], optional: readonly string[] = []): void => {
    for (const key of Object.keys(value)) if (![...allowed, ...optional].includes(key)) fail(path, `field "${key}" is not allowed`);
    for (const key of allowed) if (!(key in value)) fail(path, `field "${key}" is missing`);
  };
  const line = (path: string, value: unknown, max: number): void => {
    if (typeof value !== "string" || value.trim() === "") return fail(path, "must be non-empty text");
    if (Array.from(value).length > max) fail(path, `exceeds ${max} code points`);
    if (UNSAFE.test(value)) fail(path, "contains markup or a URL");
    if (!hasThai(value)) fail(path, "must be Thai text");
  };
  const text = (path: string, value: unknown, max: number, paragraphs?: number): void => {
    if (!isObj(value)) return fail(path, "must be an overlay text object");
    const reviewed = value.review === "reviewed";
    exactKeys(path, value, reviewed ? ["th", "review", "reviewRecord"] : ["th", "review"]);
    if (value.review !== "draft" && !reviewed) fail(path, "review must be draft or reviewed");
    if (reviewed && (typeof value.reviewRecord !== "string" || value.reviewRecord.trim() === "")) {
      fail(path, "a reviewed text needs the Owner's review record");
    }
    if (paragraphs === undefined) return line(`${path}.th`, value.th, max);
    if (!Array.isArray(value.th) || value.th.length !== paragraphs) {
      return fail(`${path}.th`, `must have ${paragraphs} paragraphs, as the source does`);
    }
    value.th.forEach((p, i) => line(`${path}.th[${i}]`, p, max));
  };
  const table = (
    name: "families" | "notes" | "perfumes" | "articles",
    value: unknown,
    known: ReadonlyMap<string, Obj>,
    check: (path: string, entry: Obj, source: Obj) => void,
  ): void => {
    if (!isObj(value)) return fail(name, "must be an object keyed by fixture id");
    for (const [id, entry] of Object.entries(value)) {
      const source = known.get(id);
      if (!source) {
        fail(`${name}.${id}`, "unknown fixture id");
        continue;
      }
      if (!isObj(entry)) {
        fail(`${name}.${id}`, "must be an object");
        continue;
      }
      check(`${name}.${id}`, entry, source);
    }
  };
  const byId = <T extends { readonly id: string }>(list: readonly T[]) => new Map(list.map((x) => [x.id, x as unknown as Obj]));

  if (!isObj(input)) return ["overlay: must be an object"];
  exactKeys("root", input, ["synthetic", "rights", "provenance", "families", "notes", "perfumes", "articles"]);
  if (input.synthetic !== true) fail("synthetic", "must be literal true");
  if (input.rights !== "project_owned_synthetic") fail("rights", "must be project_owned_synthetic");
  if (!isObj(input.provenance) || input.provenance.kind !== "locally_authored_fixture") {
    fail("provenance", "must be a locally authored fixture");
  }

  table("families", input.families, byId(fixtures.families), (path, entry) => {
    exactKeys(path, entry, ["descriptor"]);
    text(`${path}.descriptor`, entry.descriptor, 200);
  });
  table("notes", input.notes, byId(fixtures.notes), (path, entry) => {
    exactKeys(path, entry, ["descriptor"]);
    text(`${path}.descriptor`, entry.descriptor, 200);
  });
  table("perfumes", input.perfumes, byId(fixtures.perfumes), (path, entry, source) => {
    exactKeys(path, entry, ["description"]);
    const description = source.description as { state: string; value?: string };
    if (description.state !== "known") return fail(`${path}.description`, "source field is unknown; no text may be given");
    if (hasThai(description.value ?? "")) fail(`${path}.description`, "source is already Thai");
    text(`${path}.description`, entry.description, 600);
  });
  table("articles", input.articles, byId(fixtures.articles), (path, entry, source) => {
    exactKeys(path, entry, ["title", "excerpt", "body"]);
    text(`${path}.title`, entry.title, 120);
    text(`${path}.excerpt`, entry.excerpt, 240);
    text(`${path}.body`, entry.body, 900, (source.body as readonly string[]).length);
  });
  return errors;
}

export function assertOverlay(input: unknown, fixtures: FixtureSet): ThaiOverlay {
  const errors = validateOverlay(input, fixtures);
  if (errors.length) throw new Error(`Thai overlay rejected:\n- ${errors.join("\n- ")}`);
  return input as ThaiOverlay;
}
