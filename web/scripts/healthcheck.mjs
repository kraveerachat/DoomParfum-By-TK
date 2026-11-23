// Container health: an existing route answers inside the container. No extra API route is added.
try {
  const response = await fetch("http://127.0.0.1:3000/about", { signal: AbortSignal.timeout(3000) });
  process.exit(response.status === 200 ? 0 : 1);
} catch {
  process.exit(1);
}
