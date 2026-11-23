"use client";

import { ChevronDown, X } from "lucide-react";
import Link from "next/link";
import { useSearchParams } from "next/navigation";
import { useEffect, useMemo, useRef } from "react";
import { countLabel, exploreHref, filterEntries, parseQuery, type Filters, type SortKey } from "@/catalogue/search";
import type { CatalogueView } from "@/fixtures/view-model";
import { CountStatus } from "./count-status";
import { navigation } from "./navigation-memory";
import { PerfumeEntry } from "./perfume-entry";
import { QueryInput } from "./query-input";
import { SelectField } from "./select-field";
import { usePageState } from "./use-page-state";

type ExploreState = { readonly query: string; readonly sort: SortKey; readonly filtersOpen: boolean };
const FRESH: ExploreState = { query: "", sort: "name-asc", filtersOpen: false };
const NONE: Filters = { family: null, note: null };
const SORTS = [
  { value: "name-asc", label: "Name A–Z" },
  { value: "name-desc", label: "Name Z–A" },
] as const;

function replaceUrl(href: string) {
  // A filter change is not a navigation: it must not move focus or request the server.
  navigation.set(null);
  window.history.replaceState(null, "", href);
}

export function ExploreCatalogue({ catalogue }: { catalogue: CatalogueView }) {
  const params = useSearchParams();
  const search = params.toString();
  const allowed = useMemo(
    () => ({
      families: new Set(catalogue.families.map((f) => f.id)),
      notes: new Set(catalogue.notes.map((n) => n.id)),
    }),
    [catalogue],
  );
  const { filters, invalid, unsupported } = useMemo(
    () => parseQuery(new URLSearchParams(search), allowed),
    [search, allowed],
  );

  const [{ query, sort, filtersOpen }, setState] = usePageState(FRESH);
  const input = useRef<HTMLInputElement>(null);
  const disclosure = useRef<HTMLButtonElement>(null);
  const familySelect = useRef<HTMLSelectElement>(null);
  const noteSelect = useRef<HTMLSelectElement>(null);

  // Unsupported keys are dropped. Recognised keys stay, including an unavailable value that
  // the page still has to explain.
  useEffect(() => {
    if (!unsupported) return;
    const kept = new URLSearchParams();
    for (const [key, value] of new URLSearchParams(search)) {
      if (key === "family" || key === "note") kept.append(key, value);
    }
    const rest = kept.toString();
    // Deferred so that the router's own history patch is already installed.
    const timer = setTimeout(() => replaceUrl(rest ? `/explore?${rest}` : "/explore"), 0);
    return () => clearTimeout(timer);
  }, [unsupported, search]);

  const results = invalid ? [] : filterEntries(catalogue.entries, query, filters, sort);
  const family = catalogue.families.find((f) => f.id === filters.family);
  const note = catalogue.notes.find((n) => n.id === filters.note);
  const narrowed = query.trim() !== "" || filters.family !== null || filters.note !== null || sort !== FRESH.sort || invalid;
  // A note whose relationships were never supplied is not a note with zero studies.
  const unsupplied = !invalid && note !== undefined && note.membership === null;

  const setFilters = (next: Filters) => replaceUrl(exploreHref(next));
  const visible = (el: HTMLElement | null) => (el && el.getClientRects().length > 0 ? el : null);
  const clearAll = () => {
    setState((s) => ({ ...s, query: FRESH.query, sort: FRESH.sort }));
    setFilters(NONE);
    input.current?.focus();
  };
  const remove = (key: "family" | "note") => {
    setFilters({ ...filters, [key]: null });
    const select = key === "family" ? familySelect.current : noteSelect.current;
    (visible(select) ?? disclosure.current)?.focus();
  };

  if (catalogue.entries.length === 0) {
    return (
      <div className="border-ink mt-10 border-t py-12">
        <p className="type-entry">No mock studies are available</p>
        <Link href="/about" prefetch={false} className="link-action mt-3">
          About this mock
        </Link>
      </div>
    );
  }

  return (
    <div className="mt-8 w1024:mt-12">
      <QueryInput
        ref={input}
        label="Search mock catalogue"
        help="Searches the names, house and descriptions of fictional studies."
        value={query}
        onChange={(value) => setState((s) => ({ ...s, query: value }))}
      />

      <button
        ref={disclosure}
        type="button"
        className="button-quiet mt-5 w640:hidden"
        aria-expanded={filtersOpen}
        aria-controls="explore-filters"
        onClick={() => setState((s) => ({ ...s, filtersOpen: !s.filtersOpen }))}
      >
        Filter and sort
        <ChevronDown
          aria-hidden="true"
          size={20}
          strokeWidth={1.5}
          className={`transition-transform duration-(--motion-feedback) ${filtersOpen ? "rotate-180" : ""}`}
        />
      </button>
      <div
        id="explore-filters"
        className={`${filtersOpen ? "grid" : "hidden"} mt-4 grid-cols-1 gap-4 w640:mt-5 w640:grid w640:grid-cols-2 w1024:grid-cols-3 w1024:gap-6`}
      >
        <SelectField
          ref={familySelect}
          label="Family"
          value={invalid ? "" : (filters.family ?? "")}
          options={[
            { value: "", label: "All families" },
            ...catalogue.families.map((f) => ({ value: f.id, label: f.label })),
          ]}
          onChange={(value) => setFilters({ ...filters, family: value || null })}
        />
        <SelectField
          ref={noteSelect}
          label="Note"
          value={invalid ? "" : (filters.note ?? "")}
          options={[
            { value: "", label: "All notes" },
            ...[...catalogue.notes]
              .sort((a, b) => a.label.localeCompare(b.label, "en"))
              .map((n) => ({ value: n.id, label: n.label })),
          ]}
          onChange={(value) => setFilters({ ...filters, note: value || null })}
        />
        <SelectField
          label="Sort"
          value={sort}
          options={SORTS}
          onChange={(value) => setState((s) => ({ ...s, sort: value === "name-desc" ? "name-desc" : "name-asc" }))}
        />
      </div>

      <div className="border-ink mt-8 flex min-h-16 flex-wrap items-center gap-x-6 gap-y-2 border-t pt-3">
        <h2 tabIndex={-1} data-list-heading className="sr-only">
          Mock studies
        </h2>
        <CountStatus text={unsupplied ? "Relationship not supplied" : countLabel(results.length)} />
        {(family || note) && (
          <ul className="flex flex-wrap gap-2" aria-label="Active filters">
            {family && (
              <li>
                <button type="button" className="button-quiet text-meta" onClick={() => remove("family")}>
                  {family.label}
                  <X aria-hidden="true" size={16} strokeWidth={1.5} />
                  <span className="sr-only">, remove family filter</span>
                </button>
              </li>
            )}
            {note && (
              <li>
                <button type="button" className="button-quiet text-meta" onClick={() => remove("note")}>
                  {note.label}
                  <X aria-hidden="true" size={16} strokeWidth={1.5} />
                  <span className="sr-only">, remove note filter</span>
                </button>
              </li>
            )}
          </ul>
        )}
        {narrowed && !invalid && results.length > 0 && (
          <button type="button" className="link-action ms-auto" onClick={clearAll}>
            Clear all
          </button>
        )}
      </div>

      {invalid ? (
        <div className="py-12" data-state="invalid-filter">
          <p className="type-entry">This filter is unavailable</p>
          <p className="text-text-secondary mt-2 max-w-[52ch]">
            The link asks for a family or note that does not exist in this mock.
          </p>
          <button type="button" className="button-quiet mt-5" onClick={clearAll}>
            Reset filters
          </button>
        </div>
      ) : unsupplied ? (
        <div className="py-12" data-state="unsupplied">
          <p className="type-entry">Relationship not supplied for {note.label} in this mock</p>
          <p className="text-text-secondary mt-2 max-w-[52ch]">
            No study lists it, and some studies have layers that were never supplied.
          </p>
          <button type="button" className="button-quiet mt-5" onClick={clearAll}>
            Clear filters
          </button>
        </div>
      ) : results.length === 0 ? (
        <div className="py-12" data-state="no-results">
          <p className="type-entry">No mock studies fit these filters.</p>
          <p className="text-text-secondary mt-2 max-w-[52ch]">
            A study matches a note only when the note is written in one of its lists.
          </p>
          <button type="button" className="button-quiet mt-5" onClick={clearAll}>
            Clear filters
          </button>
        </div>
      ) : (
        <ul className="mt-4 grid grid-cols-1 gap-x-4 gap-y-12 w480:grid-cols-2 w640:gap-x-5 w768:gap-x-6 w1024:grid-cols-3 w1024:gap-y-16 w1280:grid-cols-4">
          {results.map((entry, i) => (
            <li key={entry.id} className="min-w-0">
              <PerfumeEntry entry={entry} eager={i < 4} />
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}
