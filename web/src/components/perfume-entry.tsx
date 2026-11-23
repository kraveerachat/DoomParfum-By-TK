import Link from "next/link";
import type { Entry } from "@/fixtures/view-model";
import { ScriptText, scriptLang } from "./script-text";
import { StudyVisual } from "./study-visual";

type Props = { readonly entry: Entry; readonly eager?: boolean; readonly as?: "h2" | "h3" };

/** One catalogue record: visual and title share a single link named by the title. */
export function PerfumeEntry({ entry, eager = false, as: Heading = "h3" }: Props) {
  return (
    <article className="min-w-0" data-entry={entry.slug}>
      <Link
        href={`/perfume/${entry.slug}`}
        prefetch={false}
        data-focus-key={`entry-${entry.slug}`}
        aria-labelledby={`title-${entry.slug}`}
        className="group block"
      >
        <StudyVisual study={entry.visual} name={entry.name} eager={eager} />
        <Heading id={`title-${entry.slug}`} lang={scriptLang(entry.name)} className="type-entry mt-4">
          <span className="underline decoration-transparent decoration-1 underline-offset-[0.25em] transition-[text-decoration-color] duration-(--motion-feedback) group-hover:decoration-current">
            {entry.name}
          </span>
        </Heading>
      </Link>
      <p className="text-meta text-text-secondary mt-1">
        <ScriptText>{entry.house}</ScriptText>
      </p>
      <p className="text-meta mt-0.5">
        <span className="font-medium">Mock</span> · {entry.family?.label ?? "Family unknown"}
      </p>
    </article>
  );
}
