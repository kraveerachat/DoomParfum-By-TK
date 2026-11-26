"use client";

import { Menu, Search, UserRound } from "lucide-react";
import Link from "next/link";
import { usePathname } from "next/navigation";
import { useLocale, useT } from "@/i18n/client";
import { localize } from "@/i18n/locale";
import { LanguageLinks, LanguageSwitch, type FilterIds } from "./language-links";
import { isCurrent, NAV_LINKS } from "./nav-links";
import { useOverlay } from "./overlay";

const icon = { "aria-hidden": true, size: 20, strokeWidth: 1.5 } as const;

/** The text identity, always in Latin script (K03). The footer repeats it without a link. */
export function Lockup() {
  return (
    <>
      <span lang="en" className="wordmark-name leading-[1.15] font-medium tracking-[0.06em]">
        DOOMPARFUM
      </span>{" "}
      <span lang="en" className="text-signature text-gold-readable font-medium tracking-[0.1em]">
        BY TK
      </span>
    </>
  );
}

function Wordmark() {
  const locale = useLocale();
  const t = useT();
  return (
    <Link
      href={localize(locale, "/")}
      prefetch={false}
      aria-label={t.site.homeLink}
      data-focus-key="brand"
      className="inline-flex min-h-11 flex-col justify-center whitespace-nowrap"
    >
      <Lockup />
    </Link>
  );
}

export function SiteHeader({ filterIds }: { filterIds: FilterIds }) {
  const pathname = usePathname();
  const locale = useLocale();
  const t = useT();
  const { active, open } = useOverlay();

  return (
    <header className="site-header">
      <div className="site-header-inner rule-masthead pb-[6px]">
        <div className="page-container"><div className="wrap">
          <div className="header-grid" data-header-grid>
            <button
              type="button"
              className="header-menu icon-button -ms-[12px]"
              aria-label={t.nav.menu}
              aria-haspopup="dialog"
              aria-expanded={active === "menu"}
              data-focus-key="menu-trigger"
              onClick={(event) => open("menu", event.currentTarget)}
            >
              <Menu {...icon} />
            </button>
            <div className="header-brand min-w-0" data-header-brand>
              <Wordmark />
            </div>
            <nav className="header-nav" aria-label={t.nav.primary} data-header-nav>
              <ul className="flex gap-8">
                {NAV_LINKS.map(({ href, key }) => {
                  const current = isCurrent(pathname, href);
                  const label = t.nav[key];
                  return (
                    <li key={href}>
                      <Link
                        href={localize(locale, href)}
                        prefetch={false}
                        aria-current={current ? "page" : undefined}
                        data-focus-key={`nav-${href}`}
                        className={`inline-flex min-h-11 min-w-11 items-center justify-center text-[0.9375rem] leading-6 ${current ? "font-semibold" : "font-medium"}`}
                      >
                        <span
                          data-label={label}
                          className={`nav-label inline-block border-b-2 py-0.5 transition-colors duration-(--motion-feedback) ${current ? "border-gold-500" : "can-hover:border-control-border border-transparent"}`}
                        >
                          {label}
                        </span>
                      </Link>
                    </li>
                  );
                })}
              </ul>
            </nav>
            <div className="header-utils flex items-center gap-2" data-header-utils>
              <button
                type="button"
                className="icon-button"
                aria-label={t.nav.search}
                aria-haspopup="dialog"
                aria-expanded={active === "search"}
                data-focus-key="search-trigger"
                onClick={(event) => open("search", event.currentTarget)}
              >
                <Search {...icon} />
              </button>
              <button
                type="button"
                className="icon-button header-profile"
                aria-label={t.nav.profile}
                aria-haspopup="dialog"
                aria-expanded={active === "profile"}
                data-focus-key="profile-trigger"
                onClick={(event) => open("profile", event.currentTarget)}
              >
                <UserRound {...icon} />
              </button>
              <span aria-hidden="true" className="lang-divider lang-full" />
              <LanguageLinks filterIds={filterIds} className="lang-full -me-[12px] items-center" />
              <span className="lang-compact -me-[12px]">
                <LanguageSwitch filterIds={filterIds} />
              </span>
            </div>
          </div>
        </div></div>
      </div>
    </header>
  );
}
