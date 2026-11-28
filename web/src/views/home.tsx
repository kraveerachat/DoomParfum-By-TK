import { ArrowRight } from "lucide-react";
import type { Metadata } from "next";
import Link from "next/link";
import { exploreHref } from "@/catalogue/search";
import { SyntheticNotice } from "@/components/mock-label";
import { PerfumeEntry } from "@/components/perfume-entry";
import { ScentFolio } from "@/components/scent-folio";
import { localize, textLang, type Locale } from "@/i18n/locale";
import { MESSAGES } from "@/i18n/messages";
import { articlesFor, catalogueFor, fixtureSet } from "@/server/catalogue";

export function homeMetadata(locale: Locale): Metadata {
  const t = MESSAGES[locale];
  return { title: { absolute: `${t.titles.home} · ${t.site.name}` } };
}

export function HomeView({ locale }: { locale: Locale }) {
  const t = MESSAGES[locale];
  const catalogue = catalogueFor(locale);
  const articles = articlesFor(locale);
  const href = (path: string) => localize(locale, path);
  const latin = locale === "th" ? "en" : undefined;
  const featured = fixtureSet.featured.flatMap((slug) => catalogue.entries.filter((e) => e.slug === slug));

  return (
    <>
      <SyntheticNotice />
      <section className="wrap hero-spread" data-hero>
        <div className="grid-12 items-end gap-y-10 w768:grid-cols-2 w768:items-center w768:gap-x-6 w1024:grid-cols-12">
          <div className="w1024:col-span-5 w1024:pb-8" data-hero-text>
            <h1 className={`type-hero ${locale === "th" ? "max-w-[12ch]" : "max-w-[10ch]"}`}>{t.home.h1}</h1>
            <p className="mt-6 max-w-[38ch] w1024:mt-8">{t.home.lead}</p>
            <Link href={href("/explore")} prefetch={false} data-focus-key="hero-explore" className="button-primary mt-8">
              {t.home.cta}
            </Link>
          </div>
          <figure className="hero-art min-w-0 w1024:col-span-7 w1600:-me-[min(12rem,calc((100cqi-1440px)/2))]">
            <img
              src="/studies/hero.svg"
              alt={t.home.heroAlt}
              width={1250}
              height={1000}
              fetchPriority="high"
              className="bg-surface-muted aspect-[5/4] w-full object-cover"
            />
            <figcaption className="text-meta text-text-secondary mt-3">{t.visual.caption}</figcaption>
          </figure>
        </div>
      </section>

      <section className="wrap" aria-labelledby="featured-heading">
        <div className="rule-section flex flex-wrap items-baseline justify-between gap-x-8 gap-y-2 pt-6">
          <h2 id="featured-heading" className="type-section">
            {t.home.featured}
          </h2>
          <Link href={href("/explore")} prefetch={false} data-focus-key="featured-all" className="link-action type-control group gap-2">
            {t.home.viewAll}
            <ArrowRight aria-hidden="true" size={16} strokeWidth={1.5} className="arrow-nudge" />
          </Link>
        </div>
        <ul className="entry-grid mt-8 grid grid-cols-1 gap-x-4 gap-y-12 w480:grid-cols-2 w640:gap-x-5 w768:gap-x-6 w1024:mt-12 w1024:grid-cols-3">
          {featured.map((entry, i) => (
            <li key={entry.id} className={i === 2 ? "entry-spread w480:col-span-2 w1024:col-span-1" : undefined}>
              <PerfumeEntry entry={entry} />
            </li>
          ))}
        </ul>
      </section>

      <section className="wrap section-gap" aria-labelledby="families-heading">
        <h2 id="families-heading" className="type-section rule-section pt-6">
          {t.home.families}
        </h2>
        <ul className="mt-8 grid grid-cols-1 border-t border-divider w640:grid-cols-3 w640:border-t-0 w1024:mt-12">
          {catalogue.families.map((family) => (
            <li
              key={family.id}
              className="group/family border-divider border-b w640:border-gold-500 w640:border-s w640:first:border-s-0 w640:border-b-0"
            >
              <Link
                href={exploreHref({ family: family.id, note: null }, href("/explore"))}
                prefetch={false}
                data-focus-key={`family-${family.id}`}
                className="group can-hover:bg-gold-50 flex h-full items-center gap-6 py-6 transition-colors duration-(--motion-feedback) w640:flex-col w640:items-start w640:px-6 w640:py-8 w640:group-first/family:ps-0 w1024:px-8 w1024:py-12"
              >
                <img
                  src={`/studies/${family.id.replace("mock-family-", "mark-")}.svg`}
                  alt=""
                  width={120}
                  height={120}
                  loading="lazy"
                  className="size-14 flex-none w1024:size-24"
                />
                <span className="min-w-0 w640:pt-8">
                  <span
                    lang={latin}
                    className="type-section block underline decoration-control-border decoration-1 underline-offset-[0.2em] transition-[text-decoration-color] duration-(--motion-feedback) group-hover:decoration-gold-500"
                  >
                    {family.label}
                  </span>
                  <span lang={textLang(family.descriptor, locale)} className="mt-2 block">
                    {family.descriptor}
                  </span>
                  <span className="mt-3 flex items-baseline gap-2">
                    <span className="numeral text-[1.25rem] leading-none">{family.count}</span>
                    <span className="text-meta text-text-secondary">
                      {family.count === 1 ? t.count.studyWord : t.count.studiesWord}
                    </span>
                  </span>
                </span>
              </Link>
            </li>
          ))}
        </ul>
      </section>

      <ScentFolio />

      <section className="wrap section-gap-top" aria-labelledby="journal-heading">
        <div className="grid-12 gap-y-8">
          <div className="w1024:col-span-4">
            <h2 id="journal-heading" className="type-section">
              {t.home.journal}
            </h2>
            <p className="text-text-secondary mt-4 max-w-[34ch]">{t.home.journalIntro}</p>
            <Link href={href("/about#journal")} prefetch={false} data-focus-key="journal-all" className="link-action type-control mt-2">
              {t.home.journalAll}
            </Link>
          </div>
          <ul className="rule-section w1024:col-span-8">
            {articles.map((article) => (
              <li key={article.id} className="border-divider border-t py-8 first:border-t-0 w1024:first:pt-6">
                <Link
                  href={href(`/about#${article.anchor}`)}
                  prefetch={false}
                  data-focus-key={`article-${article.id}`}
                  className="group grid grid-cols-[minmax(0,1fr)_auto] items-start gap-x-6"
                >
                  <span>
                    <h3 className="type-section">
                      <span className="underline decoration-control-border decoration-1 underline-offset-[0.2em] transition-[text-decoration-color] duration-(--motion-feedback) group-hover:decoration-gold-500">
                        {article.title}
                      </span>
                    </h3>
                    <p className="mt-3 max-w-[52ch]">{article.excerpt}</p>
                  </span>
                  <ArrowRight aria-hidden="true" size={20} strokeWidth={1.5} className="arrow-nudge mt-3" />
                </Link>
              </li>
            ))}
          </ul>
        </div>
      </section>
    </>
  );
}
