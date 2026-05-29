from typing import List, Dict, Any
from sqlalchemy import or_
from sakipro.storage.database import SessionLocal
from sakipro.storage.models import DocumentChunk, Document

from sakipro.core.config import settings

def retrieve_context(query: str, top_k: int = 15) -> List[Dict[str, Any]]:
    """Retrieve relevant chunks using a scoring engine that prioritizes Profile Context."""
    db = SessionLocal()
    
    # 1. Base Query Keywords
    keywords = set(kw for kw in query.lower().split() if len(kw) > 2)
    
    # 2. Extract Profile Keywords for massive boosting
    opd_kws = set()
    pemda_kws = set()
    if settings.opd_name and "belum diatur" not in settings.opd_name.lower():
        opd_kws.update([w for w in settings.opd_name.lower().split() if len(w) > 3])
    if settings.pemda_name and "belum diatur" not in settings.pemda_name.lower():
        pemda_kws.update([w for w in settings.pemda_name.lower().split() if len(w) > 3])
        
    conditions = []
    for kw in keywords:
        conditions.append(DocumentChunk.content.ilike(f"%{kw}%"))
        
    try:
        # Fetch all candidate chunks from database
        results = (
            db.query(DocumentChunk, Document)
            .join(Document)
            .filter(or_(*conditions))
            .all()
        )
        
        # 3. Smart Scoring Engine
        scored_results = []
        for chunk, doc in results:
            content_lower = chunk.content.lower()
            file_lower = doc.file_path.lower()
            
            score = 0
            
            # Score base keywords
            for kw in keywords:
                if kw in content_lower:
                    score += 1
                if kw in file_lower:
                    score += 2
                    
            # OPD is KING (Very high weight to prevent another OPD from winning)
            for o_kw in opd_kws:
                if o_kw in content_lower:
                    score += 20
                if o_kw in file_lower:
                    score += 50
                    
            # Pemda is Secondary (Low weight, just to resolve ties, won't overpower OPD)
            for p_kw in pemda_kws:
                if p_kw in content_lower:
                    score += 2
                if p_kw in file_lower:
                    score += 5
                    
            if score > 0:
                scored_results.append((score, chunk, doc))
                
        # Sort by highest score first
        scored_results.sort(key=lambda x: x[0], reverse=True)
        
        # Take Top K
        best_results = scored_results[:top_k]
        
        context = []
        for score, chunk, doc in best_results:
            context.append({
                "chunk_id": chunk.id,
                "content": chunk.content,
                "source": doc.file_path,
                "page": chunk.page_num,
                "sheet": chunk.sheet_name
            })
            
        return context
    finally:
        db.close()

def format_context_for_llm(context: List[Dict[str, Any]]) -> str:
    """Format the retrieved context as a string for the LLM prompt."""
    if not context:
        return "Tidak ada konteks dokumen yang ditemukan."
        
    formatted = "Dokumen Referensi:\n"
    for i, item in enumerate(context, 1):
        source = item['source']
        if item['page']:
            source += f" (Halaman {item['page']})"
        elif item['sheet']:
            source += f" (Sheet {item['sheet']})"
            
        formatted += f"[{i}] {source}\n{item['content']}\n\n"
        
    return formatted
