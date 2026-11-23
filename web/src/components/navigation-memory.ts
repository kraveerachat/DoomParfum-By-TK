/**
 * Same-tab navigation memory. Values live in module memory only: nothing is written to
 * browser storage, and a hard reload clears everything. Mutated from events and effects only.
 */
type NavigationKind = "push" | "pop" | null;
type Departure = { readonly focusKey: string | null; readonly scrollY: number };

let kind: NavigationKind = null;
const pageStates = new Map<string, unknown>();
const departures = new Map<string, Departure>();

export const locationKey = () => window.location.pathname + window.location.search;

/** Identifies the history entry, so two visits to one URL stay separate. Falls back to the URL. */
export function entryKey(): string {
  const api = (window as { navigation?: { currentEntry?: { key?: string } | null } }).navigation;
  return api?.currentEntry?.key ?? locationKey();
}

/** What has focus now, named so that it can be found again. */
export function currentFocusKey(): string | null {
  return document.activeElement?.closest<HTMLElement>("[data-focus-key]")?.dataset.focusKey ?? null;
}

export const navigation = {
  kind: () => kind,
  set: (next: NavigationKind) => {
    kind = next;
  },
  depart: (key: string, departure: Departure) => {
    departures.set(key, departure);
  },
  departure: (key: string) => departures.get(key) ?? null,
  savePage: (key: string, state: unknown) => {
    pageStates.set(key, state);
  },
  /** Typed text and open filters return only through Back or Forward, never on a fresh visit. */
  restorePage: <T>(initial: T): T => {
    if (typeof window === "undefined" || kind !== "pop") return initial;
    return (pageStates.get(entryKey()) as T | undefined) ?? initial;
  },
};
