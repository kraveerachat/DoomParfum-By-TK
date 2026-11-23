"use client";

import "./globals.css";

export default function GlobalError({ reset }: { error: Error; reset: () => void }) {
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
            <button type="button" className="button-primary mt-8" onClick={reset}>
              Retry
            </button>
          </div>
        </main>
      </body>
    </html>
  );
}
