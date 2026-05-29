# CLI_BLUEPRINT.md

# SAKIPRO v1.0

# Advanced Interactive CLI Blueprint

Version: 1.0
Product: SAKIPRO
Mode: Python CLI
Inspired by: Claude Code CLI, Gemini CLI
Stack: Python 3.12 · Typer · Rich · prompt_toolkit · questionary
Status: Design Reference

---

## 1. Filosofi Desain

CLI workstation interaktif (Default REPL, async thinking/step-mode, auto-hint, bottom status bar, inline diffs, decision gates) ramah pengguna non-teknis.

### Satu Perintah, Satu Pintu

```bash
sakipro
```

Cukup satu perintah. Tidak ada subcommand wajib. `sakipro` langsung menampilkan banner, status workspace, lalu membuka **REPL interaktif** siap terima input. User bisa langsung mengetik — slash command, bahasa natural, atau pertanyaan — tanpa harus tahu subcommand apapun.

Tiga mode yang tersedia tapi tidak wajib diketahui user:

```
Mode Default   : sakipro               → banner + REPL (slash cmd + chat)
Mode Wizard    : sakipro wizard        → panduan langkah demi langkah
Mode Satu Shot : sakipro <command>     → jalankan satu perintah dan keluar
```

Prinsip tidak bisa dilanggar:

1. **Satu perintah cukup.** `sakipro` saja sudah membuka seluruh kemampuan CLI.
2. User tidak wajib hafal command apapun — autocomplete dan hint selalu tersedia.
3. Setiap proses menampilkan progress nyata, bukan diam.
4. Setiap error menjelaskan penyebab dan tindakan perbaikan.
5. File asli tidak pernah dimodifikasi atau dihapus.
6. Setiap output AI diberi status "DRAFT" dan confidence score.
7. Biaya token selalu transparan sebelum task berat dijalankan.
8. **Setiap respons selalu diakhiri rekomendasi langkah berikutnya.**

---

## 2. Startup Experience

### 2.1 Full Banner

Ditampilkan saat `sakipro` dijalankan (tanpa argumen apapun).

```
╔══════════════════════════════════════════════════════════════════╗
║                                                                  ║
║   ███████╗ █████╗ ██╗  ██╗██╗██████╗ ██████╗  ██████╗            ║
║   ██╔════╝██╔══██╗██║ ██╔╝██║██╔══██╗██╔══██╗██╔═══██╗           ║
║   ███████╗███████║█████╔╝ ██║██████╔╝██████╔╝██║   ██║           ║
║   ╚════██║██╔══██║██╔═██╗ ██║██╔═══╝ ██╔══██╗██║   ██║           ║
║   ███████║██║  ██║██║  ██╗██║██║     ██║  ██║╚██████╔╝           ║
║   ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝╚═╝     ╚═╝  ╚═╝ ╚═════╝            ║
║                                                                  ║
║   AI CLI Assistant for OPD SAKIP Planning Documents  v1.0.0      ║
║   Review  •  Improve  •  Draft  •  Evidence  •  Report           ║
║   Hak Cipta(c)2026 -syams_ideris •  syamsuddin.ideris@gmail.com  ║
║                                                                  ║
╚══════════════════════════════════════════════════════════════════╝
```

Setelah banner, tampilkan **Startup Panel** secara langsung (tidak menunggu input), lalu REPL prompt langsung aktif:

```
╭─ Workspace ──────────────────────────────────────────────────╮
│  Project      : DISDIK_2026                                  │
│  Folder       : ./Dokumen_SAKIP_DisDik   (9 dokumen indexed) │
│  Model        : claude-sonnet-4-20250514  [API Key Ready]    │
│  Privacy      : standard                                     │
│  Token Bulan  : 412.900 / 1.000.000  ▓▓▓▓░░░░░░  41%         │
│  Status       : ✓ Siap                                       │
╰──────────────────────────────────────────────────────────────╯

 Ketik /  untuk perintah    •    Ketik ?  untuk bantuan    •    Ctrl+D untuk keluar

sakipro ❯ 
```

REPL aktif secara langsung. User tidak perlu mengetik subcommand tambahan. Kursor siap menerima input — slash command, pertanyaan, atau perintah natural language.

### 2.2 First-Run Experience

Saat user pertama kali menjalankan SAKIPRO tanpa konfigurasi:

```
╭─ 
│                                                              │
│  Ini pertama kali SAKIPRO dijalankan.                        │
│  Mari siapkan workspace Anda.                                │
│                                                              │
│  Langkah 1 dari 3: Pilih Provider AI                         │
╰──────────────────────────────────────────────────────────────╯

  Pilih provider AI:
  ❯ Anthropic (claude-sonnet-4-20250514) [API Key Ready]
    OpenAI    (gpt-4o)
    Google    (gemini-1.5-pro)
    DeepSeek  (deepseek-chat)
```

Setup wizard berjalan otomatis: provider → API key → folder default → privacy mode. Tidak perlu user baca dokumentasi.

### 2.3 Startup Modes

| Cara Memanggil | Tampilan | Kasus |
| --- | --- | --- |
| `sakipro` | Full banner + status panel + REPL | Default — satu-satunya yang perlu user tahu |
| `sakipro wizard` | Banner compact + wizard menu | User pemula, panduan langkah demi langkah |
| `sakipro <command>` | Banner compact + jalankan command + keluar | Mode satu-shot untuk user advanced |
| `sakipro --compact` | `SAKIPRO v1.0 · gpt-4o · DISDIK_2026` + REPL | Session lanjutan tanpa banner besar |
| `sakipro --silent` | Tidak ada banner, output murni | Automation, cron, pipe |
| `sakipro --no-banner` | Hanya status panel + REPL | Gunakan berulang kali dalam sehari |

---

## 3. Status Bar Persisten

SAKIPRO menampilkan **status bar satu baris** di bagian bawah terminal selama mode interaktif aktif. Terinspirasi dari Claude Code dan IDE modern.

```
 gpt-4o  │  DISDIK_2026  │  9 dok  │  Token: 18.420  │  standard  │  ctrl+d keluar
```

Status bar diperbarui secara real-time saat:

- Model berubah
- Token bertambah setelah setiap AI call
- Privacy mode berubah
- Dokumen baru terindeks

Implementasi: `prompt_toolkit` `bottom_toolbar` dengan `HTML` styling.

---

## 4. Mode REPL — Mode Default SAKIPRO

Ini adalah mode yang aktif saat user menjalankan `sakipro`. Tidak perlu subcommand. REPL langsung siap menerima input apa saja.

### 4.1 Prompt Utama

```
sakipro ❯ 
```

Warna Prompt:

- `cyan` → normal, siap menerima input
- `yellow` → memproses (AI sedang berpikir / tool berjalan)
- `red` → error terjadi, perlu perhatian
- `green` → task selesai

### 4.2 Apa yang Bisa Diketik User

User bisa mengetik **tiga jenis input** — semuanya diterima tanpa setup:

```
sakipro ❯ /review-pk              ← slash command
sakipro ❯ review PK saya          ← bahasa natural
sakipro ❯ apa kelemahan indikator saya?  ← pertanyaan bebas
```

### 4.3 Multi-line Input

User bisa mengirim perintah panjang multi-baris:

```
sakipro ❯ tolong review PK saya secara menyeluruh,
        . bandingkan dengan IKU dan Renstra,
        . lalu buat daftar perbaikan
        .
        . [Enter untuk kirim]
```

Shortcut:

- `Enter` → kirim perintah
- `Alt+Enter` atau `Shift+Enter` → newline dalam input (multi-baris)
- `Ctrl+C` → batalkan input saat ini

### 4.4 Thinking & Step Mode (Tampilan Proses Berpikir)

Ini adalah fitur inti SAKIPRO CLI. Setiap kali AI memproses input, user melihat **secara langsung** apa yang sedang dilakukan — step per step, transparan, real-time. Tidak ada layar diam atau loading tanpa informasi.

Alur tampilan lengkap dari input hingga hasil:

```
sakipro ❯ apa kelemahan indikator OPD saya?

 ╭─ Thinking ──────────────────────────────────────────────────╮
 │  ◌  Memahami pertanyaan...                                  │
 │  ◌  Mencari konteks dokumen yang relevan...                 │
 ╰─────────────────────────────────────────────────────────────╯

 ╭─ Langkah 1 — Membaca Dokumen ───────────────────────────────╮
 │  ⠸  IKU_OPD.docx              membaca...                    │
 │  ✓  IKU_OPD.docx              15 indikator ditemukan        │
 │  ⠸  PK_2026.docx              membaca...                   │
 │  ✓  PK_2026.docx              12 indikator ditemukan        │
 │  ✓  Renstra_OPD.docx          12 sasaran ditemukan          │
 ╰─────────────────────────────────────────────────────────────╯

 ╭─ Langkah 2 — Analisis AI ───────────────────────────────────╮
 │  ◌  Memeriksa orientasi setiap indikator...                 │
 │  ◌  Membandingkan indikator dengan standar outcome...       │
 │  ◌  Mengidentifikasi indikator tanpa formula...             │
 │  ◌  Mengidentifikasi indikator tanpa sumber data...         │
 │  ✓  Analisis selesai   [token: 12.450]                      │
 ╰─────────────────────────────────────────────────────────────╯
```

Setelah thinking selesai, respons muncul secara **streaming** karakter per karakter:

```
 Berdasarkan dokumen IKU_OPD.docx dan Renstra_OPD.docx, saya
 menemukan beberapa kelemahan pada indikator OPD Anda:

 1. **8 indikator masih mengukur aktivitas, bukan outcome**
    Contoh: "Jumlah pelatihan guru" mengukur berapa kali
    pelatihan dilaksanakan, bukan dampaknya terhadap mutu
    pengajaran.

 2. **5 indikator tidak memiliki formula pengukuran**
    Tanpa formula, tidak bisa diverifikasi cara menghitung
    capaian yang valid.

 3. **6 indikator tidak mencantumkan sumber data**
    ...
```

Untuk pertanyaan sederhana (tidak membutuhkan tool), thinking lebih ringkas:

```
sakipro ❯ apa itu indikator outcome?

 ◌  Memahami pertanyaan...

 Indikator outcome adalah indikator yang mengukur **perubahan
 nyata** yang dirasakan oleh penerima layanan, bukan sekedar
 kegiatan yang dilaksanakan...
```

Untuk task berat multi-langkah, gunakan **Chapter Mode**:

```
sakipro ❯ /review-pk

═══════════════════ REVIEW PERJANJIAN KINERJA ═══════════════════

 [CHAPTER 1: MEMBACA DOKUMEN] ───────────────────────────────────
  ✓  PK_2026.docx          12 sasaran, 28 halaman
  ✓  IKU_OPD.docx          15 indikator
  ✓  Renstra_OPD.docx      5 tujuan, 12 sasaran strategis

 [CHAPTER 2: EKSTRAKSI DATA] ────────────────────────────────────
  ✓  Sasaran PK diekstrak    12 sasaran
  ✓  Indikator PK            18 indikator
  ✓  Target PK               18 target dengan satuan
  ⠸  Membandingkan dengan IKU...

 [CHAPTER 3: ANALISIS AI] ───────────────────────────────────────
  ◌  Memeriksa konsistensi target antar dokumen...
  ◌  Memverifikasi satuan target...
  ◌  Mencari indikator yang tidak ada di IKU...
  ✓  Analisis selesai   [token: 14.200 / ~18.000]

 [CHAPTER 4: MENYUSUN TEMUAN] ───────────────────────────────────
  ✓  2 konflik target ditemukan
  ✓  3 indikator PK tidak ada di IKU
  ✓  Laporan disusun
```

### 4.5 Streaming AI Response & Thread-Safe UI Queue

Respons muncul karakter per karakter setelah thinking selesai. Tidak ada blank screen menunggu.

**Implementasi:** LiteLLM `stream=True` + `rich.live.Live` dengan panel yang di-refresh per token.

Guna menghindari kerusakan tata letak terminal (*rendering collision*) antara input REPL (`prompt_toolkit`) dengan keluaran status/stream AI secara asinkron (`Rich.Live`), SAKIPRO mengimplementasikan **Thread-Safe Terminal Rich Output Queue**:

1. Seluruh token teks keluaran AI, update token counter, dan log pemanggilan tool dikirimkan secara non-blocking ke antrean keluaran aman utas (*thread-safe UI queue*).
2. Utas utama UI (UI Thread) secara periodik melakukan polling pada antrean tersebut dan memperbarui objek `rich.live.Live` secara asinkron.
3. Pendekatan ini menjamin status bar persisten di baris paling bawah terminal tidak akan tertimpa, bergeser, atau pecah saat AI sedang menulis draf laporan secara langsung.

### 4.6 Live Tool Call Display

Setiap agent/tool yang dipanggil AI ditampilkan secara transparan di dalam panel Thinking atau Chapter yang sedang aktif. User bisa melihat persis apa yang dikerjakan sistem.

```
 ╭─ Langkah 1 — Membaca Dokumen ───────────────────────────────╮
 │  ⠸  read_file("PK_2026.docx")                               │
 │  ✓  read_file                    selesai, 28 hal            │
 │  ⠸  extract_indicators(doc)                                 │
 │  ✓  extract_indicators           18 item                    │
 │  ⠸  compare_with_iku(indicators, iku_doc)                   │
 ╰─────────────────────────────────────────────────────────────╯
```

---

## 5. Slash Command System

### 5.1 Activation dan Popup Menu

Saat user mengetik `/` di REPL, sistem langsung menampilkan **popup menu** di atas prompt:

```
╭─ Perintah ──────────────────────────────────────────────────╮
│  /help            Bantuan kontekstual                       │
│  /status          Status project                            │
│  /scan            Baca folder dokumen                       │
│  /cek-indikator   Review mutu indikator                     │
│  /cek-cascading   Review logika cascading                   │
│  /review-pk       Review Perjanjian Kinerja                 │
│  /review-lkjip    Review LKjIP                              │
│  /cek-evidence    Audit bukti dukung                        │
│  /draft           Buat draft dokumen                        │
│  /report          Buat laporan                              │
│  /token           Penggunaan token                          │
│  /model           Ganti model AI                            │
│  /config          Pengaturan                                │
│  /clear           Bersihkan layar                           │
│  /exit            Keluar                                    │
╰─────────────────────────────────────────────────────────────╯
sakipro ❯ /
```

### 5.2 Fuzzy Filter saat Mengetik

Saat user melanjutkan mengetik setelah `/`, daftar difilter secara real-time:

```
sakipro ❯ /cek

╭─ Perintah ──────────────────────────────────────────────────╮
│  /cek-indikator   Review mutu indikator         [Ctrl+I]    │
│  /cek-cascading   Review logika cascading       [Ctrl+G]    │
│  /cek-pohon       Visualisasi pohon kinerja                 │
│  /cek-evidence    Audit bukti dukung                        │
╰─────────────────────────────────────────────────────────────╯
```

### 5.3 Ghost Text (Inline Autocomplete)

Setelah 2-3 karakter, tampilkan sisa perintah sebagai **ghost text** berwarna abu-abu:

```
sakipro ❯ /rev██iew-pk
```

Karakter yang sudah diketik berwarna putih, ghost text berwarna `grey50`. Tekan `→` atau `Tab` untuk accept.

### 5.4 Parameter Hint

Setelah slash command dipilih, tampilkan hint parameter:

```
sakipro ❯ /draft 

  Usage: /draft [jenis]
  Pilihan: rekomendasi-indikator | narasi-lkjip | matriks-lhe | catatan-pk
  Contoh: /draft narasi-lkjip
```

Hint tampil di bawah prompt, terhapus saat user mulai mengetik parameter.

### 5.5 Slash Command Reference Lengkap

| Command | Deskripsi | Keyboard Shortcut |
|---------|-----------|-------------------|
| `/help` | Bantuan kontekstual | `?` |
| `/status` | Status project dan dokumen | `Ctrl+S` |
| `/scan [folder]` | Indeks ulang dokumen | — |
| `/cek-indikator` | Review mutu indikator | `Ctrl+I` |
| `/cek-cascading` | Review logika sasaran-program | `Ctrl+G` |
| `/cek-pohon` | Visualisasi pohon kinerja | — |
| `/review-pk [file]` | Review Perjanjian Kinerja | `Ctrl+P` |
| `/review-lkjip [file]` | Review LKjIP | `Ctrl+L` |
| `/cek-evidence` | Audit bukti dukung | — |
| `/draft [jenis]` | Buat draft dokumen | — |
| `/task [deskripsi]` | Task panjang multi-langkah | — |
| `/report [jenis]` | Generate laporan | — |
| `/token` | Penggunaan token dan biaya | — |
| `/model [list\|switch\|info]` | Manajemen model AI | — |
| `/privacy [mode]` | Atur privacy mode | — |
| `/config [key] [value]` | Atur konfigurasi | — |
| `/output` | Buka folder output | — |
| `/resume` | Lanjutkan session sebelumnya | — |
| `/history` | Riwayat perintah session ini | — |
| `/clear` | Bersihkan layar | `Ctrl+L` |
| `/exit` | Keluar | `Ctrl+D` |

---

## 6. Autocomplete System (Tiga Lapisan)

### 6.1 Shell-Level Autocomplete

Didaftarkan ke shell (Bash, Zsh, Fish, PowerShell) via shellingham + Typer completion.

```bash
sakipro rev<TAB>
# → review-pk    review-lkjip
```

Install:

```bash
sakipro --install-completion   # otomatis deteksi shell
```

### 6.2 REPL-Level Slash Autocomplete

Dalam REPL (mode default `sakipro`), autocomplete bekerja secara real-time menggunakan `prompt_toolkit.completion.Completer`.

Sistem autocomplete memiliki tiga behavior:

**A. Popup Dropdown** — saat user mengetik `/ce`:

```
      ╭──────────────────────────────────────────────╮
      │  /cek-indikator  Review mutu indikator       │
    ❯ │  /cek-cascading  Review logika sasaran       │
      │  /cek-evidence   Audit bukti dukung          │
      ╰──────────────────────────────────────────────╯
sakipro ❯ /ce
```

**B. Ghost Text** — saat ada satu kandidat dominan:

```
sakipro ❯ /review-pk█████-lkjip
```

**C. Context Hint** — setelah perintah dipilih:

```
sakipro ❯ /review-pk 
   ⓘ  Pilih file: PK_2026.docx (ditemukan) atau ketik nama file lain
```

### 6.3 Context Autocomplete (Berbasis Dokumen)

Setelah `/scan` berhasil, REPL mengetahui nama-nama indikator dan file. Autocomplete menjadi "sadar konteks":

```
sakipro ❯ cek indikator <TAB>
╭──────────────────────────────────────────────────────╮
│  Persentase sekolah bermutu baik    [IKU_OPD.docx]   │
│  Nilai SAKIP OPD                    [PK_2026.docx]   │
│  Angka Partisipasi Sekolah          [Renstra.docx]   │
│  Jumlah pelatihan guru              [Renja_2026.xlsx]│
╰──────────────────────────────────────────────────────╯
```

```
sakipro ❯ review file <TAB>
╭────────────────────────────────────────────────────╮
│  PK_2026.docx                                      │
│  LKjIP_2025.docx                                   │
│  IKU_OPD.docx                                      │
│  Renstra_OPD.docx                                  │
╰────────────────────────────────────────────────────╯
```

---

## 7. Progress System

### 7.1 Spinner untuk Operasi Singkat

Untuk operasi di bawah 3 detik, gunakan spinner teks:

```
 ⠸  Membaca PK_2026.docx...
 ⠹  Mengekstrak indikator...
 ✓  12 indikator ditemukan
```

Tipe spinner: `dots`, `dots2`, `line` (pilih berdasarkan terminal capability).

### 7.2 Progress Bar untuk Operasi Panjang

Untuk operasi multi-file atau analisis panjang:

```
 Memindai dokumen OPD                    ━━━━━━━━━━░░░░░░░░░░  45%  4/9 files
 Mengekstrak indikator                   ━━━━━━━━━━━━━━━━━━░░  87%
 Estimasi selesai dalam: ~12 detik
```

### 7.3 Multi-Step Progress (Chapter System)

Untuk task kompleks seperti `/review-pk`, tampilkan progress per chapter:

```
═══════════════════ REVIEW PERJANJIAN KINERJA ═══════════════════

 [CHAPTER 1: PERSIAPAN DOKUMEN] ─────────────────────────────────
  ✓  Membaca PK_2026.docx               (12 sasaran, 28 halaman)
  ✓  Membaca IKU_OPD.docx              (15 indikator)
  ✓  Membaca Renstra_OPD.docx          (5 tujuan, 12 sasaran)

 [CHAPTER 2: EKSTRAKSI DATA] ────────────────────────────────────
  ✓  Mengekstrak sasaran PK             12 sasaran
  ✓  Mengekstrak indikator PK           18 indikator
  ✓  Mengekstrak target PK              18 target
  ⠸  Membandingkan dengan IKU...

 [CHAPTER 3: ANALISIS AI] ───────────────────────────────────────
  ⠹  Mengirim ke gpt-4o  (estimasi 15.000 token)...
```

### 7.4 Live Token Counter

Selama AI memproses, tampilkan token yang dikonsumsi secara live:

```
 ⠸  gpt-4o sedang menganalisis...   [token: 12.450 / ~18.000]
```

---

## 8. Output Display System

### 8.1 Summary Panel

Setiap command utama menghasilkan **summary panel** yang ringkas terlebih dahulu:

```
╭─ Review PK — Ringkasan ──────────────────────────────────────╮
│  Dokumen PK    : PK_2026.docx                                │
│  Sasaran       : 5  │  Indikator  : 12  │  Target : 12       │
│  Target Valid  : 10  │  Konflik   : 2                        │
│  Status        : ⚠ PERLU CEK                                 │
│  Waktu         : 18 detik  │  Token : 14.200  │  Biaya: Rp 4k│
╰──────────────────────────────────────────────────────────────╯
```

### 8.2 Severity-Coded Panels

Temuan dikategorikan dan diberi warna border sesuai urgensi:

```
╭─ KRITIS ─ Inkonsistensi Target Fatal ──────────────── [red] ─╮
│  Indikator "Nilai SAKIP OPD"                                 │
│  Target di PK      : 75 poin                                 │
│  Target di IKU     : 80 poin                                 │
│  Target di Renstra : 78 poin                                 │
│  → Tiga dokumen berbeda. Tentukan satu angka acuan.          │
╰──────────────────────────────────────────────────────────────╯

╭─ PERHATIAN ─ Indikator Tidak Outcome ────────────── [yellow] ╮
│  "Jumlah pelatihan guru" (Renja_2026.xlsx)                   │
│  Jenis saat ini : Aktivitas                                  │
│  Saran          : Ganti ke "Persentase guru bersertifikat"   │
│  Alasan         : Mengukur output kegiatan, bukan hasil.     │
╰──────────────────────────────────────────────────────────────╯

╭─ DRAFT AI ─ Usulan Rumusan Baru ─────────────────── [green] ╮
│  Original : "Jumlah pelatihan guru yang dilaksanakan"        │
│  DRAFT AI : "Persentase guru yang meningkat kompetensinya    │
│              setelah mengikuti pelatihan"                    │
│  Confidence : 78%  │  Status : DRAFT — perlu validasi manual │
╰──────────────────────────────────────────────────────────────╯
```

### 8.3 Tabel Hasil

```
 Review Indikator OPD — DISDIK_2026

 ┌────┬────────────────────────────────┬───────────┬────────────────┬─────────────────────┐
 │ No │ Indikator                      │ Jenis     │ Status         │ Saran               │
 ├────┼────────────────────────────────┼───────────┼────────────────┼─────────────────────┤
 │  1 │ Nilai SAKIP OPD                │ Outcome   │ ✓ OK           │ —                   │
 │  2 │ Jumlah pelatihan guru          │ Aktivitas │ ✗ Tidak Outcome│ Ganti ke persentase │
 │  3 │ Persentase sekolah bermutu     │ Outcome   │ ⚠ Formula kurang│ Lengkapi formula   │
 │  4 │ Jumlah dokumen SAKIP lengkap   │ Output    │ ✗ Tidak Outcome│ Ukur dampak layanan │
 └────┴────────────────────────────────┴───────────┴────────────────┴─────────────────────┘

 ✗ 8 dari 18 indikator perlu revisi  •  ⚠ 5 formula belum lengkap
```

### 8.4 Tree View (Pohon Kinerja)

```
 Pohon Kinerja OPD — DISDIK_2026
 ────────────────────────────────────────────────────
 Misi OPD: Meningkatkan mutu pendidikan dasar
 │
 ├── Sasaran 1: Meningkatnya mutu layanan pendidikan  ✓
 │   ├── Indikator: Persentase sekolah bermutu        ✓
 │   ├── Program: Program Pengelolaan Pendidikan
 │   │   └── Kegiatan: Pembinaan SMP                 ✓
 │   └── Evidence: 3 dokumen ditemukan               ✓
 │
 └── Sasaran 2: Meningkatnya tata kelola
     ├── Indikator: Nilai SAKIP OPD                  ✓
     ├── Program: Program Penunjang Urusan            ✓
     └── Kegiatan: Pelatihan Operator                ⚠ [rantai putus]
         └── ⚠ Belum terhubung ke sasaran outcome
```

### 8.5 Diff View untuk Saran Perubahan

Ketika AI menyarankan perbaikan teks dokumen, tampilkan sebagai diff:

```
 Saran Perbaikan — Rumusan Indikator PK

 ─── Original ────────────────────────────────────────────
 - Jumlah sekolah yang mendapatkan pembinaan mutu
 ─────────────────────────────────────────────────────────

 +++ Saran AI (DRAFT) ────────────────────────────────────
 + Persentase sekolah yang meningkat akreditasinya menjadi
 + minimal B setelah program pembinaan mutu
 ─────────────────────────────────────────────────────────

 Simpan ke draf laporan? [y/N/skip]
```

### 8.6 Inline Source References

Setiap klaim analisis AI disertai sumber dokumen:

```
 Analisis:

 Indikator "Nilai SAKIP OPD" sudah berorientasi outcome dan memiliki
 target yang konsisten di tiga dokumen.
     ↳ Sumber: IKU_OPD.docx [hal.4] · PK_2026.docx [hal.2] · Renstra [hal.8]

 Namun, tidak ditemukan formula pengukuran yang eksplisit.
     ↳ Sumber: IKU_OPD.docx [hal.4] — kolom "Formula" kosong
```

### 8.7 Muted Metadata Footer

Di bawah setiap output AI, tampilkan metadata secara redup:

```
 ─────────────────────────────────────────────────────────────────
 Model: gpt-4o  │  Confidence: 82%  │  Token: 14.200  │  Est. Biaya: Rp 4.200
 Status: DRAFT AI — validasi manual diperlukan sebelum digunakan
```

---

## 9. Interactive Decision Gates

Setelah setiap unit analisis, berikan **gerbang keputusan** kepada user:

```
 Temuan: 3 konflik target antara PK dan IKU.

 Apa yang ingin Anda lakukan?

   [1]  Simpan temuan ke draf laporan          (rekomendasi)
   [2]  Tampilkan detail konflik
   [3]  Buat saran perbaikan otomatis (AI)
   [4]  Lewati temuan ini
   [5]  Batalkan review

 Pilih [1-5] atau tekan Enter untuk simpan:
```

---

## 10. Plan Mode (Execution Preview)

Sebelum menjalankan task berat, tampilkan **rencana eksekusi** dan minta konfirmasi:

```
╭─ Execution Plan ────────────────────────────────────────────╮
│                                                             │
│  Task: Review menyeluruh dokumen SAKIP OPD                  │
│                                                             │
│  Langkah 1: Scan folder ./Dokumen_SAKIP_DisDik              │
│             3 DOCX, 1 PDF, 2 XLSX                           │
│  Langkah 2: Ekstrak indikator dari semua dokumen            │
│             Estimasi: ~5 detik                              │
│  Langkah 3: Review indikator (18 unit)         [gpt-4o]     │
│             Estimasi: ~45.000 token                         │
│  Langkah 4: Review PK dan bandingkan           [gpt-4o]     │
│             Estimasi: ~15.000 token                         │
│  Langkah 5: Cek cascading sasaran-program      [gpt-4o]     │
│             Estimasi: ~10.000 token                         │
│  Langkah 6: Generate laporan Markdown + XLSX                │
│             Output: 3 files                                 │
│                                                             │
│  Total estimasi token : 70.000                              │
│  Total estimasi biaya : Rp 21.000                           │
│  Total estimasi waktu : ~3 menit                            │
│                                                             │
╰─────────────────────────────────────────────────────────────╯

Lanjutkan eksekusi? [y/n/edit]
  y = Jalankan sesuai rencana
  n = Batalkan
  e = Edit rencana (pilih langkah mana saja)
```

---

## 11. Smart Help System

### 11.1 Help Kontekstual per Fase

`/help` menampilkan saran berbeda tergantung state sistem:

**State: Belum ada workspace**

```
╭─ Memulai SAKIPRO ───────────────────────────────────────────╮
│  Belum ada workspace aktif.                                 │
│                                                             │
│  Langkah yang disarankan:                                   │
│  1. sakipro init                → setup workspace baru      │
│  2. sakipro wizard              → panduan langkah demi langkah│
│  3. /scan ./folder_dokumen      → langsung baca dokumen     │
╰─────────────────────────────────────────────────────────────╯
```

**State: Setelah scan selesai**

```
╭─ Dokumen sudah terindeks — Apa selanjutnya? ────────────────╮
│                                                             │
│  Disarankan:                                                │
│  1. /cek-indikator    Periksa mutu 18 indikator             │
│  2. /review-pk        Review Perjanjian Kinerja             │
│  3. /status           Lihat ringkasan dokumen lengkap       │
│                                                             │
│  Tanya langsung: "apa masalah utama dokumen SAKIP saya?"    │
╰─────────────────────────────────────────────────────────────╯
```

### 11.2 Typo Detection

```bash
sakipro cek-indkator
```

```
╭─ Perintah Tidak Ditemukan ─────────────────────────────────╮
│  Input    : cek-indkator                                    │
│                                                             │
│  Maksud Anda?                                               │
│    1. cek-indikator   (jarak edit: 1)                       │
│    2. cek-cascading                                         │
│    3. ask "cek indikator"                                   │
╰─────────────────────────────────────────────────────────────╯
```

### 11.3 Quick Help Inline

Tekan `?` di mana saja dalam REPL:

```
sakipro ❯ ?

Perintah cepat:  /help /status /scan /cek-indikator /review-pk
Tanya AI:        Tulis pertanyaan dalam bahasa natural
Slash command:   Ketik / untuk menu lengkap
Keluar:          Ctrl+D atau /exit
```

---

## 12. Wizard Mode

### 12.1 Aktivasi

```bash
sakipro wizard
```

### 12.2 Main Menu Wizard

```
╭─ SAKIPRO Wizard ────────────────────────────────────────────╮
│                                                             │
│  Apa yang ingin Anda kerjakan hari ini?                     │
│                                                             │
╰─────────────────────────────────────────────────────────────╯

  Pekerjaan:

  ❯  1. Baca folder dokumen SAKIP OPD
     2. Cek mutu indikator kinerja
     3. Review Perjanjian Kinerja (PK)
     4. Review LKjIP
     5. Cek cascading sasaran & program
     6. Audit bukti kinerja (evidence)
     7. Buat laporan perbaikan akhir
     8. Tanya SAKIPRO bebas
     9. Keluar
```

Gunakan `↑↓` untuk navigasi, `Enter` untuk pilih.

### 12.3 Wizard Flow per Pekerjaan

Setiap pilihan mengikuti alur:

```
1. Konfirmasi dokumen/folder yang akan diproses
2. Tampilkan estimasi token dan biaya
3. Minta konfirmasi: [y/n/back]
4. Tampilkan progress real-time (chapter system)
5. Tampilkan ringkasan hasil
6. Tawarkan: simpan laporan / langkah berikutnya / wizard menu
```

---

## 13. Natural Language Command

SAKIPRO menerima perintah bahasa natural dan memetakannya ke command inti.

Input:

```
sakipro "tolong cek indikator saya"
sakipro "review PK tahun 2026"
sakipro "apa kelemahan LKjIP saya?"
```

Output:

```
╭─ Interpretasi Perintah ────────────────────────────────────╮
│  Input   : "review PK tahun 2026"                          │
│  Dipahami: sakipro review-pk --file PK_2026.docx           │
│  Keyakinan: 94%                                            │
╰─────────────────────────────────────────────────────────────╯

Lanjutkan?  [1] Ya   [2] Pilih perintah lain   [3] Batalkan
```

---

## 14. Token & Cost Awareness System

### 14.1 Pre-Task Warning

Sebelum task yang menggunakan lebih dari `ask_confirmation_above_tokens`:

```
╭─ Konfirmasi Token ──────────────────────────────────────────╮
│  Task ini membutuhkan model reasoning.                      │
│  Estimasi token   : 80.000                                  │
│  Estimasi biaya   : Rp 24.000                               │
│                                                             │
│  [1] Lanjutkan dengan gpt-4o          (Rp 24.000)          │
│  [2] Gunakan gemini-flash              (Rp 3.200 — hemat)   │
│  [3] Batalkan                                               │
╰─────────────────────────────────────────────────────────────╯
```

### 14.2 Token Budget Warning

Saat token bulanan mencapai 80%:

```
╭─ Token Warning ─────────────────────────────────────────────╮
│  ⚠  Token bulanan sudah 82%.                                │
│  Sisa estimasi : ~180.000 token                             │
│  Saran         : Gunakan gemini-flash untuk task ringan.    │
╰─────────────────────────────────────────────────────────────╯
```

### 14.3 /token Dashboard

```
╭─ Token Usage & Cost — Mei 2026 ─────────────────────────────╮
│  Hari ini       : 18.420 token                              │
│  Minggu ini     : 89.300 token                              │
│  Bulan ini      : 412.900 / 1.000.000 token  [41%]         │
│  Estimasi biaya : Rp 96.000                                 │
│                                                             │
│  Distribusi Model:                                          │
│  ████████████████░░░░  gemini-flash   320.000 (77%)         │
│  ████░░░░░░░░░░░░░░░░  gpt-4o         82.000  (20%)         │
│  █░░░░░░░░░░░░░░░░░░░  claude-sonnet  10.900  (3%)          │
│                                                             │
│  Top Commands:                                              │
│  /cek-indikator    45.200 token  (11%)                      │
│  /review-pk        38.100 token  (9%)                       │
│  /review-lkjip     31.400 token  (8%)                       │
╰─────────────────────────────────────────────────────────────╯
```

---

## 15. Error & Recovery System

### 15.1 Error Panel

```
╭─ Error ─────────────────────────────────────────────────────╮
│  ✗  PDF gagal dibaca                                        │
│  File    : LHE_2025_scan.pdf                                │
│  Penyebab: File hasil scan tanpa text layer (gambar saja)   │
│  Saran   :                                                  │
│    1. Aktifkan OCR: sakipro doctor --enable-ocr             │
│    2. Atau gunakan PDF dengan text layer                    │
│    3. Atau jalankan tanpa file ini: /scan --skip-errors     │
╰─────────────────────────────────────────────────────────────╯
```

### 15.2 API Error dengan Recovery

```
╭─ API Error ─────────────────────────────────────────────────╮
│  ✗  Gagal terhubung ke OpenAI                               │
│  Kode    : 429 Rate Limit Exceeded                          │
│  Saran   :                                                  │
│    1. Tunggu 30 detik lalu coba lagi  [otomatis dalam 28s]  │
│    2. Ganti ke model hemat: /model switch gemini-flash      │
│    3. Cek status API: sakipro doctor                        │
╰─────────────────────────────────────────────────────────────╯

 Retry otomatis dalam: 28 ⠸
```

### 15.3 Interrupt Handling

Saat user menekan `Ctrl+C` di tengah proses:

```
 ✗  Task dibatalkan oleh user

 Progres yang sudah selesai:
   ✓  Scan dokumen         (9 files)
   ✓  Ekstrak indikator    (18 indikator)
   ✗  Review AI            (dibatalkan di langkah 3)

 Lanjutkan dari langkah 3?  [y/N]
```

---

## 16. Privacy & Security Display

### 16.1 Privacy Warning Standar

```
╭─ Privacy Notice ────────────────────────────────────────────╮
│  Dokumen mengandung kemungkinan data sensitif (NIK, NIP).   │
│  Mode aktif  : standard                                     │
│  Tindakan    : Data sensitif akan di-mask sebelum dikirim   │
│                ke API cloud.                                │
│  File asli   : tidak diubah, tidak dikirim utuh             │
╰─────────────────────────────────────────────────────────────╯
```

### 16.2 Privacy Mode Strict

```
╭─ Diblokir — Privacy Mode Strict ───────────────────────────╮
│  ✗  Dokumen ini tidak dikirim ke AI cloud.                 │
│  File    : Data_ASN_Rahasia.xlsx                           │
│  Alasan  : Privacy mode strict aktif                       │
│  Saran   : Ubah ke mode standard dengan:                   │
│            sakipro privacy set standard                    │
╰────────────────────────────────────────────────────────────╯
```

---

## 17. Keyboard Shortcuts

### 17.1 Shortcuts REPL Mode

```
Input & Navigation:
  Enter          Kirim perintah
  Alt+Enter      Newline dalam input (multi-line)
  ↑ / ↓          Navigasi riwayat command
  ← / →          Gerak kursor kiri/kanan
  Ctrl+A         Ke awal baris
  Ctrl+E         Ke akhir baris
  Ctrl+W         Hapus kata sebelumnya
  Tab            Accept autocomplete / ghost text
  →              Accept ghost text (inline)

Perintah Cepat:
  /              Buka slash command menu
  ?              Quick help inline
  Ctrl+I         /cek-indikator
  Ctrl+P         /review-pk
  Ctrl+L         Bersihkan layar
  Ctrl+S         /status
  Ctrl+G         /cek-cascading

Session:
  Ctrl+C         Batalkan proses yang berjalan
  Ctrl+D         Keluar (konfirmasi jika task aktif)
  Ctrl+R         Cari riwayat command (incremental search)
```

### 17.2 Shortcuts Wizard Mode

```
  ↑ / ↓          Navigasi menu
  Enter          Pilih item
  Esc / Q        Kembali ke menu sebelumnya
  Ctrl+D         Keluar wizard
```

---

## 18. Workbench Mode

```bash
sakipro workbench
```

Layout terminal split menggunakan `rich.layout.Layout`:

```
╭──────────────────────────── SAKIPRO WORKBENCH ────────────────────────────╮
│ DISDIK_2026  •  gpt-4o  •  standard  •  412.900 token          Mei 2026   │
├─────────────────────┬─────────────────────────────────────────────────────┤
│ MENU                │ PANEL UTAMA                                         │
│                     │                                                     │
│ [1] Dokumen         │ Ringkasan Status OPD                                │
│ [2] Indikator       │                                                     │
│ [3] Cascading       │  ┌──────────────────┬──────────────────────────┐    │
│ [4] PK              │  │ Area             │ Status                   │    │
│ [5] LKjIP           │  ├──────────────────┼──────────────────────────┤    │
│ [6] Evidence        │  │ Indikator        │ ⚠  PERLU REVISI (8/18)  │     │
│ [7] Laporan         │  │ PK               │ ⚠  PERLU CEK   (2 konflik)│   │
│ [8] Token           │  │ LKjIP            │ ○  Belum di-review       │    │
│ [9] Pengaturan      │  │ Evidence         │ ✗  KURANG      (4/24)    │    │
│                     │  │ Cascading        │ ○  Belum di-review       │    │
│ [/] Slash Command   │  └──────────────────┴──────────────────────────┘    │
│ [?] Bantuan         │                                                     │
│ [Q] Keluar          │  Ketik nomor menu atau command langsung             │
│                     │                                                     │
├─────────────────────┴─────────────────────────────────────────────────────┤
│  workbench ❯                                                              │
╰───────────────────────────────────────────────────────────────────────────╯
```

---

## 19. Resume Session

```bash
sakipro resume
```

```
╭─ Session Sebelumnya ────────────────────────────────────────╮
│  Proyek    : DISDIK_2026                                    │
│  Task      : Review menyeluruh dokumen SAKIP                │
│  Progress  : 5 dari 7 langkah selesai                       │
│  Terakhir  : Kemarin, 15:42                                 │
│  Menunggu  : Audit evidence (langkah 6)                     │
╰─────────────────────────────────────────────────────────────╯

Lanjutkan?  [1] Ya   [2] Mulai dari awal   [3] Batalkan
```

---

## 20. Output Naming & Path Display

Setiap file output ditampilkan dengan path lengkap dan bisa dibuka:

```
╭─ Output Berhasil Dibuat ────────────────────────────────────╮
│  ✓  outputs/02_REVIEW_INDIKATOR.xlsx                        │
│  ✓  outputs/04_REVIEW_PK.md                                 │
│                                                             │
│  Buka folder output?  [y/N]                                 │
╰─────────────────────────────────────────────────────────────╯
```

Konvensi penamaan output:

```
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

## 21. Rekomendasi Berikutnya — Wajib di Setiap Respons

Ini adalah **fitur wajib** yang tidak boleh dihilangkan. Setiap respons SAKIPRO — baik dari slash command maupun dari chat natural language — **selalu** diakhiri dengan blok rekomendasi.

### 21.1 Format Standar

Blok rekomendasi muncul setelah setiap respons selesai, dipisahkan oleh garis pemisah tipis:

```
 ─────────────────────────────────────────────────────────────
 Selanjutnya, Anda bisa:

   /review-pk         Review PK (ada 2 konflik yang perlu dicek)
   /cek-cascading     Cek apakah indikator terhubung ke program
   apa prioritas perbaikan yang paling mendesak?

sakipro ❯ 
```

REPL prompt langsung muncul setelah blok rekomendasi. User bisa memilih dengan mengetik ulang perintah, atau langsung bertanya hal lain.

### 21.2 Rekomendasi Berbasis Konteks

Saran **bukan** daftar statis. Isinya berubah berdasarkan situasi:

**Setelah /scan berhasil:**

```
 Selanjutnya, Anda bisa:

   /cek-indikator     Periksa mutu 18 indikator yang ditemukan
   /review-pk         Review Perjanjian Kinerja (PK_2026.docx ada)
   apa dokumen yang paling bermasalah?
```

**Setelah /cek-indikator menemukan masalah:**

```
 Selanjutnya, Anda bisa:

   /review-pk             Cek apakah 2 konflik target juga ada di PK
   /draft rekomendasi-indikator   Buat draft perbaikan 8 indikator
   tunjukkan indikator mana yang paling mudah diperbaiki duluan
```

**Setelah pertanyaan chat dijawab:**

```
 Selanjutnya, Anda bisa:

   /cek-indikator     Jalankan cek otomatis semua indikator
   tanya lebih lanjut tentang formula indikator outcome
   contohkan indikator outcome yang baik untuk OPD pendidikan
```

**Setelah semua review selesai:**

```
 Selanjutnya, Anda bisa:

   /report final      Buat laporan perbaikan akhir (semua review selesai)
   /draft rekomendasi-indikator   Buat draft perubahan indikator
   ringkaskan semua temuan dalam satu paragraf untuk laporan
```

### 21.3 Aturan Rekomendasi

1. Selalu tampilkan **tepat 3 rekomendasi** — tidak kurang, tidak lebih.
2. Minimal **1 slash command** dan **1 pertanyaan chat bahasa natural**.
3. Rekomendasi slash command disertai **alasan singkat dalam kurung**.
4. Pertanyaan chat ditulis apa adanya — bisa langsung disalin user.
5. Jika semua review sudah selesai, dorong ke `/report final`.
6. Jika ada temuan kritis, rekomendasi pertama selalu terkait temuan itu.

### 21.4 Sumber Data untuk Menentukan Rekomendasi

```python
get_contextual_suggestions(context: ReviewContext) -> list[Suggestion]:
    # Prioritas:
    # 1. Temuan kritis yang belum ditindaklanjuti
    # 2. Dokumen yang belum direview
    # 3. Tahap logis berikutnya dalam alur review SAKIP
    # 4. Pertanyaan natural yang relevan dengan temuan
```

---

## 22. Doctor Command

```bash
sakipro doctor
```

Output lengkap:

```
╭─ SAKIPRO Doctor ────────────────────────────────────────────╮
│                                                             │
│  System:                                                    │
│  ✓  Python 3.12.3                                           │
│  ✓  Terminal: Windows Terminal / iTerm2 / xterm-256color    │
│  ✓  Rich display: OK                                        │
│  ✓  prompt_toolkit: OK                                      │
│                                                             │
│  API Keys:                                                  │
│  ✓  OpenAI       : Configured [sk-proj-****...****]         │
│  ✓  Google AI    : Configured [AIza****...****]             │
│  ✗  Anthropic    : Not configured                           │
│                                                             │
│  Optional Features:                                         │
│  ✓  OCR (Tesseract): OK                                     │
│  ✗  LibreOffice    : Not found (PDF export tidak tersedia)  │
│                                                             │
│  Workspace:                                                 │
│  ✓  Config file    : ~/.sakipro/config.yaml                 │
│  ✓  Database       : ~/.sakipro/sakipro.db (2.4 MB)         │
│  ✓  Logs           : ~/.sakipro/logs/                       │
│  ✓  Outputs        : ./outputs/                             │
│                                                             │
│  Status: ✓ Siap digunakan (1 warning)                       │
╰─────────────────────────────────────────────────────────────╯
```

---

## 23. Color & Theme System

### 23.1 Palet Warna

```python
# sakipro/ui/theme.py

THEME = {
    "primary":     "cyan",
    "secondary":   "bright_cyan",
    "success":     "green",
    "warning":     "yellow",
    "error":       "red",
    "critical":    "bright_red",
    "info":        "blue",
    "muted":       "grey50",
    "ghost":       "grey37",       # ghost text autocomplete
    "ai_agent":    "magenta",
    "document":    "cyan",
    "evidence":    "green",
    "draft":       "green",
    "risk_high":   "red",
    "risk_medium": "yellow",
    "risk_low":    "green",
    "chapter":     "bright_white",
    "prompt":      "cyan",
}
```

### 23.2 Panel Border Style

```python
PANEL_STYLE = {
    "summary":   "cyan",
    "critical":  "red",
    "warning":   "yellow",
    "draft":     "green",
    "info":      "blue",
    "error":     "red",
    "success":   "green",
    "privacy":   "yellow",
    "token":     "blue",
}
```

### 23.3 Icon Mapping

```python
ICONS = {
    "success":   "✓",
    "error":     "✗",
    "warning":   "⚠",
    "info":      "ⓘ",
    "spinner":   "⠸",
    "project":   "📁",
    "document":  "📄",
    "evidence":  "🧾",
    "ai_agent":  "🤖",
    "score":     "★",
    "task":      "☐",
    "memory":    "🧠",
    "token":     "◉",
    "security":  "🔒",
}

# Safe fallback tanpa emoji (untuk terminal Windows lama)
ICONS_ASCII = {
    "success":   "[OK]",
    "error":     "[ERR]",
    "warning":   "[!]",
    "info":      "[i]",
}
```

---

## 24. Config UI

File: `~/.sakipro/config.yaml`

```yaml
ui:
  banner: full            # full | compact | none
  theme: dark
  use_emoji: true
  show_token_cost: true
  show_sources: true
  show_confidence: true
  show_next_steps: true
  compact_mode: false
  autocomplete: true
  ghost_text: true
  slash_commands: true
  wizard_enabled: true
  streaming: true
  status_bar: true
  live_tool_display: true
  diff_view: true
```

---

## 25. Module Structure

```
sakipro/ui/
  __init__.py          Export helper functions
  theme.py             Warna, ikon, style constants
  console.py           Rich Console singleton
  banner.py            print_banner(), print_compact_banner()
  panels.py            print_startup_panel(), print_summary_panel()
                       print_error_panel(), print_success_panel()
                       print_privacy_warning(), print_token_warning()
  tables.py            render_table(), render_indicator_table()
  tree.py              render_kinerja_tree()
  progress.py          spinner(), progress_bar(), chapter_header()
                       live_token_counter()
  diff.py              render_diff(), render_source_ref()
  repl.py              SAKIPROCompleter, ghost_text_completer
                       run_repl(), build_keybindings()
  wizard.py            run_wizard(), wizard_menu()
  workbench.py         run_workbench(), build_layout()
  status_bar.py        build_status_bar()
  help.py              print_help(), print_contextual_help()
                       print_command_hint()
  suggestions.py       print_next_steps(), get_contextual_suggestions()
  plan_mode.py         show_execution_plan(), confirm_execution()
  decision_gates.py    show_decision_gate()
  streaming.py         stream_ai_response(), live_tool_display()
```

---

## 26. Helper Functions Wajib

```python
# Banner & Startup
print_banner(mode="full" | "compact" | "none")
print_startup_panel(workspace: WorkspaceState)
print_first_run_setup()

# Panels
print_summary_panel(title, fields: dict, status: str)
print_error_panel(error: SAKIPROError)
print_success_panel(message, file_outputs: list)
print_privacy_warning(mode, filename)
print_token_warning(pct_used: float)

# Review Output
render_indicator_table(indicators: list[IndicatorResult])
render_pk_panel(pk_result: PKReviewResult)
render_kinerja_tree(tree: KinerjaTree)
render_diff(original: str, suggestion: str, confidence: float)
print_source_refs(sources: list[SourceRef])
print_muted_footer(model, confidence, tokens, cost)

# Severity Panels
print_critical_panel(finding: Finding)
print_warning_panel(finding: Finding)
print_draft_panel(draft: DraftResult)

# Progress
chapter_header(chapter_name: str, description: str)
spinner_context(message: str)   # as context manager
progress_bar(total: int, label: str)
live_token_counter(initial: int)

# Interactive
show_execution_plan(plan: ExecutionPlan) -> bool
show_decision_gate(options: list[str]) -> int
stream_ai_response(response_stream, panel_title: str)
live_tool_display(tool_calls: list[ToolCall])

# Smart UX
print_next_steps(context: ReviewContext)
print_contextual_help(state: WorkspaceState)
print_natural_language_interpretation(input: str, command: str, confidence: float)
print_typo_suggestion(input: str, candidates: list[str])

# Utility
format_token_count(n: int) -> str   # "18.420 token"
format_idr(amount: float) -> str    # "Rp 4.200"
format_status_badge(status: str) -> str
```

---

## 27. Library & Justifikasi

| Library | Versi | Fungsi | Keterangan |
|---------|-------|--------|------------|
| `rich` | ≥13 | Panel, Table, Tree, Progress, Live, Markdown, Syntax | Core UI engine |
| `prompt_toolkit` | ≥3.0 | REPL, autocomplete, ghost text, keybindings, status bar | Interactive input engine |
| `questionary` | ≥2.0 | Wizard menu, confirm, select, checkbox | User-friendly prompts |
| `typer` | ≥0.12 | CLI command routing, type hints, --help otomatis | Command framework |
| `shellingham` | ≥1.5 | Deteksi shell untuk install autocomplete | Shell integration |
| `pyyaml` | ≥6.0 | Parsing config.yaml | Config management |

Pembagian tanggung jawab yang ketat:

- `typer` → routing command, tidak boleh ada UI logic
- `rich` → semua rendering output, tidak boleh ada business logic
- `prompt_toolkit` → semua interactive input, tidak boleh ada rendering non-input
- `questionary` → semua wizard dan confirm prompt

---

## 28. Implementation Priority

### v1.0 Core — Wajib

- [ ] Banner startup + startup panel
- [ ] Project status display
- [ ] Quick command mode (semua command tanpa interactive)
- [ ] Rich progress bar (spinner + multi-step)
- [ ] Rich summary panel per command
- [ ] Rich error panel dengan saran
- [ ] Rich success panel dengan output path
- [ ] Token warning panel
- [ ] Privacy warning panel
- [ ] Suggested next steps di akhir setiap command
- [ ] Help system (`--help` dan `/help` kontekstual)
- [ ] Doctor command
- [ ] Output path display
- [ ] Natural language command basic (→ minta konfirmasi sebelum jalankan)

### v1.0 Expanded — Should Have

- [ ] Interactive REPL sebagai default mode `sakipro` (prompt_toolkit)
- [ ] Slash command popup menu + fuzzy filter
- [ ] Ghost text autocomplete
- [ ] Thinking & Step Mode display (panel thinking + chapter system)
- [ ] Streaming AI response via `rich.live`
- [ ] Live tool call display dalam panel thinking
- [ ] Rekomendasi berikutnya wajib di setiap akhir respons
- [ ] Wizard mode (questionary)
- [ ] Status bar persisten
- [ ] Plan mode (execution preview + konfirmasi)
- [ ] Decision gates di akhir analisis unit
- [ ] Diff view untuk saran perbaikan
- [ ] Severity-coded panels (critical/warning/draft)
- [ ] Inline source references
- [ ] Report preview (`sakipro report preview`)

### Post-v1.0 — Nice to Have

- [ ] Workbench mode (split layout)
- [ ] Context autocomplete berbasis dokumen (indikator, nama file)
- [ ] Resume session
- [ ] Live token counter real-time
- [ ] Theme switching
- [ ] Task board (`/task`)
- [ ] Command palette (Ctrl+P)
- [ ] History search (Ctrl+R)
- [ ] Notification system non-blocking

---

## 29. Acceptance Criteria

CLI dianggap selesai untuk v1.0 Core jika semua kondisi ini terpenuhi:

1. `sakipro` (tanpa argumen) langsung menampilkan banner + status panel + REPL prompt — tanpa subcommand tambahan.
2. Banner muncul tanpa error di Windows 10/11, macOS, Ubuntu.
3. REPL menerima slash command, pertanyaan natural language, dan perintah campur keduanya.
4. Mengetik `/` di REPL langsung memunculkan popup menu daftar perintah.
5. Mengetik sebagian perintah memunculkan ghost text (autohint inline).
6. Thinking & Step Mode tampil saat AI memproses — user tidak pernah melihat layar diam.
7. Respons AI muncul streaming setelah thinking selesai.
8. Setiap respons diakhiri rekomendasi perintah atau chat berikutnya yang relevan.
9. `sakipro doctor` memberi status lengkap sistem dan API key.
10. Setiap command menampilkan progress real (spinner / progress bar / chapter).
11. Error ditampilkan dalam panel dengan penyebab dan saran solusi.
12. Token warning muncul saat >80% budget.
13. Privacy warning muncul sebelum data sensitif dikirim.
14. `--silent` menekan semua banner dan panel (output murni data).
15. Semua UI berjalan di Windows tanpa karakter rusak (safe unicode).
16. User biasa (non-teknis) bisa menyelesaikan review PK langsung dari REPL tanpa mengetahui subcommand apapun.

---

## 30. Developer Rules

1. **Pisahkan UI dari logic.** Module `ui/` tidak boleh import dari `agents/` atau `sakip/`. UI hanya menerima data struct yang sudah jadi.
2. **Semua output melalui helper.** Tidak boleh ada `print()` atau `console.print()` langsung di `cli/commands.py` atau `agents/`. Semua lewat `ui/` helpers.
3. **Setiap proses panjang pakai progress.** Gunakan `chapter_header()` + `spinner_context()` atau `progress_bar()`. Tidak boleh ada proses diam tanpa feedback.
4. **Setiap error lewat `print_error_panel()`.** Format error konsisten, selalu ada saran perbaikan.
5. **Ghost text hanya untuk slash command.** Jangan aktifkan untuk input natural language — akan membingungkan user.
6. **Streaming aktif di REPL (default).** Mode satu-shot (`sakipro review-pk` tanpa REPL) tampilkan hasil setelah selesai, bukan streaming — karena tidak ada `rich.live` yang bisa di-refresh.
7. **Semua output AI diberi status DRAFT dan confidence.** Tidak ada output AI tanpa label status.
8. **Test UI di Windows PowerShell.** Target utama adalah laptop kantor Windows. Unicode fallback harus berfungsi.
9. **Emoji opsional via config.** Aktifkan `ui.use_emoji: false` untuk terminal yang tidak mendukung.
10. **Status bar hanya aktif di REPL mode.** Quick command mode tidak perlu status bar.

---

END OF CLI_BLUEPRINT.md
