---
id: DPT-UX-004
project: DoomParfum By TK
type: ux_screen_spec
status: draft
owner: project
updated: 2026-11-10
tags:
  - doomparfum
  - ux
  - screens
  - cart
  - shopping_tracker
source_of_truth: "../README.md"
---

# Screen Spec: Shopping Tracker (My Cart) — DoomParfum By TK

> **Document Type:** UI/UX Screen Specification
> **Target Route:** `/cart`
> **Source Baseline:** `../README.md` (Section 2.2 & 5.4)
> **Status:** Draft / Confirmed UX Spec

---

## 1. Purpose / Scope

เอกสารนี้กำหนดข้อกำหนดสำหรับหน้าจอ **Shopping Tracker (`My Cart`)** ซึ่งทำหน้าที่เป็นกระดานบันทึกรายการน้ำหอมเตรียมซื้อ จัดเก็บลิงก์ร้านค้าภายนอก (Shopee) หลายร้านต่อหนึ่งน้ำหอม และเป็นจุดเปลี่ยนผ่านสถานะการสั่งซื้อด้วยมือ (Manual State Transition) โดยปราศจากระบบ Checkout จริง

---

## 2. Layout Wireframe & Tabs

```text
+-------------------------------------------------------------------------+
|  DoomParfum By TK — Personal Shopping Tracker                           |
+-------------------------------------------------------------------------+
|  [ To Buy / My Cart (3) ]   [ Ordered / Awaiting (1) ]   [ History (8) ]|
+-------------------------------------------------------------------------+
|  +-------------------------------------------------------------------+  |
|  | [Img]  BE CHERIE PARFUM — White Instinct (Extrait)                |  |
|  |        Brand: Thailand (Indie) | Added: 10 Nov 2026               |  |
|  |                                                                   |  |
|  |  SAVED BUYING SOURCES:                                            |  |
|  |  (o) Shopee: TK Official Store — ฿1,290 [100ml] [เปิดลิงก์ ↗]     |  |
|  |      Note: "ร้าน Mall ของแท้ ส่งฟรีจาก กทม."                     |  |
|  |  ( ) Shopee: Discount Fragrance — ฿1,150 [100ml] [เปิดลิงก์ ↗]    |  |
|  |      Note: "ร้านหิ้ว รอวัน Payday มีโค้ดลด 15%"                  |  |
|  |                                                                   |  |
|  |  [+ Add Another Source]   [Edit Notes]                            |  |
|  |                                                                   |  |
|  |  ACTIONS:                                                         |  |
|  |  [🛒 Mark as Ordered...]          [Move to Wishlist]   [Remove]   |  |
|  +-------------------------------------------------------------------+  |
|                                                                         |
|  +-------------------------------------------------------------------+  |
|  | [Img]  SÚNDALO — Rhapsody Sky (50ml)                              |  |
|  |        Brand: Thailand (Indie) | Added: 08 Nov 2026               |  |
|  |                                                                   |  |
|  |  SAVED BUYING SOURCES:                                            |  |
|  |  (o) Shopee: SÚNDALO Official — ฿1,690 [50ml] [เปิดลิงก์ ↗]       |  |
|  |                                                                   |  |
|  |  [+ Add Another Source]                                           |  |
|  |  [🛒 Mark as Ordered...]          [Move to Wishlist]   [Remove]   |  |
|  +-------------------------------------------------------------------+  |
|                                                                         |
|  SUMMARY BAR (INFORMATIONAL ONLY — NO CHECKOUT):                        |
|  Items in Cart: 2 items | Estimated Budget: ฿2,840 - ฿2,980             |
|  *แอปนี้ไม่มีการตัดเงิน โปรดกดลิงก์ร้านค้าเพื่อสั่งซื้อบน Shopee ด้วยตนเอง*|
+-------------------------------------------------------------------------+
```

---

## 3. Key Interaction Flows & Modals

### 3.1 Modal: "+ Add Buying Source"
- เมื่อผู้ใช้กดปุ่มเพิ่มแหล่งซื้อ ระบบจะเปิด Dialog Modal:
  - **Platform:** Dropdown (ค่าเริ่มต้น: Shopee, Lazada, Official Web, Other)
  - **Store Name:** ช่องกรอกชื่อร้าน (เช่น "SÚNDALO Official")
  - **Product URL:** ช่องกรอกลิงก์ตรงไปยังสินค้า
  - **Observed Price:** ตัวเลขราคาที่เห็น (บาท)
  - **Bottle Volume (mL):** ขนาดขวด (เช่น 50ml, 100ml)
  - **Personal Note:** หมายเหตุความน่าเชื่อถือหรือโปรโมชัน

### 3.2 Modal: "Mark as Ordered" (R25)
- เมื่อผู้ใช้ไปสั่งซื้อที่ Shopee สำเร็จและกลับมากดปุ่มนี้:
  - ระบบจะแสดง Modal ยืนยัน:
    - *เลือกร้านที่สั่งซื้อจริง:* (เลือกจาก Saved Sources ที่มี)
    - *ราคาจ่ายจริง (Paid Price):* (ตัวเลข Optional - ใส่ยอดสุทธิหลังลด)
    - *วันที่สั่งซื้อ (Order Date):* (Default: วันปัจจุบัน)
  - เมื่อกดยืนยัน รายการจะถูกย้ายไปยังแท็บ `Ordered / Awaiting Delivery` ทันที

### 3.3 Duplicate Warning Protection (R30)
- หากผู้ใช้กดเพิ่มน้ำหอมรุ่นที่มีใน Cart อยู่แล้ว ระบบจะแสดง Alert:
  > *"น้ำหอมรุ่นนี้มีอยู่ใน My Cart แล้ว คุณต้องการเพิ่มแหล่งซื้อใหม่ หรือเปิดดูในตะกร้า?"*

---

## 4. Requirements Covered

- [[Requirements_Register#R09|R09]] — Manual Import & Links
- [[Requirements_Register#R10|R10]] — Multiple Retail Sources per Perfume
- [[Requirements_Register#R11|R11]] — Status Lifecycle Tracking
- [[Requirements_Register#R23|R23]] — Universal Brand In-App Cart
- [[Requirements_Register#R24|R24]] — Multiple Links & Notes
- [[Requirements_Register#R25|R25]] — Manual Mark as Ordered
- [[Requirements_Register#R30|R30]] — Duplicate Warning

---

## 5. Dependencies & Links

- โดเมนโมเดลตะกร้า: [[My_Cart_and_Ownership]]
- ผังข้อมูล: [[ERD_Draft#saved_buying_sources|ERD_Draft]]
- หน้าจอคอลเลกชัน: [[Collection_Dashboard]]

---

## 6. Change Notes

- `2026-11-10`: ร่างสเปกหน้าจอ Shopping Tracker ครบถ้วนตามแบบจำลอง No-Checkout Cart
