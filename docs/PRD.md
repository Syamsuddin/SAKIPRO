# PRD.md
# SAKIPRO v1.0
# AI CLI Agent untuk Kasubbag Perencanaan OPD

Version: 1.0  
Document Type: Product Requirements Document  
Target Reader: Vibe Coding AI Agent, Python Developer, AI Engineer  
Primary Mode: Python CLI  
UI Mode: Rich Interactive CLI  
AI Mode: API Key Model AI Berbasis Token  
Target Device: Laptop Kantor CPU-only  
Status: Implementation Ready  

---

## 1. Ringkasan Produk

SAKIPRO v1.0 adalah AI CLI Agent ringan untuk membantu Kasubbag Perencanaan OPD memperbaiki mutu dokumen SAKIP yang tersedia di folder kerja.

SAKIPRO membaca dokumen seperti Renstra, Renja, IKU, Perjanjian Kinerja, LKjIP, RKA, DPA, LHE, rencana aksi, dan evidence. Sistem kemudian membantu user melakukan review indikator, review cascading, review pohon kinerja, review PK, review LKjIP, audit evidence, drafting rekomendasi, serta pembuatan laporan perbaikan.

SAKIPRO dirancang untuk berjalan di laptop kantor tanpa GPU. AI dipanggil melalui API Key model berbasis token seperti OpenAI, Gemini, atau Claude melalui abstraction layer LiteLLM.

---

## 2. Visi Produk

Menjadikan SAKIPRO sebagai asisten kerja harian Kasubbag Perencanaan OPD yang mampu membaca folder dokumen SAKIP, menemukan kelemahan dokumen, memberi rekomendasi perbaikan, menyusun draft, dan menghasilkan laporan review dengan cepat.

SAKIPRO bukan platform besar multi-OPD. SAKIPRO adalah alat bantu kerja praktis untuk satu OPD.

---

## 3. Positioning

Nama produk:

SAKIPRO

Makna operasional:

SAKIP Planning Review Officer

Tagline:

Review, Improve, Draft, Evidence, Report

Positioning:

AI CLI Assistant for OPD SAKIP Planning Documents

---

## 4. Masalah yang Diselesaikan

Kasubbag Perencanaan OPD sering menghadapi masalah berikut:

1. Dokumen SAKIP tersebar dalam banyak file dan folder.
2. Indikator kinerja belum berorientasi outcome.
3. Formula indikator belum jelas.
4. Sumber data indikator tidak tertulis.
5. Target PK berbeda dengan IKU, Renstra, atau Renja.
6. Cascading sasaran, indikator, program, kegiatan, dan subkegiatan belum logis.
7. Pohon kinerja belum menggambarkan hubungan sebab akibat.
8. LKjIP banyak narasi tetapi kurang analisis.
9. LKjIP belum menjelaskan efisiensi anggaran.
10. Evidence belum terhubung dengan klaim kinerja.
11. Tindak lanjut LHE belum terdokumentasi baik.
12. User harus mengecek dokumen secara manual menjelang evaluasi.

SAKIPRO membantu mengurangi pekerjaan manual tersebut.

---

## 5. Sasaran Produk

### 5.1 Sasaran Bisnis

1. Membantu OPD meningkatkan kualitas dokumen SAKIP.
2. Mempercepat review dokumen oleh Kasubbag Perencanaan.
3. Mengurangi risiko kesalahan sebelum evaluasi.
4. Membantu penyusunan rekomendasi perbaikan.
5. Membantu OPD lebih siap menghadapi reviu internal dan evaluasi SAKIP.

### 5.2 Sasaran Produk

1. Membaca folder dokumen OPD.
2. Mengenali jenis dokumen SAKIP.
3. Mengekstrak indikator, sasaran, target, program, kegiatan, dan evidence.
4. Memberi hasil review indikator.
5. Memberi hasil review cascading.
6. Memberi hasil review PK.
7. Memberi hasil review LKjIP.
8. Memberi hasil audit evidence.
9. Membuat draft rekomendasi.
10. Membuat laporan Markdown, XLSX, dan DOCX.

### 5.3 Sasaran Teknis

1. Berbasis Python 3.11 atau 3.12.
2. Berjalan sebagai CLI.
3. Memakai Rich untuk tampilan terminal.
4. Memakai Typer untuk command.
5. Memakai prompt_toolkit untuk interactive mode dan autocomplete jika fitur Should Have ikut dirilis pada v0.2.
6. Memakai LiteLLM untuk AI provider.
7. Memakai SQLite untuk database lokal.
8. Memakai SQLite FTS/BM25 atau keyword retrieval sebagai retrieval default v0.2.
9. Ditiadakan (tidak menggunakan ChromaDB atau FAISS demi efisiensi).
10. Menjadikan NetworkX graph sebagai optional v0.2 untuk cascading dan pohon kinerja.
11. Tidak membutuhkan GPU lokal.

---

## 6. Non Goals

SAKIPRO v1.0 tidak membangun:

1. Web dashboard.
2. Multi-user login.
3. Sistem level kabupaten.
4. Integrasi langsung SIPD.
5. Integrasi langsung e-SAKIP.
6. Integrasi langsung SIMPEG.
7. Tanda tangan elektronik.
8. Database server terpusat.
9. Local LLM GPU.
10. Mobile app.

Fitur tersebut dapat menjadi pengembangan versi berikutnya.

---

## 7. Target User

### 7.1 Primary User

1. Kasubbag Perencanaan OPD.
2. Staf perencanaan OPD.
3. Operator SAKIP OPD.
4. Tim penyusun LKjIP OPD.

### 7.2 Secondary User

1. Sekretaris OPD.
2. Kepala OPD.
3. Bagian Organisasi.
4. Bappeda.
5. Inspektorat pembina.
6. Konsultan pendamping SAKIP.

---

## 8. Persona

### 8.1 Kasubbag Perencanaan OPD

Kebutuhan:

1. Cepat mengetahui kelemahan dokumen OPD.
2. Mengecek konsistensi indikator dan target.
3. Menyiapkan bahan review PK.
4. Menyiapkan bahan review LKjIP.
5. Menyiapkan laporan perbaikan.

Pain point:

1. Banyak file harus dibaca.
2. Waktu terbatas.
3. Format dokumen tidak seragam.
4. Sulit menulis analisis LKjIP yang tajam.

### 8.2 Staf Perencanaan OPD

Kebutuhan:

1. Menyiapkan dokumen.
2. Menjalankan scan folder.
3. Mengekspor laporan.
4. Mengisi evidence yang kurang.

Pain point:

1. Tidak hafal semua aturan SAKIP.
2. Tidak terbiasa command line.
3. Butuh wizard dan help yang mudah.

### 8.3 Inspektorat Pembina

Kebutuhan:

1. Melihat ringkasan kelemahan OPD.
2. Mengecek evidence.
3. Menyiapkan catatan reviu.
4. Membantu OPD memperbaiki dokumen.

Pain point:

1. Dokumen OPD tidak konsisten.
2. Evidence sulit dilacak.
3. Butuh laporan cepat.

---

## 9. Prinsip Desain Produk

SAKIPRO harus mengikuti prinsip berikut:

1. Tidak mengubah file asli.
2. Semua hasil dibuat sebagai file baru.
3. Semua output berstatus draft.
4. Semua rekomendasi harus berbasis dokumen.
5. Semua klaim harus memiliki sumber.
6. Semua hasil AI harus memiliki confidence score.
7. Semua operasi mahal harus meminta konfirmasi.
8. API Key tidak boleh muncul di log.
9. User biasa harus dapat memakai wizard tanpa menghafal command.
10. CLI harus informatif, sugestif, dan aman.

Dokumen pengendali tambahan:

1. `SCOPE.md` untuk batas v1.0 Core, v1.0 Expanded, dan Post-v1.0.
2. `SAKIP_RULEBOOK.md` untuk rubrik review yang dapat diuji.
3. `AI_CONTRACT.md` untuk schema input/output AI dan citation.
4. `PRIVACY.md` untuk privacy pipeline dan data masking.
5. `ERROR_HANDLING.md` untuk error code dan partial success.
6. `TEST_PLAN.md` untuk golden dataset dan coverage gate.
7. `PACKAGING.md` dan `RELEASE_CHECKLIST.md` untuk distribusi.

---

## 10. Mode Operasi

Mode operasi di bawah adalah desain produk lintas versi. Untuk v1.0 Core, mode wajib adalah Quick Command Mode. Interactive Agent Mode dan Wizard Mode berstatus Should Have. Workbench Mode dan Task Mode masuk Post-v1.0.

### 10.1 Quick Command Mode

Untuk user yang tahu command.

Contoh:

```bash
sakipro scan ./Dokumen_SAKIP_OPD
sakipro cek-indikator
sakipro review-pk
```

### 10.2 Interactive Agent Mode

Masuk dengan:

```bash
sakipro chat
```

User dapat bertanya dalam bahasa natural.

Contoh:

```text
Apa kelemahan indikator OPD saya?
Review PK tahun 2026.
Apa indikator yang belum punya sumber data?
```

### 10.3 Wizard Mode

Masuk dengan:

```bash
sakipro wizard
```

Cocok untuk user biasa.

Menu:

1. Baca folder dokumen SAKIP OPD.
2. Cek mutu indikator.
3. Review PK.
4. Tanya SAKIPRO.
5. Keluar.

Menu review LKjIP, cascading, evidence, dan laporan akhir termasuk scope v1.0 Expanded.

### 10.4 Workbench Mode

Masuk dengan:

```bash
sakipro workbench
```

Menampilkan panel terminal Rich berisi status dokumen, indikator, PK, LKjIP, evidence, task, dan output.

### 10.5 Task Mode

Masuk dengan:

```bash
sakipro task "Review seluruh dokumen SAKIP OPD dan buat daftar perbaikan"
```

SAKIPRO memecah tugas panjang menjadi subtask.

---

## 11. Command Utama

### 11.1 Command v1.0 Core

Command wajib v0.2:

```bash
sakipro init
sakipro doctor
sakipro scan
sakipro status
sakipro ask
sakipro cek-indikator
sakipro review-pk
sakipro token
sakipro usage          # alias untuk sakipro token
sakipro privacy
```

Command v1.0 Core Should Have:

```bash
sakipro chat
sakipro wizard
```

### 11.2 Command v1.0 Expanded

Command tambahan scope v0.2:

```bash
sakipro workbench
sakipro cek-pohon
sakipro review-lkjip
sakipro cek-cascading
sakipro cek-evidence
sakipro draft
sakipro task
sakipro report final
sakipro resume
sakipro config
sakipro model
sakipro output
```

---

## 12. Slash Command

Slash command tersedia pada interactive mode dan workbench mode. Untuk v0.2, slash command hanya wajib jika chat mode Should Have ikut dirilis.

Daftar slash command:

Daftar lengkap berikut adalah target v1.0 Expanded dan Post-v1.0. Untuk v0.2, slash command hanya wajib jika chat mode Should Have ikut dirilis.

```text
/help
/status
/scan
/cek-indikator
/cek-cascading
/cek-pohon
/review-pk
/review-lkjip
/cek-evidence
/draft
/task
/report
/token
/model
/privacy
/output
/clear
/exit
```

### 12.1 Perilaku Slash Command

Jika user mengetik:

```text
/cek
```

Sistem menampilkan suggestion:

```text
/cek-indikator
/cek-cascading
/cek-pohon
/cek-evidence
```

---

## 13. Autocomplete

SAKIPRO harus menyediakan tiga jenis autocomplete.

Untuk v1.0 Core, autocomplete tidak wajib. Basic command autocomplete berstatus Should Have, sedangkan context autocomplete masuk setelah scan dan retrieval stabil.

### 13.1 Shell Autocomplete

Contoh:

```bash
sakipro rev<TAB>
```

Menampilkan:

```text
review-pk
```

### 13.2 Slash Autocomplete

Dalam mode chat:

```text
/rev<TAB>
```

Menampilkan:

```text
/review-pk
```

### 13.3 Context Autocomplete

Berbasis isi dokumen.

Contoh:

```text
cek indikator <TAB>
```

Menampilkan indikator yang ditemukan dalam dokumen OPD.

---

## 14. AI Agent

SAKIPRO v1.0 memakai 7 agent utama. Agent wajib Core adalah Folder Scanner Agent, Indicator Review Agent, PK Review Agent, dan OPD Planning Copilot Agent. Agent LKjIP, cascading, dan evidence masuk scope v1.0 Expanded.

### 14.1 Folder Scanner Agent

Tugas:

1. Membaca folder kerja.
2. Mengenali tipe file.
3. Mengklasifikasi dokumen.
4. Menandai dokumen yang belum ada.
5. Membuat ringkasan dokumen.

### 14.2 Indicator Review Agent

Tugas:

1. Mengekstrak indikator.
2. Menentukan jenis indikator.
3. Mengecek formula.
4. Mengecek sumber data.
5. Mengecek baseline.
6. Mengecek target.
7. Memberi rekomendasi perbaikan.

Kategori indikator:

1. Input.
2. Aktivitas.
3. Output.
4. Outcome.
5. Impact.
6. Tidak jelas.

### 14.3 Cascading Review Agent

Status: v1.0 Expanded.

Tugas:

1. Mengekstrak sasaran.
2. Mengekstrak indikator.
3. Mengekstrak program.
4. Mengekstrak kegiatan.
5. Mengekstrak subkegiatan.
6. Membangun relasi.
7. Mendeteksi rantai putus.

### 14.4 PK Review Agent

Tugas:

1. Membaca Perjanjian Kinerja.
2. Membandingkan PK dengan IKU.
3. Membandingkan PK dengan Renstra.
4. Mengecek target.
5. Mengecek satuan.
6. Mengecek dukungan program.

### 14.5 LKjIP Review Agent

Status: v1.0 Expanded.

Tugas:

1. Membaca LKjIP.
2. Mengecek kesesuaian dengan PK.
3. Mengecek target dan realisasi.
4. Mengecek analisis keberhasilan.
5. Mengecek analisis kegagalan.
6. Mengecek analisis efisiensi.
7. Mengecek tindak lanjut.

### 14.6 Evidence Review Agent

Status: v1.0 Expanded.

Tugas:

1. Membaca folder evidence.
2. Mengidentifikasi bukti pendukung.
3. Menghubungkan klaim dengan evidence.
4. Menilai kekuatan evidence.
5. Menyusun daftar evidence kurang.

### 14.7 OPD Planning Copilot Agent

Tugas:

1. Menjawab pertanyaan user.
2. Memberi saran langkah berikutnya.
3. Membantu membuat draft.
4. Menjelaskan hasil review.
5. Menjalankan task sederhana.

---

## 15. Dokumen yang Didukung

SAKIPRO harus dapat membaca:

1. DOCX.
2. PDF.
3. XLSX.
4. CSV.
5. TXT.
6. Markdown.

Jenis dokumen yang dikenali:

1. Renstra.
2. Renja.
3. IKU.
4. Perjanjian Kinerja.
5. LKjIP.
6. RKA.
7. DPA.
8. LHE.
9. Rencana Aksi.
10. Matriks Tindak Lanjut.
11. Evidence.
12. Dokumen lain.

---

## 16. User Journey

Scope journey mengikuti `SCOPE.md`. Journey 1 sampai 4 adalah target v1.0 Core. Journey 5 sampai 8 tetap menjadi desain produk, tetapi delivery utamanya masuk scope v0.2 setelah retrieval, source reference, privacy, dan golden test stabil.

### 16.1 Journey 1, Setup Awal

User menjalankan:

```bash
sakipro init
```

Sistem membuat folder:

```text
.sakipro/
  config.yaml
  .env
  logs/
  cache/
  memory/
  outputs/
  history
```

Acceptance criteria:

1. Folder dibuat.
2. Config dibuat.
3. File .env.example tersedia.
4. User diberi instruksi API Key.
5. Command doctor dapat dijalankan.

### 16.2 Journey 2, Scan Folder

User menjalankan:

```bash
sakipro scan ./Dokumen_SAKIP_OPD
```

Sistem:

1. Membaca file.
2. Mengklasifikasi dokumen.
3. Menyimpan metadata.
4. Menampilkan ringkasan.

Acceptance criteria:

1. Dokumen terdaftar.
2. Dokumen gagal dibaca masuk log.
3. Ringkasan tampil.
4. Output ringkasan dibuat.

### 16.3 Journey 3, Cek Indikator

User menjalankan:

```bash
sakipro cek-indikator
```

Sistem:

1. Mengambil indikator dari dokumen.
2. Mengklasifikasi indikator.
3. Mengecek formula.
4. Mengecek sumber data.
5. Memberi rekomendasi.

Acceptance criteria:

1. Tabel indikator tampil.
2. File XLSX dibuat.
3. File Markdown dibuat.
4. Setiap indikator punya status.

### 16.4 Journey 4, Review PK

User menjalankan:

```bash
sakipro review-pk
```

Sistem:

1. Membaca PK.
2. Membandingkan dengan IKU.
3. Membandingkan dengan Renstra.
4. Mendeteksi target tidak konsisten.

Acceptance criteria:

1. Temuan PK tampil.
2. Rekomendasi tampil.
3. File report dibuat.
4. Sumber dokumen dicantumkan.

### 16.5 Journey 5, Review LKjIP

User menjalankan:

```bash
sakipro review-lkjip
```

Sistem:

1. Membaca LKjIP.
2. Mengecek kesesuaian dengan PK.
3. Mengecek analisis.
4. Mengecek efisiensi.
5. Mengecek tindak lanjut.

Acceptance criteria:

1. Kelemahan LKjIP tampil.
2. Analisis kualitas tersedia.
3. File report dibuat.
4. Saran perbaikan tersedia.

### 16.6 Journey 6, Cek Cascading

User menjalankan:

```bash
sakipro cek-cascading
```

Sistem:

1. Membangun relasi sasaran, indikator, program, kegiatan.
2. Mendeteksi rantai putus.
3. Memberi rekomendasi perbaikan.

Acceptance criteria:

1. Relasi tampil.
2. Rantai putus tampil.
3. Output Markdown dibuat.
4. Graph JSON dibuat jika memungkinkan.

### 16.7 Journey 7, Cek Evidence

User menjalankan:

```bash
sakipro cek-evidence
```

Sistem:

1. Membaca klaim kinerja.
2. Mencari evidence.
3. Menilai evidence.
4. Menemukan evidence gap.

Acceptance criteria:

1. Evidence valid tampil.
2. Evidence kurang tampil.
3. File XLSX dibuat.
4. Saran bukti tambahan tersedia.

### 16.8 Journey 8, Laporan Final

User menjalankan:

```bash
sakipro report final
```

Sistem membuat:

1. Ringkasan review dokumen.
2. Review indikator.
3. Review PK.
4. Review LKjIP.
5. Review cascading.
6. Audit evidence.
7. Daftar rekomendasi.
8. Daftar task perbaikan.

Acceptance criteria:

1. File DOCX dibuat.
2. File Markdown dibuat.
3. File XLSX pendukung dibuat.
4. Status laporan draft ditampilkan.

---

## 17. Functional Requirements

### FR-001 Init Workspace

Sistem harus menyediakan command:

```bash
sakipro init
```

Fungsi:

1. Membuat folder konfigurasi.
2. Membuat config.yaml.
3. Membuat .env.example.
4. Membuat folder outputs.
5. Membuat folder logs.

Priority: Must Have

### FR-002 Doctor Check

Sistem harus menyediakan:

```bash
sakipro doctor
```

Cek:

1. Python runtime.
2. File config.
3. API Key.
4. Folder output.
5. Permission folder.
6. Library utama.
7. Internet connection.

Priority: Must Have

### FR-003 Scan Folder

Sistem harus membaca folder dokumen OPD.

Priority: Must Have

### FR-004 Document Classification

Sistem harus mengenali jenis dokumen SAKIP.

Priority: Must Have

### FR-005 Document Text Extraction

Sistem harus mengekstrak teks dan tabel dari DOCX, PDF, XLSX, CSV, TXT, dan Markdown.

Priority: Must Have

### FR-006 Local Index

Sistem harus menyimpan metadata dokumen ke SQLite.

Priority: Must Have

### FR-007 Basic Retrieval

Sistem harus menyediakan retrieval dokumen berbasis SQLite FTS/BM25 atau keyword search untuk tanya jawab dan review berbasis sumber.

Priority: Must Have

### FR-007B Vector Memory (Ditiadakan)

Sistem secara eksklusif menggunakan pencarian berbasis indeks teks penuh **SQLite FTS5 (BM25)** dan deteksi kata kunci deterministik. Vector memory ditiadakan sepenuhnya demi menjamin RAM tetap 0% overhead tambahan pada laptop kantor.

Priority: Ditiadakan

### FR-008 Ask Document

Sistem harus menyediakan tanya jawab berbasis dokumen.

Priority: Must Have

### FR-009 Indicator Review

Sistem harus mereview indikator OPD.

Priority: Must Have

### FR-010 PK Review

Sistem harus mereview Perjanjian Kinerja.

Priority: Must Have

### FR-011 LKjIP Review

Sistem harus mereview LKjIP.

Priority: v1.0 Expanded

### FR-012 Cascading Review

Sistem harus mereview cascading.

Priority: v1.0 Expanded

### FR-013 Performance Tree Review

Sistem harus menampilkan pohon kinerja.

Priority: v1.0 Expanded

### FR-014 Evidence Audit

Sistem harus mengaudit evidence.

Priority: v1.0 Expanded

### FR-015 Draft Generator

Sistem harus membuat draft rekomendasi.

Priority: v1.0 Expanded

### FR-016 Final Report

Sistem harus membuat laporan final review OPD.

Priority: v1.0 Expanded

### FR-017 Token & Usage Report

Sistem harus mencatat pemakaian token (input, output, total) dan estimasi biaya per pemanggilan AI, serta menyediakan laporan ringkasan lewat CLI dengan perintah `sakipro usage` (alias `sakipro token`).

Priority: Must Have

### FR-017B Multi-Model Management

Sistem harus memungkinkan user untuk:
1. Melihat daftar model yang didukung (OpenAI, Anthropic, Gemini, Grok, DeepSeek).
2. Mengganti model aktif lewat CLI (`sakipro model switch`).
3. Memilih model yang berbeda untuk tier yang berbeda (Light vs Default vs Reasoning).

Priority: Should Have

### FR-017C Interactive API Key Input

Sistem harus menyediakan perintah CLI (`sakipro config set-key`) untuk menginput dan menyimpan API Key ke dalam file `.env` secara interaktif tanpa mengharuskan user mengedit file secara manual.

Priority: Should Have

### FR-018 Interactive Chat

Sistem harus menyediakan mode chat.

Priority: Should Have

### FR-019 Wizard Mode

Sistem harus menyediakan wizard.

Priority: Should Have

### FR-020 Slash Command

Sistem harus mendukung slash command inti.

Priority: Should Have

### FR-021 Autocomplete

Sistem harus mendukung autocomplete command.

Priority: Should Have

### FR-021B Slash Command Autohints

Dalam mode interaktif (`chat` atau `wizard`), sistem harus menampilkan **Autohint** (teks bayangan atau daftar saran real-time) saat user mengetik karakter slash (`/`) atau teks perintah yang belum lengkap, guna membantu user menemukan perintah yang relevan secara instan.

Priority: Must Have (for Interactive Mode)

### FR-022 Smart Suggestion

Sistem harus memberi saran langkah berikutnya.

Priority: Must Have

### FR-023 Privacy Mode

Sistem harus mendukung privacy mode.

Priority: Must Have

### FR-024 Safe Output

Sistem tidak boleh mengubah file asli.

Priority: Must Have

### FR-025 Plan Mode & Execution Strategy

Sistem harus mampu memberikan rencana kerja (Plan) sebelum melakukan eksekusi audit yang berat. Plan mencakup urutan langkah, dokumen yang akan diproses, dan estimasi biaya token.

Priority: Must Have

### FR-026 Sub-Agent Orchestration

Sistem harus menggunakan arsitektur agen spesialis (Sub-agents) untuk menangani tugas audit yang berbeda, guna meningkatkan akurasi dan meminimalkan interferensi prompt.

Priority: Must Have

### FR-027 Workspace Memory Persistence

Sistem harus mampu menyimpan konteks spesifik organisasi (Profil OPD, preferensi audit) ke dalam file memori lokal (`MEMORY.md`) untuk digunakan kembali pada sesi berikutnya.

Priority: Must Have

### FR-028 SAKIP Predicate Simulation & Scoring

Sistem harus mampu mensimulasikan perhitungan nilai SAKIP berdasarkan 4 komponen (Perencanaan, Pengukuran, Pelaporan, Evaluasi Internal) dan memberikan estimasi predikat (AA, A, BB, B, CC, C, D) berdasarkan temuan audit.

Priority: v1.0 Expanded

### FR-029 Follow-up Audit (LHE Tracking)

Sistem harus mampu menganalisis Matriks Tindak Lanjut dan dokumen LHE tahun sebelumnya untuk memastikan rekomendasi evaluator telah diimplementasikan dalam dokumen tahun berjalan.

Priority: v1.0 Expanded

---

## 18. Non Functional Requirements

### NFR-001 Performance

1. Scan 100 file ukuran sedang selesai kurang dari 20 menit.
2. Command status selesai kurang dari 5 detik.
3. Review indikator satu OPD selesai kurang dari 10 menit, tergantung API.
4. UI terminal tetap responsif.

### NFR-002 Laptop Friendly

1. Minimal RAM 8 GB.
2. Tidak membutuhkan GPU.
3. Dapat berjalan di Windows, macOS, dan Linux.
4. Dapat berjalan dari executable GitHub Release.

### NFR-003 Reliability

1. Jika satu file gagal dibaca, file lain tetap diproses.
2. Error dicatat di logs.
3. Output parsial tetap disimpan.
4. API retry tersedia.

### NFR-004 Security

1. API Key tidak dicetak.
2. .env tidak masuk log.
3. File asli tidak ditimpa.
4. Data sensitif dapat dimasking.
5. Privacy mode default adalah standard.

### NFR-005 Maintainability

1. Struktur kode modular.
2. Prompt dipisahkan dari kode.
3. Agent dipisahkan per file.
4. UI helper dipisahkan.
5. Test minimal tersedia.

### NFR-006 Usability

1. User biasa dapat memakai wizard.
2. Command punya help.
3. Error memberi solusi.
4. Saran langkah berikutnya selalu muncul.
5. Output terminal rapi memakai Rich.

---

## 19. AI Requirements

### 19.1 AI Provider

Sistem memakai LiteLLM agar mendukung:

1. OpenAI.
2. Gemini.
3. Claude.

### 19.2 Model Routing

Model ringan:

1. Klasifikasi dokumen.
2. Ringkasan.
3. Metadata.

Model standar:

1. Review indikator.
2. Review PK.
3. Review LKjIP.
4. Review evidence.

Model reasoning:

1. Review menyeluruh.
2. Task panjang.
3. Rekomendasi strategis.

### 19.3 Output AI

Output AI harus berbentuk struktur berikut:

```json
{
  "status": "success",
  "summary": "",
  "findings": [],
  "recommendations": [],
  "sources": [],
  "confidence": "medium",
  "needs_human_validation": true
}
```

### 19.4 Guardrail AI

AI tidak boleh:

1. Mengarang angka.
2. Mengklaim evidence ada jika tidak ada.
3. Mengubah dokumen asli.
4. Menetapkan output final tanpa user.
5. Mengabaikan privacy mode.
6. Menghapus file.

---

## 20. CLI UX Requirements

### 20.1 Startup Banner

SAKIPRO menampilkan banner:

```text
╔════════════════════════════════════════════════════════════╗
║                                                            ║
║   ███████╗ █████╗ ██╗  ██╗██╗██████╗ ██████╗  ██████╗    ║
║   ██╔════╝██╔══██╗██║ ██╔╝██║██╔══██╗██╔══██╗██╔═══██╗   ║
║   ███████╗███████║█████╔╝ ██║██████╔╝██████╔╝██║   ██║   ║
║   ╚════██║██╔══██║██╔═██╗ ██║██╔═══╝ ██╔══██╗██║   ██║   ║
║   ███████║██║  ██║██║  ██╗██║██║     ██║  ██║╚██████╔╝   ║
║   ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝╚═╝     ╚═╝  ╚═╝ ╚═════╝    ║
║                                                            ║
║        AI CLI Assistant for OPD SAKIP Planning             ║
║        Review • Improve • Draft • Evidence • Report        ║
║                                                            ║
╚════════════════════════════════════════════════════════════╝
```

### 20.2 Status Panel

Contoh:

```text
Project       : DISDIK_2026
Folder        : ./dokumen_sakip
AI Provider   : OpenAI
Privacy Mode  : standard
Documents     : 9 indexed
Evidence      : 32 files
Status        : Ready
```

### 20.3 Rich Components

Gunakan:

1. Panel.
2. Table.
3. Tree.
4. Progress.
5. Prompt.
6. Confirm.
7. Markdown.
8. Syntax.
9. Live.

### 20.4 Error UX

Error harus menjelaskan:

1. Apa yang gagal.
2. Penyebab.
3. Solusi.
4. File terkait jika ada.

---

## 21. Data Model

Model data v0.2 harus mendukung traceability dari output review kembali ke dokumen sumber.

### 21.0 workspaces

Kolom:

1. id.
2. name.
3. root_path.
4. privacy_mode.
5. created_at.
6. updated_at.

### 21.1 documents

Kolom:

1. id.
2. workspace_id.
3. file_path.
4. file_name.
5. file_hash.
6. document_type.
7. year.
8. opd.
9. sensitivity_level.
10. status.
11. read_error_code.
12. created_at.
13. updated_at.

### 21.1B document_versions

Kolom:

1. id.
2. document_id.
3. file_hash.
4. file_size.
5. modified_at.
6. indexed_at.
7. extraction_status.

### 21.2 document_chunks

Kolom:

1. id.
2. document_id.
3. document_version_id.
4. chunk_index.
5. chunk_text.
6. masked_text.
7. page.
8. sheet.
9. cell_range.
10. paragraph_index.
11. metadata_json.
12. created_at.

### 21.2B source_refs

Kolom:

1. id.
2. document_id.
3. chunk_id.
4. file_path.
5. document_type.
6. page.
7. sheet.
8. cell_range.
9. paragraph_index.
10. quote.
11. extraction_method.
12. confidence.

### 21.3 indicators

Kolom:

1. id.
2. name.
3. definition.
4. formula.
5. unit.
6. source_data.
7. target.
8. year.
9. category.
10. quality_status.
11. recommendation.
12. source_ref_id.

### 21.4 evidence_files

Kolom:

1. id.
2. workspace_id.
3. file_path.
4. file_hash.
5. evidence_type.
6. related_indicator.
7. related_claim.
8. status.
9. confidence.
10. source_ref_id.

### 21.5 reviews

Kolom:

1. id.
2. workspace_id.
3. review_type.
4. command.
5. summary.
6. findings_json.
7. recommendations_json.
8. sources_json.
9. confidence.
10. draft.
11. created_at.

### 21.5B review_findings

Kolom:

1. id.
2. review_id.
3. rule_id.
4. severity.
5. title.
6. description.
7. impact.
8. recommendation.
9. confidence.
10. needs_human_validation.

### 21.5C review_sources

Kolom:

1. id.
2. review_id.
3. finding_id.
4. source_ref_id.

### 21.6 tasks

Kolom:

1. id.
2. title.
3. description.
4. status.
5. priority.
6. created_at.
7. updated_at.

### 21.7 token_usage

Kolom:

1. id.
2. provider.
3. model.
4. input_tokens.
5. output_tokens.
6. total_tokens.
7. estimated_cost.
8. command.
9. created_at.

### 21.8 run_history

Kolom:

1. id.
2. workspace_id.
3. command.
4. status.
5. started_at.
6. finished_at.
7. error_code.
8. output_paths_json.

---

## 22. Folder Runtime

Folder user:

```text
~/.sakipro/
  config.yaml
  .env
  logs/
  cache/
  memory/
  outputs/
  history
  sakipro.db
```

Folder kerja OPD:

```text
Dokumen_SAKIP_OPD/
  Renstra_OPD.docx
  Renja_2026.xlsx
  IKU_OPD.docx
  PK_2026.docx
  LKjIP_2025.docx
  RKA_2026.xlsx
  DPA_2026.xlsx
  LHE_2025.pdf
  Evidence/
```

Folder output:

```text
outputs/
  01_RINGKASAN_DOKUMEN_OPD.md
  02_REVIEW_INDIKATOR.xlsx
  03_REVIEW_CASCADING.md
  04_REVIEW_PK.md
  05_REVIEW_LKJIP.md
  06_AUDIT_EVIDENCE.xlsx
  07_REKOMENDASI_PERBAIKAN.docx
  08_DAFTAR_TASK_PERBAIKAN.md
```

---

## 23. Software Stack

Bahasa:

```text
Python 3.11 atau 3.12
```

CLI:

```text
Typer
Rich
Questionary
prompt_toolkit
```

AI:

```text
LiteLLM
OpenAI API
Gemini API
Claude API
```

Dokumen:

```text
python-docx
docxtpl
PyMuPDF
pdfplumber
openpyxl
pandas
```

Database:

```text
SQLite
SQLAlchemy
```

Retrieval v0.2:

```text
SQLite FTS/BM25 atau keyword retrieval
```

Vector memory (Ditiadakan):

```text
Ditiadakan
```

Graph:

```text
NetworkX
```

Testing:

```text
pytest
ruff
```

Packaging:

```text
PyInstaller
GitHub Actions
pipx
uv
```

---

## 24. Hardware Requirement

### 24.1 Minimum

```text
CPU: 4 core
RAM: 8 GB
Storage: SSD 256 GB
Internet: wajib
GPU: tidak wajib
OS: Windows 10/11, macOS, atau Linux
```

### 24.2 Recommended

```text
CPU: 8 core
RAM: 16 GB
Storage: SSD 512 GB
Internet: stabil
GPU: tidak wajib
```

---

## 25. Distribution Requirement

SAKIPRO harus dapat dikemas sebagai:

1. GitHub Release executable Windows untuk v0.2 Should Have.
2. pipx install dari GitHub.
3. Source install untuk developer.
4. Artifact macOS dan Linux yang dipoles termasuk scope v1.0 Expanded.

### 25.1 GitHub Release

Windows:

```text
sakipro-windows-x64.zip
```

macOS:

```text
sakipro-macos-arm64.tar.gz, v0.2
sakipro-macos-x64.tar.gz, v0.2
```

Linux:

```text
sakipro-linux-x64.tar.gz, v0.2
```

Isi paket:

```text
sakipro.exe atau sakipro
config.example.yaml
.env.example
templates/
install.ps1
install.sh
README_INSTALL.md
```

### 25.2 pipx

```bash
pipx install git+https://github.com/NAMA-ORG/sakipro.git
```

### 25.3 Source

```bash
git clone https://github.com/NAMA-ORG/sakipro.git
cd sakipro
uv sync
uv run sakipro doctor
```

---

## 26. Output Requirements

### 26.1 Terminal Output

Harus memakai Rich:

1. Panel.
2. Table.
3. Progress bar.
4. Tree.
5. Markdown preview.
6. Error panel.
7. Success panel.
8. Suggested next steps.

### 26.2 File Output

Format:

1. Markdown.
2. XLSX.
3. DOCX.
4. JSON.
5. PDF opsional.

### 26.3 Naming Convention

```text
YYYYMMDD_HHMM_<jenis_laporan>_<opd>.<ext>
```

Contoh:

```text
20260527_2110_review_pk_disdik.md
```

---

## 27. Acceptance Criteria Global

SAKIPRO v1.0 dianggap selesai jika:

1. CLI dapat diinstal.
2. Command init berjalan.
3. Command doctor berjalan.
4. Command scan membaca folder.
5. DOCX terbaca.
6. PDF terbaca.
7. XLSX terbaca.
8. Review indikator berjalan.
9. Review PK berjalan.
10. Ask document berjalan dengan source refs.
11. Retrieval dasar berjalan menggunakan SQLite FTS5 eksklusif tanpa vector DB.
12. Command status menampilkan workspace, dokumen, output, dan privacy mode.
13. Rich UI tampil untuk panel, table, progress, success, dan error.
14. Command token berjalan dan token usage tercatat.
15. API Key aman.
16. Command privacy berjalan untuk mode standard dan strict.
17. File asli tidak berubah.
18. Output tersimpan di outputs.
19. Output AI berlabel draft.
20. Golden test dataset lulus.
21. Error code utama tercatat di logs.

---

## 28. v0.2 Scope

### 28.1 Must Have

1. init.
2. doctor.
3. scan.
4. status.
5. ask.
6. cek-indikator.
7. review-pk.
8. token command dan token usage log.
9. privacy command dan privacy mode.
10. SQLite document registry.
11. basic retrieval.
12. Markdown report.
13. XLSX report.
14. Rich panel, table, progress, error, success.
15. source refs dan confidence.
16. golden tests.

### 28.2 Should Have

1. chat.
2. wizard.
3. basic autocomplete.
4. output DOCX sederhana.
5. PyInstaller Windows one-folder.

### 28.3 v1.0 Expanded Must Have

1. review-lkjip.
2. cek-cascading.
3. cek-evidence.
4. report final.
5. draft rekomendasi.
6. final DOCX draft.
7. graph-ready data model.
8. slash command inti v0.2.

### 28.4 v0.2 Advanced Should Have

1. vector memory.
2. graph analysis.
3. packaging macOS dan Linux.
4. resume session.

---

## 29. Roadmap

### Sprint 1, CLI Foundation

Deliverables:

1. Typer CLI.
2. Rich UI helper.
3. Banner.
4. Config loader.
5. Logger.
6. init.
7. doctor.

### Sprint 2, Document Engine

Deliverables:

1. DOCX reader.
2. PDF reader.
3. XLSX reader.
4. Document classifier.
5. scan command.

### Sprint 3, Storage and Memory

Deliverables:

1. SQLite database.
2. SQLAlchemy models.
3. Chunk storage.
4. Source reference storage.
5. SQLite FTS/BM25 atau keyword retrieval.

### Sprint 4, AI Layer

Deliverables:

1. LiteLLM client.
2. Model router.
3. Prompt manager.
4. Token manager.
5. Guardrail.

### Sprint 5, Ask and Chat

Deliverables:

1. ask command.
2. chat mode (Should Have).
3. slash command (Should Have, jika chat mode ikut dirilis).
4. source output.
5. confidence output.

### Sprint 6, Review Agents

Deliverables:

1. Indicator Review Agent.
2. PK Review Agent.
3. Rulebook integration.
4. Citation validation.
5. AI output schema validation.

### Sprint 7, Report Generator

Deliverables:

1. Markdown report.
2. XLSX report.
3. Draft label.
4. Source reference appendix.

### Sprint 8, UX Completion

Deliverables:

1. wizard mode.
2. autocomplete.
3. smart suggestion.
4. token warning.
5. setup packaging.
6. release checklist.

---

## 30. Testing Requirements

Detail test resmi mengikuti `TEST_PLAN.md`.

### 30.1 Unit Test

1. Config loader.
2. Document classifier.
3. DOCX reader.
4. PDF reader.
5. XLSX reader.
6. Token manager.
7. Prompt manager.
8. Report writer.
9. Privacy filter.
10. Source reference builder.

### 30.2 Integration Test

1. scan folder.
2. ask document.
3. cek-indikator.
4. review-pk.
5. token usage.
6. privacy mode standard.
7. privacy mode strict.
8. report Markdown/XLSX.

Test integrasi `review-lkjip`, `cek-cascading`, `cek-evidence`, dan `report final` termasuk scope v1.0 Expanded.

### 30.3 AI Output Test

1. Output JSON valid.
2. Confidence ada.
3. Sources ada.
4. Finding tidak kosong.
5. Recommendation tidak kosong.
6. Tidak ada klaim angka tanpa sumber.
7. Source refs memiliki document_id, chunk_id, dan lokasi dokumen.
8. Output tanpa source refs ditolak.
9. Golden dataset menghasilkan finding utama yang sama.

---

## 31. Risk Register

### Risk 1, User Tidak Terbiasa CLI

Mitigation:

1. Wizard mode.
2. Help kontekstual.
3. Slash command.
4. Autocomplete.
5. Smart suggestion.

### Risk 2, Biaya Token Membesar

Mitigation:

1. Token report.
2. Model routing.
3. Konfirmasi task mahal.
4. Cache.
5. Ringkas dokumen sebelum analisis.

### Risk 3, AI Mengarang

Mitigation:

1. RAG berbasis dokumen.
2. Confidence score.
3. Source requirement.
4. Human validation.
5. Guardrail.

### Risk 4, Dokumen Tidak Seragam

Mitigation:

1. Document classifier.
2. Manual override.
3. Warning.
4. Report file gagal.

### Risk 5, Data Sensitif

Mitigation:

1. Privacy mode.
2. Masking.
3. API warning.
4. Strict mode.

---

## 32. Definition of Done

Satu fitur dianggap selesai jika:

1. Command berjalan.
2. Help tersedia.
3. Output Rich rapi.
4. Error tertangani.
5. Log dibuat.
6. Output file dibuat jika diperlukan.
7. Token tercatat jika memakai AI.
8. Test minimal tersedia.
9. Tidak mengubah file asli.
10. Dokumentasi singkat tersedia.

---

## 33. Developer Instructions for Vibe Coding AI Agent

1. Bangun project Python modular.
2. Gunakan Typer untuk CLI.
3. Gunakan Rich untuk terminal UI.
4. Gunakan prompt_toolkit jika interactive mode dan autocomplete v0.2 Should Have ikut dikerjakan.
5. Gunakan LiteLLM untuk AI provider.
6. Gunakan SQLite sebagai storage awal.
7. Gunakan SQLAlchemy untuk ORM.
8. Gunakan python-docx untuk DOCX.
9. Gunakan PyMuPDF dan pdfplumber untuk PDF.
10. Gunakan openpyxl dan pandas untuk XLSX.
11. Pisahkan prompt dari kode.
12. Semua agent harus punya schema input dan output.
13. Semua output AI harus punya confidence dan sources.
14. Semua command panjang harus punya progress bar.
15. Semua hasil masuk folder outputs.
16. Semua error masuk folder logs.
17. Jangan hardcode API Key.
18. Jangan mengubah file asli.
19. Tampilkan suggested next steps setelah command selesai.
20. Buat README command singkat.

---

## 34. Initial File Structure

```text
sakipro/
  pyproject.toml
  README.md
  PRD.md
  .env.example
  config.example.yaml

  sakipro/
    __init__.py
    main.py

    cli/
      __init__.py
      commands.py
      init_cmd.py
      scan_cmd.py
      ask_cmd.py
      chat_cmd.py
      wizard_cmd.py
      review_cmd.py
      evidence_cmd.py
      report_cmd.py
      token_cmd.py
      doctor_cmd.py

    ui/
      __init__.py
      banner.py
      theme.py
      panels.py
      tables.py
      progress.py
      prompts.py
      autocomplete.py
      repl.py
      wizard.py
      suggestions.py
      errors.py

    ai/
      __init__.py
      llm_client.py
      model_router.py
      prompt_manager.py
      token_manager.py
      guardrails.py

    agents/
      __init__.py
      folder_scanner_agent.py
      indicator_review_agent.py
      cascading_review_agent.py
      pk_review_agent.py
      lkjip_review_agent.py
      evidence_review_agent.py
      opd_planning_copilot_agent.py

    documents/
      __init__.py
      docx_reader.py
      pdf_reader.py
      xlsx_reader.py
      csv_reader.py
      classifier.py
      chunker.py
      metadata.py

    sakip/
      __init__.py
      indicator_checker.py
      cascading_checker.py
      pk_checker.py
      lkjip_checker.py
      evidence_checker.py
      report_builder.py

    storage/
      __init__.py
      database.py
      models.py
      repositories.py

    reports/
      __init__.py
      markdown_report.py
      xlsx_report.py
      docx_report.py

    templates/
      prompts/
      docx/
      xlsx/

  tests/
```

---

## 35. Final Product Statement

SAKIPRO v1.0 adalah AI CLI Agent ringan dan berbasis dokumen untuk membantu Kasubbag Perencanaan OPD memperbaiki mutu dokumen SAKIP. Sistem berjalan di laptop kantor, memakai AI API berbasis token, memiliki Rich CLI, scan dokumen, ask document, review indikator, review PK, review LKjIP, cascading, evidence audit, privacy mode, source refs, token tracking, dan report Markdown/XLSX/DOCX draft.

SAKIPRO v1.0 menjadi fondasi praktis untuk meningkatkan kualitas dokumen SAKIP OPD tanpa harus membangun platform besar.

---

END OF PRD.md
