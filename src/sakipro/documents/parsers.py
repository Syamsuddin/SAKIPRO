import os
from typing import Generator, Dict, Any

def parse_docx(file_path: str) -> Generator[Dict[str, Any], None, None]:
    """Parse DOCX file and yield chunks."""
    try:
        from docx import Document
        doc = Document(file_path)
        for i, para in enumerate(doc.paragraphs):
            text = para.text.strip()
            if text:
                yield {
                    "content": text,
                    "chunk_index": i,
                    "page_num": None,
                    "sheet_name": None
                }
    except Exception as e:
        print(f"Error parsing DOCX {file_path}: {e}")

def parse_pdf(file_path: str) -> Generator[Dict[str, Any], None, None]:
    """Parse PDF file and yield chunks by page."""
    try:
        import fitz # PyMuPDF
        with fitz.open(file_path) as doc:
            for i, page in enumerate(doc):
                text = page.get_text("text").strip()
                if text:
                    yield {
                        "content": text,
                        "chunk_index": i,
                        "page_num": i + 1,
                        "sheet_name": None
                    }
    except Exception as e:
        print(f"Error parsing PDF {file_path}: {e}")

def parse_xlsx(file_path: str) -> Generator[Dict[str, Any], None, None]:
    """Parse XLSX file and yield row-based chunks."""
    try:
        import pandas as pd
        # Read all sheets
        sheets = pd.read_excel(file_path, sheet_name=None)
        chunk_idx = 0
        for sheet_name, df in sheets.items():
            for i, row in df.iterrows():
                row_dict = row.dropna().to_dict()
                if row_dict:
                    text = " | ".join([f"{k}: {v}" for k, v in row_dict.items()])
                    yield {
                        "content": text,
                        "chunk_index": chunk_idx,
                        "page_num": None,
                        "sheet_name": sheet_name
                    }
                    chunk_idx += 1
    except Exception as e:
        print(f"Error parsing XLSX {file_path}: {e}")

def parse_txt(file_path: str) -> Generator[Dict[str, Any], None, None]:
    """Parse TXT or Markdown file."""
    try:
        with open(file_path, "r", encoding="utf-8", errors="replace") as f:
            for i, line in enumerate(f):
                text = line.strip()
                if text:
                    yield {
                        "content": text,
                        "chunk_index": i,
                        "page_num": None,
                        "sheet_name": None
                    }
    except Exception as e:
        print(f"Error parsing TXT {file_path}: {e}")
