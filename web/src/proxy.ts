import { NextResponse, type NextRequest } from "next/server";

/**
 * Per-response nonce CSP and no-store delivery (Luxury_Docker_Runtime_Proposal).
 * The development branch is loopback-only and is removed from production builds.
 */
export function proxy(request: NextRequest) {
  const nonce = btoa(String.fromCharCode(...crypto.getRandomValues(new Uint8Array(18))));
  const dev = process.env.NODE_ENV === "development";

  const policy = [
    "default-src 'self'",
    `script-src 'self' 'nonce-${nonce}'${dev ? " 'unsafe-eval'" : ""}`,
    dev ? "style-src 'self' 'unsafe-inline'" : `style-src 'self' 'nonce-${nonce}'`,
    "img-src 'self'",
    "font-src 'self'",
    "media-src 'self'",
    dev ? "connect-src 'self' ws://localhost:3000" : "connect-src 'self'",
    "manifest-src 'self'",
    "worker-src 'none'",
    "object-src 'none'",
    "frame-src 'none'",
    "frame-ancestors 'none'",
    "form-action 'none'",
    "base-uri 'self'",
  ].join("; ");

  const headers = new Headers(request.headers);
  headers.set("x-nonce", nonce);
  headers.set("Content-Security-Policy", policy);

  // The optimizer is unused. Refusing it here keeps its handler, and its disk cache, unreachable.
  const response = request.nextUrl.pathname.startsWith("/_next/image")
    ? new NextResponse(null, { status: 404 })
    : NextResponse.next({ request: { headers } });
  response.headers.set("Content-Security-Policy", policy);
  response.headers.set("Cache-Control", "private, no-store, max-age=0");
  return response;
}

export const config = {
  // Hashed framework assets and owned static studies keep their own caching headers.
  matcher: ["/((?!_next/static|studies/|icon.svg).*)"],
};
