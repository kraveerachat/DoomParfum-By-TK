# DoomParfum By TK

> **Project Blueprint / Living README**
> Version: `0.2.0-planning` · Updated: `2026-11-10` (Asia/Bangkok)
> Status: **Planning baseline** — ยังไม่เริ่ม Implement โค้ด และเริ่มกระบวนการ Planning PR ตาม Workflow ของ Agent/GitHub
> Scope: **Private-first perfume research web app** (ไม่ใช่ Marketplace หรือระบบ Checkout)

---

## ภาพรวมโปรเจกต์ (Project Overview)

### DoomParfum คืออะไร?

**DoomParfum By TK** เป็นโปรเจกต์เว็บแอปแบบ **Private-first Perfume Research & Personal Collection** สำหรับศึกษาน้ำหอม ค้นหาและเปรียบเทียบกลิ่น จัดการรายการที่สนใจ ติดตามแหล่งซื้อ และบันทึกน้ำหอมที่เคยสั่งซื้อหรือครอบครอง โดยเริ่มจากการใช้งานส่วนตัว ไม่ใช่ร้านค้าออนไลน์

### ทำไมจึงสร้างโปรเจกต์นี้?

การพบรีวิวน้ำหอมผ่าน TikTok, YouTube หรือแพลตฟอร์มอื่นทำให้มีรายชื่อและลิงก์ที่ต้องค้นซ้ำหลายครั้ง ข้อมูล Notes, Accords, ความติดทน ความเห็นผู้ใช้ และร้านค้ามักกระจัดกระจาย DoomParfum จึงตั้งใจรวบรวมข้อมูลที่มีสิทธิ์ใช้และมีแหล่งอ้างอิงให้อยู่ในระบบเดียว พร้อมช่วยค้นหาน้ำหอมกลิ่นใกล้เคียงในงบที่เหมาะสม

### เป้าหมายและความสามารถที่วางแผนไว้

- **Perfume Catalogue:** ค้นหาน้ำหอมจาก Designer, Niche, Middle Eastern, Thai, Indonesian และแบรนด์อื่น ๆ โดยจำแนกประเทศกับประเภทแบรนด์แยกกัน
- **Scent Profile & Perfume Pyramid:** แสดง Top / Heart / Base Notes, Main Accords, ภาพโน้ตที่ใช้งานได้ตามสิทธิ์ และรายละเอียดลักษณะกลิ่น
- **Scent DNA Matching:** เลือกรุ่นอ้างอิง Designer/Niche แล้วค้นหาตัวเลือกที่ใกล้เคียงจาก Notes, Accords และหลักฐานรีวิวจริง พร้อมแยก Similarity Score จาก Evidence Confidence
- **Search & Filters:** ค้นหาตามโน้ต ตระกูลกลิ่น สถานการณ์ใช้งาน แบรนด์ ประเทศ และงบประมาณ (เช่น 1,000–2,000 บาท โดยปรับได้)
- **My Cart & Buying Sources:** บันทึกรายการที่สนใจ ลิงก์ร้านค้า (รวม Shopee) ราคา ขนาด และร้านที่เลือกไว้ **โดยไม่มี Checkout และไม่สั่งซื้อแทนผู้ใช้**
- **Purchase History & Collection:** บันทึกสถานะ Ordered / Owned / Previously Owned ด้วยมือ รองรับการซื้อซ้ำและ Dashboard สถิติในอนาคต
- **Research & Data Provenance:** เก็บที่มาข้อมูล สิทธิ์ใช้งาน วันตรวจสอบ และข้อจำกัด ไม่ดึงหรือคัดลอกข้อมูลจากแหล่งที่ไม่อนุญาตโดยอัตโนมัติ

### สถานะโปรเจกต์

**Planning / Documentation Bootstrap** — เอกสารและโครงสร้างการทำงานเป็นการเตรียมแผน **ยังไม่ใช่เว็บที่พัฒนาและเปิดใช้งานแล้ว**; เทคโนโลยีเช่น Next.js, TypeScript, PostgreSQL, Drizzle และ Docker เป็นเพียงข้อเสนอที่ปรับเปลี่ยนได้หลังการทบทวนแผน

### วิธีทำงานและเอกสาร

- [`AGENTS.md`](AGENTS.md): กฎสำหรับ AI Agent, เครื่องมือ และขอบเขตสิทธิ์
- [`DEVELOPMENT_WORKFLOW.md`](DEVELOPMENT_WORKFLOW.md): ขั้นตอนการออกแบบ Planning PR → เจ้าของ Merge → Implementation PR → เจ้าของ Merge
- [`Structure DB Obsidian/README.md`](Structure%20DB%20Obsidian/README.md): ฐานความรู้รายละเอียด Requirements, Domain, Data, Matching, UX, Engineering, Roadmap, Decision Log และรายงานการทำงาน

การตัดสินใจทางเทคนิคและข้อกำหนดที่ยังไม่ยืนยันต้องระบุสถานะอย่างโปร่งใส เอกสาร Obsidian คือรายละเอียดปฏิบัติการ ส่วน README ที่ Root คือภาพรวมของโปรเจกต์ ทั้งสองต้องสอดคล้องกัน

---

## 0. อ่านเอกสารนี้อย่างไร

เอกสารนี้เป็น **Single Source of Truth สำหรับข้อกำหนดระดับโปรเจกต์ ณ เวลาที่จัดทำ** ใช้ต่อยอดใน ChatGPT และเป็นข้อมูลตั้งต้นให้ Agent สร้างเอกสารละเอียดใน Obsidian ภายใต้ `Structure DB Obsidian/` โดยไม่ถือว่าทุกข้อเสนอด้านเทคนิคได้รับอนุมัติเป็นการตัดสินใจถาวร

สัญลักษณ์สถานะ:
- **[CONFIRMED]** สิ่งที่ผู้ใช้ระบุ/ยืนยันจากบทสนทนา
- **[PROPOSED]** แนวทางที่เสนอ รอยืนยันหรือปรับรายละเอียด
- **[RESEARCH]** ต้องทดสอบ/ตรวจสอบความถูกต้อง สิทธิ์ หรือความเป็นไปได้ก่อนใช้จริง
- **[DEFERRED]** เผื่อโครงสร้างไว้ แต่ยังไม่ใช่งานใน MVP

**กฎ:** หากขัดแย้งระหว่างเอกสารนี้กับคำสั่งผู้ใช้ใหม่ ให้บันทึกข้อเปลี่ยนแปลงใน Decision Log และแก้เอกสารที่เกี่ยวข้อง ไม่แก้เงียบ ๆ

---

## 1. Product Vision

**[CONFIRMED]** DoomParfum By TK คือเว็บแอปส่วนตัวสำหรับศึกษากลิ่นน้ำหอม จัดการรุ่นที่สนใจ เปรียบเทียบน้ำหอม Designer/Niche กับทางเลือกคุ้มค่าจากแบรนด์อาหรับ ไทย อินโดนีเซีย และแบรนด์อื่น ตลอดจนเก็บร้านค้า/ลิงก์สั่งซื้อและบันทึกประวัติที่เคยซื้อหรือครอบครอง

### 1.1 ปัญหาที่จะแก้
1. พบคำแนะนำจาก TikTok/YouTube/โซเชียล แล้วลืมว่าเคยดูรุ่นไหนหรือเก็บไว้ที่ใด
2. ต้องเปิดหลายเว็บเพื่อดู Top/Heart/Base Notes, Accords, ความเหมาะสมในการใช้ และรีวิว
3. ต้องค้นเองว่าแบรนด์ราคาย่อมเยามีน้ำหอมใกล้เคียงกับ Designer/Niche รุ่นต้นแบบหรือไม่
4. มีสินค้า/ลิงก์ใน Shopee หลายร้านและไม่รู้ว่าบันทึก/ซื้อ/เคยมีรุ่นนั้นแล้วหรือยัง
5. ต้องการวิเคราะห์คอลเลกชันส่วนตัวในอนาคต โดยไม่ทำระบบซื้อขายจริง

### 1.2 Non-goals: สิ่งที่ไม่ทำ
- **[CONFIRMED]** ไม่มีระบบจ่ายเงิน, สั่งซื้อจริง, checkout, ตัดสต็อกให้ร้าน หรือรับคำสั่งซื้อแทนผู้ใช้
- **[CONFIRMED]** "ตะกร้าในแอป" เป็น **รายการที่ผู้ใช้บันทึกไว้** ไม่ใช่ตะกร้า Shopee ที่ซิงก์อัตโนมัติ
- **[PROPOSED]** ไม่เริ่มด้วยการฝึก LLM ใหม่, ไมโครเซอร์วิส, Vector DB หรือการเก็บฐานข้อมูลทั่วโลกทั้งหมด
- **[PROPOSED]** ไม่เผยแพร่สำเนาข้อมูล/ภาพ/รีวิวจากแหล่งภายนอกหากไม่มีสิทธิ์ใช้งาน

### 1.3 Target User & Budget
- **[CONFIRMED]** เริ่มต้นด้วยผู้ใช้ส่วนตัวคนเดียว แต่ไม่ปิดทางรองรับผู้ใช้หลายคนในอนาคต
- **[CONFIRMED]** งบค้นหาน้ำหอมทางเลือกเริ่มต้นประมาณ **฿1,000–2,000** (แก้ตัวกรองได้)
- **[CONFIRMED]** ให้ Designer/Niche เป็น reference perfume และหาตัวเลือกกลิ่นคล้ายในตลาดราคาคุ้มค่า
- **[PROPOSED]** ระบบคิดราคา **ต่อ SKU/ขนาด/ร้าน** ไม่ตัดสินว่าแบรนด์ทั้งแบรนด์อยู่ในงบ

---

## 2. Functional Scope & Requirements

### 2.1 Catalogue, Research & Discovery

| ID | สถานะ | ข้อกำหนด |
|---|---|---|
| R01 | CONFIRMED | มีแคตตาล็อกน้ำหอมหลายประเทศ/หลายปี ไม่จำกัดเฉพาะของที่ผู้ใช้มี |
| R02 | CONFIRMED | จำแนก Country/Region และ Brand Positioning แยกคนละมิติ เช่น Designer, Niche, Independent, Inspired House |
| R03 | CONFIRMED | แสดง Top, Heart/Middle, Base Notes และ Accords |
| R04 | CONFIRMED | มีการกรองตาม Day/Night, การใช้งาน, กลุ่มเป้าหมาย/Unisex, ลักษณะกลิ่น และฤดูกาล |
| R05 | CONFIRMED | เลือก Designer/Niche รุ่นอ้างอิงเพื่อค้นหากลิ่นใกล้เคียง |
| R06 | CONFIRMED | รองรับตัวเลือกแบรนด์ Middle Eastern, Thai, Indonesian และกลุ่มราคาคุ้มค่าอื่น ๆ |
| R07 | CONFIRMED | เทียบโครงสร้าง Notes/Accords และข้อมูลจากรีวิว/หลักฐานความคล้าย |
| R08 | CONFIRMED | ค้นหาและกรองงบเริ่มต้นไม่เกิน ฿2,000 (ปรับได้) |
| R12 | CONFIRMED | มี AI Assistant ช่วยค้นคว้า/อธิบาย โดยต้องแสดงหลักฐานและแยกสิ่งที่ไม่รู้ |
| R13 | CONFIRMED | หน้ารายละเอียดมี **Perfume Pyramid พร้อมภาพโน้ต** Top / Middle / Base |
| R14 | CONFIRMED | กด Note แล้วค้นหารุ่นอื่นที่มีโน้ตนั้นได้ |
| R15 | CONFIRMED | เปรียบเทียบสองรุ่นแบบ Side-by-Side พร้อมไฮไลต์โน้ตที่ตรง/ต่าง |
| R16 | PROPOSED | ให้คะแนน Structural Similarity จากข้อมูลที่ตรวจสอบได้ |
| R17 | CONFIRMED | แสดงหลักฐานที่ระบุความคล้าย/ความต่างจากรีวิวภายนอกที่มีสิทธิ์ใช้ |
| R18 | PROPOSED | แยก Similarity Score ออกจาก Evidence Confidence |
| R19 | PROPOSED | ใช้ AI/ETL Agent นำเข้าข้อมูลจากแหล่งที่ใช้งานได้อย่างถูกต้อง |
| R20 | CONFIRMED | เพิ่มน้ำหอมที่ไม่อยู่ในฐานข้อมูลเปิดได้ โดยเฉพาะแบรนด์ไทย |
| R21 | PROPOSED | เก็บแหล่งอ้างอิง สิทธิ์ใช้ และวันที่ตรวจสอบของแต่ละข้อมูล/ภาพ |
| R22 | CONFIRMED | เพิ่ม Thai Brand Registry: **La Palette (lapalette), SCENTERY, BE CHERIE PARFUM, SÚNDALO** รวมทั้งแบรนด์ไทยก่อนหน้านี้ตามลำดับความสำคัญ |

### 2.2 Personal Cart, Buying Sources, Purchase History & Collection

> **คำจำกัดความสำคัญ [CONFIRMED]:** `My Cart` ใน DoomParfum คือ **ตะกร้าบันทึกส่วนตัว** สำหรับเก็บรุ่นที่เลือกและแหล่งซื้อ ไม่ใช่ระบบสั่งซื้อและไม่ผูกกับ Shopee Cart จริงโดยอัตโนมัติ

| ID | สถานะ | ข้อกำหนด |
|---|---|---|
| R09 | CONFIRMED | นำเข้าข้อมูลส่วนตัวจากลิงก์/ภาพหน้าจอ/รายการที่ผู้ใช้เตรียม (ไม่สมมติว่ามี Buyer Cart API) |
| R10 | CONFIRMED | เก็บร้านค้า Marketplace/Platform, ลิงก์ซื้อ, ราคา, ขนาด และตัวเลือกสินค้าได้หลายรายการต่อหนึ่งน้ำหอม |
| R11 | CONFIRMED | บันทึกสถานะสนใจ, วิจัย, ตะกร้าภายในแอป, ซื้อแล้ว, มีอยู่, ทดลองแล้ว, ไม่สนใจ |
| R23 | CONFIRMED | เพิ่มน้ำหอม **ทุกกลุ่มแบรนด์** เข้า `My Cart` ในแอปได้ |
| R24 | CONFIRMED | ใน `My Cart` ผูก **ลิงก์แหล่งซื้อหนึ่งหรือหลายลิงก์** และโน้ตร้านที่ไว้ใจ/เหตุผลเลือกได้ |
| R25 | CONFIRMED | ผู้ใช้ **เปลี่ยนสถานะว่า “สั่งซื้อแล้ว/ซื้อแล้ว” ด้วยมือ** โดยไม่เกิดธุรกรรมในแอป |
| R26 | CONFIRMED | เก็บประวัติว่าเคยซื้อ/เคยมีรุ่นอะไรแล้ว แม้ภายหลังหมดขวด/ขาย/ให้ผู้อื่น |
| R27 | CONFIRMED | รองรับ Dashboard สรุปน้ำหอมที่เคยซื้อ/มีอยู่ แยกแบรนด์ ประเภทกลิ่น Notes และหมวดอื่น ๆ |
| R28 | PROPOSED | เก็บ purchase record แยกจาก ownership/inventory (ซื้อซ้ำหลายครั้งได้) |
| R29 | PROPOSED | เก็บราคาที่จ่ายจริง ปริมาณ ขนาด วันที่ซื้อ ร้านค้า และสถานะรับสินค้าเป็นข้อมูลเสริมที่ไม่บังคับ |
| R30 | PROPOSED | ป้องกันการบันทึกน้ำหอมเดียวกันซ้ำโดยเตือนและให้เพิ่มแหล่งซื้อแทน |
| R31 | DEFERRED | สรุปใช้จ่าย/ราคาเฉลี่ยต่อ mL/จำนวนขวด/แนวกลิ่นที่สะสมและสถิติย้อนหลัง |

**ตัวอย่าง User Journey (ไม่ใช่ Checkout)**
1. พบ `Perfume A` จากคลิปรีวิว → บันทึกรุ่นเข้า `Wishlist` หรือ `My Cart`
2. กด `Save Buying Source` → บันทึกลิงก์ร้าน Shopee + ขนาด + ราคาที่เห็น + เวลาบันทึก
3. ถ้าได้สั่งซื้อภายนอกแล้ว → กด `Mark as Ordered` พร้อมรายละเอียดที่ต้องการ
4. เมื่อได้ของแล้ว → กด `Mark as Received / Owned` และบันทึกขวดในคอลเลกชัน
5. เมื่อใช้หมด/ขาย/ให้คนอื่น → เปลี่ยนสถานะขวดใน Inventory แต่ **ประวัติการซื้อยังอยู่**
6. Dashboard อ่านจาก `purchase_records` / `inventory_items` ไม่ใช่แค่สถานะตะกร้า

**อย่าปะปนคำเหล่านี้:** `Saved Buying Source` = มีแหล่งซื้อที่บันทึกไว้, `In App Cart` = อยู่ในรายการเตรียมซื้อ, `Ordered` = ผู้ใช้รายงานว่าสั่งภายนอกแล้ว, `Owned` = มีขวดจริงในครอบครอง, `Previously Owned` = เคยมีแต่ปัจจุบันไม่มี

---

## 3. Scope ของแบรนด์และชื่อรุ่น

### 3.1 หลักการ Taxonomy
- `origin_country`: ประเทศต้นกำเนิดแบรนด์ (ไม่ใช่ประเทศที่ผลิตทุกล็อต)
- `market_position`: Designer / Niche / Independent / Mass Market / Inspired House / Unknown; **ไม่บังคับให้เป็นหมวดที่ห้ามซ้อนกัน** หากต้องการหลายป้ายให้ใช้ tag relation
- `product_relationship`: Inspired By / Reported Dupe / Similar Profile / Community Comparison / Other; เป็นความสัมพันธ์ **ระหว่างน้ำหอมสองรุ่น** ไม่ใช่ตัดสินทั้งแบรนด์
- `family` และ `accords` แยกจาก `notes` และ `ingredient_materials`
- `target_audience`, `occasion`, `season` อาจเป็นข้อมูลที่ขึ้นกับแหล่งอ้างอิงและความเห็นส่วนบุคคล ไม่ใช่ความจริงตายตัว

### 3.2 Brand Registry ที่ผู้ใช้ให้ความสำคัญ
- **Thailand:** La Palette (lapalette), SCENTERY, BE CHERIE PARFUM, SÚNDALO; เสริมแบรนด์ไทยอื่นเมื่อยืนยันชื่อและสินค้าได้
- **Middle East:** เช่น Lattafa, Armaf, Afnan, Rasasi, Paris Corner, Fragrance World (ตัวอย่างลิสต์เริ่มต้น ต้องตรวจสอบเป็นรายรุ่น)
- **Indonesia:** เช่น HMNS, SAFF & Co., Mykonos (ตัวอย่างลิสต์สำรวจ ไม่ยืนยันสินค้าทุกรุ่น/ราคา/การขายในไทย)
- **Designer/Niche:** ใช้เป็น Reference Pool สำหรับเทียบกลิ่น ไม่จำเป็นต้องมีร้านค้าราคาประหยัด
- ตัวอย่างรายการในตะกร้าที่ผู้ใช้ส่งเป็นภาพ: `BE CHERIE White Instinct`, `BE CHERIE Love White [ตรวจสอบชื่อรุ่น]`, `SÚNDALO Rhapsody Sky`, `SÚNDALO Unspoken Rose`; ยัง **ไม่ถือเป็นรายการที่นำเข้าระบบจริง**

---

## 4. Data Architecture — Conceptual Model

> **[PROPOSED]** ส่วนนี้เป็นแบบจำลองเชิงแนวคิด Agent ต้องขยายเป็น ERD และ Data Dictionary ก่อนเขียน migration

### 4.1 Perfume Master Data

| Entity / Table | จุดประสงค์หลัก | ความสัมพันธ์สำคัญ |
|---|---|---|
| `brands` | แบรนด์ ชื่อแฝง ประเทศ ตำแหน่งตลาด | 1 brand → many perfumes |
| `perfumes` | รุ่น/สูตรกลิ่นที่เป็นเอกลักษณ์ ชื่อ concentration, release year, flanker/version | many perfumes → 1 brand |
| `product_variants` | ขนาด/แพ็ก/ความเข้มข้นกรณีเป็น SKU ต่างกัน | many variants → 1 perfume |
| `notes` | คลังโน้ตที่ Normalize พร้อมชื่อไทย/อังกฤษ | many-to-many perfumes |
| `note_aliases` | ชื่อพ้อง เช่น Heart/Middle, สะกดต่างรูป | many aliases → 1 note |
| `perfume_notes` | Note + top/middle/base + ranking/source | join perfumes ↔ notes |
| `accords` | Family/Accord เช่น Woody, Amber, Aromatic | many-to-many perfumes |
| `perfume_accords` | ลำดับ/น้ำหนัก Accord ตามแหล่งข้อมูล | join perfumes ↔ accords |
| `note_images` | ภาพวัตถุดิบ/ไอคอนพร้อม license/attribution | many images → 1 note |
| `perfume_images` | ภาพผลิตภัณฑ์ที่ใช้ได้อย่างถูกต้อง | many images → 1 perfume/variant |
| `source_records` | provenance, URL, type, checked_at, permission/license, confidence | reference หลาย entity |

### 4.2 Matching & Research

| Entity / Table | จุดประสงค์ |
|---|---|
| `perfume_relations` | คู่รุ่น A–B และประเภทความสัมพันธ์ (มีทิศทางหาก Inspired By) |
| `comparison_evidence` | หลักฐานรีวิว/ความคล้าย อ้างอิง source + วันที่ + ประเภทคำกล่าว + ข้อขัดแย้ง |
| `review_aggregates` | คะแนนความชอบ/ความติดทน/โหวต (แยกกับคะแนนความคล้าย) |
| `matching_results` | คะแนนคำนวณ, ส่วนประกอบคะแนน, algorithm_version, data_version, confidence |
| `social_sources` | ลิงก์โพสต์/คลิป แพลตฟอร์ม ผู้สร้างคอนเทนต์ วันที่บันทึก |
| `ingestion_jobs` | ประวัติงาน import/normalize/validation/error/retry |

### 4.3 Shopping & Ownership (แยกจาก Master Data)

| Entity / Table | จุดประสงค์ | หมายเหตุ |
|---|---|---|
| `users` | ผู้ใช้/เจ้าของข้อมูล | รองรับ single-user ก่อน |
| `user_lists` | ชื่อรายการ เช่น Wishlist, My Cart, To Test, Skipped | `My Cart` ไม่ checkout |
| `user_list_items` | สมาชิกของรายการและเวลาที่เพิ่ม | allow หลาย list ต่อ perfume |
| `retail_listings` | ร้านค้า แพลตฟอร์ม URL/SKU/ขนาด/ราคา ณ เวลาตรวจสอบ | many listings → one perfume/variant |
| `saved_buying_sources` | ผู้ใช้ผูกแหล่งซื้อที่เลือกไว้กับรายการ | บันทึกหลายลิงก์ได้ |
| `price_observations` | สแนปช็อตราคา + สกุลเงิน + collected_at | ไม่แสดงเป็น live หากไม่ใช่ live |
| `purchase_records` | ประวัติสั่ง/ซื้อจริงที่ผู้ใช้กรอกเอง, paid_price, ordered_at, received_at | ซื้อรุ่นเดิมซ้ำหลายครั้งได้ |
| `inventory_items` | ขวดที่ครอบครอง สถานะ owned/finished/sold/gifted | เชื่อม purchase ถ้ามี |
| `personal_reviews` | ความรู้สึกหลังลองกลิ่น, performance ส่วนตัว | ไม่ใช่ community data |

**กฎข้อมูลขั้นต่ำ:**
- `perfume` ≠ `retail_listing` ≠ `purchase_record` ≠ `inventory_item` (เป็นคนละแนวคิด)
- 1 รุ่นมีหลายขนาด หลายร้าน หลาย purchase record ได้
- ตั้ง canonical perfume ID แล้วใช้ alias/matching ป้องกันชื่อสินค้า Shopee ที่ผสมคีย์เวิร์ด SEO
- แยก `ordered_at` ออกจาก `received_at` และ `owned_since`; ไม่มีวันที่ต้องเก็บเป็น `null` ไม่คาดเดา
- คำว่า `Top/Middle/Base Notes` เป็น **olfactory notes** ไม่ใช่สูตรเคมี/วัตถุดิบจริงที่ผู้ผลิตใช้ปรุง
- ข้อมูลราคาเป็น observation ณ วันเวลา/ขนาด/ร้าน ระบุ currency เสมอ

---

## 5. Scent DNA Matching — Proposed Logic

### 5.1 Pipeline
1. เลือก `Reference Perfume` จาก Designer/Niche หรือรุ่นใด ๆ
2. หา Candidate จากกลุ่มประเทศ/แบรนด์/ช่วงราคา/availability ที่ **มีข้อมูลจริง**
3. Normalize Notes และ Synonyms → เปรียบเทียบ **Top, Heart, Base**
4. เปรียบเทียบ Accords, Family และโครงสร้างกลิ่นโดยรวม
5. รวมหลักฐาน `Reported Similarity` จากรีวิวที่ได้รับสิทธิ์ใช้งาน
6. แสดง **structural match, community evidence, confidence** แยกอย่างชัดเจน
7. อธิบายความเหมือน/ต่าง รวมโน้ตที่ตรง ชั้นที่ไม่ตรง และข้อควรระวัง

### 5.2 คะแนน (ค่าทดลอง ไม่ใช่ค่าที่ยืนยัน)
- [PROPOSED] `Note Pyramid` 40%; `Accords` 25%; `Fragrance Family` 15%; `Evidence` 20%
- คิดคะแนนจาก feature ที่มี **พร้อมระบุ coverage**; ข้อมูลที่ไม่มีต้องไม่ถูกตีความว่าเป็น 0 หรือ 100 โดยอัตโนมัติ
- อาจใช้ Weighted Jaccard สำหรับ sets และแยกน้ำหนัก Note ตามชั้น/ความเด่น
- `similarity_score` คือ **ความคล้ายตามโมเดลข้อมูล** ไม่ใช่เปอร์เซ็นต์ที่คนจะดมแล้วเหมือนจริง
- `evidence_confidence` พิจารณา coverage, number/independence of sources, freshness, contradictions และ quality
- แยก Overall Rating / Popularity ออกจาก Similarity Evidence; **Rating สูงไม่ได้แปลว่ากลิ่นคล้าย**
- [DEFERRED] ทำ learning-to-rank/train model เมื่อมี labeled scent pairs ที่ใช้งานได้ถูกต้องและมากพอ

### 5.3 ผลลัพธ์ 3 แบบ
- `Documented Alternative`: มีหลักฐานระบุว่าใกล้เคียงกับคู่ต้นแบบ
- `Profile Similarity`: มี Notes/Accords/Family ใกล้เคียงตามสูตร
- `Same Vibe`: บุคลิกคล้าย แต่ไม่ได้รับรองเป็น Dupe

### 5.4 ตัวอย่าง UI ที่ต้องการ
- Perfume Detail: ภาพโน้ต Top/Heart/Base เรียงอย่างในตัวอย่างภาพของผู้ใช้
- Compare: สองขวดเคียงกัน, Highlight match/mismatch, Evidence Summary, Confidence
- Browse: ค้นหาจากชื่อ/แบรนด์/โน้ต/accord/ราคา/การใช้งาน/ประเทศ
- My Cart: รายการบันทึก + ลิงก์ร้าน + เปลี่ยนสถานะด้วยมือ
- Collection Dashboard: เคยซื้ออะไร, มีอยู่, เคยมี, สัดส่วน families/brands/notes, งบ/ค่าใช้จ่ายหากบันทึก

---

## 6. Data Collection & Responsible Ingestion

### 6.1 Sources & Priority
1. **[RESEARCH]** Open datasets ที่มีใบอนุญาตชัดเจน (เช่น Scento perfume dataset) เพื่อ seed catalogue
2. **[RESEARCH]** Official/partner APIs ที่เงื่อนไขรองรับรูปแบบการใช้งานและการจัดเก็บ
3. **[RESEARCH]** เว็บไซต์เจ้าของแบรนด์/ร้านค้าเมื่อได้รับอนุญาตหรือข้อมูลเผยแพร่ให้ใช้ตามเงื่อนไข
4. **[CONFIRMED]** User Input: ลิงก์ Shopee, สรุปส่วนตัว, CSV, ภาพหน้าจอที่ผู้ใช้นำเข้าและตรวจยืนยัน
5. **[RESEARCH]** Social/review evidence จากแหล่งที่สามารถนำเนื้อหามาใช้ได้ ไม่เก็บคัดลอกรีวิวจำนวนมากโดยไม่มีสิทธิ์

### 6.2 Fragrantica และ Scraping
- Fragrantica ใช้เป็น **reference/source discovery** สำหรับการตรวจสอบด้วยตนเองได้ตามเงื่อนไขที่เกี่ยวข้อง
- **ห้ามตั้งสมมติฐานว่าการพบ Scraper บน GitHub = ได้รับอนุญาตให้ดึงข้อมูลจำนวนมาก**
- ตรวจ Terms, robots, API access, copyright, storage/republication/AI use; หากข้อกำหนดห้ามหรือไม่มีสิทธิ์ ให้ **ไม่ทำ automated extraction** จากแหล่งนั้น
- ไม่ออกแบบงานเพื่อ bypass CAPTCHA, login, rate limit หรือกลไกป้องกัน
- หากสิทธิ์ไม่ชัด ให้เก็บ **ลิงก์อ้างอิงและข้อมูลที่ผู้ใช้บันทึกเอง** ไม่ดึงข้อมูล/ภาพ/รีวิวโดยพลการ

### 6.3 Tools (ยังไม่บังคับใช้)
- `Python + Jupyter / Google Colab`: exploratory ETL, test normalization & similarity
- `Scrapy / Playwright`: ใช้ **เฉพาะแหล่งที่อนุญาต** และจำกัดอัตราคำขอ
- `API Client`: ถ้ามี official API ที่รองรับวัตถุประสงค์
- `AI Research Agent`: ตรวจชื่อรุ่นและความขัดแย้ง สรุปหลักฐาน ยื่นข้อมูลรออนุมัติก่อนเข้า canonical DB
- `PostgreSQL`: ฐานข้อมูลหลัก, separate data provenance

### 6.4 Data Quality Gates
- normalized brand/name/version/concentration/volume ก่อน dedup
- ตรวจ license, provenance, source URL, checked_at, field-level evidence
- uncertain / contradictory / missing มีสถานะเป็นข้อมูล ไม่ใช้ AI เติมให้เหมือนข้อเท็จจริง
- `draft` → `reviewed` → `approved` ก่อนใช้เป็น reference ใน matching production
- ภาพโน้ตและขวดต้องมี rights/attribution (หรือสร้าง artwork ของตัวเอง) และ alt text

---

## 7. Technical Architecture (Proposed, not locked)

```text
[Next.js / TypeScript / PWA]
         |
[App API / Auth / Validation]
         |
[PostgreSQL + Drizzle ORM]
         |
[Catalogue] [Matching Engine] [User Collections]
         ^
         |
[Permitted APIs / Licensed datasets / User Imports]
         |
[ETL & Validation + AI Research Assistant]
```

- Frontend: Next.js, TypeScript, Tailwind CSS, shadcn/ui
- Backend: Next.js Route Handlers (สำหรับ MVP)
- Database: PostgreSQL; ORM: Drizzle
- Search: Postgres Full-Text + Trigram ก่อนพิจารณา Vector DB
- Deployment: Docker Compose; Private-first access; Secrets ผ่าน environment ไม่ commit
- Image storage: URI/asset storage พร้อม license metadata ไม่ใช้ Hotlink โดยไม่มีสิทธิ์
- Auth: แม้ single user ต้องมีการป้องกันข้อมูลส่วนตัว/ปิด public endpoints ของ admin/import
- **หมายเหตุ:** เทคโนโลยีด้านบนเป็น [PROPOSED] ไม่ถือว่าเลือกแล้วจนกว่าจะมี Architecture Decision Record (ADR)

---

## 8. Roadmap / Delivery Phases

| Phase | เป้าหมาย | Deliverable หลัก |
|---|---|---|
| P0 — Documentation | Requirement + Vault Structure + Decisions | README + Obsidian specs + backlog |
| P1 — Foundation | Data Schema, seed dataset, Brand/Perfume catalogue | Search, Detail, Note Pyramid |
| P2 — Matching | Compare Notes/Accords + evidence model | Scent Matching & explanation |
| P3 — My Cart & Ownership | บันทึกแหล่งซื้อ, สถานะ Ordered/Owned, purchase records | My Cart, Source Links, Collection |
| P4 — Dashboard | สรุปเคยซื้อ/ครอบครอง และสถิติจากข้อมูลผู้ใช้ | Ownership Dashboard |
| P5 — AI Research | AI ช่วยค้นคว้า/ตรวจสอบหลักฐาน/เสนอข้อมูล | Human-reviewed research pipeline |
| P6 — Expansion | เพิ่มแบรนด์ไทย/อาหรับ/อินโด, ปรับ Ranking | Coverage & quality improvements |

**เงื่อนไขก่อนเริ่ม Code:** Finalize domain model, data policy, MVP acceptance criteria, selection of dataset/API rights, and first screen map.

---

## 9. Project Layout (วางโครงเบื้องต้น ไม่ใช่โค้ดที่สร้างแล้ว)

```text
DoomParfum By TK/
├── README.md                       # This project blueprint
├── Structure DB Obsidian/          # Obsidian vault สำหรับ spec, decision, change log
│   └── README.md                   # Agent bootstrap prompt & vault contract
├── web/                            # [FUTURE] Next.js app
├── data-pipeline/                  # [FUTURE] ETL, validation and import scripts
├── database/                       # [FUTURE] schema, migrations, seed
└── .github/                        # [FUTURE] CI/review workflow หลังผู้ใช้ส่ง workflow ตัวอย่าง
```

**GitHub policy ขณะนี้:**
- [CONFIRMED] มีแผนเก็บทั้ง Source Code และ Obsidian Markdown บน GitHub
- [OPEN] ยังไม่กำหนด Repository (ชื่อ/URL/visibility), branch strategy, PR rules, push permissions, CI, agent workflow
- [PROPOSED] เก็บเอกสารและโค้ดใน repository เดียวก่อนเพื่อ trace changes; ประเมิน repo แยกภายหลัง
- [PROPOSED] Commit เฉพาะ docs/source; ไม่ commit `.env`, API keys, session/cookies, order references, private user exports, copyrighted content/raw scrape, หรือข้อมูลที่ไม่มีสิทธิ์เผยแพร่
- **ห้าม Agent push / create repo / sync vault โดยอัตโนมัติจนกว่าผู้ใช้ระบุ Workflow และอนุญาต**

---

## 10. Decision Register

| ID | Decision | สถานะ |
|---|---|---|
| DEC-001 | DoomParfum เป็น Research/Comparison/Collection App ไม่ใช่ E-commerce | CONFIRMED |
| DEC-002 | `My Cart` เป็น Saved Items + Buying Sources ในแอป ไม่ sync Shopee Cart โดยตรง | CONFIRMED |
| DEC-003 | มี Manual Ordered/Owned Status และ Purchase/Ownership History | CONFIRMED |
| DEC-004 | Designer/Niche เป็น reference; ทางเลือกให้เน้น value <= ฿2,000 (ปรับได้) | CONFIRMED |
| DEC-005 | แยก Brand Origin กับ Market Position | PROPOSED |
| DEC-006 | เริ่ม Rule-Based Similarity + source-backed evidence; ไม่ train ใหม่ทันที | PROPOSED |
| DEC-007 | เปิดรับข้อมูลจาก licensed datasets/APIs และ user import; scrape เฉพาะเมื่อได้รับอนุญาต | PROPOSED (ข้อจำกัดสิทธิ์ต้องปฏิบัติ) |
| DEC-008 | Next.js/PostgreSQL/Drizzle/Docker เป็น Stack ตั้งต้น | PROPOSED |
| DEC-009 | Obsidian vault ใช้สำหรับ living design/decision docs และ GitHub เป็น version control | CONFIRMED (วิธี sync ยัง OPEN) |

## 11. Open Questions — รอรายละเอียดเพิ่มเติม

1. จะเก็บค่าความคล้ายโดยให้น้ำหนัก Notes มากกว่า Community Reviews หรือใช้แบบผสมอย่างไร? (Draft 40/25/15/20 ยังเป็นข้อเสนอ)
2. รีวิว Creator จาก TikTok/YouTube เป็น **primary evidence** หรือ **supporting evidence**? และจะนำมาเก็บแบบใดให้ตรงสิทธิ์?
3. รักษาความเป็นส่วนตัวแบบ Single-user ตลอดหรือเตรียมระบบ Multi-user?
4. ราคา/การมีขาย: ต้องเก็บเฉพาะ Shopee หรืออนุญาตแหล่งซื้ออื่น?
5. Purchase History ต้องมีรายละเอียดขั้นต่ำอะไรบ้าง? (`date`, `price`, `volume`, `seller` เป็น optional ใน V1)
6. เลือก dataset/API ใดเมื่อทดสอบสิทธิ์ใช้งานและ coverage ของ Thai/Arabic/Indonesian brands แล้ว?
7. GitHub repo, Obsidian sync, Coding Agent, ChatGPT workflow และ commit/PR rules — **รอไฟล์ workflow ตัวอย่างจากผู้ใช้**

---

## 12. Next Actions (Documentation-first)

1. วาง `README.md` นี้ใน root `DoomParfum By TK/`
2. วาง `Structure DB Obsidian/README.md` ใน vault ที่ผู้ใช้จัดเตรียม
3. ส่งไฟล์ README ฝั่ง Obsidian ให้ Agent อ่าน แล้วสั่งสร้าง Vault Structure และ Markdown ตามคำสั่งในเอกสารนั้น
4. Review เอกสาร `Requirements`, `Domain_Model`, `Data_Dictionary`, `Scent_Matching`, `My_Cart_and_Ownership`, `Data_Sources` ก่อน implement
5. เมื่อผู้ใช้ส่ง Workflow ตัวอย่างของ ChatGPT/Agent ให้เพิ่มแผน GitHub + Automation โดยใช้ ADR
6. **ยังไม่สร้างระบบ Checkout และยังไม่เริ่ม Scrape แหล่งข้อมูลที่ไม่มีสิทธิ์**

### References to evaluate (ไม่ใช่การยืนยันความถูกต้องหรือสิทธิ์ของทุกแหล่ง)
- Fragrantica brand index: https://www.fragrantica.com/designers/
- Scento dataset: https://github.com/Scento-com/perfume-dataset
- Scento API: https://www.scento.com/developers/perfume-api
- Scrapy documentation: https://docs.scrapy.org/
- Playwright: https://playwright.dev/
- Openverse API: https://api.openverse.org/v1/

---

**Maintenance contract:** เมื่อแก้ Scope / Feature / Data Model / Ranking / Tooling ให้แก้ README ที่เกี่ยวข้อง, Update Obsidian decision/changelog, และเปิดคำถามที่ยังไม่ยืนยันไว้ชัดเจน การแก้เอกสารไม่เท่ากับอนุมัติให้ Deploy/Push/สืบค้นข้อมูลอัตโนมัติ
