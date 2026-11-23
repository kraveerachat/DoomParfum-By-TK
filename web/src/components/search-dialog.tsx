"use client";

import Link from "next/link";
import { useEffect, useRef, useState } from "react";
import { countLabel, filterEntries } from "@/catalogue/search";
import type { Entry } from "@/fixtures/view-model";
import { keepFocus, type OverlayDialogProps } from "./menu-dialog";
import { QueryInput } from "./query-input";
import { ScriptText } from "./script-text";
import { CountStatus } from "./count-status";
import { Dialog, DialogDescription, DialogHeader, DialogPanel, DialogTitle } from "./ui/dialog";

const NO_FILTERS = { family: null, note: null } as const;

/** Keeps the panel inside the visual viewport while a virtual keyboard is open. */
function useVisualViewport(active: boolean) {
  useEffect(() => {
    const viewport = window.visualViewport;
    if (!active || !viewport) return;
    const root = document.documentElement;
    const update = () => {
      root.style.setProperty("--vv-height", `${viewport.height}px`);
      root.style.setProperty("--vv-top", `${viewport.offsetTop}px`);
    };
    update();
    viewport.addEventListener("resize", update);
    viewport.addEventListener("scroll", update);
    return () => {
      viewport.removeEventListener("resize", update);
      viewport.removeEventListener("scroll", update);
      root.style.removeProperty("--vv-height");
      root.style.removeProperty("--vv-top");
    };
  }, [active]);
}

function SearchBody({ entries, onNavigate }: { entries: readonly Entry[]; onNavigate: () => void }) {
  const [query, setQuery] = useState("");
  const input = useRef<HTMLInputElement>(null);
  const results = filterEntries(entries, query, NO_FILTERS);

  return (
    <>
      <div className="border-divider flex-none border-b px-4 pb-4">
        <QueryInput ref={input} label="Search mock catalogue" help="Fictional studies only" value={query} onChange={setQuery} />
      </div>
      <div className="min-h-0 flex-1 overflow-y-auto overscroll-contain px-4 pt-3 pb-6">
        <CountStatus text={countLabel(results.length)} className="text-meta text-text-secondary" />
        {results.length === 0 ? (
          <div className="py-8">
            <p className="type-entry">No mock fragrances found</p>
            <button
              type="button"
              className="button-quiet mt-4"
              onClick={() => {
                setQuery("");
                input.current?.focus();
              }}
            >
              Clear search
            </button>
          </div>
        ) : (
          <ul className="mt-2">
            {results.map((entry) => (
              <li key={entry.id} className="border-divider border-b" data-focus-key="search-trigger">
                <Link
                  href={`/perfume/${entry.slug}`}
                  prefetch={false}
                  onClick={onNavigate}
                  className="can-hover:bg-surface-muted -mx-2 flex min-h-14 flex-wrap items-baseline justify-between gap-x-6 px-2 py-3"
                >
                  <ScriptText className="font-medium">{entry.name}</ScriptText>
                  <span className="text-meta text-text-secondary">Mock · {entry.family?.label ?? "Family unknown"}</span>
                </Link>
              </li>
            ))}
          </ul>
        )}
      </div>
    </>
  );
}

export function SearchDialog({ open, onClose, onNavigate, entries }: OverlayDialogProps & { entries: readonly Entry[] }) {
  useVisualViewport(open);
  return (
    <Dialog open={open} onOpenChange={(next) => !next && onClose()}>
      <DialogPanel
        className="panel panel-search"
        data-panel
        onCloseAutoFocus={keepFocus}
        onOpenAutoFocus={(event) => {
          event.preventDefault();
          (event.currentTarget as HTMLElement).querySelector<HTMLElement>("input")?.focus();
        }}
      >
        <DialogHeader>
          <DialogTitle className="text-control font-medium">Search</DialogTitle>
        </DialogHeader>
        <DialogDescription className="sr-only">
          Results update as you type and cover fictional studies only.
        </DialogDescription>
        <SearchBody entries={entries} onNavigate={onNavigate} />
      </DialogPanel>
    </Dialog>
  );
}
