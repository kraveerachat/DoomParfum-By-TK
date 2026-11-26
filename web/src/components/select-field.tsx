"use client";

import { ChevronDown } from "lucide-react";
import { useId, type Ref } from "react";

type Option = { readonly value: string; readonly label: string; readonly lang?: string | undefined };
type Props = {
  readonly label: string;
  readonly value: string;
  readonly options: readonly Option[];
  readonly onChange: (value: string) => void;
  readonly ref?: Ref<HTMLSelectElement>;
  readonly id?: string;
  /** Label beside the control on wider screens (T4 compact toolbar). */
  readonly inline?: boolean;
};

export function SelectField({ label, value, options, onChange, ref, id, inline = false }: Props) {
  const auto = useId();
  const controlId = id ?? auto;
  return (
    <div className={`min-w-0${inline ? " toolbar-field" : ""}`}>
      <label htmlFor={controlId} className="type-control block font-medium">
        {label}
      </label>
      <div className="relative mt-1.5">
        <select
          ref={ref}
          id={controlId}
          value={value}
          onChange={(event) => onChange(event.target.value)}
          className="field-control appearance-none pe-11 text-ellipsis"
        >
          {options.map((option) => (
            <option key={option.value} value={option.value} lang={option.lang}>
              {option.label}
            </option>
          ))}
        </select>
        <ChevronDown
          aria-hidden="true"
          size={20}
          strokeWidth={1.5}
          className="pointer-events-none absolute end-3 top-1/2 -translate-y-1/2"
        />
      </div>
    </div>
  );
}
