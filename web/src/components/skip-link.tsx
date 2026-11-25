"use client";

/** Moves focus without adding a history entry that the router could not restore. */
export function SkipLink() {
  return (
    <a
      href="#main-content"
      onClick={(event) => {
        const main = document.getElementById("main-content");
        if (!main) return;
        event.preventDefault();
        main.focus({ preventScroll: true });
        main.scrollIntoView({ block: "start" });
      }}
      className="bg-ink text-on-dark focus-visible:z-[100] fixed start-4 top-4 -translate-y-24 px-4 py-3 font-medium focus-visible:translate-y-0"
    >
      Skip to content
    </a>
  );
}
