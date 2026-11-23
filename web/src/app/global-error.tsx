"use client";

import "./globals.css";

export default function GlobalError({ retry }: { error: Error; retry: () => void }) {
  return (
    <html lang="en">
      <head>
        <title>Unavailable · DoomParfum By TK</title>
        <meta name="robots" content="noindex, nofollow" />
      </head>
      <body>
        <main className="page-container">
          <div className="wrap pt-20" role="alert">
            <h1 className="type-page">This mock could not be shown</h1>
            <p className="measure mt-4">The local app failed to render. No data was sent anywhere.</p>
            <div className="mt-8 flex flex-wrap items-center gap-x-6 gap-y-3">
              <button type="button" className="button-primary" onClick={retry}>
                Retry
              </button>
              {/* A full load: the client router is part of what failed. */}
              <a href="/explore" className="link-action">
                Return to Explore
              </a>
            </div>
          </div>
        </main>
      </body>
    </html>
  );
}
