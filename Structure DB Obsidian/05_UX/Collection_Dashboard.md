---
id: DPT-UX-005
project: DoomParfum By TK
type: ux_screen_spec
status: draft
owner: project
updated: 2026-11-10
tags:
  - doomparfum
  - ux
  - screens
  - collection
  - dashboard
  - analytics
source_of_truth: "../README.md"
---

# Screen Spec: Collection & Analytics Dashboard — DoomParfum By TK

> **Document Type:** UI/UX Screen Specification
> **Target Routes:** `/collection` (Inventory & History) & `/dashboard` (Analytics)
> **Source Baseline:** `../README.md` (Section 2.2 & 5.4)
> **Status:** Draft / Confirmed UX Spec

---

## 1. Purpose / Scope

เอกสารนี้กำหนดข้อกำหนดสำหรับ **หน้าคอลเลกชันส่วนตัว (`My Collection`)** และ **หน้าแดชบอร์ดวิเคราะห์สถิติ (`Collection Dashboard`)** โดยมีหัวใจสำคัญคือการแยกสถิติระหว่าง **"น้ำหอมที่เคยซื้อทั้งหมด (Ever Purchased)"** กับ **"น้ำหอมที่มีอยู่ในครอบครองปัจจุบัน (Currently Owned)"** ออกจากกันอย่างชัดเจน

---

## 2. Layout Wireframe: Collection Manager (`/collection`)

```text
+-------------------------------------------------------------------------+
|  DoomParfum By TK — My Collection & History                             |
+-------------------------------------------------------------------------+
|  [ Current Inventory (12 Bottles) ]     [ Purchase History (18 Orders) ]|
+-------------------------------------------------------------------------+
|  FILTERS: [All Brands v]  [Status: Owned (10), Finished (2) v]          |
+-------------------------------------------------------------------------+
|  +-------------------------------------------------------------------+  |
|  | [Img]  BE CHERIE PARFUM — White Instinct (100ml Extrait)          |  |
|  |        Status: 🟢 OWNED | Acquired: 15 Oct 2026                   |  |
|  |        Remaining: ~85% [████████░░]                               |  |
|  |        Originated From: Purchase on 10 Oct 2026 (฿1,250)          |  |
|  |                                                                   |  |
|  |  [✏️ Edit Level]   [Mark Finished]   [Mark Sold/Gifted]   [Notes]  |  |
|  +-------------------------------------------------------------------+  |
|                                                                         |
|  +-------------------------------------------------------------------+  |
|  | [Img]  Dior — Sauvage EDT (100ml)                                 |  |
|  |        Status: ⚪ FINISHED (ใช้หมดแล้วเมื่อ 02 ก.ย. 2026)          |  |
|  |        Originated From: Purchase on 12 ม.ค. 2025 (฿4,200)         |  |
|  |        *ประวัติการซื้อยังคงถูกบันทึกไว้ในระบบ*                   |  |
|  |                                                                   |  |
|  |  [Re-buy -> Add to My Cart]   [View Purchase Detail]              |  |
|  +-------------------------------------------------------------------+  |
+-------------------------------------------------------------------------+
```

---

## 3. Layout Wireframe: Analytics Dashboard (`/dashboard`)

```text
+-------------------------------------------------------------------------+
|  DoomParfum By TK — Scent Collection Insights                           |
+-------------------------------------------------------------------------+
|  KEY METRICS SUMMARY:                                                   |
|  +-------------------------+  +-------------------------+               |
|  | 📦 CURRENTLY OWNED      |  | 🧾 EVER PURCHASED       |               |
|  | 10 Bottles in Cabinet   |  | 18 Bottles Lifetime     |               |
|  | Total Volume: 850 mL    |  | Total Records: 18       |               |
|  +-------------------------+  +-------------------------+               |
|  +-------------------------+  +-------------------------+               |
|  | 🇹🇭 THAI BRANDS          |  | 💰 ESTIMATED SPENT      |               |
|  | 60% of Collection       |  | ฿19,450 (Avg ฿1,080/btl)|               |
|  +-------------------------+  +-------------------------+               |
+-------------------------------------------------------------------------+
|  BREAKDOWN CHARTS:                                                      |
|                                                                         |
|  1. FRAGRANCE FAMILIES (แนวกลิ่นที่สะสม):                                |
|  - Fresh / Citrus:  ████████████████████ (40%)                          |
|  - Woody / Amber:   ███████████████ (30%)                               |
|  - Aromatic Spicy:  ██████████ (20%)                                    |
|  - Floral:          █████ (10%)                                         |
|                                                                         |
|  2. BRAND ORIGIN DISTRIBUTION:                                          |
|  - Thailand (60%) | Middle East (25%) | France (10%) | Other (5%)       |
|                                                                         |
|  3. TOP RECURRING NOTES (โน้ตกลิ่นที่คุณชอบที่สุดในตู้):                |
|  #1 Bergamot (8 ขวด) | #2 Ambroxan (7 ขวด) | #3 Cedarwood (6 ขวด)       |
+-------------------------------------------------------------------------+
|  [R31 - OPTIONAL DEFERRED STATS]                                        |
|  - Average Cost per mL: ฿18.50 / mL                                     |
|  - Bottle Consumption Rate: ~1.2 bottles / quarter                      |
+-------------------------------------------------------------------------+
```

---

## 4. Fundamental Business Logic in Dashboard

1. **Dual Metrics Integrity (R27):**
   - **`Currently Owned`:** คำนวณจาก `inventory_items` ที่มี `status = 'owned'` เท่านั้น
   - **`Ever Purchased`:** คำนวณจาก `purchase_records` ทั้งหมดในประวัติศาสตร์ โดยไม่สนว่าขวดใน Inventory จะถูกเปลี่ยนเป็น `finished`, `sold`, หรือถูกลบ
2. **Missing Spending Gracefulness:**
   - หากผู้ใช้ไม่ได้กรอกราคาตอนสั่งซื้อ (`paid_price = null`) ระบบจะไม่แสดงผลว่า ฿0 แต่จะระบุว่า `คำนวณจาก 12 จาก 18 รายการที่มีข้อมูลราคา`
3. **Note Preferences Aggregation:**
   - ระบบนับความถี่ของ Notes จากทุกรุ่นที่อยู่ในคอลเลกชันปัจจุบัน เพื่อสรุปเป็น "Taste Profile" ของผู้ใช้

---

## 5. Requirements Covered

- [[Requirements_Register#R11|R11]] — Ownership Lifecycle Status
- [[Requirements_Register#R26|R26]] — Purchase History Persistence
- [[Requirements_Register#R27|R27]] — Collection Analytics Dashboard
- [[Requirements_Register#R28|R28]] — Separate Purchase Record from Inventory
- [[Requirements_Register#R29|R29]] — Optional Purchase Pricing
- [[Requirements_Register#R31|R31]] — Historical Spending Analytics (Deferred)

---

## 6. Dependencies & Links

- โดเมนโมเดล: [[My_Cart_and_Ownership]]
- ผังข้อมูล: [[ERD_Draft#inventory_items|ERD_Draft]]
- พจนานุกรมข้อมูล: [[Data_Dictionary_Draft#purchase_records|Data_Dictionary_Draft]]

---

## 7. Change Notes

- `2026-11-10`: ร่างสเปกหน้าคอลเลกชันและแดชบอร์ด แยกสถิติ Currently Owned vs Ever Purchased อย่างชัดเจน
