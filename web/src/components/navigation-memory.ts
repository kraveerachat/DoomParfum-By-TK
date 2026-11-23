/**
 * Same-tab navigation memory. Values live in module memory only: nothing is written to
 * browser storage, and a hard reload clears everything. Mutated from events and effects only.
 */
import type { SortKey } from "@/catalogue/search";

type NavigationKind = "push" | "pop" | null;
export type ExploreState = { readonly query: string; readonly sort: SortKey };
type Departure = { readonly focusKey: string | null; readonly scrollY: number };

let kind: NavigationKind = null;
const exploreStates = new Map<string, ExploreState>();
const departures = new Map<string, Departure>();

export const locationKey = () => window.location.pathname + window.location.search;

export const navigation = {
  kind: () => kind,
  set: (next: NavigationKind) => {
    kind = next;
  },
  depart: (key: string, departure: Departure) => {
    departures.set(key, departure);
  },
  departure: (key: string) => departures.get(key) ?? null,
  saveExplore: (key: string, state: ExploreState) => {
    exploreStates.set(key, state);
  },
  /** Typed search returns only through Back or Forward, never on a fresh visit. */
  restoreExplore: (key: string): ExploreState | null => (kind === "pop" ? (exploreStates.get(key) ?? null) : null),
};
