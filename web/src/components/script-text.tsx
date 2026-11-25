import { isThai } from "@/catalogue/search";

/** Marks Thai text so it is announced, shaped and spaced as Thai. */
export const scriptLang = (text: string) => (isThai(text) ? "th" : undefined);

export function ScriptText({ children, className }: { children: string; className?: string }) {
  return (
    <span lang={scriptLang(children)} className={className}>
      {children}
    </span>
  );
}
