"use client";

import { usePathname, useSearchParams } from "next/navigation";
import { useEffect, useRef, useState } from "react";
import { locationKey, navigation } from "./navigation-memory";

const nextFrames = (run: () => void) => requestAnimationFrame(() => requestAnimationFrame(run));

function focusForward() {
  const id = decodeURIComponent(window.location.hash.slice(1));
  const target = (id && document.getElementById(id)) || document.querySelector<HTMLElement>("main h1");
  if (!target) return;
  if (!target.hasAttribute("tabindex")) target.setAttribute("tabindex", "-1");
  target.focus({ preventScroll: true });
}

/** Returns a message when the original entry is gone, otherwise an empty string. */
function restore(key: string): string {
  const departure = navigation.departure(key);
  if (!departure) return "";
  let message = "";
  if (departure.focusKey) {
    const origin = Array.from(document.querySelectorAll<HTMLElement>("[data-focus-key]")).find(
      (el) => el.dataset.focusKey === departure.focusKey && el.getClientRects().length > 0,
    );
    const heading = document.querySelector<HTMLElement>("[data-list-heading]");
    if (origin) origin.focus({ preventScroll: true });
    else if (heading) {
      heading.focus({ preventScroll: true });
      message = "The entry you opened is no longer in this list.";
    }
  }
  window.scrollTo(0, departure.scrollY);
  return message;
}

/**
 * Forward navigation focuses the destination h1 (or the linked section). Back and Forward
 * restore the originating entry and scroll position instead.
 */
export function RouteMemory() {
  const pathname = usePathname();
  const search = useSearchParams().toString();
  const first = useRef(true);
  const [message, setMessage] = useState("");

  useEffect(() => {
    const onPop = () => navigation.set("pop");
    const onClick = (event: MouseEvent) => {
      if (event.defaultPrevented || event.button !== 0 || event.metaKey || event.ctrlKey || event.shiftKey || event.altKey) return;
      const link = event.target instanceof Element ? event.target.closest("a") : null;
      if (!link || link.origin !== window.location.origin || link.target) return;
      const key = locationKey();
      if (link.pathname + link.search === key) return;
      const focusKey = link.closest<HTMLElement>("[data-focus-key]")?.dataset.focusKey ?? null;
      navigation.depart(key, { focusKey, scrollY: window.scrollY });
      navigation.set("push");
    };
    window.addEventListener("popstate", onPop, true);
    document.addEventListener("click", onClick, true);
    return () => {
      window.removeEventListener("popstate", onPop, true);
      document.removeEventListener("click", onClick, true);
    };
  }, []);

  useEffect(() => {
    // The framework announcer would repeat the heading that receives focus below.
    document.querySelector("next-route-announcer")?.setAttribute("aria-hidden", "true");

    // Only /explore reads query parameters; elsewhere they are dropped without a request.
    if (pathname !== "/explore" && window.location.search) {
      window.history.replaceState(null, "", window.location.pathname + window.location.hash);
      if (!first.current && navigation.kind() === null) return;
    }
    if (first.current) {
      first.current = false;
      navigation.set(null);
      return;
    }
    const kind = navigation.kind();
    navigation.set(null);
    if (kind === "push") nextFrames(focusForward);
    if (kind === "pop") nextFrames(() => setMessage(restore(locationKey())));
  }, [pathname, search]);

  return (
    <p className="sr-only" role="status">
      {message}
    </p>
  );
}
