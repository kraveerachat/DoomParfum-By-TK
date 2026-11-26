import type { Metadata } from "next";
import { SyntheticNotice } from "@/components/mock-label";
import { NotesIndex } from "@/components/notes-index";
import type { Locale } from "@/i18n/locale";
import { MESSAGES } from "@/i18n/messages";
import { catalogueFor } from "@/server/catalogue";

export const notesMetadata = (locale: Locale): Metadata => ({ title: MESSAGES[locale].titles.notes });

export function NotesView({ locale }: { locale: Locale }) {
  const t = MESSAGES[locale];
  return (
    <>
      <SyntheticNotice />
      <div className="wrap pt-10 w1024:pt-16">
        <h1 className="type-page">{t.titles.notes}</h1>
        <p className="measure mt-4">{t.notes.lead}</p>
        <NotesIndex catalogue={catalogueFor(locale)} />
      </div>
    </>
  );
}
