"use client";

import Link from "next/link";
import { SyntheticNotice } from "@/components/mock-label";

/** Recoverable render failure. Technical detail is never shown. */
export default function RenderError({ reset }: { error: Error; reset: () => void }) {
  return (
    <>
      <SyntheticNotice />
      <div className="wrap pt-10 w1024:pt-20" role="alert">
        <h1 className="type-page max-w-[18ch]">This page could not be shown</h1>
        <p className="measure mt-4">The local page failed to render. Try again, or return to the mock catalogue.</p>
        <div className="mt-8 flex flex-wrap items-center gap-x-6 gap-y-3">
          <button type="button" className="button-primary" onClick={reset}>
            Retry
          </button>
          <Link href="/explore" prefetch={false} className="link-action">
            Return to Explore
          </Link>
        </div>
      </div>
    </>
  );
}
