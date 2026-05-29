# STACK.md
# SAKIPRO v1.0
# Technology Stack Blueprint

Version: 1.0  
Product: SAKIPRO  
Mode: Python CLI  
Target User: Kasubbag Perencanaan OPD  
Target Device: Laptop Kantor CPU-only  
AI Mode: API Key Model AI Berbasis Token  
Status: Implementation Ready  

---

## 1. Ringkasan Stack

SAKIPRO v1.0 adalah aplikasi CLI berbasis Python untuk membantu Kasubbag Perencanaan OPD melakukan review dokumen SAKIP di folder kerja.

Stack dipilih agar:

1. Ringan di laptop kantor.
2. Tidak membutuhkan GPU.
3. Dapat berjalan di Windows, macOS, dan Linux.
4. Dapat dikemas menjadi executable dari GitHub Release.
5. Mendukung AI API berbasis token.
6. Mendukung Rich terminal UI.
7. Mendukung document processing untuk DOCX, PDF, XLSX, CSV, TXT, dan Markdown.
8. Mendukung local database, retrieval dasar, graph optional, dan report generator.

---

## 2. Target Runtime

### 2.1 Python Version

Rekomendasi utama:

```text
Python 3.12
```

Versi minimum:

```text
Python 3.11
```

Alasan:

1. Stabil.
2. Ekosistem AI dan dokumen matang.
3. Cocok untuk CLI modern.
4. Dukungan packaging baik.
5. Kompatibel dengan Typer, Rich, LiteLLM, SQLAlchemy, dan library dokumen.

---

## 3. Target Operating System

SAKIPRO v1.0 harus berjalan pada:

```text
Windows 10/11
Windows 11 WSL2
macOS Intel
macOS Apple Silicon
Ubuntu Linux 22.04/24.04
Debian-based Linux
```

Prioritas operasional:

1. Windows 10/11 untuk laptop kantor umum.
2. macOS untuk developer.
3. Ubuntu Linux untuk server internal atau developer.

---

## 4. Hardware Requirement

### 4.1 Minimum Hardware

```text
CPU     : 4 core
RAM     : 8 GB
Storage : SSD 256 GB
GPU     : Tidak wajib
Internet: Wajib untuk AI API
OS      : Windows, macOS, atau Linux
```

Cocok untuk:

1. Scan folder kecil.
2. Review satu OPD.
3. Dokumen kurang dari 100 file.
4. Penggunaan AI API standar.

### 4.2 Recommended Hardware

```text
CPU     : 8 core
RAM     : 16 GB
Storage : SSD 512 GB
GPU     : Tidak wajib
Internet: Stabil
OS      : Windows 11, macOS, atau Ubuntu
```

Cocok untuk:

1. Penggunaan harian Kasubbag Perencanaan.
2. Dokumen OPD lengkap.
3. Review indikator, PK, LKjIP, cascading, dan evidence.
4. Generate laporan Markdown, XLSX, dan DOCX.

### 4.3 Power User Hardware

```text
CPU     : 8 sampai 12 core
RAM     : 32 GB
Storage : NVMe 1 TB
GPU     : Tidak wajib
Internet: Stabil
OS      : Windows 11 WSL2, macOS, atau Ubuntu
```

Cocok untuk:

1. Banyak dokumen multi-tahun.
2. Banyak evidence.
3. Batch review.
4. Development dan testing.

---

## 5. Core Software Stack

### 5.1 Bahasa Utama

```text
Python
```

Package manager utama:

```text
uv
```

Alternatif:

```text
pip
pipx
poetry
```

Rekomendasi:

1. `uv` untuk development cepat.
2. `pipx` untuk install sebagai CLI app.
3. `PyInstaller` untuk executable release.

---

## 6. CLI Framework Stack

### 6.1 Command Framework

```text
Typer
```

Fungsi:

1. Membuat command CLI.
2. Mendukung type hint.
3. Membuat help otomatis.
4. Cocok untuk command tree.
5. Mudah diintegrasikan dengan Rich.

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

Command v0.2 Should Have:

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
```

### 6.2 Terminal UI

```text
Rich
```

Dipakai untuk:

1. Banner.
2. Panel.
3. Table.
4. Tree.
5. Progress bar.
6. Markdown preview.
7. Syntax highlight.
8. Error panel.
9. Success panel.
10. Token warning.

### 6.3 Interactive Prompt

```text
prompt_toolkit
questionary
```

`prompt_toolkit` digunakan untuk:
1. **Interactive REPL:** Untuk mode `sakipro chat`.
2. **Real-time Autohints:** Menampilkan ghost text atau popup menu saat mengetik perintah.
3. **Command History:** Navigasi ke atas/bawah untuk perintah sebelumnya.
4. **Syntax Highlighting:** Mewarnai perintah slash agar berbeda dengan teks biasa.

questionary dipakai untuk:

1. Wizard.
2. Menu pilihan.
3. Confirm prompt.
4. Multi-select sederhana.

### 6.4 Shell Detection

```text
shellingham
```

Dipakai untuk:

1. Deteksi shell.
2. Instalasi autocomplete.
3. Penyesuaian Windows PowerShell, Bash, Zsh, dan Fish.

---

## 7. AI API Stack

### 7.1 AI Provider Abstraction

```text
LiteLLM
```

Fungsi:

1. Satu interface untuk banyak provider.
2. Mudah berpindah model.
3. Memudahkan model routing.
4. Memudahkan token tracking.
5. Cocok untuk OpenAI, Gemini, Claude, dan provider lain.

### 7.2 Provider AI yang Didukung (v0.2 ready)

Provider yang didukung via LiteLLM:

```text
1. OpenAI    : gpt-4o, gpt-4o-mini
2. Google    : gemini-1.5-pro, gemini-1.5-flash (Best for Context Window)
3. Anthropic : claude-3-5-sonnet, claude-3-haiku, claude-sonnet-4-20250514 (API Key Ready / Aktif di sistem)
4. xAI       : grok-beta
5. DeepSeek  : deepseek-chat, deepseek-coder (Best for Economy)
6. Groq      : llama-3-70b (Best for Speed)
```

Konfigurasi via `.env`:

```env
SAKIPRO_AI_PROVIDER=anthropic
OPENAI_API_KEY=
GEMINI_API_KEY=
ANTHROPIC_API_KEY=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
XAI_API_KEY=
DEEPSEEK_API_KEY=
GROQ_API_KEY=

SAKIPRO_DEFAULT_MODEL=claude-sonnet-4-20250514
SAKIPRO_LIGHT_MODEL=claude-sonnet-4-20250514
SAKIPRO_REASONING_MODEL=claude-sonnet-4-20250514
```

### 7.3 Model Routing

SAKIPRO harus membagi model berdasarkan tingkat pekerjaan.

#### Light Model

Dipakai untuk:

1. Klasifikasi dokumen.
2. Ringkasan singkat.
3. Ekstraksi metadata.
4. Jawaban ringan.

Contoh model:

```text
gpt-4o-mini
gemini-1.5-flash
claude-3-haiku
```

#### Default Model

Dipakai untuk:

1. Review indikator.
2. Review PK.
3. Review LKjIP.
4. Review cascading.
5. Review evidence.

Contoh model:

```text
gpt-4o
gemini-1.5-pro
claude-3-5-sonnet
```

#### Reasoning Model

Dipakai untuk:

1. Task panjang.
2. Review menyeluruh.
3. Rekomendasi strategis.
4. Analisis dokumen kompleks.

Contoh model:

```text
o3
claude-3-opus
gemini-1.5-pro
```

---

## 8. AI Orchestration Stack

### 8.1 Basic Agent Orchestration

Untuk v0.2, agent orchestration dapat dibuat ringan dengan Python class biasa.

Struktur:

```text
BaseAgent
FolderScannerAgent
IndicatorReviewAgent
CascadingReviewAgent
PKReviewAgent
LKjIPReviewAgent
EvidenceReviewAgent
OPDPlanningCopilotAgent
```

### 8.2 Optional Advanced Orchestration

```text
LangGraph
```

Status:

```text
Optional untuk v0.2
Recommended untuk v0.2+
```

Dipakai jika task mode semakin kompleks.

### 8.3 Prompt Management

Prompt disimpan di folder:

```text
sakipro/templates/prompts/
```

Format prompt:

```text
YAML atau Markdown
```

Contoh:

```text
indicator_review_prompt.md
pk_review_prompt.md
lkjip_review_prompt.md
evidence_review_prompt.md
```

### 8.4 Schema Validation

```text
Pydantic
Pydantic Settings
```

Dipakai untuk:

1. Input schema.
2. Output schema.
3. Config validation.
4. AI response validation.
5. Agent result validation.

---

## 9. Document Processing Stack

### 9.1 DOCX

```text
python-docx
docxtpl
```

Dipakai untuk:

1. Membaca Renstra, IKU, PK, LKjIP.
2. Membaca tabel DOCX.
3. Generate rekomendasi DOCX.
4. Generate laporan final DOCX berbasis template.

### 9.2 PDF

```text
PyMuPDF
pdfplumber
```

Dipakai untuk:

1. Membaca LHE PDF.
2. Membaca regulasi.
3. Membaca laporan hasil scan yang masih memiliki text layer.
4. Membaca tabel sederhana.

### 9.3 OCR Optional

```text
Tesseract OCR
pytesseract
Pillow
```

Status:

```text
Optional
```

Dipakai jika PDF berupa scan gambar.

Catatan:

1. OCR tidak wajib pada v1.0 Core.
2. Jika OCR tidak tersedia, tampilkan warning.
3. Jangan membuat proses gagal total hanya karena OCR tidak tersedia.

### 9.4 Excel dan CSV

```text
openpyxl
pandas
```

Dipakai untuk:

1. Membaca Renja XLSX.
2. Membaca RKA/DPA XLSX.
3. Membaca matriks indikator.
4. Membuat laporan review indikator XLSX.
5. Membuat laporan audit evidence XLSX.

### 9.5 Markdown dan TXT

```text
markdown
python built-in pathlib
```

Dipakai untuk:

1. Membaca catatan.
2. Membuat output laporan utama.
3. Preview laporan di terminal.

---

## 10. Storage Stack

### 10.1 Local Database

```text
SQLite
```

Alasan:

1. Ringan.
2. Tidak butuh server database.
3. Cocok untuk laptop kantor.
4. Mudah backup.
5. Cocok untuk single user.

### 10.2 ORM

```text
SQLAlchemy
```

Dipakai untuk:

1. Model database.
2. Query data.
3. Repository layer.
4. Migrasi ke PostgreSQL pada versi masa depan.

### 10.3 Migration

```text
Alembic
```

Status:

```text
Recommended
```

Untuk v0.2, migration dapat dibuat sederhana.

### 10.4 Database File

Lokasi default:

```text
~/.sakipro/sakipro.db
```

---

## 11. Retrieval and Memory Stack

### 11.1 Default Retrieval v0.2

```text
SQLite FTS/BM25 atau keyword retrieval
```

Alasan:
1. Ringan untuk laptop kantor.
2. Mudah dipaketkan.
3. Cukup untuk v1.0 Core.

### 11.2 Hybrid Retrieval Strategy (SQLite FTS5 Exclusive)

Sistem secara eksklusif menggunakan pola **SQLite FTS5 (Full-Text Search) dengan ranking BM25** untuk penelusuran dokumen:
1. **FTS5/BM25 (Eksklusif):** Digunakan untuk pencarian istilah teknis, nama indikator, target, program, dan kode aturan SAKIP secara instan.
2. **Deterministic Keyword Matcher:** Logika pencarian berbasis pemetaan kata kunci dan kode aturan `SAKIP_RULEBOOK.md` digabungkan langsung pada query tingkat SQLite untuk akurasi maksimal.
3. **Zero Vector Overhead:** Pustaka database vektor eksternal (seperti ChromaDB/FAISS) **ditiadakan** sepenuhnya demi menjamin RAM tetap 0% overhead tambahan pada laptop kantor.

### 11.3 Memory Efficiency & Context Budgeting for Office Laptops

Untuk menjaga RAM minimal 8GB tetap aman:
1. **Sliding Context Budget:** Batas token masukan dinamis (15k token untuk Light Tier, 60k token untuk Default/Reasoning Tier) dikendalikan secara ketat pada pemrosesan chunk untuk menghindari pembengkakan penggunaan memori.
2. **Streaming Data:** Gunakan generator/streaming saat membaca XLSX besar dengan `openpyxl` (mode read-only) dan PDF besar.
3. **Chunk Processing:** Proses dokumen per batch, jangan muat seluruh folder ke RAM.
4. **Connection Pooling:** Kelola koneksi SQLite agar tidak terjadi kebocoran memori saat task panjang.

### 11.4 Embedding (Ditiadakan)

Model Embedding berbasis API maupun lokal **ditiadakan sepenuhnya** pada rilis v0.2/v1.0. Penelusuran berbasis teks murni terstruktur menggunakan SQLite FTS5 terbukti sangat akurat dan hemat daya komputasi untuk dokumen kedinasan SAKIP.

---

## 12. Graph Stack

### 12.1 Local Graph Engine

```text
NetworkX
```

Dipakai untuk:

1. Pohon kinerja.
2. Cascading.
3. Relasi sasaran, indikator, program, kegiatan.
4. Task dependency sederhana.

### 12.2 Future Upgrade

```text
Neo4j
```

Status:

```text
Future upgrade
```

Tidak diperlukan pada v0.2.

---

## 13. Report Generation Stack

### 13.1 Markdown Report

```text
Markdown text writer
Rich Markdown Preview
```

Markdown menjadi output utama karena ringan dan mudah dibaca.

### 13.2 XLSX Report

```text
openpyxl
pandas
```

Dipakai untuk:

1. Review indikator.
2. Audit evidence.
3. Matriks perbaikan.
4. Daftar task perbaikan.

### 13.3 DOCX Report

```text
python-docx
docxtpl
```

Dipakai untuk:

1. Laporan final.
2. Rekomendasi perbaikan.
3. Draft narasi LKjIP.
4. Catatan review PK.

### 13.4 PDF Report

```text
weasyprint
LibreOffice headless
```

Status:

```text
Optional
```

Untuk v0.2, PDF boleh ditunda.

---

## 14. UI Stack

### 14.1 Rich Components

Gunakan komponen berikut:

```text
Console
Panel
Table
Tree
Progress
Spinner
Status
Prompt
Confirm
Markdown
Syntax
Live
Layout
```

### 14.2 UI Modules

Struktur:

```text
sakipro/ui/
  __init__.py
  banner.py
  theme.py
  console.py
  panels.py
  tables.py
  progress.py
  prompts.py
  autocomplete.py
  repl.py
  wizard.py
  workbench.py
  help.py
  errors.py
  suggestions.py
```

### 14.3 UI Helper Functions

Wajib ada:

```text
print_banner()
print_startup_panel()
print_project_status()
print_success()
print_warning()
print_error()
print_help()
print_sources()
print_confidence()
print_next_steps()
render_table()
render_tree()
render_progress()
render_task_board()
render_report_summary()
```

---

## 15. Configuration Stack

### 15.1 Environment

```text
python-dotenv
```

File:

```text
.env
.env.example
```

Contoh `.env`:

```env
SAKIPRO_AI_PROVIDER=anthropic
OPENAI_API_KEY=
GEMINI_API_KEY=
ANTHROPIC_API_KEY=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

SAKIPRO_DEFAULT_MODEL=claude-sonnet-4-20250514
SAKIPRO_LIGHT_MODEL=claude-sonnet-4-20250514
SAKIPRO_REASONING_MODEL=claude-sonnet-4-20250514

SAKIPRO_PRIVACY_MODE=standard
SAKIPRO_OUTPUT_DIR=outputs
```

### 15.2 YAML Config

```text
PyYAML
```

File:

```text
~/.sakipro/config.yaml
```

Contoh:

```yaml
project:
  name: DISDIK_2026
  default_folder: ./dokumen_sakip

ai:
  provider: anthropic
  default_model: claude-sonnet-4-20250514
  light_model: claude-sonnet-4-20250514
  reasoning_model: claude-sonnet-4-20250514
  max_tokens_per_task: 80000
  ask_confirmation_above_tokens: 50000

privacy:
  mode: standard
  mask_sensitive_data: true
  allow_cloud_ai: true

ui:
  banner: full
  theme: dark
  use_emoji: true
  show_token_cost: true
  show_sources: true
  show_confidence: true
  show_next_steps: true
  autocomplete: true
  slash_commands: true
  wizard_enabled: true

storage:
  database_path: ~/.sakipro/sakipro.db
  retrieval: sqlite_fts
  vector_store: disabled
  memory_dir: ~/.sakipro/memory

output:
  default_dir: outputs
  generate_markdown: true
  generate_xlsx: true
  generate_docx: true
```

---

## 16. Security Stack

### 16.1 Secret Management

Untuk v0.2:

```text
.env
```

Aturan:

1. API Key tidak hardcode.
2. API Key tidak masuk log.
3. File .env masuk .gitignore.
4. .env.example tidak memuat secret.
5. Command doctor hanya menampilkan status API Key, bukan nilainya.

### 16.2 Privacy Mode

Mode:

```text
open
standard
strict
```

Default:

```text
standard
```

#### open

Semua konteks boleh dikirim ke AI API.

#### standard

Data sensitif dimasking sebelum dikirim.

#### strict

Dokumen sensitif tidak dikirim ke AI API.

### 16.3 Data Masking

Pola masking:

1. NIK.
2. Nomor HP.
3. Email personal.
4. Nomor rekening.
5. Data ASN sensitif.
6. Data internal rahasia.

### 16.4 Guardrail

Aturan:

1. AI tidak boleh mengubah file asli.
2. AI tidak boleh membuat angka tanpa sumber.
3. AI tidak boleh mengklaim evidence ada jika tidak ditemukan.
4. AI tidak boleh menghapus file.
5. Output AI harus diberi status draft.
6. Output AI harus memiliki confidence score.

---

## 17. Logging Stack

### 17.1 Logger

```text
loguru
```

Dipakai untuk:

1. Command log.
2. Error log.
3. File processing log.
4. Agent run log.
5. Token usage log.
6. Debug log.

### 17.2 Log Folder

Default:

```text
~/.sakipro/logs/
```

File:

```text
sakipro.log
errors.log
agent_runs.log
token_usage.log
```

---

## 18. Token Management Stack

Token usage wajib dicatat.

Tabel:

```text
token_usage
```

Kolom:

```text
id
provider
model
input_tokens
output_tokens
total_tokens
estimated_cost
command
created_at
```

Command:

```bash
sakipro token
```

Output:

```text
Hari ini        : 18.420 token
Bulan ini       : 412.900 token
Estimasi biaya  : Rp 96.000
Model terbanyak : gpt-4o-mini
```

---

## 19. Testing Stack

### 19.1 Unit Test

```text
pytest
```

Test minimal:

1. Config loader.
2. Document classifier.
3. DOCX reader.
4. PDF reader.
5. XLSX reader.
6. Token manager.
7. Report writer.
8. UI helper.

### 19.2 Linting

```text
ruff
```

Dipakai untuk:

1. Lint.
2. Import sorting.
3. Format check.

### 19.3 Type Checking

```text
mypy
```

Status:

```text
Recommended
```

---

## 20. Packaging Stack

### 20.1 Executable Builder

```text
PyInstaller
```

Dipakai untuk membuat executable:

```text
sakipro.exe
sakipro-linux
sakipro-macos
```

Rekomendasi awal:

```text
PyInstaller one-folder mode
```

Alasan:

1. Lebih mudah debug.
2. Lebih aman untuk file template.
3. Lebih stabil untuk dependency dokumen.
4. Startup lebih cepat dibanding one-file.

### 20.2 GitHub Release

Artifact:

```text
sakipro-v1.0.0-windows-x64.zip
checksums.txt
```

Artifact Linux dan macOS termasuk v0.2 Advanced:

```text
sakipro-v1.0.0-linux-x64.tar.gz
sakipro-v1.0.0-macos-x64.tar.gz
sakipro-v1.0.0-macos-arm64.tar.gz
```

### 20.3 pipx Install

Untuk user teknis:

```bash
pipx install git+https://github.com/NAMA-ORG/sakipro.git
```

### 20.4 Source Install

Untuk developer:

```bash
git clone https://github.com/NAMA-ORG/sakipro.git
cd sakipro
uv sync
uv run sakipro doctor
```

---

## 21. CI/CD Stack

### 21.1 GitHub Actions

Workflow:

```text
test.yml
build-release.yml
```

test.yml:

1. Install dependencies.
2. Run ruff.
3. Run pytest.
4. Test CLI help.

build-release.yml:

1. Build Windows artifact.
2. Build Linux artifact.
3. Build macOS x64 artifact.
4. Build macOS arm64 artifact.
5. Generate checksum.
6. Upload to GitHub Release.

### 21.2 Target Runners

```text
windows-latest
ubuntu-latest
macos-latest
```

---

## 22. Project File Structure

```text
sakipro/
  pyproject.toml
  README.md
  PRD.md
  STACK.md
  CLI_UX.md
  INSTALL.md
  LICENSE
  .env.example
  config.example.yaml
  .gitignore

  sakipro/
    __init__.py
    main.py

    cli/
      __init__.py
      commands.py
      init_cmd.py
      scan_cmd.py
      status_cmd.py
      ask_cmd.py
      chat_cmd.py
      wizard_cmd.py
      review_cmd.py
      evidence_cmd.py
      report_cmd.py
      token_cmd.py
      doctor_cmd.py

    ui/
      __init__.py
      banner.py
      theme.py
      console.py
      panels.py
      tables.py
      progress.py
      prompts.py
      autocomplete.py
      repl.py
      wizard.py
      workbench.py
      help.py
      errors.py
      suggestions.py

    ai/
      __init__.py
      llm_client.py
      model_router.py
      prompt_manager.py
      token_manager.py
      guardrails.py

    agents/
      __init__.py
      base_agent.py
      folder_scanner_agent.py
      indicator_review_agent.py
      cascading_review_agent.py
      pk_review_agent.py
      lkjip_review_agent.py
      evidence_review_agent.py
      opd_planning_copilot_agent.py

    documents/
      __init__.py
      docx_reader.py
      pdf_reader.py
      xlsx_reader.py
      csv_reader.py
      txt_reader.py
      markdown_reader.py
      classifier.py
      chunker.py
      metadata.py

    sakip/
      __init__.py
      indicator_checker.py
      cascading_checker.py
      pk_checker.py
      lkjip_checker.py
      evidence_checker.py
      report_builder.py

    storage/
      __init__.py
      database.py
      models.py
      repositories.py

    memory/
      __init__.py
      search.py
      retrieval.py
      vector_store.py   # optional v0.2
      graph_store.py    # optional v0.2

    reports/
      __init__.py
      markdown_report.py
      xlsx_report.py
      docx_report.py
      json_report.py

    templates/
      prompts/
        indicator_review_prompt.md
        pk_review_prompt.md
        lkjip_review_prompt.md
        cascading_review_prompt.md
        evidence_review_prompt.md
      docx/
        final_report_template.docx
      xlsx/
        indicator_review_template.xlsx

  tests/
    test_config.py
    test_docx_reader.py
    test_pdf_reader.py
    test_xlsx_reader.py
    test_classifier.py
    test_cli_help.py
    test_token_manager.py

  scripts/
    build_windows.ps1
    build_linux.sh
    build_macos.sh
    install_windows.ps1
    install_linux.sh
    install_macos.sh

  .github/
    workflows/
      test.yml
      build-release.yml
```

---

## 23. Runtime Folder Structure

User runtime folder:

```text
~/.sakipro/
  config.yaml
  .env
  logs/
  cache/
  memory/
    retrieval/
    vector/  # optional v0.2
    graph/   # optional v0.2
  outputs/
  history
  sakipro.db
```

Project folder OPD:

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

Output folder:

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
```

---

## 24. Dependency List

### 24.1 Minimum Dependencies

```text
typer
rich
questionary
prompt_toolkit
pydantic
pydantic-settings
python-dotenv
PyYAML
litellm
sqlalchemy
pandas
openpyxl
python-docx
docxtpl
pymupdf
pdfplumber
loguru
shellingham
alembic
pytest
ruff
```

### 24.2 Optional Dependencies

Optional dependency hanya dipakai jika fitur terkait diaktifkan pada v0.2+ atau eksperimen Post-v1.0.

```text
faiss-cpu
chromadb
networkx
pytesseract
Pillow
weasyprint
markdown
mypy
langgraph
langchain
llama-index
```

---

## 25. pyproject.toml Target

```toml
[project]
name = "sakipro"
version = "0.2.0"
description = "AI CLI Assistant for OPD SAKIP Planning Documents"
requires-python = ">=3.11"
authors = [
  { name = "SAKIPRO Team" }
]

[project.scripts]
sakipro = "sakipro.main:app"

[tool.ruff]
line-length = 100

[tool.pytest.ini_options]
testpaths = ["tests"]
```

---

## 26. Recommended Development Setup

### 26.1 Clone Project

```bash
git clone https://github.com/NAMA-ORG/sakipro.git
cd sakipro
```

### 26.2 Install uv

```bash
pip install uv
```

### 26.3 Install Dependencies

```bash
uv sync
```

### 26.4 Setup Env

```bash
cp .env.example .env
```

Isi API Key.

### 26.5 Run Doctor

```bash
uv run sakipro doctor
```

### 26.6 Run CLI

```bash
uv run sakipro --help
```

---

## 27. Recommended User Setup

### 27.1 Windows Executable

1. Download `sakipro-v1.0.0-windows-x64.zip`.
2. Extract ke `C:\SAKIPRO`.
3. Jalankan `install.ps1`.
4. Isi `.env`.
5. Jalankan:

```powershell
sakipro doctor
```

### 27.2 macOS

1. Download artifact macOS.
2. Extract.
3. Jalankan `install_macos.sh`.
4. Isi `.env`.
5. Jalankan:

```bash
sakipro doctor
```

### 27.3 Linux

1. Download artifact Linux.
2. Extract.
3. Jalankan `install_linux.sh`.
4. Isi `.env`.
5. Jalankan:

```bash
sakipro doctor
```

---

## 28. Technology Decision Summary

| Area | Stack | Status | Alasan |
|---|---|---|---|
| Bahasa | Python 3.12 | Wajib | Ekosistem AI dan dokumen kuat |
| CLI | Typer | Wajib | Command rapi dan type hint |
| Terminal UI | Rich | Wajib | Panel, tabel, progress |
| Interactive | prompt_toolkit | Should Have | REPL dan autocomplete |
| Wizard | questionary | Should Have | User biasa lebih mudah |
| AI API | LiteLLM | Wajib | Multi provider |
| Database | SQLite | Wajib | Ringan laptop kantor |
| ORM | SQLAlchemy | Wajib | Modular dan scalable |
| Retrieval | SQLite FTS/BM25 | Wajib | Ringan dan mudah dipaketkan |
| Vector | ChromaDB atau FAISS | v0.2 Advanced Should Have | RAG semantik dengan SQLite retrieval sebagai fallback |
| Graph | NetworkX | v0.2 Advanced Should Have | Cascading dan pohon |
| DOCX | python-docx | Wajib | Baca dokumen |
| DOCX Template | docxtpl | Should Have | Tulis DOCX sederhana |
| PDF | PyMuPDF, pdfplumber | Wajib | Baca PDF |
| XLSX | openpyxl, pandas | Wajib | Baca dan tulis Excel |
| Logging | loguru | Wajib | Log rapi |
| Test | pytest | Wajib | Uji fitur |
| Lint | ruff | Wajib | Kualitas kode |
| Packaging | PyInstaller | Should Have | Executable GitHub Release |

---

## 29. Stack v0.2 Final

Untuk SAKIPRO v1.0 Core, gunakan stack ini:

```text
Python 3.12
Typer
Rich
LiteLLM
Pydantic
python-dotenv
PyYAML
SQLite
SQLAlchemy
SQLite FTS/BM25 atau keyword retrieval
python-docx
PyMuPDF
pdfplumber
openpyxl
pandas
loguru
pytest
ruff
```

v1.0 Expanded dan Advanced:

```text
prompt_toolkit
Questionary
docxtpl
PyInstaller
```

---

## 30. Final Recommendation

SAKIPRO v1.0 harus dibangun sebagai Python CLI ringan dengan Rich interactive UI, AI API berbasis token, document processing lokal, SQLite storage, SQLite FTS/BM25 atau keyword retrieval, citation traceability, dan PyInstaller packaging.

Stack ini paling sesuai untuk laptop kantor, mudah dipasang dari GitHub, tidak membutuhkan GPU, dan cukup kuat untuk membaca dokumen SAKIP OPD, mengecek indikator, mereview PK, mereview LKjIP, mengecek cascading, mengaudit evidence, dan membuat laporan perbaikan berbasis sumber. Vector memory dan graph analysis adalah v0.2 Advanced Should Have dengan fallback SQLite retrieval dan graph-ready schema.

END OF STACK.md
