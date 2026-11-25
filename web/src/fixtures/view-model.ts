import type { Field, FixtureSet } from "./types.ts";

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
};
export type Membership = { readonly slug: string; readonly name: string; readonly places: readonly string[] };
export type NoteView = {
  readonly id: string;
  readonly label: string;
  readonly descriptor: string;
  readonly family: LabelRef | null;
  /** null means the relationship was not supplied; it is never shown as zero. */
  readonly membership: readonly Membership[] | null;
};
export type FamilyView = LabelRef & { readonly descriptor: string; readonly count: number };
export type CatalogueView = {
  readonly entries: readonly Entry[];
  readonly families: readonly FamilyView[];
  readonly notes: readonly NoteView[];
};

const values = (f: Field<readonly string[]>) => (f.state === "known" ? f.value : []);
const PLACES = [
  ["top", "Top"],
  ["heart", "Heart"],
  ["base", "Base"],
  ["generalNotes", "General notes"],
] as const;

export function buildCatalogue(set: FixtureSet): CatalogueView {
  const family = new Map(set.families.map((f) => [f.id, { id: f.id, label: f.label }]));
  const lookup = (f: Field<string>): LabelRef | null => (f.state === "known" ? (family.get(f.value) ?? null) : null);

  const entries = set.perfumes.map((p): Entry => ({
    id: p.id,
    slug: p.slug,
    name: p.name,
    house: p.houseLabel,
    description: p.description.state === "known" ? p.description.value : null,
    family: lookup(p.family),
    noteIds: [...new Set(PLACES.flatMap(([key]) => values(p[key])))],
    visual: p.visual.state === "known" ? p.visual.value : null,
  }));

  const notes = set.notes.map((note): NoteView => {
    const membership = set.perfumes.flatMap((p): Membership[] => {
      const places = PLACES.filter(([key]) => values(p[key]).includes(note.id)).map(([, label]) => label);
      return places.length ? [{ slug: p.slug, name: p.name, places }] : [];
    });
    return {
      id: note.id,
      label: note.label,
      descriptor: note.descriptor,
      family: lookup(note.family),
      // Some records have unknown layers, so "no membership found" cannot be reported as zero.
      membership: membership.length ? membership : null,
    };
  });

  return {
    entries,
    notes,
    families: set.families.map((f) => ({
      id: f.id,
      label: f.label,
      descriptor: f.descriptor,
      count: entries.filter((e) => e.family?.id === f.id).length,
    })),
  };
}
