/** Pure, shared search and filter semantics. No ranking, scoring or regular expressions built from input. */
import type { Entry, NoteView } from "../fixtures/view-model.ts";

export const QUERY_LIMIT = 120;
export type SortKey = "name-asc" | "name-desc";
export type Filters = { readonly family: string | null; readonly note: string | null };

export const clipQuery = (raw: string) => Array.from(raw).slice(0, QUERY_LIMIT).join("");
export const fold = (text: string) => text.normalize("NFKC").toLowerCase();

export function matchesText(query: string, fields: readonly (string | null)[]): boolean {
  const needle = fold(clipQuery(query).trim());
  return needle === "" || fields.some((f) => f !== null && fold(f).includes(needle));
}

const thaiQuery = (query: string) => /[฀-๿]/.test(query);

/** Extra representations join only where DPT-PLAN-013 4.5 allows, so English results never change. */
const withExtra = (query: string, x: { readonly extra: readonly string[]; readonly extraNeedsThai: boolean }) =>
  x.extraNeedsThai && !thaiQuery(query) ? [] : x.extra;

export const matchesQuery = (e: Entry, query: string) =>
  matchesText(query, [e.name, e.house, e.description, ...withExtra(query, e)]);

const collator = new Intl.Collator(["en", "th"], { sensitivity: "base", numeric: true });
const byId = (a: { id: string }, b: { id: string }) => (a.id < b.id ? -1 : a.id > b.id ? 1 : 0);

export function sortEntries(entries: readonly Entry[], sort: SortKey): Entry[] {
  const direction = sort === "name-desc" ? -1 : 1;
  return [...entries].sort((a, b) => direction * collator.compare(a.name, b.name) || byId(a, b));
}

export function filterEntries(
  entries: readonly Entry[],
  query: string,
  filters: Filters,
  sort: SortKey = "name-asc",
): Entry[] {
  const kept = entries.filter(
    (e) =>
      matchesQuery(e, query) &&
      (filters.family === null || e.family?.id === filters.family) &&
      (filters.note === null || e.noteIds.includes(filters.note)),
  );
  return sortEntries(kept, sort);
}

export function filterNotes(notes: readonly NoteView[], query: string, family: string | null): NoteView[] {
  return notes
    .filter((n) => matchesText(query, [n.label, n.descriptor, ...withExtra(query, n)]) && (family === null || n.family?.id === family))
    .sort((a, b) => collator.compare(a.label, b.label) || byId(a, b));
}

export type ParsedQuery = { readonly filters: Filters; readonly invalid: boolean; readonly unsupported: boolean };

export function parseQuery(
  params: URLSearchParams,
  allowed: { readonly families: ReadonlySet<string>; readonly notes: ReadonlySet<string> },
): ParsedQuery {
  let invalid = false;
  const read = (key: "family" | "note", pool: ReadonlySet<string>): string | null => {
    const all = params.getAll(key);
    const only = all[0];
    if (only === undefined) return null;
    if (all.length > 1 || !pool.has(only)) {
      invalid = true;
      return null;
    }
    return only;
  };
  const filters = { family: read("family", allowed.families), note: read("note", allowed.notes) };
  const unsupported = [...params.keys()].some((k) => k !== "family" && k !== "note");
  return { filters, invalid, unsupported };
}

export function exploreHref(filters: Filters, base = "/explore"): string {
  const params = new URLSearchParams();
  if (filters.family) params.set("family", filters.family);
  if (filters.note) params.set("note", filters.note);
  const query = params.toString();
  return query ? `${base}?${query}` : base;
}

export const countLabel = (count: number) => `${count} mock ${count === 1 ? "study" : "studies"}`;
export const isThai = (text: string) => /[฀-๿]/.test(text);
