import { request as httpRequest, type IncomingHttpHeaders } from "node:http";
import { test as base, expect, type Page } from "@playwright/test";

export const ORIGIN = process.env.E2E_ORIGIN ?? "http://localhost:3000";

export const ROUTES = [
  { path: "/", title: "Home · DoomParfum By TK" },
  { path: "/explore", title: "Explore mock fragrances · DoomParfum By TK" },
  { path: "/perfume/paper-study-a", title: "Paper study A · Mock study · DoomParfum By TK" },
  { path: "/notes", title: "Notes · DoomParfum By TK" },
  { path: "/about", title: "About · DoomParfum By TK" },
] as const;

/** Every test fails on a console error, page error, CSP violation or cross-origin request. */
export const test = base.extend<{ problems: string[] }>({
  problems: [
    async ({ page }, use) => {
      const problems: string[] = [];
      page.on("console", (m) => {
        if (m.type() === "error" || m.type() === "warning") problems.push(`${m.type()}: ${m.text()}`);
      });
      page.on("pageerror", (e) => problems.push(`pageerror: ${e.message}`));
      page.on("request", (r) => {
        if (new URL(r.url()).origin !== ORIGIN) problems.push(`cross-origin: ${r.url()}`);
      });
      await use(problems);
      expect(problems).toEqual([]);
    },
    { auto: true },
  ],
});

/** Waits for hydration: the client-only status element exists and a click handler is attached. */
export async function ready(page: Page, path: string) {
  await page.goto(path);
  await page.waitForFunction(() => {
    const button = document.querySelector("header button");
    return !!button && Object.keys(button).some((k) => k.startsWith("__reactProps"));
  });
  await page.evaluate(() => document.fonts.ready);
}

/** Sends the exact request target. Browsers and HTTP clients rewrite slashes and escapes first. */
export const raw = (method: string, target: string, extra: Record<string, string> = {}) =>
  new Promise<{ status: number; headers: IncomingHttpHeaders; body: string }>((resolve, reject) => {
    const { hostname, port, host } = new URL(ORIGIN);
    const call = httpRequest({ hostname, port, family: 4, agent: false, method, path: target, headers: { ...extra, host } }, (response) => {
      let body = "";
      response.setEncoding("utf8");
      response.on("data", (part: string) => (body += part));
      response.on("end", () => resolve({ status: response.statusCode ?? 0, headers: response.headers, body }));
    });
    call.on("error", reject);
    call.end();
  });

export const focused = (page: Page) =>
  page.evaluate(() => {
    const el = document.activeElement as HTMLElement | null;
    return el ? (el.dataset.focusKey ?? el.getAttribute("aria-label") ?? el.id ?? "") || el.tagName : "";
  });

export const noOverflow = (page: Page) =>
  page.evaluate(() => {
    const width = document.documentElement.clientWidth;
    const bad = [...document.querySelectorAll<HTMLElement>("body *")]
      .filter((el) => {
        const box = el.getBoundingClientRect();
        if (box.width === 0 || el.closest(".sr-only, [aria-hidden='true'], .panel")) return false;
        return box.right > width + 1 || box.left < -1;
      })
      .map((el) => `${el.tagName}.${el.className} ${Math.round(el.getBoundingClientRect().right)}`);
    return { scroll: document.documentElement.scrollWidth - width, bad: bad.slice(0, 5) };
  });

export { expect };
