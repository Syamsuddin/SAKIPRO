import pytest
from unittest.mock import patch
from sakipro.agents.draft_agent import DraftAgent
from sakipro.agents.iku_reviewer import IkuReviewAgent

@patch("sakipro.agents.draft_agent.retrieve_context")
@patch("sakipro.agents.draft_agent.call_llm_stream")
def test_draft_agent_run(mock_call_llm_stream, mock_retrieve_context):
    # Setup mocks
    mock_retrieve_context.return_value = [{"content": "Mock document content", "source": "fake.docx", "page": 1}]
    mock_call_llm_stream.return_value = (chunk for chunk in ["Draft usulan: ", "Indikator X " "[DRAFT: Harap periksa ulang]"])
    
    agent = DraftAgent()
    request = {"query": "Usulkan perbaikan indikator"}
    
    result = list(agent.run(request))
    assert len(result) == 2
    assert "".join(result) == "Draft usulan: Indikator X [DRAFT: Harap periksa ulang]"
    mock_retrieve_context.assert_called_once()
    mock_call_llm_stream.assert_called_once()

@patch("sakipro.agents.iku_reviewer.retrieve_context")
@patch("sakipro.agents.iku_reviewer.call_llm_stream")
def test_iku_reviewer_run(mock_call_llm_stream, mock_retrieve_context):
    mock_retrieve_context.return_value = [{"content": "IKU document", "source": "fake.docx", "page": 1}]
    mock_call_llm_stream.return_value = (chunk for chunk in ["Review IKU: " "Kurang berorientasi hasil."])
    
    agent = IkuReviewAgent()
    result = list(agent.run({"query": "review IKU"}))
    assert "".join(result) == "Review IKU: Kurang berorientasi hasil."
