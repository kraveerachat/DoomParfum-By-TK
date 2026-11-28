import "server-only";
import type { Locale } from "../i18n/locale.ts";
import { fixtures } from "../fixtures/data.ts";
import { thaiOverlay } from "../fixtures/th.ts";
import { assertFixtures } from "../fixtures/validate.ts";
import { assertOverlay } from "../fixtures/validate-overlay.ts";
import { buildArticles, buildCatalogue } from "../fixtures/view-model.ts";

export const fixtureSet = assertFixtures(fixtures);
/** Server-only: Thai prose never enters an immutable client chunk. */
export const overlay = assertOverlay(thaiOverlay, fixtureSet);
export const catalogue = buildCatalogue(fixtureSet, "en", overlay);

const views = { en: catalogue, th: buildCatalogue(fixtureSet, "th", overlay) } as const;
const articleViews = { en: buildArticles(fixtureSet), th: buildArticles(fixtureSet, "th", overlay) } as const;

export const catalogueFor = (locale: Locale) => views[locale];
export const articlesFor = (locale: Locale) => articleViews[locale];
