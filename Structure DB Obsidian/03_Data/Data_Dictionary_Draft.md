---
id: DPT-DAT-002
project: DoomParfum By TK
type: data_dictionary
status: draft
owner: project
updated: 2026-11-10
tags:
  - doomparfum
  - data
  - dictionary
  - schema
source_of_truth: "../README.md"
---

# Data Dictionary Draft — DoomParfum By TK

> **Document Type:** Conceptual Schema & Field Specifications
> **Source Baseline:** `../README.md` (Section 4)
> **Status:** Draft / Proposed Data Dictionary

---

## 1. Overview

เอกสารนี้ระบุรายละเอียดโครงสร้างข้อมูลระดับคอลัมน์ (Column-level specifications) รวมถึงชนิดข้อมูล (Data Types), ข้อจำกัด (Constraints: PK, FK, Unique, Nullable), แหล่งข้อมูลตั้งต้น (Source), และคำอธิบายความหมายเชิงธุรกิจสำหรับตารางหลักในระบบ

---

## 2. Table Specifications

### 2.1 `brands` (แบรนด์ผู้ผลิต)
| Column Name | Data Type | Nullable | Unique | FK Reference | Source | Notes |
|---|---|---|---|---|---|---|
| `id` | UUID | NO | YES (PK) | - | System | Generated UUIDv4 |
| `name` | VARCHAR(150) | NO | NO | - | Dataset / Manual | ชื่อทางการของแบรนด์ เช่น "BE CHERIE PARFUM" |
| `slug` | VARCHAR(160) | NO | YES | - | System | URL-safe slug เช่น "be-cherie-parfum" |
| `origin_country` | VARCHAR(60) | NO | NO | - | Master Data | ประเทศต้นกำเนิด เช่น "Thailand", "UAE" |
| `market_position` | VARCHAR(40) | NO | NO | - | Taxonomy | "Designer", "Niche", "Indie", "Inspired House" |
| `website_url` | TEXT | YES | NO | - | Official | เว็บไซต์ทางการของแบรนด์ (ถ้ามี) |
| `created_at` | TIMESTAMPTZ | NO | NO | - | System | วันเวลาที่สร้างข้อมูล |

### 2.2 `perfumes` (รุ่นน้ำหอมหลัก)
| Column Name | Data Type | Nullable | Unique | FK Reference | Source | Notes |
|---|---|---|---|---|---|---|
| `id` | UUID | NO | YES (PK) | - | System | Primary Key |
| `brand_id` | UUID | NO | NO | `brands(id)` | Master Data | รหัสแบรนด์ผู้ผลิต |
| `name` | VARCHAR(200) | NO | NO | - | Dataset / Manual | ชื่อรุ่นทางการ เช่น "White Instinct" |
| `slug` | VARCHAR(220) | NO | YES | - | System | URL-safe slug |
| `release_year` | SMALLINT | YES | NO | - | Master Data | ปีที่เปิดตัว เช่น 2024 |
| `gender` | VARCHAR(30) | YES | NO | - | Master Data | "Men", "Women", "Unisex" |
| `description` | TEXT | YES | NO | - | Dataset / Brand | คำอธิบายกลิ่นอย่างเป็นทางการ |
| `status` | VARCHAR(30) | NO | NO | - | System | "draft", "reviewed", "approved" |
| `created_at` | TIMESTAMPTZ | NO | NO | - | System | วันเวลาที่บันทึก |

### 2.3 `notes` (คลังโน้ตมาตรฐาน)
| Column Name | Data Type | Nullable | Unique | FK Reference | Source | Notes |
|---|---|---|---|---|---|---|
| `id` | UUID | NO | YES (PK) | - | System | Primary Key |
| `canonical_name` | VARCHAR(100) | NO | YES | - | Olfactory Master | ชื่อสากลภาษาอังกฤษ เช่น "Bergamot" |
| `name_th` | VARCHAR(120) | YES | NO | - | Translation | ชื่อภาษาไทย เช่น "มะกรูดฝรั่ง" |
| `family` | VARCHAR(50) | YES | NO | - | Taxonomy | กลุ่มโน้ต เช่น "Citrus", "Woody", "Floral" |
| `description` | TEXT | YES | NO | - | Olfactory Master | คำอธิบายโทนกลิ่นของโน้ต |

### 2.4 `perfume_notes` (การจับคู่โน้ตกับน้ำหอม)
| Column Name | Data Type | Nullable | Unique | FK Reference | Source | Notes |
|---|---|---|---|---|---|---|
| `id` | UUID | NO | YES (PK) | - | System | Primary Key |
| `perfume_id` | UUID | NO | NO | `perfumes(id)` | Relation | รหัสน้ำหอม |
| `note_id` | UUID | NO | NO | `notes(id)` | Relation | รหัสโน้ต |
| `layer` | VARCHAR(20) | NO | NO | - | Master Data | "TOP", "HEART", "BASE" |
| `sort_order` | SMALLINT | YES | NO | - | Master Data | ลำดับการแสดงผลในชั้น |

### 2.5 `accords` & `perfume_accords` (ตระกูลและลักษณะกลิ่น)
| Column Name | Data Type | Nullable | Unique | FK Reference | Source | Notes |
|---|---|---|---|---|---|---|
| `accord_id` | UUID | NO | YES (PK) | - | System | Primary Key ของ `accords` |
| `name` | VARCHAR(60) | NO | YES | - | Taxonomy | ชื่อ Accord เช่น "Fresh Spicy", "Woody" |
| `name_th` | VARCHAR(80) | YES | NO | - | Translation | ชื่อภาษาไทย เช่น "เผ็ดสดชื่น" |
| `score_weight` | NUMERIC(4,2)| YES | NO | - | Ingestion / Data | น้ำหนักความเด่น (เช่น 0.00 – 1.00) ใน `perfume_accords` |

### 2.6 `retail_listings` (รายการสินค้าบนร้านค้า)
| Column Name | Data Type | Nullable | Unique | FK Reference | Source | Notes |
|---|---|---|---|---|---|---|
| `id` | UUID | NO | YES (PK) | - | System | Primary Key |
| `variant_id` | UUID | YES | NO | `product_variants(id)`| Catalog | รหัสขนาด/รุ่นย่อย (ถ้ามี) |
| `platform` | VARCHAR(50) | NO | NO | - | User / Observation | "Shopee", "Lazada", "Official" |
| `shop_name` | VARCHAR(150) | NO | NO | - | User Input | ชื่อร้านค้า |
| `product_url` | TEXT | NO | NO | - | User Input | ลิงก์ตรงไปยังสินค้า |
| `current_price` | NUMERIC(10,2)| YES | NO | - | User / Scrape | ราคาที่เห็น ณ เวลาบันทึก (บาท) |
| `currency` | CHAR(3) | NO | NO | - | Default | ค่าเริ่มต้น "THB" |
| `last_checked_at`| TIMESTAMPTZ | YES | NO | - | System | วันเวลาที่สแนปช็อตราคา |

### 2.7 `user_list_items` (รายการตะกร้า/รายการที่บันทึก)
| Column Name | Data Type | Nullable | Unique | FK Reference | Source | Notes |
|---|---|---|---|---|---|---|
| `id` | UUID | NO | YES (PK) | - | System | Primary Key |
| `list_id` | UUID | NO | NO | `user_lists(id)` | User Domain | รหัสกลุ่มรายการ (เช่น Cart, Wishlist) |
| `perfume_id` | UUID | NO | NO | `perfumes(id)` | Master Data | รหัสน้ำหอม |
| `status` | VARCHAR(30) | NO | NO | - | State Machine | "in_cart", "ordered", "skipped" |
| `notes` | TEXT | YES | NO | - | User Input | หมายเหตุส่วนตัว |
| `added_at` | TIMESTAMPTZ | NO | NO | - | System | วันที่เพิ่มเข้าตะกร้า |

### 2.8 `saved_buying_sources` (การผูกร้านค้ากับรายการตะกร้า)
| Column Name | Data Type | Nullable | Unique | FK Reference | Source | Notes |
|---|---|---|---|---|---|---|
| `id` | UUID | NO | YES (PK) | - | System | Primary Key |
| `list_item_id` | UUID | NO | NO | `user_list_items(id)`| User Domain | รายการในตะกร้า |
| `listing_id` | UUID | NO | NO | `retail_listings(id)`| Marketplace | แหล่งซื้อร้านค้าที่เลือกผูกไว้ |
| `user_notes` | TEXT | YES | NO | - | User Input | เช่น "ร้าน Mall ส่งไว", "รอใช้โค้ด" |

### 2.9 `purchase_records` (ประวัติการซื้อถาวร)
| Column Name | Data Type | Nullable | Unique | FK Reference | Source | Notes |
|---|---|---|---|---|---|---|
| `id` | UUID | NO | YES (PK) | - | System | Primary Key |
| `user_id` | UUID | NO | NO | `users(id)` | User Domain | ผู้ใช้ที่ซื้อ |
| `perfume_id` | UUID | NO | NO | `perfumes(id)` | Master Data | น้ำหอมที่ซื้อ |
| `listing_id` | UUID | YES | NO | `retail_listings(id)`| Marketplace | ร้านที่ซื้อ (Nullable) |
| `paid_price` | NUMERIC(10,2)| YES | NO | - | User Input | ยอดเงินที่จ่ายจริง (บาท) |
| `currency` | CHAR(3) | NO | NO | - | Default | ค่าเริ่มต้น "THB" |
| `bottle_volume_ml`| INTEGER | YES | NO | - | User Input | ปริมาตรขวด เช่น 50, 100 |
| `ordered_at` | DATE | YES | NO | - | User Input | วันที่สั่งซื้อ |
| `received_at` | DATE | YES | NO | - | User Input | วันที่ได้รับสินค้า |
| `notes` | TEXT | YES | NO | - | User Input | ประสบการณ์สั่งซื้อ/โค้ดส่วนลด |

### 2.10 `inventory_items` (คลังขวดที่ครอบครอง)
| Column Name | Data Type | Nullable | Unique | FK Reference | Source | Notes |
|---|---|---|---|---|---|---|
| `id` | UUID | NO | YES (PK) | - | System | Primary Key |
| `user_id` | UUID | NO | NO | `users(id)` | User Domain | เจ้าของ |
| `perfume_id` | UUID | NO | NO | `perfumes(id)` | Master Data | น้ำหอมขวดนี้ |
| `purchase_record_id`| UUID | YES | NO | `purchase_records(id)`| Purchase | บันทึกการซื้อต้นทาง (ถ้ามี) |
| `status` | VARCHAR(30) | NO | NO | - | Lifecycle | "owned", "finished", "sold", "gifted" |
| `remaining_percentage`| SMALLINT| YES | NO | - | User Input | ปริมาณคงเหลือโดยประมาณ (0–100%) |
| `acquired_at` | DATE | YES | NO | - | User Input | วันที่ได้รับมา |
| `finished_at` | DATE | YES | NO | - | User Input | วันที่ใช้หมด/จำหน่ายออก |

---

## 3. Data Types & Precision Standards

- **ID:** `UUIDv4` เพื่อความปลอดภัย ไม่เผยแพร่ Auto-increment ID
- **Currency/Prices:** `NUMERIC(10, 2)` ป้องกันปัญหาปัดเศษของ Floating Point
- **Dates/Timestamps:**
  - `TIMESTAMPTZ` สำหรับ Audit timestamps (`created_at`, `updated_at`, `checked_at`)
  - `DATE` สำหรับเหตุการณ์ในชีวิตประจำวันของผู้ใช้ (`ordered_at`, `received_at`) โดยไม่ต้องระบุเวลาแม่นยำ

---

## 4. Requirements Covered

- [[Requirements_Register#R01|R01]], [[Requirements_Register#R03|R03]], [[Requirements_Register#R10|R10]]
- [[Requirements_Register#R24|R24]], [[Requirements_Register#R26|R26]], [[Requirements_Register#R28|R28]], [[Requirements_Register#R29|R29]]

---

## 5. Dependencies & Links

- ผังความสัมพันธ์: [[ERD_Draft]]
- โดเมนโมเดล: [[Domain_Model]]
- ตะกร้าและการครอบครอง: [[My_Cart_and_Ownership]]

---

## 6. Change Notes

- `2026-11-10`: จัดทำร่างพจนานุกรมข้อมูลฉบับสมบูรณ์สำหรับ 10 เอนทิตีหลัก
