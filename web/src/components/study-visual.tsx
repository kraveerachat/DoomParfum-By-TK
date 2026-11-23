"use client";

import { useState } from "react";

type Props = {
  readonly study: string | null;
  readonly name: string;
  readonly alt?: string;
  readonly className?: string;
  readonly eager?: boolean;
};

/** Owned local study, or a typographic study when none exists or the file cannot load. */
export function StudyVisual({ study, name, alt = "", className = "aspect-[4/5]", eager = false }: Props) {
  const [broken, setBroken] = useState(false);
  if (study === null || broken) {
    return (
      <div
        className={`bg-surface-muted relative flex w-full items-center justify-center overflow-hidden ${className}`}
        data-visual-fallback
      >
        <span aria-hidden="true" className="font-display text-text-secondary text-[7rem] leading-none select-none">
          {Array.from(name.trim()).at(-1)}
        </span>
        <span className="text-meta text-text-secondary absolute inset-x-4 bottom-3">
          Visual unavailable in this mock
        </span>
      </div>
    );
  }
  return (
    <img
      src={`/studies/${study}.svg`}
      alt={alt}
      width={800}
      height={1000}
      loading={eager ? "eager" : "lazy"}
      decoding="async"
      ref={(img) => {
        // Covers a failure that happened before hydration.
        if (img?.complete && img.naturalWidth === 0) setBroken(true);
      }}
      onError={() => setBroken(true)}
      className={`bg-surface-muted w-full object-cover ${className}`}
    />
  );
}
