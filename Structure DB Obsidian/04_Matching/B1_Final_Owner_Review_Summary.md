---
id: B1-FINAL-OWNER-REVIEW-1
project: DoomParfum By TK
type: final_owner_contract_review_summary
status: awaiting-exact-owner-approval
owner: human-owner
updated: 2026-11-15
tags: [doomparfum, synthetic, b1, owner-review]
source_of_truth: "../../README.md"
---

# Final Owner Review Summary — B1-PD-TYPED-1

สถานะ: **Contract ผ่าน independent review แต่ยังไม่มี Exact Owner Approval ให้เริ่ม implementation**
Owner ตอบว่า “ยังไม่อนุมัติ implementation” และขอตรวจสรุปฉบับนี้ก่อน การเห็นชอบในหลักการต่อ method,
config, task และ synthetic scope ไม่ถูกนำมาแทนการยอมรับ exact contract/hash นี้
เอกสารนี้สรุปฉบับเดิมโดยไม่แก้ contract และไม่เพิ่มนโยบายใหม่ หากสรุปไม่ครบให้ใช้ contract ฉบับ hash ด้านล่างเป็นหลัก

## 1. Contract, version, hash และตำแหน่ง

| รายการ | ฉบับที่เสนอให้ตรวจรับ |
|---|---|
| Contract ID / version | B1-PD-TYPED-1 |
| Proposal revision | 2; แก้ property wording ก่อน Owner approval ไม่เปลี่ยนสูตร/schema/bounds |
| SHA-256 | 77bfca59dab449313eb02def8c30ff355e341a2b88397dbc412a09af970a5977 |
| ขนาด | 40,403 bytes, UTF-8 LF |
| Method | mc-b1-pyramid-positive-domain-p1 |
| Config / schema | b1-pd-typed-config-1 / b1-pd-typed-schema-1 |
| Implementation task | IMP-MATCH-03 |
| ไฟล์ | Structure DB Obsidian/04_Matching/B1_Positive_Domain_Typed_Contract.md |
| Base / detached preparation HEAD | 604d447e599aa8359d3427dfbfbceaac85373e48 |

ดู [[B1_Positive_Domain_Typed_Contract]] และ [[B1_Exact_Owner_Decision_Batch]]
PR26 ถูก Human Owner merge แล้ว; merge tree ตรงกับ M1 head63cb56c54aacef99fa8937e7a5211acca8ae6a63
ทุกไฟล์ ไม่มีการทำ M1 planning/implementation ซ้ำ และไม่แก้ M1 contracts/tests/receipts

## 2. สูตรที่ยังรออนุมัติ: Coverage80% + Focus20%

สำหรับ positive clauses ที่ normalize แล้ว แต่ละข้อมีน้ำหนักจำนวนเต็ม w_i และ verified match m_i:

```text
Q = Coverage = sum(w_i * m_i) / sum(w_i)
H = Focus = จำนวน distinct matched (note_id, layer) occurrences / |D|
fit = (4/5)Q + (1/5)H
```

ตัวหาร Q รวม required และ optional ทุกข้อ รวม optional ที่ไม่ match; excluded ไม่มี score weight
D รวมทุก membership ใน layer ที่ positive clauses ค้นหาเท่านั้น ไม่เพิ่ม excluded-only layers
แสดง numeric fit ได้เมื่อ required/excluded gates ผ่าน, positive domain ครบ/compatible และ match อย่างน้อย1positive
Q/H เป็น exact Fraction; ไม่ใช่ Data Confidence, measured smell similarity หรือ pairwise evidence
Focus เป็นความชอบของโมเดลที่ลดคะแนนเมื่อมี unrequested notes มากขึ้น ไม่ใช่หลักฐานว่ากลิ่นด้อยกว่า

## 3. ตัวอย่างคำนวณจริงจาก synthetic complete domains

x,y,z,w,q เป็นสัญลักษณ์อธิบาย fixture เท่านั้น; typed input จริงต้องใช้ canonical UUID

| กรณี | Coverage Q | Focus H | การคำนวณ fit | Display |
|---|---|---|---|---|
| required(x,top,1),optional(y,top,1); Top{x,y,z,w} | (1+1)/(1+1)=1 | 2/4=1/2 | (4/5)*1+(1/5)*(1/2)=9/10 |90.0|
| optional(x,top,1),optional(y,top,1); Top{x,z} |1/2|1/2|(4/5)*(1/2)+(1/5)*(1/2)=1/2|50.0|
| required(x,top,2),optional(y,heart,1); Top{x,z},Heart{q} |2/(2+1)=2/3|1/3|(4/5)*(2/3)+(1/5)*(1/3)=3/5|60.0|

ตัวอย่างเพิ่มเติม: x ปรากฏใน required Top ที่ incomplete ยังเป็น unverified_required_domain และ fit=None
กรณี complete Top positives แต่ excluded note ปรากฏใน compatible incomplete Base ต้อง rejected_excluded,
fit=None แม้ Q/H diagnostics จะทราบค่า ห้ามแสดงเป็น ranked0 หรือ100
ตรวจสามสมการด้วย literal Fraction arithmetic แล้ว ไม่ได้รัน B1 query evaluator หรือ feature tests

## 4. Required / Optional / Excluded

- Required: ทุกข้อต้องมี verified witness ใน requested domain ที่ complete และ compatible
- Optional: เป็น soft positive; ไม่ต้อง match ทุกข้อ แต่ unmatched weight ยังคงอยู่ใน Q denominator
- Excluded: weight ต้องเป็น None; ถ้าพบใน compatible present layer ให้ reject แม้ layer นั้น incomplete
  การผ่านเพราะไม่พบต้องตรวจทุก searched layer ว่า complete/compatible ก่อน ไม่มีข้อมูลไม่ใช่ absence
- ต้องมี positive clause อย่างน้อย1ข้อ และ verified matched positive อย่างน้อย1ข้อ จึงอาจให้ numeric fit

## 5. Exact-layer / Any-pyramid

Exact selectors คือ top,heart,base; Base ไม่ใช้แทน Top และ input middle ไม่แปลงเป็น heart อัตโนมัติ
any_pyramid ค้นทั้ง3layers รวม missing/incomplete layers ด้วย ต้องครบทั้ง3ตามกฎก่อน verified positive/absence
หนึ่ง positive clause ใช้ได้มากสุด1occurrence; occurrence เดียวไม่ถูกใช้ซ้ำ เลือก witness Top,Heart,Base ตามลำดับ
General/flat/any_flat เป็นคนละ method ไม่แปลงหรือ fallback ภายใน contract นี้

## 6. Hard rules และ contradictions

Identical canonical clauses collapse ครั้งเดียวหลังตรวจ raw bound การเพิ่มคำซ้ำไม่เพิ่มน้ำหนัก
Same note_id/selector ที่ต่าง role หรือต่าง weight เป็น invalid query; same ID ที่มี any_pyramid ร่วมกับ exact
selector ก็ invalid ห้ามเลือก max weight/รวม weight/เลือก required แทน optional เอง
ต่าง exact selectors แยกกันได้ เช่น required(x,top)+excluded(x,base) และต้องผ่านแต่ละ domain

Candidate reason precedence คงที่: rejected_excluded, rejected_missing_required,
unverified_required_domain, unverified_exclusion_domain, unverified_positive_domain,
rejected_no_positive_match, computed โดยยังคืนทุก gate/clause state เพื่ออธิบายได้

## 7. Missing / Unknown / Incomplete

None คือ missing layer ไม่ใช่ complete empty set การมีสาม columns ไม่สร้าง completeness assertion
Positive/required ใน searched domain ที่ยัง unavailable เป็น unverified แม้เห็น partial positive
Q,H และ positive_domain_size เป็น None จน positive domain ครบ/compatible; verified subset counts เป็น diagnostics เท่านั้น
เมื่อ positive search domain D ทั้งหมด complete/compatible และว่าง ให้ diagnostic Q=H=0 ได้ แต่ positive minimum ไม่ผ่าน จึง fit=None ไม่เป็น perfect match
Excluded ไม่มีข้อมูลเป็น unverified ไม่ใช่ passed; ถ้าพบ excluded ใน compatible preview ให้ failed
Domain-incompatible membership ไม่ใช้เป็น witness ข้อมูลจริงไม่มี completeness/rights/eligibility เพิ่มจาก synthetic flags

**ยืนยัน: incomplete ไม่ใช่ absence; excluded ไม่ผ่านเพราะไม่มีข้อมูล; unknown ไม่ถูกเปลี่ยนเป็น zero**

## 8. Canonical IDs และ typed schema

Entry point ที่เสนอ: score_synthetic_b1(query,candidates,*,vocabulary,config)
ทุก record เป็น exact frozen dataclass ทุก constructor field ต้อง supplied; containers เป็น exact tuple/frozenset

| Record | เนื้อหาหลัก |
|---|---|
| B1Query / B1Clause | clauses tuple; note_id,selector,role,weight ทุก field required |
| B1Profile | perfume_id,top,heart,base; แต่ละ layer เป็น B1Layer หรือ None |
| B1Layer | unchanged SetInput พร้อม canonical set/complete/domain และ assertion/claim/capture/revision/snapshot/scope lineage |
| B1Vocabulary | explicit versions,512-note finite vocabulary/fingerprint,expected Top/Heart/Base domains,snapshot/scope |
| B1Config | explicit method/config/schema,policy IDs,positive minimum,formula weights และ bounds ทุกตัวตาม contract |

Note IDs เป็น lowercase UUID36ตัว: prefix20000000-0000-4000-8000- ตามด้วย12hexที่ไม่เป็นศูนย์
Perfume IDs ใช้ prefix10000000-0000-4000-8000-; suffix ไม่มีความหมายเรื่องคะแนน
ทุก query/candidate note ต้องอยู่ใน supplied vocabulary และ candidate identities ห้ามซ้ำ
Vocabulary version=synth-notes-b1-v1, alias version=canonical-id-only-b1-v1; fingerprint เป็น SHA-256 ของ sorted IDs
คั่นด้วย ASCII LF ไม่มี terminal LF ต้อง supplied/verified ไม่มี alias resolver, fuzzy lookup หรือ string-to-ID guessing
Query clause deduplication เป็น request semantics เท่านั้น ไม่ใช่ source normalization/promotion

## 9. Bounds และ validation

| ขอบเขต | ค่า exact ที่เสนอ |
|---|---|
| Raw / normalized clauses |สูงสุด30/30; reject raw31ก่อน dedup; empty-positive query invalid|
| Candidates |0..64; empty candidates ยังต้อง validate query/context/config|
| Memberships |สูงสุด512ต่อ candidate รวม incomplete/irrelevant layers; note คนละ layer นับแยก|
| Vocabulary |สูงสุด512notes|
| Positive weights / excluded |exact int1..5 / exactly None|
| Identifier tokens / numeric inputs |1..128ASCII chars / สูงสุด128bits; UUID/fingerprint มีกฎความยาวเฉพาะ|
| Total memberships |สูงสุด32768=64*512; redundant cap ไม่อ้าง negative case ที่เป็นไปไม่ได้|

ตรวจ exact types/counts, config types/bits/values, vocabulary/set sizes และ token lengths ก่อน expensive work
ตรวจ identity/fingerprint/membership/lineage/clauses ก่อนให้ผลทุก candidate; ไม่มี partial result เมื่อท้าย batch invalid
Reject bool-as-number,float,Decimal,subclasses,lists/maps/generators,coercion และ config ที่หาย/ผิด version
TypeError ใช้กับผิด declared type; ValueError ใช้กับ shape/value/bounds/lineage/query errors พร้อม fixed bounded messages
ไม่มี repr/private payload/fallback/implicit config และไม่อ้างว่าพิสูจน์8KiB request-byte boundary

## 10. Deterministic ordering / explanation

เปรียบเทียบเฉพาะ exact normalized query/config/context/masks/domains เดียวกัน หนึ่ง batch มี0หรือ1numeric partition
Numeric candidates เรียง exact unrounded fit descending แล้ว canonical UUID ascending เฉพาะ exact ties
Unranked แยกต่างหากและเรียง UUID; ไม่ใช้ reason,confidence,pair evidence หรือ rounded score จัดอันดับ
Display ใช้ exact half-up หนึ่งทศนิยมหลัง sorting; None ไม่แสดงเป็น0.0 ไม่มี cross-query/global best-match promise
Explanations คืน canonical clauses,ทุก gate,3layer states,denominators,witness/lineage และ specificity อย่างคงที่
ไม่คืน full candidate note sets; Data Confidence/pair evidence เป็น separate not-evaluated constants

## 11. Golden / property tests: specifications เท่านั้น

MC-B01–MC-B14 ยังคง semantics เดิม; MC-B15 ใช้เป็น unsupported flat/general negative ไม่ใช่เพิ่ม flat scorer
มี10extra goldens และ8property families: permutation/dedup/idempotence,occurrence non-reuse,unknown/closure,
Focus monotonicityภายใต้เงื่อนไขที่ถูกต้อง,exact sort/rounding,identity conservation,frozen outputs/bounds/no defaults
หลัง Exact Approval จึงทำ RED tests จริงก่อน code แล้ว GREEN,focused/properties และ M1/math/research/adapter offline regressions
ตามด้วย independent implementation review ที่ exact source SHA,เก็บ failures,หนึ่ง receipt และหนึ่ง Draft PR
**B1 runtime/golden/property feature tests: NOT RUN; ไม่มี scorer หรือ implementation branch/PR**

## 12. Independent Contract Review

125/125 assertions PASS,failed0,open findings0; bound กับ contract SHA-256 นี้ครบทุก20requested surfaces
ประกอบด้วย22static/18schema/35manualsemantic-text/26goldenspec/16literalFraction/3resolution/5Ownerbatch
เป็น document/specification review ไม่ใช่125feature tests และไม่ใช่ independent implementation review
IR-B1-01 MEDIUM แก้แล้ว: H ไม่เพิ่มเมื่อเพิ่ม unrequested membership; strict decrease เฉพาะ witness count บวก
และ fit monotonicity ใช้เฉพาะ admitted numeric outcomes กรณี zero matches ไม่อ้าง H ลดลงต่อไป
เก็บ initial finding/snapshots/checker correction ครบ ไม่มี formula/schema/bounds change
Report: .local/b1-contract/independent_review.json
Report SHA-256: f233451ba86c6b83940101709b9b2f414af1a5035b15a2b4d28c6227b69a2943
M1 sources/tests/evidence,22receipts,8migrations และ57protected base files ยังคงเดิม

## 13. สิ่งที่ไม่ได้อนุมัติ และ Final Owner Approval ที่เสนอ

ตอนนี้ยังไม่อนุมัติ B1 implementation แม้ Owner เห็นชอบในหลักการ การตอบ exact contract ต้องเกิดก่อน branch/RED/code
หากยอมรับภายหลัง จะอนุมัติเฉพาะ synthetic-only pure typed Python IMP-MATCH-03 ตาม exact version/hash นี้
ไม่รวม Full Mode A/B2,real-data matching/ranking,API/UI,transport/8KiB parser,DB mutation,cloud/Production/deployment,
scraping/import/source-image acquisition,source normalization/promotion,44holds/eligibility change หรือ agent merge
ไม่มีการอนุมัติ real-source completeness,rights,app authorization หรือ broader DM/OP policies
PR8 ยังคง BLOCKED ไม่มี speculative timestamp fix หรือ equivalent experiment
Data Enrichment/Media Rights Research ทำต่อใน wave นี้แยกกัน โดยไม่รอ B1 และไม่อนุมัติ binary intake/import เอง

ข้อความเสนอให้ Owner ตอบเมื่อได้อ่านและยอมรับครบถ้วน (ยังไม่ใช่ approval ที่ได้รับ):

> ฉันอนุมัติ B1-PD-TYPED-1 SHA-256 77bfca59dab449313eb02def8c30ff355e341a2b88397dbc412a09af970a5977
> method mc-b1-pyramid-positive-domain-p1/config b1-pd-typed-config-1 และข้อกำหนดทุกส่วนของ contract
> สำหรับ IMP-MATCH-03 แบบ Synthetic-only Pure Typed Python รวมสูตร Coverage80%/Focus20%,TDD,
> golden/property/regression tests,independent implementation review และหนึ่ง isolated branch/Draft PR
> ตาม acceptance criteria โดยไม่มีสิทธิ์ขยายไปยังสิ่งที่ระบุว่าไม่อนุมัติ และไม่มี agent merge
