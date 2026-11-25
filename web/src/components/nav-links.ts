export const NAV_LINKS = [
  { href: "/", label: "Home" },
  { href: "/explore", label: "Explore" },
  { href: "/notes", label: "Notes" },
  { href: "/about", label: "About" },
] as const;

/** A perfume detail belongs to Explore. */
export function isCurrent(pathname: string, href: string): boolean {
  if (href === "/explore") return pathname === "/explore" || pathname.startsWith("/perfume/");
  return pathname === href;
}
