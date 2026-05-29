# SAKIPRO Task & Memory Management Blueprint

Version: 1.0
Date: 2026-05-28
Document Type: Task Management, Skill Routing, and Memory Architecture Blueprint
Audience: AI Engineer, Python Developer, Product Owner, QA Tester
Status: Implementation Blueprint
Changes from v0.2: Two-level task model; model routing per subtask tier; result cache; context sharing; three-tier memory; prompt caching; token budget controller; incremental indexing; updated skill registry (SKL-022–026).

---

## 1. Spesifikasi Operasional v1.0

## 2. Prinsip Task Management

1. Task panjang harus dipecah menjadi subtask kecil yang jelas.
2. Setiap subtask harus memiliki `skill_id` yang eksplisit dari skill registry.
3. Subtask hanya boleh berjalan jika dependency sudah selesai.
4. Subtask yang memakai AI wajib melewati privacy pipeline dan token preflight.
5. Subtask review wajib menghasilkan source refs.
6. Subtask tidak boleh mengubah file asli.
7. Hasil setiap subtask harus disimpan agar dapat di-resume.
8. Jika satu subtask gagal, task utama tidak kehilangan semua hasil subtask lain.
9. User mendapat ringkasan progress, failure, warning, dan next steps.
10. **Template deterministik didahulukan sebelum AI decomposition** — jangan panggil AI untuk memecah task yang sudah punya template.
11. **Model di-route per bobot subtask** — ekstraksi ringan pakai light model; analisis mendalam pakai default model.
12. **Output subtask di-cache** — jika dokumen tidak berubah, hasil review tidak diulang.
13. **Context di-share antar subtask** — output subtask sebelumnya dipakai sebagai input subtask berikutnya tanpa re-ekstraksi.
14. **Single-step operations tidak butuh task plan overhead** — REPL command biasa berjalan langsung tanpa membuat Task record.

---

## 3. Dua Level Eksekusi

Ini adalah perbaikan utama dari v0.2. Tidak semua pekerjaan perlu overhead Task + Subtask + Dependency records.

### Level 1 — Direct Execution (Mayoritas operasi)

Untuk operasi satu skill yang dipicu dari REPL atau command langsung. Tidak ada task plan, tidak ada database record overhead.

Contoh:

```text
/review-pk          → langsung panggil PKReviewAgent → tampilkan hasil → selesai
/cek-indikator      → langsung panggil IndicatorReviewAgent → tampilkan hasil
apa kelemahan IKU?  → langsung panggil CopilotAgent → tampilkan jawaban
```

Flow direct execution:

```text
SKL-022 (route input) → skill dipanggil langsung
  → privacy preflight
  → token preflight (jika AI)
  → result cache check (skip AI jika hit)
  → jalankan skill
  → simpan result ke cache
  → tampilkan output
  → SKL-023 (next-step recommendations)
```

Tidak ada Task, Subtask, atau Dependency record. Overhead minimal.

### Level 2 — Task Plan Execution (Operasi multi-skill)

Untuk perintah yang memerlukan lebih dari satu skill berjalan dalam urutan, atau perintah yang butuh resume. Task Plan dibuat, divalidasi, ditampilkan ke user untuk konfirmasi, lalu dieksekusi.

Contoh:

```text
"review semua dokumen SAKIP OPD saya"
"buat laporan perbaikan lengkap"
/task review-full
```

Trigger untuk Level 2:

- Input dideteksi SKL-022 sebagai `complex_task`
- User secara eksplisit mengetik `/task`
- Jumlah estimated tokens > threshold (default: 40.000)

---

## 4. Scope Versi

| Version | Task Management Scope |
| --- | --- |
| v1.0 Core | Direct execution untuk semua skill Core; Skill Registry; result cache; token budget per subtask. |
| v0.2 Should Have | Task Plan untuk alur review lengkap; resume; lite task decomposer dengan template-first. |
| v1.0 Expanded | Context sharing protokol antar subtask; model routing otomatis per subtask tier. |
| Post-v1.0 | AI-assisted task decomposition untuk request tidak terstruktur; task board penuh; dependency graph visual. |

---

## 5. Skill Registry

Skill registry adalah sumber kebenaran tunggal. Task manager, SKL-022, dan semua routing tidak boleh memilih agent secara bebas tanpa registry.

### 5.1 Registry Schema

```json
{
  "skill_id": "SKL-008",
  "skill_name": "Indicator Review Skill",
  "agent": "IndicatorReviewAgent",
  "command": "sakipro cek-indikator",
  "status": "v0.2",
  "execution_tier": "default",
  "requires_ai": true,
  "requires_source_refs": true,
  "requires_privacy_pipeline": true,
  "requires_token_preflight": true,
  "cacheable": true,
  "cache_key_fields": ["workspace_id", "document_hashes"],
  "capabilities": [
    "extract_indicators",
    "review_indicator_quality",
    "check_formula",
    "check_unit",
    "check_data_source",
    "check_baseline",
    "check_target_consistency",
    "check_target_realism",
    "check_proxy_validity"
  ],
  "required_inputs": ["workspace_id", "indexed_documents", "source_refs"],
  "optional_inputs": ["year", "document_filters"],
  "outputs": ["indicator_findings", "indicator_report_markdown", "indicator_report_xlsx"]
}
```

### 5.2 Execution Tier per Skill

Setiap skill diberi tier yang menentukan model AI yang dipakai:

| Tier | Model Used | Token Cost | Contoh Skill |
| --- | --- | --- | --- |
| `no_ai` | — | 0 | SKL-001, SKL-002, SKL-003, SKL-004, SKL-022, SKL-023 |
| `light` | gemini-flash / gpt-4o-mini / claude-sonnet-4-20250514 (API Key Ready) | ~0.15 USD/1M | SKL-006 (extraction only), SKL-018, SKL-025 |
| `default` | gpt-4o / gemini-1.5-pro / claude-sonnet-4-20250514 (API Key Ready) | ~2.50 USD/1M | SKL-007, SKL-008, SKL-009, SKL-010, SKL-012, SKL-013 |
| `reasoning` | claude-3-5-sonnet / o3 / claude-sonnet-4-20250514 (API Key Ready) | ~15 USD/1M | SKL-021, SKL-026 (conflict analysis) |

Model routing otomatis:

- Skill dengan tier `light` selalu memakai `SAKIPRO_LIGHT_MODEL` dari config
- Skill dengan tier `default` memakai `SAKIPRO_DEFAULT_MODEL`
- Skill dengan tier `reasoning` memakai `SAKIPRO_REASONING_MODEL`
- User bisa override per-call tapi diberi warning estimasi biaya

### 5.3 Core Skill Registry

| Skill ID | Agent | Command | Tier | Cacheable | Status |
| --- | --- | --- | --- | --- | --- |
| `SKL-001` | Init flow | `sakipro init` | `no_ai` | No | v0.2 |
| `SKL-002` | Doctor flow | `sakipro doctor` | `no_ai` | No | v0.2 |
| `SKL-003` | FolderScannerAgent | `sakipro scan` | `no_ai` | No | v0.2 |
| `SKL-004` | FolderScannerAgent | `sakipro scan` | `no_ai` | Yes | v0.2 |
| `SKL-005` | Shared | internal | `no_ai` | No | v0.2 |
| `SKL-006` | Shared | internal | `light` | Yes | v0.2 |
| `SKL-007` | OPDPlanningCopilotAgent | `sakipro ask`, REPL | `default` | No | v0.2 |
| `SKL-008` | IndicatorReviewAgent | `sakipro cek-indikator` | `default` | Yes | v0.2 |
| `SKL-009` | PKReviewAgent | `sakipro review-pk` | `default` | Yes | v0.2 |
| `SKL-010` | LKjIPReviewAgent | `sakipro review-lkjip` | `default` | Yes | v0.2 |
| `SKL-011` | CascadingReviewAgent | `sakipro cek-cascading` | `default` | Yes | v0.2 |
| `SKL-012` | EvidenceReviewAgent | `sakipro cek-evidence` | `default` | Yes | v0.2 |
| `SKL-013` | DraftAgent | `sakipro draft` | `default` | No | v0.2 |
| `SKL-014` | Shared | internal | `no_ai` | No | v0.2 |
| `SKL-015` | Shared | internal | `no_ai` | No | v0.2 |
| `SKL-016` | Shared | internal | `no_ai` | No | v0.2 |
| `SKL-017` | ReportAgent | `sakipro report` | `no_ai` | No | v0.2 |
| `SKL-018` | TaskAgent | `sakipro task` | `light` | No | v0.2 Should Have |
| `SKL-019` | Shared | `sakipro model` | `no_ai` | No | v0.2 Should Have |
| `SKL-020` | Shared | `sakipro config set-key` | `no_ai` | No | v0.2 Should Have |
| `SKL-021` | DeskEvaluationAgent | `sakipro report final` | `reasoning` | Yes | v1.0 Expanded |
| `SKL-022` | CLIRouterAgent | REPL internal | `no_ai` | No | v1.0 Expanded |
| `SKL-023` | Shared | internal | `no_ai` | No | v1.0 Expanded |
| `SKL-024` | RencanaAksiReviewAgent | `sakipro review-rencana-aksi` | `default` | Yes | v1.0 Expanded |
| `SKL-025` | LHETrackingAgent | `sakipro cek-tindak-lanjut-lhe` | `light` | Yes | v1.0 Expanded |
| `SKL-026` | Shared (cross-doc) | internal | `reasoning` | Yes | v1.0 Expanded |

---

## 6. Result Cache

Result cache adalah komponen kritis untuk efisiensi token. Sebelum memanggil AI untuk review, sistem memeriksa apakah hasil yang sama sudah ada dan masih valid.

### 6.1 Cache Key

```python
cache_key = sha256(
    skill_id
    + workspace_id
    + sorted(document_hashes)   # hash SHA256 setiap file yang relevan
    + rule_ids                   # rule yang dipakai
    + model_id                   # model yang dipakai
)
```

### 6.2 Cache Invalidation

Cache untuk skill X diinvalidasi jika:

- File yang di-hash oleh skill X berubah (ukuran atau mtime berbeda)
- Skill version di registry berubah
- Model berubah
- Privacy mode berubah (bisa mempengaruhi chunks yang masuk konteks)

### 6.3 Cache Storage

```python
# SQLite table: review_cache
{
    "cache_key": "sha256_hash",
    "skill_id": "SKL-008",
    "workspace_id": "ws_001",
    "document_hashes_json": "[{...}]",
    "result_json": "{...}",        # full SkillResult JSON
    "created_at": "2026-05-28T10:00:00",
    "expires_at": None,            # None = tidak expire, hanya diinvalidasi by hash
    "token_saved": 14200           # berapa token yang dihemat dari cache hit
}
```

### 6.4 Cache Hit Flow

```text
User: /review-pk
  → result cache check:
      key = hash(SKL-009, ws_001, [pk_hash, iku_hash, renstra_hash])
      HIT → tampilkan hasil cached + label "(dari cache — dokumen belum berubah)"
      MISS → jalankan full review, simpan ke cache
```

Target cache hit rate untuk operasi rutin: >80%.

---

## 7. Context Sharing antar Subtask

Ini adalah optimasi penting untuk Task Plan (Level 2). Subtask yang sudah selesai mewariskan output ke subtask berikutnya tanpa mengekstrak ulang dari dokumen.

### 7.1 Shared Context Protocol

```python
@dataclass
class SubtaskContext:
    """Context yang dibangun secara kumulatif selama task berjalan."""
    indexed_documents: list[DocumentMeta]    # dari SKL-003, SKL-004
    source_refs: list[SourceRef]             # dari SKL-005
    extracted_indicators: list[Indicator]    # dari SKL-008 (dipakai SKL-009, SKL-026)
    extracted_pk_data: PKData | None         # dari SKL-009 (dipakai SKL-010, SKL-021)
    extracted_lkjip_data: LKjIPData | None   # dari SKL-010 (dipakai SKL-012, SKL-021)
    cascading_map: CascadingMap | None       # dari SKL-011 (dipakai SKL-021)
    evidence_matrix: EvidenceMatrix | None   # dari SKL-012 (dipakai SKL-021)
    coherence_findings: list[CoherenceReport]  # dari SKL-026 (dipakai semua review)
```

### 7.2 Context Flow dalam Full Review Task

```text
Step 1: SKL-003 scan → mengisi indexed_documents + source_refs
Step 2: SKL-004 classify → menambah doc_type ke indexed_documents
Step 3: SKL-006 retrieval → mengambil chunks dari indexed_documents (shared)
Step 4: SKL-008 → ekstrak indicators → simpan ke shared context
Step 5: SKL-026 → pakai indicators dari shared context, tidak re-ekstraksi
Step 6: SKL-009 → pakai extracted_indicators dari shared context (tidak re-ekstraksi)
Step 7: SKL-010 → pakai pk_data dari shared context
...
```

**Token yang dihemat**: Tanpa context sharing, setiap review agent mengekstrak ulang indikator dari dokumen masing-masing. Dengan sharing, ekstraksi terjadi sekali dan hasilnya dipakai semua. Estimasi hemat: 30–50% total token untuk full review.

---

## 8. Token Budget Allocation

Sebelum task plan dieksekusi, hitung dan alokasikan token budget per subtask.

### 8.1 Budget Planning

```python
def plan_token_budget(subtasks: list[Subtask], total_budget: int) -> BudgetPlan:
    # Subtask no_ai mendapat 0 token allocation
    # Subtask light mendapat estimasi berdasarkan ukuran dokumen
    # Subtask default mendapat estimasi berdasarkan rule count × chunk size
    # Subtask reasoning mendapat estimasi berdasarkan finding count
    ...
```

### 8.2 Budget Enforcement

```text
Jika estimated_total > config.ask_confirmation_above_tokens:
    → Tampilkan execution plan dengan estimasi per subtask
    → Tawarkan: (1) Jalankan penuh, (2) Jalankan hanya Core subtasks, (3) Pilih model hemat, (4) Batalkan

Jika satu subtask melebihi budget-nya saat berjalan:
    → Potong retrieval chunks ke jumlah yang cukup
    → Atau minta konfirmasi user untuk continue
```

### 8.3 Smart Chunk Targeting

Untuk setiap review skill, hanya ambil chunks yang relevan — bukan semua chunk dari semua dokumen.

```python
CHUNK_BUDGET = {
    "SKL-008": 4000,   # indikator review: tabel indikator saja
    "SKL-009": 6000,   # PK review: sasaran + target dari 3 dokumen
    "SKL-010": 8000,   # LKjIP: analisis + realisasi + bukti
    "SKL-011": 5000,   # cascading: struktur sasaran-program
    "SKL-007": 3000,   # Q&A: top-k relevant chunks saja
}
```

---

## 9. Task Data Model

### 9.1 Task

| Field | Type | Required | Description |
| --- | --- | ---: | --- |
| `id` | string | Yes | Stable task ID |
| `workspace_id` | string | Yes | Workspace |
| `title` | string | Yes | Short title |
| `user_request` | string | Yes | Original natural language request |
| `execution_level` | enum | Yes | `direct` atau `task_plan` |
| `status` | enum | Yes | Current task status |
| `privacy_mode` | enum | Yes | `open`, `standard`, `strict` |
| `estimated_tokens` | integer | No | Preflight estimate |
| `actual_tokens` | integer | No | Total tokens used |
| `tokens_saved_cache` | integer | No | Token saved by cache hits |
| `output_paths_json` | JSON | No | Generated files |
| `warnings_json` | JSON | No | Task-level warnings |
| `error_code` | string | No | Stable error code |
| `created_at` | datetime | Yes | — |

### 9.2 Subtask

| Field | Type | Required | Description |
| --- | --- | ---: | --- |
| `id` | string | Yes | Stable subtask ID |
| `task_id` | string | Yes | Parent task |
| `step_no` | integer | Yes | Execution order |
| `title` | string | Yes | Human-readable title |
| `skill_id` | string | Yes | From skill registry |
| `execution_tier` | enum | Yes | `no_ai`, `light`, `default`, `reasoning` |
| `model_used` | string | No | Actual model called |
| `status` | enum | Yes | Current status |
| `depends_on` | list[string] | No | Subtask IDs |
| `cache_key` | string | No | Cache key for result lookup |
| `cache_hit` | boolean | No | Whether result came from cache |
| `context_inputs_json` | JSON | Yes | Which shared context fields this subtask reads |
| `context_outputs_json` | JSON | No | Which shared context fields this subtask writes |
| `estimated_tokens` | integer | No | Budget allocation |
| `actual_tokens` | integer | No | Actual usage |
| `started_at` | datetime | No | — |
| `finished_at` | datetime | No | — |
| `error_code` | string | No | — |

### 9.3 Status Model

Task status:

| Status | Meaning |
| --- | --- |
| `draft` | Plan exists but not confirmed |
| `pending` | Confirmed but not started |
| `running` | At least one subtask running |
| `waiting_user` | Token/privacy confirmation needed |
| `blocked` | Privacy or dependency issue |
| `partial_success` | Some subtasks failed/skipped |
| `completed` | All required subtasks done |
| `failed` | Cannot continue |
| `cancelled` | User cancelled |

Subtask status:

| Status | Meaning |
| --- | --- |
| `pending` | Ready |
| `waiting_dependency` | Waiting for upstream |
| `waiting_user` | Needs confirmation |
| `running` | Executing |
| `cache_hit` | Served from cache, no AI call |
| `completed` | Done |
| `partial_success` | Done with warnings |
| `failed` | Failed, may retry |
| `blocked` | Privacy/token issue |
| `skipped` | Not available this version |
| `cancelled` | Cancelled |

---

## 10. Skill Routing

### 10.1 Routing by Intent

| User Intent | Skill | Tier | Agent |
| --- | --- | --- | --- |
| Deteksi intent REPL | `SKL-022` | `no_ai` | CLIRouterAgent |
| Tanya jawab dokumen | `SKL-007` | `default` | OPDPlanningCopilotAgent |
| Cek indikator | `SKL-008` | `default` | IndicatorReviewAgent |
| Review PK | `SKL-009` | `default` | PKReviewAgent |
| Review LKjIP | `SKL-010` | `default` | LKjIPReviewAgent |
| Cek cascading/pohon | `SKL-011` | `default` | CascadingReviewAgent |
| Cek evidence | `SKL-012` | `default` | EvidenceReviewAgent |
| Review rencana aksi | `SKL-024` | `default` | RencanaAksiReviewAgent |
| Cek tindak lanjut LHE | `SKL-025` | `light` | LHETrackingAgent |
| Cross-doc coherence | `SKL-026` | `reasoning` | Shared (auto-called) |
| Buat rekomendasi | `SKL-013` | `default` | DraftAgent |
| Buat laporan | `SKL-017` | `no_ai` | ReportAgent |
| Rekomendasi berikutnya | `SKL-023` | `no_ai` | Shared (auto) |
| Pecah task panjang | `SKL-018` | `light` | TaskAgent |

### 10.2 Routing by Required Output

| Desired Output | Skill Chain (Token-Optimized) |
| --- | --- |
| Ringkasan dokumen OPD | `SKL-003` → `SKL-004` → `SKL-005` → `SKL-017` |
| Jawaban berbasis dokumen | `SKL-022` → `SKL-006[light]` → `SKL-014` → `SKL-007[default]` → `SKL-015` → `SKL-023` |
| Review indikator | `SKL-006[light]` → `SKL-014` → `SKL-008[default]` → `SKL-026[reasoning]` → `SKL-015` → `SKL-017` → `SKL-023` |
| Review PK | `SKL-006[light]` → `SKL-014` → `SKL-009[default]` → `SKL-026[reasoning]` → `SKL-015` → `SKL-017` → `SKL-023` |
| Review LKjIP | `SKL-006[light]` → `SKL-014` → `SKL-010[default]` → `SKL-026[reasoning]` → `SKL-015` → `SKL-017` → `SKL-023` |
| Peta cascading | `SKL-006[light]` → `SKL-011[default]` → `SKL-015` → `SKL-017` → `SKL-023` |
| Audit evidence | `SKL-006[light]` → `SKL-014` → `SKL-012[default]` → `SKL-015` → `SKL-017` → `SKL-023` |
| LHE tracking | `SKL-003` → `SKL-025[light]` → `SKL-015` → `SKL-017` → `SKL-023` |
| Laporan final | `semua review` → `SKL-021[reasoning]` → `SKL-013[default]` → `SKL-017` |

### 10.3 Routing Guardrails

Task Router harus menolak routing ketika:

1. Required skill tidak tersedia di versi aktif.
2. Required input tidak ada.
3. Scan belum selesai dan skill membutuhkan source refs.
4. Privacy mode memblokir context yang dibutuhkan.
5. Estimated token melebihi batas dan user belum konfirmasi.
6. Cache key valid tapi model berubah (perlu user konfirmasi apakah mau re-run).

---

## 11. Default Task Templates

Template ini dipakai oleh SKL-018 lite untuk mencocokkan perintah user tanpa AI. Template-first, AI-assisted hanya untuk edge case.

### 11.1 Full SAKIP Review

Trigger: "review semua dokumen", "review lengkap", `/task review-full`

| Step | Subtask | Skill | Tier | Depends On | Context Output |
| ---: | --- | --- | --- | --- | --- |
| 1 | Validasi runtime | `SKL-002` | `no_ai` | — | — |
| 2 | Scan folder | `SKL-003` | `no_ai` | 1 | `indexed_documents` |
| 3 | Klasifikasi | `SKL-004` | `no_ai` | 2 | `doc_types`, `health_signals` |
| 4 | Index dan source refs | `SKL-005`, `SKL-006` | `no_ai`/`light` | 3 | `source_refs`, `retrieval_index` |
| 5 | Review indikator | `SKL-008` | `default` | 4 | `extracted_indicators` |
| 6 | Cross-doc coherence (indikator) | `SKL-026` | `reasoning` | 5 | `coherence_findings` |
| 7 | Review PK | `SKL-009` | `default` | 4, 5 | `pk_data` |
| 8 | Review LKjIP | `SKL-010` | `default` | 4, 7 | `lkjip_data` |
| 9 | Review Rencana Aksi | `SKL-024` | `default` | 4, 7 | `rencana_aksi_data` |
| 10 | Cek cascading | `SKL-011` | `default` | 4, 5, 7 | `cascading_map` |
| 11 | LHE tracking | `SKL-025` | `light` | 4 | `lhe_matrix` |
| 12 | Audit evidence | `SKL-012` | `default` | 4, 8 | `evidence_matrix` |
| 13 | Desk evaluation | `SKL-021` | `reasoning` | 5,7,8,10,12 | `desk_score` |
| 14 | Draft rekomendasi | `SKL-013` | `default` | 5,7,8,9,10,11,12 | — |
| 15 | Laporan final | `SKL-017` | `no_ai` | 13,14 | `output_files` |

Token estimate tanpa cache: ~95.000. Dengan cache (semua hit): 0.

### 11.2 Indicator Improvement

Trigger: "cek indikator", "perbaiki indikator", `/cek-indikator`

| Step | Subtask | Skill | Tier | Depends On |
| ---: | --- | --- | --- | --- |
| 1 | Pastikan scan selesai | `SKL-003`, `SKL-004` | `no_ai` | — |
| 2 | Ambil konteks indikator | `SKL-006` | `light` | 1 |
| 3 | Review indikator | `SKL-008` | `default` | 2 |
| 4 | Cross-doc coherence | `SKL-026` | `reasoning` | 3 |
| 5 | Validasi output AI | `SKL-015` | `no_ai` | 3, 4 |
| 6 | Report indikator | `SKL-017` | `no_ai` | 5 |
| 7 | Rekomendasi berikutnya | `SKL-023` | `no_ai` | 6 |

### 11.3 PK Consistency

Trigger: "review PK", `/review-pk`

| Step | Subtask | Skill | Tier | Depends On |
| ---: | --- | --- | --- | --- |
| 1 | Pastikan PK, IKU, Renstra terindeks | `SKL-003`, `SKL-004` | `no_ai` | — |
| 2 | Ambil konteks pembanding | `SKL-006` | `light` | 1 |
| 3 | Review PK | `SKL-009` | `default` | 2 |
| 4 | Cross-doc coherence target | `SKL-026` | `reasoning` | 3 |
| 5 | Validasi source refs | `SKL-015` | `no_ai` | 3, 4 |
| 6 | Report PK | `SKL-017` | `no_ai` | 5 |
| 7 | Rekomendasi berikutnya | `SKL-023` | `no_ai` | 6 |

### 11.4 Evidence Gap

Trigger: "cek evidence", "klaim tanpa bukti", `/cek-evidence`

| Step | Subtask | Skill | Tier | Depends On |
| ---: | --- | --- | --- | --- |
| 1 | Pastikan LKjIP dan evidence folder terindeks | `SKL-003`, `SKL-004` | `no_ai` | — |
| 2 | Ambil klaim kinerja LKjIP | `SKL-010` | `default` | 1 |
| 3 | Audit evidence | `SKL-012` | `default` | 2 |
| 4 | Validasi output | `SKL-015` | `no_ai` | 3 |
| 5 | Report evidence | `SKL-017` | `no_ai` | 4 |
| 6 | Rekomendasi berikutnya | `SKL-023` | `no_ai` | 5 |

---

## 12. Execution Algorithm

### 12.1 Decomposition

```text
1. Terima user request (via SKL-022 atau /task command).
2. Cek apakah ini Direct Execution (single skill) atau Task Plan (multi-skill).
3. Jika Task Plan:
   a. Cari template matching dari pattern request.
   b. Jika cocok → pakai template langsung (tidak perlu AI).
   c. Jika tidak cocok → gunakan SKL-018 lite untuk decompose.
4. Untuk setiap subtask dalam plan:
   a. Hitung cache key.
   b. Cek cache → jika hit, tandai sebagai cache_hit.
   c. Hitung estimated tokens untuk subtask yang bukan cache hit.
5. Hitung total estimated tokens dan biaya.
6. Tampilkan execution plan ke user jika token > threshold atau ada subtask reasoning.
7. Tunggu konfirmasi jika perlu.
```

### 12.2 Execution

```text
1. Tandai task sebagai running.
2. Inisialisasi SubtaskContext kosong.
3. Temukan subtask yang semua dependency-nya selesai.
4. Untuk setiap subtask siap:
   a. Cek cache → jika hit, ambil hasil dan update SubtaskContext. Skip ke langkah h.
   b. Validasi required inputs dari SubtaskContext.
   c. Jalankan privacy preflight jika needed.
   d. Jalankan token preflight dan periksa budget.
   e. Pilih model berdasarkan execution_tier.
   f. Jalankan skill/agent dengan SubtaskContext sebagai input tambahan.
   g. Validasi hasil via AI contract jika AI-bound.
   h. Simpan hasil ke SubtaskContext (context sharing).
   i. Simpan hasil ke result cache jika cacheable.
   j. Simpan token usage.
   k. Update subtask status.
5. Ulangi sampai semua subtask selesai, blocked, skipped, atau failed.
6. Hitung task final status.
7. Render next-step recommendations via SKL-023.
```

### 12.3 Resume

```text
1. Load task by ID atau last active task.
2. Load subtask statuses, outputs, dan SubtaskContext dari database.
3. Revalidasi workspace dan file hashes.
4. Invalidasi cache untuk subtask yang dokumen inputnya berubah.
5. Reset subtask yang cache-nya invalid ke pending.
6. Lanjutkan dari pending atau failed-retryable subtasks.
7. Preserve completed subtasks yang cache-nya masih valid.
```

---

## 13. Retry dan Failure Policy

| Failure | Retry | Status |
| --- | --- | --- |
| Transient AI provider error (5xx, timeout) | Retry max 2× dengan exponential backoff | `failed` jika masih gagal |
| AI JSON invalid | 1× schema repair retry | `failed` dengan `AI_SCHEMA_INVALID` |
| Missing source refs | No retry kecuali retrieval bisa diperluas | `blocked` atau `failed` |
| Privacy blocked | Minta user ubah mode atau hapus data sensitif | `blocked` |
| Token budget exceeded | Tawarkan: potong scope / model hemat / konfirmasi | `waiting_user` |
| File read failed | Lanjutkan file lain | `partial_success` |
| Required dependency failed | Subtask dependent jadi `blocked` | — |
| Optional dependency failed | Subtask dependent lanjut dengan warning | — |
| Cache stale (hash mismatch) | Re-run subtask otomatis | — |

---

## 14. Memory Architecture

Memory SAKIPRO dibagi menjadi tiga tier yang sangat berbeda karakteristiknya.

### 14.1 Tier 1 — Persistent Memory (SQLite)

Hidup di `~/.sakipro/sakipro.db`. Bertahan antar sesi.

Konten:

- Indexed document chunks + metadata
- Source references
- Review results (via result cache)
- Token usage log
- Task dan subtask history
- Workspace config dan state

Komponen: `storage/database.py`, `storage/models.py`, `storage/repositories.py`

**Strategi indexing**: Incremental — hanya file yang berubah (hash berbeda) yang di-re-index. File yang tidak berubah tidak diproses ulang.

```python
def incremental_index(folder: Path, workspace_id: str):
    existing = repo.get_all_document_hashes(workspace_id)
    for file in scan_folder(folder):
        current_hash = sha256_file(file)
        if existing.get(str(file)) == current_hash:
            continue  # tidak berubah, skip
        index_document(file, workspace_id)  # index ulang hanya yang berubah
        existing[str(file)] = current_hash
```

### 14.2 Tier 2 — Session Memory (RAM)

Hidup selama satu sesi REPL aktif. Hilang saat terminal ditutup.

Konten:

- Riwayat percakapan REPL sesi ini (max N turns)
- State review terkini (apa yang sudah direview, temuan aktif)
- SubtaskContext dari task yang sedang berjalan
- Hasil skill terakhir (untuk SKL-023)

Komponen: `memory/session_context.py`

```python
@dataclass
class SessionContext:
    conversation_history: list[Turn]     # max 20 turns, FIFO
    review_state: ReviewState            # apa yang sudah direview
    last_skill_result: SkillResult | None
    active_task_id: str | None
    workspace_id: str
```

**Truncation policy**: Jika conversation history > 20 turns, hapus turns lama. Jangan summarize dengan AI — terlalu mahal. Cukup truncate.

### 14.3 Tier 3 — Working Memory (Context Window)

Hidup hanya selama satu AI call. Dibuang setelah response diterima.

Konten: prompt yang dikirim ke AI — system prompt + document chunks + conversation turns + user query.

Komponen: `memory/context_builder.py`

**Token Budget Controller**:

```python
class ContextBudgetController:
    MAX_TOKENS = 32_000  # default context budget per call (konservatif untuk laptop)

    BUDGET_ALLOCATION = {
        "system_prompt": 1_500,      # tetap, cache-able
        "skill_instructions": 500,   # tetap, cache-able
        "document_chunks": 20_000,   # mayoritas budget
        "conversation_history": 3_000,  # max 5 turns terakhir
        "user_query": 500,
        "output_format": 500,
        "safety_margin": 6_000,      # untuk AI response
    }
```

Jika total chunks melebihi `document_chunks` budget, potong dengan priority:

1. Chunks dengan relevance score tertinggi untuk query ini
2. Chunks dari dokumen yang paling relevan dengan skill saat ini
3. Hapus chunks yang sudah ada di result cache untuk subtask lain

---

## 15. Prompt Caching Strategy

Prompt caching adalah cara termudah menghemat biaya token yang sering diabaikan. LiteLLM mendukung ini via Anthropic Claude dan OpenAI.

### 15.1 Apa yang Cacheable

| Bagian Prompt | Cache? | Alasan |
| --- | --- | --- |
| System prompt (base) | **Ya** | Tidak berubah per session |
| Skill instructions (SAKIP rules, format output) | **Ya** | Per skill, jarang berubah |
| Indexed document chunks (bukan per-query) | **Ya** | Chunks sama dipakai banyak skill |
| Conversation history | Tidak | Berubah setiap turn |
| User query | Tidak | Selalu unik |

### 15.2 Implementasi LiteLLM Cache

```python
# Di llm_client.py
from litellm import completion

def call_ai(prompt: PromptBundle) -> AIResponse:
    messages = [
        {
            "role": "system",
            "content": [
                {
                    "type": "text",
                    "text": prompt.system_prompt,
                    "cache_control": {"type": "ephemeral"}  # cache system prompt
                }
            ]
        },
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": prompt.document_context,
                    "cache_control": {"type": "ephemeral"}  # cache document context
                },
                {
                    "type": "text",
                    "text": prompt.user_query
                }
            ]
        }
    ]
    return completion(model=model_id, messages=messages)
```

### 15.3 Estimasi Penghematan

Untuk review yang memanfaatkan cache (operasi kedua dan seterusnya pada hari yang sama):

- System prompt (1.500 token): cache hit → hemat ~100% biaya input
- Document chunks (20.000 token): cache hit → hemat ~90% biaya input (Anthropic rate)
- Estimasi total hemat per repeat operation: **70–85% dari token input cost**

Untuk sesi kerja harian di mana user menjalankan beberapa review, penghematan nyata bisa sangat signifikan.

---

## 16. Memory Manager

`memory/memory_manager.py` adalah koordinator yang mengelola ketiga tier.

```python
class MemoryManager:
    def __init__(self, workspace_id: str, session: SessionContext):
        self.persistent = PersistentStore(workspace_id)
        self.session = session
        self.result_cache = ResultCache(workspace_id)

    def get_context_for_skill(
        self,
        skill_id: str,
        query: str,
        query_type: str,
        token_budget: int
    ) -> ContextBundle:
        """
        Bangun context window untuk AI call secara efisien.
        1. Ambil cached document chunks dari persistent store.
        2. Filter berdasarkan query_type dan relevance.
        3. Tambah conversation history dari session (max 5 turns).
        4. Potong ke token_budget.
        5. Tandai cacheable parts untuk prompt caching.
        """
        ...

    def store_skill_result(self, skill_id: str, result: SkillResult, cache_key: str):
        """Simpan ke persistent store dan update session state."""
        ...

    def check_result_cache(self, cache_key: str) -> SkillResult | None:
        """Cek apakah hasil skill ini masih valid di cache."""
        ...
```

---

## 17. Strategi Token Optimization Ringkasan

| Strategi | Estimasi Hemat | Implementasi |
| --- | --- | --- |
| Result cache (dokumen tidak berubah) | 100% token review | `memory/result_cache.py` |
| Prompt caching (system + doc chunks) | 70–85% input cost (repeat calls) | `ai/llm_client.py` |
| Context sharing antar subtask | 30–50% total token per full review | `tasks/subtask_context.py` |
| Smart chunk targeting per skill | 40–60% token vs load-all | `memory/context_builder.py` |
| Model routing per tier | 60–80% cost vs all-default | `ai/model_router.py` |
| Deterministic-first (no AI for extraction) | Significant — no AI call at all | `sakip/` domain modules |
| Incremental indexing | No token cost | `memory/indexer.py` |
| Two-level execution (no overhead for simple ops) | Latency + zero overhead | `tasks/task_runner.py` |

Target: untuk penggunaan harian Kasubbag Perencanaan (review 1–2 dokumen per hari), total token per hari harus di bawah 20.000 dengan kombinasi strategi di atas.

---

## 18. Security dan Privacy

1. SubtaskContext tidak boleh menyimpan raw document content — hanya IDs, hashes, dan extracted structured data.
2. Result cache tidak boleh menyimpan raw prompt atau sensitive document quotes.
3. Prompt caching melalui API cloud hanya boleh diaktifkan jika privacy mode bukan `strict`.
4. Jika privacy mode berubah, invalidasi seluruh result cache dan prompt cache.
5. Session memory di-clear saat user keluar dari REPL.
6. Token usage log tidak boleh menyimpan prompt content.

---

## 19. Acceptance Criteria

Task dan Memory Management dianggap implementation-ready ketika:

1. Direct execution bekerja tanpa membuat Task record untuk single-skill operations.
2. Task Plan dibuat untuk complex task dan ditampilkan ke user sebelum eksekusi.
3. Result cache mengembalikan hasil tanpa AI call jika dokumen tidak berubah.
4. Prompt caching aktif untuk system prompt dan document chunks.
5. Subtask yang selesai mewariskan output ke SubtaskContext untuk subtask berikutnya.
6. Model routing memilih tier yang tepat berdasarkan skill registry.
7. Incremental indexing hanya memproses file yang berubah.
8. Resume melanjutkan dari subtask yang belum selesai dan mempertahankan cache-valid results.
9. Token usage per operasi harian < 20.000 untuk workflow rutin.
10. `sakipro resume` menampilkan SubtaskContext dan task progress yang tersimpan.
11. Cache hit ditandai jelas di task board ("[dari cache]").
12. Privacy mode `strict` menonaktifkan prompt caching ke cloud.

---

## 20. Test Plan

| Test ID | Scenario | Expected Result |
| --- | --- | --- |
| `TC-TASK-001` | Direct execution `/review-pk` | Tidak ada Task record; hasil langsung ditampilkan |
| `TC-TASK-002` | Result cache hit pada `/review-pk` kedua (dokumen sama) | No AI call; labeled "dari cache" |
| `TC-TASK-003` | Result cache invalidation setelah file berubah | Full review dijalankan ulang |
| `TC-TASK-004` | Full review task — context sharing | SKL-009 memakai `extracted_indicators` dari SKL-008 tanpa re-ekstraksi |
| `TC-TASK-005` | Model routing | SKL-025 memanggil light model; SKL-021 memanggil reasoning model |
| `TC-TASK-006` | Token budget exceeded sebelum task | `waiting_user` dengan pilihan: scope reduction / cheaper model |
| `TC-TASK-007` | Privacy strict + prompt caching | Prompt caching dinonaktifkan |
| `TC-TASK-008` | Resume setelah interrupted task | Completed + cache-valid subtasks dipertahankan |
| `TC-TASK-009` | Incremental indexing | File tidak berubah tidak di-index ulang |
| `TC-TASK-010` | Session context truncation | History > 20 turns → FIFO truncate, tidak summarize |
| `TC-TASK-011` | Decompose "review semua" request | Template match → task plan tanpa AI decomposition call |
| `TC-TASK-012` | Task board render | Cache hits ditandai, token saved ditampilkan, output paths terlihat |

---

## 21. Implementation Priority

1. `result_cache.py` — highest ROI untuk token saving
2. `model_router.py` — update untuk tier routing
3. `task_runner.py` — tambah SubtaskContext dan two-level execution
4. `context_builder.py` — tambah ContextBudgetController
5. `llm_client.py` — tambah prompt caching support
6. `memory_manager.py` — koordinator ketiga tier
7. `indexer.py` — incremental indexing
8. `session_context.py` — session state untuk REPL
9. `skill_registry.py` — update dengan SKL-022–026 dan execution_tier
10. `task_decomposer.py` — template-first matching
11. Task Plan UI — execution plan display + konfirmasi
12. `sakipro resume` — load dan continue task

Penting: implementasikan result_cache dan model_router sebelum mengerjakan task templates. Dua komponen ini memberikan dampak terbesar pada penghematan token dan semua fitur lain bergantung pada keduanya.
