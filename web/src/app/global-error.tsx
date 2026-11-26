"use client";

import "./globals.css";

/**
 * The root shell itself failed, so the locale is not dependable here (DPT-PLAN-013 4.2). Both
 * languages are shown, each marked with its own language.
 */
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
            <p lang="th" className="type-section mt-10">
              ไม่สามารถแสดงการจำลองนี้ได้
            </p>
            <p lang="th" className="measure mt-3">
              แอปในเครื่องแสดงผลไม่สำเร็จ ไม่มีข้อมูลถูกส่งออกไปที่ใด
            </p>
            <div className="mt-8 flex flex-wrap items-center gap-x-6 gap-y-3">
              <button type="button" className="button-primary" onClick={retry}>
                Retry · <span lang="th">ลองอีกครั้ง</span>
              </button>
              {/* A full load: the client router is part of what failed. */}
              {/* eslint-disable-next-line @next/next/no-html-link-for-pages -- see above */}
              <a href="/explore" className="link-action">
                Return to Explore
              </a>
              {/* eslint-disable-next-line @next/next/no-html-link-for-pages -- see above */}
              <a href="/th/explore" className="link-action" lang="th">
                กลับไปยังหน้าสำรวจ
              </a>
            </div>
          </div>
        </main>
      </body>
    </html>
  );
}
