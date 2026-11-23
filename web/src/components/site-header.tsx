"use client";

import { Menu, Search, UserRound } from "lucide-react";
import Link from "next/link";
import { usePathname } from "next/navigation";
import { isCurrent, NAV_LINKS } from "./nav-links";
import { useOverlay } from "./overlay";

const icon = { "aria-hidden": true, size: 20, strokeWidth: 1.5 } as const;

function Wordmark() {
  return (
    <Link
      href="/"
      prefetch={false}
      aria-label="DoomParfum By TK home"
      data-focus-key="brand"
      className="inline-flex min-h-11 flex-col justify-center whitespace-nowrap"
    >
      <span className="wordmark-name leading-[1.15] font-medium tracking-[0.06em]">DOOMPARFUM</span>{" "}
      <span className="text-signature text-gold-readable font-medium tracking-[0.1em]">BY TK</span>
    </Link>
  );
}

export function SiteHeader() {
  const pathname = usePathname();
  const { active, open } = useOverlay();

  return (
    <header className="site-header border-divider bg-paper border-b">
      <div className="page-container">
        <div className="wrap">
          <div className="header-grid" data-header-grid>
            <button
              type="button"
              className="header-menu icon-button -ms-[12px]"
              aria-label="Menu"
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
            <nav className="header-nav" aria-label="Primary" data-header-nav>
              <ul className="flex gap-8">
                {NAV_LINKS.map(({ href, label }) => {
                  const current = isCurrent(pathname, href);
                  return (
                    <li key={href}>
                      <Link
                        href={href}
                        prefetch={false}
                        aria-current={current ? "page" : undefined}
                        data-focus-key={`nav-${href}`}
                        className={`inline-flex min-h-11 min-w-11 items-center justify-center text-[0.9375rem] leading-6 ${current ? "font-semibold" : "font-medium"}`}
                      >
                        <span
                          className={`border-b py-0.5 transition-colors duration-(--motion-feedback) ${current ? "border-ink" : "can-hover:border-control-border border-transparent"}`}
                        >
                          {label}
                        </span>
                      </Link>
                    </li>
                  );
                })}
              </ul>
            </nav>
            <div className="header-utils flex gap-2" data-header-utils>
              <button
                type="button"
                className="icon-button"
                aria-label="Search mock catalogue"
                aria-haspopup="dialog"
                aria-expanded={active === "search"}
                data-focus-key="search-trigger"
                onClick={(event) => open("search", event.currentTarget)}
              >
                <Search {...icon} />
              </button>
              <button
                type="button"
                className="icon-button -me-[12px]"
                aria-label="Profile unavailable in this mock"
                aria-haspopup="dialog"
                aria-expanded={active === "profile"}
                data-focus-key="profile-trigger"
                onClick={(event) => open("profile", event.currentTarget)}
              >
                <UserRound {...icon} />
              </button>
            </div>
          </div>
        </div>
      </div>
    </header>
  );
}
