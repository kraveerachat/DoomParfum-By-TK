import type { NextConfig } from "next";

// Docker Desktop bind mounts do not always deliver file events. The dev Compose
// file opts in to bounded polling; preview builds never set this variable.
const poll = Number(process.env.WEB_DEV_POLL_MS ?? 0);

const config: NextConfig = {
  output: "standalone",
  outputFileTracingRoot: import.meta.dirname,
  turbopack: { root: import.meta.dirname },
  poweredByHeader: false,
  reactStrictMode: true,
  productionBrowserSourceMaps: false,
  images: { unoptimized: true },
  // Keep title and robots metadata in the initial <head> for every client.
  htmlLimitedBots: /.*/,
  ...(poll > 0 ? { watchOptions: { pollIntervalMs: poll } } : {}),
  async headers() {
    return [
      {
        source: "/:path*",
        headers: [
          { key: "X-Robots-Tag", value: "noindex, nofollow" },
          { key: "X-Content-Type-Options", value: "nosniff" },
          { key: "Referrer-Policy", value: "same-origin" },
          { key: "Permissions-Policy", value: "camera=(), microphone=(), geolocation=(), browsing-topics=()" },
          { key: "Cross-Origin-Opener-Policy", value: "same-origin" },
        ],
      },
    ];
  },
};

export default config;
