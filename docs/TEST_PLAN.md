# TEST_PLAN.md
# SAKIPRO v1.0 Test Plan

Version: 1.0  
Status: Blueprint Revision  
Purpose: Memastikan fitur inti dapat diverifikasi tanpa bergantung pada live AI call.

---

## 1. Test Strategy

Testing v0.2 memakai:

1. Unit test untuk parser, config, privacy, token, dan report writer.
2. Integration test untuk command CLI.
3. Golden dataset untuk output review yang stabil.
4. Mock AI client untuk semua test otomatis.
5. Smoke test manual untuk executable release.

---

## 2. Golden Dataset

Folder:

```text
tests/fixtures/golden/
```

Isi minimal:

1. `renstra_sample.docx`
2. `iku_sample.docx`
3. `pk_2026_sample.docx`
4. `lkjip_sample.docx`
5. `renja_sample.xlsx`
6. `evidence_sample.pdf`
7. `expected_scan.json`
8. `expected_review_indikator.json`
9. `expected_review_pk.json`

---

## 3. Required Test Cases

### Unit

1. Config loader membaca `.env` dan `config.yaml`.
2. Privacy filter memasking NIK, nomor HP, email, rekening, dan API key.
3. Document reader mengembalikan text, metadata, dan source spans.
4. Token manager menghitung estimasi biaya.
5. AI output parser menolak JSON tanpa `sources`.

### Integration

1. `sakipro init` membuat workspace.
2. `sakipro doctor` memvalidasi config tanpa menampilkan secret.
3. `sakipro scan tests/fixtures/golden` membuat registry.
4. `sakipro status` menampilkan workspace, dokumen, output, dan privacy mode.
5. `sakipro ask` menjawab dengan source refs.
6. `sakipro cek-indikator` membuat Markdown dan XLSX.
7. `sakipro review-pk` membuat findings berbasis rule.
8. `sakipro token` menampilkan usage tanpa prompt mentah.
9. `sakipro privacy` menampilkan dan mengubah mode dengan validasi.
10. `sakipro review-lkjip` membuat findings berbasis rule dan source refs.
11. `sakipro cek-cascading` membuat relasi dan gap berbasis sumber.
12. `sakipro cek-evidence` menghubungkan klaim dengan bukti dukung.
13. `sakipro report final` membuat Markdown/XLSX/DOCX draft dengan source appendix.

### Security

1. Secret tidak muncul di log.
2. Mode `strict` memblokir chunk sensitif.
3. File asli tidak berubah setelah semua command.

---

## 4. Commands

```bash
uv run ruff check .
uv run pytest
uv run pytest tests/test_privacy.py
uv run pytest tests/test_cli_scan.py
```

---

## 5. Coverage Gate

Target awal:

1. Unit coverage minimal 70% untuk modul inti.
2. Semua command Must Have punya minimal satu integration test.
3. Semua rule indikator, PK, LKjIP, cascading, dan evidence punya minimal satu fixture positif dan negatif.
