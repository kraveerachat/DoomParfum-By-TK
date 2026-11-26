import Link from "next/link";
import { SyntheticNotice } from "@/components/mock-label";
import { localize, type Locale } from "@/i18n/locale";
import { MESSAGES } from "@/i18n/messages";

/**
 * Unknown address in either language, with a real 404 status. A server component, so its text is in
 * the server's response even where the framework delivers the page through its error document.
 */
export function UnavailableView({ locale }: { locale: Locale }) {
  const t = MESSAGES[locale];
  return (
    <>
      <SyntheticNotice />
      <div className="wrap pt-10 w1024:pt-20" data-state="unavailable">
        <h1 className="type-page max-w-[18ch]">{t.errors.unavailableTitle}</h1>
        <p className="measure mt-4">{t.errors.unavailableText}</p>
        <Link href={localize(locale, "/explore")} prefetch={false} className="button-primary mt-8">
          {t.errors.unavailableAction}
        </Link>
      </div>
    </>
  );
}
