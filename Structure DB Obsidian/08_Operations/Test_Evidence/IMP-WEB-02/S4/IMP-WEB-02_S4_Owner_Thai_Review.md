# DoomParfum — Thai translation review (IMP-WEB-02)

For: the Owner. Date: 2026-11-27. Code: `c3f9688` (preview http://127.0.0.1:3000/th). Public-safe: fictional mock content only.

**State of every line below: DRAFT.** Your terminology (2026-11-26) is applied. No line is marked reviewed until you answer. The 160 interface and 32 fixture lines were regenerated from the code at `689b177` (Thai text unchanged in `c3f9688`) and match the CP5 sheet in the vault exactly.

## How to answer

Tick **OK** or write the correction after **Fix:**. "All OK except U12, F4" is a complete answer. Lines you have not answered stay draft.

## Decisions in this document

1. **Line review** of U1–U160 and F1–F32 (below).
2. **Family and accord labels on Thai pages** (Bright study, Folded quiet …): they stay in Latin, marked English, until you decide. Options: keep Latin, or give Thai labels (they would be added as drafts for one more review).
3. Fictional perfume and note names stay unchanged, as you directed. No decision is needed.

## Your approved terminology (already applied)

| English | Thai |
|---|---|
| Home | หน้าแรก |
| Explore | สำรวจ |
| Notes | โน้ตกลิ่น |
| About | เกี่ยวกับเรา |
| Top / Heart / Base | ท็อปโน้ต / ฮาร์ตโน้ต / เบสโน้ต |
| General notes | โน้ตทั่วไป |
| Family | ตระกูลกลิ่น |
| Accords | แอคคอร์ด |
| Three layers | โครงสร้างกลิ่น 3 ระดับ |
| Explore by scent | สำรวจตามตระกูลกลิ่น |
| Not supplied | ไม่ได้ระบุ |
| No entries | ไม่มีรายการ |

## Interface text (160)

`{name}`, `{count}` and similar are placeholders filled in by the page.

| # | Key | English | Thai draft | Your answer |
|---|---|---|---|---|
| U1 | `site.name` | DoomParfum By TK | DoomParfum By TK | ☐ OK · ☐ Fix: |
| U2 | `site.description` | A mock-only fragrance notebook. Every record is fictional. | สมุดบันทึกน้ำหอมฉบับจำลอง ทุกรายการเป็นเรื่องสมมติ | ☐ OK · ☐ Fix: |
| U3 | `site.homeLink` | DoomParfum By TK home | หน้าแรก DoomParfum By TK | ☐ OK · ☐ Fix: |
| U4 | `titles.home` | Home | หน้าแรก | ☐ OK · ☐ Fix: |
| U5 | `titles.explore` | Explore mock fragrances | สำรวจน้ำหอมจำลอง | ☐ OK · ☐ Fix: |
| U6 | `titles.detail` | {name} · Mock study | {name} · แบบศึกษาจำลอง | ☐ OK · ☐ Fix: |
| U7 | `titles.notes` | Notes | โน้ตกลิ่น | ☐ OK · ☐ Fix: |
| U8 | `titles.about` | About | เกี่ยวกับเรา | ☐ OK · ☐ Fix: |
| U9 | `titles.unavailable` | Unavailable | ไม่พบหน้านี้ | ☐ OK · ☐ Fix: |
| U10 | `skip` | Skip to content | ข้ามไปยังเนื้อหาหลัก | ☐ OK · ☐ Fix: |
| U11 | `nav.primary` | Primary | เมนูหลัก | ☐ OK · ☐ Fix: |
| U12 | `nav.home` | Home | หน้าแรก | ☐ OK · ☐ Fix: |
| U13 | `nav.explore` | Explore | สำรวจ | ☐ OK · ☐ Fix: |
| U14 | `nav.notes` | Notes | โน้ตกลิ่น | ☐ OK · ☐ Fix: |
| U15 | `nav.about` | About | เกี่ยวกับเรา | ☐ OK · ☐ Fix: |
| U16 | `nav.menu` | Menu | เมนู | ☐ OK · ☐ Fix: |
| U17 | `nav.menuTitle` | Navigation | เมนู | ☐ OK · ☐ Fix: |
| U18 | `nav.menuList` | Menu | เมนูนำทาง | ☐ OK · ☐ Fix: |
| U19 | `nav.search` | Search mock catalogue | ค้นหาในแคตตาล็อกจำลอง | ☐ OK · ☐ Fix: |
| U20 | `nav.profile` | Profile unavailable in this mock | โปรไฟล์ยังไม่เปิดใช้ในฉบับจำลองนี้ | ☐ OK · ☐ Fix: |
| U21 | `nav.close` | Close | ปิด | ☐ OK · ☐ Fix: |
| U22 | `language.group` | Language | ภาษา | ☐ OK · ☐ Fix: |
| U23 | `language.enShort` | EN | EN | ☐ OK · ☐ Fix: |
| U24 | `language.enName` | English | English | ☐ OK · ☐ Fix: |
| U25 | `language.thShort` | TH | TH | ☐ OK · ☐ Fix: |
| U26 | `language.thName` | ภาษาไทย | ภาษาไทย | ☐ OK · ☐ Fix: |
| U27 | `notice` | Synthetic mock study. Nothing here describes a real fragrance. | นี่คือแบบศึกษาจำลอง ไม่มีข้อมูลใดในหน้านี้อ้างถึงน้ำหอมจริง | ☐ OK · ☐ Fix: |
| U28 | `mock` | Mock | จำลอง | ☐ OK · ☐ Fix: |
| U29 | `familyUnknown` | Family unknown | ไม่ทราบตระกูลกลิ่น | ☐ OK · ☐ Fix: |
| U30 | `count.studyOne` | {n} mock study | แบบศึกษาจำลอง {n} รายการ | ☐ OK · ☐ Fix: |
| U31 | `count.studyOther` | {n} mock studies | แบบศึกษาจำลอง {n} รายการ | ☐ OK · ☐ Fix: |
| U32 | `count.noteOne` | {n} mock note | โน้ตจำลอง {n} รายการ | ☐ OK · ☐ Fix: |
| U33 | `count.noteOther` | {n} mock notes | โน้ตจำลอง {n} รายการ | ☐ OK · ☐ Fix: |
| U34 | `count.studiesWord` | mock studies | แบบศึกษาจำลอง | ☐ OK · ☐ Fix: |
| U35 | `count.studyWord` | mock study | แบบศึกษาจำลอง | ☐ OK · ☐ Fix: |
| U36 | `layers.top` | Top | ท็อปโน้ต | ☐ OK · ☐ Fix: |
| U37 | `layers.heart` | Heart | ฮาร์ตโน้ต | ☐ OK · ☐ Fix: |
| U38 | `layers.base` | Base | เบสโน้ต | ☐ OK · ☐ Fix: |
| U39 | `layers.generalNotes` | General notes | โน้ตทั่วไป | ☐ OK · ☐ Fix: |
| U40 | `visual.unavailable` | Visual unavailable in this mock | ฉบับจำลองนี้ยังไม่มีภาพประกอบ | ☐ OK · ☐ Fix: |
| U41 | `visual.caption` | Synthetic visual study | ภาพศึกษาสังเคราะห์ | ☐ OK · ☐ Fix: |
| U42 | `footer.about` | About | เกี่ยวกับเรา | ☐ OK · ☐ Fix: |
| U43 | `footer.scope` | Mock scope | ขอบเขตของฉบับจำลอง | ☐ OK · ☐ Fix: |
| U44 | `footer.credits` | Local credits | เครดิต | ☐ OK · ☐ Fix: |
| U45 | `footer.text` | A local mock. Every fragrance, house, note and article here is fictional. | ฉบับจำลองที่ทำงานภายในเครื่อง น้ำหอม แบรนด์ โน้ต และบทความทั้งหมดในที่นี้เป็นเรื่องสมมติ | ☐ OK · ☐ Fix: |
| U46 | `home.h1` | A personal atlas of scent. | แผนที่กลิ่นส่วน⁠ตัว | ☐ OK · ☐ Fix: |
| U47 | `home.lead` | A mock study of how a private perfume notebook could read: fictional fragrances, plainly layered. | แบบศึกษาจำลองของสมุดบันทึกน้ำหอมส่วนตัว: น้ำหอมสมมติที่อ่านเป็นลำดับชั้นอย่างเรียบง่าย | ☐ OK · ☐ Fix: |
| U48 | `home.cta` | Explore mock catalogue | สำรวจแคตตาล็อกจำลอง | ☐ OK · ☐ Fix: |
| U49 | `home.heroAlt` | Abstract study: a folded paper sheet and a dark slab crossed by contour lines. | ภาพศึกษานามธรรม: แผ่นกระดาษพับและแท่งสีเข้มที่มีเส้นชั้นความสูงพาดผ่าน | ☐ OK · ☐ Fix: |
| U50 | `home.featured` | Featured discoveries | รายการคัดสรร | ☐ OK · ☐ Fix: |
| U51 | `home.viewAll` | View all mock fragrances | ดูน้ำหอมจำลองทั้งหมด | ☐ OK · ☐ Fix: |
| U52 | `home.families` | Explore by scent | สำรวจตามตระกูลกลิ่น | ☐ OK · ☐ Fix: |
| U53 | `home.folio` | Read it in three layers | อ่านโครงสร้างกลิ่น 3 ระดับ | ☐ OK · ☐ Fix: |
| U54 | `home.folioIntro` | Illustrative only. Each drawing carries the same number of lines, because a layer records labels and never amounts. | ภาพประกอบเพื่อการอธิบายเท่านั้น ทุกภาพมีจำนวนเส้นเท่ากัน เพราะแต่ละระดับบันทึกเพียงชื่อโน้ต ไม่ได้บันทึกปริมาณ | ☐ OK · ☐ Fix: |
| U55 | `home.folioTop` | What a record lists first. In this mock it is only an order of reading, like the opening line of a page. | โน้ตที่บันทึกไว้เป็นลำดับแรก ในฉบับจำลองนี้หมายถึงลำดับการอ่านเท่านั้น เหมือนบรรทัดแรกของหน้ากระดาษ | ☐ OK · ☐ Fix: |
| U56 | `home.folioHeart` | What a record keeps in the middle. Some studies in this mock list two labels here, and some never supplied any. | โน้ตที่บันทึกไว้ตรงกลาง บางแบบศึกษาระบุไว้สองชื่อ และบางแบบศึกษาไม่เคยระบุเลย | ☐ OK · ☐ Fix: |
| U57 | `home.folioBase` | What a record lists last. In this mock an empty base is an answer, and an unknown base is still a question. | โน้ตที่บันทึกไว้เป็นลำดับสุดท้าย ในฉบับจำลองนี้ เบสโน้ตที่บันทึกว่าว่างเปล่าคือคำตอบ ส่วนเบสโน้ตที่ไม่ได้ระบุยังคงเป็นคำถาม | ☐ OK · ☐ Fix: |
| U58 | `home.folioDrawing` | {layer}, illustrative drawing | ภาพประกอบ: {layer} | ☐ OK · ☐ Fix: |
| U59 | `home.journal` | From the scent notebook | จากสมุดบันทึกกลิ่น | ☐ OK · ☐ Fix: |
| U60 | `home.journalIntro` | Sample articles, written for this mock. | บทความตัวอย่างที่เขียนขึ้นสำหรับฉบับจำลองนี้ | ☐ OK · ☐ Fix: |
| U61 | `home.journalAll` | Read the scent notebook | อ่านสมุดบันทึกกลิ่น | ☐ OK · ☐ Fix: |
| U62 | `explore.lead` | Every study in this mock, listed by name. Narrow the list by family or note. | แบบศึกษาทั้งหมดในฉบับจำลองนี้ เรียงตามชื่อ เลือกดูตามตระกูลกลิ่นหรือโน้ตได้ | ☐ OK · ☐ Fix: |
| U63 | `explore.searchLabel` | Search mock catalogue | ค้นหาในแคตตาล็อกจำลอง | ☐ OK · ☐ Fix: |
| U64 | `explore.searchHelp` | Searches the names, house and descriptions of fictional studies. | ค้นหาจากชื่อ แบรนด์ หรือคำบรรยายของแบบศึกษาสมมติ | ☐ OK · ☐ Fix: |
| U65 | `explore.filterToggle` | Filter and sort | ตัวกรองและการเรียงลำดับ | ☐ OK · ☐ Fix: |
| U66 | `explore.family` | Family | ตระกูลกลิ่น | ☐ OK · ☐ Fix: |
| U67 | `explore.note` | Note | โน้ต | ☐ OK · ☐ Fix: |
| U68 | `explore.sort` | Sort | เรียงตาม | ☐ OK · ☐ Fix: |
| U69 | `explore.allFamilies` | All families | ทุกตระกูลกลิ่น | ☐ OK · ☐ Fix: |
| U70 | `explore.allNotes` | All notes | ทุกโน้ต | ☐ OK · ☐ Fix: |
| U71 | `explore.sortAsc` | Name A–Z | ชื่อ A–Z | ☐ OK · ☐ Fix: |
| U72 | `explore.sortDesc` | Name Z–A | ชื่อ Z–A | ☐ OK · ☐ Fix: |
| U73 | `explore.activeFilters` | Active filters | ตัวกรองที่เลือก | ☐ OK · ☐ Fix: |
| U74 | `explore.removeFamily` | , remove family filter |  ล้างตัวกรองตระกูลกลิ่น | ☐ OK · ☐ Fix: |
| U75 | `explore.removeNote` | , remove note filter |  ล้างตัวกรองโน้ต | ☐ OK · ☐ Fix: |
| U76 | `explore.clearAll` | Clear all | ล้างทั้งหมด | ☐ OK · ☐ Fix: |
| U77 | `explore.listHeading` | Mock studies | แบบศึกษาจำลอง | ☐ OK · ☐ Fix: |
| U78 | `explore.filterUnavailable` | Filter unavailable | ใช้ตัวกรองนี้ไม่ได้ | ☐ OK · ☐ Fix: |
| U79 | `explore.invalidTitle` | This filter is unavailable | ใช้ตัวกรองนี้ไม่ได้ | ☐ OK · ☐ Fix: |
| U80 | `explore.invalidText` | The link asks for a family or note that does not exist in this mock. | ลิงก์นี้ระบุตระกูลกลิ่นหรือโน้ตที่ไม่มีในฉบับจำลองนี้ | ☐ OK · ☐ Fix: |
| U81 | `explore.resetFilters` | Reset filters | ล้างตัวกรอง | ☐ OK · ☐ Fix: |
| U82 | `explore.unsuppliedCount` | Relationship not supplied | ไม่ได้ระบุความเชื่อมโยง | ☐ OK · ☐ Fix: |
| U83 | `explore.unsuppliedTitle` | Relationship not supplied for {note} in this mock | ฉบับจำลองนี้ไม่ได้ระบุความเชื่อมโยงของ {note} | ☐ OK · ☐ Fix: |
| U84 | `explore.unsuppliedText` | No study lists it, and some studies have layers that were never supplied. | ไม่มีแบบศึกษาใดระบุโน้ตนี้ และบางแบบศึกษายังมีระดับที่ไม่ได้ระบุ | ☐ OK · ☐ Fix: |
| U85 | `explore.clearFilters` | Clear filters | ล้างตัวกรอง | ☐ OK · ☐ Fix: |
| U86 | `explore.noResults` | No mock studies fit these filters. | ไม่พบแบบศึกษาที่ตรงกับตัวกรอง | ☐ OK · ☐ Fix: |
| U87 | `explore.noResultsText` | A study matches a note only when the note is written in one of its lists. | แบบศึกษาจะตรงกับโน้ตก็ต่อเมื่อมีโน้ตนั้นอยู่ในรายการใดรายการหนึ่งของแบบศึกษา | ☐ OK · ☐ Fix: |
| U88 | `explore.noData` | No mock studies are available | ยังไม่มีแบบศึกษาจำลอง | ☐ OK · ☐ Fix: |
| U89 | `explore.noDataLink` | About this mock | เกี่ยวกับฉบับจำลองนี้ | ☐ OK · ☐ Fix: |
| U90 | `detail.breadcrumb` | Breadcrumb | เส้นทางนำทาง | ☐ OK · ☐ Fix: |
| U91 | `detail.explore` | Explore | สำรวจ | ☐ OK · ☐ Fix: |
| U92 | `detail.visualAlt` | Abstract study drawn for this fictional record | ภาพศึกษานามธรรมที่วาดขึ้นสำหรับบันทึกสมมตินี้ | ☐ OK · ☐ Fix: |
| U93 | `detail.family` | Family | ตระกูลกลิ่น | ☐ OK · ☐ Fix: |
| U94 | `detail.unknown` | Unknown | ไม่ทราบ | ☐ OK · ☐ Fix: |
| U95 | `detail.descriptionUnknown` | Description not supplied in this mock | ฉบับจำลองนี้ไม่ได้ระบุคำบรรยาย | ☐ OK · ☐ Fix: |
| U96 | `detail.allNotes` | Read about the notes | อ่านเกี่ยวกับโน้ตกลิ่น | ☐ OK · ☐ Fix: |
| U97 | `detail.layersHeading` | Three layers | โครงสร้างกลิ่น 3 ระดับ | ☐ OK · ☐ Fix: |
| U98 | `detail.layersNote` | Illustrative labels. No amounts are recorded. | ชื่อโน้ตเพื่อการอ่านเท่านั้น ไม่มีการบันทึกปริมาณ | ☐ OK · ☐ Fix: |
| U99 | `detail.notSupplied` | Not supplied in this mock | ไม่ได้ระบุ | ☐ OK · ☐ Fix: |
| U100 | `detail.emptyLayer` | No entries in this mock layer | ไม่มีรายการในระดับนี้ | ☐ OK · ☐ Fix: |
| U101 | `detail.emptyList` | No entries in this mock list | ไม่มีรายการ | ☐ OK · ☐ Fix: |
| U102 | `detail.emptyEntries` | No entries | ไม่มีรายการ | ☐ OK · ☐ Fix: |
| U103 | `detail.browseNote` | , browse mock studies |  ดูแบบศึกษาที่มีโน้ตนี้ | ☐ OK · ☐ Fix: |
| U104 | `detail.generalNotesNote` | Listed for the whole record, outside the layers. | ระบุไว้สำหรับทั้งบันทึก แยกจากโครงสร้าง 3 ระดับ | ☐ OK · ☐ Fix: |
| U105 | `detail.accords` | Accords | แอคคอร์ด | ☐ OK · ☐ Fix: |
| U106 | `detail.accordsNote` | Fictional descriptors, without weights. | คำบรรยายสมมติ ไม่มีการให้น้ำหนัก | ☐ OK · ☐ Fix: |
| U107 | `detail.record` | About this mock record | ข้อมูลบันทึกจำลองนี้ | ☐ OK · ☐ Fix: |
| U108 | `detail.recordId` | Record | รหัสบันทึก | ☐ OK · ☐ Fix: |
| U109 | `detail.recordKind` | Kind | ประเภท | ☐ OK · ☐ Fix: |
| U110 | `detail.recordKindValue` | Locally authored fixture, entirely synthetic | ข้อมูลตัวอย่างที่จัดทำขึ้นภายในโครงการ เป็นข้อมูลสังเคราะห์ทั้งหมด | ☐ OK · ☐ Fix: |
| U111 | `detail.recordVersion` | Version | เวอร์ชัน | ☐ OK · ☐ Fix: |
| U112 | `detail.recordFor` | Authored for | จัดทำสำหรับ | ☐ OK · ☐ Fix: |
| U113 | `detail.recordRights` | Rights | สิทธิ์ | ☐ OK · ☐ Fix: |
| U114 | `detail.recordRightsValue` | Original project material | ผลงานต้นฉบับของโครงการ | ☐ OK · ☐ Fix: |
| U115 | `detail.back` | Back to the mock catalogue | กลับไปยังแคตตาล็อกจำลอง | ☐ OK · ☐ Fix: |
| U116 | `notes.lead` | Nine invented labels. They name impressions for this mock and do not refer to any ingredient or material. | ชื่อโน้ตที่ประดิษฐ์ขึ้นเก้าชื่อ ใช้เรียกความรู้สึกในฉบับจำลองนี้ และไม่ได้หมายถึงวัตถุดิบหรือสารใดจริง | ☐ OK · ☐ Fix: |
| U117 | `notes.searchLabel` | Search mock notes | ค้นหาโน้ตจำลอง | ☐ OK · ☐ Fix: |
| U118 | `notes.searchHelp` | Searches labels and descriptions. | ค้นหาจากชื่อและคำบรรยาย | ☐ OK · ☐ Fix: |
| U119 | `notes.listHeading` | Mock notes | โน้ตจำลอง | ☐ OK · ☐ Fix: |
| U120 | `notes.showAll` | Show all | แสดงทั้งหมด | ☐ OK · ☐ Fix: |
| U121 | `notes.none` | No mock notes found | ไม่พบโน้ตจำลอง | ☐ OK · ☐ Fix: |
| U122 | `notes.showAllNotes` | Show all notes | แสดงโน้ตทั้งหมด | ☐ OK · ☐ Fix: |
| U123 | `notes.browse` | Browse {count} | ดู{count} | ☐ OK · ☐ Fix: |
| U124 | `notes.browseWith` |  with {note} |  ที่มี {note} | ☐ OK · ☐ Fix: |
| U125 | `notes.unsupplied` | Relationship not supplied | ไม่ได้ระบุความเชื่อมโยง | ☐ OK · ☐ Fix: |
| U126 | `notes.listed` | Where {note} is listed | {note} อยู่ในแบบศึกษาใดบ้าง | ☐ OK · ☐ Fix: |
| U127 | `notes.jump` | Jump to letter | ไปยังตัวอักษร | ☐ OK · ☐ Fix: |
| U128 | `search.title` | Search | ค้นหา | ☐ OK · ☐ Fix: |
| U129 | `search.description` | Results update as you type and cover fictional studies only. | ผลการค้นหาเปลี่ยนตามที่พิมพ์ และครอบคลุมเฉพาะแบบศึกษาสมมติ | ☐ OK · ☐ Fix: |
| U130 | `search.help` | Fictional studies only | เฉพาะแบบศึกษาสมมติ | ☐ OK · ☐ Fix: |
| U131 | `search.none` | No mock fragrances found | ไม่พบน้ำหอมจำลอง | ☐ OK · ☐ Fix: |
| U132 | `search.clear` | Clear search | ล้างคำค้นหา | ☐ OK · ☐ Fix: |
| U133 | `profile.title` | Profile | โปรไฟล์ | ☐ OK · ☐ Fix: |
| U134 | `profile.text` | Profile is not available in this mock. No sign-in or account data is used. | ฉบับจำลองนี้ยังไม่มีโปรไฟล์ ไม่มีการลงชื่อเข้าใช้และไม่ใช้ข้อมูลบัญชีใด ๆ | ☐ OK · ☐ Fix: |
| U135 | `route.missing` | The entry you opened is no longer in this list. | รายการที่คุณเปิดไว้ไม่อยู่ในรายการนี้แล้ว | ☐ OK · ☐ Fix: |
| U136 | `route.pending` | Opening the next page | กำลังเปิดหน้าถัดไป | ☐ OK · ☐ Fix: |
| U137 | `errors.renderTitle` | This page could not be shown | ไม่สามารถแสดงหน้านี้ได้ | ☐ OK · ☐ Fix: |
| U138 | `errors.renderText` | The local page failed to render. Try again, or return to the mock catalogue. | หน้านี้แสดงผลไม่สำเร็จ ลองอีกครั้ง หรือกลับไปยังแคตตาล็อกจำลอง | ☐ OK · ☐ Fix: |
| U139 | `errors.retry` | Retry | ลองอีกครั้ง | ☐ OK · ☐ Fix: |
| U140 | `errors.returnExplore` | Return to Explore | กลับไปยังหน้าสำรวจ | ☐ OK · ☐ Fix: |
| U141 | `errors.unavailableTitle` | This page is unavailable | ไม่พบหน้านี้ | ☐ OK · ☐ Fix: |
| U142 | `errors.unavailableText` | Nothing in this mock uses that address. The link may be incomplete. | ฉบับจำลองนี้ไม่มีหน้าที่อยู่นี้ ลิงก์อาจไม่ครบถ้วน | ☐ OK · ☐ Fix: |
| U143 | `errors.unavailableAction` | Return to the mock catalogue | กลับไปยังแคตตาล็อกจำลอง | ☐ OK · ☐ Fix: |
| U144 | `about.h1` | A notebook that says what it does not know. | สมุดบันทึกที่บอกตรง ๆ ว่ายังไม่รู้อะไรบ้าง | ☐ OK · ☐ Fix: |
| U145 | `about.lead` | DoomParfum By TK is planned as a private place to read about fragrance, follow notes and keep track of a collection. This is a mock of how that place could look and behave. Every record in it was invented. | DoomParfum By TK ถูกวางแผนให้เป็นพื้นที่ส่วนตัวสำหรับอ่านเรื่องน้ำหอม ติดตามโน้ตกลิ่น และบันทึกคอลเลกชัน หน้านี้คือฉบับจำลองที่แสดงว่าพื้นที่นั้นอาจมีหน้าตาและการใช้งานอย่างไร ทุกบันทึกในที่นี้สร้างขึ้นเพื่อการสาธิต | ☐ OK · ☐ Fix: |
| U146 | `about.contents` | On this page | ในหน้านี้ | ☐ OK · ☐ Fix: |
| U147 | `about.purpose` | Purpose | จุดประสงค์ | ☐ OK · ☐ Fix: |
| U148 | `about.purposeText` | A fragrance record mixes several kinds of information: what a thing is called, which notes it declares, what people say about it, who sells it and whether you own it. Those belong in different places. This notebook is designed so that none of them can stand in for another. | บันทึกน้ำหอมหนึ่งรายการมีข้อมูลหลายประเภทปะปนกัน ทั้งชื่อเรียก โน้ตที่ระบุไว้ ความเห็นของผู้คน ผู้จำหน่าย และสถานะว่าคุณเป็นเจ้าของหรือไม่ ข้อมูลเหล่านี้ควรแยกจากกัน สมุดบันทึกนี้จึงออกแบบให้ข้อมูลประเภทหนึ่งไม่อาจแทนที่อีกประเภทหนึ่งได้ | ☐ OK · ☐ Fix: |
| U149 | `about.demonstrates` | What this mock demonstrates | สิ่งที่ฉบับจำลองนี้แสดง | ☐ OK · ☐ Fix: |
| U150 | `about.demo1` | Browsing and filtering a small set of fictional studies. | การเลือกดูและกรองแบบศึกษาสมมติชุดเล็ก ๆ | ☐ OK · ☐ Fix: |
| U151 | `about.demo2` | Reading top, heart and base layers as labels, with general notes and accords kept apart. | การอ่านท็อปโน้ต ฮาร์ตโน้ต และเบสโน้ตในฐานะชื่อเรียก โดยแยกโน้ตทั่วไปและแอคคอร์ดไว้ต่างหาก | ☐ OK · ☐ Fix: |
| U152 | `about.demo3` | Following a note to every study that lists it. | การติดตามโน้ตหนึ่งไปยังทุกแบบศึกษาที่ระบุโน้ตนั้น | ☐ OK · ☐ Fix: |
| U153 | `about.demo4` | Telling an unknown field from one that was authored as empty. | การแยกข้อมูลที่ไม่ได้ระบุ ออกจากข้อมูลที่บันทึกไว้ว่าว่างเปล่า | ☐ OK · ☐ Fix: |
| U154 | `about.scope` | What remains future | สิ่งที่ยังเป็นงานในอนาคต | ☐ OK · ☐ Fix: |
| U155 | `about.scopeText1` | Nothing here connects to a real catalogue, an account or a store. Scent matching, the private catalogue, permission to use outside sources, account security, the cart and the collection are separate pieces of work. Each has its own approval, and this mock approves none of them. | ไม่มีส่วนใดในที่นี้เชื่อมต่อกับแคตตาล็อกจริง บัญชีผู้ใช้ หรือร้านค้า ทั้งการจับคู่กลิ่น แคตตาล็อกส่วนตัว สิทธิ์ในการใช้แหล่งข้อมูลภายนอก ความปลอดภัยของบัญชี ตะกร้า และคอลเลกชัน ล้วนเป็นงานแยกกันที่ต้องได้รับอนุมัติของตนเอง และฉบับจำลองนี้ไม่ได้อนุมัติงานใดเลย | ☐ OK · ☐ Fix: |
| U156 | `about.scopeText2` | The mock runs on one computer. It asks search engines not to index it, and that request is not a security control. | ฉบับจำลองนี้ทำงานบนคอมพิวเตอร์เครื่องเดียว มีการขอไม่ให้เครื่องมือค้นหาจัดทำดัชนี แต่คำขอนั้นไม่ใช่มาตรการด้านความปลอดภัย | ☐ OK · ☐ Fix: |
| U157 | `about.journal` | The scent notebook | สมุดบันทึกกลิ่น | ☐ OK · ☐ Fix: |
| U158 | `about.journalText` | Two sample articles about reading this mock. They make no claim about any real product. | บทความตัวอย่างสองบทว่าด้วยการอ่านฉบับจำลองนี้ ไม่ได้กล่าวอ้างถึงผลิตภัณฑ์จริงใด | ☐ OK · ☐ Fix: |
| U159 | `about.credits` | Local credits | เครดิต | ☐ OK · ☐ Fix: |
| U160 | `about.creditsText` | The drawings, records and articles were made for this project. Type is set in Bodoni Moda, Fahkwang and Noto Sans Thai under the SIL Open Font License 1.1, and icons come from Lucide under the ISC license. All of it is served from this computer. | ภาพวาด บันทึก และบทความทั้งหมดจัดทำขึ้นสำหรับโครงการนี้ ตัวอักษรใช้ Bodoni Moda, Fahkwang และ Noto Sans Thai ภายใต้ SIL Open Font License 1.1 ไอคอนมาจาก Lucide ภายใต้สัญญาอนุญาต ISC ทั้งหมดให้บริการจากคอมพิวเตอร์เครื่องนี้ | ☐ OK · ☐ Fix: |

## Fixture prose (32)

| # | Record and field | English source | Thai draft | Your answer |
|---|---|---|---|---|
| F1 | `mock-family-bright` descriptor | Edges, rims and thin light. | ขอบ ริม และแสงบาง ๆ | ☐ OK · ☐ Fix: |
| F2 | `mock-family-soft` descriptor | Folds, threads and slow curves. | รอยพับ เส้นด้าย และส่วนโค้งที่ค่อย ๆ เปลี่ยน | ☐ OK · ☐ Fix: |
| F3 | `mock-family-deep` descriptor | Strata, weight and late ink. | ชั้นหิน น้ำหนัก และหมึกยามดึก | ☐ OK · ☐ Fix: |
| F4 | `mock-note-001` descriptor | The cool edge of a cut sheet. | ขอบเย็นของแผ่นกระดาษที่เพิ่งตัด | ☐ OK · ☐ Fix: |
| F5 | `mock-note-002` descriptor | A dry thread pulled straight. | เส้นด้ายแห้งที่ถูกดึงจนตึง | ☐ OK · ☐ Fix: |
| F6 | `mock-note-003` descriptor | A bright rim, seen edge-on. | ริมที่สว่าง มองจากด้านข้าง | ☐ OK · ☐ Fix: |
| F7 | `mock-note-004` descriptor | Warm dust on a high shelf. | ฝุ่นอุ่นบนชั้นวางสูง | ☐ OK · ☐ Fix: |
| F8 | `mock-note-005` descriptor | Wet slate before noon. | หินชนวนเปียกก่อนเที่ยง | ☐ OK · ☐ Fix: |
| F9 | `mock-note-006` descriptor | Soft wax, barely marked. | ขี้ผึ้งนุ่มที่แทบไม่มีรอย | ☐ OK · ☐ Fix: |
| F10 | `mock-note-007` descriptor | Late ink, not yet dry. | หมึกยามดึกที่ยังไม่แห้ง | ☐ OK · ☐ Fix: |
| F11 | `mock-note-008` descriptor | A pale trace left in a room. | ร่องรอยจาง ๆ ที่หลงเหลืออยู่ในห้อง | ☐ OK · ☐ Fix: |
| F12 | `mock-note-009` descriptor | A label with no supplied relationships. | ชื่อที่ยังไม่มีการระบุความเชื่อมโยง | ☐ OK · ☐ Fix: |
| F13 | `mock-perfume-001` description | A fictional record kept deliberately incomplete. Its heart was never supplied, and its base was authored as empty. The two read differently on purpose. | บันทึกสมมติที่ตั้งใจเก็บไว้ไม่ครบ ฮาร์ตโน้ตไม่เคยได้รับการระบุ ส่วนเบสโน้ตถูกบันทึกไว้ว่าว่างเปล่า สองสิ่งนี้จึงมีความหมายต่างกันโดยเจตนา | ☐ OK · ☐ Fix: |
| F14 | `mock-perfume-002` description | A fictional sheet folded once, written as a quiet opening that settles without hurry. | กระดาษสมมติที่พับเพียงครั้งเดียว เปิดอย่างแผ่วเบา แล้วค่อย ๆ สงบลงโดยไม่เร่งรีบ | ☐ OK · ☐ Fix: |
| F15 | `mock-perfume-003` description | A fictional page of late ink. Most of its weight was authored into the last layer. | หน้ากระดาษสมมติที่เขียนด้วยหมึกยามดึก น้ำหนักส่วนใหญ่ถูกบันทึกไว้ในระดับสุดท้าย | ☐ OK · ☐ Fix: |
| F16 | `mock-perfume-004` description | Fictional cloth in morning light: one thread at the start, one at the end, and room between them. | ผืนผ้าสมมติในแสงยามเช้า มีด้ายหนึ่งเส้นตอนเริ่ม อีกหนึ่งเส้นตอนจบ และมีที่ว่างอยู่ระหว่างกลาง | ☐ OK · ☐ Fix: |
| F17 | `mock-perfume-005` description | A fictional weave recorded at three distances. Every layer was supplied, so this is the plainest record to read first. | ลายทอสมมติที่บันทึกไว้จากสามระยะ ทุกระดับได้รับการระบุครบ จึงเป็นบันทึกที่อ่านง่ายที่สุดสำหรับผู้เริ่มต้น | ☐ OK · ☐ Fix: |
| F18 | `mock-perfume-007` description | A fictional pane seen edge-on. Bright at the rim, then almost nothing. | แผ่นกระจกสมมติที่มองจากด้านข้าง สว่างที่ขอบ แล้วแทบไม่มีอะไรเลย | ☐ OK · ☐ Fix: |
| F19 | `mock-perfume-008` description | Fictional light through two curved surfaces, arriving in order: rim, slate, wax. | แสงสมมติที่ผ่านพื้นผิวโค้งสองชั้น มาถึงตามลำดับ: ริม หินชนวน ขี้ผึ้ง | ☐ OK · ☐ Fix: |
| F20 | `mock-perfume-009` description | A fictional study whose family was never assigned. It stays in the catalogue with its family shown as unknown. | แบบศึกษาสมมติที่ไม่เคยได้รับการกำหนดตระกูลกลิ่น ยังคงอยู่ในแคตตาล็อกโดยแสดงตระกูลกลิ่นว่าไม่ทราบ | ☐ OK · ☐ Fix: |
| F21 | `mock-perfume-010` description | Fictional strata, read from the surface down. The base carries three labels and is the longest list in this mock. | ชั้นหินสมมติที่อ่านจากผิวลงไป เบสโน้ตมีสามชื่อ และเป็นรายการที่ยาวที่สุดในฉบับจำลองนี้ | ☐ OK · ☐ Fix: |
| F22 | `mock-perfume-011` description | A fictional boulder with a long and slightly impractical description, kept here so that wrapping, zooming and larger text can be checked against something more demanding than a single tidy line. It names no real material and makes no claim about wear. | ก้อนหินสมมติที่มีคำบรรยายยาวและออกจะไม่ค่อยมีประโยชน์นัก เก็บไว้เพื่อใช้ตรวจการตัดบรรทัด การขยายหน้าจอ และข้อความขนาดใหญ่ กับสิ่งที่ยากกว่าบรรทัดสั้น ๆ ที่เรียบร้อยเพียงบรรทัดเดียว คำบรรยายนี้ไม่ได้ระบุวัสดุจริงใด และไม่ได้กล่าวอ้างเรื่องความคงทน | ☐ OK · ☐ Fix: |
| F23 | `mock-article-001` title | Reading a layer | อ่านทีละระดับ | ☐ OK · ☐ Fix: |
| F24 | `mock-article-001` excerpt | Top, heart and base are an order of reading. They are not a recipe. | ท็อปโน้ต ฮาร์ตโน้ต และเบสโน้ต คือลำดับของการอ่าน ไม่ใช่สูตรผสม | ☐ OK · ☐ Fix: |
| F25 | `mock-article-001` body ¶1 | Every record in this mock can carry three layers. Top is what was written first, heart is what was written to stay, and base is what was written to remain. The order describes reading, in the way chapters do. | ทุกบันทึกในฉบับจำลองนี้มีได้สามระดับ ท็อปโน้ตคือสิ่งที่บันทึกไว้ก่อน ฮาร์ตโน้ตคือสิ่งที่บันทึกไว้ให้คงอยู่ และเบสโน้ตคือสิ่งที่บันทึกไว้ให้หลงเหลือ ลำดับนี้บรรยายการอ่าน เช่นเดียวกับบทต่าง ๆ ในหนังสือ | ☐ OK · ☐ Fix: |
| F26 | `mock-article-001` body ¶2 | A layer holds labels, never amounts. Nothing here says how much of anything exists, how long it lasts or what it is made of. When a record lists one label and another lists three, the second list is longer and that is all it means. | แต่ละระดับเก็บเพียงชื่อโน้ต ไม่เคยเก็บปริมาณ ไม่มีสิ่งใดในที่นี้บอกว่ามีสิ่งใดอยู่มากเท่าใด ติดทนนานเท่าใด หรือทำจากอะไร เมื่อบันทึกหนึ่งมีหนึ่งชื่อและอีกบันทึกมีสามชื่อ รายการที่สองก็เพียงยาวกว่า และมีความหมายเพียงเท่านั้น | ☐ OK · ☐ Fix: |
| F27 | `mock-article-001` body ¶3 | General notes sit apart from the layers. They belong to the whole record and are never moved up or down to fill a gap. | โน้ตทั่วไปอยู่แยกจากโครงสร้าง 3 ระดับ เป็นของทั้งบันทึก และไม่เคยถูกย้ายขึ้นหรือลงเพื่อเติมช่องว่าง | ☐ OK · ☐ Fix: |
| F28 | `mock-article-002` title | Empty is not unknown | ว่างเปล่าไม่ใช่ไม่ทราบ | ☐ OK · ☐ Fix: |
| F29 | `mock-article-002` excerpt | Two records can look equally bare and mean opposite things. | บันทึกสองรายการอาจดูว่างเหมือนกัน แต่มีความหมายตรงข้ามกัน | ☐ OK · ☐ Fix: |
| F30 | `mock-article-002` body ¶1 | Paper study A has a heart that was never supplied and a base that was authored as empty. The first is a question nobody has answered. The second is an answer. | Paper study A มีฮาร์ตโน้ตที่ไม่เคยได้รับการระบุ และเบสโน้ตที่ถูกบันทึกไว้ว่าว่างเปล่า อย่างแรกคือคำถามที่ยังไม่มีใครตอบ อย่างหลังคือคำตอบ | ☐ OK · ☐ Fix: |
| F31 | `mock-article-002` body ¶2 | Catalogues often flatten the two into one blank space, and a reader then fills that space with a guess. This notebook keeps them apart: one says it was not supplied, the other says it has no entries. | แคตตาล็อกจำนวนมากมักรวมสองอย่างนี้ไว้เป็นช่องว่างเดียว แล้วผู้อ่านก็เติมช่องนั้นด้วยการคาดเดา สมุดบันทึกนี้แยกทั้งสองไว้ อย่างหนึ่งบอกว่าไม่ได้ระบุ อีกอย่างบอกว่าไม่มีรายการ | ☐ OK · ☐ Fix: |
| F32 | `mock-article-002` body ¶3 | The same care applies to a family, a description or a picture. When something is missing, the page says what is missing and leaves it there. | ความระมัดระวังเดียวกันใช้กับตระกูลกลิ่น คำบรรยาย หรือภาพ เมื่อมีสิ่งใดขาดไป หน้านั้นจะบอกว่าขาดอะไร และปล่อยไว้อย่างนั้น | ☐ OK · ☐ Fix: |

## Kept in Latin on Thai pages (for reference)

Fictional proper names stay unchanged (Owner-directed). Family and accord labels also stay Latin until the Owner decides; they are marked `lang="en"`. `mock-perfume-001` name "Paper study A"; `mock-perfume-002` name "Paper study B"; `mock-perfume-003` name "Paper study C"; `mock-perfume-004` name "Linen study D"; `mock-perfume-005` name "Linen study E"; `mock-perfume-006` name "Linen study F"; `mock-perfume-007` name "Glass study G"; `mock-perfume-008` name "Glass study H"; `mock-perfume-009` name "Glass study I"; `mock-perfume-010` name "Stone study J"; `mock-perfume-011` name "Stone study K"; `mock-perfume-012` name "แบบศึกษากระดาษ ลำดับที่สิบสอง"; `mock-note-001` "Ivrel"; `mock-note-002` "Oskane"; `mock-note-003` "Tavren"; `mock-note-004` "Marovane"; `mock-note-005` "Quellis"; `mock-note-006` "Sendrel"; `mock-note-007` "Ondrith"; `mock-note-008` "Luthmere"; `mock-note-009` "Vesk"; `mock-family-bright` "Bright study"; `mock-family-soft` "Soft study"; `mock-family-deep` "Deep study"; `mock-accord-001` "Folded quiet"; `mock-accord-002` "Open weave"; `mock-accord-003` "Settled weight"; `mock-accord-004` "Clear edge".

Paper study L is authored in Thai and keeps its Thai name and description on English pages (V11-OD-10: no English version by default).
