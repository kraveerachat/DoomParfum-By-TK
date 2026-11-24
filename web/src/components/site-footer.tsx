import Link from "next/link";
import { Lockup } from "./site-header";

const links = [
  { href: "/about", label: "About" },
  { href: "/about#scope", label: "Mock scope" },
  { href: "/about#credits", label: "Local credits" },
] as const;

export function SiteFooter() {
  return (
    <footer className="page-container">
      <div className="wrap pt-12 w768:pt-16 w1024:pt-24">
        <div className="border-divider flex flex-col gap-8 border-t pt-8 pb-12 w768:flex-row w768:items-start w768:justify-between">
          {/* The 44px targets are centred on their text, so the first line is pulled level with the lockup. */}
          <ul className="-mt-3 flex flex-wrap gap-x-8">
            {links.map(({ href, label }) => (
              <li key={href}>
                <Link href={href} prefetch={false} data-focus-key={`footer-${href}`} className="link-action text-meta">
                  {label}
                </Link>
              </li>
            ))}
          </ul>
          <div className="w768:w-[44ch] w768:max-w-1/2">
            <p className="flex flex-col whitespace-nowrap">
              <Lockup />
            </p>
            <p className="text-meta text-text-secondary mt-4 text-balance">
              A local mock. Every fragrance, house, note and article here is fictional.
            </p>
          </div>
        </div>
      </div>
    </footer>
  );
}
