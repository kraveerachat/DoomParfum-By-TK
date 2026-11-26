import { logicalPath } from "@/i18n/locale";

/** Logical paths; components place them in the current locale. */
export const NAV_LINKS = [
  { href: "/", key: "home" },
  { href: "/explore", key: "explore" },
  { href: "/notes", key: "notes" },
  { href: "/about", key: "about" },
] as const;

/** A perfume detail belongs to Explore. Works for both locales. */
export function isCurrent(pathname: string, href: string): boolean {
  const path = logicalPath(pathname);
  if (href === "/explore") return path === "/explore" || path.startsWith("/perfume/");
  return path === href;
}
