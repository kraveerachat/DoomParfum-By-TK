import { ChevronDown } from "lucide-react";
import type { Metadata } from "next";
import Link from "next/link";
import { notFound } from "next/navigation";
import { exploreHref } from "@/catalogue/search";
import { MockMarker, SyntheticNotice } from "@/components/mock-label";
import { ScriptText, scriptLang } from "@/components/script-text";
import { StudyVisual } from "@/components/study-visual";
import type { Field } from "@/fixtures/types";
import { catalogue, fixtureSet } from "@/server/catalogue";

type Props = { params: Promise<{ slug: string }> };

const find = (slug: string) => fixtureSet.perfumes.find((p) => p.slug === slug);

export async function generateMetadata({ params }: Props): Promise<Metadata> {
  const perfume = find((await params).slug);
  // The unavailable view supplies its own title.
  if (!perfume) return {};
  return { title: `${perfume.name} · Mock study` };
}

/** Unknown, authored-empty and listed are three different sentences. */
function NoteList({ field, empty }: { field: Field<readonly string[]>; empty: string }) {
  if (field.state === "unknown") {
    return (
      <p className="text-text-secondary flex min-h-11 items-center" data-field="unknown">
        Not supplied in this mock
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
              href={exploreHref({ family: null, note: id })}
              prefetch={false}
              data-focus-key={`note-${id}`}
              className="link-action type-entry"
            >
              {note.label}
              <span className="sr-only">, browse mock studies</span>
            </Link>
            <span className="text-text-secondary">{note.descriptor}</span>
          </li>
        );
      })}
    </ul>
  );
}

const LAYERS = [
  ["top", "Top"],
  ["heart", "Heart"],
  ["base", "Base"],
] as const;

export default async function PerfumePage({ params }: Props) {
  const perfume = find((await params).slug);
  if (!perfume) notFound();

  const family = catalogue.entries.find((e) => e.id === perfume.id)?.family;
  const visual = perfume.visual.state === "known" ? perfume.visual.value : null;
  const accords = perfume.accords;

  return (
    <>
      <SyntheticNotice />
      <div className="wrap pt-6 w1024:pt-10">
        <nav aria-label="Breadcrumb">
          <ol className="text-meta flex flex-wrap items-center gap-x-3">
            <li>
              <Link href="/explore" prefetch={false} data-focus-key="breadcrumb" className="link-action">
                Explore
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
              <MockMarker /> <span className="text-text-secondary">{perfume.houseLabel}</span>
            </p>
            <h1 lang={scriptLang(perfume.name)} className="type-page mt-4">
              {perfume.name}
            </h1>
          </div>

          <div className="min-w-0 w1024:col-span-7 w1024:col-start-1 w1024:row-span-2 w1024:row-start-1">
            <StudyVisual
              study={visual}
              name={perfume.name}
              alt="Abstract study drawn for this fictional record"
              eager
              className="aspect-[4/3] w1024:aspect-[4/5]"
              caption="Synthetic visual study"
            />
          </div>

          <div className="w1024:col-span-5 w1024:col-start-8 w1024:ps-6">
            <dl className="border-divider border-t">
              <div className="border-divider flex flex-wrap items-center gap-x-8 border-b py-3">
                <dt className="text-meta text-text-secondary">Family</dt>
                <dd>
                  {family ? (
                    <Link
                      href={exploreHref({ family: family.id, note: null })}
                      prefetch={false}
                      data-focus-key="family"
                      className="link-action"
                    >
                      {family.label}
                    </Link>
                  ) : (
                    <span data-field="unknown">Unknown</span>
                  )}
                </dd>
              </div>
            </dl>
            <p lang={perfume.description.state === "known" ? scriptLang(perfume.description.value) : undefined} className="mt-6 max-w-[48ch]">
              {perfume.description.state === "known" ? (
                perfume.description.value
              ) : (
                <span className="text-text-secondary" data-field="unknown">
                  Description not supplied in this mock
                </span>
              )}
            </p>
            <Link href="/notes" prefetch={false} data-focus-key="all-notes" className="link-action type-control mt-4">
              Read about the notes
            </Link>
          </div>
        </div>

        <section className="mt-12 w768:mt-16 w1024:mt-24" aria-labelledby="layers-heading">
          <div className="flex flex-wrap items-baseline justify-between gap-x-8 gap-y-2">
            <h2 id="layers-heading" className="type-section">
              Three layers
            </h2>
            <p className="text-meta text-text-secondary">Illustrative labels. No amounts are recorded.</p>
          </div>
          <div className="border-ink mt-8 border-t">
            {LAYERS.map(([key, label]) => (
              <div
                key={key}
                data-layer={key}
                className="border-divider grid grid-cols-1 gap-y-2 border-b py-6 w768:grid-cols-[minmax(0,1fr)_minmax(0,3fr)] w768:gap-x-6 w1024:py-10"
              >
                <h3 className="type-section">
                  {label}
                </h3>
                <NoteList field={perfume[key]} empty="No entries in this mock layer" />
              </div>
            ))}
          </div>
        </section>

        <div className="mt-12 grid grid-cols-1 gap-x-6 gap-y-12 w768:mt-16 w768:grid-cols-2 w1024:mt-24">
          <div data-layer="generalNotes">
            <h2 className="type-entry">General notes</h2>
            <p className="text-meta text-text-secondary mt-1">Listed for the whole record, outside the layers.</p>
            <div className="border-divider mt-4 border-t pt-2">
              <NoteList field={perfume.generalNotes} empty="No entries in this mock list" />
            </div>
          </div>
          <div data-layer="accords">
            <h2 className="type-entry">Accords</h2>
            <p className="text-meta text-text-secondary mt-1">Fictional descriptors, without weights.</p>
            <div className="border-divider mt-4 border-t pt-2">
              {accords.state === "unknown" ? (
                <p className="text-text-secondary flex min-h-11 items-center" data-field="unknown">
                  Not supplied in this mock
                </p>
              ) : accords.value.length === 0 ? (
                <p className="flex min-h-11 items-center" data-field="empty">
                  No entries in this mock list
                </p>
              ) : (
                <ul data-field="known">
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

        <details className="group border-divider mt-12 border-y w768:mt-16">
          <summary className="flex min-h-14 cursor-pointer items-center justify-between gap-4 font-medium">
            About this mock record
            <ChevronDown
              aria-hidden="true"
              size={20}
              strokeWidth={1.5}
              className="transition-transform duration-(--motion-feedback) group-open:rotate-180"
            />
          </summary>
          <dl className="text-meta grid grid-cols-[minmax(0,1fr)_minmax(0,2fr)] w768:grid-cols-[minmax(0,1fr)_minmax(0,5fr)] gap-x-6 gap-y-2 pb-6 [&_dd]:min-w-0 [&_dd]:break-words [&_dt]:text-text-secondary">
            <dt>Record</dt>
            <dd>{perfume.id}</dd>
            <dt>Kind</dt>
            <dd>Locally authored fixture, entirely synthetic</dd>
            <dt>Version</dt>
            <dd>{perfume.provenance.fixtureVersion}</dd>
            <dt>Authored for</dt>
            <dd>{perfume.provenance.authoredFor}</dd>
            <dt>Rights</dt>
            <dd>Original project material</dd>
          </dl>
        </details>

        <Link href="/explore" prefetch={false} data-focus-key="back" className="link-action type-control mt-8">
          Back to the mock catalogue
        </Link>
      </div>
    </>
  );
}
