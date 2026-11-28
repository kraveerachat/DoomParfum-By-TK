# DoomParfum By TK — IMP-WEB-02 Thai translation review recommendations

**Review status: ADVISORY — OWNER APPROVAL PENDING.** This is a ChatGPT language review, not Owner acceptance or a source-code change. Do not mark translations reviewed until the Human Owner explicitly approves the exact proposed text.

Source: `DoomParfum_IMP-WEB-02_Thai_Translation_Review_2026-11-27.md`, candidate `c3f968853b64b4ee65df2d9cf8c6b94e0b13014b`.

Source SHA-256: `e1b55370459214d236cf40631d9ec2c716c7a92a36196551140d836b62906f16`. Both submitted files are byte-identical.

Reviewed: 160 interface strings and 32 fixture prose entries (192 total).

| Group | Recommend keep | Recommend replace | Total |
|---|---:|---:|---:|
| Interface | 134 | 26 | 160 |
| Fixture prose | 25 | 7 | 32 |
| Total | 159 | 33 | 192 |

## Implementation constraints (after Owner approval)

- Apply only the exact Thai replacements below. Keep all other strings unchanged. No English fixture changes, new facts, new identifiers, inferred relationships, or redesign.
- Preserve the approved glossary, all existing proper names, Latin family/accord labels and their language metadata. Preserve Paper study L as authored in Thai. Keep mock-only disclosures and distinguish unknown/not supplied from explicitly empty.
- Preserve placeholders, concatenation semantics and intentional line-breaking characters; U46 has an intentional-looking U+2060 WORD JOINER and is unchanged. U123 adds a space before `{count}`; verify composed visible and accessible names with U124. Check leading spaces in concatenated labels rather than normalizing them globally.
- Verify F15 remains figurative editorial description, not quantified accord weights or concentration; F22 does not assert real-world performance.
- If approved text changes the reviewed source candidate, run relevant localization, search, accessibility, layout and regression verification, rebuild preview on port 3000, and obtain a fresh read-only review of the exact delta. Reconcile candidate/records SHA and evidence. Do not reuse an obsolete code acceptance SHA. No push or PR without separate scoped Owner authorization.
- This review compares text in the supplied file only; it does not verify the local running site, actual dictionary values, or final visual layout. Notes physical check and publication remain separate. A05 stage deferral and Latin family/accord labels were already selected by Owner.

## Exact replacement list

| ID | Key / record | Proposed Thai text |
|---|---|---|
| U41 | `visual.caption` | ภาพประกอบจำลอง |
| U45 | `footer.text` | ฉบับจำลองที่ทำงานบนเครื่องนี้ น้ำหอม แบรนด์ โน้ต และบทความทั้งหมดเป็นข้อมูลสมมติ |
| U47 | `home.lead` | ตัวอย่างสมุดบันทึกน้ำหอมส่วนตัวที่นำเสนอข้อมูลน้ำหอมสมมติผ่านโครงสร้างกลิ่นอย่างเรียบง่าย |
| U54 | `home.folioIntro` | ภาพเหล่านี้ใช้ประกอบคำอธิบายเท่านั้น ทุกภาพมีจำนวนเส้นเท่ากัน เพราะแต่ละระดับระบุเพียงชื่อโน้ต ไม่ใช่ปริมาณ |
| U56 | `home.folioHeart` | โน้ตที่บันทึกไว้ในระดับกลาง บางแบบศึกษาระบุไว้สองชื่อ ขณะที่บางแบบศึกษาไม่ได้ระบุข้อมูลในระดับนี้ |
| U57 | `home.folioBase` | โน้ตที่บันทึกไว้เป็นลำดับสุดท้าย ในฉบับจำลองนี้ การระบุว่าไม่มีรายการเบสโน้ตคือคำตอบ ส่วนเบสโน้ตที่ไม่ได้ระบุยังคงเป็นคำถาม |
| U84 | `explore.unsuppliedText` | ไม่มีแบบศึกษาใดระบุโน้ตนี้ และบางแบบศึกษายังไม่ได้ระบุข้อมูลกลิ่นในบางระดับ |
| U87 | `explore.noResultsText` | แบบศึกษาจะตรงกับตัวกรองโน้ตก็ต่อเมื่อมีชื่อโน้ตนั้นอยู่ในรายการใดรายการหนึ่งของแบบศึกษา |
| U98 | `detail.layersNote` | ชื่อโน้ตใช้ประกอบการอธิบายเท่านั้น ไม่มีการบันทึกปริมาณ |
| U104 | `detail.generalNotesNote` | เป็นโน้ตที่ระบุสำหรับบันทึกทั้งรายการ โดยแยกจากโครงสร้างกลิ่น 3 ระดับ |
| U107 | `detail.record` | เกี่ยวกับบันทึกจำลองนี้ |
| U110 | `detail.recordKindValue` | ข้อมูลตัวอย่างสมมติทั้งหมดที่จัดทำขึ้นภายในโครงการ |
| U116 | `notes.lead` | ชื่อโน้ตสมมติ 9 ชื่อ ใช้สื่อถึงความรู้สึกในฉบับจำลองนี้ ไม่ได้หมายถึงส่วนผสมหรือวัตถุดิบจริง |
| U123 | `notes.browse` | ดู {count} |
| U129 | `search.description` | ผลการค้นหาจะอัปเดตขณะพิมพ์ โดยแสดงเฉพาะแบบศึกษาสมมติ |
| U134 | `profile.text` | ฉบับจำลองนี้ยังไม่เปิดใช้โปรไฟล์ ไม่มีการลงชื่อเข้าใช้และไม่มีการใช้ข้อมูลบัญชี |
| U142 | `errors.unavailableText` | ไม่พบหน้าที่ตรงกับที่อยู่นี้ในฉบับจำลอง ลิงก์อาจไม่ครบถ้วน |
| U144 | `about.h1` | สมุดบันทึกที่บอกตรงไปตรงมาว่าข้อมูลใดยังไม่ทราบ |
| U145 | `about.lead` | DoomParfum By TK วางแนวทางไว้ให้เป็นพื้นที่ส่วนตัวสำหรับอ่านเรื่องน้ำหอม ติดตามโน้ตกลิ่น และบันทึกคอลเลกชัน ฉบับจำลองนี้แสดงตัวอย่างหน้าตาและการใช้งานของพื้นที่ดังกล่าว โดยใช้ข้อมูลสมมติทุกรายการ |
| U148 | `about.purposeText` | บันทึกน้ำหอมหนึ่งรายการประกอบด้วยข้อมูลหลายประเภท ทั้งชื่อ โน้ตที่ระบุ ความคิดเห็นของผู้คน ผู้จำหน่าย และสถานะการเป็นเจ้าของ ข้อมูลเหล่านี้ควรจัดเก็บแยกจากกัน สมุดบันทึกนี้จึงออกแบบให้ข้อมูลแต่ละประเภทไม่ถูกนำมาใช้แทนกัน |
| U151 | `about.demo2` | การอ่านรายชื่อโน้ตตามโครงสร้างท็อปโน้ต ฮาร์ตโน้ต และเบสโน้ต โดยแยกโน้ตทั่วไปและแอคคอร์ดออกจากกัน |
| U152 | `about.demo3` | การเลือกดูแบบศึกษาทุกรายการที่ระบุโน้ตนั้น |
| U154 | `about.scope` | สิ่งที่ยังต้องพัฒนาในอนาคต |
| U155 | `about.scopeText1` | ฉบับจำลองนี้ไม่ได้เชื่อมต่อกับแคตตาล็อกจริง บัญชีผู้ใช้ หรือร้านค้า ระบบจับคู่กลิ่น แคตตาล็อกส่วนตัว สิทธิ์ในการใช้แหล่งข้อมูลภายนอก ความปลอดภัยของบัญชี ตะกร้า และคอลเลกชัน ล้วนเป็นงานแยกส่วนที่ต้องได้รับการอนุมัติแยกกัน ฉบับจำลองนี้ไม่ถือเป็นการอนุมัติงานใดในส่วนเหล่านั้น |
| U158 | `about.journalText` | บทความตัวอย่างสองบทเกี่ยวกับการอ่านข้อมูลในฉบับจำลองนี้ โดยไม่มีการกล่าวอ้างถึงผลิตภัณฑ์จริง |
| U160 | `about.creditsText` | ภาพวาด บันทึก และบทความทั้งหมดจัดทำขึ้นสำหรับโครงการนี้ ใช้แบบอักษร Bodoni Moda, Fahkwang และ Noto Sans Thai ภายใต้สัญญาอนุญาต SIL Open Font License 1.1 และไอคอนจาก Lucide ภายใต้สัญญาอนุญาต ISC ทั้งหมดให้บริการจากคอมพิวเตอร์เครื่องนี้ |
| F13 | `mock-perfume-001` description | บันทึกสมมติที่จงใจให้ข้อมูลไม่ครบ โดยไม่ได้ระบุฮาร์ตโน้ต แต่ระบุไว้อย่างชัดเจนว่าเบสโน้ตไม่มีรายการ ทั้งสองสถานะจึงมีความหมายต่างกันโดยเจตนา |
| F15 | `mock-perfume-003` description | หน้ากระดาษสมมติที่เขียนด้วยหมึกยามดึก โดยให้น้ำหนักเชิงการบรรยายกับระดับสุดท้ายเป็นหลัก |
| F22 | `mock-perfume-011` description | ก้อนหินสมมติที่มีคำบรรยายยาวและไม่ค่อยเหมาะกับการใช้งานทั่วไปนัก เก็บไว้เพื่อทดสอบการตัดบรรทัด การซูม และการขยายขนาดตัวอักษรด้วยข้อความที่ท้าทายกว่าประโยคสั้น ๆ เพียงบรรทัดเดียว คำบรรยายนี้ไม่ได้ระบุวัสดุจริงหรือกล่าวอ้างถึงลักษณะของน้ำหอมขณะใช้ |
| F26 | `mock-article-001` body ¶2 | แต่ละระดับระบุเพียงชื่อโน้ต ไม่ใช่ปริมาณ ไม่มีข้อมูลใดบอกว่าสิ่งนั้นมีอยู่มากเพียงใด ติดทนนานเท่าใด หรือประกอบด้วยอะไร หากบันทึกหนึ่งระบุหนึ่งชื่อและอีกบันทึกระบุสามชื่อ ความแตกต่างมีเพียงความยาวของรายการเท่านั้น |
| F27 | `mock-article-001` body ¶3 | โน้ตทั่วไปแยกจากโครงสร้างกลิ่น 3 ระดับ เป็นข้อมูลของบันทึกทั้งรายการ และจะไม่ถูกย้ายไปอยู่ในระดับใดเพื่อเติมช่องว่าง |
| F28 | `mock-article-002` title | ไม่มีรายการ ไม่ได้หมายความว่าไม่ทราบ |
| F30 | `mock-article-002` body ¶1 | Paper study A ไม่ได้ระบุฮาร์ตโน้ต แต่ระบุไว้อย่างชัดเจนว่าเบสโน้ตไม่มีรายการ อย่างแรกคือคำถามที่ยังไม่มีใครตอบ ส่วนอย่างหลังคือคำตอบ |

## Complete line-by-line advisory review

`KEEP` recommends accepting the original text; `REPLACE` recommends the exact replacement shown. Neither status is Owner approval.

| ID | Key / record | English source | Current Thai | Recommendation |
|---|---|---|---|---|
| U1 | `site.name` | DoomParfum By TK | DoomParfum By TK | KEEP |
| U2 | `site.description` | A mock-only fragrance notebook. Every record is fictional. | สมุดบันทึกน้ำหอมฉบับจำลอง ทุกรายการเป็นเรื่องสมมติ | KEEP |
| U3 | `site.homeLink` | DoomParfum By TK home | หน้าแรก DoomParfum By TK | KEEP |
| U4 | `titles.home` | Home | หน้าแรก | KEEP |
| U5 | `titles.explore` | Explore mock fragrances | สำรวจน้ำหอมจำลอง | KEEP |
| U6 | `titles.detail` | {name} · Mock study | {name} · แบบศึกษาจำลอง | KEEP |
| U7 | `titles.notes` | Notes | โน้ตกลิ่น | KEEP |
| U8 | `titles.about` | About | เกี่ยวกับเรา | KEEP |
| U9 | `titles.unavailable` | Unavailable | ไม่พบหน้านี้ | KEEP |
| U10 | `skip` | Skip to content | ข้ามไปยังเนื้อหาหลัก | KEEP |
| U11 | `nav.primary` | Primary | เมนูหลัก | KEEP |
| U12 | `nav.home` | Home | หน้าแรก | KEEP |
| U13 | `nav.explore` | Explore | สำรวจ | KEEP |
| U14 | `nav.notes` | Notes | โน้ตกลิ่น | KEEP |
| U15 | `nav.about` | About | เกี่ยวกับเรา | KEEP |
| U16 | `nav.menu` | Menu | เมนู | KEEP |
| U17 | `nav.menuTitle` | Navigation | เมนู | KEEP |
| U18 | `nav.menuList` | Menu | เมนูนำทาง | KEEP |
| U19 | `nav.search` | Search mock catalogue | ค้นหาในแคตตาล็อกจำลอง | KEEP |
| U20 | `nav.profile` | Profile unavailable in this mock | โปรไฟล์ยังไม่เปิดใช้ในฉบับจำลองนี้ | KEEP |
| U21 | `nav.close` | Close | ปิด | KEEP |
| U22 | `language.group` | Language | ภาษา | KEEP |
| U23 | `language.enShort` | EN | EN | KEEP |
| U24 | `language.enName` | English | English | KEEP |
| U25 | `language.thShort` | TH | TH | KEEP |
| U26 | `language.thName` | ภาษาไทย | ภาษาไทย | KEEP |
| U27 | `notice` | Synthetic mock study. Nothing here describes a real fragrance. | นี่คือแบบศึกษาจำลอง ไม่มีข้อมูลใดในหน้านี้อ้างถึงน้ำหอมจริง | KEEP |
| U28 | `mock` | Mock | จำลอง | KEEP |
| U29 | `familyUnknown` | Family unknown | ไม่ทราบตระกูลกลิ่น | KEEP |
| U30 | `count.studyOne` | {n} mock study | แบบศึกษาจำลอง {n} รายการ | KEEP |
| U31 | `count.studyOther` | {n} mock studies | แบบศึกษาจำลอง {n} รายการ | KEEP |
| U32 | `count.noteOne` | {n} mock note | โน้ตจำลอง {n} รายการ | KEEP |
| U33 | `count.noteOther` | {n} mock notes | โน้ตจำลอง {n} รายการ | KEEP |
| U34 | `count.studiesWord` | mock studies | แบบศึกษาจำลอง | KEEP |
| U35 | `count.studyWord` | mock study | แบบศึกษาจำลอง | KEEP |
| U36 | `layers.top` | Top | ท็อปโน้ต | KEEP |
| U37 | `layers.heart` | Heart | ฮาร์ตโน้ต | KEEP |
| U38 | `layers.base` | Base | เบสโน้ต | KEEP |
| U39 | `layers.generalNotes` | General notes | โน้ตทั่วไป | KEEP |
| U40 | `visual.unavailable` | Visual unavailable in this mock | ฉบับจำลองนี้ยังไม่มีภาพประกอบ | KEEP |
| U41 | `visual.caption` | Synthetic visual study | ภาพศึกษาสังเคราะห์ | REPLACE: ภาพประกอบจำลอง |
| U42 | `footer.about` | About | เกี่ยวกับเรา | KEEP |
| U43 | `footer.scope` | Mock scope | ขอบเขตของฉบับจำลอง | KEEP |
| U44 | `footer.credits` | Local credits | เครดิต | KEEP |
| U45 | `footer.text` | A local mock. Every fragrance, house, note and article here is fictional. | ฉบับจำลองที่ทำงานภายในเครื่อง น้ำหอม แบรนด์ โน้ต และบทความทั้งหมดในที่นี้เป็นเรื่องสมมติ | REPLACE: ฉบับจำลองที่ทำงานบนเครื่องนี้ น้ำหอม แบรนด์ โน้ต และบทความทั้งหมดเป็นข้อมูลสมมติ |
| U46 | `home.h1` | A personal atlas of scent. | แผนที่กลิ่นส่วน⁠ตัว | KEEP |
| U47 | `home.lead` | A mock study of how a private perfume notebook could read: fictional fragrances, plainly layered. | แบบศึกษาจำลองของสมุดบันทึกน้ำหอมส่วนตัว: น้ำหอมสมมติที่อ่านเป็นลำดับชั้นอย่างเรียบง่าย | REPLACE: ตัวอย่างสมุดบันทึกน้ำหอมส่วนตัวที่นำเสนอข้อมูลน้ำหอมสมมติผ่านโครงสร้างกลิ่นอย่างเรียบง่าย |
| U48 | `home.cta` | Explore mock catalogue | สำรวจแคตตาล็อกจำลอง | KEEP |
| U49 | `home.heroAlt` | Abstract study: a folded paper sheet and a dark slab crossed by contour lines. | ภาพศึกษานามธรรม: แผ่นกระดาษพับและแท่งสีเข้มที่มีเส้นชั้นความสูงพาดผ่าน | KEEP |
| U50 | `home.featured` | Featured discoveries | รายการคัดสรร | KEEP |
| U51 | `home.viewAll` | View all mock fragrances | ดูน้ำหอมจำลองทั้งหมด | KEEP |
| U52 | `home.families` | Explore by scent | สำรวจตามตระกูลกลิ่น | KEEP |
| U53 | `home.folio` | Read it in three layers | อ่านโครงสร้างกลิ่น 3 ระดับ | KEEP |
| U54 | `home.folioIntro` | Illustrative only. Each drawing carries the same number of lines, because a layer records labels and never amounts. | ภาพประกอบเพื่อการอธิบายเท่านั้น ทุกภาพมีจำนวนเส้นเท่ากัน เพราะแต่ละระดับบันทึกเพียงชื่อโน้ต ไม่ได้บันทึกปริมาณ | REPLACE: ภาพเหล่านี้ใช้ประกอบคำอธิบายเท่านั้น ทุกภาพมีจำนวนเส้นเท่ากัน เพราะแต่ละระดับระบุเพียงชื่อโน้ต ไม่ใช่ปริมาณ |
| U55 | `home.folioTop` | What a record lists first. In this mock it is only an order of reading, like the opening line of a page. | โน้ตที่บันทึกไว้เป็นลำดับแรก ในฉบับจำลองนี้หมายถึงลำดับการอ่านเท่านั้น เหมือนบรรทัดแรกของหน้ากระดาษ | KEEP |
| U56 | `home.folioHeart` | What a record keeps in the middle. Some studies in this mock list two labels here, and some never supplied any. | โน้ตที่บันทึกไว้ตรงกลาง บางแบบศึกษาระบุไว้สองชื่อ และบางแบบศึกษาไม่เคยระบุเลย | REPLACE: โน้ตที่บันทึกไว้ในระดับกลาง บางแบบศึกษาระบุไว้สองชื่อ ขณะที่บางแบบศึกษาไม่ได้ระบุข้อมูลในระดับนี้ |
| U57 | `home.folioBase` | What a record lists last. In this mock an empty base is an answer, and an unknown base is still a question. | โน้ตที่บันทึกไว้เป็นลำดับสุดท้าย ในฉบับจำลองนี้ เบสโน้ตที่บันทึกว่าว่างเปล่าคือคำตอบ ส่วนเบสโน้ตที่ไม่ได้ระบุยังคงเป็นคำถาม | REPLACE: โน้ตที่บันทึกไว้เป็นลำดับสุดท้าย ในฉบับจำลองนี้ การระบุว่าไม่มีรายการเบสโน้ตคือคำตอบ ส่วนเบสโน้ตที่ไม่ได้ระบุยังคงเป็นคำถาม |
| U58 | `home.folioDrawing` | {layer}, illustrative drawing | ภาพประกอบ: {layer} | KEEP |
| U59 | `home.journal` | From the scent notebook | จากสมุดบันทึกกลิ่น | KEEP |
| U60 | `home.journalIntro` | Sample articles, written for this mock. | บทความตัวอย่างที่เขียนขึ้นสำหรับฉบับจำลองนี้ | KEEP |
| U61 | `home.journalAll` | Read the scent notebook | อ่านสมุดบันทึกกลิ่น | KEEP |
| U62 | `explore.lead` | Every study in this mock, listed by name. Narrow the list by family or note. | แบบศึกษาทั้งหมดในฉบับจำลองนี้ เรียงตามชื่อ เลือกดูตามตระกูลกลิ่นหรือโน้ตได้ | KEEP |
| U63 | `explore.searchLabel` | Search mock catalogue | ค้นหาในแคตตาล็อกจำลอง | KEEP |
| U64 | `explore.searchHelp` | Searches the names, house and descriptions of fictional studies. | ค้นหาจากชื่อ แบรนด์ หรือคำบรรยายของแบบศึกษาสมมติ | KEEP |
| U65 | `explore.filterToggle` | Filter and sort | ตัวกรองและการเรียงลำดับ | KEEP |
| U66 | `explore.family` | Family | ตระกูลกลิ่น | KEEP |
| U67 | `explore.note` | Note | โน้ต | KEEP |
| U68 | `explore.sort` | Sort | เรียงตาม | KEEP |
| U69 | `explore.allFamilies` | All families | ทุกตระกูลกลิ่น | KEEP |
| U70 | `explore.allNotes` | All notes | ทุกโน้ต | KEEP |
| U71 | `explore.sortAsc` | Name A–Z | ชื่อ A–Z | KEEP |
| U72 | `explore.sortDesc` | Name Z–A | ชื่อ Z–A | KEEP |
| U73 | `explore.activeFilters` | Active filters | ตัวกรองที่เลือก | KEEP |
| U74 | `explore.removeFamily` | , remove family filter |  ล้างตัวกรองตระกูลกลิ่น | KEEP |
| U75 | `explore.removeNote` | , remove note filter |  ล้างตัวกรองโน้ต | KEEP |
| U76 | `explore.clearAll` | Clear all | ล้างทั้งหมด | KEEP |
| U77 | `explore.listHeading` | Mock studies | แบบศึกษาจำลอง | KEEP |
| U78 | `explore.filterUnavailable` | Filter unavailable | ใช้ตัวกรองนี้ไม่ได้ | KEEP |
| U79 | `explore.invalidTitle` | This filter is unavailable | ใช้ตัวกรองนี้ไม่ได้ | KEEP |
| U80 | `explore.invalidText` | The link asks for a family or note that does not exist in this mock. | ลิงก์นี้ระบุตระกูลกลิ่นหรือโน้ตที่ไม่มีในฉบับจำลองนี้ | KEEP |
| U81 | `explore.resetFilters` | Reset filters | ล้างตัวกรอง | KEEP |
| U82 | `explore.unsuppliedCount` | Relationship not supplied | ไม่ได้ระบุความเชื่อมโยง | KEEP |
| U83 | `explore.unsuppliedTitle` | Relationship not supplied for {note} in this mock | ฉบับจำลองนี้ไม่ได้ระบุความเชื่อมโยงของ {note} | KEEP |
| U84 | `explore.unsuppliedText` | No study lists it, and some studies have layers that were never supplied. | ไม่มีแบบศึกษาใดระบุโน้ตนี้ และบางแบบศึกษายังมีระดับที่ไม่ได้ระบุ | REPLACE: ไม่มีแบบศึกษาใดระบุโน้ตนี้ และบางแบบศึกษายังไม่ได้ระบุข้อมูลกลิ่นในบางระดับ |
| U85 | `explore.clearFilters` | Clear filters | ล้างตัวกรอง | KEEP |
| U86 | `explore.noResults` | No mock studies fit these filters. | ไม่พบแบบศึกษาที่ตรงกับตัวกรอง | KEEP |
| U87 | `explore.noResultsText` | A study matches a note only when the note is written in one of its lists. | แบบศึกษาจะตรงกับโน้ตก็ต่อเมื่อมีโน้ตนั้นอยู่ในรายการใดรายการหนึ่งของแบบศึกษา | REPLACE: แบบศึกษาจะตรงกับตัวกรองโน้ตก็ต่อเมื่อมีชื่อโน้ตนั้นอยู่ในรายการใดรายการหนึ่งของแบบศึกษา |
| U88 | `explore.noData` | No mock studies are available | ยังไม่มีแบบศึกษาจำลอง | KEEP |
| U89 | `explore.noDataLink` | About this mock | เกี่ยวกับฉบับจำลองนี้ | KEEP |
| U90 | `detail.breadcrumb` | Breadcrumb | เส้นทางนำทาง | KEEP |
| U91 | `detail.explore` | Explore | สำรวจ | KEEP |
| U92 | `detail.visualAlt` | Abstract study drawn for this fictional record | ภาพศึกษานามธรรมที่วาดขึ้นสำหรับบันทึกสมมตินี้ | KEEP |
| U93 | `detail.family` | Family | ตระกูลกลิ่น | KEEP |
| U94 | `detail.unknown` | Unknown | ไม่ทราบ | KEEP |
| U95 | `detail.descriptionUnknown` | Description not supplied in this mock | ฉบับจำลองนี้ไม่ได้ระบุคำบรรยาย | KEEP |
| U96 | `detail.allNotes` | Read about the notes | อ่านเกี่ยวกับโน้ตกลิ่น | KEEP |
| U97 | `detail.layersHeading` | Three layers | โครงสร้างกลิ่น 3 ระดับ | KEEP |
| U98 | `detail.layersNote` | Illustrative labels. No amounts are recorded. | ชื่อโน้ตเพื่อการอ่านเท่านั้น ไม่มีการบันทึกปริมาณ | REPLACE: ชื่อโน้ตใช้ประกอบการอธิบายเท่านั้น ไม่มีการบันทึกปริมาณ |
| U99 | `detail.notSupplied` | Not supplied in this mock | ไม่ได้ระบุ | KEEP |
| U100 | `detail.emptyLayer` | No entries in this mock layer | ไม่มีรายการในระดับนี้ | KEEP |
| U101 | `detail.emptyList` | No entries in this mock list | ไม่มีรายการ | KEEP |
| U102 | `detail.emptyEntries` | No entries | ไม่มีรายการ | KEEP |
| U103 | `detail.browseNote` | , browse mock studies |  ดูแบบศึกษาที่มีโน้ตนี้ | KEEP |
| U104 | `detail.generalNotesNote` | Listed for the whole record, outside the layers. | ระบุไว้สำหรับทั้งบันทึก แยกจากโครงสร้าง 3 ระดับ | REPLACE: เป็นโน้ตที่ระบุสำหรับบันทึกทั้งรายการ โดยแยกจากโครงสร้างกลิ่น 3 ระดับ |
| U105 | `detail.accords` | Accords | แอคคอร์ด | KEEP |
| U106 | `detail.accordsNote` | Fictional descriptors, without weights. | คำบรรยายสมมติ ไม่มีการให้น้ำหนัก | KEEP |
| U107 | `detail.record` | About this mock record | ข้อมูลบันทึกจำลองนี้ | REPLACE: เกี่ยวกับบันทึกจำลองนี้ |
| U108 | `detail.recordId` | Record | รหัสบันทึก | KEEP |
| U109 | `detail.recordKind` | Kind | ประเภท | KEEP |
| U110 | `detail.recordKindValue` | Locally authored fixture, entirely synthetic | ข้อมูลตัวอย่างที่จัดทำขึ้นภายในโครงการ เป็นข้อมูลสังเคราะห์ทั้งหมด | REPLACE: ข้อมูลตัวอย่างสมมติทั้งหมดที่จัดทำขึ้นภายในโครงการ |
| U111 | `detail.recordVersion` | Version | เวอร์ชัน | KEEP |
| U112 | `detail.recordFor` | Authored for | จัดทำสำหรับ | KEEP |
| U113 | `detail.recordRights` | Rights | สิทธิ์ | KEEP |
| U114 | `detail.recordRightsValue` | Original project material | ผลงานต้นฉบับของโครงการ | KEEP |
| U115 | `detail.back` | Back to the mock catalogue | กลับไปยังแคตตาล็อกจำลอง | KEEP |
| U116 | `notes.lead` | Nine invented labels. They name impressions for this mock and do not refer to any ingredient or material. | ชื่อโน้ตที่ประดิษฐ์ขึ้นเก้าชื่อ ใช้เรียกความรู้สึกในฉบับจำลองนี้ และไม่ได้หมายถึงวัตถุดิบหรือสารใดจริง | REPLACE: ชื่อโน้ตสมมติ 9 ชื่อ ใช้สื่อถึงความรู้สึกในฉบับจำลองนี้ ไม่ได้หมายถึงส่วนผสมหรือวัตถุดิบจริง |
| U117 | `notes.searchLabel` | Search mock notes | ค้นหาโน้ตจำลอง | KEEP |
| U118 | `notes.searchHelp` | Searches labels and descriptions. | ค้นหาจากชื่อและคำบรรยาย | KEEP |
| U119 | `notes.listHeading` | Mock notes | โน้ตจำลอง | KEEP |
| U120 | `notes.showAll` | Show all | แสดงทั้งหมด | KEEP |
| U121 | `notes.none` | No mock notes found | ไม่พบโน้ตจำลอง | KEEP |
| U122 | `notes.showAllNotes` | Show all notes | แสดงโน้ตทั้งหมด | KEEP |
| U123 | `notes.browse` | Browse {count} | ดู{count} | REPLACE: ดู {count} |
| U124 | `notes.browseWith` |  with {note} |  ที่มี {note} | KEEP |
| U125 | `notes.unsupplied` | Relationship not supplied | ไม่ได้ระบุความเชื่อมโยง | KEEP |
| U126 | `notes.listed` | Where {note} is listed | {note} อยู่ในแบบศึกษาใดบ้าง | KEEP |
| U127 | `notes.jump` | Jump to letter | ไปยังตัวอักษร | KEEP |
| U128 | `search.title` | Search | ค้นหา | KEEP |
| U129 | `search.description` | Results update as you type and cover fictional studies only. | ผลการค้นหาเปลี่ยนตามที่พิมพ์ และครอบคลุมเฉพาะแบบศึกษาสมมติ | REPLACE: ผลการค้นหาจะอัปเดตขณะพิมพ์ โดยแสดงเฉพาะแบบศึกษาสมมติ |
| U130 | `search.help` | Fictional studies only | เฉพาะแบบศึกษาสมมติ | KEEP |
| U131 | `search.none` | No mock fragrances found | ไม่พบน้ำหอมจำลอง | KEEP |
| U132 | `search.clear` | Clear search | ล้างคำค้นหา | KEEP |
| U133 | `profile.title` | Profile | โปรไฟล์ | KEEP |
| U134 | `profile.text` | Profile is not available in this mock. No sign-in or account data is used. | ฉบับจำลองนี้ยังไม่มีโปรไฟล์ ไม่มีการลงชื่อเข้าใช้และไม่ใช้ข้อมูลบัญชีใด ๆ | REPLACE: ฉบับจำลองนี้ยังไม่เปิดใช้โปรไฟล์ ไม่มีการลงชื่อเข้าใช้และไม่มีการใช้ข้อมูลบัญชี |
| U135 | `route.missing` | The entry you opened is no longer in this list. | รายการที่คุณเปิดไว้ไม่อยู่ในรายการนี้แล้ว | KEEP |
| U136 | `route.pending` | Opening the next page | กำลังเปิดหน้าถัดไป | KEEP |
| U137 | `errors.renderTitle` | This page could not be shown | ไม่สามารถแสดงหน้านี้ได้ | KEEP |
| U138 | `errors.renderText` | The local page failed to render. Try again, or return to the mock catalogue. | หน้านี้แสดงผลไม่สำเร็จ ลองอีกครั้ง หรือกลับไปยังแคตตาล็อกจำลอง | KEEP |
| U139 | `errors.retry` | Retry | ลองอีกครั้ง | KEEP |
| U140 | `errors.returnExplore` | Return to Explore | กลับไปยังหน้าสำรวจ | KEEP |
| U141 | `errors.unavailableTitle` | This page is unavailable | ไม่พบหน้านี้ | KEEP |
| U142 | `errors.unavailableText` | Nothing in this mock uses that address. The link may be incomplete. | ฉบับจำลองนี้ไม่มีหน้าที่อยู่นี้ ลิงก์อาจไม่ครบถ้วน | REPLACE: ไม่พบหน้าที่ตรงกับที่อยู่นี้ในฉบับจำลอง ลิงก์อาจไม่ครบถ้วน |
| U143 | `errors.unavailableAction` | Return to the mock catalogue | กลับไปยังแคตตาล็อกจำลอง | KEEP |
| U144 | `about.h1` | A notebook that says what it does not know. | สมุดบันทึกที่บอกตรง ๆ ว่ายังไม่รู้อะไรบ้าง | REPLACE: สมุดบันทึกที่บอกตรงไปตรงมาว่าข้อมูลใดยังไม่ทราบ |
| U145 | `about.lead` | DoomParfum By TK is planned as a private place to read about fragrance, follow notes and keep track of a collection. This is a mock of how that place could look and behave. Every record in it was invented. | DoomParfum By TK ถูกวางแผนให้เป็นพื้นที่ส่วนตัวสำหรับอ่านเรื่องน้ำหอม ติดตามโน้ตกลิ่น และบันทึกคอลเลกชัน หน้านี้คือฉบับจำลองที่แสดงว่าพื้นที่นั้นอาจมีหน้าตาและการใช้งานอย่างไร ทุกบันทึกในที่นี้สร้างขึ้นเพื่อการสาธิต | REPLACE: DoomParfum By TK วางแนวทางไว้ให้เป็นพื้นที่ส่วนตัวสำหรับอ่านเรื่องน้ำหอม ติดตามโน้ตกลิ่น และบันทึกคอลเลกชัน ฉบับจำลองนี้แสดงตัวอย่างหน้าตาและการใช้งานของพื้นที่ดังกล่าว โดยใช้ข้อมูลสมมติทุกรายการ |
| U146 | `about.contents` | On this page | ในหน้านี้ | KEEP |
| U147 | `about.purpose` | Purpose | จุดประสงค์ | KEEP |
| U148 | `about.purposeText` | A fragrance record mixes several kinds of information: what a thing is called, which notes it declares, what people say about it, who sells it and whether you own it. Those belong in different places. This notebook is designed so that none of them can stand in for another. | บันทึกน้ำหอมหนึ่งรายการมีข้อมูลหลายประเภทปะปนกัน ทั้งชื่อเรียก โน้ตที่ระบุไว้ ความเห็นของผู้คน ผู้จำหน่าย และสถานะว่าคุณเป็นเจ้าของหรือไม่ ข้อมูลเหล่านี้ควรแยกจากกัน สมุดบันทึกนี้จึงออกแบบให้ข้อมูลประเภทหนึ่งไม่อาจแทนที่อีกประเภทหนึ่งได้ | REPLACE: บันทึกน้ำหอมหนึ่งรายการประกอบด้วยข้อมูลหลายประเภท ทั้งชื่อ โน้ตที่ระบุ ความคิดเห็นของผู้คน ผู้จำหน่าย และสถานะการเป็นเจ้าของ ข้อมูลเหล่านี้ควรจัดเก็บแยกจากกัน สมุดบันทึกนี้จึงออกแบบให้ข้อมูลแต่ละประเภทไม่ถูกนำมาใช้แทนกัน |
| U149 | `about.demonstrates` | What this mock demonstrates | สิ่งที่ฉบับจำลองนี้แสดง | KEEP |
| U150 | `about.demo1` | Browsing and filtering a small set of fictional studies. | การเลือกดูและกรองแบบศึกษาสมมติชุดเล็ก ๆ | KEEP |
| U151 | `about.demo2` | Reading top, heart and base layers as labels, with general notes and accords kept apart. | การอ่านท็อปโน้ต ฮาร์ตโน้ต และเบสโน้ตในฐานะชื่อเรียก โดยแยกโน้ตทั่วไปและแอคคอร์ดไว้ต่างหาก | REPLACE: การอ่านรายชื่อโน้ตตามโครงสร้างท็อปโน้ต ฮาร์ตโน้ต และเบสโน้ต โดยแยกโน้ตทั่วไปและแอคคอร์ดออกจากกัน |
| U152 | `about.demo3` | Following a note to every study that lists it. | การติดตามโน้ตหนึ่งไปยังทุกแบบศึกษาที่ระบุโน้ตนั้น | REPLACE: การเลือกดูแบบศึกษาทุกรายการที่ระบุโน้ตนั้น |
| U153 | `about.demo4` | Telling an unknown field from one that was authored as empty. | การแยกข้อมูลที่ไม่ได้ระบุ ออกจากข้อมูลที่บันทึกไว้ว่าว่างเปล่า | KEEP |
| U154 | `about.scope` | What remains future | สิ่งที่ยังเป็นงานในอนาคต | REPLACE: สิ่งที่ยังต้องพัฒนาในอนาคต |
| U155 | `about.scopeText1` | Nothing here connects to a real catalogue, an account or a store. Scent matching, the private catalogue, permission to use outside sources, account security, the cart and the collection are separate pieces of work. Each has its own approval, and this mock approves none of them. | ไม่มีส่วนใดในที่นี้เชื่อมต่อกับแคตตาล็อกจริง บัญชีผู้ใช้ หรือร้านค้า ทั้งการจับคู่กลิ่น แคตตาล็อกส่วนตัว สิทธิ์ในการใช้แหล่งข้อมูลภายนอก ความปลอดภัยของบัญชี ตะกร้า และคอลเลกชัน ล้วนเป็นงานแยกกันที่ต้องได้รับอนุมัติของตนเอง และฉบับจำลองนี้ไม่ได้อนุมัติงานใดเลย | REPLACE: ฉบับจำลองนี้ไม่ได้เชื่อมต่อกับแคตตาล็อกจริง บัญชีผู้ใช้ หรือร้านค้า ระบบจับคู่กลิ่น แคตตาล็อกส่วนตัว สิทธิ์ในการใช้แหล่งข้อมูลภายนอก ความปลอดภัยของบัญชี ตะกร้า และคอลเลกชัน ล้วนเป็นงานแยกส่วนที่ต้องได้รับการอนุมัติแยกกัน ฉบับจำลองนี้ไม่ถือเป็นการอนุมัติงานใดในส่วนเหล่านั้น |
| U156 | `about.scopeText2` | The mock runs on one computer. It asks search engines not to index it, and that request is not a security control. | ฉบับจำลองนี้ทำงานบนคอมพิวเตอร์เครื่องเดียว มีการขอไม่ให้เครื่องมือค้นหาจัดทำดัชนี แต่คำขอนั้นไม่ใช่มาตรการด้านความปลอดภัย | KEEP |
| U157 | `about.journal` | The scent notebook | สมุดบันทึกกลิ่น | KEEP |
| U158 | `about.journalText` | Two sample articles about reading this mock. They make no claim about any real product. | บทความตัวอย่างสองบทว่าด้วยการอ่านฉบับจำลองนี้ ไม่ได้กล่าวอ้างถึงผลิตภัณฑ์จริงใด | REPLACE: บทความตัวอย่างสองบทเกี่ยวกับการอ่านข้อมูลในฉบับจำลองนี้ โดยไม่มีการกล่าวอ้างถึงผลิตภัณฑ์จริง |
| U159 | `about.credits` | Local credits | เครดิต | KEEP |
| U160 | `about.creditsText` | The drawings, records and articles were made for this project. Type is set in Bodoni Moda, Fahkwang and Noto Sans Thai under the SIL Open Font License 1.1, and icons come from Lucide under the ISC license. All of it is served from this computer. | ภาพวาด บันทึก และบทความทั้งหมดจัดทำขึ้นสำหรับโครงการนี้ ตัวอักษรใช้ Bodoni Moda, Fahkwang และ Noto Sans Thai ภายใต้ SIL Open Font License 1.1 ไอคอนมาจาก Lucide ภายใต้สัญญาอนุญาต ISC ทั้งหมดให้บริการจากคอมพิวเตอร์เครื่องนี้ | REPLACE: ภาพวาด บันทึก และบทความทั้งหมดจัดทำขึ้นสำหรับโครงการนี้ ใช้แบบอักษร Bodoni Moda, Fahkwang และ Noto Sans Thai ภายใต้สัญญาอนุญาต SIL Open Font License 1.1 และไอคอนจาก Lucide ภายใต้สัญญาอนุญาต ISC ทั้งหมดให้บริการจากคอมพิวเตอร์เครื่องนี้ |
| F1 | `mock-family-bright` descriptor | Edges, rims and thin light. | ขอบ ริม และแสงบาง ๆ | KEEP |
| F2 | `mock-family-soft` descriptor | Folds, threads and slow curves. | รอยพับ เส้นด้าย และส่วนโค้งที่ค่อย ๆ เปลี่ยน | KEEP |
| F3 | `mock-family-deep` descriptor | Strata, weight and late ink. | ชั้นหิน น้ำหนัก และหมึกยามดึก | KEEP |
| F4 | `mock-note-001` descriptor | The cool edge of a cut sheet. | ขอบเย็นของแผ่นกระดาษที่เพิ่งตัด | KEEP |
| F5 | `mock-note-002` descriptor | A dry thread pulled straight. | เส้นด้ายแห้งที่ถูกดึงจนตึง | KEEP |
| F6 | `mock-note-003` descriptor | A bright rim, seen edge-on. | ริมที่สว่าง มองจากด้านข้าง | KEEP |
| F7 | `mock-note-004` descriptor | Warm dust on a high shelf. | ฝุ่นอุ่นบนชั้นวางสูง | KEEP |
| F8 | `mock-note-005` descriptor | Wet slate before noon. | หินชนวนเปียกก่อนเที่ยง | KEEP |
| F9 | `mock-note-006` descriptor | Soft wax, barely marked. | ขี้ผึ้งนุ่มที่แทบไม่มีรอย | KEEP |
| F10 | `mock-note-007` descriptor | Late ink, not yet dry. | หมึกยามดึกที่ยังไม่แห้ง | KEEP |
| F11 | `mock-note-008` descriptor | A pale trace left in a room. | ร่องรอยจาง ๆ ที่หลงเหลืออยู่ในห้อง | KEEP |
| F12 | `mock-note-009` descriptor | A label with no supplied relationships. | ชื่อที่ยังไม่มีการระบุความเชื่อมโยง | KEEP |
| F13 | `mock-perfume-001` description | A fictional record kept deliberately incomplete. Its heart was never supplied, and its base was authored as empty. The two read differently on purpose. | บันทึกสมมติที่ตั้งใจเก็บไว้ไม่ครบ ฮาร์ตโน้ตไม่เคยได้รับการระบุ ส่วนเบสโน้ตถูกบันทึกไว้ว่าว่างเปล่า สองสิ่งนี้จึงมีความหมายต่างกันโดยเจตนา | REPLACE: บันทึกสมมติที่จงใจให้ข้อมูลไม่ครบ โดยไม่ได้ระบุฮาร์ตโน้ต แต่ระบุไว้อย่างชัดเจนว่าเบสโน้ตไม่มีรายการ ทั้งสองสถานะจึงมีความหมายต่างกันโดยเจตนา |
| F14 | `mock-perfume-002` description | A fictional sheet folded once, written as a quiet opening that settles without hurry. | กระดาษสมมติที่พับเพียงครั้งเดียว เปิดอย่างแผ่วเบา แล้วค่อย ๆ สงบลงโดยไม่เร่งรีบ | KEEP |
| F15 | `mock-perfume-003` description | A fictional page of late ink. Most of its weight was authored into the last layer. | หน้ากระดาษสมมติที่เขียนด้วยหมึกยามดึก น้ำหนักส่วนใหญ่ถูกบันทึกไว้ในระดับสุดท้าย | REPLACE: หน้ากระดาษสมมติที่เขียนด้วยหมึกยามดึก โดยให้น้ำหนักเชิงการบรรยายกับระดับสุดท้ายเป็นหลัก |
| F16 | `mock-perfume-004` description | Fictional cloth in morning light: one thread at the start, one at the end, and room between them. | ผืนผ้าสมมติในแสงยามเช้า มีด้ายหนึ่งเส้นตอนเริ่ม อีกหนึ่งเส้นตอนจบ และมีที่ว่างอยู่ระหว่างกลาง | KEEP |
| F17 | `mock-perfume-005` description | A fictional weave recorded at three distances. Every layer was supplied, so this is the plainest record to read first. | ลายทอสมมติที่บันทึกไว้จากสามระยะ ทุกระดับได้รับการระบุครบ จึงเป็นบันทึกที่อ่านง่ายที่สุดสำหรับผู้เริ่มต้น | KEEP |
| F18 | `mock-perfume-007` description | A fictional pane seen edge-on. Bright at the rim, then almost nothing. | แผ่นกระจกสมมติที่มองจากด้านข้าง สว่างที่ขอบ แล้วแทบไม่มีอะไรเลย | KEEP |
| F19 | `mock-perfume-008` description | Fictional light through two curved surfaces, arriving in order: rim, slate, wax. | แสงสมมติที่ผ่านพื้นผิวโค้งสองชั้น มาถึงตามลำดับ: ริม หินชนวน ขี้ผึ้ง | KEEP |
| F20 | `mock-perfume-009` description | A fictional study whose family was never assigned. It stays in the catalogue with its family shown as unknown. | แบบศึกษาสมมติที่ไม่เคยได้รับการกำหนดตระกูลกลิ่น ยังคงอยู่ในแคตตาล็อกโดยแสดงตระกูลกลิ่นว่าไม่ทราบ | KEEP |
| F21 | `mock-perfume-010` description | Fictional strata, read from the surface down. The base carries three labels and is the longest list in this mock. | ชั้นหินสมมติที่อ่านจากผิวลงไป เบสโน้ตมีสามชื่อ และเป็นรายการที่ยาวที่สุดในฉบับจำลองนี้ | KEEP |
| F22 | `mock-perfume-011` description | A fictional boulder with a long and slightly impractical description, kept here so that wrapping, zooming and larger text can be checked against something more demanding than a single tidy line. It names no real material and makes no claim about wear. | ก้อนหินสมมติที่มีคำบรรยายยาวและออกจะไม่ค่อยมีประโยชน์นัก เก็บไว้เพื่อใช้ตรวจการตัดบรรทัด การขยายหน้าจอ และข้อความขนาดใหญ่ กับสิ่งที่ยากกว่าบรรทัดสั้น ๆ ที่เรียบร้อยเพียงบรรทัดเดียว คำบรรยายนี้ไม่ได้ระบุวัสดุจริงใด และไม่ได้กล่าวอ้างเรื่องความคงทน | REPLACE: ก้อนหินสมมติที่มีคำบรรยายยาวและไม่ค่อยเหมาะกับการใช้งานทั่วไปนัก เก็บไว้เพื่อทดสอบการตัดบรรทัด การซูม และการขยายขนาดตัวอักษรด้วยข้อความที่ท้าทายกว่าประโยคสั้น ๆ เพียงบรรทัดเดียว คำบรรยายนี้ไม่ได้ระบุวัสดุจริงหรือกล่าวอ้างถึงลักษณะของน้ำหอมขณะใช้ |
| F23 | `mock-article-001` title | Reading a layer | อ่านทีละระดับ | KEEP |
| F24 | `mock-article-001` excerpt | Top, heart and base are an order of reading. They are not a recipe. | ท็อปโน้ต ฮาร์ตโน้ต และเบสโน้ต คือลำดับของการอ่าน ไม่ใช่สูตรผสม | KEEP |
| F25 | `mock-article-001` body ¶1 | Every record in this mock can carry three layers. Top is what was written first, heart is what was written to stay, and base is what was written to remain. The order describes reading, in the way chapters do. | ทุกบันทึกในฉบับจำลองนี้มีได้สามระดับ ท็อปโน้ตคือสิ่งที่บันทึกไว้ก่อน ฮาร์ตโน้ตคือสิ่งที่บันทึกไว้ให้คงอยู่ และเบสโน้ตคือสิ่งที่บันทึกไว้ให้หลงเหลือ ลำดับนี้บรรยายการอ่าน เช่นเดียวกับบทต่าง ๆ ในหนังสือ | KEEP |
| F26 | `mock-article-001` body ¶2 | A layer holds labels, never amounts. Nothing here says how much of anything exists, how long it lasts or what it is made of. When a record lists one label and another lists three, the second list is longer and that is all it means. | แต่ละระดับเก็บเพียงชื่อโน้ต ไม่เคยเก็บปริมาณ ไม่มีสิ่งใดในที่นี้บอกว่ามีสิ่งใดอยู่มากเท่าใด ติดทนนานเท่าใด หรือทำจากอะไร เมื่อบันทึกหนึ่งมีหนึ่งชื่อและอีกบันทึกมีสามชื่อ รายการที่สองก็เพียงยาวกว่า และมีความหมายเพียงเท่านั้น | REPLACE: แต่ละระดับระบุเพียงชื่อโน้ต ไม่ใช่ปริมาณ ไม่มีข้อมูลใดบอกว่าสิ่งนั้นมีอยู่มากเพียงใด ติดทนนานเท่าใด หรือประกอบด้วยอะไร หากบันทึกหนึ่งระบุหนึ่งชื่อและอีกบันทึกระบุสามชื่อ ความแตกต่างมีเพียงความยาวของรายการเท่านั้น |
| F27 | `mock-article-001` body ¶3 | General notes sit apart from the layers. They belong to the whole record and are never moved up or down to fill a gap. | โน้ตทั่วไปอยู่แยกจากโครงสร้าง 3 ระดับ เป็นของทั้งบันทึก และไม่เคยถูกย้ายขึ้นหรือลงเพื่อเติมช่องว่าง | REPLACE: โน้ตทั่วไปแยกจากโครงสร้างกลิ่น 3 ระดับ เป็นข้อมูลของบันทึกทั้งรายการ และจะไม่ถูกย้ายไปอยู่ในระดับใดเพื่อเติมช่องว่าง |
| F28 | `mock-article-002` title | Empty is not unknown | ว่างเปล่าไม่ใช่ไม่ทราบ | REPLACE: ไม่มีรายการ ไม่ได้หมายความว่าไม่ทราบ |
| F29 | `mock-article-002` excerpt | Two records can look equally bare and mean opposite things. | บันทึกสองรายการอาจดูว่างเหมือนกัน แต่มีความหมายตรงข้ามกัน | KEEP |
| F30 | `mock-article-002` body ¶1 | Paper study A has a heart that was never supplied and a base that was authored as empty. The first is a question nobody has answered. The second is an answer. | Paper study A มีฮาร์ตโน้ตที่ไม่เคยได้รับการระบุ และเบสโน้ตที่ถูกบันทึกไว้ว่าว่างเปล่า อย่างแรกคือคำถามที่ยังไม่มีใครตอบ อย่างหลังคือคำตอบ | REPLACE: Paper study A ไม่ได้ระบุฮาร์ตโน้ต แต่ระบุไว้อย่างชัดเจนว่าเบสโน้ตไม่มีรายการ อย่างแรกคือคำถามที่ยังไม่มีใครตอบ ส่วนอย่างหลังคือคำตอบ |
| F31 | `mock-article-002` body ¶2 | Catalogues often flatten the two into one blank space, and a reader then fills that space with a guess. This notebook keeps them apart: one says it was not supplied, the other says it has no entries. | แคตตาล็อกจำนวนมากมักรวมสองอย่างนี้ไว้เป็นช่องว่างเดียว แล้วผู้อ่านก็เติมช่องนั้นด้วยการคาดเดา สมุดบันทึกนี้แยกทั้งสองไว้ อย่างหนึ่งบอกว่าไม่ได้ระบุ อีกอย่างบอกว่าไม่มีรายการ | KEEP |
| F32 | `mock-article-002` body ¶3 | The same care applies to a family, a description or a picture. When something is missing, the page says what is missing and leaves it there. | ความระมัดระวังเดียวกันใช้กับตระกูลกลิ่น คำบรรยาย หรือภาพ เมื่อมีสิ่งใดขาดไป หน้านั้นจะบอกว่าขาดอะไร และปล่อยไว้อย่างนั้น | KEEP |
