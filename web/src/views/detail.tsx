import { ArrowLeft, ArrowRight, Minus, Plus } from "lucide-react";
import type { Metadata } from "next";
import Link from "next/link";
import { notFound } from "next/navigation";
import { exploreHref } from "@/catalogue/search";
import { MockMarker, SyntheticNotice } from "@/components/mock-label";
import { ScriptText } from "@/components/script-text";
import { StudyVisual } from "@/components/study-visual";
import type { Field } from "@/fixtures/types";
import { localize, textLang, type Locale } from "@/i18n/locale";
import { format, MESSAGES, type Dictionary } from "@/i18n/messages";
import { catalogueFor, fixtureSet } from "@/server/catalogue";

const find = (slug: string) => fixtureSet.perfumes.find((p) => p.slug === slug);

export function detailMetadata(locale: Locale, slug: string): Metadata {
  const perfume = find(slug);
  // The unavailable view supplies its own title.
  if (!perfume) return {};
  return { title: format(MESSAGES[locale].titles.detail, { name: perfume.name }) };
}

/** Unknown, authored-empty and listed are three different sentences, and unknown is also set apart in type. */
function NoteList({ field, empty, locale, t }: { field: Field<readonly string[]>; empty: string; locale: Locale; t: Dictionary }) {
  const catalogue = catalogueFor(locale);
  if (field.state === "unknown") {
    return (
      <p className="text-text-secondary flex min-h-11 items-center italic" data-field="unknown">
        {t.detail.notSupplied}
      </p>
    );
  }
  if (field.value.length === 0) {
    return (
      <p className="flex min-h-11 items-center" data-field="empty">
        {empty}
      </p>
    );
  }
  return (
    <ul data-field="known">
      {field.value.map((id) => {
        const note = catalogue.notes.find((n) => n.id === id);
        if (!note) return null;
        return (
          <li
            key={id}
            className="flex flex-wrap items-center gap-x-5 w1024:grid w1024:grid-cols-[minmax(0,12rem)_minmax(0,1fr)] w1024:justify-items-start"
          >
            <Link
              href={exploreHref({ family: null, note: id }, localize(locale, "/explore"))}
              prefetch={false}
              data-focus-key={`note-${id}`}
              className="link-action type-entry"
            >
              <span lang={locale === "th" ? "en" : undefined}>{note.label}</span>
              <span className="sr-only">{t.detail.browseNote}</span>
            </Link>
            <span lang={textLang(note.descriptor, locale)} className="text-text-secondary">
              {note.descriptor}
            </span>
          </li>
        );
      })}
    </ul>
  );
}

const LAYERS = [
  ["top", "I"],
  ["heart", "II"],
  ["base", "III"],
] as const;

/**
 * One record-sheet value (T3). It reads the same field and the same note view as the layer section, so
 * the summary cannot disagree with the detail: known names, "not supplied" (unknown, in italics) or
 * "no entries" (authored empty). Names are text here; the links stay in the layer section below.
 */
function SheetValue({ field, names, locale, t }: { field: Field<readonly string[]>; names: (id: string) => string | undefined; locale: Locale; t: Dictionary }) {
  if (field.state === "unknown") {
    return (
      <dd className="text-text-secondary italic" data-field="unknown">
        {t.detail.notSupplied}
      </dd>
    );
  }
  if (field.value.length === 0) return <dd data-field="empty">{t.detail.emptyEntries}</dd>;
  return (
    <dd data-field="known" lang={locale === "th" ? "en" : undefined}>
      {field.value.map(names).filter(Boolean).join(", ")}
    </dd>
  );
}

export function DetailView({ locale, slug }: { locale: Locale; slug: string }) {
  const perfume = find(slug);
  if (!perfume) notFound();
  const t = MESSAGES[locale];
  const catalogue = catalogueFor(locale);
  const entry = catalogue.entries.find((e) => e.id === perfume.id);
  const family = entry?.family;
  const description = entry?.description ?? null;
  const visual = perfume.visual.state === "known" ? perfume.visual.value : null;
  const accords = perfume.accords;
  const explore = localize(locale, "/explore");
  const latin = locale === "th" ? "en" : undefined;
  const noteName = (id: string) => catalogue.notes.find((n) => n.id === id)?.label;
  const accordName = (id: string) => fixtureSet.accords.find((a) => a.id === id)?.label;

  return (
    <>
      <SyntheticNotice />
      <div className="wrap pt-6 w1024:pt-10">
        <nav aria-label={t.detail.breadcrumb}>
          <ol className="text-meta flex flex-wrap items-center gap-x-3">
            <li>
              <Link href={explore} prefetch={false} data-focus-key="breadcrumb" className="link-action">
                {t.detail.explore}
              </Link>
            </li>
            <li aria-hidden="true" className="text-text-secondary">
              /
            </li>
            <li aria-current="page" className="text-text-secondary min-w-0">
              <ScriptText>{perfume.name}</ScriptText>
            </li>
          </ol>
        </nav>

        <div className="mt-4 grid grid-cols-1 gap-y-8 w1024:mt-6 w1024:grid-cols-12 w1024:grid-rows-[auto_1fr] w1024:gap-x-6">
          <div className="w1024:col-span-5 w1024:col-start-8 w1024:ps-6">
            <p className="flex flex-wrap items-center gap-x-4 gap-y-2">
              <MockMarker /> <span lang={latin} className="text-text-secondary">{perfume.houseLabel}</span>
            </p>
            <h1 lang={textLang(perfume.name, locale)} className="type-page mt-4">
              {perfume.name}
            </h1>
          </div>

          <div className="min-w-0 w1024:col-span-7 w1024:col-start-1 w1024:row-span-2 w1024:row-start-1">
            <StudyVisual
              study={visual}
              name={perfume.name}
              alt={t.detail.visualAlt}
              eager
              className="aspect-[4/3] w1024:aspect-[4/5]"
              caption={t.visual.caption}
            />
          </div>

          <div className="w1024:col-span-5 w1024:col-start-8 w1024:ps-6">
            <dl className="record-sheet rule-section" data-record-sheet>
              <div className="record-row border-divider border-b py-3">
                <dt className="text-meta text-text-secondary">{t.detail.family}</dt>
                <dd>
                  {family ? (
                    <Link
                      href={exploreHref({ family: family.id, note: null }, explore)}
                      prefetch={false}
                      data-focus-key="family"
                      className="link-action group gap-2"
                    >
                      <span lang={latin}>{family.label}</span>
                      <ArrowRight aria-hidden="true" size={16} strokeWidth={1.5} className="arrow-nudge" />
                    </Link>
                  ) : (
                    <span className="italic" data-field="unknown">
                      {t.detail.unknown}
                    </span>
                  )}
                </dd>
              </div>
              {(
                [
                  [t.layers.top, perfume.top, noteName],
                  [t.layers.heart, perfume.heart, noteName],
                  [t.layers.base, perfume.base, noteName],
                  [t.layers.generalNotes, perfume.generalNotes, noteName],
                  [t.detail.accords, perfume.accords, accordName],
                ] as const
              ).map(([label, field, names]) => (
                <div key={label} className="record-row border-divider border-b py-3">
                  <dt className="text-meta text-text-secondary">{label}</dt>
                  <SheetValue field={field} names={names} locale={locale} t={t} />
                </div>
              ))}
            </dl>
            <p lang={description ? textLang(description, locale) : undefined} className="mt-6 max-w-[48ch]">
              {description ?? (
                <span className="text-text-secondary italic" data-field="unknown">
                  {t.detail.descriptionUnknown}
                </span>
              )}
            </p>
            <Link href={localize(locale, "/notes")} prefetch={false} data-focus-key="all-notes" className="link-action type-control mt-4">
              {t.detail.allNotes}
            </Link>
          </div>
        </div>

        <section className="mt-12 w768:mt-16 w1024:mt-24" aria-labelledby="layers-heading">
          <div className="flex flex-wrap items-baseline justify-between gap-x-8 gap-y-2">
            <h2 id="layers-heading" className="type-section">
              {t.detail.layersHeading}
            </h2>
            <p className="text-meta text-text-secondary">{t.detail.layersNote}</p>
          </div>
          <div className="rule-section mt-6">
            {LAYERS.map(([key, numeral]) => (
              <div
                key={key}
                data-layer={key}
                className="border-divider grid grid-cols-1 gap-y-2 border-b py-6 w768:grid-cols-[minmax(0,1fr)_minmax(0,3fr)] w768:gap-x-6 w1024:py-8"
              >
                <h3 className="type-section flex items-baseline gap-4">
                  <span aria-hidden="true" className="numeral text-bronze-700 w-8 flex-none text-[1.125rem]">
                    {numeral}
                  </span>
                  {t.layers[key]}
                </h3>
                <NoteList field={perfume[key]} empty={t.detail.emptyLayer} locale={locale} t={t} />
              </div>
            ))}
          </div>
        </section>

        <div className="mt-12 grid grid-cols-1 gap-x-6 gap-y-12 w768:mt-16 w768:grid-cols-2 w1024:mt-20">
          <div data-layer="generalNotes">
            <h2 className="type-entry">{t.layers.generalNotes}</h2>
            <p className="text-meta text-text-secondary mt-1">{t.detail.generalNotesNote}</p>
            <div className="rule-section mt-4 pt-2">
              <NoteList field={perfume.generalNotes} empty={t.detail.emptyList} locale={locale} t={t} />
            </div>
          </div>
          <div data-layer="accords">
            <h2 className="type-entry">{t.detail.accords}</h2>
            <p className="text-meta text-text-secondary mt-1">{t.detail.accordsNote}</p>
            <div className="rule-section mt-4 pt-2">
              {accords.state === "unknown" ? (
                <p className="text-text-secondary flex min-h-11 items-center italic" data-field="unknown">
                  {t.detail.notSupplied}
                </p>
              ) : accords.value.length === 0 ? (
                <p className="flex min-h-11 items-center" data-field="empty">
                  {t.detail.emptyList}
                </p>
              ) : (
                <ul data-field="known" lang={latin}>
                  {accords.value.map((id) => (
                    <li key={id} className="flex min-h-11 items-center">
                      {fixtureSet.accords.find((a) => a.id === id)?.label}
                    </li>
                  ))}
                </ul>
              )}
            </div>
          </div>
        </div>

        <details className="disclosure group border-divider mt-12 border-y w768:mt-16">
          <summary className="flex min-h-14 cursor-pointer items-center justify-between gap-4 font-medium">
            {t.detail.record}
            <Plus aria-hidden="true" size={20} strokeWidth={1.5} className="group-open:hidden" />
            <Minus aria-hidden="true" size={20} strokeWidth={1.5} className="hidden group-open:block" />
          </summary>
          <dl className="bg-gold-50 text-meta mb-6 grid grid-cols-[minmax(0,1fr)_minmax(0,2fr)] gap-x-6 gap-y-2 p-4 w768:grid-cols-[minmax(0,1fr)_minmax(0,5fr)] [&_dd]:min-w-0 [&_dd]:break-words [&_dt]:text-text-secondary">
            <dt>{t.detail.recordId}</dt>
            <dd lang="en">{perfume.id}</dd>
            <dt>{t.detail.recordKind}</dt>
            <dd>{t.detail.recordKindValue}</dd>
            <dt>{t.detail.recordVersion}</dt>
            <dd>{perfume.provenance.fixtureVersion}</dd>
            <dt>{t.detail.recordFor}</dt>
            <dd lang="en">{perfume.provenance.authoredFor}</dd>
            <dt>{t.detail.recordRights}</dt>
            <dd>{t.detail.recordRightsValue}</dd>
          </dl>
        </details>

        <Link href={explore} prefetch={false} data-focus-key="back" className="link-action type-control group mt-8 gap-2">
          <ArrowLeft aria-hidden="true" size={16} strokeWidth={1.5} className="arrow-nudge-back" />
          {t.detail.back}
        </Link>
      </div>
    </>
  );
}
