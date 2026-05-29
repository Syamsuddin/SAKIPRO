import os
import hashlib
from typing import Optional
import uuid
from sakipro.storage.database import SessionLocal, init_db
from sakipro.storage.models import Workspace, Document, DocumentChunk
from sakipro.documents.parsers import parse_docx, parse_pdf, parse_xlsx, parse_txt

def get_file_hash(file_path: str) -> str:
    """Calculate SHA256 hash of a file."""
    hasher = hashlib.sha256()
    with open(file_path, 'rb') as f:
        buf = f.read(65536)
        while len(buf) > 0:
            hasher.update(buf)
            buf = f.read(65536)
    return hasher.hexdigest()

def scan_directory(folder_path: str, workspace_name: str = "DEFAULT_WORKSPACE"):
    """Scan folder, extract text, and save to SQLite."""
    init_db()
    db = SessionLocal()
    
    # Setup workspace
    workspace = db.query(Workspace).filter_by(name=workspace_name).first()
    if not workspace:
        workspace = Workspace(id=str(uuid.uuid4()), name=workspace_name)
        db.add(workspace)
        db.commit()

    processed_count = 0
    ignore_dirs = {".venv", ".git", "node_modules", "build", "dist", "__pycache__"}
    
    for root, dirs, files in os.walk(folder_path):
        # In-place modification of dirs to skip hidden and ignored directories
        dirs[:] = [d for d in dirs if not d.startswith('.') and d not in ignore_dirs]
        
        for file in files:
            file_path = os.path.join(root, file)
            ext = os.path.splitext(file)[1].lower()
            
            # Skip hidden files
            if file.startswith('.'):
                continue
                
            file_hash = get_file_hash(file_path)
            
            # Check if document already exists
            existing_doc = db.query(Document).filter_by(file_hash=file_hash).first()
            if existing_doc:
                continue
                
            doc_id = str(uuid.uuid4())
            document = Document(
                id=doc_id,
                workspace_id=workspace.id,
                file_path=file_path,
                file_hash=file_hash,
                document_type="unknown" # For v0.2 MVP
            )
            db.add(document)
            
            # Extract content based on extension
            parser = None
            if ext == '.docx':
                parser = parse_docx(file_path)
            elif ext == '.pdf':
                parser = parse_pdf(file_path)
            elif ext == '.xlsx':
                parser = parse_xlsx(file_path)
            elif ext in ['.txt', '.md', '.csv']:
                parser = parse_txt(file_path)
                
            if parser:
                for chunk_data in parser:
                    chunk = DocumentChunk(
                        id=str(uuid.uuid4()),
                        document_id=doc_id,
                        chunk_index=chunk_data["chunk_index"],
                        content=chunk_data["content"],
                        page_num=chunk_data.get("page_num"),
                        sheet_name=chunk_data.get("sheet_name")
                    )
                    db.add(chunk)
            
            db.commit()
            processed_count += 1
            
    db.close()
    return processed_count
