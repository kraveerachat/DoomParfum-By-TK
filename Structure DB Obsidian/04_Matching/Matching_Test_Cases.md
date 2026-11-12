---
id: DPT-MAT-003
project: DoomParfum By TK
type: test_specification
status: draft
owner: project
updated: 2026-11-11
tags:
  - doomparfum
  - matching
  - testing
  - test_cases
source_of_truth: "../README.md"
---

# Matching Test Cases — DoomParfum By TK

## Dual-mode test specification extension — PROPOSED, 2026-11-11

[[Dual_Mode_Matching_Acceptance_Tests]] defines50 future deterministic A/B1/B2, missing-data, rights,
privacy and operational cases with explicit expected outcomes. Legacy examples below are synthetic
v0 illustrations, not new-version numerical oracles, product facts, measured sensory accuracy or PASS
results. New formulas keep structural fit, data confidence and pair evidence independent.

> **Document Type:** Algorithm Verification & Simulated Test Scenarios
> **Source Baseline:** `../README.md` (Section 5)
> **Status:** Draft / Conceptual Test Suite

---

## 1. Purpose / Scope

เอกสารนี้รวบรวมกรณีทดสอบจำลอง (Abstract & Synthetic Test Cases) เพื่อใช้ตรวจสอบความถูกต้องของตรรกะใน [[Scent_Matching_Spec]] โดยใช้ข้อมูลทดสอบเชิงสังเคราะห์ เพื่อป้องกันไม่ให้มีการกุตัวเลขคะแนนความแม่นยำในโลกจริงขึ้นมาโดยไม่มีการทดลองทางวิทยาศาสตร์รองรับ

---

## 2. Testing Principles

> [!NOTE]
> ตัวเลขคะแนนในกรณีทดสอบเหล่านี้เป็น **ค่าคาดหวังตามสมมติฐานทางคณิตศาสตร์ของโมเดล** ไม่ใช่การเคลมว่าคนจริงดมแล้วจะรู้สึกตรงตามตัวเลข 100%

---

## 3. Synthetic Test Cases

### TC-MAT-01: Identical Pyramid & Accords (คู่เหมือนทางทฤษฎี)
- **วัตถุประสงค์:** ตรวจสอบว่าหากสองรุ่นมีโน้ตและแอคคอร์ดเหมือนกันทุกประการ คะแนนต้องสูงสุด
- **ข้อมูลจำลอง:**
  - *Perfume A (Ref):* Top (Bergamot, Lemon), Heart (Lavender, Geranium), Base (Cedarwood, Ambroxan), Accords (Citrus 40%, Fresh Spicy 30%, Woody 30%)
  - *Perfume B (Cand):* โน้ตและแอคคอร์ดตรงกับ Perfume A 100% + มีรีวิวระบุว่าเป็นคู่โคลนตรง
- **ผลลัพธ์ที่คาดหวัง:**
  - $S_{notes} = 1.0$, $S_{accords} = 1.0$, $S_{family} = 1.0$, $S_{evidence} = 1.0$
  - Composite Score: $\approx 95\% - 100\%$
  - Tier: **Documented Alternative**
  - Confidence: **High**

---

### TC-MAT-02: Shared Base & Heart, Different Top (กลิ่นเปิดต่างแต่ดรายดาวน์เหมือน)
- **วัตถุประสงค์:** ตรวจสอบการถ่วงน้ำหนักชั้นโน้ต โดยกลิ่นเปิดต่างกันแต่หัวใจและฐานตรงกัน
- **ข้อมูลจำลอง:**
  - *Perfume Ref:* Top (Grapefruit), Heart (Ginger, Nutmeg), Base (Sandalwood, Incense, Patchouli)
  - *Perfume Cand:* Top (Apple, Mint), Heart (Ginger, Nutmeg), Base (Sandalwood, Incense, Patchouli)
- **ผลลัพธ์ที่คาดหวัง:**
  - $S_{notes}$: Top ต่ำ แต่ Heart และ Base สูง ทำให้คะแนนรวมยังอยู่ในเกณฑ์ดี ($\approx 65\% - 75\%$)
  - Tier: **Profile Similarity**
  - Explainability: ต้องระบุใน UI ชัดเจนว่า "กลิ่นเปิดเปิดคนละโทน (Grapefruit vs Apple/Mint) แต่ช่วงดรายดาวน์ให้กลิ่นฐานไม้หอมและกำยานเหมือนกัน"

---

### TC-MAT-03: Shared Accords but Disjoint Notes (แนวกลิ่นเดียวกันแต่วัตถุดิบต่าง)
- **วัตถุประสงค์:** ตรวจสอบกรณีที่ไม่มีชื่อโน้ตตรงกันตรงๆ แต่ทั้งคู่จัดอยู่ในกลุ่ม "Woody Aromatic" และมี Accords คล้ายกัน
- **ข้อมูลจำลอง:**
  - *Perfume Ref:* Top (Bergamot), Heart (Clary Sage), Base (Vetiver)
  - *Perfume Cand:* Top (Cardamom), Heart (Rosemary), Base (Cedarwood)
  - ทั้งคู่มี Accords: Woody 50%, Aromatic 30%, Fresh Spicy 20%
- **ผลลัพธ์ที่คาดหวัง:**
  - $S_{notes}$ ต่ำมาก ($\approx 0\%$)
  - $S_{accords}$ สูง ($\approx 85\%$)
  - Composite Score: $\approx 40\% - 55\%$
  - Tier: **Same Vibe**
  - Explainability: "โครงสร้างโน้ตต่างกัน แต่มีคาแรคเตอร์ของกลิ่น (Accords) ไปในทิศทางเดียวกัน"

---

### TC-MAT-04: Missing Note Layer on Candidate (ข้อมูล Candidate ไม่ครบ 3 ชั้น)
- **วัตถุประสงค์:** ตรวจสอบว่าระบบไม่แครช และลด Confidence Score อย่างเหมาะสม
- **ข้อมูลจำลอง:**
  - *Perfume Ref:* มี Top, Heart, Base ครบถ้วน
  - *Perfume Cand:* มีเฉพาะ "General Notes" 4 รายการ (ไม่มีการระบุชั้น)
- **ผลลัพธ์ที่คาดหวัง:**
  - ระบบ fallback ไปใช้ Overall Note Overlap
  - Similarity Score ถูกคำนวณตามสัดส่วนที่มี
  - **Confidence Score ต้องถูกปรับลดลงเป็น LOW หรือ MEDIUM**
  - UI ต้องแจ้งเตือน: "ข้อมูลพีระมิดโน้ตของรุ่นทางเลือกยังไม่สมบูรณ์"

---

### TC-MAT-05: Conflicting Evidence Penalty (มีรีวิวขัดแย้งรุนแรง)
- **วัตถุประสงค์:** ตรวจสอบการปรับลดคะแนนเมื่อมีรีวิวคัดค้าน
- **ข้อมูลจำลอง:**
  - โครงสร้างโน้ตคำนวณได้คะแนน 80%
  - มีรีวิว 2 แหล่งบอกว่า "เปิดเหมือนกันมาก"
  - แต่มีรีวิวอีก 2 แหล่งบอกว่า "ช่วงกลางเป็นกลิ่นเคมีรุนแรง ไม่เหมือนของแท้เลย"
- **ผลลัพธ์ที่คาดหวัง:**
  - $S_{evidence}$ ถูกลดทอนลงเหลือไม่เกิน 50%
  - Confidence Score ถูกปรับลดเป็น Medium
  - Explainability แสดงกล่องข้อความเตือนความเห็นที่ขัดแย้งกัน

---

## 4. Requirements Covered

- [[Requirements_Register#R16|R16]] — Structural Similarity Scoring
- [[Requirements_Register#R18|R18]] — Separate Similarity from Confidence

---

## 5. Dependencies & Links

- สเปกการจับคู่กลิ่น: [[Scent_Matching_Spec]]
- หลักฐานและความเชื่อมั่น: [[Review_Evidence_and_Confidence]]

---

## 6. Change Notes

- `2026-11-10`: กำหนดกรณีทดสอบจำลอง 5 รูปแบบครอบคลุมทั้งกรณีเหมือน, กลิ่นเปิดต่าง, ข้อมูลไม่ครบ, และรีวิวขัดแย้ง
