import type { Metadata } from "next";
import Link from "next/link";
import { countLabel, exploreHref } from "@/catalogue/search";
import { SyntheticNotice } from "@/components/mock-label";
import { PerfumeEntry } from "@/components/perfume-entry";
import { ScentFolio } from "@/components/scent-folio";
import { catalogue, fixtureSet } from "@/server/catalogue";

export const metadata: Metadata = { title: { absolute: "Home · DoomParfum By TK" } };

const FEATURED_STAGGER = ["", "w1024:mt-16", ""];

export default function HomePage() {
  const featured = fixtureSet.featured.flatMap((slug) => catalogue.entries.filter((e) => e.slug === slug));

  return (
    <>
      <SyntheticNotice />
      <section className="wrap pt-10 pb-10 w1024:pt-12 w1024:pb-6">
        <div className="grid-12 items-end gap-y-10 w768:grid-cols-2 w768:gap-x-6 w1024:grid-cols-12">
          <div className="w1024:col-span-5 w1024:pb-8">
            <h1 className="type-hero max-w-[10ch]">A personal atlas of scent.</h1>
            <p className="mt-6 max-w-[38ch] w1024:mt-8">
              A mock study of how a private perfume notebook could read: fictional fragrances, plainly layered.
            </p>
            <Link href="/explore" prefetch={false} data-focus-key="hero-explore" className="button-primary mt-8">
              Explore mock catalogue
            </Link>
          </div>
          <figure className="min-w-0 w1024:col-span-7 w1600:-me-[min(12rem,calc((100cqi-1440px)/2))]">
            <img
              src="/studies/hero.svg"
              alt="Abstract study: a folded paper sheet and a dark slab crossed by contour lines."
              width={1250}
              height={1000}
              fetchPriority="high"
              className="bg-surface-muted aspect-[5/4] w-full object-cover"
            />
            <figcaption className="text-meta text-text-secondary mt-3">Synthetic visual study</figcaption>
          </figure>
        </div>
      </section>

      <section className="wrap" aria-labelledby="featured-heading">
        <div className="border-ink flex flex-wrap items-baseline justify-between gap-x-8 gap-y-2 border-t pt-6">
          <h2 id="featured-heading" className="type-section">
            Featured discoveries
          </h2>
          <Link href="/explore" prefetch={false} data-focus-key="featured-all" className="link-action">
            View all mock fragrances
          </Link>
        </div>
        <ul className="mt-8 grid grid-cols-1 gap-x-4 gap-y-12 w480:grid-cols-2 w640:gap-x-5 w768:gap-x-6 w1024:mt-12 w1024:grid-cols-3">
          {featured.map((entry, i) => (
            <li key={entry.id} className={FEATURED_STAGGER[i]}>
              <PerfumeEntry entry={entry} />
            </li>
          ))}
        </ul>
      </section>

      <section className="wrap py-12 w768:py-16 w1024:py-24" aria-labelledby="families-heading">
        <h2 id="families-heading" className="type-section">
          Explore by scent
        </h2>
        <ul className="border-ink mt-8 grid grid-cols-1 border-t w640:grid-cols-3 w1024:mt-12">
          {catalogue.families.map((family) => (
            <li
              key={family.id}
              className="group/family border-divider border-b w640:border-s w640:first:border-s-0 w640:border-b-0"
            >
              <Link
                href={exploreHref({ family: family.id, note: null })}
                prefetch={false}
                data-focus-key={`family-${family.id}`}
                className="group can-hover:bg-surface-muted flex h-full items-center gap-6 py-6 transition-colors duration-(--motion-feedback) w640:flex-col w640:items-start w640:px-6 w640:py-8 w640:group-first/family:ps-0 w1024:px-8 w1024:py-12"
              >
                <img
                  src={`/studies/${family.id.replace("mock-family-", "mark-")}.svg`}
                  alt=""
                  width={120}
                  height={120}
                  loading="lazy"
                  className="size-16 flex-none w1024:size-24"
                />
                <span className="min-w-0 w640:pt-8">
                  <span className="type-section block underline decoration-control-border decoration-1 underline-offset-[0.2em] transition-[text-decoration-color] duration-(--motion-feedback) group-hover:decoration-current">
                    {family.label}
                  </span>
                  <span className="mt-2 block">{family.descriptor}</span>
                  <span className="text-meta text-text-secondary mt-1 block tabular-nums">
                    {countLabel(family.count)}
                  </span>
                </span>
              </Link>
            </li>
          ))}
        </ul>
      </section>

      <ScentFolio />

      <section className="wrap pt-12 w768:pt-16 w1024:pt-24" aria-labelledby="journal-heading">
        <div className="grid-12 gap-y-8">
          <div className="w1024:col-span-4">
            <h2 id="journal-heading" className="type-section">
              From the scent notebook
            </h2>
            <p className="text-text-secondary mt-4 max-w-[34ch]">Sample articles, written for this mock.</p>
            <Link href="/about#journal" prefetch={false} data-focus-key="journal-all" className="link-action mt-2">
              Read the scent notebook
            </Link>
          </div>
          <ul className="w1024:col-span-8">
            {fixtureSet.articles.map((article) => (
              <li key={article.id} className="border-divider border-t py-8 first:border-ink w1024:first:pt-6">
                <Link
                  href={`/about#${article.anchor}`}
                  prefetch={false}
                  data-focus-key={`article-${article.id}`}
                  className="group block"
                >
                  <h3 className="type-section">
                    <span className="underline decoration-control-border decoration-1 underline-offset-[0.2em] transition-[text-decoration-color] duration-(--motion-feedback) group-hover:decoration-current">
                      {article.title}
                    </span>
                  </h3>
                  <p className="mt-3 max-w-[52ch]">{article.excerpt}</p>
                </Link>
              </li>
            ))}
          </ul>
        </div>
      </section>
    </>
  );
}
