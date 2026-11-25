import type { Metadata } from "next";
import { ExploreCatalogue } from "@/components/explore-catalogue";
import { SyntheticNotice } from "@/components/mock-label";
import { catalogue } from "@/server/catalogue";

export const metadata: Metadata = { title: "Explore mock fragrances" };

export default function ExplorePage() {
  return (
    <>
      <SyntheticNotice />
      <div className="wrap pt-10 w1024:pt-16">
        <h1 className="type-page">Explore mock fragrances</h1>
        <p className="measure mt-4">Every study in this mock, listed by name. Narrow the list by family or note.</p>
        <ExploreCatalogue catalogue={catalogue} />
      </div>
    </>
  );
}
