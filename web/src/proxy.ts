import { NextResponse, type NextRequest } from "next/server";

/** Owned static files. A missing one still falls through to the HTML 404, so it keeps the policy. */
const OWNED_ASSET = /^\/(?:studies\/[a-z-]+\.svg|icon\.svg)$/;

const decodes = (pathname: string) => {
  try {
    decodeURIComponent(pathname);
    return true;
  } catch {
    return false;
  }
};

/**
 * Per-response nonce CSP and no-store delivery (Luxury_Docker_Runtime_Proposal).
 * The development branch is loopback-only and is removed from production builds.
 */
export function proxy(request: NextRequest) {
  const nonce = btoa(String.fromCharCode(...crypto.getRandomValues(new Uint8Array(18))));
  const dev = process.env.NODE_ENV === "development";
  const { pathname } = request.nextUrl;

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

  const answer = () => {
    // The optimizer is unused. Refusing it here keeps its handler, and its disk cache, unreachable.
    if (pathname.startsWith("/_next/image")) return new NextResponse(null, { status: 404 });
    // An address that cannot be decoded is served the unavailable view by a path no route uses.
    if (!decodes(pathname)) return NextResponse.rewrite(new URL("/unavailable", request.url), { request: { headers } });
    // Redirected here, not by the framework, so that the response carries the headers below.
    if (pathname !== "/" && pathname.endsWith("/")) {
      const url = new URL(request.url);
      // One leading slash only: "//host" would name another origin.
      url.pathname = `/${pathname.replace(/^[/\\]+|\/+$/g, "")}`;
      return NextResponse.redirect(url, 308);
    }
    return NextResponse.next({ request: { headers } });
  };
  const response = answer();
  response.headers.set("Content-Security-Policy", policy);
  response.headers.set("X-Robots-Tag", "noindex, nofollow");
  if (!OWNED_ASSET.test(pathname)) response.headers.set("Cache-Control", "private, no-store, max-age=0");
  return response;
}

export const config = {
  // Only hashed framework assets bypass the proxy; their 404 is plain text.
  matcher: ["/((?!_next/static/).*)"],
};
