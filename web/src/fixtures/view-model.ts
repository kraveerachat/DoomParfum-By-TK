import type { ArticleFixture, Field, FixtureSet, OverlayText, ThaiOverlay } from "./types.ts";

export type ViewLocale = "en" | "th";

export type LabelRef = { readonly id: string; readonly label: string };
export type Entry = {
  readonly id: string;
  readonly slug: string;
  readonly name: string;
  readonly house: string;
  readonly description: string | null;
  readonly family: LabelRef | null;
  /** Explicit memberships only: top, heart, base and generalNotes lists that are known. */
  readonly noteIds: readonly string[];
  readonly visual: string | null;
  /** Further searchable text (DPT-PLAN-013 4.5): the other language's representation. */
  readonly extra: readonly string[];
  /** On English pages, Thai text joins the search only for a query that contains Thai. */
  readonly extraNeedsThai: boolean;
};
export type Place = "top" | "heart" | "base" | "generalNotes";
export type Membership = { readonly slug: string; readonly name: string; readonly places: readonly Place[] };
export type NoteView = {
  readonly id: string;
  readonly label: string;
  readonly descriptor: string;
  readonly family: LabelRef | null;
  /** null means the relationship was not supplied; it is never shown as zero. */
  readonly membership: readonly Membership[] | null;
  readonly extra: readonly string[];
  readonly extraNeedsThai: boolean;
};
export type ArticleView = Pick<ArticleFixture, "id" | "anchor"> & {
  readonly title: string;
  readonly excerpt: string;
  readonly body: readonly string[];
};
export type FamilyView = LabelRef & { readonly descriptor: string; readonly count: number };
export type CatalogueView = {
  readonly entries: readonly Entry[];
  readonly families: readonly FamilyView[];
  readonly notes: readonly NoteView[];
};

const values = (f: Field<readonly string[]>) => (f.state === "known" ? f.value : []);
const PLACES = ["top", "heart", "base", "generalNotes"] as const;

/**
 * Text for a locale. English pages show the English source; Thai pages show the overlay where it
 * exists, else the English source. Search gets the other representation: on Thai pages the English
 * source; on English pages only reviewed Thai text, and only for a query containing Thai.
 */
function pick(source: string, overlay: OverlayText | undefined, locale: ViewLocale) {
  if (!overlay) return { shown: source, extra: [] as string[] };
  if (locale === "th") return { shown: overlay.th, extra: [source] };
  return { shown: source, extra: overlay.review === "reviewed" ? [overlay.th] : [] };
}

export function buildCatalogue(set: FixtureSet, locale: ViewLocale = "en", overlay?: ThaiOverlay): CatalogueView {
  const family = new Map(set.families.map((f) => [f.id, { id: f.id, label: f.label }]));
  const lookup = (f: Field<string>): LabelRef | null => (f.state === "known" ? (family.get(f.value) ?? null) : null);

  const entries = set.perfumes.map((p): Entry => {
    const text = p.description.state === "known" ? pick(p.description.value, overlay?.perfumes[p.id]?.description, locale) : null;
    return {
      id: p.id,
      slug: p.slug,
      name: p.name,
      house: p.houseLabel,
      description: text?.shown ?? null,
      family: lookup(p.family),
      noteIds: [...new Set(PLACES.flatMap((key) => values(p[key])))],
      visual: p.visual.state === "known" ? p.visual.value : null,
      extra: text?.extra ?? [],
      extraNeedsThai: locale === "en",
    };
  });

  const notes = set.notes.map((note): NoteView => {
    const membership = set.perfumes.flatMap((p): Membership[] => {
      const places = PLACES.filter((key) => values(p[key]).includes(note.id));
      return places.length ? [{ slug: p.slug, name: p.name, places }] : [];
    });
    const text = pick(note.descriptor, overlay?.notes[note.id]?.descriptor, locale);
    return {
      id: note.id,
      label: note.label,
      descriptor: text.shown,
      family: lookup(note.family),
      // Some records have unknown layers, so "no membership found" cannot be reported as zero.
      membership: membership.length ? membership : null,
      extra: text.extra,
      extraNeedsThai: locale === "en",
    };
  });

  return {
    entries,
    notes,
    families: set.families.map((f) => ({
      id: f.id,
      label: f.label,
      descriptor: pick(f.descriptor, overlay?.families[f.id]?.descriptor, locale).shown,
      count: entries.filter((e) => e.family?.id === f.id).length,
    })),
  };
}

export function buildArticles(set: FixtureSet, locale: ViewLocale = "en", overlay?: ThaiOverlay): ArticleView[] {
  return set.articles.map((a) => {
    const o = locale === "th" ? overlay?.articles[a.id] : undefined;
    return {
      id: a.id,
      anchor: a.anchor,
      title: o?.title.th ?? a.title,
      excerpt: o?.excerpt.th ?? a.excerpt,
      body: o?.body.th ?? a.body,
    };
  });
}
