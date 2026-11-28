"use client";

import { ChevronDown } from "lucide-react";
import Link from "next/link";
import { useEffect, useState } from "react";
import { useT } from "@/i18n/client";

type Anchor = { readonly id: string; readonly label: string };

/**
 * Page contents. On wide, tall screens it stays beside the text and marks the section being read
 * (aria-current="location"). On narrow screens it is a disclosure. Without scripting it is a plain,
 * always visible list of working anchor links.
 */
export function AboutContents({ anchors }: { anchors: readonly Anchor[] }) {
  const t = useT();
  const [open, setOpen] = useState(false);
  const [current, setCurrent] = useState<string | null>(null);

  useEffect(() => {
    const sections = anchors
      .map((a) => document.getElementById(a.id))
      .filter((el): el is HTMLElement => el !== null);
    const visible = new Map<string, boolean>();
    const observer = new IntersectionObserver(
      (records) => {
        for (const r of records) visible.set(r.target.id, r.isIntersecting);
        const first = sections.find((s) => visible.get(s.id));
        if (first) setCurrent(first.id);
      },
      { rootMargin: "-30% 0px -60% 0px" },
    );
    for (const s of sections) observer.observe(s);
    return () => observer.disconnect();
  }, [anchors]);

  return (
    <nav aria-label={t.about.contents} className="about-contents" data-open={open ? "" : undefined}>
      <button
        type="button"
        className="contents-toggle button-quiet w-full justify-between"
        aria-expanded={open}
        aria-controls="about-contents-list"
        onClick={() => setOpen((v) => !v)}
      >
        {t.about.contents}
        <ChevronDown
          aria-hidden="true"
          size={20}
          strokeWidth={1.5}
          className={`transition-transform duration-(--motion-feedback) ${open ? "rotate-180" : ""}`}
        />
      </button>
      <ul id="about-contents-list" className="contents-list rule-section py-2">
        {anchors.map(({ id, label }) => (
          <li key={id}>
            <Link
              href={`#${id}`}
              prefetch={false}
              aria-current={current === id ? "location" : undefined}
              data-focus-key={`anchor-${id}`}
              className="contents-link link-inline text-meta flex min-h-11 items-center py-1"
            >
              {label}
            </Link>
          </li>
        ))}
      </ul>
    </nav>
  );
}
