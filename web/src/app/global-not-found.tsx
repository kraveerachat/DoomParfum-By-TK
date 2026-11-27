import type { Metadata } from "next";
import { headers } from "next/headers";
import { RootShell, shellMetadata, shellViewport } from "@/components/root-shell";
import { LOCALE_HEADER, type Locale } from "@/i18n/locale";
import { MESSAGES } from "@/i18n/messages";
import { UnavailableView } from "@/views/unavailable";
import "./globals.css";

/**
 * The 404 page for every address without a page, in both languages (experimental `globalNotFound`,
 * Owner-authorized for IMP-WEB-02 S9). It is rendered on the server as a full document, so the first
 * byte carries `lang` and the page reads without scripting (DPT-PLAN-013 4.2, V01).
 *
 * The proxy sets the locale header from the requested path on every request and rewrites malformed
 * addresses and unknown slugs here; anything but "th" is English.
 */
async function requestLocale(): Promise<Locale> {
  return (await headers()).get(LOCALE_HEADER) === "th" ? "th" : "en";
}

export async function generateMetadata(): Promise<Metadata> {
  const locale = await requestLocale();
  const t = MESSAGES[locale];
  return { ...shellMetadata(locale), title: `${t.titles.unavailable} · ${t.site.name}` };
}

export const viewport = shellViewport;

export default async function GlobalNotFound() {
  const locale = await requestLocale();
  return (
    <RootShell locale={locale}>
      <UnavailableView locale={locale} />
    </RootShell>
  );
}
