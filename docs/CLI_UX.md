# CLI_UX.md
# SAKIPRO v1.0
# Rich Interactive CLI Blueprint for OPD SAKIP Planning Assistant

Version: 1.0  
Mode: Python CLI  
Target User: Kasubbag Perencanaan OPD  
UI Style: Rich, Interactive, Autocomplete, Slash Command, Wizard  
Target Device: Laptop Kantor CPU-only  
Status: Implementation Ready  
Related Documents: AGENT_SKILLS.md, TASK_MANAGEMENT.md, PRD.md  

---

## 1. Spesifikasi Operasional v1.0

## 2. Identitas CLI

Nama command utama:

```bash
sakipro
```

Nama tampilan:

```text
SAKIPRO CLI
AI Planning Assistant for OPD SAKIP Documents
```

Tagline:

```text
Review • Improve • Draft • Evidence • Report
```

Positioning:

```text
AI CLI Agent ringan untuk membantu Kasubbag Perencanaan OPD memperbaiki mutu dokumen SAKIP.
```

---

## 3. Prinsip Desain UX

SAKIPRO CLI mengikuti prinsip berikut:

1. User tidak wajib hafal command.
2. Semua command penting tersedia dalam wizard.
3. Semua command penting tersedia dalam slash command.
4. Autocomplete tersedia untuk command dan konteks dokumen.
5. Semua proses panjang menampilkan progress bar.
6. Semua hasil tampil dalam panel dan tabel Rich.
7. Semua error menjelaskan penyebab dan solusi.
8. Semua hasil analisis menyertakan status.
9. Semua rekomendasi menyertakan alasan.
10. Semua jawaban berbasis dokumen menyertakan sumber.
11. Semua proses mahal memberi estimasi token dan meminta konfirmasi.
12. Semua file asli aman dan tidak ditimpa.
13. Semua output dibuat di folder outputs.
14. Setiap command memberi saran langkah berikutnya.

---

## 4. Mode Operasi CLI

SAKIPRO sebagai produk memiliki beberapa mode operasi. Untuk v1.0 Core, Quick Command Mode wajib. Interactive Agent Mode dan Wizard Mode berstatus Should Have. Workbench dan report preview penuh masuk Post-v1.0.

### 4.1 Quick Command Mode

Mode perintah langsung.

Contoh:

```bash
sakipro scan ./dokumen_sakip
sakipro cek-indikator
sakipro review-pk
```

Cocok untuk user yang sudah terbiasa.

---

### 4.2 Interactive Agent Mode

Mode percakapan interaktif.

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
Buat daftar perbaikan indikator saya.
```

---

### 4.3 Wizard Mode

Mode panduan langkah demi langkah.

Masuk dengan:

```bash
sakipro wizard
```

Cocok untuk user biasa.

Menu utama:

```text
Apa yang ingin Anda kerjakan?

1. Baca folder dokumen SAKIP OPD
2. Cek mutu indikator
3. Review Perjanjian Kinerja
4. Tanya SAKIPRO
5. Keluar
```

Menu review LKjIP, cascading, evidence, dan laporan akhir termasuk scope v1.0 Expanded.

---

### 4.4 Workbench Mode

Mode dashboard terminal interaktif.

Masuk dengan:

```bash
sakipro workbench
```

Workbench menampilkan ringkasan status dokumen, indikator, PK, LKjIP, evidence, task, dan output dalam layout terminal.

---

### 4.5 Report Preview Mode

Mode membaca hasil laporan langsung di terminal.

Contoh:

```bash
sakipro report preview outputs/04_REVIEW_PK.md
```

---

## 5. Startup Banner

### 5.1 Full Banner

Banner utama saat SAKIPRO dijalankan:

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

### 5.2 Startup Panel

Setelah banner, tampilkan panel status.

```text
╭─ Workspace ───────────────────────────────────╮
│ Project       : DISDIK_2026                   │
│ Folder        : ./dokumen_sakip               │
│ AI Provider   : OpenAI                         │
│ Privacy Mode  : standard                      │
│ Documents     : 9 indexed                     │
│ Evidence      : 32 files                      │
│ Status        : Ready                         │
╰───────────────────────────────────────────────╯
```

Jika belum ada workspace:

```text
╭─ Setup Awal ──────────────────────────────────╮
│ Belum ada workspace aktif.                    │
│ Jalankan: sakipro init                        │
│ Atau gunakan: sakipro wizard                  │
╰───────────────────────────────────────────────╯
```

### 5.3 Compact Banner

Dipakai untuk mode ringkas.

```bash
sakipro --compact
```

Output:

```text
SAKIPRO v1.0 • AI CLI Assistant for OPD SAKIP Planning
```

### 5.4 Silent Mode

Dipakai untuk automation atau cron.

```bash
sakipro --silent
```

Silent mode tidak menampilkan banner.

---

## 6. Command Taxonomy

Command utama SAKIPRO:

```bash
sakipro init
sakipro scan
sakipro status
sakipro ask
sakipro chat
sakipro wizard
sakipro workbench
sakipro cek-indikator
sakipro cek-cascading
sakipro cek-pohon
sakipro review-pk
sakipro review-lkjip
sakipro cek-evidence
sakipro draft
sakipro task
sakipro resume
sakipro report
sakipro token
sakipro model
sakipro privacy
sakipro config
sakipro doctor
```

Command v1.0 Core wajib:

```bash
sakipro init
sakipro doctor
sakipro scan
sakipro status
sakipro ask
sakipro cek-indikator
sakipro review-pk
sakipro token
sakipro privacy
```

Command v1.0 Core Should Have:

```bash
sakipro chat
sakipro wizard
```

Command v1.0 Expanded:

```bash
sakipro review-lkjip
sakipro cek-cascading
sakipro cek-evidence
sakipro report final
sakipro draft
```

---

## 7. Slash Command

Slash command tersedia pada chat mode dan workbench mode. Pada v0.2, slash command hanya wajib jika chat mode ikut dirilis sebagai Should Have.

Daftar slash command:

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
/config
/privacy
/output
/clear
/exit
```

---

## 8. Detail Slash Command

### 8.1 /help

Menampilkan bantuan sesuai konteks.

Jika workspace belum siap:

```text
Langkah awal:
1. /scan
2. Pilih folder dokumen SAKIP OPD
3. Lanjutkan dengan /cek-indikator
```

Jika workspace sudah siap:

```text
Perintah yang tersedia:
1. /cek-indikator    Periksa mutu indikator
2. /review-pk        Review Perjanjian Kinerja
3. /review-lkjip     Review LKjIP
4. /cek-cascading    Cek hubungan sasaran, indikator, program
5. /cek-evidence     Cek bukti dukung
6. /report           Buat laporan akhir
```

---

### 8.2 /status

Menampilkan status project.

```text
╭─ Status Project ──────────────────────────────╮
│ Project        : DISDIK_2026                  │
│ Dokumen        : 9 terbaca                    │
│ Evidence       : 32 file                      │
│ Indikator      : 18 ditemukan                 │
│ PK             : Ada                          │
│ LKjIP          : Ada                          │
│ LHE            : Ada                          │
│ Risiko Awal    : Sedang                       │
╰───────────────────────────────────────────────╯
```

---

### 8.3 /scan

Memilih folder dokumen.

```text
Pilih folder dokumen SAKIP OPD:
> ./Dokumen_SAKIP_DisDik
```

Setelah scan:

```text
╭─ Hasil Scan Folder ───────────────────────────╮
│ Dokumen ditemukan                             │
│ ✓ Renstra_OPD.docx                            │
│ ✓ Renja_2026.xlsx                             │
│ ✓ IKU_OPD.docx                                │
│ ✓ PK_2026.docx                                │
│ ✓ LKjIP_2025.docx                             │
│ ✓ LHE_2025.pdf                                │
│ ✓ Evidence folder                             │
│                                               │
│ Belum ditemukan                               │
│ ✗ Rencana Aksi                                │
│ ✗ Matriks Tindak Lanjut LHE                   │
╰───────────────────────────────────────────────╯
```

---

### 8.4 /cek-indikator

Memeriksa semua indikator.

```text
╭─ Review Indikator ────────────────────────────╮
│ Total indikator     : 18                      │
│ Outcome             : 6                       │
│ Output              : 8                       │
│ Aktivitas           : 4                       │
│ Formula kosong      : 5                       │
│ Sumber data kosong  : 6                       │
│ Status              : PERLU REVISI             │
╰───────────────────────────────────────────────╯
```

Tabel hasil:

```text
┌────┬────────────────────────────┬───────────┬────────────┬─────────────┐
│ No │ Indikator                  │ Jenis     │ Masalah    │ Saran       │
├────┼────────────────────────────┼───────────┼────────────┼─────────────┤
│ 1  │ Jumlah pelatihan guru      │ Aktivitas │ Tidak ukur │ Ganti ke    │
│    │                            │           │ outcome    │ peningkatan │
│ 2  │ Persentase sekolah baik    │ Outcome   │ Formula    │ Lengkapi    │
│    │                            │           │ kurang     │ formula     │
└────┴────────────────────────────┴───────────┴────────────┴─────────────┘
```

---

### 8.5 /review-pk

Memeriksa Perjanjian Kinerja.

Cek:

1. Sasaran ada.
2. Indikator ada.
3. Target ada.
4. Satuan jelas.
5. Konsisten dengan IKU.
6. Konsisten dengan Renstra.
7. Ada dukungan program.

Output:

```text
╭─ Review PK ───────────────────────────────────╮
│ Dokumen PK      : PK_2026.docx                │
│ Sasaran         : 5                            │
│ Indikator       : 12                           │
│ Target lengkap  : 10                           │
│ Target konflik  : 2                            │
│ Status          : PERLU CEK                    │
╰───────────────────────────────────────────────╯
```

---

### 8.6 /review-lkjip

Status: v1.0 Expanded.

Memeriksa LKjIP.

Cek:

1. Sesuai PK.
2. Ada target dan realisasi.
3. Ada analisis keberhasilan.
4. Ada analisis kegagalan.
5. Ada efisiensi anggaran.
6. Ada tindak lanjut.
7. Ada evidence.

Output:

```text
╭─ Review LKjIP ────────────────────────────────╮
│ Dokumen LKjIP         : LKjIP_2025.docx        │
│ Sesuai PK             : Perlu cek              │
│ Analisis capaian      : Sedang                 │
│ Analisis efisiensi    : Kurang                 │
│ Tindak lanjut         : Kurang spesifik        │
│ Status                : PERLU REVISI           │
╰───────────────────────────────────────────────╯
```

---

### 8.7 /cek-cascading

Status: v1.0 Expanded.

Memeriksa hubungan:

```text
Sasaran OPD
→ Indikator
→ Program
→ Kegiatan
→ Subkegiatan
→ Anggaran
→ Evidence
```

Output:

```text
╭─ Review Cascading ────────────────────────────╮
│ Sasaran ditemukan       : 5                   │
│ Indikator ditemukan     : 12                  │
│ Program terkait         : 8                   │
│ Rantai lengkap          : 6                   │
│ Rantai putus            : 4                   │
│ Status                  : PERLU REVISI         │
╰───────────────────────────────────────────────╯
```

---

### 8.8 /cek-pohon

Status: v1.0 Expanded.

Menampilkan pohon kinerja dalam Rich Tree.

```text
Pohon Kinerja OPD
├── Sasaran 1: Meningkatnya mutu layanan pendidikan
│   ├── Indikator: Persentase sekolah bermutu baik
│   ├── Program: Program Pengelolaan Pendidikan
│   └── Kegiatan: Pembinaan SMP
└── Sasaran 2: Meningkatnya tata kelola pendidikan
    ├── Indikator: Nilai SAKIP OPD
    └── Program: Program Penunjang Urusan Pemerintahan
```

Jika ada rantai putus:

```text
⚠ Kegiatan "Pelatihan Operator" belum terhubung ke sasaran outcome.
```

---

### 8.9 /cek-evidence

Status: v1.0 Expanded.

Memeriksa bukti dukung.

```text
╭─ Audit Evidence ──────────────────────────────╮
│ Klaim kinerja    : 24                         │
│ Evidence valid   : 14                         │
│ Evidence lemah   : 6                          │
│ Evidence kosong  : 4                          │
│ Status           : PERLU LENGKAPI              │
╰───────────────────────────────────────────────╯
```

---

### 8.10 /draft

Status: v1.0 Expanded.

Membuat draft.

Menu:

```text
Pilih jenis draft:
1. Rekomendasi perbaikan indikator
2. Narasi analisis LKjIP
3. Matriks tindak lanjut LHE
4. Perbaikan rumusan sasaran
5. Catatan review PK
```

---

### 8.11 /task

Status: Post-v1.0.

Menerima tugas panjang.

Contoh:

```text
/task review seluruh dokumen SAKIP OPD dan buat daftar perbaikan
```

SAKIPRO memecah task:

```text
1. Scan dokumen
2. Ekstrak sasaran
3. Ekstrak indikator
4. Review PK
5. Review LKjIP
6. Cek cascading
7. Cek evidence
8. Susun laporan final
```

---

### 8.12 /report

Status: v1.0 Expanded untuk laporan final; v0.2 hanya membutuhkan output Markdown/XLSX per review indikator dan PK.

Membuat laporan.

Pilihan:

```text
1. Ringkasan dokumen
2. Review indikator
3. Review cascading
4. Review PK
5. Review LKjIP
6. Audit evidence
7. Laporan final perbaikan OPD
```

---

### 8.13 /token (alias /usage)

Menampilkan pemakaian token dan estimasi biaya.

```text
╭─ Token Usage & Cost ──────────────────────────╮
│ Hari ini        : 18.420 token                │
│ Bulan ini       : 412.900 token               │
│ Estimasi biaya  : Rp 96.000                   │
│                                               │
│ Distribusi Model:                             │
│ 1. gemini-1.5-flash : 320.000 token (77%)     │
│ 2. gpt-4o           : 82.000 token (20%)      │
│ 3. claude-3-5-sonn  : 10.900 token (3%)       │
╰───────────────────────────────────────────────╯
```

---

### 8.14 /model

Mengatur model AI yang digunakan.

Contoh `sakipro model list`:

```text
╭─ Supported AI Models ────────────────────────────────────────────────╮
│ PROVIDER   │ MODEL ID                   │ TIER     │ STATUS          │
├────────────┼────────────────────────────┼──────────┼─────────────────┤
│ Google     │ gemini-1.5-flash           │ Light    │ Available       │
│ OpenAI     │ gpt-4o-mini                │ Light    │ Available       │
│ OpenAI     │ gpt-4o                     │ Default  │ Available       │
│ Anthropic  │ claude-3-5-sonnet          │ Default  │ Available       │
│ Anthropic  │ claude-sonnet-4-20250514   │ Default  │ API Key Ready   │
│ xAI (Grok) │ grok-beta                  │ Reasoning│ Available       │
│ DeepSeek   │ deepseek-chat              │ Economy  │ Available       │
╰────────────┴────────────────────────────┴──────────┴─────────────────╯
```

Contoh `sakipro model switch`:

```text
Pilih model utama:
> [1] Anthropic: claude-sonnet-4-20250514 (API Key Ready - Aktif)
  [2] Google: gemini-1.5-flash (Fast & Large Context)
  [3] OpenAI: gpt-4o (Smart & Balanced)
  [4] Anthropic: claude-3-5-sonnet (Best Reasoning)
  [5] DeepSeek: deepseek-chat (Cost Effective)

[✓] Berhasil beralih ke claude-sonnet-4-20250514.
```

### 8.15 /config set-key

Menginput API Key secara interaktif.

Contoh `sakipro config set-key`:

```text
Pilih Provider:
> [1] OpenAI
  [2] Anthropic
  [3] Google (Gemini)
  [4] xAI (Grok)
  [5] DeepSeek

Masukkan API Key untuk OpenAI:
> sk-proj-........................................

[✓] API Key berhasil disimpan di .env secara aman.
```

---

## 9. Autocomplete

SAKIPRO wajib memiliki autocomplete pada 3 level.

### 9.1 Shell Autocomplete

Contoh:

```bash
sakipro rev<TAB>
```

Menampilkan:

```text
review-pk
review-lkjip
```

Command yang harus didukung:

```text
scan
status
ask
chat
wizard
workbench
cek-indikator
cek-cascading
cek-pohon
review-pk
review-lkjip
cek-evidence
draft
task
report
doctor
token
config
```

---

### 9.2 Interactive Slash Autocomplete & Autohint

Saat user berada dalam mode `chat` dan mengetik karakter `/`, sistem harus:
1. **Daftar Saran (Popup):** Menampilkan menu drop-down kecil berisi perintah yang tersedia.
2. **Autohint (Ghost Text):** Menampilkan sisa perintah dalam teks berwarna abu-abu (muted) sebagai saran yang bisa diambil dengan menekan tombol `→` (panah kanan) atau `End`.

Contoh visual saat user mengetik `/ce`:
```text
sakipro > /ce
           /cek-indikator    [Audit Mutu Indikator]
           /cek-cascading    [Review Logika Sasaran]
           /cek-evidence     [Audit Bukti Dukung]
```
*(User cukup menekan panah bawah atau terus mengetik untuk mempersempit pilihan)*

---

### 9.3 Context Autocomplete

Autocomplete berbasis isi dokumen.

Contoh:

```text
cek indikator <TAB>
```

Pilihan:

```text
Persentase sekolah bermutu baik
Nilai SAKIP OPD
Angka Partisipasi Sekolah
Jumlah pelatihan guru
```

Contoh:

```text
review file <TAB>
```

Pilihan:

```text
PK_2026.docx
LKjIP_2025.docx
IKU_OPD.docx
Renstra_OPD.docx
```

---

## 10. Smart Suggestion

Setiap command harus diakhiri dengan saran.

Contoh setelah scan:

```text
Saran berikutnya:
1. sakipro cek-indikator
2. sakipro review-pk
3. sakipro ask "dokumen apa yang belum lengkap?"
```

Contoh setelah review PK:

```text
Saran berikutnya:
1. Perbaiki 3 target yang tidak konsisten
2. Lengkapi sumber data indikator
3. Simpan hasil review PK sebagai draft
```

---

## 11. Help System

SAKIPRO harus memiliki help bertingkat.

### 11.1 Help Umum

```bash
sakipro --help
```

Output:

```text
Perintah v1.0 Core:
scan             Baca folder dokumen OPD
ask              Tanya jawab dengan dokumen
cek-indikator    Review mutu indikator
review-pk        Review Perjanjian Kinerja
token            Lihat pemakaian token
privacy          Lihat atau ubah privacy mode
doctor           Cek kesiapan sistem

Perintah v1.0 Expanded:
review-lkjip, cek-cascading, cek-evidence, draft, report final
```
```

---

### 11.2 Help Per Command

```bash
sakipro review-pk --help
```

Output:

```text
review-pk

Fungsi:
Mereview Perjanjian Kinerja OPD.

Contoh:
sakipro review-pk
sakipro review-pk --file PK_2026.docx
sakipro review-pk --compare IKU_OPD.docx

Output:
outputs/review_pk.md
outputs/review_pk.xlsx
```

---

### 11.3 Help Kontekstual

Jika user salah mengetik:

```bash
sakipro cek-indkator
```

SAKIPRO membalas:

```text
Perintah tidak ditemukan: cek-indkator

Mungkin maksud Anda:
1. cek-indikator
2. review-pk
3. ask
```

---

## 12. Wizard Mode

Command:

```bash
sakipro wizard
```

Status: Should Have untuk v0.2 dengan menu terbatas; menu penuh di bawah adalah target v1.0 Expanded.

Tampilan:

```text
Apa yang ingin Anda kerjakan?

1. Baca folder dokumen SAKIP OPD
2. Cek mutu indikator
3. Review Perjanjian Kinerja
4. Review LKjIP
5. Cek cascading
6. Cek evidence
7. Buat laporan akhir
8. Tanya SAKIPRO
9. Keluar
```

Wizard flow minimal:

1. Pilih aksi.
2. Pilih folder atau dokumen.
3. Tampilkan estimasi proses.
4. Jalankan proses.
5. Tampilkan ringkasan.
6. Tawarkan simpan laporan.
7. Tawarkan langkah berikutnya.

---

## 13. Workbench Mode

Command:

```bash
sakipro workbench
```

Layout:

```text
╭──────────────────── SAKIPRO WORKBENCH ────────────────────╮
│ Project: DISDIK_2026        Mode: OPD Workspace            │
├───────────────────┬───────────────────────────────────────┤
│ Menu              │ Panel Utama                            │
│                   │                                       │
│ 1. Dokumen        │ Ringkasan Risiko                       │
│ 2. Indikator      │                                       │
│ 3. Cascading      │ ┌──────────────┬──────────────┐       │
│ 4. PK             │ │ Area         │ Status       │       │
│ 5. LKjIP          │ ├──────────────┼──────────────┤       │
│ 6. Evidence       │ │ Indikator    │ Perlu Revisi │       │
│ 7. Task           │ │ PK           │ Perlu Cek    │       │
│ 8. Laporan        │ │ Evidence     │ Kurang       │       │
│ 9. Pengaturan     │ └──────────────┴──────────────┘       │
├───────────────────┴───────────────────────────────────────┤
│ Ketik angka menu atau command.                             │
╰───────────────────────────────────────────────────────────╯
```

---

## 14. Advanced UI Components (Inspired by Gemini CLI)

### 14.1 Narrative Topic System

Untuk pekerjaan audit panjang, CLI harus menampilkan transisi fase (Chapter) yang jelas:
- **Style:** Header tebal dengan latar warna redup.
- **Content:** Nama Chapter dan ringkasan singkat apa yang sedang dilakukan.

### 14.2 Severity-Coded Finding Panels

Gunakan panel Rich dengan border berwarna untuk membedakan urgensi temuan:
- **[CRITICAL] Red Border:** Inkonsistensi target fatal, data sensitif bocor.
- **[WARNING] Yellow Border:** Indikator tidak berorientasi outcome.
- **[DRAFT] Green Border:** Usulan revisi teks/narasi dari AI.

### 14.3 Interactive Decision Gates

Di akhir setiap analisis unit (misal: satu indikator), CLI memberikan gerbang keputusan:
- **Confirm Prompt:** `[y/n]` untuk menyimpan temuan ke draf laporan.
- **Choice Menu:** Memberikan opsi aksi (Revisi, Lewati, Validasi Manual).

### 14.4 Muted Technical Metadata

Informasi pelengkap ditampilkan secara redup (grey50) di bagian bawah output:
- `Model: <name> | Confidence: <score> | Token: <count> | Est. Cost: <idr>`

### 14.5 Plan Mode Visualization

Sebelum eksekusi berat, tampilkan rencana strategi audit:

```text
╭─ Execution Plan ──────────────────────────────╮
│ Step 1: Scan Renstra (3 files)                │
│ Step 2: Extract Indicators (Target 15 units)  │
│ Step 3: Compare to PK 2026                    │
│                                               │
│ Est. Tokens: 45,000 | Est. Cost: Rp 12.000    │
╰───────────────────────────────────────────────╯
Lanjutkan eksekusi? [y/n]
```

### 14.6 Narrative Topic System (Detailed)

Gunakan header blok untuk setiap transisi fase kerja:

```text
[CHAPTER: DATA INGESTION] ──────────────────────────
> Reading Renstra_Disdik_2026.docx... Done.
> Reading IKU_OPD_Final.xlsx... Done.
```

---

## 15. Output Status Standard

Status standar:

```text
AMAN
PERLU CEK
PERLU REVISI
RISIKO TINGGI
DATA KURANG
GAGAL
SELESAI
```

Warna:

```text
AMAN          : green
PERLU CEK     : yellow
PERLU REVISI  : yellow
RISIKO TINGGI : red
DATA KURANG   : red
GAGAL         : red
SELESAI       : green
```

---

## 15. Natural Language Command

SAKIPRO menerima perintah natural.

Contoh:

```bash
sakipro "tolong cek indikator saya"
sakipro "review PK tahun 2026"
sakipro "apa kelemahan LKjIP saya"
sakipro "buatkan laporan perbaikan dokumen"
```

SAKIPRO memetakan ke command inti.

Contoh output:

```text
Saya pahami sebagai: cek-indikator

Lanjutkan?
[1] Ya
[2] Pilih perintah lain
[3] Batalkan
```

---

## 16. Konfirmasi Cerdas

### 16.1 Konfirmasi Token

Sebelum task mahal:

```text
╭─ Konfirmasi Token ────────────────────────────╮
│ Task ini memakai model reasoning.             │
│ Estimasi token : 80.000                       │
│ Estimasi biaya : Rp 2Stable Release00                    │
│ Lanjutkan?                                    │
╰───────────────────────────────────────────────╯

[1] Lanjut
[2] Pakai model hemat
[3] Batalkan
```

### 16.2 Konfirmasi Generate File

```text
File akan dibuat:
outputs/REVIEW_PK_2026.docx

Lanjutkan?
[1] Ya
[2] Ganti nama file
[3] Batalkan
```

---

## 17. Layout Laporan Akhir di Terminal

```text
╭─ Laporan Final SAKIPRO ───────────────────────╮
│ OPD        : Dinas Pendidikan                 │
│ Tahun      : 2026                             │
│ Status     : PERLU REVISI                     │
│ Risiko     : Sedang                           │
╰───────────────────────────────────────────────╯

Temuan utama:
1. 8 indikator masih output atau aktivitas.
2. 3 target PK tidak konsisten dengan IKU.
3. LKjIP belum memuat analisis efisiensi yang cukup.
4. 4 klaim kinerja belum punya evidence kuat.

File dibuat:
1. outputs/REVIEW_INDIKATOR.xlsx
2. outputs/REVIEW_PK.md
3. outputs/REVIEW_LKJIP.md
4. outputs/LAPORAN_FINAL.docx
```

---

## 18. Keyboard Shortcut Interactive Mode

```text
Ctrl + C    Batalkan proses
Ctrl + D    Keluar
Ctrl + L    Bersihkan layar
Tab         Autocomplete
Up/Down     Riwayat command
?           Help cepat
/           Slash command
```

---

## 19. Riwayat Command

SAKIPRO menyimpan riwayat command di:

```text
~/.sakipro/history
```

Manfaat:

1. User mudah mengulang perintah.
2. Interactive mode terasa nyaman.
3. Resume session lebih mudah.

---

## 20. Resume Session

Command:

```bash
sakipro resume
```

Output:

```text
╭─ Resume Session ──────────────────────────────╮
│ Last Project : DISDIK_2026                    │
│ Last Task    : Review seluruh dokumen SAKIP   │
│ Progress     : 5 dari 7 tahap selesai         │
│ Status       : Menunggu audit evidence        │
╰───────────────────────────────────────────────╯

Lanjutkan?
[1] Ya
[2] Tidak
```

---

## 21. Error Layout

```text
╭─ Error ───────────────────────────────────────╮
│ PDF gagal dibaca: LHE_2025_scan.pdf           │
│ Penyebab: file hasil scan tanpa teks.         │
│ Saran: aktifkan OCR atau unggah PDF teks.     │
╰───────────────────────────────────────────────╯
```

---

## 22. Success Layout

```text
╭─ Success ─────────────────────────────────────╮
│ Laporan berhasil dibuat.                      │
│ File: outputs/REVIEW_PK_2026.md               │
╰───────────────────────────────────────────────╯
```

---

## 23. Privacy Warning

Jika dokumen mengandung data sensitif:

```text
╭─ Privacy Warning ─────────────────────────────╮
│ Dokumen mengandung data sensitif.             │
│ Sistem akan melakukan masking sebelum         │
│ mengirim konteks ke AI API.                   │
│ Mode aktif: standard                          │
╰───────────────────────────────────────────────╯
```

Jika mode strict:

```text
╭─ Blocked by Privacy Mode ─────────────────────╮
│ Dokumen ini tidak dikirim ke AI cloud karena  │
│ privacy mode strict.                          │
╰───────────────────────────────────────────────╯
```

---

## 24. Token Warning

```text
╭─ Token Warning ───────────────────────────────╮
│ Token bulanan sudah mencapai 85%.             │
│ Gunakan model hemat untuk task ringan.        │
╰───────────────────────────────────────────────╯
```

---

## 25. Theme Design

### 25.1 Color Mapping

```text
Primary       : cyan
Success       : green
Warning       : yellow
Error         : red
Info          : blue
Muted         : grey50
Evidence      : green
Risk High     : red
Risk Medium   : yellow
Risk Low      : green
AI Agent      : magenta
Document      : cyan
```

### 25.2 Icon Mapping

Icon bersifat opsional.

```text
Project       : 📁
Document      : 📄
Evidence      : 🧾
AI Agent      : 🤖
Warning       : ⚠
Success       : ✓
Error         : ✗
Score         : ★
Task          : ☐
Memory        : 🧠
Token         : ◉
Security      : 🔒
```

Config:

```yaml
ui:
  use_emoji: true
  theme: dark
  compact: false
```

---

## 26. Rich Component Mapping

Gunakan komponen Rich:

```text
Console
Panel
Table
Tree
Progress
Spinner
Status
Prompt
Confirm
Markdown
Syntax
Live
Layout
```

Fungsi:

1. Panel untuk summary.
2. Table untuk laporan ringkas.
3. Tree untuk pohon kinerja.
4. Progress untuk proses panjang.
5. Live untuk workbench.
6. Markdown untuk preview laporan.
7. Syntax untuk preview JSON.

---

## 27. Project Tree View

Command:

```bash
sakipro project tree
```

Output:

```text
Dokumen_SAKIP_OPD
├── Renstra_OPD.docx
├── Renja_2026.xlsx
├── IKU_OPD.docx
├── PK_2026.docx
├── LKjIP_2025.docx
├── LHE_2025.pdf
└── Evidence
    ├── Notulen_Monev_Q1.pdf
    └── Screenshot_eSAKIP.png
```

---

## 28. Report Preview

Command:

```bash
sakipro report preview outputs/REVIEW_PK_2026.md
```

Tampilan memakai Rich Markdown.

---

## 29. Config UI

File:

```yaml
ui:
  banner: full
  theme: dark
  use_emoji: true
  show_token_cost: true
  show_sources: true
  show_confidence: true
  show_next_steps: true
  compact_mode: false
  autocomplete: true
  slash_commands: true
  wizard_enabled: true
```

---

## 30. Struktur Modul UI

```text
sakipro/
  ui/
    __init__.py
    banner.py
    theme.py
    console.py
    panels.py
    tables.py
    progress.py
    prompts.py
    autocomplete.py
    repl.py
    wizard.py
    workbench.py
    help.py
    errors.py
    suggestions.py
```

---

## 31. Fungsi Helper Wajib

```text
print_banner()
print_startup_panel()
print_project_status()
print_success()
print_warning()
print_error()
print_help()
print_sources()
print_confidence()
print_next_steps()
render_table()
render_tree()
render_progress()
render_task_board()
render_report_summary()
```

---

## 32. Rekomendasi Library UI

Untuk implementasi Python:

```text
typer
rich
prompt_toolkit
questionary
shellingham
pyyaml
```

Pembagian:

1. Typer untuk CLI command.
2. Rich untuk panel, tabel, tree, markdown, progress.
3. prompt_toolkit untuk interactive REPL dan autocomplete.
4. Questionary untuk wizard.
5. shellingham untuk deteksi shell.
6. PyYAML untuk config.

---

## 33. Acceptance Criteria CLI UI

CLI UI dianggap selesai jika:

1. Startup banner tampil.
2. Project status panel tampil.
3. Quick command mode berjalan.
4. Ask document tampil dengan source refs.
5. Wizard mode berjalan jika fitur Should Have diaktifkan.
6. Interactive chat mode berjalan jika fitur Should Have diaktifkan.
7. Slash command inti tersedia jika chat mode diaktifkan.
8. Autocomplete command tersedia jika fitur Should Have diaktifkan.
9. Rich progress bar tampil.
10. Rich table result tampil.
11. Error panel tampil.
12. Success panel tampil.
13. Suggested next steps tampil.
14. Token warning tampil.
15. Help perintah tersedia.
16. Output file diberi lokasi jelas.
17. Privacy warning tampil saat perlu.
18. User biasa dapat menjalankan review PK melalui command langsung, dan melalui wizard jika Should Have diaktifkan.

---

## 34. v0.2 CLI UI Scope

Wajib dibuat pada v1.0 Core:

1. Banner startup.
2. Project status panel.
3. Quick command mode.
4. Ask result panel dengan source refs.
5. Review result table.
6. Privacy warning.
7. Rich progress bar.
8. Rich table result.
9. Error panel.
10. Success panel.
11. Suggested next steps.
12. Token warning.
13. Help perintah.
14. Output path display.

v1.0 Expanded:

1. Wizard mode penuh untuk scan, indikator, PK, LKjIP, cascading, evidence, dan final report.
2. Interactive chat mode penuh.
3. Slash command inti v0.2.
4. Report preview untuk output Markdown.

Post-v1.0:

1. Workbench mode penuh.
2. Context autocomplete indikator.
3. Live dashboard.
4. Theme switching.
5. Task board.
6. Resume session.

---

## 35. Developer Notes for Vibe Coding Agent

1. Buat modul ui terpisah.
2. Jangan campur logic analisis dengan logic tampilan.
3. Semua command harus memakai helper UI.
4. Semua proses panjang harus memakai progress bar.
5. Semua error harus masuk print_error.
6. Semua success harus masuk print_success.
7. Semua hasil review harus punya summary panel.
8. Semua hasil review harus punya suggested next steps.
9. Interactive mode memakai prompt_toolkit.
10. Wizard mode memakai questionary.
11. Autocomplete harus bertahap, mulai dari command autocomplete.
12. Context autocomplete indikator dapat dibuat setelah scan folder.
13. Banner harus dapat dimatikan dengan --silent.
14. Emoji harus dapat dimatikan via config.
15. Output CLI harus tetap terbaca pada terminal Windows.

---

## 36. Positioning Akhir

CLI_UX SAKIPRO v1.0 dirancang sebagai antarmuka terminal modern yang ramah untuk user biasa. Desain ini menggabungkan Rich GUI terminal, wizard, slash command, autocomplete, smart suggestion, report preview, token warning, dan help kontekstual agar Kasubbag Perencanaan OPD dapat menjalankan review dokumen SAKIP dengan mudah dan aman.

END OF CLI_UX.md
