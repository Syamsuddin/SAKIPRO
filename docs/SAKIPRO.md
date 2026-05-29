# SAKIPRO v1.0

AI CLI Agent untuk Kasubbag Perencanaan OPD

## 1. Definisi Singkat

SAKIPRO v1.0 adalah agen AI berbasis CLI untuk membantu Kasubbag Perencanaan OPD memperbaiki mutu dokumen SAKIP yang tersimpan di folder kerja.

SAKIPRO fokus pada pekerjaan praktis level OPD, seperti:

1. Membaca dokumen SAKIP OPD.
2. Mengecek mutu indikator.
3. Mengecek cascading.
4. Mengecek pohon kinerja.
5. Mereview Perjanjian Kinerja.
6. Mereview LKjIP.
7. Mengecek bukti dukung.
8. Menyusun rekomendasi perbaikan.
9. Membuat laporan hasil review.
10. Membantu task panjang secara bertahap.

SAKIPRO bukan sistem besar level kabupaten seperti SAKIPMAN.

SAKIPRO adalah asisten kerja harian Kasubbag Perencanaan OPD.

## 2. Positioning Produk

AI Planning Assistant for OPD SAKIP Documents (Review, Improve, Draft, Evidence, Report).

## 3. Target Pengguna

Pengguna utama:

1. Kasubbag Perencanaan OPD.
2. Staf perencanaan OPD.
3. Tim penyusun LKjIP OPD.
4. Operator SAKIP OPD.
5. Tim internal yang membantu review dokumen OPD.

Pengguna pendukung:

1. Sekretaris OPD.
2. Kepala OPD.
3. Inspektorat pembina.
4. Bagian Organisasi.
5. Bappeda pembina perencanaan.

## 4. Masalah yang Diselesaikan

Masalah umum di OPD:

1. Dokumen SAKIP tersebar di banyak folder.
2. Indikator masih banyak berupa output atau aktivitas.
3. Formula indikator belum jelas.
4. Target dalam PK tidak konsisten dengan IKU atau Renstra.
5. LKjIP banyak narasi, tetapi kurang analisis.
6. Evidence tidak terhubung dengan klaim kinerja.
7. Cascading belum logis.
8. Pohon kinerja belum menggambarkan sebab akibat.
9. Kasubbag Perencanaan harus mengecek banyak file secara manual.
10. Persiapan evaluasi sering dilakukan menjelang batas waktu.

## 5. Filosofi SAKIPRO

Prinsip utama:

Kasubbag Perencanaan tidak perlu menelusuri seluruh dokumen secara manual. SAKIPRO membaca folder kerja, memahami dokumen, menemukan kelemahan, memberi saran, lalu membuat laporan perbaikan.

Prinsip kerja:

1. Tidak mengubah file asli.
2. Semua hasil review dibuat sebagai file baru.
3. Semua rekomendasi harus berbasis dokumen.
4. Semua klaim harus memiliki sumber.
5. Semua output berstatus draft.
6. Finalisasi tetap dilakukan manusia.

## 6. Mode Operasi

SAKIPRO sebagai produk dirancang memiliki 5 mode utama. Untuk v0.2, Quick Command Mode wajib, Interactive Agent Mode dan Wizard Mode menjadi Should Have, sedangkan Workbench Mode dan Task Mode masuk Post-v1.0.

### 6.1 Quick Command Mode

Untuk pengguna yang sudah terbiasa terminal.

Contoh:

```bash
sakipro scan ./dokumen_sakip
sakipro cek-indikator
sakipro review-pk
sakipro ask "indikator mana yang belum punya sumber data?"
```

### 6.2 Interactive Agent Mode

Masuk melalui:

```bash
sakipro chat
```

Status v0.2: Should Have.

User bertanya secara natural:

```text
Apa kelemahan indikator OPD saya?
Review PK tahun 2026.
Cek apakah LKjIP saya sudah sesuai PK.
```

### 6.3 Wizard Mode

Masuk melalui:

```bash
sakipro wizard
```

Status v0.2: Should Have.

Cocok untuk user biasa yang tidak hafal command.

Menu utama:

1. Baca folder dokumen.
2. Cek mutu indikator.
3. Review PK.
4. Tanya SAKIPRO.
5. Keluar.

Menu review LKjIP, cascading, evidence, dan laporan akhir termasuk scope v1.0 Expanded.

### 6.4 Workbench Mode

Masuk melalui:

```bash
sakipro workbench
```

Status: Post-v1.0.

Menampilkan dashboard terminal berbasis Rich untuk melihat dokumen, indikator, PK, LKjIP, evidence, task, dan laporan.

### 6.5 Task Mode

Untuk pekerjaan panjang.

Contoh:

```bash
sakipro task "Review seluruh dokumen SAKIP OPD dan buat daftar perbaikan"
```

Status: Post-v1.0.

SAKIPRO memecah task menjadi:

1. Scan folder.
2. Ekstrak dokumen.
3. Cek indikator.
4. Cek cascading.
5. Review PK.
6. Review LKjIP.
7. Audit evidence.
8. Buat laporan final.

## 7. Command Inti SAKIPRO

Command produk penuh:

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
sakipro report
sakipro token
sakipro doctor
```

Command v1.0 Core:

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

## 8. Slash Command

Dalam mode chat dan workbench, SAKIPRO mendukung slash command. Untuk v0.2, slash command hanya wajib jika chat mode Should Have ikut dirilis; daftar lengkap berikut adalah target v1.0 Expanded dan Post-v1.0.

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

Tujuannya agar user biasa tidak perlu mengetik command panjang.

## 9. Autocomplete

SAKIPRO dirancang memiliki 3 jenis autocomplete. Untuk v1.0 Core, autocomplete tidak wajib. Basic command autocomplete berstatus Should Have, sedangkan context autocomplete masuk setelah scan dan retrieval stabil.

### 9.1 Shell Autocomplete

Contoh:

```bash
sakipro rev<TAB>
```

Menampilkan:

```text
review-pk
```

### 9.2 Slash Autocomplete

Dalam mode chat:

```text
/cek<TAB>
```

Menampilkan:

```text
/cek-indikator
```

### 9.3 Context Autocomplete

SAKIPRO membaca isi dokumen lalu memberi pilihan.

Contoh:

```text
cek indikator <TAB>
```

Menampilkan indikator yang ditemukan di dokumen OPD.

## 10. Agent Utama

SAKIPRO produk penuh memakai beberapa agent kecil. Untuk v1.0 Core, agent wajib adalah Folder Scanner Agent, Indicator Review Agent, PK Review Agent, dan OPD Planning Copilot Agent. Agent LKjIP, cascading, dan evidence termasuk scope v1.0 Expanded.

### 10.1 Folder Scanner Agent

Membaca folder kerja, mengenali dokumen, dan membuat daftar file.

### 10.2 Indicator Review Agent

Menilai indikator, formula, sumber data, baseline, target, dan jenis indikator.

### 10.3 Cascading Review Agent

Status: v1.0 Expanded.

Mengecek hubungan sasaran, indikator, program, kegiatan, subkegiatan, dan anggaran.

### 10.4 PK Review Agent

Mereview Perjanjian Kinerja, konsistensi target, sasaran, indikator, dan dukungan program.

### 10.5 LKjIP Review Agent

Status: v1.0 Expanded.

Mereview struktur LKjIP, analisis capaian, efisiensi, kegagalan, keberhasilan, dan tindak lanjut.

### 10.6 Evidence Review Agent

Status: v1.0 Expanded.

Mencari dan menilai bukti dukung untuk klaim kinerja.

### 10.7 OPD Planning Copilot Agent

Menjawab pertanyaan, memberi saran langkah kerja, dan membantu membuat draft.

## 11. Fungsi Utama

### 11.1 Scan Folder Dokumen

Command:

```bash
sakipro scan ./Dokumen_SAKIP_OPD
```

SAKIPRO mendeteksi:

1. Renstra.
2. Renja.
3. IKU.
4. PK.
5. LKjIP.
6. RKA.
7. DPA.
8. LHE.
9. Evidence.
10. Rencana Aksi.
11. Matriks tindak lanjut.

### 11.2 Cek Indikator

Command:

```bash
sakipro cek-indikator
```

Output:

1. Daftar indikator.
2. Jenis indikator.
3. Formula.
4. Sumber data.
5. Target.
6. Masalah.
7. Rekomendasi perbaikan.

### 11.3 Cek Cascading

Status: v1.0 Expanded.

Command:

```bash
sakipro cek-cascading
```

Output:

1. Relasi sasaran dengan indikator.
2. Relasi indikator dengan program.
3. Relasi program dengan kegiatan.
4. Rantai putus.
5. Kegiatan tidak relevan.
6. Rekomendasi perbaikan.

### 11.4 Cek Pohon Kinerja

Status: v1.0 Expanded.

Command:

```bash
sakipro cek-pohon
```

Output:

Pohon kinerja dalam tampilan terminal.

### 11.5 Review PK

Command:

```bash
sakipro review-pk
```

Cek:

1. Sasaran.
2. Indikator.
3. Target.
4. Satuan.
5. Konsistensi dengan IKU.
6. Konsistensi dengan Renstra.
7. Program pendukung.

### 11.6 Review LKjIP

Status: v1.0 Expanded.

Command:

```bash
sakipro review-lkjip
```

Cek:

1. Kesesuaian dengan PK.
2. Target dan realisasi.
3. Analisis keberhasilan.
4. Analisis kegagalan.
5. Analisis efisiensi.
6. Evidence.
7. Tindak lanjut.

### 11.7 Cek Evidence

Status: v1.0 Expanded.

Command:

```bash
sakipro cek-evidence
```

Cek:

1. Klaim kinerja.
2. Bukti terkait.
3. Bukti valid.
4. Bukti lemah.
5. Bukti kosong.
6. Rekomendasi bukti tambahan.

### 11.8 Draft Rekomendasi

Status: v1.0 Expanded.

Command:

```bash
sakipro draft rekomendasi-indikator
sakipro draft narasi-lkjip
sakipro draft tindak-lanjut-lhe
```

Output:

1. Draft narasi.
2. Draft rekomendasi.
3. Draft matriks.
4. Draft catatan review.

### 11.9 Token dan Cost

Command:

```bash
sakipro token
sakipro usage  # alias
```

Menampilkan pemakaian token dan estimasi biaya.

### 11.10 Model Management

Command:

```bash
sakipro model list
sakipro model switch
```

Mengelola model AI yang digunakan.

### 11.11 Config Management

Command:

```bash
sakipro config set-key
```

Menginput dan mengelola API Key dan konfigurasi.

## 12. Output File

SAKIPRO menghasilkan folder:

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
  sources.json
```

Output v0.2 dapat menambahkan review cascading, LKjIP, audit evidence, rekomendasi DOCX, dan daftar task perbaikan.

Format output:

1. Markdown.
2. XLSX.
3. DOCX.
4. JSON.
5. PDF, opsional.

## 13. Desain CLI Rich

SAKIPRO memakai tampilan terminal modern berbasis Rich.

Fitur UI:

1. Startup banner.
2. Panel status project.
3. Tabel hasil review.
4. Progress bar.
5. Error panel.
6. Success panel.
7. Suggested next steps.
8. Token warning.
9. Confidence score.
10. Source panel.
11. Privacy warning.
12. Help kontekstual.

Fitur Task board dan Workbench terminal masuk Post-v1.0.

## 14. Startup Banner

Banner utama:

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

Panel startup:

```text
Project       : DISDIK_2026
Folder        : ./dokumen_sakip
AI Provider   : OpenAI / Gemini / Claude
Privacy Mode  : standard
Documents     : 9 indexed
Evidence      : 32 files
Status        : Ready
```

## 15. Stack Software

Bahasa:

```text
Python 3.11 atau 3.12
```

CLI dan UI:

```text
Typer
Rich
Questionary, Should Have
prompt_toolkit, Should Have
```

AI API:

```text
LiteLLM
OpenAI API
Gemini API
Claude API
```

Dokumen:

```text
python-docx
docxtpl, Should Have untuk DOCX report sederhana
PyMuPDF
pdfplumber
openpyxl
pandas
```

Database lokal:

```text
SQLite
SQLAlchemy
```

Retrieval v0.2:

```text
SQLite FTS/BM25 atau keyword search
```

Vector search optional v0.2:

```text
ChromaDB atau FAISS
```

Graph sederhana:

```text
NetworkX
```

Status: optional v0.2.

Testing:

```text
pytest
ruff
```

## 16. Stack Hardware

Target utama adalah laptop kantor.

Minimum:

```text
CPU: 4 core
RAM: 8 GB
Storage: SSD 256 GB
Internet: wajib
GPU: tidak wajib
OS: Windows 10/11, macOS, atau Linux
```

Rekomendasi nyaman:

```text
CPU: 8 core
RAM: 16 GB
Storage: SSD 512 GB
Internet stabil
GPU tidak wajib
```

Karena SAKIPRO memakai AI API berbasis token, laptop kantor tidak perlu GPU.

## 17. Pola Distribusi dan Instalasi

SAKIPRO dikemas dari GitHub.

### 17.1 GitHub Release Executable

Untuk user umum.

Windows:

```text
sakipro-windows-x64.zip
```

macOS:

```text
sakipro-macos-arm64.tar.gz
sakipro-macos-x64.tar.gz
```

Linux:

```text
sakipro-linux-x64.tar.gz
```

Isi paket:

```text
sakipro.exe / sakipro
config.example.yaml
.env.example
templates/
install.ps1
install.sh
README_INSTALL.md
```

### 17.2 pipx Install

Untuk admin TIK dan user teknis.

```bash
pipx install git+https://github.com/NAMA-ORG/sakipro.git
```

### 17.3 Source Install

Untuk developer.

```bash
git clone https://github.com/NAMA-ORG/sakipro.git
cd sakipro
uv sync
uv run sakipro doctor
```

## 18. Struktur Folder Project

Struktur runtime user:

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

Struktur folder OPD:

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

## 19. Keamanan

Aturan keamanan:

1. API Key disimpan di file .env.
2. .env tidak boleh masuk Git.
3. File asli tidak diubah.
4. Hasil review disimpan sebagai file baru.
5. Data sensitif bisa dimasking.
6. Semua output berstatus draft.
7. User wajib menyetujui task mahal yang memakai banyak token.
8. Privacy mode tersedia.

Privacy mode:

```text
open
standard
strict
```

Default:

```text
standard
```

## 20. Token Management

SAKIPRO harus menampilkan pemakaian token.

Command:

```bash
sakipro token
```

Output:

```text
Hari ini        : 18.420 token
Bulan ini       : 412.900 token
Estimasi biaya  : Rp 96.000
Model terbanyak : claude-sonnet-4-20250514 (API Key Ready)
```

Jika task besar:

```text
Task ini memakai model reasoning.
Estimasi token : 80.000
Estimasi biaya : Rp 200.000
Lanjutkan?
```

## 21. Help System

SAKIPRO harus punya bantuan bertingkat.

Help umum:

```bash
sakipro --help
```

Help per command:

```bash
sakipro review-pk --help
```

Help interaktif:

```text
/help
```

Jika user salah ketik:

```text
Perintah tidak ditemukan: cek-indkator

Mungkin maksud Anda:
1. cek-indikator
2. cek-cascading
3. cek-evidence
```

## 22. Smart Suggestion

Setelah setiap proses, SAKIPRO memberi saran langkah berikutnya.

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
1. Perbaiki target yang tidak konsisten
2. Lengkapi sumber data indikator
3. Simpan hasil review PK sebagai draft
```

## 23. Roadmap SAKIPRO

### v1.0 Core

Fokus Core:

1. CLI dasar.
2. Scan folder.
3. Baca DOCX, PDF, XLSX.
4. Ask dokumen.
5. Cek indikator.
6. Review PK.
7. Source refs dan confidence.
8. Privacy mode standard dan strict.
9. Output Markdown dan XLSX.
10. Rich UI dasar.
11. Golden tests.
12. Help dasar.

### v1.0 Expanded

Tambahan:

1. Cek cascading.
2. Cek pohon kinerja.
3. Cek evidence.
4. Review LKjIP.
5. Draft rekomendasi.
6. Report final.
7. Token command.
8. Wizard dan chat yang lebih matang.
9. Autocomplete.
10. Vector search dan graph analysis.

### Post-v1.0

Tambahan:

1. Workbench mode.
2. Task mode.
3. Report DOCX penuh.
4. Slash command lengkap.
5. Resume session.

### Stable Release

Target stabil:

1. Siap dipakai Kasubbag Perencanaan OPD.
2. Installer GitHub Release tersedia.
3. Dokumentasi lengkap.
4. Template laporan tersedia.
5. Aman untuk laptop kantor.

## 24. Perbedaan SAKIPRO dan SAKIPMAN

SAKIPMAN:

1. Level kabupaten.
2. Multi OPD.
3. Multi user.
4. Platform besar.
5. Governance operating system.

SAKIPRO:

1. Level OPD.
2. Fokus Kasubbag Perencanaan.
3. CLI ringan.
4. Berjalan di laptop kantor.
5. Membaca folder dokumen.
6. Membantu review, perbaikan, dan laporan.

## 25. Positioning Final

SAKIPRO v1.0 adalah AI CLI Agent ringan untuk Kasubbag Perencanaan OPD yang membantu membaca folder dokumen SAKIP, bertanya berbasis dokumen, mengecek mutu indikator, mereview PK, mereview LKjIP, menilai cascading, mengaudit evidence, dan menghasilkan laporan perbaikan berbasis sumber secara cepat di laptop kantor.

SAKIPRO sebagai produk dirancang menjadi asisten kerja praktis, interaktif, sugestif, informatif, dan mudah dipakai oleh user biasa melalui Rich CLI, wizard, slash command, autocomplete, dan help kontekstual. Untuk v1.0, fitur interaktif penuh terintegrasi secara bawaan.
