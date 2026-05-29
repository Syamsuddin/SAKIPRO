---
name: sakipro-project-overview
description: SAKIPRO v0.2 — AI CLI Agent untuk review dokumen SAKIP OPD; Python 3.12, Rich, prompt_toolkit, LiteLLM
metadata:
  type: project
---

SAKIPRO v0.2 adalah AI CLI Agent berbasis Python untuk membantu Kasubbag Perencanaan OPD mereview dokumen SAKIP (Renstra, IKU, PK, LKjIP, evidence).

**Why:** OPD butuh alat bantu review dokumen SAKIP yang praktis, ringan, bisa jalan di laptop kantor tanpa GPU.

**Stack utama:** Python 3.12 · Typer · Rich · prompt_toolkit · questionary · LiteLLM · SQLite · SQLAlchemy

**AI Providers via LiteLLM:** OpenAI, Google Gemini, Anthropic Claude, DeepSeek, Groq

**Target device:** Laptop kantor Windows 10/11 CPU-only, RAM 8GB minimum

**Output:** Markdown, XLSX, DOCX di folder `outputs/`

**Packaging:** PyInstaller executable + GitHub Release

**How to apply:** Saat menyarankan solusi, selalu pertimbangkan keterbatasan laptop kantor (RAM 8GB, CPU-only, Windows-first). Hindari dependency berat.
