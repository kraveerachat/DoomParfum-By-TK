"use client";

import { useT } from "@/i18n/client";

/** Persistent disclosures. They are never dismissible and never depend on hover. */
export function SyntheticNotice() {
  const t = useT();
  return (
    <p className="wrap text-meta text-text-secondary pt-4" data-synthetic-notice>
      {t.notice}
    </p>
  );
}

export function MockMarker() {
  const t = useT();
  return (
    <span
      className="border-bronze-700 text-bronze-700 text-meta rounded-button inline-block border px-2 py-0.5 font-medium"
      data-mock-marker
    >
      {t.mock}
    </span>
  );
}
