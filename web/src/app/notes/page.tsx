import type { Metadata } from "next";
import { SyntheticNotice } from "@/components/mock-label";
import { NotesIndex } from "@/components/notes-index";
import { catalogue } from "@/server/catalogue";

export const metadata: Metadata = { title: "Notes" };

export default function NotesPage() {
  return (
    <>
      <SyntheticNotice />
      <div className="wrap pt-10 w1024:pt-16">
        <h1 className="type-page">Notes</h1>
        <p className="measure mt-4">
          Nine invented labels. They name impressions for this mock and do not refer to any ingredient or material.
        </p>
        <NotesIndex catalogue={catalogue} />
      </div>
    </>
  );
}
