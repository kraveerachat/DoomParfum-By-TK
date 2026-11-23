import Link from "next/link";

const links = [
  { href: "/about", label: "About" },
  { href: "/about#scope", label: "Mock scope" },
  { href: "/about#credits", label: "Local credits" },
] as const;

export function SiteFooter() {
  return (
    <footer className="page-container">
      <div className="wrap pt-16 w1024:pt-32">
        <div className="border-divider flex flex-col gap-6 border-t pt-8 pb-12 w768:flex-row w768:items-start w768:justify-between">
          <ul className="flex flex-wrap gap-x-8">
            {links.map(({ href, label }) => (
              <li key={href}>
                <Link href={href} prefetch={false} data-focus-key={`footer-${href}`} className="link-action text-meta">
                  {label}
                </Link>
              </li>
            ))}
          </ul>
          <p className="text-meta text-text-secondary max-w-[44ch]">
            <span className="text-ink font-medium">DoomParfum By TK.</span> A local mock. Every fragrance, house, note
            and article here is fictional.
          </p>
        </div>
      </div>
    </footer>
  );
}
