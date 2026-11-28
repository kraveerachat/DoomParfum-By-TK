// Generated pair: (en) and th render the same view with their locale (DPT-PLAN-013 4.2).
import type { ReactNode } from "react";
import { RootShell, shellMetadata, shellViewport } from "@/components/root-shell";
import "../globals.css";

export const metadata = shellMetadata("th");
export const viewport = shellViewport;

export default function Layout({ children }: { children: ReactNode }) {
  return <RootShell locale="th">{children}</RootShell>;
}
