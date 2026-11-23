"use client";

import { usePathname, useSearchParams } from "next/navigation";
import { useEffect, useRef, useState } from "react";
import { currentFocusKey, entryKey, locationKey, navigation } from "./navigation-memory";

/** Shorter transitions show no pending state at all. */
const PENDING_AFTER_MS = 400;

const nextFrames = (run: () => void) => requestAnimationFrame(() => requestAnimationFrame(run));

function focusTarget(target: HTMLElement | null) {
  if (!target) return;
  if (!target.hasAttribute("tabindex")) target.setAttribute("tabindex", "-1");
  target.focus({ preventScroll: true });
}

function focusForward() {
  const id = decodeURIComponent(window.location.hash.slice(1));
  focusTarget((id && document.getElementById(id)) || document.querySelector<HTMLElement>("main h1"));
}

/** Returns a message when the original entry is gone, otherwise an empty string. */
function restore(key: string): string {
  const departure = navigation.departure(key);
  if (!departure) return "";
  let message = "";
  if (departure.focusKey) {
    const origins = Array.from(document.querySelectorAll<HTMLElement>("[data-focus-key]")).filter(
      (el) => el.dataset.focusKey === departure.focusKey,
    );
    for (const el of origins) el.closest("details")?.setAttribute("open", "");
    const origin = origins.find((el) => el.getClientRects().length > 0);
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
  const entry = useRef("");
  const pendingTimer = useRef<ReturnType<typeof setTimeout>>(undefined);
  const [message, setMessage] = useState("");
  const [pendingFrom, setPendingFrom] = useState<string | null>(null);
  const current = search ? `${pathname}?${search}` : pathname;

  useEffect(() => {
    const clearPending = () => {
      clearTimeout(pendingTimer.current);
      document.getElementById("main-content")?.removeAttribute("aria-busy");
      setPendingFrom(null);
    };
    const onPop = () => {
      clearPending();
      // The URL has already changed; focus and scroll still belong to the page being left.
      if (entry.current) navigation.depart(entry.current, { focusKey: currentFocusKey(), scrollY: window.scrollY });
      const key = entryKey();
      navigation.set("pop");
      entry.current = key;
      // A fragment-only step renders nothing, so the kind must not linger.
      setTimeout(() => {
        if (entryKey() === key && navigation.kind() === "pop") navigation.set(null);
      }, 1000);
    };
    const onClick = (event: MouseEvent) => {
      if (event.defaultPrevented || event.button !== 0 || event.metaKey || event.ctrlKey || event.shiftKey || event.altKey) return;
      const link = event.target instanceof Element ? event.target.closest("a") : null;
      if (!link || link.origin !== window.location.origin || link.target) return;
      clearPending();
      const key = locationKey();
      if (link.pathname + link.search === key) {
        navigation.set(null);
        const id = decodeURIComponent(link.hash.slice(1));
        if (id) nextFrames(() => focusTarget(document.getElementById(id)));
        return;
      }
      const focusKey = link.closest<HTMLElement>("[data-focus-key]")?.dataset.focusKey ?? null;
      navigation.depart(entryKey(), { focusKey, scrollY: window.scrollY });
      navigation.set("push");
      pendingTimer.current = setTimeout(() => {
        document.getElementById("main-content")?.setAttribute("aria-busy", "true");
        setPendingFrom(key);
      }, PENDING_AFTER_MS);
    };
    window.addEventListener("popstate", onPop, true);
    document.addEventListener("click", onClick, true);
    return () => {
      window.removeEventListener("popstate", onPop, true);
      document.removeEventListener("click", onClick, true);
      clearTimeout(pendingTimer.current);
    };
  }, []);

  useEffect(() => {
    clearTimeout(pendingTimer.current);
    document.getElementById("main-content")?.removeAttribute("aria-busy");
    entry.current = entryKey();

    // The framework announcer would repeat the heading that receives focus below.
    document.querySelector("next-route-announcer")?.setAttribute("aria-hidden", "true");

    // Only /explore reads query parameters; elsewhere they are dropped without a request.
    // Deferred so that the router's own history patch is already installed.
    const strip = setTimeout(() => {
      if (pathname !== "/explore" && window.location.search) {
        window.history.replaceState(null, "", window.location.pathname + window.location.hash);
      }
    }, 0);

    const kind = first.current ? null : navigation.kind();
    first.current = false;
    navigation.set(null);
    if (kind === "push") nextFrames(focusForward);
    if (kind === "pop") nextFrames(() => setMessage(restore(entry.current)));
    return () => clearTimeout(strip);
  }, [pathname, search]);

  return (
    <>
      <p className="sr-only" role="status">
        {message}
      </p>
      <p className="route-pending" role="status" data-route-pending>
        {pendingFrom === current ? "Opening the next page" : ""}
      </p>
    </>
  );
}
