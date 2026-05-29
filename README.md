# SAKIPRO v1.0 🚀

[![Python Version](https://img.shields.io/badge/python-3.11%2B-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Build Status](https://img.shields.io/badge/build-passing-brightgreen.svg)]()

**SAKIPRO** (Sistem Akuntabilitas Kinerja Instansi Pemerintah Professional) adalah AI-Powered CLI Agent yang dirancang khusus untuk mempermudah tugas Kasubbag Perencanaan / Tim Evaluator SAKIP di tingkat OPD (Organisasi Perangkat Daerah). SAKIPRO memanfaatkan kecerdasan buatan (LLM) untuk membaca, menganalisis, dan mengevaluasi dokumen perencanaan dan pelaporan secara otomatis.

---

## 🎯 Fitur Utama & Keunggulan

- 📂 **Smart Folder Scanner (`/scan`)**: Mengekstrak teks dari berbagai format dokumen (PDF, DOCX, XLSX, TXT) ke dalam *database* lokal (SQLite FTS5) tanpa bergantung pada *cloud embedding* (100% aman untuk laptop kantor).
- 🧠 **Smart Context RAG & Profiling**: Sistem dibekali pengaturan profil instansi (`/profile`) dan *Smart Scoring Engine* untuk memastikan agen AI mampu membedakan dokumen lintas instansi dan berfokus hanya pada target evaluasi.
- 💬 **Interactive Chat & UI**: Memiliki UI *terminal* interaktif (REPL) dengan *fuzzy autocomplete* responsif di setiap ketikan, indikator status *real-time*, animasi *spinner* cerdas, dan dukungan chat tanya jawab (*Natural Language*).
- 💾 **Auto-Export Markdown & Word**: Mengekspor otomatis seluruh temuan evaluasi ke dalam format **Markdown** dan **Microsoft Word (.docx)**.

---

## 🤖 Daftar Agen Evaluator Khusus

1. 📊 **Indicator Reviewer (`/cek-indikator`)**: Meninjau kelayakan dan orientasi Indikator Kinerja Utama (IKU) agar sesuai kaidah berorientasi hasil (*outcome*).
2. 📖 **RPJMD Reviewer (`/review-rpjmd`)**: Mengaudit dan menyelaraskan program kegiatan dari Rencana Pembangunan Jangka Menengah Daerah.
3. 📝 **PK & Renstra Reviewer (`/review-pk`, `/review-renstra`)**: Memvalidasi kesesuaian target Perjanjian Kinerja (PK) dan Rencana Strategis (Renstra).
4. 📈 **LKjIP Reviewer (`/review-lkjip`)**: Mengevaluasi bab capaian kinerja pada Laporan Kinerja Instansi Pemerintah.
5. 🔍 **Evidence Reviewer (`/cek-evidence`)**: Melakukan tabulasi silang antara laporan capaian dengan ketersediaan/relevansi bukti fisik.
6. 🌲 **Cascading Verifier (`/cek-cascading`)**: Menguji keselarasan pohon kinerja (*cascading*) dari level Sasaran Strategis hingga ke level Sub-kegiatan.
7. ✍️ **AI Drafter (`/draft`)**: Memberikan usulan/saran perbaikan redaksional (teks) perencanaan yang lebih tajam dan terukur.
8. 📑 **Final Report Generator (`/report`)**: Merangkum hasil temuan dari seluruh agen menjadi format Draf Laporan Hasil Evaluasi (LHE).

---

## 💻 Kebutuhan Sistem

- OS: **Windows 10/11**, **macOS**, atau **Linux**
- RAM: Minimal **8 GB**
- CPU: **Dual-Core / Quad-Core** standar laptop kantor
- Internet: **Dibutuhkan** (untuk panggilan API AI)
- Python (Bila di-build dari source): **3.11 atau lebih baru**

---

## 🚀 Instalasi & Persiapan

### 1. Mode Standalone / Executable (Direkomendasikan)
Anda dapat menggunakan SAKIPRO tanpa menginstal Python menggunakan *pre-built binaries*.
1. Unduh *file* zip SAKIPRO untuk sistem operasi Anda melalui halaman [Releases](#).
2. Ekstrak folder tersebut (misal: di desktop Anda).
3. Salin file `.env.example` menjadi `.env` lalu masukkan *API Key* Anda:
   ```ini
   SAKIPRO_AI_PROVIDER=anthropic
   ANTHROPIC_API_KEY=sk-ant-...
   ```
4. Jalankan aplikasi via terminal/command prompt:
   - **Mac/Linux:** `./sakipro`
   - **Windows:** `.\sakipro.exe`

### 2. Mode Developer (Dari Source Code)
Jika Anda adalah *developer* yang ingin mengembangkan SAKIPRO, ikuti langkah berikut:

```bash
# 1. Clone repository
git clone https://github.com/username/sakipro.git
cd sakipro

# 2. Buat virtual environment dan install dependencies
python3 -m venv .venv
source .venv/bin/activate  # Untuk Windows: .venv\Scripts\activate
pip install -e .

# 3. Konfigurasi kredensial AI
cp .env.example .env
# Edit .env dan masukkan API Key Anda (OpenAI, Anthropic, Gemini, dll)

# 4. Jalankan aplikasi
sakipro
```

---

## 🛠 Panduan Penggunaan Lengkap

Saat SAKIPRO dijalankan, Anda akan disambut oleh **Interactive REPL (Read-Eval-Print Loop)**. SAKIPRO siap menerima perintah *Slash Commands* atau obrolan santai biasa.

### 1. Sistem & Utilitas
- `/wizard` : Menjalankan ulang konfigurasi (setup awal).
- `/profile`: **Wajib!** Mengatur Konteks Profil Pemda (Tahun, Nama Pemda, Nama OPD) agar AI fokus membaca dokumen instansi yang tepat.
- `/status` : Menampilkan status dokumen terindeks dan rekapitulasi pemakaian *token*.
- `/ls <dir>`: Melihat daftar file dan *size* dari direktori kerja.
- `/reset`  : Menghapus seluruh database dan profil secara bersih untuk *fresh start*.
- `/clear`  : Membersihkan layar terminal.
- `/exit`   : Keluar dari aplikasi.

### 2. Pemindaian Dokumen
- `/scan <folder>`: Memindai folder, mengekstrak isi PDF/DOCX/Excel, dan memasukkannya ke otak SAKIPRO. 
  *(Contoh: `/scan ./Dokumen_SAKIP`)*

### 3. Eksekusi Evaluasi (Audit)
Setelah di-*scan*, ketik perintah berikut diikuti kueri/pertanyaan detail (atau jalankan kosongan):
- `/cek-indikator analisis IKU Dinas Pendidikan`
- `/review-rpjmd cek keselarasan program lintas OPD`
- `/review-pk evaluasi target PK eselon 3`
- `/review-lkjip periksa narasi kegagalan pada bab 3`
- `/review-renstra cek kelengkapan matriks sasaran`
- `/cek-cascading validasi rentang kendali pohon kinerja`
- `/cek-evidence cross-check foto fisik kegiatan`

### 4. Output & Laporan Akhir
- `/draft perbaiki kalimat indikator X agar lebih SMART`
- `/report rangkum semua temuan error hari ini menjadi format LHE`

---

## 🔒 Privasi dan Keamanan (Privacy By Design)

SAKIPRO menyadari sensitivitas dokumen birokrasi pemerintahan:
- **No Cloud Vector DB:** SAKIPRO tidak mengunggah seluruh dokumen Anda ke *vector database* awan. Ekstraksi (*parsing*) dan indeks penelusuran secara **sepenuhnya terjadi offline** di laptop Anda.
- **Micro-Prompting:** SAKIPRO hanya mengirimkan potongan paragraf (chunk) teks spesifik ke LLM (seperti Anthropic atau OpenAI) yang relevan untuk proses *review*, bukan keseluruhan *file* mentah Anda.

---

## 🏗 Roadmap Pengembangan

- [x] **v0.1**: Engine pemrosesan dokumen lokal & Database (SQLite FTS5).
- [x] **v0.2**: Agent Utama (IKU & PK Reviewer).
- [x] **v1.0**: *Expanded Agents* (Cascading, Evidence, LKjIP, Renstra, RPJMD, Drafter, Report).
- [x] **v1.1**: UI Enhancements (Rich Animations, Autocomplete) & Smart Context RAG Profile.
- [ ] **Next**: Dukungan Audit Multi-Tahun, Task Board, Visualisasi Graf Pohon Kinerja.

---

## 🤝 Kontribusi

Kami sangat menyambut kontribusi (*Pull Requests*, *Issues*, maupun *Discussions*) dari *developer* maupun praktisi pemerintahan untuk membuat SAKIPRO lebih baik lagi! 

Mohon baca dokumen desain kami di `docs/AI_AGENT_TECHNICAL_DESIGN.md` untuk memahami pola arsitektur agen SAKIPRO sebelum mengembangkan fitur baru.

---

## 📜 Lisensi

Aplikasi ini dirilis di bawah naungan lisensi **MIT License**. Lihat file `LICENSE` untuk informasi lebih lanjut.

*Dibangun dengan ❤️ untuk mendorong birokrasi yang lebih berorientasi hasil dan akuntabel.*
