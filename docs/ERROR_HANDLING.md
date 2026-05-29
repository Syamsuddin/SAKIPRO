# ERROR_HANDLING.md
# SAKIPRO v1.0 Error Handling Blueprint

Version: 1.0  
Status: Blueprint Revision  
Purpose: Membuat error CLI jelas untuk user biasa dan tetap berguna untuk developer.

---

## 1. Error UX Standard

Setiap error harus menampilkan:

1. Apa yang gagal.
2. Penyebab yang mungkin.
3. Solusi yang dapat dilakukan user.
4. File atau command terkait.
5. Error code stabil.

Semua error juga masuk log aman tanpa secret dan tanpa isi dokumen sensitif.

---

## 2. Error Code

| Code | Kondisi | Aksi User |
|---|---|---|
| CONFIG_MISSING | `config.yaml` tidak ditemukan | Jalankan `sakipro init` |
| API_KEY_MISSING | API key belum diisi | Isi `.env`, lalu jalankan `sakipro doctor` |
| FILE_READ_FAILED | File tidak dapat dibaca | Cek format, password, atau kerusakan file |
| FILE_PARTIAL_READ | File terbaca sebagian | Lihat log dan lanjutkan dengan validasi manual |
| PRIVACY_BLOCKED | Mode privacy memblokir konteks | Gunakan mode lebih longgar atau hapus data sensitif |
| TOKEN_LIMIT_EXCEEDED | Estimasi token melewati batas | Kurangi dokumen atau naikkan limit dengan konfirmasi |
| AI_SCHEMA_INVALID | Output AI tidak sesuai schema | Retry otomatis, lalu laporkan jika tetap gagal |
| AI_SOURCE_REQUIRED | Output AI tidak memiliki sumber | Scan ulang atau tambah dokumen relevan |
| OUTPUT_WRITE_FAILED | Report gagal disimpan | Cek permission folder `outputs/` |
| DB_LOCKED | SQLite sedang terkunci | Tutup proses lain atau ulangi command |
| AI_RETRY_EXHAUSTED | Retry AI call atau JSON parse gagal semua | Cek koneksi, lalu coba lagi; atau ganti model |

---

## 3. Partial Success

Command `scan` dan report harus mendukung partial success:

1. File berhasil dibaca tetap disimpan.
2. File gagal baca dicatat dalam summary.
3. User mendapat daftar file bermasalah.
4. Command keluar dengan status non-zero hanya jika tidak ada file yang berhasil diproses.

---

## 4. Retry Policy

1. File read: tidak retry otomatis untuk file rusak atau password-protected.
2. AI call: maksimal dua retry untuk error transient.
3. JSON parse: satu retry dengan prompt perbaikan schema.
4. Output write: tidak overwrite file lama; gunakan nama baru.
