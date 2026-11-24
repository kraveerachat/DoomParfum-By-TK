"use client";

import Link from "next/link";
import { usePathname } from "next/navigation";
import { isCurrent, NAV_LINKS } from "./nav-links";
import { Dialog, DialogHeader, DialogPanel, DialogTitle } from "./ui/dialog";

export type OverlayDialogProps = {
  readonly open: boolean;
  readonly onClose: () => void;
  /** Called by links: focus goes to the destination, or back to the trigger on the same page. */
  readonly onNavigate: () => void;
};

export const keepFocus = (event: Event) => event.preventDefault();

export function MenuDialog({ open, onClose, onNavigate }: OverlayDialogProps) {
  const pathname = usePathname();
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
        <DialogHeader>
          <DialogTitle className="text-entry font-medium">Navigation</DialogTitle>
        </DialogHeader>
        <nav aria-label="Menu" className="px-4 pt-4 pb-8 md:px-6">
          <ul className="border-divider border-t">
            {NAV_LINKS.map(({ href, label }) => {
              const current = isCurrent(pathname, href);
              return (
                <li key={href} className="border-divider border-b" data-focus-key="menu-trigger">
                  <Link
                    href={href}
                    prefetch={false}
                    aria-current={current ? "page" : undefined}
                    onClick={onNavigate}
                    className="type-section can-hover:text-navy flex min-h-16 items-center py-3"
                  >
                    <span className={current ? "border-ink border-b" : undefined}>{label}</span>
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
