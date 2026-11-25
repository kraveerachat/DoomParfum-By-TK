"use client";

import { ChevronDown } from "lucide-react";
import Link from "next/link";
import { useRef } from "react";
import { countLabel, exploreHref, filterNotes } from "@/catalogue/search";
import type { CatalogueView, NoteView } from "@/fixtures/view-model";
import { CountStatus } from "./count-status";
import { QueryInput } from "./query-input";
import { ScriptText } from "./script-text";
import { SelectField } from "./select-field";
import { usePageState } from "./use-page-state";

const FRESH = { query: "", family: "" };

function NoteRow({ note }: { note: NoteView }) {
  return (
    <li className="border-divider border-t pt-4 pb-3 first:border-t-0" data-note={note.id}>
      <div className="grid gap-x-6 gap-y-1 w1024:grid-cols-[minmax(0,2fr)_minmax(0,4fr)_12rem] w1024:items-baseline">
        <h4 className="type-entry">{note.label}</h4>
        <p className="min-w-0">
          {note.descriptor}{" "}
          <span className="text-meta text-text-secondary block">
            {note.family ? `Mock · ${note.family.label}` : "Mock · Family unknown"}
          </span>
        </p>
        {note.membership ? (
          <Link
            href={exploreHref({ family: null, note: note.id })}
            prefetch={false}
            data-focus-key={`browse-${note.id}`}
            className="link-action type-control tabular-nums w1024:justify-self-end"
          >
            Browse {countLabel(note.membership.length)}
            <span className="sr-only"> with {note.label}</span>
          </Link>
        ) : (
          <p className="text-text-secondary flex min-h-11 items-center w1024:justify-self-end">Relationship not supplied</p>
        )}
      </div>
      {note.membership && (
        <details className="group mt-1">
          <summary className="text-meta inline-flex min-h-11 cursor-pointer items-center gap-2 font-medium">
            <ChevronDown
              aria-hidden="true"
              size={16}
              strokeWidth={1.5}
              className="transition-transform duration-(--motion-feedback) group-open:rotate-180"
            />
            Where {note.label} is listed
          </summary>
          <ul className="mt-1 mb-3">
            {note.membership.map((m) => (
              <li key={m.slug} className="flex flex-wrap items-center gap-x-4">
                <Link
                  href={`/perfume/${m.slug}`}
                  prefetch={false}
                  data-focus-key={`listed-${note.id}-${m.slug}`}
                  className="link-action"
                >
                  <ScriptText>{m.name}</ScriptText>
                </Link>
                <span className="text-meta text-text-secondary">{m.places.join(", ")}</span>
              </li>
            ))}
          </ul>
        </details>
      )}
    </li>
  );
}

export function NotesIndex({ catalogue }: { catalogue: CatalogueView }) {
  const [{ query, family }, setState] = usePageState(FRESH);
  const input = useRef<HTMLInputElement>(null);
  const notes = filterNotes(catalogue.notes, query, family || null);
  const groups = Map.groupBy(notes, (n) => Array.from(n.label)[0]?.toUpperCase() ?? "");
  const count = `${notes.length} mock ${notes.length === 1 ? "note" : "notes"}`;
  const reset = () => {
    setState(FRESH);
    input.current?.focus();
  };

  return (
    <div className="mt-8 w1024:mt-16 w1024:grid w1024:grid-cols-12 w1024:gap-x-6">
      <div className="grid gap-5 w768:grid-cols-2 w1024:col-span-3 w1024:grid-cols-1 w1024:self-start">
        <QueryInput
          ref={input}
          label="Search mock notes"
          help="Searches labels and descriptions."
          value={query}
          onChange={(value) => setState((s) => ({ ...s, query: value }))}
        />
        <SelectField
          label="Family"
          value={family}
          options={[
            { value: "", label: "All families" },
            ...catalogue.families.map((f) => ({ value: f.id, label: f.label })),
          ]}
          onChange={(value) => setState((s) => ({ ...s, family: value }))}
        />
      </div>
      <div className="mt-8 w1024:col-span-9 w1024:mt-0">
        <h2 tabIndex={-1} data-list-heading className="sr-only">
          Mock notes
        </h2>
        <div className="flex min-h-11 flex-wrap items-center justify-between gap-x-6">
          <CountStatus text={count} />
          {(query.trim() !== "" || family !== "") && notes.length > 0 && (
            <button type="button" className="link-action type-control" onClick={reset}>
              Show all
            </button>
          )}
        </div>
        {notes.length === 0 ? (
          <div className="border-ink border-t py-12" data-state="no-results">
            <p className="type-entry">No mock notes found</p>
            <button type="button" className="button-quiet mt-5" onClick={reset}>
              Show all notes
            </button>
          </div>
        ) : (
          <div className="grid items-start gap-x-6 w768:grid-cols-2 w1024:grid-cols-1">
            {[...groups].map(([initial, group]) => (
              <div
                key={initial}
                className="border-control-border first:border-ink border-t w1024:grid w1024:grid-cols-[6rem_minmax(0,1fr)] w1024:items-baseline"
              >
                <h3 className="type-section pt-4 leading-none">{initial}</h3>
                <ul>
                  {group.map((note) => (
                    <NoteRow key={note.id} note={note} />
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
