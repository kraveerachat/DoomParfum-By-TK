import type { Metadata } from "next";
import Link from "next/link";
import { SyntheticNotice } from "@/components/mock-label";

export const metadata: Metadata = { title: "Unavailable" };

export default function NotFound() {
  return (
    <>
      <SyntheticNotice />
      <div className="wrap pt-10 w1024:pt-20" data-state="unavailable">
        <h1 className="type-page max-w-[18ch]">This page is unavailable</h1>
        <p className="measure mt-4">Nothing in this mock uses that address. The link may be incomplete.</p>
        <Link href="/explore" prefetch={false} className="button-primary mt-8">
          Return to the mock catalogue
        </Link>
      </div>
    </>
  );
}
