---
id: DPT-DAT-001
project: DoomParfum By TK
type: erd_draft
status: draft
owner: project
updated: 2026-11-10
tags:
  - doomparfum
  - data
  - erd
  - schema
source_of_truth: "../README.md"
---

# ERD Draft — DoomParfum By TK

> **Document Type:** Entity-Relationship Diagram Draft
> **Source Baseline:** `../README.md` (Section 4)
> **Status:** Draft / Proposed Schema Architecture

---

## 1. Purpose / Scope

เอกสารนี้นำเสนอแบบจำลองความสัมพันธ์ระหว่างข้อมูล (Entity-Relationship Diagram) ในรูปแบบ Mermaid ERD ที่สอดคล้องกับ Bounded Contexts ทั้งหมดใน [[Domain_Model]] เพื่อเป็นพิมพ์เขียวสำหรับทำ Data Dictionary และ Drizzle ORM Schema ในระยะ P1

---

## 2. Mermaid Entity-Relationship Diagram

```mermaid
erDiagram
    BRANDS ||--o{ PERFUMES : manufactures
    PERFUMES ||--o{ PRODUCT_VARIANTS : has
    PERFUMES ||--o{ PERFUME_NOTES : contains
    NOTES ||--o{ PERFUME_NOTES : classified_in
    NOTES ||--o{ NOTE_ALIASES : has_synonyms
    NOTES ||--o{ NOTE_IMAGES : illustrated_by
    PERFUMES ||--o{ PERFUME_ACCORDS : expresses
    ACCORDS ||--o{ PERFUME_ACCORDS : categorized_in
    PERFUMES ||--o{ PERFUME_IMAGES : depicted_by

    PERFUMES ||--o{ PERFUME_RELATIONS : source_perfume
    PERFUMES ||--o{ PERFUME_RELATIONS : target_perfume
    PERFUME_RELATIONS ||--o{ COMPARISON_EVIDENCE : supported_by
    PERFUME_RELATIONS ||--o{ MATCHING_RESULTS : evaluated_as

    PRODUCT_VARIANTS ||--o{ RETAIL_LISTINGS : listed_at
    RETAIL_LISTINGS ||--o{ PRICE_OBSERVATIONS : tracks_price

    USERS ||--o{ USER_LISTS : creates
    USER_LISTS ||--o{ USER_LIST_ITEMS : contains
    PERFUMES ||--o{ USER_LIST_ITEMS : referenced_in
    USER_LIST_ITEMS ||--o{ SAVED_BUYING_SOURCES : links_to
    RETAIL_LISTINGS ||--o{ SAVED_BUYING_SOURCES : points_to

    USERS ||--o{ PURCHASE_RECORDS : bought_by
    PERFUMES ||--o{ PURCHASE_RECORDS : purchased_item
    RETAIL_LISTINGS ||--o{ PURCHASE_RECORDS : purchased_from
    USERS ||--o{ INVENTORY_ITEMS : owned_by
    PERFUMES ||--o{ INVENTORY_ITEMS : physical_bottle
    PURCHASE_RECORDS ||--o{ INVENTORY_ITEMS : originating_purchase

    SOURCE_RECORDS ||--o{ PERFUMES : provenance
    SOURCE_RECORDS ||--o{ COMPARISON_EVIDENCE : provenance
    SOURCE_RECORDS ||--o{ NOTE_IMAGES : license_info
    SOURCE_RECORDS ||--o{ PERFUME_IMAGES : license_info

    BRANDS {
        uuid id PK
        string name
        string slug UK
        string origin_country
        string market_position
        timestamp created_at
    }

    PERFUMES {
        uuid id PK
        uuid brand_id FK
        string name
        string slug UK
        integer release_year
        string gender
        string status
        timestamp created_at
    }

    PRODUCT_VARIANTS {
        uuid id PK
        uuid perfume_id FK
        integer volume_ml
        string concentration
        string sku
    }

    NOTES {
        uuid id PK
        string canonical_name UK
        string name_th
        string family
        string description
    }

    PERFUME_NOTES {
        uuid id PK
        uuid perfume_id FK
        uuid note_id FK
        string layer
        integer sort_order
    }

    ACCORDS {
        uuid id PK
        string name UK
        string name_th
    }

    PERFUME_ACCORDS {
        uuid id PK
        uuid perfume_id FK
        uuid accord_id FK
        decimal score_weight
    }

    PERFUME_RELATIONS {
        uuid id PK
        uuid reference_perfume_id FK
        uuid candidate_perfume_id FK
        string relation_type
        decimal similarity_score
        decimal confidence_score
    }

    COMPARISON_EVIDENCE {
        uuid id PK
        uuid relation_id FK
        uuid source_id FK
        string claim_type
        text excerpt_text
        string verdict
    }

    RETAIL_LISTINGS {
        uuid id PK
        uuid variant_id FK
        string platform
        string shop_name
        string product_url
        decimal current_price
        string currency
        timestamp last_checked_at
    }

    USERS {
        uuid id PK
        string username UK
        string email UK
        string display_name
        timestamp created_at
    }

    USER_LISTS {
        uuid id PK
        uuid user_id FK
        string list_type
        string name
    }

    USER_LIST_ITEMS {
        uuid id PK
        uuid list_id FK
        uuid perfume_id FK
        string status
        text notes
        timestamp added_at
    }

    SAVED_BUYING_SOURCES {
        uuid id PK
        uuid list_item_id FK
        uuid listing_id FK
        text user_notes
    }

    PURCHASE_RECORDS {
        uuid id PK
        uuid user_id FK
        uuid perfume_id FK
        uuid listing_id FK
        decimal paid_price
        string currency
        integer bottle_volume_ml
        date ordered_at
        date received_at
        text notes
    }

    INVENTORY_ITEMS {
        uuid id PK
        uuid user_id FK
        uuid perfume_id FK
        uuid purchase_record_id FK
        string status
        integer remaining_percentage
        date acquired_at
        date finished_at
    }

    SOURCE_RECORDS {
        uuid id PK
        string source_type
        string source_url
        string license_type
        boolean rights_verified
        timestamp checked_at
    }
```

---

## 3. Key Relationships Explained

1. **Master Catalogue:**
   - 1 `BRANDS` $\rightarrow$ หลาย `PERFUMES`
   - 1 `PERFUMES` $\rightarrow$ หลาย `PRODUCT_VARIANTS`
   - `PERFUMES` และ `NOTES` เชื่อมกันแบบ Many-to-Many ผ่าน `PERFUME_NOTES` พร้อมระบุ `layer` (`TOP`, `HEART`, `BASE`)
   - `PERFUMES` และ `ACCORDS` เชื่อมกันแบบ Many-to-Many ผ่าน `PERFUME_ACCORDS`
2. **Matching & Evidence:**
   - `PERFUME_RELATIONS` เก็บการจับคู่ระหว่าง `reference_perfume` และ `candidate_perfume`
   - มี `COMPARISON_EVIDENCE` รองรับหลายข้อความอ้างอิง และเชื่อมไปยัง `SOURCE_RECORDS` เพื่อสอบทานที่มา
3. **Shopping & Personal Collection:**
   - `USER_LIST_ITEMS` สำหรับ `My Cart` เชื่อมกับ `SAVED_BUYING_SOURCES` เพื่อรองรับหลายร้านต่อหนึ่งน้ำหอม
   - `PURCHASE_RECORDS` เก็บข้อมูลการซื้อถาวรแบบอิสระ ไม่ถูกลบ
   - `INVENTORY_ITEMS` เก็บขวดที่มีอยู่จริง เชื่อมโยงประวัติการซื้อต้นทาง (`purchase_record_id`) แบบ Nullable

---

## 4. Requirements Covered

- [[Requirements_Register#R01|R01]], [[Requirements_Register#R02|R02]], [[Requirements_Register#R03|R03]]
- [[Requirements_Register#R10|R10]], [[Requirements_Register#R16|R16]], [[Requirements_Register#R17|R17]]
- [[Requirements_Register#R21|R21]], [[Requirements_Register#R26|R26]], [[Requirements_Register#R28|R28]]

---

## 5. Dependencies & Links

- รายละเอียดฟิลด์และคีย์: [[Data_Dictionary_Draft]]
- โดเมนโมเดล: [[Domain_Model]]
- ธรรมาภิบาลข้อมูล: [[Data_Quality_and_Provenance]]

---

## 6. Change Notes

- `2026-11-10`: ร่างผัง ERD ฉบับแรก รองรับครบทุก Bounded Context ตาม Blueprint
