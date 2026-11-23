/** Reserves geometry during a real route transition. It does not animate or simulate progress. */
export function RoutePlaceholder({ title, rows }: { title: string; rows: number }) {
  return (
    <div className="wrap pt-16" aria-busy="true">
      <p className="type-page">{title}</p>
      <p className="mt-4">Opening this page.</p>
      <div aria-hidden="true" className="mt-12 grid grid-cols-1 gap-4 w480:grid-cols-2 w1024:grid-cols-3 w1280:grid-cols-4">
        {Array.from({ length: rows }, (_, i) => (
          <div key={i} className="bg-surface-muted aspect-[4/5]" />
        ))}
      </div>
    </div>
  );
}
