"use client";

import { ChevronDown, X } from "lucide-react";
import Link from "next/link";
import { useSearchParams } from "next/navigation";
import { useEffect, useMemo, useRef } from "react";
import { exploreHref, filterEntries, parseQuery, type Filters, type SortKey } from "@/catalogue/search";
import { useLocale, useT } from "@/i18n/client";
import { localize } from "@/i18n/locale";
import { format, studies } from "@/i18n/messages";
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

function replaceUrl(href: string) {
  // A filter change is not a navigation: it must not move focus or request the server.
  navigation.set(null);
  window.history.replaceState(null, "", href);
}

export function ExploreCatalogue({ catalogue }: { catalogue: CatalogueView }) {
  const t = useT();
  const locale = useLocale();
  const base = localize(locale, "/explore");
  const latin = locale === "th" ? "en" : undefined;
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
    const timer = setTimeout(() => replaceUrl(rest ? `${base}?${rest}` : base), 0);
    return () => clearTimeout(timer);
  }, [unsupported, search, base]);

  const results = invalid ? [] : filterEntries(catalogue.entries, query, filters, sort);
  const family = catalogue.families.find((f) => f.id === filters.family);
  const note = catalogue.notes.find((n) => n.id === filters.note);
  const narrowed = query.trim() !== "" || filters.family !== null || filters.note !== null || sort !== FRESH.sort || invalid;
  // A note whose relationships were never supplied is not a note with zero studies.
  const unsupplied = !invalid && note !== undefined && note.membership === null;

  const setFilters = (next: Filters) => replaceUrl(exploreHref(next, base));
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
        <p className="type-entry">{t.explore.noData}</p>
        <Link href={localize(locale, "/about")} prefetch={false} className="link-action mt-3">
          {t.explore.noDataLink}
        </Link>
      </div>
    );
  }

  return (
    <div className="mt-5">
      <QueryInput
        ref={input}
        label={t.explore.searchLabel}
        help={t.explore.searchHelp}
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
        {t.explore.filterToggle}
        <ChevronDown
          aria-hidden="true"
          size={20}
          strokeWidth={1.5}
          className={`transition-transform duration-(--motion-feedback) ${filtersOpen ? "rotate-180" : ""}`}
        />
      </button>
      <div
        id="explore-filters"
        className={`${filtersOpen ? "grid" : "hidden"} mt-4 grid-cols-1 gap-4 w640:mt-3 w640:grid w640:grid-cols-2 w640:gap-x-6 w640:gap-y-3 w1024:grid-cols-3`}
      >
        <SelectField
          inline
          ref={familySelect}
          label={t.explore.family}
          value={invalid ? "" : (filters.family ?? "")}
          options={[
            { value: "", label: t.explore.allFamilies },
            ...catalogue.families.map((f) => ({ value: f.id, label: f.label, lang: latin })),
          ]}
          onChange={(value) => setFilters({ ...filters, family: value || null })}
        />
        <SelectField
          inline
          ref={noteSelect}
          label={t.explore.note}
          value={invalid ? "" : (filters.note ?? "")}
          options={[
            { value: "", label: t.explore.allNotes },
            ...[...catalogue.notes]
              .sort((a, b) => a.label.localeCompare(b.label, "en"))
              .map((n) => ({ value: n.id, label: n.label, lang: latin })),
          ]}
          onChange={(value) => setFilters({ ...filters, note: value || null })}
        />
        <SelectField
          inline
          label={t.explore.sort}
          value={sort}
          options={[
            { value: "name-asc", label: t.explore.sortAsc },
            { value: "name-desc", label: t.explore.sortDesc },
          ]}
          onChange={(value) => setState((s) => ({ ...s, sort: value === "name-desc" ? "name-desc" : "name-asc" }))}
        />
      </div>

      <div className="rule-section mt-5 flex min-h-12 flex-wrap items-center gap-x-6 gap-y-2 pt-2">
        <h2 tabIndex={-1} data-list-heading className="sr-only">
          {t.explore.listHeading}
        </h2>
        <CountStatus text={invalid ? t.explore.filterUnavailable : unsupplied ? t.explore.unsuppliedCount : studies(t, results.length)} />
        {(family || note) && (
          <ul className="flex flex-wrap gap-2" aria-label={t.explore.activeFilters}>
            {family && (
              <li>
                <button type="button" className="button-quiet filter-chip text-meta" onClick={() => remove("family")}>
                  <span lang={latin}>{family.label}</span>
                  <X aria-hidden="true" size={16} strokeWidth={1.5} />
                  <span className="sr-only">{t.explore.removeFamily}</span>
                </button>
              </li>
            )}
            {note && (
              <li>
                <button type="button" className="button-quiet filter-chip text-meta" onClick={() => remove("note")}>
                  <span lang={latin}>{note.label}</span>
                  <X aria-hidden="true" size={16} strokeWidth={1.5} />
                  <span className="sr-only">{t.explore.removeNote}</span>
                </button>
              </li>
            )}
          </ul>
        )}
        {narrowed && !invalid && results.length > 0 && (
          <button type="button" className="link-action type-control ms-auto" onClick={clearAll}>
            {t.explore.clearAll}
          </button>
        )}
      </div>

      {invalid ? (
        <div className="py-12" data-state="invalid-filter">
          <p className="type-entry">{t.explore.invalidTitle}</p>
          <p className="text-text-secondary mt-2 max-w-[52ch]">{t.explore.invalidText}</p>
          <button type="button" className="button-quiet mt-5" onClick={clearAll}>
            {t.explore.resetFilters}
          </button>
        </div>
      ) : unsupplied ? (
        <div className="py-12" data-state="unsupplied">
          <p className="type-entry">{format(t.explore.unsuppliedTitle, { note: note.label })}</p>
          <p className="text-text-secondary mt-2 max-w-[52ch]">{t.explore.unsuppliedText}</p>
          <button type="button" className="button-quiet mt-5" onClick={clearAll}>
            {t.explore.clearFilters}
          </button>
        </div>
      ) : results.length === 0 ? (
        <div className="py-12" data-state="no-results">
          <p className="type-entry">{t.explore.noResults}</p>
          <p className="text-text-secondary mt-2 max-w-[52ch]">{t.explore.noResultsText}</p>
          <button type="button" className="button-quiet mt-5" onClick={clearAll}>
            {t.explore.clearFilters}
          </button>
        </div>
      ) : (
        <ul className="entry-grid mt-4 grid grid-cols-1 gap-x-4 gap-y-12 w480:grid-cols-2 w640:gap-x-5 w768:gap-x-6 w1024:grid-cols-3 w1024:gap-y-16 w1280:grid-cols-4">
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
