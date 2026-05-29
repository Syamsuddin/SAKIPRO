from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime, Boolean
from sqlalchemy.orm import relationship
from datetime import datetime
from sakipro.storage.database import Base

class Workspace(Base):
    __tablename__ = "workspaces"
    id = Column(String, primary_key=True, index=True)
    name = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    documents = relationship("Document", back_populates="workspace")

class Document(Base):
    __tablename__ = "documents"
    id = Column(String, primary_key=True, index=True)
    workspace_id = Column(String, ForeignKey("workspaces.id"), nullable=False)
    file_path = Column(String, nullable=False)
    document_type = Column(String, nullable=True) # e.g., 'pk', 'iku', 'renstra'
    file_hash = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    workspace = relationship("Workspace", back_populates="documents")
    chunks = relationship("DocumentChunk", back_populates="document")

class DocumentChunk(Base):
    __tablename__ = "document_chunks"
    id = Column(String, primary_key=True, index=True)
    document_id = Column(String, ForeignKey("documents.id"), nullable=False)
    chunk_index = Column(Integer, nullable=False)
    content = Column(Text, nullable=False)
    page_num = Column(Integer, nullable=True) # For PDF
    sheet_name = Column(String, nullable=True) # For Excel
    
    document = relationship("Document", back_populates="chunks")

class SourceRef(Base):
    __tablename__ = "source_refs"
    id = Column(String, primary_key=True, index=True)
    document_id = Column(String, ForeignKey("documents.id"), nullable=False)
    chunk_id = Column(String, ForeignKey("document_chunks.id"), nullable=False)
    quote_text = Column(Text, nullable=True)

class TokenUsage(Base):
    __tablename__ = "token_usage"
    id = Column(String, primary_key=True, index=True)
    model = Column(String, nullable=False)
    input_tokens = Column(Integer, default=0)
    output_tokens = Column(Integer, default=0)
    estimated_cost = Column(String, nullable=True)
    command = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

class Review(Base):
    __tablename__ = "reviews"
    id = Column(String, primary_key=True, index=True)
    workspace_id = Column(String, ForeignKey("workspaces.id"), nullable=False)
    command = Column(String, nullable=False)
    summary = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    findings = relationship("ReviewFinding", back_populates="review")

class ReviewFinding(Base):
    __tablename__ = "review_findings"
    id = Column(String, primary_key=True, index=True)
    review_id = Column(String, ForeignKey("reviews.id"), nullable=False)
    rule_id = Column(String, nullable=True)
    severity = Column(String, nullable=True)
    description = Column(Text, nullable=True)
    recommendation = Column(Text, nullable=True)
    
    review = relationship("Review", back_populates="findings")

