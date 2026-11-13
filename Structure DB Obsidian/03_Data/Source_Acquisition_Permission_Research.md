---
id: DPT-PLAN-006-SOURCES
project: DoomParfum By TK
type: research
status: proposed
owner: human-owner
updated: 2026-11-13
tags: [doomparfum, sources, permissions, workstream-g]
source_of_truth: "../../README.md"
---

# Incremental source permission research

Research as of 2026-11-13. These are candidate assessments, not new permissions or legal approval.
Only public documentation was read in this lane. No API catalogue payload, product scrape, image,
bulk export, paid subscription, authentication or publisher contact was performed. The local pinned
source already exists outside Git; its separate rights and hashes remain authoritative for that
snapshot. Public visibility, no API key and an accessible URL do not confer all reuse rights.

## Candidate and operation matrix

In this table, **conditional** means a documented licensing path whose asset/field/use obligations
still require verification. **Unknown** means evidence is insufficient, never permission. All new
adapters and source-specific intake remain **PROPOSED / PLANNING GATE NOT MERGED**.

| Candidate | Fields / fit | Automation and storage | Display / redistribution / updates | Gate and recommendation |
|---|---|---|---|---|
| Existing pinned Scento Git dataset | perfume/house/material claims; exact snapshot 1479/160/420, not current marketing counts | existing local approval applies to revision086769ecf1add770ea6646bd4d88d39f0e7cddeb with CC BY4.0 attribution | local use approved; the operator rights row still restricts redistribution; no automatic publication, image or newer-revision approval | continue verifying the pinned package; no new download/promotion in this plan |
| Scento live reference API | documented perfume/house/material/family and structural-neighbour responses; vendor taxonomy and model outputs require separate review | documented keyless read-only lookup; wholesale competing-catalogue copying prohibited; persistent bulk replication not approved | cite/link requirements and exact proposed storage/display/update use need scope review; no general media grant found | low priority for bulk coverage; request a specific permitted use before any adapter; never merge neighbour scores with our fit or Dupe evidence |
| Wikidata structured data | identifiers/brand links/possible country claims; perfume coverage and exact edition links unknown | structured entity data CC0; official access methods and responsible request limits apply; user-agent and429/backoff required | structured-data reuse path documented; preserve revision/provenance; linked images/text have independent rights | candidate bounded identifier audit after planning approval; not proof of pyramid, family, stock or completeness |
| Wikimedia Commons | potential ingredient illustrations or bottle photos; per-file eligibility unknown | per-file license, authorship and upstream provenance must permit download/storage | attribution, modifications and share-alike depend on each file; trademark/personality restrictions may remain; updates/replacement require revalidation | no image intake until exact file/revision/asset rights and task approval; existing15 candidates remain blocked |
| Open Beauty Facts / Product Opener | possible barcode, packaging and cosmetic metadata; fragrance-note and edition coverage unmeasured | official docs describe beauty deployment; database/contents/image licenses differ; current deployment-specific full terms not verified | ODbL/DbCL/CC BY-SA obligations and combination/publication impact need review; ingredient labels are not olfactory pyramids | research candidate only; no API/data/image acquisition; do not infer beauty-instance permission from food docs alone |
| GS1 US Data Hub licensed APIs/feed | GTIN/product/brand identifiers; not a claimed note/accord or scent-similarity source | subscription/API entitlement and authenticated contract required; no account or fee authorized | storage/display/redistribution/update conditions require actual current contract review | deferred paid/credential lane; Owner must approve cost, account and exact licensed use separately |
| Manufacturer or authorized publisher feed | potential exact edition/lifecycle/notes and licensed bottle media; no usable feed established | public website terms do not supply an automated feed grant; written field/use permission required | explicitly negotiate storage, private/public display, derivatives, redistribution, update/deletion and attribution | prioritize permission/sample request preparation for regional gaps; no contact sent or new permission assumed |
| Owner-created media / manual private records | own photos or commissioned ingredient illustrations and user shopping bookmarks | actual authorship, third-party rights and private scope must be established; no bulk extraction implied | separate Owner consent and asset grant; personal/private records must not inherit public catalogue visibility | possible future small intake task after approved plan and evidence; purchase receipt alone is not image copyright permission |

## Verified primary references and limitations

**Pinned dataset:** [exact revision](https://github.com/Scento-com/perfume-dataset/tree/086769ecf1add770ea6646bd4d88d39f0e7cddeb).
Retain its LICENSE, attribution to Scento and origin link, revision, file hashes and transformation
notice. CC BY attribution includes credit, license link and indicated changes; do not suggest
endorsement. Dataset licensing does not transfer rights to unrelated website images. The exact
rights row in the existing private pilot is more restrictive than a theoretical redistribution
capability of the license; this planning task does not amend it.

**Live API is a different contract:** [official API guide](https://www.scento.com/developers/perfume-api)
describes anonymous read-only access and several reference endpoints. Its FAQ points to
[Terms of Service section22](https://www.scento.com/terms-of-service#perfume-api), last updated
2026-11-05. Those terms allow lookup/tools, prohibit overload, limit evasion and wholesale copying
to reconstruct a competing catalogue, disclaim accuracy/availability and forbid implied house
endorsement. The guide requests reasonable rates and caching; that is not a perpetual bulk archive,
redistribution or media grant. Recommendation: do not use the live service to fill our entire
catalogue without a specifically compatible permission. No current numerical rate limit is adopted.

**Wikidata:** [licensing](https://www.wikidata.org/wiki/Wikidata:Licensing) distinguishes CC0
structured namespaces from other text. [Data access](https://www.wikidata.org/wiki/Wikidata:Data_access)
documents APIs/dumps and responsible access. Treat identifiers and country assertions as claims,
not an edition merge instruction or evidence of a brand's market availability. The linked
Wikimedia Foundation API-usage page failed to open in this session; its full current terms remain
NOT VERIFIED. No live entity/SPARQL query or dump was fetched.

**Commons:** [reuse guidance](https://commons.wikimedia.org/wiki/Commons:Contact_us/Reuse) and
[per-file licensing guidance](https://commons.wikimedia.org/wiki/Commons:Licensing) require checking
the actual file. A page revision binding or search thumbnail does not prove permission for its
binary, derivative or our publication. No new file-page or asset acquisition ran in this lane.

**Open Beauty Facts:** [official deployment documentation](https://openfoodfacts.github.io/openfoodfacts-server/api/tutorials/scanning-cosmetics-pet-food-and-other-products/)
describes cosmetics separately and currently lists some cross-project features as unsupported.
[General API documentation](https://openfoodfacts.github.io/openfoodfacts-server/api/) and
[license guidance](https://openfoodfacts.github.io/openfoodfacts-server/api/tutorials/license-be-on-the-legal-side/)
distinguish database ODbL, contents DbCL and image CC BY-SA, with possible other image rights.
The beauty data page returned a crawler restriction; it was not retried through another method.
The current beauty-instance-specific full terms and usable fragrance sample remain unresolved.
Do not plan seller-price coverage from a feature the beauty deployment does not support.

**First-party boundary:** [Lattafa's terms](https://lattafa.com/terms-conditions/) provide no located
third-party automation or asset-reuse license. That is a limited evidence statement, not a legal
finding that no license could be obtained. Brand websites and reseller sites must be distinguished;
neither source visibility nor a retailer's inventory grants manufacturer copyright. No product
pages or assets were scraped. No verified regional licensed sample was obtained.

**Licensed identifiers:** [GS1 US APIs](https://www.gs1us.org/tools/gs1-us-data-hub/gs1-us-apis)
describe subscription/API entitlements. Current contractual use rights, costs and credentials have
not been accepted or obtained. A historical2022 agreement is not treated as a current grant.

## Permission dossier required before intake

For every proposed source/version record: publisher and actual rights holder; exact product/edition
and field/sample; retrieval method/limits and terms date/hash; operation decisions for automation,
storage, display, cache, redistribution, derivatives and updates; audience/territory/expiry/revocation;
attribution; permitted binary formats/size; cost/account requirements; written evidence locator and
reviewer. Unknown fields stay unknown. A new publication use needs separate approval even if local
storage was already permitted. A changed page is retained as a new evidence version, never rewritten.

No Fragrantica or Shopee scraping, endpoint replay, anti-bot circumvention or private account access
is proposed. Pairwise reports require their own exact claim, identity/edition, rights and reviewer;
vendor neighbours, shared notes, seller keywords and review counts cannot become measured smell
similarity or independently verified Dupe relationships.
