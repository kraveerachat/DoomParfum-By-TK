/** Fixture field states. `unknown` and an authored empty list are different facts. */
export type Known<T> = { readonly state: "known"; readonly value: T };
export type Unknown = { readonly state: "unknown" };
export type Unavailable = { readonly state: "unavailable" };
export type Field<T> = Known<T> | Unknown;
export type VisualField = Known<string> | Unavailable;

export type Provenance = {
  readonly kind: "locally_authored_fixture";
  readonly fixtureVersion: string;
  readonly authoredFor: string;
};

type Marked = {
  readonly synthetic: true;
  readonly rights: "project_owned_synthetic";
  readonly provenance: Provenance;
};

export type FamilyFixture = Marked & { readonly id: string; readonly label: string; readonly descriptor: string };
export type AccordFixture = Marked & { readonly id: string; readonly label: string };
export type NoteFixture = Marked & {
  readonly id: string;
  readonly label: string;
  readonly descriptor: string;
  readonly family: Field<string>;
};

export type PerfumeFixture = Marked & {
  readonly id: string;
  readonly slug: string;
  readonly name: string;
  readonly houseLabel: string;
  readonly description: Field<string>;
  readonly family: Field<string>;
  readonly top: Field<readonly string[]>;
  readonly heart: Field<readonly string[]>;
  readonly base: Field<readonly string[]>;
  readonly generalNotes: Field<readonly string[]>;
  readonly accords: Field<readonly string[]>;
  readonly visual: VisualField;
};

export type ArticleFixture = Marked & {
  readonly id: string;
  readonly anchor: string;
  readonly title: string;
  readonly excerpt: string;
  readonly body: readonly string[];
};

export type FixtureSet = {
  readonly families: readonly FamilyFixture[];
  readonly accords: readonly AccordFixture[];
  readonly notes: readonly NoteFixture[];
  readonly perfumes: readonly PerfumeFixture[];
  readonly articles: readonly ArticleFixture[];
  readonly featured: readonly string[];
};
