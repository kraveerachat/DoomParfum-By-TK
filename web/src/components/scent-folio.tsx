"use client";

import { useEffect, useRef } from "react";
import { useT } from "@/i18n/client";
import { format } from "@/i18n/messages";

const LAYERS = [
  { key: "top", numeral: "I" },
  { key: "heart", numeral: "II" },
  { key: "base", numeral: "III" },
] as const;

/**
 * One open folio: three leaves of a single drawing beside three layers that are always legible.
 * The Roman numerals mark the order of reading, which is the information a layer carries; they are
 * decorative for assistive technology because the heading already names the layer.
 */
export function ScentFolio() {
  const t = useT();
  const root = useRef<HTMLOListElement>(null);
  const text = { top: t.home.folioTop, heart: t.home.folioHeart, base: t.home.folioBase };

  useEffect(() => {
    const layers = Array.from(root.current?.children ?? []);
    const below = layers.filter((el) => el.getBoundingClientRect().top > window.innerHeight);
    if (!below.length || window.matchMedia("(prefers-reduced-motion: reduce)").matches) return;
    const observer = new IntersectionObserver(
      (records) => {
        for (const record of records) {
          if (!record.isIntersecting) continue;
          record.target.removeAttribute("data-armed");
          observer.unobserve(record.target);
        }
      },
      { threshold: 0.1 },
    );
    for (const el of below) {
      el.setAttribute("data-armed", "");
      observer.observe(el);
    }
    return () => {
      observer.disconnect();
      for (const el of below) el.removeAttribute("data-armed");
    };
  }, []);

  return (
    <section className="bg-navy text-on-dark on-dark" aria-labelledby="folio-heading">
      <div className="wrap py-16 w1024:py-32">
        <div className="grid-12 items-end gap-y-6">
          <h2 id="folio-heading" className="type-section w1024:col-span-5">
            {t.home.folio}
          </h2>
          <p className="measure w1024:col-span-5 w1024:col-start-8">{t.home.folioIntro}</p>
        </div>
        <ol ref={root} className="folio-list mt-12 w1024:mt-20">
          {LAYERS.map(({ key, numeral }) => {
            const title = t.layers[key];
            return (
              <li
                key={key}
                className="folio-layer grid grid-cols-1 items-stretch gap-y-6 py-8 w1024:grid-cols-12 w1024:gap-x-6 w1024:py-0"
              >
                <div className="w1024:border-gold-on-navy grid content-start gap-4 w1024:col-span-6 w1024:grid-cols-6 w1024:gap-x-6 w1024:border-e w1024:py-10">
                  <div className="w1024:col-span-2">
                    <span aria-hidden="true" className="numeral text-gold-on-navy block text-[1.5rem] leading-none">
                      {numeral}
                    </span>
                    <h3 className="type-page mt-3">{title}</h3>
                  </div>
                  <div className="max-w-[38ch] w1024:col-span-4 w1024:pe-6 w1024:pt-8">
                    <p>{text[key]}</p>
                    <p className="text-meta mt-3">{format(t.home.folioDrawing, { layer: title })}</p>
                  </div>
                </div>
                <img
                  src={`/studies/folio-${key}.svg`}
                  alt=""
                  width={800}
                  height={420}
                  loading="lazy"
                  decoding="async"
                  className="aspect-[40/21] w-full w1024:col-span-6"
                />
              </li>
            );
          })}
        </ol>
      </div>
    </section>
  );
}
