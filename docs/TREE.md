# TREE.md
# SAKIPRO v1.0
# Project Folder and File Structure

Version: 1.0
Product: SAKIPRO
Mode: Python CLI
Target: Vibe Coding AI Agent, Python Developer, AI Engineer
Status: Implementation Ready
Changes from v0.2: Added agents CLI Router, Rencana Aksi, LHE Tracking; UI modules streaming/thinking/diff/plan_mode/decision_gates/status_bar/tree; sakip rulebook.py, desk_scorer.py; tasks task_templates.py; memory tier (result_cache, session_context, context_budget); new prompts, templates, golden fixtures, and sample docs.

---

## 1. Spesifikasi Operasional v1.0

## 2. Root Project Tree

```text
sakipro/
├── README.md
├── PRD.md
├── STACK.md
├── CLI_UX.md
├── TREE.md
├── SCOPE.md
├── SAKIP_RULEBOOK.md
├── AI_CONTRACT.md
├── PRIVACY.md
├── ERROR_HANDLING.md
├── TEST_PLAN.md
├── PACKAGING.md
├── RELEASE_CHECKLIST.md
├── INSTALL.md                    # planned
├── USER_GUIDE.md                 # planned
├── CHANGELOG.md                  # planned
├── LICENSE
├── pyproject.toml
├── uv.lock
├── .env.example
├── config.example.yaml
├── .gitignore
├── .python-version
│
├── sakipro/
│   ├── __init__.py
│   ├── __main__.py
│   ├── main.py
│   │
│   ├── cli/
│   │   ├── __init__.py
│   │   ├── commands.py
│   │   ├── init_cmd.py
│   │   ├── doctor_cmd.py
│   │   ├── scan_cmd.py
│   │   ├── status_cmd.py
│   │   ├── ask_cmd.py
│   │   ├── chat_cmd.py
│   │   ├── wizard_cmd.py
│   │   ├── workbench_cmd.py
│   │   ├── indicator_cmd.py
│   │   ├── cascading_cmd.py
│   │   ├── tree_cmd.py
│   │   ├── pk_cmd.py
│   │   ├── lkjip_cmd.py
│   │   ├── rencana_aksi_cmd.py
│   │   ├── lhe_cmd.py
│   │   ├── evidence_cmd.py
│   │   ├── draft_cmd.py
│   │   ├── task_cmd.py
│   │   ├── resume_cmd.py
│   │   ├── report_cmd.py
│   │   ├── token_cmd.py
│   │   ├── model_cmd.py
│   │   ├── privacy_cmd.py
│   │   ├── config_cmd.py
│   │   └── output_cmd.py
│   │
│   ├── ui/
│   │   ├── __init__.py
│   │   ├── banner.py
│   │   ├── theme.py
│   │   ├── console.py
│   │   ├── panels.py
│   │   ├── tables.py
│   │   ├── progress.py
│   │   ├── prompts.py
│   │   ├── autocomplete.py
│   │   ├── repl.py
│   │   ├── wizard.py
│   │   ├── workbench.py
│   │   ├── status_bar.py
│   │   ├── streaming.py
│   │   ├── thinking.py
│   │   ├── plan_mode.py
│   │   ├── decision_gates.py
│   │   ├── diff.py
│   │   ├── tree.py
│   │   ├── help.py
│   │   ├── errors.py
│   │   ├── suggestions.py
│   │   ├── markdown_viewer.py
│   │   ├── report_preview.py
│   │   └── icons.py
│   │
│   ├── core/
│   │   ├── __init__.py
│   │   ├── settings.py
│   │   ├── paths.py
│   │   ├── logger.py
│   │   ├── exceptions.py
│   │   ├── constants.py
│   │   ├── version.py
│   │   ├── bootstrap.py
│   │   └── app_context.py
│   │
│   ├── ai/
│   │   ├── __init__.py
│   │   ├── llm_client.py
│   │   ├── model_router.py
│   │   ├── prompt_manager.py
│   │   ├── token_manager.py
│   │   ├── guardrails.py
│   │   ├── privacy_filter.py
│   │   ├── response_parser.py
│   │   ├── schemas.py
│   │   └── cost_estimator.py
│   │
│   ├── agents/
│   │   ├── __init__.py
│   │   ├── base_agent.py
│   │   ├── folder_scanner_agent.py
│   │   ├── cli_router_agent.py
│   │   ├── indicator_review_agent.py
│   │   ├── cascading_review_agent.py
│   │   ├── pk_review_agent.py
│   │   ├── lkjip_review_agent.py
│   │   ├── evidence_review_agent.py
│   │   ├── rencana_aksi_review_agent.py
│   │   ├── lhe_tracking_agent.py
│   │   ├── opd_planning_copilot_agent.py
│   │   ├── draft_agent.py
│   │   ├── report_agent.py
│   │   ├── desk_evaluation_agent.py
│   │   └── task_agent.py
│   │
│   ├── documents/
│   │   ├── __init__.py
│   │   ├── base_reader.py
│   │   ├── docx_reader.py
│   │   ├── pdf_reader.py
│   │   ├── xlsx_reader.py
│   │   ├── csv_reader.py
│   │   ├── txt_reader.py
│   │   ├── markdown_reader.py
│   │   ├── classifier.py
│   │   ├── chunker.py
│   │   ├── metadata.py
│   │   ├── file_scanner.py
│   │   ├── file_registry.py
│   │   └── document_service.py
│   │
│   ├── sakip/
│   │   ├── __init__.py
│   │   ├── rulebook.py
│   │   ├── indicator_checker.py
│   │   ├── cascading_checker.py
│   │   ├── performance_tree.py
│   │   ├── pk_checker.py
│   │   ├── lkjip_checker.py
│   │   ├── evidence_checker.py
│   │   ├── rencana_aksi_checker.py
│   │   ├── lhe_tracker.py
│   │   ├── coherence_checker.py
│   │   ├── consistency_checker.py
│   │   ├── desk_scorer.py
│   │   ├── recommendation_builder.py
│   │   ├── quality_gate.py
│   │   └── sakip_terms.py
│   │
│   ├── memory/
│   │   ├── __init__.py
│   │   ├── vector_store.py          # ditiadakan
│   │   ├── graph_store.py
│   │   ├── search.py
│   │   ├── retrieval.py
│   │   ├── indexer.py
│   │   ├── memory_manager.py
│   │   ├── context_builder.py
│   │   ├── result_cache.py
│   │   ├── session_context.py
│   │   └── context_budget.py
│   │
│   ├── storage/
│   │   ├── __init__.py
│   │   ├── database.py
│   │   ├── models.py
│   │   ├── repositories.py
│   │   ├── migrations.py
│   │   ├── seed.py
│   │   └── unit_of_work.py
│   │
│   ├── reports/
│   │   ├── __init__.py
│   │   ├── markdown_report.py
│   │   ├── xlsx_report.py
│   │   ├── docx_report.py
│   │   ├── json_report.py
│   │   ├── final_report.py
│   │   ├── indicator_report.py
│   │   ├── pk_report.py
│   │   ├── lkjip_report.py
│   │   ├── cascading_report.py
│   │   ├── evidence_report.py
│   │   ├── rencana_aksi_report.py
│   │   ├── lhe_report.py
│   │   └── report_paths.py
│   │
│   ├── tasks/
│   │   ├── __init__.py
│   │   ├── task_model.py
│   │   ├── task_templates.py
│   │   ├── task_decomposer.py
│   │   ├── task_runner.py
│   │   ├── task_router.py
│   │   ├── task_state.py
│   │   ├── task_history.py
│   │   ├── task_board.py
│   │   ├── task_suggestions.py
│   │   ├── skill_registry.py
│   │   └── subtask_context.py
│   │
│   ├── config/
│   │   ├── __init__.py
│   │   ├── config_loader.py
│   │   ├── env_loader.py
│   │   ├── config_writer.py
│   │   ├── defaults.py
│   │   └── validation.py
│   │
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── datetime_utils.py
│   │   ├── file_utils.py
│   │   ├── text_utils.py
│   │   ├── slug_utils.py
│   │   ├── table_utils.py
│   │   ├── json_utils.py
│   │   ├── money_utils.py
│   │   └── safe_write.py
│   │
│   └── templates/
│       ├── prompts/
│       │   ├── system_base.md
│       │   ├── folder_scan_prompt.md
│       │   ├── indicator_review_prompt.md
│       │   ├── cascading_review_prompt.md
│       │   ├── pk_review_prompt.md
│       │   ├── lkjip_review_prompt.md
│       │   ├── evidence_review_prompt.md
│       │   ├── rencana_aksi_review_prompt.md
│       │   ├── lhe_tracking_prompt.md
│       │   ├── coherence_analysis_prompt.md
│       │   ├── ask_copilot_prompt.md
│       │   ├── desk_evaluation_prompt.md
│       │   ├── draft_recommendation_prompt.md
│       │   ├── final_report_prompt.md
│       │   └── task_decomposition_prompt.md
│       │
│       ├── docx/
│       │   ├── final_report_template.docx
│       │   ├── recommendation_template.docx
│       │   ├── pk_review_template.docx
│       │   ├── lkjip_review_template.docx
│       │   └── evidence_audit_template.docx
│       │
│       ├── xlsx/
│       │   ├── indicator_review_template.xlsx
│       │   ├── evidence_audit_template.xlsx
│       │   ├── cascading_matrix_template.xlsx
│       │   ├── rencana_aksi_template.xlsx
│       │   ├── lhe_tindak_lanjut_template.xlsx
│       │   └── task_list_template.xlsx
│       │
│       └── markdown/
│           ├── final_report_template.md
│           ├── indicator_report_template.md
│           ├── pk_review_template.md
│           ├── lkjip_review_template.md
│           ├── cascading_report_template.md
│           ├── evidence_report_template.md
│           ├── rencana_aksi_report_template.md
│           └── lhe_report_template.md
│
├── tests/
│   ├── __init__.py
│   ├── test_config.py
│   ├── test_paths.py
│   ├── test_docx_reader.py
│   ├── test_pdf_reader.py
│   ├── test_xlsx_reader.py
│   ├── test_csv_reader.py
│   ├── test_classifier.py
│   ├── test_chunker.py
│   ├── test_database.py
│   ├── test_repositories.py
│   ├── test_token_manager.py
│   ├── test_model_router.py
│   ├── test_guardrails.py
│   ├── test_indicator_checker.py
│   ├── test_pk_checker.py
│   ├── test_lkjip_checker.py
│   ├── test_evidence_checker.py
│   ├── test_rencana_aksi_checker.py
│   ├── test_lhe_tracker.py
│   ├── test_coherence_checker.py
│   ├── test_result_cache.py
│   ├── test_session_context.py
│   ├── test_context_budget.py
│   ├── test_intent_router.py
│   ├── test_next_step.py
│   ├── test_task_decomposer.py
│   ├── test_report_writer.py
│   ├── test_desk_evaluation.py
│   ├── test_cli_help.py
│   ├── test_cli_init.py
│   ├── test_cli_scan.py
│   └── fixtures/
│       ├── sample_renstra.docx
│       ├── sample_iku.docx
│       ├── sample_pk.docx
│       ├── sample_lkjip.docx
│       ├── sample_lhe.pdf
│       ├── sample_renja.xlsx
│       ├── sample_evidence.pdf
│       ├── sample_config.yaml
│       └── golden/
│           ├── renstra_sample.docx
│           ├── iku_sample.docx
│           ├── pk_2026_sample.docx
│           ├── lkjip_sample.docx
│           ├── lhe_sample.pdf
│           ├── rencana_aksi_sample.xlsx
│           ├── renja_sample.xlsx
│           ├── evidence_sample.pdf
│           ├── expected_scan.json
│           ├── expected_review_indikator.json
│           ├── expected_review_pk.json
│           ├── expected_review_lkjip.json
│           ├── expected_coherence_check.json
│           └── expected_rencana_aksi_review.json
│
├── scripts/
│   ├── dev_setup.sh
│   ├── dev_setup.ps1
│   ├── run_tests.sh
│   ├── run_tests.ps1
│   ├── build_windows.ps1
│   ├── build_linux.sh
│   ├── build_macos.sh
│   ├── install_windows.ps1
│   ├── install_linux.sh
│   ├── install_macos.sh
│   ├── clean_outputs.sh
│   └── clean_outputs.ps1
│
├── examples/
│   ├── README.md
│   ├── sample_workspace/
│   │   ├── Dokumen_SAKIP_OPD/
│   │   │   ├── Renstra_OPD.docx
│   │   │   ├── IKU_OPD.docx
│   │   │   ├── PK_2026.docx
│   │   │   ├── LKjIP_2025.docx
│   │   │   ├── Renja_2026.xlsx
│   │   │   ├── RKA_2026.xlsx
│   │   │   ├── DPA_2026.xlsx
│   │   │   ├── LHE_2025.pdf
│   │   │   ├── Rencana_Aksi_2026.xlsx
│   │   │   ├── Matriks_TL_LHE_2025.xlsx
│   │   │   └── Evidence/
│   │   │       ├── Notulen_Monev_Q1.pdf
│   │   │       ├── Screenshot_eSAKIP.png
│   │   │       └── Rekap_Indikator.xlsx
│   │   └── expected_outputs/
│   │       ├── 01_RINGKASAN_DOKUMEN_OPD.md
│   │       ├── 02_REVIEW_INDIKATOR.xlsx
│   │       └── 07_REKOMENDASI_PERBAIKAN.docx
│   └── sample_config.yaml
│
├── docs/
│   ├── EXECUTIVE_SUMMARY.md
│   ├── SAKIPRO.md
│   ├── SAKIP.md
│   ├── AGENT_SKILLS.md
│   ├── AI_AGENT_TECHNICAL_DESIGN.md
│   ├── CLI_BLUEPRINT.md
│   ├── TASK_MANAGEMENT.md
│   ├── PROMPT_LIBRARY.md
│   ├── COMMANDS.md               # planned
│   ├── USER_GUIDE.md             # planned
│   ├── INSTALL_WINDOWS.md        # planned
│   ├── INSTALL_MACOS.md          # planned
│   ├── INSTALL_LINUX.md          # planned
│   ├── API_KEY_SETUP.md          # planned
│   ├── TROUBLESHOOTING.md        # planned
│   └── DEVELOPMENT.md            # planned
│
├── .github/
│   └── workflows/
│       ├── test.yml
│       ├── build-release.yml
│       └── lint.yml
│
└── dist/
    └── .gitkeep
```

---

## 3. Root Files

### README.md

Dokumentasi utama project.

Isi minimal:

1. Penjelasan SAKIPRO.
2. Fitur utama.
3. Cara install.
4. Cara pakai cepat.
5. Contoh command.
6. Link dokumen teknis.

---

### PRD.md

Product Requirements Document.

Berisi spesifikasi produk, user, fitur, acceptance criteria, dan roadmap.

---

### STACK.md

Dokumen stack teknologi.

Berisi software stack, hardware, packaging, GitHub release, dan library utama.

---

### CLI_UX.md

Blueprint UX CLI.

Berisi desain Rich CLI, slash command, autocomplete, wizard, workbench, banner, help, dan UX terminal.

---

### SCOPE.md

Dokumen pengendali scope v1.0 Core, v1.0 Expanded, dan Post-v1.0.

---

### SAKIP_RULEBOOK.md

Rubrik review indikator, PK, LKjIP, cascading, dan evidence.

---

### AI_CONTRACT.md

Schema input/output AI, source reference, retry, dan guardrail.

---

### PRIVACY.md

Pipeline privacy, data masking, dan aturan log aman.

---

### ERROR_HANDLING.md

Daftar error code, partial success, dan retry policy.

---

### TEST_PLAN.md

Golden dataset, unit test, integration test, dan security test.

---

### PACKAGING.md

Blueprint PyInstaller, bundled assets, dan verification artifact.

---

### RELEASE_CHECKLIST.md

Gate sebelum distribusi v0.2.

---

### TREE.md

Dokumen struktur folder dan file.

---

### INSTALL.md

Panduan instalasi lintas OS.

Isi:

1. Windows.
2. macOS.
3. Linux.
4. pipx.
5. source install.
6. executable release.

---

### USER_GUIDE.md

Panduan user biasa.

Isi:

1. Cara scan folder.
2. Cara review PK.
3. Cara cek indikator.
4. Cara cek LKjIP.
5. Cara membuat laporan.

---

### CHANGELOG.md

Catatan perubahan versi.

---

### LICENSE

Lisensi project.

---

### pyproject.toml

Konfigurasi Python project.

Minimal:

```toml
[project]
name = "sakipro"
version = "0.2.0"
description = "AI CLI Assistant for OPD SAKIP Planning Documents"
requires-python = ">=3.11"

[project.scripts]
sakipro = "sakipro.main:app"

[tool.ruff]
line-length = 100

[tool.pytest.ini_options]
testpaths = ["tests"]
```

---

### uv.lock

Lock file dependency dari uv.

---

### .env.example

Template API Key dan environment.

Contoh:

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

---

### config.example.yaml

Template konfigurasi.

---

### .gitignore

Wajib mengecualikan:

```text
.env
.venv/
__pycache__/
*.pyc
dist/
build/
*.spec
.sakipro/
outputs/
logs/
*.db
*.sqlite
```

---

### .python-version

Berisi:

```text
3.12
```

---

## 4. Package sakipro/

Folder utama source code.

---

### sakipro/__init__.py

Menandai package Python.

---

### sakipro/__main__.py

Agar bisa dijalankan dengan:

```bash
python -m sakipro
```

Isi memanggil app dari main.py.

---

### sakipro/main.py

Entry point utama Typer.

Tugas:

1. Membuat Typer app.
2. Register semua command.
3. Menangani global option.
4. Menjalankan banner jika diperlukan.
5. Menangani exception global.

---

## 5. Folder cli/

Folder command CLI.

---

### cli/commands.py

Aggregator untuk register semua command.

---

### cli/init_cmd.py

Command:

```bash
sakipro init
```

Tugas:

1. Membuat folder `~/.sakipro`.
2. Membuat config.
3. Membuat .env template.
4. Membuat database awal.
5. Membuat folder outputs.

---

### cli/doctor_cmd.py

Command:

```bash
sakipro doctor
```

Tugas:

1. Cek Python version.
2. Cek config.
3. Cek API Key.
4. Cek folder.
5. Cek permission.
6. Cek dependency.
7. Tampilkan hasil dengan Rich panel.

---

### cli/scan_cmd.py

Command:

```bash
sakipro scan <folder>
```

Tugas:

1. Scan folder dokumen.
2. Panggil Folder Scanner Agent.
3. Simpan metadata.
4. Buat ringkasan dokumen.
5. Tampilkan next steps.

---

### cli/status_cmd.py

Command:

```bash
sakipro status
```

Tugas:

1. Tampilkan status project.
2. Tampilkan jumlah dokumen.
3. Tampilkan jumlah evidence.
4. Tampilkan status API.
5. Tampilkan status output.

---

### cli/ask_cmd.py

Command:

```bash
sakipro ask "pertanyaan"
```

Tugas:

1. Cari konteks dari memory.
2. Panggil AI.
3. Tampilkan jawaban.
4. Tampilkan sumber.
5. Tampilkan confidence.

---

### cli/chat_cmd.py

Command:

```bash
sakipro chat
```

Tugas:

1. Jalankan interactive REPL.
2. Mendukung slash command.
3. Mendukung autocomplete.
4. Mendukung command history.

---

### cli/wizard_cmd.py

Command:

```bash
sakipro wizard
```

Tugas:

1. Tampilkan menu interaktif.
2. Arahkan user menjalankan proses.
3. Tampilkan hasil dan saran.

---

### cli/workbench_cmd.py

Command:

```bash
sakipro workbench
```

Tugas:

1. Tampilkan dashboard terminal.
2. Tampilkan menu dokumen, indikator, PK, LKjIP, evidence, report.
3. Jalankan command dari pilihan user.

---

### cli/indicator_cmd.py

Command:

```bash
sakipro cek-indikator
```

Tugas:

1. Panggil Indicator Review Agent.
2. Tampilkan hasil.
3. Generate laporan Markdown dan XLSX.

---

### cli/cascading_cmd.py

Status: v1.0 Expanded.

Command:

```bash
sakipro cek-cascading
```

Tugas:

1. Panggil Cascading Review Agent.
2. Buat relasi sasaran, indikator, program, kegiatan.
3. Tampilkan rantai putus.
4. Generate laporan.

---

### cli/tree_cmd.py

Status: v1.0 Expanded.

Command:

```bash
sakipro cek-pohon
```

Tugas:

1. Bangun pohon kinerja.
2. Render dengan Rich Tree.
3. Simpan output JSON atau Markdown.

---

### cli/pk_cmd.py

Command:

```bash
sakipro review-pk
```

Tugas:

1. Panggil PK Review Agent.
2. Bandingkan PK dengan IKU dan Renstra.
3. Tampilkan target konflik.
4. Generate report.

---

### cli/lkjip_cmd.py

Status: v1.0 Expanded.

Command:

```bash
sakipro review-lkjip
```

Tugas:

1. Panggil LKjIP Review Agent.
2. Cek kesesuaian dengan PK.
3. Cek analisis capaian.
4. Cek efisiensi.
5. Generate report.

---

### cli/evidence_cmd.py

Status: v1.0 Expanded.

Command:

```bash
sakipro cek-evidence
```

Tugas:

1. Panggil Evidence Review Agent.
2. Cocokkan klaim dengan evidence.
3. Tampilkan evidence gap.
4. Generate report.

---

### cli/rencana_aksi_cmd.py

Status: v1.0 Expanded.

Command:

```bash
sakipro review-rencana-aksi
```

Tugas:

1. Panggil RencanaAksiReviewAgent (SKL-024).
2. Periksa kelengkapan milestone triwulanan.
3. Bandingkan dengan indikator PK.
4. Generate report milestone matrix.

---

### cli/lhe_cmd.py

Status: v1.0 Expanded.

Command:

```bash
sakipro cek-tindak-lanjut-lhe
```

Tugas:

1. Panggil LHETrackingAgent (SKL-025).
2. Peta setiap rekomendasi LHE ke status tindak lanjut.
3. Tampilkan matriks tindak lanjut.
4. Generate LHE tindak lanjut report.

---

### cli/draft_cmd.py

Command:

```bash
sakipro draft
```

Tugas:

1. Membuat draft rekomendasi.
2. Membuat draft narasi LKjIP.
3. Membuat draft tindak lanjut LHE.
4. Simpan ke outputs.

---

### cli/task_cmd.py

Command:

```bash
sakipro task "..."
```

Tugas:

1. Pecah task besar.
2. Jalankan agent terkait.
3. Simpan state.
4. Tampilkan task board.

---

### cli/resume_cmd.py

Command:

```bash
sakipro resume
```

Tugas:

1. Ambil session terakhir.
2. Tampilkan progres.
3. Tawarkan lanjut.

---

### cli/report_cmd.py

Status: v1.0 Expanded untuk `report final`; v0.2 hanya membutuhkan report Markdown/XLSX per review indikator dan PK.

Command:

```bash
sakipro report final
```

Tugas:

1. Kumpulkan hasil review.
2. Buat laporan final Markdown, DOCX, XLSX.
3. Tampilkan lokasi file.

---

### cli/token_cmd.py

Command:

```bash
sakipro token
```

Tugas:

1. Tampilkan token harian.
2. Tampilkan token bulanan.
3. Tampilkan estimasi biaya.
4. Tampilkan model paling banyak dipakai.

---

### cli/model_cmd.py

Command:

```bash
sakipro model
```

Tugas:

1. Tampilkan model aktif.
2. Tampilkan model routing.
3. Ubah model jika diperlukan.

---

### cli/privacy_cmd.py

Command:

```bash
sakipro privacy
```

Tugas:

1. Tampilkan privacy mode.
2. Ubah mode open, standard, strict.
3. Tampilkan warning.

---

### cli/config_cmd.py

Command:

```bash
sakipro config
```

Tugas:

1. Lihat konfigurasi.
2. Update konfigurasi tertentu.
3. Validasi config.

---

### cli/output_cmd.py

Command:

```bash
sakipro output
```

Tugas:

1. Tampilkan daftar output.
2. Preview report.
3. Buka lokasi output.

---

## 6. Folder ui/

Folder UI terminal berbasis Rich.

---

### ui/banner.py

Fungsi:

1. print_banner().
2. print_compact_banner().
3. print_silent_mode_notice jika perlu.

---

### ui/theme.py

Berisi warna dan style.

Contoh:

```python
PRIMARY = "cyan"
SUCCESS = "green"
WARNING = "yellow"
ERROR = "red"
```

---

### ui/console.py

Menyediakan instance Rich Console global.

---

### ui/panels.py

Helper membuat panel.

Fungsi:

1. print_startup_panel().
2. print_project_status().
3. print_result_summary().
4. print_sources().
5. print_confidence().

---

### ui/tables.py

Helper membuat tabel Rich.

Fungsi:

1. render_indicator_table().
2. render_pk_table().
3. render_lkjip_table().
4. render_evidence_table().
5. render_task_table().

---

### ui/progress.py

Helper progress bar.

Fungsi:

1. render_progress().
2. run_with_spinner().
3. progress_steps().

---

### ui/prompts.py

Helper input user.

Fungsi:

1. ask_text().
2. ask_confirm().
3. ask_select().
4. ask_multi_select().

---

### ui/autocomplete.py

Autocomplete command dan slash command.

Fungsi:

1. get_command_completer().
2. get_slash_completer().
3. get_context_completer().

---

### ui/repl.py

Interactive chat loop.

Tugas:

1. Menjalankan prompt_toolkit.
2. Menerima slash command.
3. Menjalankan ask biasa.
4. Menyimpan history.

---

### ui/wizard.py

Wizard menu interaktif.

Tugas:

1. Tampilkan menu.
2. Jalankan command sesuai pilihan.
3. Tampilkan next steps.

---

### ui/workbench.py

Terminal workbench.

Tugas:

1. Tampilkan layout utama.
2. Render menu.
3. Render panel utama.
4. Terima input menu.

---

### ui/status_bar.py

Status bar satu baris di bagian bawah terminal selama REPL aktif.

Fungsi:

1. `build_status_bar()` — kembalikan `HTML` string untuk `prompt_toolkit` `bottom_toolbar`.
2. Format: `model | project | docs | token | privacy | ctrl+d keluar`.
3. Di-refresh setiap kali model/token/privacy berubah.

---

### ui/streaming.py

Tampilkan respons AI secara streaming real-time menggunakan `rich.live.Live`.

Fungsi:

1. `stream_ai_response(stream, title)` — tampilkan token satu per satu dalam panel.
2. `live_tool_display(tool_calls)` — tampilkan setiap tool call yang sedang berjalan.

---

### ui/thinking.py

Tampilkan panel Thinking & Step Mode saat AI memproses input.

Fungsi:

1. `thinking_panel(steps)` — panel "Thinking" dengan langkah-langkah berjalan.
2. `chapter_header(name, desc)` — header tebal untuk setiap chapter dalam task panjang.
3. `step_spinner(message)` — satu baris spinner dengan teks dinamis.

---

### ui/plan_mode.py

Tampilkan execution plan sebelum task berat dijalankan.

Fungsi:

1. `show_execution_plan(plan: ExecutionPlan)` — panel rencana dengan estimasi token/biaya per subtask.
2. `confirm_execution()` → `bool` — konfirmasi user: `[y/n/edit]`.

---

### ui/decision_gates.py

Gerbang keputusan interaktif di akhir setiap unit analisis.

Fungsi:

1. `show_decision_gate(options: list[str])` → `int` — tampilkan menu pilihan dan kembalikan pilihan user.

---

### ui/diff.py

Tampilkan perubahan teks yang disarankan AI sebagai before/after diff berwarna.

Fungsi:

1. `render_diff(original, suggestion, confidence)` — diff panel merah/hijau.
2. `render_source_ref(sources: list[SourceRef])` — tampilkan referensi sumber inline.

---

### ui/tree.py

Render `CascadingMap` data struct sebagai Rich Tree. Dipisah dari `sakip/` karena ini adalah rendering, bukan analisis.

Fungsi:

1. `render_kinerja_tree(map: CascadingMap)` — pohon kinerja dengan broken chains ditandai `⚠`.
2. `render_performance_tree(nodes, edges)` — alternatif dari graph data mentah.

---

### ui/help.py

Help kontekstual.

---

### ui/errors.py

Error panel.

Fungsi:

1. print_error().
2. print_file_error().
3. print_api_error().
4. print_privacy_error().

---

### ui/suggestions.py

Saran langkah berikutnya.

Fungsi:

1. suggest_after_scan().
2. suggest_after_indicator().
3. suggest_after_pk().
4. suggest_after_lkjip().
5. suggest_after_evidence().

---

## 7. Folder core/

Core application.

---

### core/settings.py

Load setting dari env dan config.

---

### core/paths.py

Path utama:

1. User home.
2. `~/.sakipro`.
3. outputs.
4. logs.
5. memory.
6. database.

---

### core/logger.py

Konfigurasi loguru.

---

### core/exceptions.py

Custom exception.

Contoh:

1. SakiproError.
2. ConfigError.
3. DocumentReadError.
4. AIProviderError.
5. PrivacyError.

---

### core/constants.py

Konstanta global.

---

### core/version.py

Versi aplikasi.

---

### core/bootstrap.py

Inisialisasi app.

---

### core/app_context.py

Context object untuk command.

Isi:

1. Config.
2. Paths.
3. Database session.
4. Console.
5. Current project.

---

## 8. Folder ai/

Modul AI API dan guardrail.

---

### ai/llm_client.py

Wrapper LiteLLM.

Tugas:

1. Panggil model.
2. Retry.
3. Tangani error.
4. Return response.

---

### ai/model_router.py

Memilih model berdasarkan task.

---

### ai/prompt_manager.py

Membaca prompt dari templates/prompts.

---

### ai/token_manager.py

Hitung token dan estimasi biaya.

---

### ai/guardrails.py

Validasi output AI.

---

### ai/privacy_filter.py

Masking data sensitif.

---

### ai/response_parser.py

Parse output JSON dari AI.

---

### ai/schemas.py

Pydantic schema untuk request dan response AI.

---

### ai/cost_estimator.py

Estimasi biaya token.

---

## 9. Folder agents/

AI Agent utama.

---

### agents/base_agent.py

Class dasar agent.

Wajib memiliki:

1. name.
2. description.
3. run().
4. validate_input().
5. validate_output().
6. log_run().

---

### agents/folder_scanner_agent.py

Membaca folder dokumen, mengklasifikasikan tipe dokumen, dan menghasilkan quick health signals deterministic (SKL-003, SKL-004).

---

### agents/cli_router_agent.py

Status: v1.0 Expanded.

Implementasi SKL-022. Menerima raw user input dari REPL, mendeteksi intent type (slash_command, natural_command, question_factual, question_conceptual, complex_task, ambiguous), dan merutekan ke skill yang tepat. Sepenuhnya deterministik — tidak memanggil AI.

---

### agents/indicator_review_agent.py

Review indikator.

---

### agents/cascading_review_agent.py

Review cascading.

---

### agents/pk_review_agent.py

Review PK.

---

### agents/lkjip_review_agent.py

Review LKjIP.

---

### agents/evidence_review_agent.py

Audit evidence (SKL-012, EVD-001–004 termasuk ketepatan waktu).

---

### agents/rencana_aksi_review_agent.py

Status: v1.0 Expanded.

Review kualitas Rencana Aksi OPD: kelengkapan milestone, keterhubungan dengan PK, dan progress monitoring (SKL-024).

---

### agents/lhe_tracking_agent.py

Status: v1.0 Expanded.

Memetakan setiap rekomendasi LHE ke status tindak lanjut dan buktinya. Menghasilkan matriks tindak lanjut lengkap (SKL-025).

---

### agents/opd_planning_copilot_agent.py

Chat assistant.

---

### agents/draft_agent.py

Draft rekomendasi.

---

### agents/report_agent.py

Menyusun laporan final.

---

### agents/desk_evaluation_agent.py

Simulasi penilaian evaluator: agregasi temuan review, hitung skor per komponen SAKIP, dan estimasi predikat AA–D.

---

### agents/task_agent.py

Memecah task besar.

---

## 10. Folder documents/

Document processing.

---

### documents/base_reader.py

Base reader interface.

---

### documents/docx_reader.py

Baca DOCX.

---

### documents/pdf_reader.py

Baca PDF.

---

### documents/xlsx_reader.py

Baca XLSX.

---

### documents/csv_reader.py

Baca CSV.

---

### documents/txt_reader.py

Baca TXT.

---

### documents/markdown_reader.py

Baca Markdown.

---

### documents/classifier.py

Klasifikasi dokumen.

Jenis:

1. Renstra.
2. Renja.
3. IKU.
4. PK.
5. LKjIP.
6. RKA.
7. DPA.
8. LHE.
9. Evidence.
10. Unknown.

---

### documents/chunker.py

Pecah dokumen menjadi chunk.

---

### documents/metadata.py

Ekstraksi metadata.

---

### documents/file_scanner.py

Scan folder rekursif.

---

### documents/file_registry.py

Register file ke database.

---

### documents/document_service.py

Service level untuk ingest dan scan.

---

## 11. Folder sakip/

Logic domain SAKIP. Semua file di folder ini menghasilkan __data struct__, bukan rendering. Rendering ada di `ui/`.

---

### sakip/rulebook.py

Encodes semua rule ID, severity, kriteria, dan kondisi tidak memenuhi dari `SAKIP_RULEBOOK.md` sebagai Python constants dan dataclasses. Dipakai oleh semua checker agar tidak ada magic string di kode.

Konten:

1. `RuleID` enum: `IND_001` sampai `IND_009`, `PK_001` sampai `PK_006`, `LKJ_001` sampai `LKJ_007`, `CAS_001` sampai `CAS_003`, `EVD_001` sampai `EVD_004`.
2. `RULE_REGISTRY: dict[RuleID, RuleDefinition]` — lookup table berisi severity, kriteria, kondisi tidak memenuhi.
3. `COMPONENT_WEIGHTS: dict[str, float]` — bobot komponen evaluasi: Perencanaan 0.30, Pengukuran 0.30, Pelaporan 0.15, Evaluasi 0.25.

---

### sakip/indicator_checker.py

Logic review indikator.

---

### sakip/cascading_checker.py

Logic review cascading.

---

### sakip/performance_tree.py

Bangun pohon kinerja.

---

### sakip/pk_checker.py

Logic review PK.

---

### sakip/lkjip_checker.py

Logic review LKjIP.

---

### sakip/evidence_checker.py

Logic audit evidence.

---

### sakip/consistency_checker.py

Cek konsistensi antar dokumen.

---

### sakip/recommendation_builder.py

Bangun rekomendasi perbaikan.

---

### sakip/desk_scorer.py

Status: v1.0 Expanded.

Logic skoring desk evaluation (SKL-021). Mengagregasi semua temuan review, menghitung skor per komponen, dan menghasilkan estimasi predikat.

Tugas:

1. Terima `AggregatedFindings` dari semua review agent.
2. Terapkan bobot dari `rulebook.COMPONENT_WEIGHTS`.
3. Hitung skor per komponen: Perencanaan, Pengukuran, Pelaporan, Evaluasi Internal.
4. Hasilkan `simulated_score`, `predicted_predicate` (AA–D), `component_breakdown`.
5. Tandai output sebagai `draft` dan `needs_human_validation=True`.

---

### sakip/quality_gate.py

Cek kelayakan output.

---

### sakip/sakip_terms.py

Kamus istilah SAKIP.

---

## 12. Folder memory/

Memory dan retrieval.

---

### memory/vector_store.py

[Ditiadakan] — Modul vector store ditiadakan sepenuhnya demi efisiensi memori. SAKIPRO secara eksklusif menggunakan pencarian berbasis teks penuh SQLite FTS5 (BM25).

---

### memory/graph_store.py

Wrapper NetworkX untuk v0.2.

---

### memory/search.py

Search dokumen.

---

### memory/retrieval.py

Retrieval untuk RAG.

---

### memory/indexer.py

Index dokumen ke SQLite chunk storage dan FTS5 index lokal. Pustaka vector store ditiadakan.

---

### memory/memory_manager.py

Koordinator ketiga tier memory (Persistent/Session/Working). Satu-satunya pintu masuk untuk semua operasi memory dari agent dan skill.

Fungsi:

1. `get_context_for_skill(skill_id, query, query_type, token_budget)` → `ContextBundle`.
2. `store_skill_result(skill_id, result, cache_key)` — simpan ke persistent + update session.
3. `check_result_cache(cache_key)` → `SkillResult | None`.

---

### memory/context_builder.py

Susun konteks prompt AI dengan token budget controller.

Fungsi:

1. `build_context(query, chunks, history, budget: ContextBudget)` → `PromptBundle`.
2. Potong chunks ke alokasi `document_chunks` budget.
3. Tandai bagian yang cacheable (system prompt + doc chunks).

---

### memory/result_cache.py

Cache hasil skill review berbasis hash dokumen. Komponen utama token saving.

Tugas:

1. `compute_cache_key(skill_id, workspace_id, doc_hashes)` → `str`.
2. `get(cache_key)` → `SkillResult | None` — kembalikan hasil tersimpan jika valid.
3. `put(cache_key, result, tokens_saved)` — simpan ke SQLite `review_cache` table.
4. `invalidate_for_documents(doc_paths)` — hapus semua cache entry yang melibatkan file yang berubah.
5. Log `tokens_saved` setiap cache hit untuk laporan penghematan.

---

### memory/session_context.py

Session memory untuk satu sesi REPL aktif. Hilang saat terminal ditutup.

Konten: `conversation_history` (max 20 turns FIFO), `review_state`, `last_skill_result`, `active_task_id`.

Tugas:

1. `add_turn(role, content)` — tambah satu turn, hapus yang tertua jika > 20.
2. `get_recent_turns(n)` → `list[Turn]` — ambil N turns terakhir untuk context window.
3. `update_review_state(result: SkillResult)` — perbarui apa yang sudah direview.

---

### memory/context_budget.py

Definisi dan kalkulasi token budget allocation per AI call.

Konten:

1. `ContextBudget` dataclass: `system_prompt=1500`, `skill_instructions=500`, `document_chunks=20000`, `conversation_history=3000`, `user_query=500`, `safety_margin=6000`.
2. `get_budget_for_skill(skill_id)` → `ContextBudget` — override budget berdasarkan skill (SKL-008 lebih sedikit dari SKL-010).
3. `calculate_remaining(used_tokens, budget)` → sisa tokens untuk chunks.

---

## 13. Folder storage/

Database lokal.

---

### storage/database.py

Koneksi SQLite.

---

### storage/models.py

SQLAlchemy models.

Model utama:

1. Document — metadata file terindeks.
2. DocumentChunk — potongan dokumen yang sudah diekstrak.
3. SourceRef — rujukan sumber untuk setiap temuan.
4. Indicator — indikator kinerja yang diekstrak.
5. EvidenceFile — file evidence yang ditemukan.
6. Review — hasil review skill (header).
7. Task — task orchestration record.
8. TaskSubtask — subtask individual dalam task plan.
9. TaskDependency — relasi dependency antar subtask.
10. TaskEvent — audit log event task execution.
11. ReviewCache — result cache dengan cache_key, skill_id, document_hashes, result_json, tokens_saved.
12. TokenUsage — log penggunaan token per AI call.
13. AgentRun — log eksekusi agent.

---

### storage/repositories.py

Repository pattern.

---

### storage/migrations.py

Migration sederhana.

---

### storage/seed.py

Seed data awal.

---

### storage/unit_of_work.py

Transaction helper.

---

## 14. Folder reports/

Generator laporan.

---

### reports/markdown_report.py

Generate Markdown.

---

### reports/xlsx_report.py

Generate XLSX.

---

### reports/docx_report.py

Generate DOCX.

---

### reports/json_report.py

Generate JSON.

---

### reports/final_report.py

Gabungkan semua hasil review menjadi laporan final.

---

### reports/indicator_report.py

Laporan indikator.

---

### reports/pk_report.py

Laporan PK.

---

### reports/lkjip_report.py

Laporan LKjIP.

---

### reports/cascading_report.py

Laporan cascading.

---

### reports/evidence_report.py

Laporan evidence.

---

### reports/report_paths.py

Naming output file.

---

## 15. Folder tasks/

Task engine — orchestrator dua level (direct execution dan task plan).

---

### tasks/task_model.py

Pydantic dan SQLAlchemy model untuk Task, TaskSubtask, TaskDependency, TaskEvent. Termasuk status enum dan field `execution_level` (direct/task_plan).

---

### tasks/task_templates.py

Kumpulan template task statis untuk SAKIP workflows yang sudah diketahui. Dipakai oleh `task_decomposer.py` dengan pendekatan template-first — tidak perlu AI call untuk request yang cocok template.

Template tersedia:

1. `FULL_SAKIP_REVIEW` — 15 subtask dari scan sampai laporan final.
2. `INDICATOR_IMPROVEMENT` — 7 subtask review indikator + cross-doc coherence.
3. `PK_CONSISTENCY` — 7 subtask review PK.
4. `EVIDENCE_GAP` — 6 subtask audit evidence.
5. `LKJIP_REVIEW` — review LKjIP termasuk multi-tahun.

---

### tasks/task_decomposer.py

Decompose perintah user menjadi task plan. Template-first: coba cocokkan ke `task_templates.py` dulu. Hanya panggil AI (SKL-018 light) jika tidak ada template yang cocok.

---

### tasks/task_runner.py

Jalankan task plan dua level. Untuk direct execution: panggil skill langsung tanpa Task record. Untuk task plan: kelola SubtaskContext, model routing per tier, result cache check, dan status tracking.

---

### tasks/task_state.py

Simpan dan transisi status task/subtask. Validasi transisi state yang tidak valid.

---

### tasks/task_history.py

Riwayat task untuk resume. Simpan SubtaskContext ke persistent store agar bisa dilanjutkan setelah restart.

---

### tasks/task_board.py

Menghasilkan `TaskBoardData` struct untuk ditampilkan oleh `ui/tables.py`. Tidak ada rendering Rich di sini — hanya data. Berisi status setiap subtask, cache_hit flag, tokens_saved, dan output paths.

---

### tasks/task_suggestions.py

Implementasi SKL-023 (Contextual Next-Step Recommendation Skill). Menghasilkan tepat 3 rekomendasi berbasis `ReviewState` saat ini. Sepenuhnya deterministik — tidak memanggil AI.

---

### tasks/skill_registry.py

Registry statis semua 26 skill (SKL-001 sampai SKL-026). Setiap entry berisi skill_id, agent, command, execution_tier, cacheable flag, dan capabilities. Satu-satunya sumber kebenaran untuk routing skill.

---

### tasks/subtask_context.py

`SubtaskContext` dataclass — context yang dibangun secara kumulatif selama task berjalan. Subtask yang selesai menulis outputnya ke sini; subtask berikutnya membaca dari sini tanpa re-ekstraksi dokumen.

---

## 16. Folder config/

Konfigurasi.

---

### config/config_loader.py

Load YAML config.

---

### config/env_loader.py

Load .env.

---

### config/config_writer.py

Tulis config.

---

### config/defaults.py

Default config.

---

### config/validation.py

Validasi config.

---

## 17. Folder utils/

Utility umum.

---

### utils/datetime_utils.py

Tanggal dan waktu.

---

### utils/file_utils.py

Helper file.

---

### utils/text_utils.py

Helper teks.

---

### utils/slug_utils.py

Slug nama file.

---

### utils/table_utils.py

Helper tabel.

---

### utils/json_utils.py

Helper JSON.

---

### utils/money_utils.py

Format biaya token.

---

### utils/safe_write.py

Menulis file secara aman tanpa menimpa file asli.

---

## 18. Folder templates/

Template prompt dan laporan.

---

### templates/prompts/

Berisi prompt AI.

---

### templates/docx/

Template DOCX.

---

### templates/xlsx/

Template XLSX.

---

### templates/markdown/

Template Markdown.

---

## 19. Folder tests/

Unit dan integration test.

Minimal test:

1. Config.
2. Reader.
3. Classifier.
4. Chunker.
5. Database.
6. Token manager.
7. Guardrail.
8. Checker.
9. Report.
10. Desk evaluation.
11. CLI help.
12. CLI init.
13. CLI scan.

---

## 20. Folder scripts/

Script pendukung.

---

### scripts/dev_setup.sh

Setup development di Linux/macOS.

---

### scripts/dev_setup.ps1

Setup development di Windows.

---

### scripts/run_tests.sh dan run_tests.ps1

Menjalankan test.

---

### scripts/build_windows.ps1

Build executable Windows.

---

### scripts/build_linux.sh

Build executable Linux.

---

### scripts/build_macos.sh

Build executable macOS.

---

### scripts/install_windows.ps1

Installer ringan Windows.

---

### scripts/install_linux.sh

Installer ringan Linux.

---

### scripts/install_macos.sh

Installer ringan macOS.

---

### scripts/clean_outputs.sh dan clean_outputs.ps1

Membersihkan output sementara.

---

## 21. Folder examples/

Contoh workspace dan sample dokumen.

Dipakai untuk:

1. Demo.
2. Test manual.
3. Dokumentasi user.
4. Validasi output.

---

## 22. Folder docs/

Dokumen teknis dan user.

---

### docs/COMMANDS.md

Daftar command.

---

### docs/USER_GUIDE.md

Panduan user.

---

### docs/INSTALL_WINDOWS.md

Panduan Windows.

---

### docs/INSTALL_MACOS.md

Panduan macOS.

---

### docs/INSTALL_LINUX.md

Panduan Linux.

---

### docs/API_KEY_SETUP.md

Panduan API Key.

---

### docs/TROUBLESHOOTING.md

Masalah umum.

---

### docs/DEVELOPMENT.md

Panduan developer.

---

## 23. Folder .github/workflows/

CI/CD GitHub Actions.

---

### test.yml

Menjalankan test.

---

### build-release.yml

Build release artifact.

---

### lint.yml

Menjalankan ruff.

---

## 24. Folder dist/

Output build executable.

Isi tidak masuk Git kecuali .gitkeep.

---

## 25. Prioritas Coding v0.2

Urutan ini dioptimalkan berdasarkan dependency teknis dan value yang dihasilkan.

### Grup 1 — Core Infrastructure (Wajib, lakukan lebih dulu)

1. `core/` — settings, paths, logger, exceptions, bootstrap.
2. `config/` — config_loader, env_loader, defaults, validation.
3. `storage/` — database, models (termasuk ReviewCache), repositories, unit_of_work.
4. `utils/` — file_utils, safe_write, json_utils, datetime_utils.
5. `cli/` init_cmd, doctor_cmd — workspace setup dan health check.

### Grup 2 — Document Processing

1. `documents/` — base_reader, docx_reader, pdf_reader, xlsx_reader, classifier, file_scanner.
2. `memory/indexer.py` — incremental indexing, hash tracking.
3. `cli/scan_cmd.py` + `agents/folder_scanner_agent.py` — scan + health signals.

### Grup 3 — AI & Memory Core

1. `ai/llm_client.py` — LiteLLM wrapper dengan prompt caching support.
2. `ai/model_router.py` — tier routing (no_ai/light/default/reasoning).
3. `ai/token_manager.py`, `ai/cost_estimator.py` — token tracking dan estimasi.
4. `ai/privacy_filter.py`, `ai/guardrails.py` — privacy pipeline dan AI contract.
5. `memory/result_cache.py` — cache berbasis hash, komponen token saving utama.
6. `memory/session_context.py`, `memory/context_budget.py`, `memory/context_builder.py`.
7. `memory/retrieval.py`, `memory/search.py` — SQLite FTS/BM25 retrieval.

### Grup 4 — Task & Routing Engine

1. `tasks/skill_registry.py` — registry SKL-001–026.
2. `tasks/subtask_context.py`, `tasks/task_model.py` — data structs.
3. `agents/cli_router_agent.py` (SKL-022) — REPL routing, deterministic.
4. `tasks/task_templates.py` — static task templates.
5. `tasks/task_runner.py` — two-level execution, direct + task plan.

### Grup 5 — SAKIP Domain & Core Review

1. `sakip/rulebook.py` — rule ID constants dan COMPONENT_WEIGHTS.
2. `sakip/indicator_checker.py` + `agents/indicator_review_agent.py` — cek-indikator.
3. `sakip/pk_checker.py` + `agents/pk_review_agent.py` — review-pk.
4. `sakip/coherence_checker.py` — cross-document coherence (SKL-026).
5. `ai/response_parser.py`, `ai/schemas.py` — validasi output AI.
6. `reports/` markdown_report, xlsx_report, report_paths — output Markdown/XLSX.

### Grup 6 — UI & Interactive REPL

1. `ui/` banner, theme, console, panels, tables, progress, errors — UI dasar.
2. `ui/` repl, autocomplete, status_bar, streaming, thinking — REPL interaktif.
3. `ui/` plan_mode, decision_gates, diff, suggestions, tree — advanced UI.
4. `tasks/task_suggestions.py` (SKL-023) — next-step recommendations.

### Grup 7 — Expanded Skills

1. `agents/opd_planning_copilot_agent.py` (SKL-007) — ask/chat.
2. `agents/lkjip_review_agent.py` + `sakip/lkjip_checker.py`.
3. `agents/cascading_review_agent.py` + `sakip/cascading_checker.py`.
4. `agents/evidence_review_agent.py` + `sakip/evidence_checker.py`.
5. `agents/rencana_aksi_review_agent.py` + `sakip/rencana_aksi_checker.py`.
6. `agents/lhe_tracking_agent.py` + `sakip/lhe_tracker.py`.
7. `sakip/desk_scorer.py` + `agents/desk_evaluation_agent.py`.
8. `agents/draft_agent.py`, `reports/final_report.py`, `reports/docx_report.py`.

### Grup 8 — Packaging & QA

1. Golden tests dengan fixture dataset.
2. Wizard mode (`ui/wizard.py`) jika Should Have diaktifkan.
3. `tasks/task_decomposer.py`, `tasks/task_state.py`, `tasks/task_history.py` — resume.
4. PyInstaller build + `install.bat` + smoke test.

---

## 26. v0.2 Minimum Files

File minimum yang wajib ada agar v1.0 Core hidup:

```text
sakipro/
├── pyproject.toml
├── README.md
├── .env.example
├── config.example.yaml
├── sakipro/
│   ├── __init__.py
│   ├── main.py
│   ├── cli/
│   │   ├── __init__.py
│   │   ├── init_cmd.py
│   │   ├── doctor_cmd.py
│   │   ├── scan_cmd.py
│   │   ├── ask_cmd.py
│   │   ├── indicator_cmd.py
│   │   ├── pk_cmd.py
│   │   ├── token_cmd.py
│   │   └── privacy_cmd.py
│   ├── ui/
│   │   ├── banner.py
│   │   ├── console.py
│   │   ├── panels.py
│   │   ├── tables.py
│   │   ├── progress.py
│   │   ├── repl.py
│   │   ├── autocomplete.py
│   │   ├── errors.py
│   │   └── suggestions.py
│   ├── core/
│   │   ├── settings.py
│   │   ├── paths.py
│   │   ├── logger.py
│   │   └── exceptions.py
│   ├── ai/
│   │   ├── llm_client.py
│   │   ├── model_router.py
│   │   ├── token_manager.py
│   │   ├── privacy_filter.py
│   │   ├── response_parser.py
│   │   ├── cost_estimator.py
│   │   └── guardrails.py
│   ├── agents/
│   │   ├── base_agent.py
│   │   ├── folder_scanner_agent.py
│   │   ├── cli_router_agent.py
│   │   ├── indicator_review_agent.py
│   │   ├── pk_review_agent.py
│   │   └── opd_planning_copilot_agent.py
│   ├── documents/
│   │   ├── docx_reader.py
│   │   ├── pdf_reader.py
│   │   ├── xlsx_reader.py
│   │   ├── classifier.py
│   │   └── file_scanner.py
│   ├── sakip/
│   │   ├── indicator_checker.py
│   │   ├── pk_checker.py
│   │   ├── coherence_checker.py
│   │   └── sakip_terms.py
│   ├── storage/
│   │   ├── database.py
│   │   ├── models.py
│   │   ├── repositories.py
│   │   └── source_refs.py
│   ├── memory/
│   │   ├── search.py
│   │   ├── retrieval.py
│   │   ├── indexer.py
│   │   ├── result_cache.py
│   │   ├── session_context.py
│   │   ├── context_budget.py
│   │   └── context_builder.py
│   ├── tasks/
│   │   ├── skill_registry.py
│   │   └── subtask_context.py
│   └── reports/
│       ├── markdown_report.py
│       ├── xlsx_report.py
│       └── report_paths.py
└── tests/
```

---

## 27. Acceptance Criteria TREE

Struktur project dianggap siap jika:

1. Semua folder utama tersedia.
2. Semua file v1.0 Core tersedia.
3. `sakipro main.py` dapat menjalankan Typer app.
4. `sakipro --help` tampil.
5. `sakipro doctor` berjalan.
6. `sakipro init` membuat folder runtime.
7. `sakipro scan` membaca folder contoh.
8. Template prompt tersedia.
9. Template report tersedia.
10. Test folder tersedia.

---

## 28. Final Notes for Vibe Coding AI Agent

Instruksi untuk AI coding agent yang akan mengimplementasikan SAKIPRO:

### Arsitektur

1. Ikuti struktur folder ini persis — jangan menggabungkan tanggung jawab dalam satu file.
2. Buat file kecil dan modular, gunakan type hint di semua fungsi publik.
3. Pisahkan CLI, Agent, Skill/Domain, Storage secara ketat. Tidak ada import silang yang melanggar layer.
4. `sakip/` menghasilkan data struct saja. `ui/` merender. Tidak ada `console.print()` di `sakip/` atau `agents/`.
5. `ui/tree.py` merender `CascadingMap`. `sakip/performance_tree.py` membangun datanya. Keduanya tidak saling import.

### Token dan Memory

1. Setiap AI call harus melalui `ai/llm_client.py` — tidak ada `litellm.completion()` langsung di agent.
2. Sebelum memanggil AI, cek `memory/result_cache.py` terlebih dahulu.
3. Semua token usage dicatat via `ai/token_manager.py`.
4. Context window dibangun via `memory/context_builder.py` dengan `ContextBudget`.
5. System prompt dan document chunks harus ditandai cacheable untuk prompt caching.

### Review dan Safety

1. Semua output AI diberi status `draft=True` dan `confidence` score.
2. Semua temuan faktual harus memiliki `source_refs` yang resolve ke database.
3. Semua rule ID yang dipakai harus ada di `sakip/rulebook.py` — tidak ada magic string rule ID.
4. File asli tidak boleh dimodifikasi atau dihapus. Gunakan `safe_write` untuk semua output.
5. Semua laporan disimpan ke folder `outputs/` dengan nama dari `reports/report_paths.py`.

### UI dan UX

1. Setiap proses panjang memakai `ui/progress.py` atau `ui/thinking.py` — tidak ada proses diam tanpa feedback.
2. Setiap respons REPL diakhiri SKL-023 via `tasks/task_suggestions.py`.
3. Banner dan semua UI dapat dimatikan via `--silent` atau `ui.banner: none` di config.

### Testing

1. Setiap skill baru harus punya minimal satu unit test dan satu golden fixture test.
2. Mock AI harus tersedia untuk semua skill yang memanggil AI — jangan test dengan live API call.
3. `tests/fixtures/golden/` berisi expected JSON output untuk setiap review skill.

---

END OF TREE.md
