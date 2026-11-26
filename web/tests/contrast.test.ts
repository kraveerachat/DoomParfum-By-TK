import assert from "node:assert/strict";
import { readFileSync } from "node:fs";
import { join } from "node:path";
import { test } from "node:test";

const css = readFileSync(join(import.meta.dirname, "../src/app/globals.css"), "utf8");
const token = (name: string) => {
  const hex = new RegExp(`--color-${name}:\\s*(#[0-9a-f]{6});`, "i").exec(css)?.[1];
  assert.ok(hex, `token ${name}`);
  return [1, 3, 5].map((i) => parseInt(hex.slice(i, i + 2), 16));
};
const luminance = (rgb: readonly number[]) => {
  const [r, g, b] = rgb.map((v) => (v / 255 <= 0.04045 ? v / 255 / 12.92 : ((v / 255 + 0.055) / 1.055) ** 2.4));
  return 0.2126 * r! + 0.7152 * g! + 0.0722 * b!;
};
const ratio = (a: readonly number[], b: readonly number[]) => {
  const [hi, lo] = [luminance(a), luminance(b)].sort((x, y) => y - x);
  return (hi! + 0.05) / (lo! + 0.05);
};
const mix = (over: readonly number[], under: readonly number[], alpha: number) =>
  over.map((v, i) => v * alpha + under[i]! * (1 - alpha));

// DPT-PLAN-012 values as amended by DPT-PLAN-013 3.1 (PR #37): divider darker; gold and gold-readable are
// now aliases of gold-500 and bronze-700; the gold–bronze scale is added. Every other value is unchanged.
const APPROVED: Record<string, string> = {
  paper: "#f7f5f0", surface: "#ffffff", "surface-muted": "#eeeae2", ink: "#161719", "text-secondary": "#5c5a55",
  gold: "#a8875a", "gold-readable": "#7a5c33", navy: "#14253d", "on-dark": "#f7f5f0", divider: "#d6cfc2",
  "control-border": "#817b70", focus: "#14253d", error: "#9a302c", success: "#365e47",
  "gold-50": "#f3ecdf", "gold-300": "#d2be98", "gold-500": "#a8875a", "bronze-700": "#7a5c33",
  "tobacco-900": "#3b2c1e", "gold-on-navy": "#c9a96e",
};

test("tokens equal the approved values (DPT-PLAN-012 as amended by DPT-PLAN-013)", () => {
  for (const [name, hex] of Object.entries(APPROVED)) {
    assert.match(css.toLowerCase(), new RegExp(`--color-${name}: ${hex};`), name);
  }
});

const text: readonly (readonly [string, string])[] = [
  ["ink", "paper"], ["ink", "surface"], ["ink", "surface-muted"],
  ["text-secondary", "paper"], ["text-secondary", "surface"], ["text-secondary", "surface-muted"],
  ["gold-readable", "paper"], ["on-dark", "ink"], ["on-dark", "navy"], ["error", "paper"], ["success", "paper"],
  ["bronze-700", "paper"], ["bronze-700", "surface"], ["bronze-700", "surface-muted"], ["bronze-700", "gold-50"],
  ["tobacco-900", "paper"], ["gold-on-navy", "navy"], ["ink", "gold-50"], ["text-secondary", "gold-50"],
];
for (const [fg, bg] of text) {
  test(`text ${fg} on ${bg} is at least 4.5:1`, () => assert.ok(ratio(token(fg), token(bg)) >= 4.5, `${ratio(token(fg), token(bg))}`));
}
const indicators: readonly (readonly [string, string])[] = [
  ["control-border", "paper"], ["control-border", "surface"], ["focus", "paper"], ["focus", "surface"],
  ["focus", "surface-muted"], ["on-dark", "navy"], ["on-dark", "ink"], ["ink", "paper"],
  ["control-border", "gold-50"], ["focus", "gold-50"], ["ink", "gold-50"],
];
for (const [fg, bg] of indicators) {
  test(`indicator ${fg} on ${bg} is at least 3:1`, () => assert.ok(ratio(token(fg), token(bg)) >= 3));
}

test("folio text stays readable even while a layer is armed at 70 percent", () => {
  assert.match(css, /\.folio-layer\[data-armed\] \{\s*opacity: 0\.7;/);
  assert.ok(ratio(mix(token("on-dark"), token("navy"), 0.7), token("navy")) >= 4.5);
});

test("the composed scrim separates dialogs from the page", () => {
  const backdrop = mix(token("ink"), token("paper"), 0.5);
  assert.ok(ratio(token("surface"), backdrop) >= 3, `${ratio(token("surface"), backdrop)}`);
});

test("gold and divider are never used as text colors", () => {
  assert.doesNotMatch(css, /[^-]color: var\(--color-(gold|divider|gold-50|gold-300|gold-500)\)/);
});

test("decorative gold stays decoration: below 3:1 where it must not carry state", () => {
  // gold-500 is under 3:1 on surface-muted and gold-50, so it may never be the only indicator there.
  assert.ok(ratio(token("gold-500"), token("surface-muted")) < 3);
  assert.ok(ratio(token("gold-500"), token("paper")) >= 3);
  // Bronze and tobacco are never on navy; gold-on-navy is never on paper.
  assert.ok(ratio(token("bronze-700"), token("navy")) < 3);
  assert.ok(ratio(token("gold-on-navy"), token("paper")) < 3);
});

test("no gold-tinted text class is used outside the readable roles", () => {
  const sources = readFileSync(join(import.meta.dirname, "../src/views/home.tsx"), "utf8");
  assert.doesNotMatch(sources, /\btext-(gold-50|gold-300|gold-500)\b/);
});
