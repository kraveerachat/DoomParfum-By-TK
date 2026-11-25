"use client";

import { useEffect, useRef, useState } from "react";

/** The visible count updates at once; the spoken count is announced once after input settles. */
export function CountStatus({ text, className }: { text: string; className?: string }) {
  const [spoken, setSpoken] = useState("");
  const first = useRef(true);
  useEffect(() => {
    if (first.current) {
      first.current = false;
      return;
    }
    const timer = setTimeout(() => setSpoken(text), 500);
    return () => clearTimeout(timer);
  }, [text]);
  return (
    <>
      <p className={className}>
        <span className="tabular-nums" data-count>
          {text}
        </span>
      </p>
      <p className="sr-only" role="status" data-count-status>
        {spoken}
      </p>
    </>
  );
}
