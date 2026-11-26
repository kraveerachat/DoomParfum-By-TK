"use client";

import { Minus, Plus } from "lucide-react";
import Link from "next/link";
import { useRef } from "react";
import { exploreHref, filterNotes } from "@/catalogue/search";
import type { CatalogueView, NoteView } from "@/fixtures/view-model";
import { useLocale, useT } from "@/i18n/client";
import { localize, textLang } from "@/i18n/locale";
import { format, notesCount, studies, type Dictionary } from "@/i18n/messages";
import { CountStatus } from "./count-status";
import { QueryInput } from "./query-input";
import { ScriptText } from "./script-text";
import { SelectField } from "./select-field";
import { usePageState } from "./use-page-state";

const FRESH = { query: "", family: "" };

/** Group letter from the displayed name. Latin names group by Latin letter; no Thai initial is invented. */
const initialOf = (label: string) => Array.from(label)[0]?.toUpperCase() ?? "";
const groupId = (initial: string) => `notes-${initial.codePointAt(0)?.toString(16) ?? "x"}`;

function NoteRow({ note, t }: { note: NoteView; t: Dictionary }) {
  const locale = useLocale();
  const latin = locale === "th" ? "en" : undefined;
  return (
    <li className="border-divider border-t pt-4 pb-3 first:border-t-0" data-note={note.id}>
      <div className="grid gap-x-6 gap-y-1 w1024:grid-cols-[minmax(0,2fr)_minmax(0,4fr)_13rem] w1024:items-baseline">
        <h4 lang={latin} className="type-entry">
          {note.label}
        </h4>
        <p className="min-w-0">
          <span lang={textLang(note.descriptor, locale)}>{note.descriptor}</span>{" "}
          <span className="text-meta text-text-secondary block">
            {t.mock} · {note.family ? <span lang={latin}>{note.family.label}</span> : t.familyUnknown}
          </span>
        </p>
        {note.membership ? (
          <Link
            href={exploreHref({ family: null, note: note.id }, localize(locale, "/explore"))}
            prefetch={false}
            data-focus-key={`browse-${note.id}`}
            className="link-action type-control tabular-nums w1024:justify-self-end"
          >
            {format(t.notes.browse, { count: studies(t, note.membership.length) })}
            <span className="sr-only">{format(t.notes.browseWith, { note: note.label })}</span>
          </Link>
        ) : (
          <p className="text-text-secondary flex min-h-11 items-center italic w1024:justify-self-end">{t.notes.unsupplied}</p>
        )}
      </div>
      {note.membership && (
        <details className="disclosure group mt-1">
          <summary className="text-meta inline-flex min-h-11 cursor-pointer items-center gap-2 font-medium">
            <Plus aria-hidden="true" size={16} strokeWidth={1.5} className="group-open:hidden" />
            <Minus aria-hidden="true" size={16} strokeWidth={1.5} className="hidden group-open:block" />
            {format(t.notes.listed, { note: note.label })}
          </summary>
          <ul className="bg-gold-50 mt-1 mb-3 px-4 py-2">
            {note.membership.map((m) => (
              <li key={m.slug} className="flex flex-wrap items-center gap-x-4">
                <Link
                  href={localize(locale, `/perfume/${m.slug}`)}
                  prefetch={false}
                  data-focus-key={`listed-${note.id}-${m.slug}`}
                  className="link-action"
                >
                  <ScriptText>{m.name}</ScriptText>
                </Link>
                <span className="text-meta text-text-secondary">{m.places.map((p) => t.layers[p]).join(", ")}</span>
              </li>
            ))}
          </ul>
        </details>
      )}
    </li>
  );
}

export function NotesIndex({ catalogue }: { catalogue: CatalogueView }) {
  const t = useT();
  const locale = useLocale();
  const [{ query, family }, setState] = usePageState(FRESH);
  const input = useRef<HTMLInputElement>(null);
  const notes = filterNotes(catalogue.notes, query, family || null);
  const groups = Map.groupBy(notes, (n) => initialOf(n.label));
  const reset = () => {
    setState(FRESH);
    input.current?.focus();
  };

  return (
    <div className="mt-8 w1024:mt-12 w1024:grid w1024:grid-cols-12 w1024:gap-x-6">
      <div className="grid gap-5 w768:grid-cols-2 w1024:col-span-3 w1024:grid-cols-1 w1024:self-start">
        <QueryInput
          ref={input}
          label={t.notes.searchLabel}
          help={t.notes.searchHelp}
          value={query}
          onChange={(value) => setState((s) => ({ ...s, query: value }))}
        />
        <SelectField
          label={t.explore.family}
          value={family}
          options={[
            { value: "", label: t.explore.allFamilies },
            ...catalogue.families.map((f) => ({ value: f.id, label: f.label, lang: locale === "th" ? "en" : undefined })),
          ]}
          onChange={(value) => setState((s) => ({ ...s, family: value }))}
        />
      </div>
      <div className="mt-8 w1024:col-span-9 w1024:mt-0">
        <h2 tabIndex={-1} data-list-heading className="sr-only">
          {t.notes.listHeading}
        </h2>
        <div className="flex min-h-11 flex-wrap items-center justify-between gap-x-6 gap-y-2">
          <CountStatus text={notesCount(t, notes.length)} />
          {groups.size > 1 && (
            <nav aria-label={t.notes.jump}>
              <ul className="flex flex-wrap" lang="en">
                {[...groups.keys()].map((initial) => (
                  <li key={initial}>
                    <a href={`#${groupId(initial)}`} className="letter-link">
                      {initial}
                    </a>
                  </li>
                ))}
              </ul>
            </nav>
          )}
          {(query.trim() !== "" || family !== "") && notes.length > 0 && (
            <button type="button" className="link-action type-control" onClick={reset}>
              {t.notes.showAll}
            </button>
          )}
        </div>
        {notes.length === 0 ? (
          <div className="rule-section py-12" data-state="no-results">
            <p className="type-entry">{t.notes.none}</p>
            <button type="button" className="button-quiet mt-5" onClick={reset}>
              {t.notes.showAllNotes}
            </button>
          </div>
        ) : (
          <div className="mt-2 grid items-start gap-x-6 w768:grid-cols-2 w1024:grid-cols-1">
            {[...groups].map(([initial, group]) => (
              <div
                key={initial}
                className="border-control-border first:border-ink border-t w1024:grid w1024:grid-cols-[6rem_minmax(0,1fr)] w1024:items-baseline"
              >
                <h3 id={groupId(initial)} lang="en" className="note-initial pt-4">
                  {initial}
                </h3>
                <ul>
                  {group.map((note) => (
                    <NoteRow key={note.id} note={note} t={t} />
                  ))}
                </ul>
              </div>
            ))}
          </div>
        )}
      </div>
    </div>
  );
}
