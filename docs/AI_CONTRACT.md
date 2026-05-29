# AI_CONTRACT.md
# SAKIPRO v1.0 AI Input and Output Contract

Version: 1.0  
Status: Blueprint Revision  
Purpose: Mengikat semua agent agar output AI konsisten, aman, dan dapat diaudit.

---

## 1. Prinsip

1. AI hanya boleh menjawab berdasarkan konteks yang diberikan retrieval layer.
2. Semua klaim faktual wajib memiliki `source_refs`.
3. Angka, target, realisasi, anggaran, dan nama dokumen tidak boleh dibuat tanpa sumber.
4. Semua output berstatus `draft`.
5. Output final hanya dapat dibuat oleh user.

---

## 2. Source Reference Object

Setiap sumber wajib memakai struktur berikut:

```json
{
  "source_id": "src_001",
  "document_id": "doc_001",
  "file_path": "Dokumen_SAKIP_OPD/PK_2026.docx",
  "document_type": "pk",
  "page": 3,
  "sheet": null,
  "cell_range": null,
  "paragraph_index": 18,
  "chunk_id": "chk_042",
  "quote": "Sasaran strategis ...",
  "extraction_method": "docx_paragraph",
  "confidence": "high"
}
```

`quote` harus singkat dan tidak boleh berisi data sensitif yang sudah dimasking.

---

## 3. Agent Input Schema

```json
{
  "workspace_id": "ws_001",
  "command": "review-pk",
  "privacy_mode": "standard",
  "task": "Review PK 2026",
  "rules": ["PK-001", "PK-002", "PK-003", "PK-004", "PK-005"],
  "context_chunks": [],
  "source_refs": [],
  "output_language": "id",
  "max_findings": 20
}
```

---

## 4. Agent Output Schema

```json
{
  "status": "success",
  "draft": true,
  "summary": "",
  "findings": [
    {
      "finding_id": "f_001",
      "rule_id": "PK-003",
      "severity": "high",
      "title": "",
      "description": "",
      "impact": "",
      "recommendation": "",
      "source_refs": ["src_001"],
      "confidence": "medium",
      "needs_human_validation": true
    }
  ],
  "recommendations": [],
  "sources": [],
  "token_usage": {
    "provider": "openai",
    "model": "gpt-4o",
    "prompt_tokens": 1200,
    "completion_tokens": 450,
    "total_tokens": 1650,
    "estimated_cost_usd": 0.015
  },
  "warnings": []
}
```

Nilai valid untuk `status`:

| Status | Deskripsi |
|---|---|
| `success` | Semua temuan berhasil diproses |
| `partial_success` | Sebagian temuan berhasil, sebagian gagal atau dilewati |
| `failed` | Proses gagal total |
| `blocked` | Proses diblokir oleh privacy mode atau dependency |
| `skipped` | Proses dilewati karena fitur belum tersedia atau tidak diperlukan |

---

## 5. Failure and Retry

1. Jika output bukan JSON valid, parser melakukan satu retry dengan prompt perbaikan schema.
2. Jika source kosong, command gagal dengan `AI_SOURCE_REQUIRED`.
3. Jika privacy mode memblokir konteks, command gagal dengan `PRIVACY_BLOCKED`.
4. Jika confidence rendah, output tetap boleh dibuat tetapi wajib ditandai perlu validasi manusia.

---

## 6. Prompt Rules

Prompt system wajib memuat:

1. Larangan membuat angka tanpa sumber.
2. Larangan mengubah file asli.
3. Kewajiban menggunakan `SAKIP_RULEBOOK.md`.
4. Kewajiban mengembalikan JSON sesuai schema.
5. Kewajiban menandai semua hasil sebagai draft.
