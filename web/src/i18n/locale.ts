/** Exactly two locales (DPT-PLAN-013 4.1). English keeps every V1 path; Thai lives under /th. */
export const LOCALES = ["en", "th"] as const;
export type Locale = (typeof LOCALES)[number];

export const THAI_PREFIX = "/th";

/**
 * Request header that carries the locale of the requested path to the global 404 page, which has no
 * route of its own. The proxy always overwrites it, so a value sent by the client is never read.
 */
export const LOCALE_HEADER = "x-doomparfum-locale";

export const hasThai = (text: string) => /[฀-๿]/.test(text);

/** The locale a pathname belongs to. Only the exact segment "th" is Thai; "/TH" or "/thx" are not. */
export function localeOf(pathname: string): Locale {
  return pathname === THAI_PREFIX || pathname.startsWith(`${THAI_PREFIX}/`) ? "th" : "en";
}

/** The logical path without the locale prefix: "/th/explore" is "/explore", "/th" is "/". */
export function logicalPath(pathname: string): string {
  if (localeOf(pathname) === "en") return pathname;
  const rest = pathname.slice(THAI_PREFIX.length);
  return rest === "" ? "/" : rest;
}

/**
 * Places an internal href ("/", "/explore?note=x", "/about#journal", "#purpose") in a locale.
 * A bare fragment stays on the current page and is returned unchanged.
 */
export function localize(locale: Locale, href: string): string {
  if (locale === "en" || !href.startsWith("/")) return href;
  const cut = href.search(/[?#]/);
  const path = cut === -1 ? href : href.slice(0, cut);
  const tail = cut === -1 ? "" : href.slice(cut);
  return (path === "/" ? THAI_PREFIX : `${THAI_PREFIX}${path}`) + tail;
}

/** Marks text written in the other script so it is announced and shaped correctly. */
export function textLang(text: string, page: Locale): Locale | undefined {
  const thai = hasThai(text);
  if (page === "en") return thai ? "th" : undefined;
  return thai ? undefined : "en";
}
