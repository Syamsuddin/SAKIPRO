# RELEASE_CHECKLIST.md
# SAKIPRO v1.0 Release Checklist

Version: 1.0
Status: Blueprint Revision
Purpose: Menentukan gate sebelum GitHub Release atau distribusi internal.

Semua gate QA menggunakan binary `sakipro` yang sudah terinstall — bukan `uv run`.
Uv dan toolchain developer hanya dipakai di pipeline build, tidak di checklist ini.

---

## 1. Build Gate

Jalankan dari mesin build (CI atau lokal developer):

1. `ruff check .` berhasil tanpa error.
2. `pytest` berhasil semua test.
3. PyInstaller build berhasil: `python packaging/build.py`
4. Folder `dist/sakipro/` terbentuk dan berisi `sakipro.exe` (Windows).
5. Asset bundled ada semua:
   - `templates/` lengkap
   - `config.example.yaml`
   - `.env.example`
   - `README_INSTALL.md`
   - `install.bat`
   - `LICENSE`
6. ZIP artifact terbentuk: `sakipro-v1.0.0-windows-x64.zip`
7. `checksums.txt` berisi SHA256 dari ZIP.

---

## 2. Install Gate

Jalankan di **mesin bersih** (bukan mesin build) setelah extract ZIP:

1. Jalankan `install.bat` — selesai tanpa error.
2. Buka terminal **baru** (bukan yang sama dengan saat install).
3. Ketik `sakipro` dari folder home (`C:\Users\<user>`) — berhasil menampilkan banner.
4. Ketik `sakipro` dari folder dokumen acak — berhasil (verifikasi PATH bekerja di folder manapun).
5. Ketik `sakipro doctor` — status siap (API key belum diisi = warning, bukan error fatal).
6. `sakipro --version` menampilkan `v1.0.0`.

---

## 3. Pre-Release Functional Gate

Jalankan menggunakan binary terinstall + workspace golden dataset:

1. `sakipro init` — setup workspace berjalan, API key bisa diisi.
2. `sakipro doctor` — semua dependency terbaca, API key valid ditandai `✓`, hilang ditandai `⚠`.
3. `sakipro scan ./Dokumen_SAKIP_Golden` — progress bar muncul, dokumen terindeks.
4. `sakipro status` — menampilkan workspace panel dengan privacy mode.
5. `sakipro cek-indikator` — tabel hasil muncul dengan source refs.
6. `sakipro review-pk` — summary panel + tabel konflik muncul dengan source refs.
7. `sakipro token` — menampilkan usage tanpa API key mentah di output.
8. `sakipro privacy` — menampilkan mode aktif, bisa diubah.
9. *(v1.0 Expanded)* `sakipro review-lkjip` — output dengan source refs.
10. *(v1.0 Expanded)* `sakipro cek-cascading` — pohon kinerja tampil.
11. *(v1.0 Expanded)* `sakipro cek-evidence` — audit table muncul.
12. *(v1.0 Expanded)* `sakipro report final` — Markdown + XLSX + DOCX draft dibuat di `outputs/`.
13. File asli pada golden dataset tidak berubah setelah semua command dijalankan.
14. Semua output AI berlabel DRAFT.

---

## 4. Interactive Mode Gate

1. `sakipro` (tanpa argumen) — banner + status panel + prompt `sakipro ❯` muncul.
2. Ketik `/` di prompt — popup daftar slash command muncul.
3. Ketik `/rev` — daftar difilter real-time ke `review-pk`, `review-lkjip`.
4. Ketik pertanyaan natural: `apa kelemahan indikator saya?` — thinking panel muncul, respons streaming, rekomendasi berikutnya muncul di akhir.
5. `Ctrl+D` — keluar dengan bersih.

---

## 5. Security & Privacy Gate

1. Log di `~/.sakipro/logs/` tidak mengandung: API key, NIK, nomor HP, email personal, nomor rekening.
2. Privacy mode `strict` memblokir dokumen sensitif dari dikirim ke AI API.
3. Privacy mode `standard` melakukan masking data sensitif sebelum kirim.
4. `.env` tidak ikut ter-bundle di dalam ZIP artifact.

---

## 6. UI & Compatibility Gate

1. Banner tampil benar di Windows Terminal (tidak ada karakter rusak).
2. Banner tampil benar di Windows PowerShell default.
3. Progress bar dan spinner muncul saat proses panjang (tidak ada layar diam).
4. Panel error muncul dengan penyebab + saran saat API key kosong.
5. Panel error muncul dengan penyebab + saran saat file tidak terbaca.
6. Token warning muncul saat >80% budget bulanan.
7. `sakipro --silent` menekan banner dan panel, output murni data.
8. Semua output file masuk ke folder `outputs/`.

---

## 7. Packaging Gate

1. ZIP dapat di-extract di Windows tanpa software tambahan (bawaan Windows).
2. `install.bat` dijalankan tanpa admin rights (tidak butuh `Run as Administrator`).
3. `install.bat` tidak merusak PATH yang sudah ada.
4. Uninstall: hapus folder `%LOCALAPPDATA%\SAKIPRO\` dan hapus entry PATH — tidak ada sisa registry.
5. Ukuran ZIP di bawah 150 MB.
6. Artifact berisi `checksums.txt` dengan SHA256.
7. `README_INSTALL.md` cukup jelas dibaca user non-teknis tanpa bantuan.

---

## 8. Release Artifacts

```text
sakipro-v1.0.0-windows-x64.zip
  ├── sakipro/          ← folder PyInstaller one-folder
  │   └── sakipro.exe
  ├── templates/
  ├── config.example.yaml
  ├── .env.example
  ├── install.bat
  ├── uninstall.bat
  ├── README_INSTALL.md
  └── LICENSE
checksums.txt
RELEASE_NOTES.md
```

Artifact macOS dan Linux masuk scope v1.0 Expanded setelah smoke test lintas OS stabil.

---

## 9. Install Script Spec (install.bat)

`install.bat` harus melakukan langkah berikut secara otomatis:

```bat
1. Salin seluruh folder ke %LOCALAPPDATA%\SAKIPRO\
2. Tambahkan %LOCALAPPDATA%\SAKIPRO\ ke PATH user (setx PATH, bukan system PATH)
3. Tampilkan konfirmasi: "SAKIPRO berhasil diinstall."
4. Tampilkan instruksi: "Buka terminal baru, lalu ketik: sakipro"
5. Buat %LOCALAPPDATA%\SAKIPRO\.env dari .env.example jika belum ada
```

`install.bat` tidak boleh:

- Membutuhkan administrator rights
- Memodifikasi system PATH
- Menimpa `.env` yang sudah ada
- Menginstall Python atau dependency lain

---

## Catatan Developer

Gate build dan QA teknis (ruff, pytest, pyinstaller) dijalankan di pipeline CI, bukan di checklist ini.
Checklist ini hanya menguji dari perspektif user yang sudah melakukan install.
