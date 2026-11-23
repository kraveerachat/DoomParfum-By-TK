import type { Metadata, Viewport } from "next";
import { connection } from "next/server";
import type { ReactNode } from "react";
import { OverlayProvider } from "@/components/overlay";
import { RouteMemory } from "@/components/route-memory";
import { SiteFooter } from "@/components/site-footer";
import { SiteHeader } from "@/components/site-header";
import { catalogue } from "@/server/catalogue";
import "./globals.css";

export const metadata: Metadata = {
  title: { default: "DoomParfum By TK", template: "%s · DoomParfum By TK" },
  description: "A mock-only fragrance notebook. Every record is fictional.",
  robots: { index: false, follow: false, nocache: true },
};

export const viewport: Viewport = { themeColor: "#f7f5f0", width: "device-width", initialScale: 1 };

export default async function RootLayout({ children }: { children: ReactNode }) {
  // Nonce CSP and no-store delivery require request-time rendering.
  await connection();

  return (
    <html lang="en">
      <body>
        <OverlayProvider entries={catalogue.entries}>
          <a
            href="#main-content"
            className="bg-ink text-on-dark focus-visible:z-[100] fixed start-4 top-4 -translate-y-24 px-4 py-3 font-medium focus-visible:translate-y-0"
          >
            Skip to content
          </a>
          <SiteHeader />
          <main id="main-content" tabIndex={-1} data-route-target className="page-container">
            {children}
          </main>
          <SiteFooter />
        </OverlayProvider>
        <RouteMemory />
      </body>
    </html>
  );
}
