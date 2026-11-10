---
id: DPT-UX-002
project: DoomParfum By TK
type: ux_screen_spec
status: draft
owner: project
updated: 2026-11-10
tags:
  - doomparfum
  - ux
  - screens
  - pyramid
  - notes
source_of_truth: "../README.md"
---

# Screen Spec: Perfume Detail & Pyramid — DoomParfum By TK

> **Document Type:** UI/UX Screen Specification
> **Target Route:** `/perfumes/:slug`
> **Source Baseline:** `../README.md` (Section 2.1 & 5.4)
> **Status:** Draft / Confirmed UX Spec

---

## 1. Purpose / Scope

เอกสารนี้กำหนดข้อกำหนดการออกแบบและการโต้ตอบ (Interaction Design) สำหรับ **หน้ารายละเอียดน้ำหอม (Perfume Detail Page)** โดยมีจุดเด่นคือการแสดง **พีระมิดโน้ต (Olfactory Pyramid) พร้อมภาพประกอบวัตถุดิบ** และระบบคลิกโน้ตเพื่อค้นหาความเชื่อมโยง

---

## 2. Layout Wireframe & Components

```text
+-------------------------------------------------------------------------+
| [<- Back]    DoomParfum By TK                  [Search] [Cart (3)] [TK] |
+-------------------------------------------------------------------------+
|                                                                         |
|  [Bottle Image]       BE CHERIE PARFUM                                  |
|  (Verified / Safe)    White Instinct                                    |
|                       Origin: Thailand | Position: Indie / Craft        |
|                       Release: 2024 | Concentration: Extrait            |
|                                                                         |
|                       [+ Add to My Cart]  [Compare Scent]  [Share]      |
|                                                                         |
+-------------------------------------------------------------------------+
|  MAIN ACCORDS:                                                          |
|  [ Citrus  ████████████ ]  [ Fresh Spicy ████████ ]  [ Woody █████ ]    |
+-------------------------------------------------------------------------+
|                                                                         |
|  OLFACTORY PYRAMID (พีระมิดโน้ต)                                        |
|                                                                         |
|  --- TOP NOTES (กลิ่นเปิด) ---                                          |
|  +--------------------+  +--------------------+                         |
|  | [Img: Bergamot]    |  | [Img: Pink Pepper] |                         |
|  | Bergamot (คลิกค้น) |  | Pink Pepper        |                         |
|  +--------------------+  +--------------------+                         |
|                                                                         |
|  --- HEART / MIDDLE NOTES (กลิ่นกลาง) ---                                |
|  +--------------------+  +--------------------+  +--------------------+ |
|  | [Img: Lavender]    |  | [Img: Geranium]    |  | [Img: Cardamom]    | |
|  | Lavender           |  | Geranium           |  | Cardamom           | |
|  +--------------------+  +--------------------+  +--------------------+ |
|                                                                         |
|  --- BASE NOTES (กลิ่นฐาน) ---                                          |
|  +--------------------+  +--------------------+  +--------------------+ |
|  | [Img: Ambroxan]    |  | [Img: Cedarwood]   |  | [Img: Vetiver]     | |
|  | Ambroxan           |  | Cedarwood          |  | Vetiver            | |
|  +--------------------+  +--------------------+  +--------------------+ |
|                                                                         |
+-------------------------------------------------------------------------+
|  SAVED BUYING SOURCES (แหล่งซื้อที่บันทึกไว้)                           |
|  - Shopee: ร้าน TK Official Store - ฿1,290 [ไปที่ร้าน ->]               |
|  - [+ Add Buying Source]                                                |
+-------------------------------------------------------------------------+
|  COMMUNITY REVIEWS & SIMILAR SCENTS                                     |
|  - สไตล์กลิ่นใกล้เคียง: Dior Sauvage (85% Structural Match)             |
|  - [ดูการเปรียบเทียบ Side-by-Side ->]                                   |
+-------------------------------------------------------------------------+
```

---

## 3. Component Specifications & Behavior

### 3.1 Note Card Component with Image (R13)
- การ์ดแต่ละใบแสดง:
  1. **ภาพวัตถุดิบ:** ขนาด thumbnail อัตราส่วน 1:1 มุมมน ภาพที่มาถูกลิขสิทธิ์ (CC หรือ Openverse)
  2. **ชื่อสากล (Canonical Name):** เช่น `Bergamot`
  3. **ชื่อไทย (Thai Translation):** เช่น `มะกรูดฝรั่ง`
  4. **Hover / Focus Effect:** ขยายเล็กน้อย พร้อมไอคอนแว่นขยาย

### 3.2 Click-to-Search Interaction (R14)
- **พฤติกรรม:** เมื่อผู้ใช้คลิกที่การ์ดโน้ตใดๆ:
  - ระบบจะนำทางไปยังหน้าค้นหา: `/explore?note=:note_slug`
  - กรองแสดงเฉพาะน้ำหอมที่มีโน้ตนั้นในแคตตาล็อก พร้อมระบุว่าโน้ตนั้นอยู่ในชั้นใดของรุ่นอื่น

### 3.3 Main Accords Bar Chart
- แสดงแถบแนวนอนความเด่นของ Accord เรียงจากมากไปน้อย
- โค้ดสีประจำ Accord (เช่น Citrus = สีเหลืองอ่อน, Woody = สีน้ำตาลอบอุ่น, Amber = สีทอง)

### 3.4 Missing Data Handling
- หากน้ำหอมบางรุ่นไม่มีการแยกชั้นโน้ต (มีเฉพาะ All Notes):
  - ระบบจะไม่แสดงกรอบสามเหลี่ยมพีระมิด แต่จะแสดงเป็นกริด `All Listed Notes`
  - มีป้ายแจ้งเตือนสีเทา: `แบรนด์ไม่ได้ระบุการแยกชั้นโน้ตอย่างเป็นทางการ`

---

## 4. Requirements Covered

- [[Requirements_Register#R02|R02]] — Brand Origin & Position Display
- [[Requirements_Register#R03|R03]] — Pyramid Notes & Accords
- [[Requirements_Register#R13|R13]] — Perfume Pyramid with Visual Cards
- [[Requirements_Register#R14|R14]] — Interactive Note Search
- [[Requirements_Register#R23|R23]] — Add to Cart CTA

---

## 5. Dependencies & Links

- โครงสร้างโน้ตและอนุกรมวิธาน: [[Perfume_and_Note_Taxonomy]]
- หน้าเปรียบเทียบ: [[Compare_View]]
- พจนานุกรมข้อมูล: [[Data_Dictionary_Draft#notes|Data_Dictionary_Draft]]

---

## 6. Change Notes

- `2026-11-10`: จัดทำสเปกหน้ารายละเอียดน้ำหอมและพีระมิดโน้ตตามตัวอย่างใน README
