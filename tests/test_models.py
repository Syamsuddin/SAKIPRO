import pytest
from sakipro.storage.models import Workspace, Document, TokenUsage, Review

def test_create_workspace(db_session):
    workspace = Workspace(id="wk-1", name="Test OPD")
    db_session.add(workspace)
    db_session.commit()
    
    assert workspace.id == "wk-1"
    assert workspace.name == "Test OPD"

def test_create_document(db_session):
    workspace = Workspace(id="wk-2", name="OPD A")
    db_session.add(workspace)
    db_session.commit()
    
    doc = Document(id="doc-1", workspace_id=workspace.id, file_path="/fake/path/doc.txt", file_hash="abc", document_type="pk")
    db_session.add(doc)
    db_session.commit()
    
    assert doc.id == "doc-1"
    assert doc.file_path == "/fake/path/doc.txt"

def test_token_usage_tracking(db_session):
    token = TokenUsage(
        id="tok-1",
        model="claude-3",
        input_tokens=100,
        output_tokens=50,
        estimated_cost="0.01",
        command="/scan"
    )
    db_session.add(token)
    db_session.commit()
    
    assert token.id == "tok-1"
    assert token.estimated_cost == "0.01"
