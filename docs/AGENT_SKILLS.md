# SAKIPRO Agent Skills Blueprint

Version: 1.0
Date: 2026-05-28
Document Type: Agent Skills Definition
Audience: AI Engineer, Python Developer, Product Owner, QA Tester
Status: Implementation Blueprint
Changes from v0.2: Added SKL-022–026; expanded rules IND-008/009, PK-006, LKJ-006/007, CAS-003, EVD-004; fixed SKL-007 concern split; fixed SKL-011 output; upgraded SKL-018 scope.

---

## 1. Spesifikasi Operasional v1.0

## 2. Definisi Skill

Skill adalah unit komputasi modular (input/output terdefinisi, cacheable, testable, compliance-checked) yang menggabungkan parser, retrieval, rule-checking, dan reasoning.

---

## 3. Prinsip Umum Skill

Prinsip Skill:

1. Semua hasil faktual harus memiliki `source_refs`.
2. Semua hasil AI berstatus `draft`.
3. Semua angka, target, realisasi, anggaran, dan nama dokumen harus berasal dari sumber.
4. Privacy pipeline wajib berjalan sebelum konteks dikirim ke AI.
5. Skill tidak boleh membaca API key langsung dari `.env`; akses konfigurasi harus melalui settings/app context.
6. Skill tidak boleh menulis file output langsung tanpa report writer atau safe write utility.
7. Skill tidak boleh mengubah, menghapus, atau menimpa file asli.
8. Skill harus mendukung partial success bila memungkinkan.
9. Skill harus mengembalikan warning bila dokumen kurang, gagal dibaca, atau confidence rendah.
10. Skill harus dapat diuji tanpa live AI call.
11. **Skill tidak boleh menghasilkan output visual (Rich, tabel, tree).** Kembalikan data struct; UI layer yang merender.
12. **Cross-document skill harus merujuk minimal dua sumber sebelum menyatakan konflik atau koherensi.**

---

## 4. Agent dan Skill Mapping

| Agent | Skill Utama |
| --- | --- |
| Folder Scanner Agent | `SKL-001`, `SKL-002`, `SKL-003`, `SKL-004`, `SKL-005`, `SKL-006`, `SKL-016` |
| CLI Router Agent | `SKL-022`, `SKL-023` |
| OPD Planning Copilot Agent | `SKL-005`, `SKL-006`, `SKL-007`, `SKL-014`, `SKL-015`, `SKL-016`, `SKL-022`, `SKL-023` |
| Indicator Review Agent | `SKL-003`, `SKL-005`, `SKL-006`, `SKL-008`, `SKL-014`, `SKL-015`, `SKL-016`, `SKL-026` |
| PK Review Agent | `SKL-003`, `SKL-005`, `SKL-006`, `SKL-009`, `SKL-014`, `SKL-015`, `SKL-016`, `SKL-026` |
| LKjIP Review Agent | `SKL-003`, `SKL-005`, `SKL-006`, `SKL-010`, `SKL-014`, `SKL-015`, `SKL-016`, `SKL-026` |
| Cascading Review Agent | `SKL-003`, `SKL-005`, `SKL-006`, `SKL-011`, `SKL-014`, `SKL-015`, `SKL-016` |
| Evidence Review Agent | `SKL-003`, `SKL-005`, `SKL-006`, `SKL-012`, `SKL-014`, `SKL-015`, `SKL-016` |
| Rencana Aksi Review Agent | `SKL-003`, `SKL-005`, `SKL-006`, `SKL-024`, `SKL-014`, `SKL-015`, `SKL-016` |
| LHE Tracking Agent | `SKL-003`, `SKL-005`, `SKL-006`, `SKL-025`, `SKL-014`, `SKL-015`, `SKL-016` |
| Draft Agent | `SKL-005`, `SKL-006`, `SKL-013`, `SKL-014`, `SKL-015`, `SKL-016` |
| Report Agent | `SKL-015`, `SKL-016`, `SKL-017` |
| Task Agent | `SKL-018` and all review skills as subtasks |

---

## 5. Skill Inventory

| Skill ID | Skill Name | Status | Primary Purpose |
| --- | --- | --- | --- |
| `SKL-001` | Workspace Initialization Skill | v0.2 | Membuat workspace lokal SAKIPRO |
| `SKL-002` | Runtime Doctor Skill | v0.2 | Mengecek kesiapan runtime, config, API key, dan asset |
| `SKL-003` | Document Reading Skill | v0.2 | Membaca file dokumen yang didukung |
| `SKL-004` | Document Classification Skill | v0.2 | Mengenali jenis dokumen SAKIP + quick health signal |
| `SKL-005` | Source Reference Skill | v0.2 | Membuat rujukan sumber yang dapat diaudit |
| `SKL-006` | Retrieval and Context Skill | v0.2 | Mengambil konteks relevan dari dokumen dengan strategi per query-type |
| `SKL-007` | Ask and Copilot Skill | v0.2 | Menjawab pertanyaan berbasis dokumen (Q&A only; routing ada di SKL-022) |
| `SKL-008` | Indicator Review Skill | v0.2 | Menilai mutu indikator kinerja (IND-001–009) |
| `SKL-009` | PK Consistency Review Skill | v0.2 | Mereview konsistensi Perjanjian Kinerja (PK-001–006) |
| `SKL-010` | LKjIP Review Skill | v0.2 | Mereview LKjIP, capaian, efisiensi, tren, dan tindak lanjut (LKJ-001–007) |
| `SKL-011` | SAKIP Mapping and Cascading Skill | v0.2 | Memetakan rantai logika kinerja, mendeteksi putus, keselarasan vertikal (CAS-001–003) |
| `SKL-012` | Evidence Audit Skill | v0.2 | Menghubungkan klaim kinerja dengan evidence (EVD-001–004) |
| `SKL-013` | Recommendation Drafting Skill | v0.2 | Menyusun draft rekomendasi berbasis sumber |
| `SKL-014` | Privacy Guardrail Skill | v0.2 | Masking dan blokir data sensitif |
| `SKL-015` | AI Contract Validation Skill | v0.2 | Validasi schema, source refs, confidence, dan draft |
| `SKL-016` | Token and Cost Control Skill | v0.2 | Estimasi dan pencatatan token |
| `SKL-017` | Report Generation Skill | v0.2 | Membuat output Markdown, XLSX, DOCX |
| `SKL-018` | Task Decomposition Skill | v0.2 Should Have (lite) | Memecah perintah panjang menjadi urutan skill calls |
| `SKL-019` | Model Management Skill | v0.2 Should Have | Mengelola model AI aktif dan daftar provider |
| `SKL-020` | Credential Management Skill | v0.2 Should Have | Menyimpan API key secara interaktif |
| `SKL-021` | Desk Evaluation Skill | v1.0 Expanded | Mensimulasikan penilaian dan estimasi predikat SAKIP |
| `SKL-022` | CLI Intent & Command Router Skill | v1.0 Expanded | Mendeteksi intent input REPL dan routing ke skill/agent yang tepat |
| `SKL-023` | Contextual Next-Step Recommendation Skill | v1.0 Expanded | Menghasilkan 3 rekomendasi langkah berikutnya berbasis state review |
| `SKL-024` | Rencana Aksi & Monitoring Skill | v1.0 Expanded | Mereview kualitas rencana aksi dan progress monitoring |
| `SKL-025` | LHE Tindak Lanjut Tracking Skill | v1.0 Expanded | Memetakan setiap rekomendasi LHE ke status tindak lanjut dan buktinya |
| `SKL-026` | Cross-Document Coherence Skill | v1.0 Expanded | Memeriksa koherensi satu indikator/target yang sama di seluruh dokumen |

---

## 6. Skill Definitions

### SKL-001, Workspace Initialization Skill

| Field | Definition |
| --- | --- |
| Status | v0.2 |
| Used By | CLI Init Command, Folder Scanner Agent |
| Purpose | Membuat struktur workspace lokal agar SAKIPRO dapat menyimpan konfigurasi, database, log, cache, output, dan history. |
| Command | `sakipro init` |
| Input | Nama project opsional, root folder opsional, privacy mode default |
| Output | Folder `.sakipro/`, `config.yaml`, `.env.example`, `logs/`, `cache/`, `memory/`, `outputs/`, `history`, database awal |
| Source Refs Required | No |
| Privacy Required | Yes, default config harus `standard` |
| Rulebook | Not applicable |
| Failure Modes | `OUTPUT_WRITE_FAILED`, `CONFIG_MISSING`, permission denied |
| Acceptance Criteria | Workspace dibuat, file config tersedia, `.env.example` tersedia, folder output/log tersedia, tidak ada secret di file contoh |
| Tests | `test_cli_init.py`, config creation test |

Implementation notes:

1. Tidak boleh menimpa konfigurasi lama tanpa konfirmasi.
2. Harus memakai safe write.
3. Harus menampilkan next steps: isi API key, jalankan `sakipro doctor`, lalu `sakipro scan`.

---

### SKL-002, Runtime Doctor Skill

| Field | Definition |
| --- | --- |
| Status | v0.2 |
| Used By | CLI Doctor Command |
| Purpose | Mengecek kesiapan lingkungan sebelum user menjalankan scan atau AI review. |
| Command | `sakipro doctor` |
| Input | Active workspace path, config path |
| Output | Status runtime, config, API key, provider, database, output dir, bundled assets |
| Source Refs Required | No |
| Privacy Required | Yes, secret tidak boleh dicetak |
| Rulebook | Not applicable |
| Failure Modes | `CONFIG_MISSING`, `API_KEY_MISSING`, `OUTPUT_WRITE_FAILED` |
| Acceptance Criteria | API key hanya tampil sebagai `found`, `missing`, atau `invalid`; `.env` tidak masuk log; asset wajib terdeteksi |
| Tests | `test_doctor.py`, secret masking test |

Implementation notes:

1. Doctor tidak boleh menjalankan live AI call kecuali user memilih validasi provider.
2. Doctor harus memeriksa template, database path, permission folder, dan package dependency inti.

---

### SKL-003, Document Reading Skill

| Field | Definition |
| --- | --- |
| Status | v0.2 |
| Used By | Folder Scanner Agent, review agents |
| Purpose | Membaca file dalam folder kerja dan mengekstrak teks/tabel yang dapat diindeks. |
| Command | `sakipro scan <folder>` |
| Input | File path, extension, workspace ID |
| Output | Extracted content, metadata, chunk candidates, read status |
| Source Refs Required | Yes, for extracted chunks |
| Privacy Required | Yes |
| Rulebook | Not applicable |
| Failure Modes | `FILE_READ_FAILED`, `FILE_PARTIAL_READ`, unsupported format, password-protected file |
| Acceptance Criteria | DOCX, PDF teks, XLSX, CSV, TXT, dan Markdown dapat diproses; file gagal masuk summary; partial success didukung |
| Tests | `test_docx_reader.py`, `test_pdf_reader.py`, `test_xlsx_reader.py`, `test_csv_reader.py`, `test_chunker.py` |

Supported file types:

| Type | Reader | Minimum Extraction |
| --- | --- | --- |
| DOCX | `python-docx` | paragraphs, tables, paragraph index |
| PDF teks | `PyMuPDF`, `pdfplumber` | text blocks, page number |
| XLSX | `openpyxl`, `pandas` | sheet, rows, cell range |
| CSV | built-in/pandas | rows and columns |
| TXT | built-in | lines or text windows |
| Markdown | built-in/markdown parser | headings, sections, lines |

Implementation notes:

1. Scan folder harus recursive.
2. File asli tidak boleh dimodifikasi.
3. PDF hasil scan gambar tanpa text layer harus diberi warning, bukan membuat proses total gagal.
4. OCR bukan v0.2 core.

---

### SKL-004, Document Classification Skill

| Field | Definition |
| --- | --- |
| Status | v0.2 |
| Used By | Folder Scanner Agent |
| Purpose | Mengenali jenis dokumen SAKIP dari nama file, struktur, metadata, dan isi awal. Setelah klasifikasi selesai, hasilkan **quick health signals** secara deterministic tanpa AI call. |
| Command | `sakipro scan <folder>` |
| Input | File metadata, file name, extracted preview, folder path |
| Output | `document_type`, year, OPD name candidate, confidence, warning, `health_signals` |
| Source Refs Required | Recommended |
| Privacy Required | Yes |
| Rulebook | Not applicable |
| Failure Modes | unknown document type, low confidence classification |
| Acceptance Criteria | Dokumen utama dapat dikenali atau ditandai unknown; `health_signals` muncul setelah scan tanpa token AI |
| Tests | `test_classifier.py`, golden scan fixture, health signal test |

Document types:

1. `renstra`
2. `renja`
3. `iku`
4. `pk`
5. `lkjip`
6. `rka`
7. `dpa`
8. `lhe`
9. `rencana_aksi`
10. `matriks_tindak_lanjut`
11. `evidence`
12. `other`

Quick Health Signal Schema (deterministik, tanpa AI):

```json
{
  "health_signals": [
    { "signal": "pk_without_iku", "severity": "high", "detail": "PK ditemukan tapi tidak ada dokumen IKU pembanding" },
    { "signal": "lkjip_without_pk", "severity": "high", "detail": "LKjIP ada tapi PK tidak ditemukan" },
    { "signal": "evidence_unreadable", "severity": "medium", "detail": "4 file evidence tidak dapat dibaca" },
    { "signal": "rencana_aksi_missing", "severity": "medium", "detail": "Rencana Aksi tidak ditemukan di folder" }
  ]
}
```

Implementation notes:

1. Deterministic filename and keyword rules harus menjadi default.
2. AI classification hanya dipakai bila klasifikasi deterministic tidak cukup dan user mengizinkan token.
3. `health_signals` dihasilkan oleh rule engine, bukan AI — tidak ada token cost.
4. `health_signals` ditampilkan sebagai summary langsung setelah scan selesai.

---

### SKL-005, Source Reference Skill

| Field | Definition |
| --- | --- |
| Status | v0.2 |
| Used By | All AI-bound agents |
| Purpose | Membuat dan memvalidasi rujukan sumber untuk setiap chunk, fakta, temuan, dan rekomendasi. |
| Command | All review and ask commands |
| Input | Extracted chunk, document metadata, location metadata |
| Output | `source_refs` records |
| Source Refs Required | Yes |
| Privacy Required | Yes, quote harus masked jika perlu |
| Rulebook | Required for review findings |
| Failure Modes | missing chunk ID, missing document ID, missing location, quote contains sensitive data |
| Acceptance Criteria | Semua klaim faktual AI dapat ditelusuri ke document ID, chunk ID, file path, document type, dan lokasi |
| Tests | source ref builder test, AI parser source validation test |

Source reference schema:

```json
{
  "source_id": "src_001",
  "document_id": "doc_001",
  "file_path": "Dokumen_SAKIP_OPD/PK_2026.docx",
  "document_type": "pk",
  "page": 3,
  "sheet": null,
  "cell_range": null,
  "paragraph_index": 18,
  "chunk_id": "chk_042",
  "quote": "short masked quote",
  "extraction_method": "docx_paragraph",
  "confidence": "high"
}
```

Implementation notes:

1. `quote` harus pendek.
2. `quote` tidak boleh berisi data sensitif yang belum dimasking.
3. Review finding tanpa source refs harus ditolak dengan `AI_SOURCE_REQUIRED`.

---

### SKL-006, Retrieval and Context Skill

| Field | Definition |
| --- | --- |
| Status | v0.2 |
| Used By | Copilot, Indicator Review, PK Review, dan semua review agents |
| Purpose | Mengambil potongan dokumen yang relevan dengan strategi retrieval yang disesuaikan per tipe query. |
| Command | `sakipro ask`, `sakipro cek-indikator`, `sakipro review-pk`, dan semua review commands |
| Input | Query, query_type, command type, rule IDs, document type filters, token budget |
| Output | Retrieval bundle containing chunks, source refs, warnings, estimated tokens |
| Source Refs Required | Yes |
| Privacy Required | Yes |
| Rulebook | Command-dependent |
| Failure Modes | no relevant source, too many chunks, token limit exceeded, strict privacy blocked |
| Acceptance Criteria | Context yang diberikan ke AI berasal dari indeks lokal dan menyertakan source refs; strategi retrieval sesuai tipe query |
| Tests | retrieval fixture test, FTS/BM25 test, no-source test, multi-doc alignment test |

Retrieval bundle:

```json
{
  "query": "review PK 2026",
  "query_type": "cross_document_comparison",
  "chunks": [],
  "source_refs": [],
  "warnings": [],
  "estimated_tokens": 12000
}
```

Strategi retrieval per tipe query:

| Query Type | Strategi | Contoh |
| --- | --- | --- |
| `exact_fact` | SQLite FTS exact match | "berapa target nilai SAKIP di PK 2026?" |
| `conceptual` | BM25 + semantic fallback | "apa maksud indikator outcome?" |
| `cross_document_comparison` | Multi-document retrieval dengan alignment | "bandingkan target PK 2026 dengan Renstra" |
| `rule_check` | Targeted extraction per rule ID | semua review commands |

Implementation notes:

1. **Arsitektur SQLite FTS-Only:** SAKIPRO secara eksklusif menggunakan pencarian berbasis indeks teks penuh **SQLite FTS5 (BM25)** dan ekstraksi kata kunci deterministik. Mengingat target laptop kantor CPU-only dengan RAM 8GB, penggunaan database vektor eksternal (seperti ChromaDB/FAISS) **ditiadakan** untuk menjaga penggunaan memori tetap minimal (0% memory overhead tambahan).
2. **Sliding Context Budget:** `core/context_builder.py` wajib menerapkan batas dinamis token masukan (*sliding token limits*):
   - **Light Tier (Fast):** Maksimal 15.000 token input.
   - **Default/Reasoning Tier:** Maksimal 60.000 token input.
3. Chunks diurutkan berdasarkan skor relevansi BM25 dan dihentikan secara kumulatif ketika token mendekati batas untuk mencegah pemborosan token dan fenomena *lost in the middle*.
4. Untuk `cross_document_comparison`, retrieval harus mengambil minimal dua sumber pembanding bila tersedia.
5. Jika sumber kurang, skill harus mengembalikan warning dan menurunkan confidence.
6. `query_type` ditentukan oleh SKL-022 (CLI Router) atau oleh review agent yang memanggil.

---

### SKL-007, Ask and Copilot Skill

| Field | Definition |
| --- | --- |
| Status | v0.2 |
| Used By | OPD Planning Copilot Agent |
| Purpose | Menjawab pertanyaan user berdasarkan dokumen yang sudah diindeks. Skill ini **hanya bertanggung jawab menjawab pertanyaan faktual/konseptual** — routing perintah natural language ke skill yang tepat dikerjakan oleh SKL-022. |
| Command | `sakipro ask`, REPL question input |
| Input | User question (already determined to be a Q&A by SKL-022), workspace ID, optional document filters |
| Output | Draft answer, source refs, confidence, suggested_next (diteruskan ke SKL-023) |
| Source Refs Required | Yes for factual answer |
| Privacy Required | Yes |
| Rulebook | Optional, depends on question |
| Failure Modes | no source found, privacy blocked, unsupported request, token limit exceeded |
| Acceptance Criteria | Jawaban berbasis dokumen memiliki sumber; jika sumber tidak ada, agent menjelaskan dokumen apa yang kurang |
| Tests | `test_ask.py`, mock AI source-required test |

Implementation notes:

1. `answer_question(query)` adalah satu-satunya public method. Routing tidak ada di sini.
2. Skill mengembalikan `suggested_next` (raw context hints) yang kemudian diproses oleh SKL-023.
3. Natural language seperti "review PK tahun 2026" **tidak** diproses di sini — itu tugas SKL-022.
4. Agent tidak boleh memberi jawaban faktual tanpa sumber.

---

### SKL-008, Indicator Review Skill

| Field | Definition |
| --- | --- |
| Status | v0.2 |
| Used By | Indicator Review Agent |
| Purpose | Mengekstrak dan menilai indikator kinerja OPD dari dokumen SAKIP. |
| Command | `sakipro cek-indikator` |
| Input | Indexed IKU, Renstra, Renja, PK, rule IDs `IND-001..IND-009` |
| Output | Indicator list, category, findings, recommendation, confidence, Markdown/XLSX report |
| Source Refs Required | Yes |
| Privacy Required | Yes |
| Rulebook | `IND-001` to `IND-009` |
| Failure Modes | indicator not found, target source missing, formula missing, low confidence extraction |
| Acceptance Criteria | Setiap indikator memiliki status, kategori, rule findings, rekomendasi, confidence, dan sumber |
| Tests | `test_indicator_checker.py`, `expected_review_indikator.json` |

Rule coverage:

| Rule ID | Skill Check |
| --- | --- |
| `IND-001` | Menilai apakah indikator outcome, output, aktivitas, input, impact, atau tidak jelas |
| `IND-002` | Memeriksa kejelasan definisi dan cakupan |
| `IND-003` | Memeriksa ketersediaan formula (numerator/denominator) |
| `IND-004` | Memeriksa satuan ukur |
| `IND-005` | Memeriksa sumber data dan unit penanggung jawab |
| `IND-006` | Memeriksa konsistensi target antar dokumen |
| `IND-007` | Memeriksa baseline |
| `IND-008` | Menilai realisme target vs baseline: apakah ada kenaikan bermakna? apakah loncat tanpa justifikasi? |
| `IND-009` | Menilai sensitivitas/validitas proxy: apakah indikator benar-benar mengukur yang diklaim? |

Implementation notes:

1. Deterministic table extraction harus digunakan sebelum AI reasoning.
2. AI dipakai untuk klasifikasi kualitatif (IND-001, IND-009) dan rekomendasi.
3. IND-008 membutuhkan data baseline — jika tidak ada, kembalikan warning bukan error.
4. Target conflict (IND-006) tidak boleh dinyatakan tanpa dua sumber pembanding; gunakan SKL-026 untuk lintas dokumen.

---

### SKL-009, PK Consistency Review Skill

| Field | Definition |
| --- | --- |
| Status | v0.2 |
| Used By | PK Review Agent |
| Purpose | Mereview Perjanjian Kinerja dan membandingkannya dengan dokumen perencanaan dan rencana aksi. |
| Command | `sakipro review-pk` |
| Input | PK, IKU, Renstra, Renja, Rencana Aksi (opsional), RKA/DPA (opsional), rule IDs `PK-001..PK-006` |
| Output | PK findings, target/unit consistency matrix, recommendation, Markdown/XLSX report |
| Source Refs Required | Yes |
| Privacy Required | Yes |
| Rulebook | `PK-001` to `PK-006` |
| Failure Modes | PK missing, comparison document missing, ambiguous indicator match, low confidence |
| Acceptance Criteria | Temuan PK memiliki rule ID, severity, source refs, confidence, dan rekomendasi |
| Tests | `test_pk_checker.py`, `expected_review_pk.json` |

Rule coverage:

| Rule ID | Skill Check |
| --- | --- |
| `PK-001` | Sasaran PK sesuai dokumen perencanaan |
| `PK-002` | Indikator PK konsisten nama, satuan, definisi |
| `PK-003` | Target PK konsisten dengan IKU/Renstra |
| `PK-004` | Program/kegiatan mendukung sasaran |
| `PK-005` | Penanggung jawab jelas |
| `PK-006` | Target milestone triwulanan/semesteran tersedia; jika tidak ada, tandai sebagai warning |

Implementation notes:

1. PK target mismatch harus memiliki source refs dari kedua dokumen.
2. Missing comparison document harus menjadi warning, bukan hallucinated conflict.
3. PK-006 bersifat advisory jika Rencana Aksi tidak ditemukan — jangan gagalkan review.
4. Hasil report wajib berstatus draft.

---

### SKL-010, LKjIP Review Skill

| Field | Definition |
| --- | --- |
| Status | v0.2 |
| Used By | LKjIP Review Agent |
| Purpose | Mereview kualitas LKjIP berdasarkan target PK, realisasi, analisis capaian, efisiensi anggaran, tren multi-tahun, evidence, dan tindak lanjut LHE. |
| Command | `sakipro review-lkjip` |
| Input | LKjIP (current + up to 2 prior years if available), PK, LHE, RKA/DPA, evidence metadata, rule IDs `LKJ-001..LKJ-007` |
| Output | LKjIP findings, analysis gap, efficiency notes, trend data, follow-up findings, recommendation |
| Source Refs Required | Yes |
| Privacy Required | Yes |
| Rulebook | `LKJ-001` to `LKJ-007` |
| Failure Modes | LKjIP missing, PK missing, realization missing, budget source missing, prior-year LKjIP not found |
| Acceptance Criteria | Kelemahan LKjIP tampil dengan sumber dan human validation flag bila bukti kurang; tren multi-tahun ditampilkan jika data tersedia |
| Tests | v0.2 golden LKjIP fixture |

Rule coverage:

| Rule ID | Skill Check |
| --- | --- |
| `LKJ-001` | Realisasi dibandingkan target PK |
| `LKJ-002` | Analisis penyebab tersedia dan mendalam |
| `LKJ-003` | Efisiensi anggaran dianalisis (% kinerja vs % serapan) |
| `LKJ-004` | Tindak lanjut LHE dicatat (link ke SKL-025 untuk detail) |
| `LKJ-005` | Evidence mendukung klaim |
| `LKJ-006` | Tren capaian minimal 3 tahun tersedia; jika hanya satu tahun, flag sebagai data kurang |
| `LKJ-007` | Kedalaman narasi analisis: apakah menjawab "mengapa" dan "apa yang akan berbeda"? |

Implementation notes:

1. Jangan menyimpulkan efisiensi anggaran tanpa sumber capaian dan anggaran.
2. LKJ-006 hanya dapat dijalankan jika LKjIP tahun sebelumnya terindeks; jika tidak, kembalikan warning bukan error.
3. LKJ-007 memerlukan AI reasoning untuk menilai kedalaman narasi.
4. Skill ini berkoordinasi dengan SKL-025 untuk detail tindak lanjut LHE.

---

### SKL-011, SAKIP Mapping and Cascading Skill

| Field | Definition |
| --- | --- |
| Status | v0.2 |
| Used By | Cascading Review Agent, Performance Tree feature |
| Purpose | Memetakan komponen SAKIP dari sasaran sampai evidence, mendeteksi rantai logika yang putus, dan memeriksa keselarasan vertikal dengan RPJMD/RKPD. |
| Command | `sakipro cek-cascading`, `sakipro cek-pohon` |
| Input | Renstra, Renja, IKU, PK, RKA, DPA, LKjIP, evidence metadata, RPJMD/RKPD (opsional) |
| Output | `CascadingMap` data struct (node list, edge list, broken chains, vertical alignment status) — **bukan Rich Tree** |
| Source Refs Required | Yes |
| Privacy Required | Yes |
| Rulebook | `CAS-001`, `CAS-002`, `CAS-003` |
| Failure Modes | missing document, ambiguous relation, disconnected chain, low confidence edge |
| Acceptance Criteria | Relasi sasaran → indikator → program → kegiatan → anggaran dapat ditampilkan atau ditandai missing; `CascadingMap` dapat dirender oleh UI layer |
| Tests | v0.2 cascading fixture, graph validation test |

Output schema:

```python
@dataclass
class CascadingMap:
    nodes: list[CascadingNode]
    edges: list[CascadingEdge]
    broken_chains: list[BrokenChain]
    vertical_alignment: VerticalAlignmentResult  # CAS-003
    warnings: list[str]
    source_refs: list[SourceRef]
```

Mapped entities:

1. `sasaran`
2. `indikator`
3. `target`
4. `program`
5. `kegiatan`
6. `subkegiatan`
7. `anggaran`
8. `realisasi`
9. `evidence`
10. `rekomendasi_lhe`
11. `tindak_lanjut`

Rule coverage:

| Rule ID | Skill Check |
| --- | --- |
| `CAS-001` | Rantai logika sasaran → indikator → program → kegiatan → subkegiatan utuh |
| `CAS-002` | Relevansi kegiatan terhadap sasaran |
| `CAS-003` | Keselarasan sasaran OPD dengan sasaran Pemda (RPJMD/RKPD); jika dokumen tidak tersedia, tandai sebagai `data_kurang` |

Implementation notes:

1. v0.2 dapat memakai NetworkX untuk graph traversal.
2. Output skill adalah data (`CascadingMap`) — **rendering Rich Tree ada di `ui/tree.py`**.
3. Relasi yang dibuat AI harus memiliki confidence dan source refs.
4. CAS-003 hanya dijalankan jika RPJMD/RKPD terindeks.

---

### SKL-012, Evidence Audit Skill

| Field | Definition |
| --- | --- |
| Status | v0.2 |
| Used By | Evidence Review Agent, LKjIP Review Agent |
| Purpose | Menghubungkan klaim kinerja dengan bukti dukung dan menilai kekuatan evidence termasuk ketepatan waktu. |
| Command | `sakipro cek-evidence` |
| Input | Evidence folder, LKjIP claims, PK indicators, source refs |
| Output | Evidence matrix, valid evidence, weak evidence, missing evidence, recommendation |
| Source Refs Required | Yes |
| Privacy Required | Yes |
| Rulebook | `EVD-001`, `EVD-002`, `EVD-003`, `EVD-004` |
| Failure Modes | unreadable evidence, claim without evidence, evidence without date/context, low relevance |
| Acceptance Criteria | Klaim kinerja terhubung ke evidence atau ditandai evidence kosong/lemah/tidak tepat waktu |
| Tests | v0.2 evidence fixture |

Rule coverage:

| Rule ID | Skill Check |
| --- | --- |
| `EVD-001` | Evidence relevan dengan klaim |
| `EVD-002` | Evidence dapat diverifikasi |
| `EVD-003` | Evidence cukup |
| `EVD-004` | Tanggal evidence dalam periode klaim; evidence retroaktif atau di luar periode ditandai sebagai lemah |

Implementation notes:

1. Evidence tidak boleh dinyatakan valid jika file tidak terbaca.
2. Evidence harus ditautkan ke klaim dan sumber klaim.
3. EVD-004 memerlukan ekstraksi tanggal dari metadata file atau isi dokumen.
4. Jika tanggal tidak dapat diekstrak, kembalikan warning bukan fail.

---

### SKL-013, Recommendation Drafting Skill

| Field | Definition |
| --- | --- |
| Status | v0.2 |
| Used By | Draft Agent, OPD Planning Copilot Agent |
| Purpose | Menyusun draft rekomendasi perbaikan berdasarkan temuan yang sudah tervalidasi. |
| Command | `sakipro draft` |
| Input | Review findings, rule IDs, source refs, output type |
| Output | Draft recommendation, narrative draft, action matrix |
| Source Refs Required | Yes |
| Privacy Required | Yes |
| Rulebook | Depends on finding type |
| Failure Modes | no finding available, source refs missing, unsupported draft type |
| Acceptance Criteria | Draft rekomendasi menyebut masalah, dampak, rekomendasi, prioritas, dan sumber |
| Tests | recommendation fixture, schema validation test |

Draft types:

1. Rekomendasi perbaikan indikator.
2. Narasi analisis LKjIP.
3. Matriks tindak lanjut LHE.
4. Perbaikan rumusan sasaran.
5. Catatan review PK.

Implementation notes:

1. Draft tidak boleh memperkenalkan fakta baru tanpa sumber.
2. Semua draft harus diberi label `draft`.

---

### SKL-014, Privacy Guardrail Skill

| Field | Definition |
| --- | --- |
| Status | v0.2 |
| Used By | All AI-bound agents |
| Purpose | Mendeteksi, mengklasifikasi, memasking, atau memblokir data sensitif sebelum AI call dan logging. |
| Command | All AI-bound commands |
| Input | Chunks, prompt context, source quote, config privacy mode |
| Output | Masked chunks, privacy warnings, blocked chunks, safe log payload |
| Source Refs Required | No, but source quotes must be safe |
| Privacy Required | Yes |
| Rulebook | Not applicable |
| Failure Modes | `PRIVACY_BLOCKED`, unsafe quote, secret detected |
| Acceptance Criteria | NIK, nomor HP, email personal, rekening, API key, dan secret termasking atau diblokir sesuai mode |
| Tests | `test_privacy.py`, secret-in-log test |

Privacy pipeline:

```text
detect -> classify -> mask -> preview -> confirm -> send -> log_safe
```

Implementation notes:

1. Mode default adalah `standard`.
2. **Local PII Blocking (Compiled Regex Filters):** Validasi PII menggunakan objek regex Python terkompilasi (`re.compile`) dijalankan secara lokal sebelum data dikirim ke API Cloud. Hal ini menjamin pemindaian instan untuk NIK 16 digit, nomor HP Indonesia, rekening bank, email personal, dan pola API key.
3. Mode `strict` memblokir chunk secara total jika terdeteksi pola PII di atas, sedangkan mode `standard` melakukan masking otomatis sebelum data dikirim.
4. Raw prompt atau teks dokumen yang belum disensor tidak boleh disimpan ke dalam berkas log default (`sakipro.log`) untuk mencegah kebocoran data di perangkat.

---

### SKL-015, AI Contract Validation Skill

| Field | Definition |
| --- | --- |
| Status | v0.2 |
| Used By | All AI-bound agents |
| Purpose | Memastikan output AI sesuai schema, memiliki source refs, confidence, status draft, dan warning yang benar. |
| Command | All AI-bound commands |
| Input | Raw AI response, expected schema, known source refs |
| Output | Validated agent result or stable error |
| Source Refs Required | Yes for factual output |
| Privacy Required | Yes |
| Rulebook | Required for review commands |
| Failure Modes | `AI_SCHEMA_INVALID`, `AI_SOURCE_REQUIRED`, invalid rule ID, missing confidence |
| Acceptance Criteria | Output tanpa sumber ditolak; JSON rusak diretry sekali; low confidence diberi human validation flag |
| Tests | response parser tests, schema repair tests |

Validation checks:

1. JSON valid.
2. `draft=true`.
3. `status` valid.
4. `findings` memiliki `rule_id`, `severity`, `confidence`, dan `source_refs`.
5. Source refs resolve ke database.
6. Rule ID ada di rulebook.
7. Low confidence menghasilkan `needs_human_validation=true`.

Implementation notes:

1. Parser melakukan satu retry untuk schema repair.
2. Guardrail tidak boleh hanya mengandalkan prompt.

---

### SKL-016, Token and Cost Control Skill

| Field | Definition |
| --- | --- |
| Status | v0.2 |
| Used By | All AI-bound agents |
| Purpose | Mengestimasi token sebelum AI call, meminta konfirmasi untuk task mahal, dan mencatat token usage. |
| Command | `sakipro token`, all AI-bound commands |
| Input | Prompt estimate, context size, model, provider, config limits |
| Output | Token estimate, confirmation prompt, token usage record |
| Source Refs Required | No |
| Privacy Required | Yes, prompt text tidak disimpan |
| Rulebook | Not applicable |
| Failure Modes | `TOKEN_LIMIT_EXCEEDED`, missing pricing config, provider usage missing |
| Acceptance Criteria | Token usage tersimpan; task mahal meminta konfirmasi; laporan token dapat ditampilkan |
| Tests | `test_token_manager.py`, token threshold test |

Implementation notes:

1. Simpan jumlah token dan estimasi biaya, bukan prompt mentah.
2. Izinkan user memilih model hemat jika estimasi token tinggi.
3. Token report harus menampilkan penggunaan harian, bulanan, estimasi biaya, dan model terbanyak.

---

### SKL-017, Report Generation Skill

| Field | Definition |
| --- | --- |
| Status | v1.0 Core for Markdown/XLSX, v1.0 Expanded for final DOCX |
| Used By | Report Agent, review agents |
| Purpose | Membuat laporan hasil scan dan review ke file output baru. |
| Command | `sakipro report`, report step inside review commands |
| Input | Review result, findings, source refs, workspace metadata |
| Output | Markdown, XLSX, DOCX, JSON report |
| Source Refs Required | Yes for review reports |
| Privacy Required | Yes |
| Rulebook | Depends on report type |
| Failure Modes | `OUTPUT_WRITE_FAILED`, unsafe file path, template missing |
| Acceptance Criteria | Output dibuat di folder `outputs/`, tidak menimpa file lama, mencantumkan draft label dan source appendix |
| Tests | `test_report_writer.py`, output safety test |

v1.0 Core reports:

1. Scan summary Markdown.
2. Indicator review Markdown.
3. Indicator review XLSX.
4. PK review Markdown.
5. PK review XLSX.

v1.0 Expanded reports:

1. LKjIP review.
2. Cascading report.
3. Evidence audit XLSX.
4. Rencana Aksi review.
5. LHE tindak lanjut matrix.
6. Final DOCX report.
7. Recommendation DOCX.

Implementation notes:

1. Gunakan safe file naming.
2. Semua report AI wajib bertanda `draft`.
3. Source reference appendix wajib ada untuk review reports.

---

### SKL-018, Task Decomposition Skill

| Field | Definition |
| --- | --- |
| Status | v0.2 Should Have (lite sequential decomposition — tidak memerlukan orchestration framework) |
| Used By | Task Agent, CLI Router Agent |
| Purpose | Memecah perintah panjang dari REPL menjadi urutan skill calls yang dapat dieksekusi, dilacak, dan dilanjutkan. |
| Command | Input panjang di REPL, `/task`, `sakipro resume` |
| Input | Natural language task (setelah SKL-022 menentukan ini adalah complex task), workspace state, available skills |
| Output | Task plan (ordered list of skill calls), subtask status, resume checkpoint |
| Source Refs Required | Depends on subtask |
| Privacy Required | Yes |
| Rulebook | Depends on subtask |
| Failure Modes | unsupported task, missing workspace, subtask failure, token limit |
| Acceptance Criteria | Perintah seperti "review semua dokumen SAKIP saya" dipecah menjadi langkah-langkah yang jelas; setiap langkah menyimpan status; user bisa resume |
| Tests | `test_task_decomposer.py` |

Lite scope untuk v0.2:

1. Decomposition sederhana: scan → review indikator → review PK → laporan.
2. Status tracking per subtask (pending/running/done/failed).
3. Resume dari langkah terakhir yang selesai.
4. Tidak menggunakan LangGraph atau orchestration framework — cukup sequential Python list + state dict.

Implementation notes:

1. Kompleksitas framework boleh ditambahkan post-v0.2 jika pipeline v0.2 stabil.
2. Task decomposition tidak boleh melewati privacy dan token confirmation.

---

### SKL-019, Model Management Skill

| Field | Definition |
| --- | --- |
| Status | v0.2 Should Have |
| Used By | Shared / CLI |
| Purpose | Mengelola model AI yang digunakan: melihat daftar model, mengganti model aktif, dan mengatur tier model. |
| Command | `sakipro model list`, `sakipro model switch` |
| Input | Current config, available providers |
| Output | Updated config, model confirmation |
| Source Refs Required | No |
| Privacy Required | No |
| Rulebook | Not applicable |
| Failure Modes | Invalid model name, provider not configured, API key missing |
| Acceptance Criteria | User dapat melihat daftar model, mengganti model aktif, dan perubahan tersimpan di config |
| Tests | `test_model_router.py` |

---

### SKL-020, Credential Management Skill

| Field | Definition |
| --- | --- |
| Status | v0.2 Should Have |
| Used By | Shared / CLI |
| Purpose | Menginput dan menyimpan API Key ke file .env secara interaktif tanpa mengedit file manual. |
| Command | `sakipro config set-key` |
| Input | Provider selection, API key input |
| Output | Updated .env file, success confirmation |
| Source Refs Required | No |
| Privacy Required | Yes (API key harus dimasking di log) |
| Rulebook | Not applicable |
| Failure Modes | File permission error, invalid key format |
| Acceptance Criteria | API key tersimpan di .env, tidak muncul di log, doctor memvalidasi key presence |
| Tests | `test_config.py` |

---

### SKL-021, Desk Evaluation Skill

| Field | Definition |
| --- | --- |
| Status | v1.0 Expanded |
| Used By | Desk Evaluation Agent |
| Purpose | Mensimulasikan penilaian evaluator: mengagregasi temuan dari semua agen review, menghitung skor per komponen SAKIP, dan menghasilkan estimasi predikat. |
| Command | `sakipro report final` (sub-step) |
| Input | Aggregated findings from IndicatorReview, PKReview, LKjIPReview, EvidenceReview, CascadingReview |
| Output | `simulated_score`, `predicted_predicate`, `component_breakdown`, `strategic_recommendations` |
| Source Refs Required | Yes (inherits from upstream findings) |
| Privacy Required | Yes |
| Rulebook | All (IND, PK, LKJ, CAS, EVD) + scoring weights from SAKIP_RULEBOOK.md |
| Failure Modes | Insufficient findings (< 2 components), upstream agent failure, scoring model error |
| Acceptance Criteria | Skor per komponen sesuai bobot SAKIP_RULEBOOK, predikat AA-D valid, semua temuan dapat ditelusuri ke sumber |
| Tests | `test_desk_evaluation.py` |

Implementation notes:

1. Skill ini dijalankan sebagai bagian dari pipeline `sakipro report final`.
2. Skor harus konsisten dengan bobot di SAKIP_RULEBOOK.md (Perencanaan 30%, Pengukuran 30%, Pelaporan 15%, Evaluasi Internal 25%).
3. Output wajib bertanda `draft` dan `needs_human_validation=true`.

---

### SKL-022, CLI Intent & Command Router Skill

| Field | Definition |
| --- | --- |
| Status | v1.0 Expanded |
| Used By | CLI Router Agent, OPD Planning Copilot Agent |
| Purpose | Mendeteksi intent input dari REPL dan merutekan ke skill atau agent yang tepat dengan konfirmasi user. |
| Command | Semua input di REPL interaktif |
| Input | Raw user input string, workspace state, available skills list |
| Output | `RouterResult` berisi intent type, mapped skill/command, confidence, confirmation prompt (jika perlu) |
| Source Refs Required | No |
| Privacy Required | No (routing tidak melibatkan dokumen konten) |
| Rulebook | Not applicable |
| Failure Modes | ambiguous intent, unknown command, multi-intent input |
| Acceptance Criteria | `/review-pk` → langsung SKL-009; "review PK saya" → deteksi, petakan, konfirmasi; "apa itu outcome?" → SKL-007; input ambigu → clarification prompt |
| Tests | `test_intent_router.py`, intent fixture dataset |

Intent types:

| Intent Type | Contoh Input | Routing |
| --- | --- | --- |
| `slash_command` | `/review-pk`, `/cek-indikator` | Langsung ke skill terkait |
| `natural_command` | "review PK saya", "cek indikator" | Petakan ke skill + konfirmasi |
| `question_factual` | "berapa target nilai SAKIP di PK?" | SKL-007 dengan `query_type=exact_fact` |
| `question_conceptual` | "apa itu indikator outcome?" | SKL-007 dengan `query_type=conceptual` |
| `complex_task` | "review semua dokumen SAKIP OPD saya" | SKL-018 (task decomposition) |
| `ambiguous` | "cek itu" | Clarification prompt |

RouterResult schema:

```json
{
  "intent_type": "natural_command",
  "mapped_skill": "SKL-009",
  "mapped_command": "review-pk",
  "confidence": 0.91,
  "display_interpretation": "Saya pahami sebagai: /review-pk",
  "requires_confirmation": true,
  "query_type": null
}
```

Implementation notes:

1. **Zero-Token Router:** Routing bersifat deterministik untuk slash command dan kata kunci terstruktur (regex / keyword matching) yang dijalankan murni pada tingkat Python lokal (tanpa memanggil AI) untuk memastikan respons instan di bawah 100ms.
2. AI hanya dipanggil sebagai fallback jika input bahasa alami sangat ambigu (semantic intent routing).
3. Natural command mapping memakai keyword rules terlebih dahulu, AI hanya untuk edge case.
4. Confidence < 0.7 selalu menghasilkan clarification prompt.
5. Skill ini tidak pernah memanggil AI secara langsung untuk menjawab pertanyaan; melainkan melimpahkan payload Q&A ke SKL-007.

---

### SKL-023, Contextual Next-Step Recommendation Skill

| Field | Definition |
| --- | --- |
| Status | v1.0 Expanded |
| Used By | Semua agent (dieksekusi setelah setiap skill call selesai) |
| Purpose | Menghasilkan tepat 3 rekomendasi langkah berikutnya yang kontekstual berdasarkan state review saat ini. |
| Command | Otomatis dipanggil setelah setiap respons di REPL |
| Input | `ReviewState` (apa yang sudah direview, temuan aktif, dokumen yang belum direview), hasil skill terakhir |
| Output | `NextStepBundle` dengan tepat 3 rekomendasi |
| Source Refs Required | No |
| Privacy Required | No |
| Rulebook | Not applicable |
| Failure Modes | empty state (first run), all reviews complete |
| Acceptance Criteria | Selalu 3 rekomendasi; minimal 1 slash command + 1 pertanyaan natural language; kontekstual berdasarkan temuan terkini |
| Tests | `test_next_step.py`, state-based recommendation test |

NextStepBundle schema:

```json
{
  "recommendations": [
    {
      "type": "slash_command",
      "command": "/review-pk",
      "reason": "Ada 2 konflik target yang perlu dicek di PK"
    },
    {
      "type": "slash_command",
      "command": "/draft rekomendasi-indikator",
      "reason": "8 indikator perlu perbaikan, draft siap dibuat"
    },
    {
      "type": "natural_language",
      "text": "tunjukkan indikator mana yang paling mudah diperbaiki duluan",
      "reason": null
    }
  ]
}
```

Priority rules untuk menentukan 3 rekomendasi:

1. Jika ada temuan kritis (severity=critical), rekomendasi pertama selalu terkait temuan itu.
2. Jika ada dokumen yang terklasifikasi tapi belum direview, rekomendasikan review tersebut.
3. Jika semua review selesai, dorong ke `/report final`.
4. Selalu sertakan satu pertanyaan natural language yang relevan dengan temuan terkini.
5. Jangan merekomendasikan skill yang barusan selesai dijalankan kecuali ada konteks berbeda.

Implementation notes:

1. Skill ini tidak memanggil AI — sepenuhnya deterministic rule-based.
2. Ringan: jalankan dalam < 50ms untuk tidak memperlambat REPL.

---

### SKL-024, Rencana Aksi & Monitoring Skill

| Field | Definition |
| --- | --- |
| Status | v1.0 Expanded |
| Used By | Rencana Aksi Review Agent |
| Purpose | Mereview kualitas Rencana Aksi OPD: kelengkapan milestone, keterhubungan dengan PK, dan progress monitoring. |
| Command | `sakipro review-rencana-aksi` |
| Input | Rencana Aksi (xlsx/docx), PK terkait, LKjIP (opsional untuk membandingkan realisasi) |
| Output | Rencana Aksi findings, milestone completeness, PK alignment, recommendation |
| Source Refs Required | Yes |
| Privacy Required | Yes |
| Rulebook | `PK-006` (milestone), `CAS-001` (rantai logika) |
| Failure Modes | Rencana Aksi tidak ditemukan, format tidak dikenali, PK tidak tersedia untuk perbandingan |
| Acceptance Criteria | Setiap milestone diperiksa keberadaan dan konsistensinya dengan PK; temuan memiliki source refs |
| Tests | `test_rencana_aksi_checker.py`, golden Rencana Aksi fixture |

Review items:

1. Milestone triwulanan/semesteran tersedia.
2. Setiap milestone terhubung ke indikator PK.
3. Target milestone realistis dan terukur.
4. Penanggung jawab per milestone jelas.
5. Progress (jika LKjIP tersedia): apakah milestone tercapai sesuai jadwal?

Implementation notes:

1. Format Rencana Aksi sangat bervariasi antar OPD — harus toleran terhadap format berbeda.
2. Jika Rencana Aksi tidak ditemukan, beri warning bahwa PK-006 tidak dapat diverifikasi.
3. Output berupa matriks: milestone × status × sumber.

---

### SKL-025, LHE Tindak Lanjut Tracking Skill

| Field | Definition |
| --- | --- |
| Status | v1.0 Expanded |
| Used By | LHE Tracking Agent, LKjIP Review Agent |
| Purpose | Memetakan setiap rekomendasi LHE (dari Inspektorat) ke status tindak lanjut OPD, bukti perbaikan, dan gap yang belum ditindaklanjuti. |
| Command | `sakipro cek-tindak-lanjut-lhe` |
| Input | LHE (current + previous if available), LKjIP (for follow-up evidence), evidence folder |
| Output | Tindak Lanjut Matrix: setiap rekomendasi → status → bukti → gap |
| Source Refs Required | Yes |
| Privacy Required | Yes |
| Rulebook | `LKJ-004` |
| Failure Modes | LHE tidak ditemukan, rekomendasi tidak dapat diekstrak, matriks tindak lanjut tidak tersedia |
| Acceptance Criteria | Setiap rekomendasi LHE terpetakan ke salah satu status: `selesai`, `dalam_proses`, `belum_ditindaklanjuti`, `tidak_relevan` |
| Tests | `test_lhe_tracker.py`, LHE fixture |

Tindak Lanjut Matrix schema:

```json
{
  "lhe_source": "LHE_2025.pdf",
  "items": [
    {
      "rekomendasi_id": "REC-001",
      "rekomendasi_text": "...",
      "status": "selesai",
      "bukti": ["LKjIP_2025.docx hal.12", "Evidence/notulen_monev.pdf"],
      "gap": null,
      "source_refs": []
    }
  ],
  "summary": {
    "total": 8,
    "selesai": 5,
    "dalam_proses": 2,
    "belum_ditindaklanjuti": 1
  }
}
```

Implementation notes:

1. Ekstraksi rekomendasi dari LHE memerlukan pattern matching — format LHE bervariasi.
2. Status `selesai` hanya bisa diberikan jika ada bukti tindak lanjut yang terbaca.
3. Output ini dipakai langsung oleh SKL-013 untuk membuat matriks tindak lanjut draft.

---

### SKL-026, Cross-Document Coherence Skill

| Field | Definition |
| --- | --- |
| Status | v1.0 Expanded |
| Used By | Indicator Review Agent, PK Review Agent, LKjIP Review Agent |
| Purpose | Memeriksa koherensi satu indikator atau target yang sama ketika muncul di beberapa dokumen sekaligus — menemukan kontradiksi lintas dokumen yang tidak terdeteksi oleh review per-dokumen. |
| Command | Dipanggil otomatis oleh SKL-008, SKL-009, SKL-010 setelah ekstraksi data |
| Input | `IndicatorKey` (nama atau kode indikator), semua dokumen yang sudah terindeks |
| Output | `CoherenceReport` berisi semua nilai yang ditemukan per dokumen, status koherensi, dan konflik terdeteksi |
| Source Refs Required | Yes — setiap nilai harus memiliki source ref |
| Privacy Required | Yes |
| Rulebook | `IND-006`, `PK-003` |
| Failure Modes | indikator hanya ada di satu dokumen (tidak cukup untuk cross-check), nama indikator ambigu |
| Acceptance Criteria | Jika indikator yang sama muncul di ≥ 2 dokumen dengan nilai berbeda, konflik terdeteksi dan dilaporkan dengan source refs dari semua sumber |
| Tests | `test_coherence_checker.py`, multi-document conflict fixture |

CoherenceReport schema:

```json
{
  "indicator_key": "Nilai SAKIP OPD",
  "occurrences": [
    { "document_type": "iku",     "value": "80", "unit": "poin", "year": "2026", "source_ref": "src_001" },
    { "document_type": "renstra", "value": "78", "unit": "poin", "year": "2026", "source_ref": "src_002" },
    { "document_type": "pk",      "value": "75", "unit": "poin", "year": "2026", "source_ref": "src_003" },
    { "document_type": "lkjip",   "value": "77", "unit": "poin", "year": "2025", "source_ref": "src_004" }
  ],
  "coherence_status": "conflict",
  "conflict_details": "Target berbeda: IKU=80, Renstra=78, PK=75",
  "rule_violated": ["IND-006", "PK-003"]
}
```

Implementation notes:

1. Skill ini tidak memanggil AI untuk mendeteksi konflik angka — sepenuhnya deterministic comparison.
2. AI dipanggil hanya untuk menghasilkan narasi rekomendasi dari konflik yang terdeteksi.
3. Threshold perbedaan yang dianggap konflik: berbeda nilai numerik, bukan hanya format.
4. Ambiguitas nama indikator (singkatan vs nama penuh) ditangani dengan fuzzy matching.
5. Jika indikator hanya ada di satu dokumen, kembalikan `coherence_status: insufficient_data`.

---

## 7. Cross-Skill Contracts

### 7.1 Common Skill Result

Semua skill sebaiknya mengembalikan struktur hasil umum:

```json
{
  "status": "success",
  "skill_id": "SKL-008",
  "summary": "",
  "data": {},
  "source_refs": [],
  "confidence": "medium",
  "warnings": [],
  "errors": [],
  "needs_human_validation": false
}
```

Status yang diperbolehkan:

1. `success`
2. `partial_success`
3. `failed`
4. `blocked`
5. `skipped`

### 7.2 Confidence Standard

| Confidence | Meaning |
| --- | --- |
| `high` | Sumber langsung tersedia dan konsisten |
| `medium` | Sumber tersedia tetapi memerlukan interpretasi |
| `low` | Sumber parsial, dokumen kurang, atau butuh validasi manual |

Rule:

1. `low` wajib menghasilkan `needs_human_validation=true`.
2. Temuan tanpa sumber tidak boleh diberi confidence `high`.

### 7.3 Severity Standard

| Severity | Meaning |
| --- | --- |
| `critical` | Kontradiksi target utama, klaim tanpa bukti, atau data sensitif bocor |
| `high` | Indikator tidak outcome, PK tidak konsisten, evidence inti tidak ada |
| `medium` | Definisi, formula, sumber data, atau analisis kurang lengkap |
| `low` | Format, penamaan, atau catatan minor |

### 7.4 Skill Interaction Rules

Skill yang saling bergantung mengikuti urutan berikut:

```text
SKL-022 (routing) → SKL-006 (retrieval) → SKL-014 (privacy)
  → SKL-008/009/010/011/012 (domain review)
    → SKL-026 (cross-doc coherence) [otomatis]
      → SKL-015 (AI contract validation)
        → SKL-017 (report)
          → SKL-023 (next-step recommendations)
```

---

## 8. Skill Versioning Strategy

| Version | Skill Scope |
| --- | --- |
| v1.0 Core | SKL-001–007, SKL-014–017, SKL-019–020 (workspace, doctor, reading, classification, source refs, retrieval, ask, privacy, AI validation, token, reports, model/credential mgmt) |
| v0.2 Should Have | SKL-018 (lite task decomposition) |
| v1.0 Expanded | SKL-008–013, SKL-021–026 (semua domain review, desk eval, CLI router, next-step, rencana aksi, LHE tracking, cross-doc coherence) |
| Post-v1.0 | SKL-018 advanced (full orchestration), workbench, graph visualization, richer automation |

Release rule:

1. v0.2 tidak boleh membuka skill Expanded sebagai fitur stabil sebelum source refs, privacy, golden tests, dan report dasar lulus.
2. Skill Post-v1.0 boleh memiliki modul skeleton, tetapi command publik harus diberi status experimental sampai release gate terkait lulus.
3. Setiap skill baru harus memiliki test minimal dan failure mode sebelum dianggap release-ready.

---

## 9. Requirement-to-Skill Traceability

| Product Requirement | Skill |
| --- | --- |
| Membaca folder dokumen OPD | `SKL-003`, `SKL-004` |
| Mengenali jenis dokumen SAKIP | `SKL-004` |
| Quick health signal setelah scan | `SKL-004` |
| Mengindeks dokumen lokal | `SKL-003`, `SKL-005`, `SKL-006` |
| Routing input REPL | `SKL-022` |
| Tanya jawab berbasis dokumen | `SKL-006`, `SKL-007` |
| Review indikator | `SKL-008`, `SKL-026` |
| Review PK | `SKL-009`, `SKL-026` |
| Review LKjIP | `SKL-010`, `SKL-026` |
| Review Rencana Aksi | `SKL-024` |
| Review cascading dan pohon kinerja | `SKL-011` |
| Audit evidence | `SKL-012` |
| Tracking tindak lanjut LHE | `SKL-025` |
| Cross-document coherence check | `SKL-026` |
| Draft rekomendasi | `SKL-013` |
| Source reference wajib | `SKL-005`, `SKL-015` |
| Privacy mode | `SKL-014` |
| Token tracking | `SKL-016` |
| Laporan Markdown/XLSX/DOCX | `SKL-017` |
| Rekomendasi langkah berikutnya | `SKL-023` |
| Task panjang bertahap | `SKL-018` |

---

## 10. Testing Matrix

| Skill | Unit Test | Integration Test | Golden Fixture | Mock AI Required |
| --- | ---: | ---: | ---: | ---: |
| `SKL-001` | Yes | Yes | No | No |
| `SKL-002` | Yes | Yes | No | No |
| `SKL-003` | Yes | Yes | Yes | No |
| `SKL-004` | Yes | Yes | Yes | No |
| `SKL-005` | Yes | Yes | Yes | No |
| `SKL-006` | Yes | Yes | Yes | No |
| `SKL-007` | Yes | Yes | Yes | Yes |
| `SKL-008` | Yes | Yes | Yes | Yes |
| `SKL-009` | Yes | Yes | Yes | Yes |
| `SKL-010` | Yes | Yes | Yes | Yes |
| `SKL-011` | Yes | Yes | Yes | Optional |
| `SKL-012` | Yes | Yes | Yes | Yes |
| `SKL-013` | Yes | Yes | Yes | Yes |
| `SKL-014` | Yes | Yes | Yes | No |
| `SKL-015` | Yes | Yes | Yes | Yes |
| `SKL-016` | Yes | Yes | No | No |
| `SKL-017` | Yes | Yes | Yes | No |
| `SKL-018` | Yes | Yes | Yes | Yes |
| `SKL-019` | Yes | No | No | No |
| `SKL-020` | Yes | No | No | No |
| `SKL-021` | Yes | Yes | Yes | Yes |
| `SKL-022` | Yes | Yes | Yes | No |
| `SKL-023` | Yes | Yes | Yes | No |
| `SKL-024` | Yes | Yes | Yes | Yes |
| `SKL-025` | Yes | Yes | Yes | Optional |
| `SKL-026` | Yes | Yes | Yes | Optional |

---

## 11. Implementation Priority

Recommended order:

1. `SKL-001` Workspace Initialization Skill
2. `SKL-002` Runtime Doctor Skill
3. `SKL-003` Document Reading Skill
4. `SKL-004` Document Classification Skill (include health signals)
5. `SKL-005` Source Reference Skill
6. `SKL-006` Retrieval and Context Skill (include query_type routing)
7. `SKL-014` Privacy Guardrail Skill
8. `SKL-015` AI Contract Validation Skill
9. `SKL-016` Token and Cost Control Skill
10. `SKL-022` CLI Intent & Command Router Skill
11. `SKL-007` Ask and Copilot Skill (Q&A only, bukan routing)
12. `SKL-008` Indicator Review Skill (IND-001–009)
13. `SKL-009` PK Consistency Review Skill (PK-001–006)
14. `SKL-026` Cross-Document Coherence Skill (dipakai oleh SKL-008 dan SKL-009)
15. `SKL-023` Contextual Next-Step Recommendation Skill
16. `SKL-017` Report Generation Skill
17. `SKL-018` Task Decomposition Skill (lite)
18. `SKL-010` LKjIP Review Skill (LKJ-001–007)
19. `SKL-011` SAKIP Mapping and Cascading Skill (CAS-001–003)
20. `SKL-012` Evidence Audit Skill (EVD-001–004)
21. `SKL-024` Rencana Aksi & Monitoring Skill
22. `SKL-025` LHE Tindak Lanjut Tracking Skill
23. `SKL-013` Recommendation Drafting Skill
24. `SKL-021` Desk Evaluation Skill
25. `SKL-019`, `SKL-020` Model & Credential Management

---

## 12. Definition of Done for a Skill

Satu skill dianggap selesai jika:

1. Input dan output schema jelas.
2. Failure mode dan error code jelas.
3. Privacy behavior jelas.
4. Source reference behavior jelas.
5. Unit test tersedia.
6. Integration test tersedia bila skill dipanggil dari command.
7. Mock AI tersedia bila skill memakai AI.
8. Golden fixture tersedia untuk review skill.
9. Log aman dari secret dan PII.
10. Output tidak mengubah file asli.
11. Output tidak mengandung kode UI/rendering.
12. Dokumentasi command atau penggunaan tersedia.

---

## 13. Final Skill Position

SAKIPRO v1.0 skills blueprint mencakup 26 skill yang mencakup seluruh siklus kerja review SAKIP: dari inisialisasi workspace, pembacaan dokumen, routing input REPL, retrieval berbasis query-type, semua domain review (indikator, PK, LKjIP, rencana aksi, cascading, evidence, LHE), cross-document coherence sebagai lapisan kecerdasan lintas dokumen, rekomendasi langkah berikutnya yang otomatis, hingga laporan draft dan estimasi predikat.

Penambahan utama dari v0.2 ke v1.0 blueprint:

1. **SKL-022** memisahkan concern routing dari Q&A — REPL menjadi cerdas tanpa membebani SKL-007.
2. **SKL-023** menjadikan rekomendasi berikutnya sebagai fitur terstruktur, bukan afterthought.
3. **SKL-024 dan SKL-025** menutup dua gap dokumen yang selama ini tidak punya skill (Rencana Aksi dan LHE Tindak Lanjut).
4. **SKL-026** adalah lapisan kecerdasan terpenting: satu indikator, semua dokumen, satu gambar koherensi.
5. Rule baru (IND-008/009, PK-006, LKJ-006/007, CAS-003, EVD-004) memastikan coverage menyeluruh terhadap standar evaluasi Permenpan RB 88/2021.
