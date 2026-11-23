"use client";

import { useEffect, useRef } from "react";

const LAYERS = [
  {
    key: "top",
    title: "Top",
    text: "What a record lists first. In this mock it is only an order of reading, like the opening line of a page.",
  },
  {
    key: "heart",
    title: "Heart",
    text: "What a record keeps in the middle. Some studies list two labels here, and some never supplied any.",
  },
  {
    key: "base",
    title: "Base",
    text: "What a record lists last. An empty base is an answer, and an unknown base is still a question.",
  },
] as const;

/** One open folio: three leaves of a single drawing beside three layers that are always legible. */
export function ScentFolio() {
  const root = useRef<HTMLOListElement>(null);

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
            Read it in three layers
          </h2>
          <p className="measure w1024:col-span-5 w1024:col-start-8">
            Illustrative only. Each drawing carries the same number of lines, because a layer records labels and never
            amounts.
          </p>
        </div>
        <ol ref={root} className="mt-12 w1024:mt-20">
          {LAYERS.map(({ key, title, text }) => (
            <li
              key={key}
              className="folio-layer border-control-border grid grid-cols-1 items-stretch gap-y-6 border-t py-8 w1024:grid-cols-12 w1024:gap-x-6 w1024:py-0"
            >
              <div className="w1024:border-gold grid content-center gap-4 w1024:col-span-6 w1024:grid-cols-6 w1024:items-baseline w1024:gap-x-6 w1024:border-e-2 w1024:py-12">
                <h3 className="font-display w1024:col-span-2 text-[2.75rem] leading-[1.1] w1024:text-[4rem]">{title}</h3>
                <p className="max-w-[38ch] w1024:col-span-4 w1024:pe-6">{text}</p>
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
          ))}
        </ol>
      </div>
    </section>
  );
}
