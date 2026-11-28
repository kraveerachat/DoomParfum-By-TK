"use client";

import { createContext, useContext, type ReactNode } from "react";
import type { Locale } from "./locale";
import { MESSAGES, type Dictionary } from "./messages";

const LocaleContext = createContext<Locale>("en");

/** The locale is fixed per document: each language has its own root layout (DPT-PLAN-013 4.2). */
export function LocaleProvider({ locale, children }: { locale: Locale; children: ReactNode }) {
  return <LocaleContext value={locale}>{children}</LocaleContext>;
}

export const useLocale = (): Locale => useContext(LocaleContext);
export const useT = (): Dictionary => MESSAGES[useContext(LocaleContext)];
