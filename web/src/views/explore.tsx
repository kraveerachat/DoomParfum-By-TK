import type { Metadata } from "next";
import { ExploreCatalogue } from "@/components/explore-catalogue";
import { SyntheticNotice } from "@/components/mock-label";
import type { Locale } from "@/i18n/locale";
import { MESSAGES } from "@/i18n/messages";
import { catalogueFor } from "@/server/catalogue";

export const exploreMetadata = (locale: Locale): Metadata => ({ title: MESSAGES[locale].titles.explore });

export function ExploreView({ locale }: { locale: Locale }) {
  const t = MESSAGES[locale];
  return (
    <>
      <SyntheticNotice />
      <div className="wrap pt-8">
        <h1 className="type-page">{t.titles.explore}</h1>
        <p className="measure mt-2">{t.explore.lead}</p>
        <ExploreCatalogue catalogue={catalogueFor(locale)} />
      </div>
    </>
  );
}
