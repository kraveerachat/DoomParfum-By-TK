import type { Metadata, Viewport } from "next";
import { connection } from "next/server";
import type { ReactNode } from "react";
import { LocaleProvider } from "@/i18n/client";
import type { Locale } from "@/i18n/locale";
import { MESSAGES } from "@/i18n/messages";
import { catalogueFor } from "@/server/catalogue";
import { HeaderOffset } from "./header-offset";
import { OverlayProvider } from "./overlay";
import { RouteMemory } from "./route-memory";
import { SiteFooter } from "./site-footer";
import { SiteHeader } from "./site-header";
import { SkipLink } from "./skip-link";

export function shellMetadata(locale: Locale): Metadata {
  const t = MESSAGES[locale];
  return {
    title: { default: t.site.name, template: `%s · ${t.site.name}` },
    description: t.site.description,
    robots: { index: false, follow: false, nocache: true },
  };
}

export const shellViewport: Viewport = { themeColor: "#f7f5f0", width: "device-width", initialScale: 1 };

/**
 * The document for one language. English and Thai each have a root layout that renders this shell,
 * so the server sends the right `lang` with the first byte and moving between them is a full load.
 */
export async function RootShell({ locale, children }: { locale: Locale; children: ReactNode }) {
  // Nonce CSP and no-store delivery require request-time rendering.
  await connection();
  const catalogue = catalogueFor(locale);
  const filterIds = { families: catalogue.families.map((f) => f.id), notes: catalogue.notes.map((n) => n.id) };

  return (
    <html lang={locale}>
      <body>
        <LocaleProvider locale={locale}>
          <OverlayProvider entries={catalogue.entries} filterIds={filterIds}>
            <SkipLink />
            <SiteHeader filterIds={filterIds} />
            <main id="main-content" tabIndex={-1} data-route-target className="page-container grow">
              {children}
            </main>
            <SiteFooter filterIds={filterIds} />
          </OverlayProvider>
          <RouteMemory />
          <HeaderOffset />
        </LocaleProvider>
      </body>
    </html>
  );
}
