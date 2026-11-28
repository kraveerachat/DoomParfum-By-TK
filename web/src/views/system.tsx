"use client";

import Link from "next/link";
import { SyntheticNotice } from "@/components/mock-label";
import { useLocale, useT } from "@/i18n/client";
import { localize } from "@/i18n/locale";

/** Recoverable render failure. Technical detail is never shown. */
export function RenderErrorView({ retry }: { retry: () => void }) {
  const t = useT();
  const locale = useLocale();
  return (
    <>
      <SyntheticNotice />
      <div className="wrap pt-10 w1024:pt-20" role="alert">
        <h1 className="type-page max-w-[18ch]">{t.errors.renderTitle}</h1>
        <p className="measure mt-4">{t.errors.renderText}</p>
        <div className="mt-8 flex flex-wrap items-center gap-x-6 gap-y-3">
          <button type="button" className="button-primary" onClick={retry}>
            {t.errors.retry}
          </button>
          <Link href={localize(locale, "/explore")} prefetch={false} className="link-action">
            {t.errors.returnExplore}
          </Link>
        </div>
      </div>
    </>
  );
}
