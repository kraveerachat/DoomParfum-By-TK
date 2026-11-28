"use client";

import { usePathname, useSearchParams } from "next/navigation";
import { useSyncExternalStore } from "react";
import { useLocale, useT } from "@/i18n/client";
import { localize, logicalPath, type Locale } from "@/i18n/locale";

export type FilterIds = { readonly families: readonly string[]; readonly notes: readonly string[] };

const FRAGMENT = /^#[A-Za-z0-9][A-Za-z0-9_-]{0,79}$/;
const subscribe = (change: () => void) => {
  window.addEventListener("hashchange", change);
  return () => window.removeEventListener("hashchange", change);
};
const readHash = () => (FRAGMENT.test(window.location.hash) ? window.location.hash : "");

/**
 * The same logical page in another language: same slug, recognized filters only, and a valid
 * fragment (DPT-PLAN-013 4.4). The fragment is added once scripting runs; the rest is server-rendered.
 */
export function useSwitchHref(filterIds: FilterIds) {
  const pathname = usePathname();
  const search = useSearchParams();
  const hash = useSyncExternalStore(subscribe, readHash, () => "");
  return (target: Locale) => {
    const logical = logicalPath(pathname);
    let query = "";
    if (logical === "/explore") {
      const kept = new URLSearchParams();
      const keep = (key: "family" | "note", pool: readonly string[]) => {
        const all = search.getAll(key);
        if (all.length === 1 && pool.includes(all[0]!)) kept.set(key, all[0]!);
      };
      keep("family", filterIds.families);
      keep("note", filterIds.notes);
      query = kept.size ? `?${kept.toString()}` : "";
    }
    return localize(target, logical) + query + hash;
  };
}

const ORDER: readonly Locale[] = ["th", "en"];

/** Both languages: the current one marked, the other a link. A document navigation, never a toggle. */
export function LanguageLinks({ filterIds, className = "", size = "short" }: { filterIds: FilterIds; className?: string; size?: "short" | "full" }) {
  const locale = useLocale();
  const t = useT();
  const href = useSwitchHref(filterIds);
  const label = (l: Locale) => ({
    short: l === "th" ? t.language.thShort : t.language.enShort,
    name: l === "th" ? t.language.thName : t.language.enName,
  });
  return (
    <div role="group" aria-label={t.language.group} className={className}>
    <ul className="flex items-center">
      {ORDER.map((l) => {
        const { short, name } = label(l);
        const shown = size === "short" ? short : name;
        const hidden = size === "short" ? <span className="sr-only" lang={l}> {name}</span> : null;
        return (
          <li key={l}>
            {l === locale ? (
              <span
                aria-current="true"
                lang={size === "full" ? l : undefined}
                className="lang-item lang-current"
              >
                <span className="lang-label">{shown}</span>
                {hidden}
              </span>
            ) : (
              <a
                href={href(l)}
                hrefLang={l}
                lang={size === "full" ? l : undefined}
                data-document-nav
                data-focus-key={`lang-${l}`}
                className="lang-item lang-link"
              >
                <span className="lang-label">{shown}</span>
                {hidden}
              </a>
            )}
          </li>
        );
      })}
    </ul>
    </div>
  );
}

/** One 44px link to the other language, for narrow headers. */
export function LanguageSwitch({ filterIds }: { filterIds: FilterIds }) {
  const locale = useLocale();
  const t = useT();
  const href = useSwitchHref(filterIds);
  const other: Locale = locale === "th" ? "en" : "th";
  return (
    <a
      href={href(other)}
      hrefLang={other}
      data-document-nav
      data-focus-key={`lang-${other}`}
      className="icon-button lang-switch"
    >
      <span className="lang-label">{other === "th" ? t.language.thShort : t.language.enShort}</span>
      <span className="sr-only" lang={other}>
        {" "}
        {other === "th" ? t.language.thName : t.language.enName}
      </span>
    </a>
  );
}
