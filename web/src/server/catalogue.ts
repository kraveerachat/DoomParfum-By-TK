import "server-only";
import { fixtures } from "../fixtures/data.ts";
import { assertFixtures } from "../fixtures/validate.ts";
import { buildCatalogue } from "../fixtures/view-model.ts";

export const fixtureSet = assertFixtures(fixtures);
export const catalogue = buildCatalogue(fixtureSet);
