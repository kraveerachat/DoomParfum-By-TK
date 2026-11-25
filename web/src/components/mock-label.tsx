/** Persistent disclosures. They are never dismissible and never depend on hover. */
export function SyntheticNotice() {
  return (
    <p className="wrap text-meta text-text-secondary pt-4" data-synthetic-notice>
      Synthetic mock study. Nothing here describes a real fragrance.
    </p>
  );
}

export function MockMarker() {
  return (
    <span
      className="border-control-border text-meta rounded-button inline-block border px-2 py-0.5 font-medium"
      data-mock-marker
    >
      Mock
    </span>
  );
}
