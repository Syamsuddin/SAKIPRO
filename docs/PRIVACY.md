# PRIVACY.md
# SAKIPRO v1.0 Privacy and Sensitive Data Blueprint

Version: 1.0  
Status: Blueprint Revision  
Purpose: Menjaga dokumen OPD, data ASN, API key, cache, dan log tetap aman.

---

## 1. Privacy Pipeline

Setiap command yang memakai AI wajib menjalankan alur:

```text
detect -> classify -> mask -> preview -> confirm -> send -> log_safe
```

1. `detect`: cari pola sensitif.
2. `classify`: beri label sensitivitas dokumen dan chunk.
3. `mask`: redaksi data sensitif.
4. `preview`: tampilkan ringkasan data yang akan dikirim, bukan isi penuh.
5. `confirm`: minta konfirmasi untuk operasi mahal atau sensitif.
6. `send`: kirim hanya konteks yang lolos.
7. `log_safe`: simpan log tanpa secret dan tanpa PII.

---

## 2. Privacy Modes

| Mode | Perilaku |
|---|---|
| open | Mengirim konteks tanpa masking tambahan. Hanya untuk data publik. |
| standard | Default. Masking PII dan data sensitif sebelum AI call. |
| strict | Tidak mengirim chunk sensitif ke AI API. Hanya metadata aman yang boleh dipakai. |

Mode `strict` harus memblokir dokumen yang berisi NIK, nomor rekening, nomor HP pribadi, email personal, data ASN sensitif, atau dokumen internal rahasia.

---

## 3. Sensitive Patterns & Local Filter Implementation

Untuk menjamin kepatuhan UU PDP tanpa menambah overhead memori, deteksi pola sensitif dilakukan secara **lokal** pada CPU menggunakan objek ekspresi reguler terkompilasi (`re.compile`) di Python sebelum data dikirim ke internet.

Pola ekspresi reguler minimal yang wajib didefinisikan:

1. **NIK (Nomor Induk Kependudukan):** `^\d{16}$` (16 digit angka berurutan).
2. **Nomor HP Indonesia:** `(?:\+62|62|0)8[1-9]\d{7,10}\b` (format lokal/internasional).
3. **Email Personal:** `[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}`.
4. **Nomor Rekening Bank:** Pola angka terstruktur sepanjang 10-15 digit.
5. **Nomor Identitas ASN (NIP):** `^\d{18}$` (18 digit angka berurutan).
6. **Alamat Rumah / Fisik:** Deteksi frasa kunci (seperti "Jl.", "Jalan", "RT/RW").
7. **Data Kesehatan & Disiplin Pegawai:** Deteksi kata kunci sensitif (seperti "sakit", "pelanggaran", "disiplin", "hukuman").
8. **API Kunci & Secret Token:** Pola deteksi string acak dengan entropi tinggi (seperti `sk-ant-...`, `AIzaSy...`).

---

## 4. Log and Cache Rules

1. `.env` tidak boleh dibaca ke log.
2. Prompt lengkap tidak boleh masuk log default.
3. Cache chunk harus menyimpan data setelah masking jika privacy mode `standard`.
4. Error log boleh menyimpan file path dan error code, tetapi tidak isi dokumen sensitif.
5. `doctor` hanya menampilkan status API key: found, missing, invalid.

---

## 5. Required Tests

1. API key tidak muncul di `sakipro.log`.
2. NIK dan nomor HP termasking sebelum AI call.
3. Mode `strict` memblokir chunk sensitif.
4. Report tidak menampilkan data yang sudah dimasking.
5. Token usage tidak menyimpan prompt mentah.
