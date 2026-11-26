"use client";

import { useEffect } from "react";

/**
 * Keeps --header-h equal to the measured sticky header, so anchors, the skip link and focused
 * controls scroll clear of it (DPT-PLAN-013 5.1). Where the header would cover more than a fifth of
 * the viewport (enlarged text, short screens) it is made static instead. CSS gives a rem fallback.
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
      if (tooTall) root.setAttribute("data-header-static", "");
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
