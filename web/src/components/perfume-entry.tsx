"use client";

import Link from "next/link";
import { useLocale, useT } from "@/i18n/client";
import { localize, textLang } from "@/i18n/locale";
import type { Entry } from "@/fixtures/view-model";
import { ScriptText } from "./script-text";
import { StudyVisual } from "./study-visual";

type Props = { readonly entry: Entry; readonly eager?: boolean; readonly as?: "h2" | "h3" };

/** One catalogue record: visual and title share a single link named by the title. */
export function PerfumeEntry({ entry, eager = false, as: Heading = "h3" }: Props) {
  const locale = useLocale();
  const t = useT();
  return (
    <article className="min-w-0" data-entry={entry.slug}>
      <Link
        href={localize(locale, `/perfume/${entry.slug}`)}
        prefetch={false}
        data-focus-key={`entry-${entry.slug}`}
        className="group block"
      >
        <StudyVisual study={entry.visual} name={entry.name} eager={eager} />
        <Heading lang={textLang(entry.name, locale)} className="type-entry entry-title mt-4">
          <span className="underline decoration-transparent decoration-1 underline-offset-[0.25em] transition-[text-decoration-color] duration-(--motion-feedback) group-hover:decoration-gold-500">
            {entry.name}
          </span>
        </Heading>
      </Link>
      <p className="text-meta text-text-secondary mt-1">
        <ScriptText>{entry.house}</ScriptText>
      </p>
      <p className="text-meta mt-0.5">
        <span className="font-medium">{t.mock}</span> ·{" "}
        {entry.family ? <span lang={locale === "th" ? "en" : undefined}>{entry.family.label}</span> : t.familyUnknown}
      </p>
    </article>
  );
}
