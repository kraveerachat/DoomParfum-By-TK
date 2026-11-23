import { fixtures } from "../src/fixtures/data.ts";
import { validateFixtures } from "../src/fixtures/validate.ts";

const errors = validateFixtures(fixtures);
if (errors.length) {
  console.error(`Synthetic fixtures rejected:\n- ${errors.join("\n- ")}`);
  process.exit(1);
}
console.log(
  `Synthetic fixtures valid: ${fixtures.perfumes.length} studies, ${fixtures.notes.length} notes, ` +
    `${fixtures.families.length} families, ${fixtures.accords.length} accords, ${fixtures.articles.length} articles.`,
);
