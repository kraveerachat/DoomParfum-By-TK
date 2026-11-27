/**
 * Thai overlay for fixture prose (DPT-PLAN-013 4.3). Keyed by existing IDs; it adds no record, name,
 * note, relationship or state, and gives no text to a field whose state is unknown. Every text below
 * is a translation of the English source that the Owner reviewed and approved word for word
 * (2026-11-28). Only the Owner marks text reviewed; a changed text goes back to draft until re-approved.
 */
import type { ThaiOverlay } from "./types.ts";

const OWNER_REVIEW = "Owner approval 2026-11-28, IMP-WEB-02 S6 Thai translation review (192 entries)";
const reviewed = (th: string) => ({ th, review: "reviewed", reviewRecord: OWNER_REVIEW }) as const;
const reviewedBody = (th: readonly string[]) => ({ th, review: "reviewed", reviewRecord: OWNER_REVIEW }) as const;

export const thaiOverlay: ThaiOverlay = {
  synthetic: true,
  rights: "project_owned_synthetic",
  provenance: { kind: "locally_authored_fixture", fixtureVersion: "1.1.0", authoredFor: "IMP-WEB-02" },
  families: {
    "mock-family-bright": { descriptor: reviewed("ขอบ ริม และแสงบาง ๆ") },
    "mock-family-soft": { descriptor: reviewed("รอยพับ เส้นด้าย และส่วนโค้งที่ค่อย ๆ เปลี่ยน") },
    "mock-family-deep": { descriptor: reviewed("ชั้นหิน น้ำหนัก และหมึกยามดึก") },
  },
  notes: {
    "mock-note-001": { descriptor: reviewed("ขอบเย็นของแผ่นกระดาษที่เพิ่งตัด") },
    "mock-note-002": { descriptor: reviewed("เส้นด้ายแห้งที่ถูกดึงจนตึง") },
    "mock-note-003": { descriptor: reviewed("ริมที่สว่าง มองจากด้านข้าง") },
    "mock-note-004": { descriptor: reviewed("ฝุ่นอุ่นบนชั้นวางสูง") },
    "mock-note-005": { descriptor: reviewed("หินชนวนเปียกก่อนเที่ยง") },
    "mock-note-006": { descriptor: reviewed("ขี้ผึ้งนุ่มที่แทบไม่มีรอย") },
    "mock-note-007": { descriptor: reviewed("หมึกยามดึกที่ยังไม่แห้ง") },
    "mock-note-008": { descriptor: reviewed("ร่องรอยจาง ๆ ที่หลงเหลืออยู่ในห้อง") },
    "mock-note-009": { descriptor: reviewed("ชื่อที่ยังไม่มีการระบุความเชื่อมโยง") },
  },
  perfumes: {
    "mock-perfume-001": {
      description: reviewed(
        "บันทึกสมมติที่จงใจให้ข้อมูลไม่ครบ โดยไม่ได้ระบุฮาร์ตโน้ต แต่ระบุไว้อย่างชัดเจนว่าเบสโน้ตไม่มีรายการ ทั้งสองสถานะจึงมีความหมายต่างกันโดยเจตนา",
      ),
    },
    "mock-perfume-002": {
      description: reviewed("กระดาษสมมติที่พับเพียงครั้งเดียว เปิดอย่างแผ่วเบา แล้วค่อย ๆ สงบลงโดยไม่เร่งรีบ"),
    },
    "mock-perfume-003": {
      description: reviewed("หน้ากระดาษสมมติที่เขียนด้วยหมึกยามดึก โดยให้น้ำหนักเชิงการบรรยายกับระดับสุดท้ายเป็นหลัก"),
    },
    "mock-perfume-004": {
      description: reviewed("ผืนผ้าสมมติในแสงยามเช้า มีด้ายหนึ่งเส้นตอนเริ่ม อีกหนึ่งเส้นตอนจบ และมีที่ว่างอยู่ระหว่างกลาง"),
    },
    "mock-perfume-005": {
      description: reviewed(
        "ลายทอสมมติที่บันทึกไว้จากสามระยะ ทุกระดับได้รับการระบุครบ จึงเป็นบันทึกที่อ่านง่ายที่สุดสำหรับผู้เริ่มต้น",
      ),
    },
    "mock-perfume-007": {
      description: reviewed("แผ่นกระจกสมมติที่มองจากด้านข้าง สว่างที่ขอบ แล้วแทบไม่มีอะไรเลย"),
    },
    "mock-perfume-008": {
      description: reviewed("แสงสมมติที่ผ่านพื้นผิวโค้งสองชั้น มาถึงตามลำดับ: ริม หินชนวน ขี้ผึ้ง"),
    },
    "mock-perfume-009": {
      description: reviewed(
        "แบบศึกษาสมมติที่ไม่เคยได้รับการกำหนดตระกูลกลิ่น ยังคงอยู่ในแคตตาล็อกโดยแสดงตระกูลกลิ่นว่าไม่ทราบ",
      ),
    },
    "mock-perfume-010": {
      description: reviewed(
        "ชั้นหินสมมติที่อ่านจากผิวลงไป เบสโน้ตมีสามชื่อ และเป็นรายการที่ยาวที่สุดในฉบับจำลองนี้",
      ),
    },
    "mock-perfume-011": {
      description: reviewed(
        "ก้อนหินสมมติที่มีคำบรรยายยาวและไม่ค่อยเหมาะกับการใช้งานทั่วไปนัก เก็บไว้เพื่อทดสอบการตัดบรรทัด การซูม และการขยายขนาดตัวอักษรด้วยข้อความที่ท้าทายกว่าประโยคสั้น ๆ เพียงบรรทัดเดียว คำบรรยายนี้ไม่ได้ระบุวัสดุจริงหรือกล่าวอ้างถึงลักษณะของน้ำหอมขณะใช้",
      ),
    },
  },
  articles: {
    "mock-article-001": {
      title: reviewed("อ่านทีละระดับ"),
      excerpt: reviewed("ท็อปโน้ต ฮาร์ตโน้ต และเบสโน้ต คือลำดับของการอ่าน ไม่ใช่สูตรผสม"),
      body: reviewedBody([
        "ทุกบันทึกในฉบับจำลองนี้มีได้สามระดับ ท็อปโน้ตคือสิ่งที่บันทึกไว้ก่อน ฮาร์ตโน้ตคือสิ่งที่บันทึกไว้ให้คงอยู่ และเบสโน้ตคือสิ่งที่บันทึกไว้ให้หลงเหลือ ลำดับนี้บรรยายการอ่าน เช่นเดียวกับบทต่าง ๆ ในหนังสือ",
        "แต่ละระดับระบุเพียงชื่อโน้ต ไม่ใช่ปริมาณ ไม่มีข้อมูลใดบอกว่าสิ่งนั้นมีอยู่มากเพียงใด ติดทนนานเท่าใด หรือประกอบด้วยอะไร หากบันทึกหนึ่งระบุหนึ่งชื่อและอีกบันทึกระบุสามชื่อ ความแตกต่างมีเพียงความยาวของรายการเท่านั้น",
        "โน้ตทั่วไปแยกจากโครงสร้างกลิ่น 3 ระดับ เป็นข้อมูลของบันทึกทั้งรายการ และจะไม่ถูกย้ายไปอยู่ในระดับใดเพื่อเติมช่องว่าง",
      ]),
    },
    "mock-article-002": {
      title: reviewed("ไม่มีรายการ ไม่ได้หมายความว่าไม่ทราบ"),
      excerpt: reviewed("บันทึกสองรายการอาจดูว่างเหมือนกัน แต่มีความหมายตรงข้ามกัน"),
      body: reviewedBody([
        "Paper study A ไม่ได้ระบุฮาร์ตโน้ต แต่ระบุไว้อย่างชัดเจนว่าเบสโน้ตไม่มีรายการ อย่างแรกคือคำถามที่ยังไม่มีใครตอบ ส่วนอย่างหลังคือคำตอบ",
        "แคตตาล็อกจำนวนมากมักรวมสองอย่างนี้ไว้เป็นช่องว่างเดียว แล้วผู้อ่านก็เติมช่องนั้นด้วยการคาดเดา สมุดบันทึกนี้แยกทั้งสองไว้ อย่างหนึ่งบอกว่าไม่ได้ระบุ อีกอย่างบอกว่าไม่มีรายการ",
        "ความระมัดระวังเดียวกันใช้กับตระกูลกลิ่น คำบรรยาย หรือภาพ เมื่อมีสิ่งใดขาดไป หน้านั้นจะบอกว่าขาดอะไร และปล่อยไว้อย่างนั้น",
      ]),
    },
  },
};
