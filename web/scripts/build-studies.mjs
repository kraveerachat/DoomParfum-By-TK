/**
 * Draws the original abstract studies in public/studies/. Deterministic: flat planes and
 * hairlines only, approved palette only. Run: node scripts/build-studies.mjs
 */
import { mkdirSync, writeFileSync } from "node:fs";
import { join } from "node:path";

const OUT = join(import.meta.dirname, "..", "public", "studies");
const C = {
  paper: "#F7F5F0", muted: "#EEEAE2", sand: "#E4DED2", divider: "#DDD9D0", stone: "#C8C1B3",
  taupe: "#817B70", grey: "#5C5A55", ink: "#161719", gold: "#AD9361", navy: "#14253D", white: "#FFFFFF",
};

const r = (v) => Number(v.toFixed(1));
const range = (count, fn) => Array.from({ length: count }, (_, i) => fn(i, count > 1 ? i / (count - 1) : 0));
const rect = (x, y, w, h, fill, extra = "") => `<rect x="${r(x)}" y="${r(y)}" width="${r(w)}" height="${r(h)}" fill="${fill}" ${extra}/>`;
const poly = (points, fill, extra = "") => `<polygon points="${points.map(([x, y]) => `${r(x)},${r(y)}`).join(" ")}" fill="${fill}" ${extra}/>`;
const circle = (x, y, radius, fill, extra = "") => `<circle cx="${r(x)}" cy="${r(y)}" r="${r(radius)}" fill="${fill}" ${extra}/>`;
const line = (x1, y1, x2, y2) => `M${r(x1)} ${r(y1)}L${r(x2)} ${r(y2)}`;
const trace = (points) => `M${points.map(([x, y]) => `${r(x)} ${r(y)}`).join("L")}`;
const strokes = (paths, color, width = 1, extra = "") => `<path d="${paths.join("")}" fill="none" stroke="${color}" stroke-width="${width}" ${extra}/>`;
const bump = (x, centre, spread) => Math.exp(-((x - centre) ** 2) / (2 * spread ** 2));
const svg = (w, h, body) => `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 ${w} ${h}" width="${w}" height="${h}" fill="none">\n${body.join("\n")}\n</svg>\n`;

const W = 800;
const H = 1000;
const plate = (body) => svg(W, H, body);
const studies = {};

/* Bright: edges, rims, thin light ------------------------------------------------ */
studies["glass-g"] = plate([
  rect(0, 0, W, H, C.muted),
  strokes(range(46, (i) => line(520 - 470 * (i / 45) ** 1.9, 0, 520 - 470 * (i / 45) ** 1.9, H)), C.taupe, 1),
  poly([[520, 90], [612, 40], [612, 960], [520, 910]], C.paper),
  poly([[612, 40], [626, 46], [626, 966], [612, 960]], C.ink),
  strokes([line(520, 90, 520, 910)], C.ink, 1.5),
]);

{
  const clip = `<clipPath id="lens"><circle cx="330" cy="470" r="262"/></clipPath>`;
  studies["glass-h"] = plate([
    rect(0, 0, W, H, C.sand),
    `<defs>${clip}</defs>`,
    circle(330, 470, 262, C.paper),
    strokes(range(34, (i) => `M${r(548 - (262 - i * 7.6))} 590a${r(262 - i * 7.6)} ${r(262 - i * 7.6)} 0 1 0 ${r(2 * (262 - i * 7.6))} 0a${r(262 - i * 7.6)} ${r(262 - i * 7.6)} 0 1 0 ${r(-2 * (262 - i * 7.6))} 0`), C.grey, 1),
    `<g clip-path="url(#lens)">${circle(548, 590, 262, C.ink)}${strokes(range(34, (i) => `M${r(548 - (262 - i * 7.6))} 590a${r(262 - i * 7.6)} ${r(262 - i * 7.6)} 0 1 0 ${r(2 * (262 - i * 7.6))} 0a${r(262 - i * 7.6)} ${r(262 - i * 7.6)} 0 1 0 ${r(-2 * (262 - i * 7.6))} 0`), C.paper, 1)}</g>`,
    circle(330, 470, 262, "none", `stroke="${C.ink}" stroke-width="1.5"`),
  ]);
}

studies["glass-i"] = plate([
  rect(0, 0, W, H, C.muted),
  ...range(3, (i) => {
    const cy = 330 + i * 260;
    const fill = [C.paper, C.stone, C.ink][i];
    const cx = 400 + [-60, 40, -20][i];
    const arcs = range(13, (j) => `M${r(cx - 210 + j * 16)} ${cy}a${r(210 - j * 16)} ${r(210 - j * 16)} 0 0 1 ${r(2 * (210 - j * 16))} 0`);
    return `<path d="M${cx - 210} ${cy}a210 210 0 0 1 420 0z" fill="${fill}"/>${strokes(arcs, i === 2 ? C.paper : C.grey, 1)}`;
  }),
  strokes(range(3, (i) => line(0, 330 + i * 260, W, 330 + i * 260)), C.ink, 1.5),
]);

/* Soft: folds, threads, slow curves ---------------------------------------------- */
studies["linen-d"] = plate([
  rect(0, 0, W, H, C.sand),
  poly([[0, 0], [300, 0], [430, H], [0, H]], C.paper),
  poly([[300, 0], [520, 0], [610, H], [430, H]], C.divider),
  poly([[520, 0], [W, 0], [W, H], [610, H]], C.muted),
  strokes(range(58, (i) => {
    const y = 10 + i * 18;
    const f = y / H;
    return trace([[0, y - 70], [300 + 130 * f, y + 18], [520 + 90 * f, y - 46], [W, y + 30]]);
  }), C.taupe, 1),
  strokes([line(300, 0, 430, H)], C.ink, 1.5),
]);

{
  const warpX = (x, y) => x + 46 * Math.sin(y / 170 + x / 420) + 30 * bump(y, 520, 190) * Math.sin(x / 120);
  const warpY = (x, y) => y + 40 * Math.sin(x / 210 - y / 500);
  studies["linen-e"] = plate([
    rect(0, 0, W, H, C.muted),
    strokes(range(38, (i) => trace(range(51, (j) => [warpX(-60 + i * 25, -20 + j * 21), warpY(-60 + i * 25, -20 + j * 21)]))), C.grey, 1),
    strokes(range(46, (i) => trace(range(45, (j) => [warpX(-60 + j * 21, -40 + i * 24), warpY(-60 + j * 21, -40 + i * 24)]))), C.stone, 1),
    poly([[0, 742], [W, 596], [W, H], [0, H]], C.stone),
    strokes([line(0, 742, W, 596)], C.ink, 1.5),
  ]);
}

studies["linen-f"] = plate([
  rect(0, 0, W, H, C.sand),
  strokes(range(64, (i, t) => trace(range(60, (j, s) => [
    -60 + 940 * s + 80 * Math.sin(s * 2.4 + t * 2.1),
    60 + 760 * t + 190 * Math.sin(s * 3.1 - t * 2.6) * (1 - 0.35 * t),
  ]))), C.grey, 1),
]);

studies["paper-b"] = plate([
  rect(0, 0, W, H, C.divider),
  poly([[150, 190], [470, 120], [470, 800], [150, 870]], C.paper),
  poly([[470, 120], [650, 220], [650, 900], [470, 800]], C.sand),
  strokes(range(22, (i) => line(470 + i * 8.2, 120 + i * 4.6, 470 + i * 8.2, 800 + i * 4.6)), C.taupe, 1),
  strokes([line(470, 120, 470, 800)], C.ink, 1.5),
  strokes([`M150 620A330 330 0 0 1 470 420`], C.ink, 1),
]);

studies["paper-l"] = plate([
  rect(0, 0, W, H, C.sand),
  ...range(10, (i) => `<g transform="rotate(${r(-16 + i * 3.4)} 400 900)"><rect x="240" y="${140 + i * 6}" width="320" height="620" fill="${i % 2 ? C.paper : C.muted}" stroke="${C.taupe}" stroke-width="1"/></g>`),
  strokes([line(120, 900, 680, 900)], C.ink, 1.5),
]);

/* Deep: strata, weight, late ink -------------------------------------------------- */
studies["paper-c"] = plate([
  rect(0, 0, W, H, C.muted),
  poly([[120, 110], [560, 70], [560, 700], [120, 740]], C.paper),
  strokes(range(26, (i) => line(150, 160 + i * 22, 530, 125.5 + i * 22)), C.taupe, 1),
  circle(520, 790, 330, C.ink),
  strokes([line(120, 110, 120, 740)], C.ink, 1.5),
]);

{
  const cut = (y, slope, fill) => poly([[0, y], [W, y + slope], [W, H], [0, H]], fill);
  studies["stone-j"] = plate([
    rect(0, 0, W, H, C.sand),
    strokes(range(15, (i) => line(0, 60 + i * 15, W, 10 + i * 15)), C.taupe, 1),
    cut(300, -50, C.stone),
    cut(452, 96, C.taupe),
    cut(600, 18, C.grey),
    cut(700, -92, C.ink),
    strokes(range(18, (i) => line(0, 722 + i * 17, W, 630 + i * 17)), C.taupe, 1),
  ]);
}

{
  const ring = (t) => `${trace(range(97, (i) => {
    const a = (i / 96) * Math.PI * 2;
    const k = 1 + 0.1 * Math.sin(a * 3 + 0.8 + t * 1.2) + 0.055 * Math.sin(a * 5 - t * 2.2);
    return [400 + 60 * t + Math.cos(a) * 300 * (1 - t) * k, 520 - 70 * t + Math.sin(a) * 350 * (1 - t) * k];
  }))}Z`;
  studies["stone-k"] = plate([
    rect(0, 0, W, H, C.ink),
    `<path d="${ring(0)}" fill="#24262A"/>`,
    strokes(range(26, (i) => ring(i / 27)), C.stone, 1),
  ]);
}

/* Home hero: one field, three planes, hairlines that invert on ink ------------------ */
{
  const w = 1250;
  const h = 1000;
  const contour = (i) => trace(range(50, (j) => {
    const x = j * 25.6;
    const base = 96 + i * 22;
    const lift = 210 * bump(x, 420, 210) * bump(i, 18, 10) + 170 * bump(x, 960, 170) * bump(i, 27, 9);
    return [x, base - lift + 12 * Math.sin(x / 190 + i / 9)];
  }));
  const field = range(42, contour).join("");
  const sheet = "150,120 520,40 520,850 150,930";
  const slab = "640,330 1060,250 1060,1000 640,1000";
  const lines = (color) => `<use href="#field" stroke="${color}"/>`;
  studies.hero = svg(w, h, [
    `<defs><path id="field" d="${field}"/><clipPath id="slab"><polygon points="${slab}"/></clipPath><clipPath id="sheet"><polygon points="${sheet}"/></clipPath></defs>`,
    rect(0, 0, w, h, C.muted),
    circle(700, 400, 340, C.divider),
    lines(C.taupe),
    `<polygon points="${sheet}" fill="${C.paper}"/>`,
    poly([[520, 40], [640, 112], [640, 922], [520, 850]], C.sand),
    `<polygon points="${slab}" fill="${C.ink}"/>`,
    `<g clip-path="url(#slab)">${lines(C.stone)}</g>`,
    `<g clip-path="url(#sheet)">${lines(C.stone)}</g>`,
    strokes([line(150, 120, 150, 930), line(520, 40, 520, 850)], C.ink, 1.5),
    strokes([line(1150, 90, 1150, 1000)], C.gold, 2),
  ]);
}

/* Scent folio: one continuous drawing cut into three equal leaves. Every leaf has the
   same number of lines, so the drawing cannot be read as quantity or strength. */
{
  const w = 800;
  const leaf = 420;
  const N = 24;
  const top = range(N, (i, t) => `M${r(400 - 390 + t * 380)} ${leaf}a${r(390 - t * 380)} ${r(390 - t * 380)} 0 0 1 ${r(2 * (390 - t * 380))} 0`);
  const heart = range(N, (i, t) => trace(range(61, (j, s) => [10 + 780 * s, leaf + (t * leaf) + Math.sin(s * Math.PI) * 130 * (0.5 - t) * 1.4])));
  const base = range(N, (i, t) => trace(range(61, (j, s) => [10 + 780 * s, leaf * 2 + 22 + t * (leaf - 44) + 16 * Math.sin(s * 5 + t * 5) * Math.sin(Math.PI * s)])));
  const body = [strokes(top, C.paper, 1), strokes(heart, C.paper, 1), strokes(base, C.paper, 1)];
  ["top", "heart", "base"].forEach((name, i) => {
    studies[`folio-${name}`] = `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 ${i * leaf} ${w} ${leaf}" width="${w}" height="${leaf}" fill="none">\n${body[i]}\n</svg>\n`;
  });
}

/* Family marks for the Home index --------------------------------------------------- */
const mark = (body) => svg(120, 120, body);
studies["mark-bright"] = mark([strokes(range(14, (i) => line(100 - 84 * (i / 13) ** 1.8, 10, 100 - 84 * (i / 13) ** 1.8, 110)), C.ink, 1)]);
studies["mark-soft"] = mark([strokes(range(14, (i, t) => trace(range(40, (j, s) => [10 + 100 * s, 28 + 64 * t + 18 * Math.sin(s * 3.4 - t * 2)]))), C.ink, 1)]);
studies["mark-deep"] = mark([strokes(range(14, (i) => line(10, 100 - 84 * (i / 13) ** 1.8, 110, 100 - 84 * (i / 13) ** 1.8)), C.ink, 1)]);

mkdirSync(OUT, { recursive: true });
for (const [name, content] of Object.entries(studies)) writeFileSync(join(OUT, `${name}.svg`), content.replace(/ +\/>/g, "/>"));
console.log(Object.entries(studies).map(([name, content]) => `${name} ${(content.length / 1024).toFixed(1)}KiB`).join("\n"));
