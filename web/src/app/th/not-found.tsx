// Generated pair: (en) and th render the same view with their locale (DPT-PLAN-013 4.2).
import type { Metadata } from "next";
import { MESSAGES } from "@/i18n/messages";
import { UnavailableView } from "@/views/unavailable";

export const metadata: Metadata = { title: MESSAGES["th"].titles.unavailable };

export default function NotFound() {
  return <UnavailableView locale="th" />;
}
