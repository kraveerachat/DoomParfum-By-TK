"use client";

import { useLocale } from "@/i18n/client";
import { textLang } from "@/i18n/locale";

/** Marks text in the other script, so it is announced, shaped and spaced in its own language. */
export function ScriptText({ children, className }: { children: string; className?: string }) {
  const locale = useLocale();
  return (
    <span lang={textLang(children, locale)} className={className}>
      {children}
    </span>
  );
}
