"use client";

import { usePathname } from "next/navigation";
import { createContext, useCallback, useContext, useEffect, useMemo, useRef, useState, type ReactNode } from "react";
import type { Entry } from "@/fixtures/view-model";
import { navigation } from "./navigation-memory";
import { MenuDialog } from "./menu-dialog";
import { ProfileDialog } from "./profile-dialog";
import { SearchDialog } from "./search-dialog";

export type OverlayName = "menu" | "search" | "profile";
type OverlayContext = { readonly active: OverlayName | null; readonly open: (name: OverlayName, trigger: HTMLElement) => void };

const Context = createContext<OverlayContext>({ active: null, open: () => undefined });
export const useOverlay = () => useContext(Context);

const reducedMotion = () => window.matchMedia("(prefers-reduced-motion: reduce)").matches;

/** Fades a detached, inert copy of the closing panel so that closing itself is immediate. */
function fadeOutCopy() {
  const panel = document.querySelector<HTMLElement>("[data-panel]");
  if (!panel || reducedMotion()) return;
  const copy = panel.cloneNode(true) as HTMLElement;
  copy.removeAttribute("data-panel");
  copy.removeAttribute("role");
  copy.removeAttribute("id");
  copy.querySelectorAll("[id]").forEach((el) => el.removeAttribute("id"));
  copy.setAttribute("data-panel-copy", "");
  copy.setAttribute("aria-hidden", "true");
  copy.inert = true;
  document.body.append(copy);
  const drawer = copy.classList.contains("panel-drawer");
  const frames = drawer ? { opacity: [1, 0], transform: ["none", "translateX(-24px)"] } : { opacity: [1, 0] };
  copy.getAnimations().forEach((animation) => animation.cancel());
  copy.animate(frames, { duration: drawer ? 180 : 160, easing: "ease-in" }).finished.then(
    () => copy.remove(),
    () => copy.remove(),
  );
}
const dropCopies = () => document.querySelectorAll("[data-panel-copy]").forEach((el) => el.remove());

export function OverlayProvider({ entries, children }: { entries: readonly Entry[]; children: ReactNode }) {
  const [active, setActive] = useState<OverlayName | null>(null);
  const trigger = useRef<HTMLElement | null>(null);
  const restoreFocus = useRef(true);
  const pathname = usePathname();

  const open = useCallback((name: OverlayName, opener: HTMLElement) => {
    dropCopies();
    // Named explicitly: some browsers do not focus a button that is clicked.
    trigger.current = opener;
    restoreFocus.current = true;
    setActive(name);
  }, []);

  const close = useCallback((returnFocus = true) => {
    fadeOutCopy();
    restoreFocus.current = returnFocus;
    setActive(null);
  }, []);

  useEffect(() => {
    document.documentElement.toggleAttribute("data-overlay", active !== null);
    if (active !== null) return;
    // The frame is interactive again before focus returns; no animation is awaited.
    if (trigger.current && restoreFocus.current) {
      const fallback = document.querySelector<HTMLElement>("header [data-focus-key='brand']");
      const target = trigger.current.getClientRects().length ? trigger.current : fallback;
      target?.focus({ preventScroll: true });
    }
    trigger.current = null;
  }, [active]);

  // No overlay survives a route change, including Back and Forward.
  const [lastPath, setLastPath] = useState(pathname);
  if (lastPath !== pathname) {
    setLastPath(pathname);
    if (active !== null) setActive(null);
  }
  useEffect(() => {
    const onPop = () => {
      restoreFocus.current = false;
      setActive(null);
    };
    window.addEventListener("popstate", onPop);
    return () => window.removeEventListener("popstate", onPop);
  }, []);

  const value = useMemo(() => ({ active, open }), [active, open]);
  const dialog = (name: OverlayName) => ({
    open: active === name,
    onClose: () => close(),
    onNavigate: () => close(navigation.kind() !== "push"),
  });

  return (
    <Context value={value}>
      <div inert={active !== null}>{children}</div>
      <div className="scrim" aria-hidden="true" />
      <MenuDialog {...dialog("menu")} />
      <SearchDialog {...dialog("search")} entries={entries} />
      <ProfileDialog {...dialog("profile")} />
    </Context>
  );
}
