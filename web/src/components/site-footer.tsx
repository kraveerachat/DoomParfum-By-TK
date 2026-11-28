"use client";

import Link from "next/link";
import { useLocale, useT } from "@/i18n/client";
import { localize } from "@/i18n/locale";
import { LanguageLinks, type FilterIds } from "./language-links";
import { Lockup } from "./site-header";

export function SiteFooter({ filterIds }: { filterIds: FilterIds }) {
  const locale = useLocale();
  const t = useT();
  const links = [
    { href: "/about", label: t.footer.about },
    { href: "/about#scope", label: t.footer.scope },
    { href: "/about#credits", label: t.footer.credits },
  ];
  return (
    <footer className="page-container">
      <div className="wrap pt-12 w768:pt-16 w1024:pt-24">
        <div className="rule-masthead-top flex flex-col gap-8 pb-12 w768:flex-row w768:items-start w768:justify-between">
          <div className="mt-6 flex flex-col gap-4">
            {/* The 44px targets are centred on their text, so the first line is pulled level with the lockup. */}
            <ul className="-mt-3 flex flex-wrap gap-x-8">
              {links.map(({ href, label }) => (
                <li key={href}>
                  <Link href={localize(locale, href)} prefetch={false} data-focus-key={`footer-${href}`} className="link-action text-meta">
                    {label}
                  </Link>
                </li>
              ))}
            </ul>
            <LanguageLinks filterIds={filterIds} size="full" className="lang-footer" />
          </div>
          <div className="mt-6 w768:w-[44ch] w768:max-w-1/2">
            <p className="flex flex-col whitespace-nowrap">
              <Lockup />
            </p>
            <p className="text-meta text-text-secondary mt-4 text-balance">{t.footer.text}</p>
          </div>
        </div>
      </div>
    </footer>
  );
}
