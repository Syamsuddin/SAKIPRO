---
name: sakipro-cli-design-vision
description: Visi desain CLI SAKIPRO — satu perintah `sakipro`, REPL default, thinking mode, rekomendasi wajib
metadata:
  type: project
---

Visi utama CLI SAKIPRO yang sudah dikonfirmasi user:

1. **Satu perintah:** `sakipro` (tanpa subcommand) = banner + status panel + REPL langsung aktif. Tidak ada `uv run sakipro`, tidak ada `sakipro chat` sebagai pintu masuk.

2. **REPL adalah mode default.** User tidak perlu tahu subcommand apapun. Cukup ketik di prompt.

3. **Input yang diterima REPL:** slash command (`/review-pk`), bahasa natural (`review PK saya`), pertanyaan bebas — semua diterima.

4. **Thinking & Step Mode wajib:** Setiap AI memproses, tampilkan panel "Thinking" + langkah-langkah yang dilakukan secara real-time. User tidak boleh melihat layar diam.

5. **Rekomendasi berikutnya wajib:** Setiap respons diakhiri dengan 3 rekomendasi kontekstual — minimal 1 slash command (dengan alasan) dan 1 pertanyaan natural language.

6. **Ghost text autohint:** Saat mengetik, tampilkan sisa perintah sebagai ghost text abu-abu. Popup dropdown muncul saat mengetik `/`.

**Why:** User adalah Kasubbag Perencanaan non-teknis. CLI harus terasa seperti asisten kerja interaktif, bukan terminal teknis. Referensi: [CLI_BLUEPRINT.md](../../docs/CLI_BLUEPRINT.md)

**How to apply:** Saat menulis kode CLI, selalu pastikan: (1) entry point `sakipro` tanpa arg = REPL, (2) setiap output AI ada thinking display, (3) setiap respons ada rekomendasi berikutnya.
