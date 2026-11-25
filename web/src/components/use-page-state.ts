"use client";

import { useSearchParams } from "next/navigation";
import { useEffect, useState, type Dispatch, type SetStateAction } from "react";
import { entryKey, navigation } from "./navigation-memory";

/**
 * Page state kept per history entry in memory. A fresh visit starts from `initial`, including a
 * visit that only changes the query string of the current path; Back and Forward restore it.
 */
export function usePageState<T>(initial: T): [T, Dispatch<SetStateAction<T>>] {
  const search = useSearchParams().toString();
  const [state, setState] = useState<T>(() => navigation.restorePage(initial));
  const [lastSearch, setLastSearch] = useState(search);

  if (lastSearch !== search) {
    setLastSearch(search);
    // A filter change made on the page itself has no navigation kind and keeps its state.
    if (navigation.kind() !== null) setState(navigation.restorePage(initial));
  }

  useEffect(() => {
    navigation.savePage(entryKey(), state);
  }, [state, search]);

  return [state, setState];
}
