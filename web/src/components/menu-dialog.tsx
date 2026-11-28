"use client";

import Link from "next/link";
import { usePathname } from "next/navigation";
import { useLocale, useT } from "@/i18n/client";
import { localize } from "@/i18n/locale";
import { LanguageLinks, type FilterIds } from "./language-links";
import { isCurrent, NAV_LINKS } from "./nav-links";
import { Dialog, DialogHeader, DialogPanel, DialogTitle } from "./ui/dialog";

export type OverlayDialogProps = {
  readonly open: boolean;
  readonly onClose: () => void;
  /** Called by links: focus goes to the destination, or back to the trigger on the same page. */
  readonly onNavigate: () => void;
};

export const keepFocus = (event: Event) => event.preventDefault();

export function MenuDialog({ open, onClose, onNavigate, filterIds }: OverlayDialogProps & { filterIds: FilterIds }) {
  const pathname = usePathname();
  const locale = useLocale();
  const t = useT();
  return (
    <Dialog open={open} onOpenChange={(next) => !next && onClose()}>
      <DialogPanel
        className="panel panel-drawer"
        data-panel
        aria-describedby={undefined}
        onCloseAutoFocus={keepFocus}
        onOpenAutoFocus={(event) => {
          event.preventDefault();
          (event.currentTarget as HTMLElement).querySelector<HTMLElement>("[data-dialog-close]")?.focus();
        }}
      >
        <DialogHeader closeLabel={t.nav.close}>
          <DialogTitle className="text-entry font-medium">{t.nav.menuTitle}</DialogTitle>
        </DialogHeader>
        <div className="px-4 pt-2 md:px-6">
          <LanguageLinks filterIds={filterIds} size="full" className="lang-segment" />
        </div>
        <nav aria-label={t.nav.menuList} className="px-4 pt-6 pb-8 md:px-6">
          <ul className="rule-section">
            {NAV_LINKS.map(({ href, key }) => {
              const current = isCurrent(pathname, href);
              return (
                <li key={href} className="border-divider border-b" data-focus-key="menu-trigger">
                  <Link
                    href={localize(locale, href)}
                    prefetch={false}
                    aria-current={current ? "page" : undefined}
                    onClick={onNavigate}
                    className="type-section can-hover:text-navy flex min-h-16 items-center py-3"
                  >
                    <span className={current ? "border-gold-500 border-b-2" : undefined}>{t.nav[key]}</span>
                  </Link>
                </li>
              );
            })}
          </ul>
        </nav>
      </DialogPanel>
    </Dialog>
  );
}
