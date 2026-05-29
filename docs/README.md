# SAKIPRO v1.0

**AI CLI Assistant for Indonesian Local Government Planning Officers (Kasubbag Perencanaan OPD).**

SAKIPRO is designed to help local government agencies (OPD) improve the quality of their Performance Accountability System (SAKIP) documents through automated AI-driven audits, consistency checks, and drafting support.

## Core Features
- **Folder Scanning:** Automated indexing and classification of SAKIP documents (Renstra, IKU, PK, LKjIP, etc.).
- **Indicator Audit:** Quality review of performance indicators based on Permenpan RB 88/2021.
- **PK Consistency Check:** Cross-referencing Performance Agreements against strategic planning documents.
- **LKjIP Analysis:** Analytical review of performance reports and realization data.
- **Privacy First:** Automatic masking of sensitive data (PII) before AI processing.
- **Grounded AI:** Every AI finding includes direct source references to original documents.

## Requirements
- Python 3.11 or 3.12
- API Key for AI Provider (OpenAI, Gemini, Claude, or DeepSeek)

## Quick Start
1. **Sync Dependencies:**
   ```bash
   uv sync
   ```
2. **Initialize Workspace:**
   ```bash
   uv run sakipro init
   ```
3. **Configure API Keys:**
   ```bash
   uv run sakipro config set-key
   ```
4. **Check System Health:**
   ```bash
   uv run sakipro doctor
   ```
5. **Scan Documents:**
   ```bash
   uv run sakipro scan ./path/to/documents
   ```
6. **Run Audit:**
   ```bash
   uv run sakipro cek-indikator
   ```

## Development
SAKIPRO uses `uv` for dependency management and `Typer` for the CLI interface.

Refer to the `docs/` folder for detailed technical blueprints and user guides.
