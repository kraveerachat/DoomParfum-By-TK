---
id: DPT-UX-003
project: DoomParfum By TK
type: ux_screen_spec
status: draft
owner: project
updated: 2026-11-10
tags:
  - doomparfum
  - ux
  - screens
  - compare
  - matching
source_of_truth: "../README.md"
---

# Screen Spec: Side-by-Side Compare — DoomParfum By TK

> **Document Type:** UI/UX Screen Specification
> **Target Route:** `/compare?ref=:id&cand=:id`
> **Source Baseline:** `../README.md` (Section 2.1 & 5.4)
> **Status:** Draft / Confirmed UX Spec

---

## 1. Purpose / Scope

เอกสารนี้กำหนดข้อกำหนดการออกแบบและการโต้ตอบสำหรับ **หน้าระบบเปรียบเทียบน้ำหอมสองรุ่นเคียงข้างกัน (Side-by-Side Compare View)** โดยเน้นการเปรียบเทียบระหว่างรุ่นอ้างอิง (Reference) และรุ่นทางเลือก (Alternative) พร้อมไฮไลต์โน้ตที่ตรงกัน โน้ตที่ต่าง และการแสดงหลักฐานเชิงประจักษ์

---

## 2. Layout Wireframe & Comparison Grid

```text
+-------------------------------------------------------------------------+
| [<- Back]    DoomParfum By TK — Scent Comparison                       |
+-------------------------------------------------------------------------+
|                                                                         |
|  OVERALL MATCH: 82% [Profile Similarity]    CONFIDENCE: HIGH [Verified] |
|  [=== Structural Similarity: 82% ===]       [=== Evidence: 85% ===]     |
|                                                                         |
+------------------------------------+------------------------------------+
|  REFERENCE PERFUME                 |  ALTERNATIVE CANDIDATE             |
|  Dior                              |  BE CHERIE PARFUM                  |
|  Sauvage EDT                       |  White Instinct                    |
|  Origin: France | Position: Designer| Origin: Thailand | Position: Indie|
|  Est. Price: ฿4,500                |  Saved Source Price: ฿1,290        |
|  [View Detail]                     |  [+ Add to My Cart]                |
+------------------------------------+------------------------------------+
|  MAIN ACCORDS COMPARISON:                                               |
|  Citrus, Fresh Spicy, Amber, Woody | Citrus, Fresh Spicy, Aromatic,Woody|
+------------------------------------+------------------------------------+
|  TOP NOTES:                                                             |
|  - Calabrian Bergamot [MATCH 🟢]   | - Bergamot [MATCH 🟢]              |
|  - Pepper [MATCH 🟢]               | - Pink Pepper [SIMILAR 🟡]         |
+------------------------------------+------------------------------------+
|  HEART NOTES:                                                           |
|  - Sichuan Pepper                  | - Cardamom [DIFF ⚪]               |
|  - Lavender [MATCH 🟢]             | - Lavender [MATCH 🟢]              |
|  - Geranium [MATCH 🟢]             | - Geranium [MATCH 🟢]              |
+------------------------------------+------------------------------------+
|  BASE NOTES:                                                            |
|  - Ambroxan [MATCH 🟢]             | - Ambroxan [MATCH 🟢]              |
|  - Cedar                           | - Cedarwood [MATCH 🟢]             |
|  - Labdanum                        | - Vetiver [DIFF ⚪]                |
+------------------------------------+------------------------------------+
|  WHY THEY ARE SIMILAR (คำอธิบายทางสุคนธศาสตร์):                         |
|  "ทั้งสองรุ่นแชร์ DNA เด่นร่วมกันคือ กลิ่นเปิดซิตรัสสดชื่น (Bergamot)  |
|  ผสานความเผ็ดสะอาดของ Lavender และ Geranium ในช่วงกลาง โดยมีกลิ่นฐาน    |
|  Ambroxan และ Cedarwood ให้ความทนทานและอบอุ่นแบบเดียวกัน               |
|  ข้อแตกต่าง: White Instinct มีกลิ่น Vetiver ชัดกว่า ทำให้โทนเขียวโปร่ง" |
+-------------------------------------------------------------------------+
|  COMMUNITY & REVIEW EVIDENCE:                                           |
|  - "กลิ่นเปิดฉีดแรกให้ฟีลคล้าย Sauvage 80% แต่ดรายดาวน์นุ่มกว่า ไม่บาดจมูก"|
|    ที่มา: TikTok @PerfumeReviewerTH (15 ก.ย. 2026) [ลิงก์]              |
+-------------------------------------------------------------------------+
```

---

## 3. Visual Highlighting Rules (กติกาการแสดงสีไฮไลต์)

- 🟢 **Exact / Canonical Match (สีเขียว):** โน้ตที่ตรงกันในชั้นเดียวกัน (เช่น Bergamot $\leftrightarrow$ Bergamot)
- 🟡 **Partial / Cross-layer Match (สีเหลืองอ่อน):** โน้ตในตระกูลเดียวกันหรืออยู่คนละชั้น (เช่น Pink Pepper ใน Top $\leftrightarrow$ Sichuan Pepper ใน Heart)
- ⚪ **Divergent Note (สีเทาอ่อน):** โน้ตที่มีเฉพาะในรุ่นใดรุ่นหนึ่ง ทำให้ผู้ใช้เห็นว่ารุ่นทางเลือกจะเพิ่มมิติกลิ่นใดเข้ามา

---

## 4. Interaction Features

1. **Swap Columns:** ปุ่มสลับฝั่งระหว่าง Reference และ Alternative เพื่อมุมมองที่ต้องการ
2. **Change Candidate:** เมนู Dropdown หรือปุ่มเลือก Candidate อื่นในลิสต์แนะนำมาเปรียบเทียบทันที
3. **One-click Add Alternative to Cart (R23):** ปุ่มลัดสำหรับกดเพิ่มรุ่นทางเลือกลงใน `My Cart` ทันทีที่พึงพอใจในความคล้ายคลึง

---

## 5. Requirements Covered

- [[Requirements_Register#R05|R05]] — Reference Scent Lookup
- [[Requirements_Register#R07|R07]] — Notes/Accords & Review Evidence Comparison
- [[Requirements_Register#R15|R15]] — Side-by-Side Comparison with Highlighting
- [[Requirements_Register#R16|R16]] — Structural Similarity Display
- [[Requirements_Register#R17|R17]] — External Review Evidence Display
- [[Requirements_Register#R18|R18]] — Separate Confidence Badge

---

## 6. Dependencies & Links

- สเปกการคำนวณการจับคู่: [[Scent_Matching_Spec]]
- หลักฐานรีวิว: [[Review_Evidence_and_Confidence]]
- หน้ารายละเอียดพีระมิด: [[Perfume_Detail_Pyramid]]

---

## 7. Change Notes

- `2026-11-10`: ร่างสเปกหน้าจอเปรียบเทียบ Side-by-Side พร้อมระบบสีไฮไลต์และกล่องคำอธิบาย
