"use client";

import { useEffect } from "react";

/**
 * Keeps --header-h equal to the measured sticky header, so anchors, the skip link and focused
 * controls scroll clear of it (DPT-PLAN-013 5.1). Where the header reflows to two rows, or would cover
 * more than a fifth of the viewport (enlarged text, short screens), it is made static instead. CSS
 * gives the rem fallback and the static rules used without scripting.
 */
export function HeaderOffset() {
  useEffect(() => {
    const header = document.querySelector<HTMLElement>(".site-header");
    if (!header) return;
    const root = document.documentElement;
    const update = () => {
      root.removeAttribute("data-header-static");
      const height = header.getBoundingClientRect().height;
      const tooTall = height > window.innerHeight * 0.2;
      // Two rows: any visible header part starts below the bottom of the brand.
      const brand = header.querySelector("[data-header-brand]")?.getBoundingClientRect();
      const parts = header.querySelector("[data-header-grid]")?.children ?? [];
      const twoRows =
        !!brand &&
        Array.from(parts).some((part) => {
          const box = part.getBoundingClientRect();
          return box.height > 0 && box.top >= brand.bottom - 1;
        });
      if (tooTall || twoRows) root.setAttribute("data-header-static", "");
      const sticky = getComputedStyle(header).position === "sticky";
      root.style.setProperty("--header-h", sticky ? `${Math.ceil(height)}px` : "0px");
    };
    update();
    const observer = new ResizeObserver(update);
    observer.observe(header);
    window.addEventListener("resize", update);
    return () => {
      observer.disconnect();
      window.removeEventListener("resize", update);
      root.style.removeProperty("--header-h");
      root.removeAttribute("data-header-static");
    };
  }, []);
  return null;
}
