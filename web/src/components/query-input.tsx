"use client";

import { Search } from "lucide-react";
import { useId, useRef, type Ref } from "react";
import { clipQuery } from "@/catalogue/search";

type Props = {
  readonly label: string;
  readonly help: string;
  readonly value: string;
  readonly onChange: (value: string) => void;
  readonly ref?: Ref<HTMLInputElement>;
};

/** A plain text input: Escape belongs to the surrounding dialog, not to a native clear action. */
export function QueryInput({ label, help, value, onChange, ref }: Props) {
  const id = useId();
  const composing = useRef(false);
  return (
    <div role="search" aria-label={label}>
      <label htmlFor={id} className="type-control block font-medium">
        {label}
      </label>
      <div className="relative mt-1.5">
        <Search
          aria-hidden="true"
          size={20}
          strokeWidth={1.5}
          className="text-text-secondary pointer-events-none absolute start-3.5 top-1/2 -translate-y-1/2"
        />
        <input
          ref={ref}
          id={id}
          type="text"
          inputMode="search"
          enterKeyHint="search"
          autoComplete="off"
          autoCorrect="off"
          spellCheck={false}
          aria-describedby={`${id}-help`}
          value={value}
          onCompositionStart={() => {
            composing.current = true;
          }}
          onCompositionEnd={(event) => {
            composing.current = false;
            onChange(clipQuery(event.currentTarget.value));
          }}
          onChange={(event) => onChange(composing.current ? event.target.value : clipQuery(event.target.value))}
          className="field-control ps-11"
        />
      </div>
      <p id={`${id}-help`} className="text-meta text-text-secondary mt-1.5">
        {help}
      </p>
    </div>
  );
}
