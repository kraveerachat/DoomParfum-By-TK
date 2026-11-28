import { NextResponse, type NextRequest } from "next/server";
import { fixtures } from "./fixtures/data.ts";
import { LOCALE_HEADER, localeOf, localize } from "./i18n/locale.ts";

/** Owned static files. A missing one still falls through to the HTML 404, so it keeps the policy. */
const OWNED_ASSET = /^\/(?:studies\/[a-z-]+\.svg|icon\.svg)$/;

/**
 * A path no route uses, in each language. Rewriting here makes the framework answer with
 * app/global-not-found.tsx, the only 404 it renders on the server with a `lang` (IMP-WEB-02 S9,
 * Owner-authorized). The target keeps the language in its path because Next.js 16.4.6 runs this
 * proxy a second time on a rewrite target that matches no route, and that pass derives the locale
 * header again from the target (verified with an instrumented build, S9).
 */
const UNMATCHED = "/_unavailable";

/**
 * A detail address and its slug; only slugs in the fixtures have a page. This must stay the same
 * set the detail view looks up (`fixtureSet` in server/catalogue.ts, the validated `fixtures`):
 * a slug accepted here but missing there would reach notFound() and its error document again.
 */
const DETAIL = /^(?:\/th)?\/perfume\/([^/]+)$/;
const SLUGS = new Set(fixtures.perfumes.map((p) => p.slug));

/** Nothing in this mock accepts a write, so only reads are answered with a page. */
const READS = ["GET", "HEAD"];

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
  // Derived from the path only; this replaces any value the client sent (DPT-PLAN-013 4.2).
  headers.set(LOCALE_HEADER, localeOf(pathname));

  const unavailable = () =>
    NextResponse.rewrite(new URL(localize(localeOf(pathname), UNMATCHED), request.url), { request: { headers } });

  const answer = () => {
    if (!READS.includes(request.method)) return new NextResponse(null, { status: 405, headers: { Allow: READS.join(", ") } });
    // The optimizer is unused. Refusing it here keeps its handler, and its disk cache, unreachable.
    if (pathname.startsWith("/_next/image")) return new NextResponse(null, { status: 404 });
    // An address that cannot be decoded gets the 404 page of its path's language, by a path no route
    // uses, so no route parameter is decoded from it. The "/th" prefix is plain ASCII.
    if (!decodes(pathname)) return unavailable();
    // Redirected here, not by the framework, so that the response carries the headers below.
    if (pathname !== "/" && pathname.endsWith("/")) {
      const url = new URL(request.url);
      // One leading slash only: "//host" would name another origin.
      url.pathname = `/${pathname.replace(/^[/\\]+|\/+$/g, "")}`;
      return NextResponse.redirect(url, 308);
    }
    // An unknown slug would otherwise reach notFound() in the page, which the framework can only send
    // as its error document, without `lang` and empty without scripting (IMP-WEB-02 S7).
    const slug = DETAIL.exec(pathname)?.[1];
    if (slug !== undefined && !SLUGS.has(decodeURIComponent(slug))) return unavailable();
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
