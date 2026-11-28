// Generated pair: (en) and th render the same view with their locale (DPT-PLAN-013 4.2).
import type { Metadata } from "next";
import { DetailView, detailMetadata } from "@/views/detail";

type Props = { params: Promise<{ slug: string }> };

export async function generateMetadata({ params }: Props): Promise<Metadata> {
  return detailMetadata("th", (await params).slug);
}

export default async function Page({ params }: Props) {
  return <DetailView locale="th" slug={(await params).slug} />;
}
