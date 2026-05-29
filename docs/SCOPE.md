# SCOPE.md
# SAKIPRO v1.0 Scope Control

Version: 1.0  
Status: Blueprint Revision  
Purpose: Kontrol cakupan rilis SAKIPRO v1.0.

---

## 1. Prinsip Scope v0.2

SAKIPRO v1.0 harus membuktikan alur inti dan perluasan review SAKIP:

1. Workspace dapat dibuat.
2. Dokumen dapat dibaca dan diindeks.
3. User dapat bertanya berbasis dokumen.
4. Review indikator, PK, LKjIP, cascading, dan evidence dapat dibuat dengan sumber.
5. Output tersimpan aman tanpa mengubah file asli.
6. Token, error, dan privacy event tercatat.

Fitur dashboard, task automation panjang, OCR, dan visualisasi lengkap masuk Post-v1.0.

---

## 2. v1.0 Core, Must Have

1. `sakipro init`
2. `sakipro doctor`
3. `sakipro scan <folder>`
4. `sakipro status`
5. `sakipro ask`
6. `sakipro cek-indikator`
7. `sakipro review-pk`
8. `sakipro token`
9. `sakipro privacy`
10. Document reader untuk DOCX, PDF teks, XLSX, CSV, TXT, dan Markdown.
11. Document classifier dan metadata registry.
12. SQLite storage untuk workspace, document, chunk, source reference, review, dan token usage.
13. Basic retrieval berbasis SQLite FTS/BM25 atau keyword search.
14. Markdown report.
15. XLSX report untuk review indikator dan PK.
16. Token usage log.
17. Privacy mode `standard` dan `strict`.
18. Rich panel, table, progress, error panel, success panel, dan suggested next steps.
19. Golden test dataset dan test offline tanpa live AI call.

---

## 3. v0.2 Should Have

1. `sakipro wizard` untuk alur scan, indikator, dan PK.
2. `sakipro chat` sederhana berbasis retrieval yang sama dengan `ask`.
3. Output DOCX sederhana dari template.
4. Basic autocomplete command.
5. Packaging PyInstaller one-folder untuk Windows.

---

## 4. v1.0 Expanded

1. `sakipro review-lkjip`
2. `sakipro cek-cascading`
3. `sakipro cek-evidence`
4. `sakipro report final`
5. Draft rekomendasi berbasis sumber.
6. Final report Markdown, XLSX pendukung, dan DOCX draft.
7. Graph-ready data model untuk cascading.
8. Slash command inti untuk fitur v0.2.

---

## 5. v0.2 Should Have, Advanced

1. Vector store (Ditiadakan - Digantikan SQLite FTS5 eksklusif untuk efisiensi).
2. Graph analysis dengan NetworkX.
3. Resume session.
4. Packaging macOS dan Linux yang dipoles.

---

## 6. Deferred to Post-v1.0

1. Workbench mode penuh.
2. Task board.
3. Graph visualization.
4. PDF export.
5. HTML report.
6. OCR scanned PDF.
7. Multi-OPD batch review.

---

## 7. Release Gate v0.2

v0.2 tidak boleh dirilis jika:

1. File asli dapat berubah oleh command apa pun.
2. API key atau data sensitif muncul di log.
3. Output AI tidak memiliki source reference.
4. Test golden dataset gagal.
5. `sakipro scan` tidak dapat menangani file gagal baca secara parsial.
6. Report tidak menandai hasil sebagai draft.
7. Review LKjIP, cascading, evidence, atau final report tidak memiliki source reference.
