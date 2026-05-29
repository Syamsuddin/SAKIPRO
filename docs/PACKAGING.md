# PACKAGING.md
# SAKIPRO v1.0 Packaging Blueprint

Version: 1.0  
Status: Blueprint Revision  
Purpose: Menjelaskan packaging executable agar stabil di laptop kantor.

---

## 1. Strategy

Gunakan PyInstaller `one-folder` untuk v0.2.

Alasan:

1. Lebih mudah debug.
2. Template DOCX/XLSX/Markdown lebih aman dibundle.
3. Dependency dokumen lebih stabil.
4. Startup lebih cepat dibanding one-file.

---

## 2. Bundled Assets

Artifact wajib menyertakan:

1. `templates/`
2. `config.example.yaml`
3. `.env.example`
4. `README_INSTALL.md`
5. `LICENSE`

Command `doctor` harus memverifikasi asset tersebut tersedia.

---

## 3. Hidden Import and Native Dependency Risk

Perlu smoke test khusus untuk:

1. PyMuPDF.
2. pdfplumber.
3. python-docx.
4. openpyxl.
5. pandas.
6. LiteLLM provider adapters.
7. prompt_toolkit dan questionary.

Jika dependency membuat artifact terlalu besar, pindahkan fitur tersebut menjadi optional extra.

---

## 4. Build Commands

```bash
uv run pyinstaller packaging/sakipro.spec
```

Script helper:

```text
scripts/build_windows.ps1
scripts/build_linux.sh
scripts/build_macos.sh
```

---

## 5. Artifact Verification

Setiap artifact wajib menjalankan:

```bash
sakipro --help
sakipro doctor
sakipro scan examples/sample_workspace/Dokumen_SAKIP_OPD
sakipro status
sakipro cek-indikator
sakipro review-pk
sakipro review-lkjip
sakipro cek-cascading
sakipro cek-evidence
sakipro report final
sakipro token
sakipro privacy
```

Verifikasi juga:

1. Tidak ada file source yang berubah.
2. Output masuk ke `outputs/`.
3. Log aman dari secret dan PII.
4. Checksum dibuat.
