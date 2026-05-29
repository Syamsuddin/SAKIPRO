from typing import Dict, Any, Generator
import networkx as nx
from sakipro.agents.base import BaseAgent
from sakipro.memory.retrieval import retrieve_context, format_context_for_llm
from sakipro.ai.llm_client import call_llm_stream
from sakipro.core.config import get_global_context_prompt

class CascadingReviewAgent(BaseAgent):
    agent_name = "Cascading Reviewer"
    supported_commands = ["/cek-cascading"]
    
    def plan(self, request: Dict[str, Any]) -> Dict[str, Any]:
        user_query = request.get("query", "").strip()
        core_keywords = "Cascading Pohon Kinerja Penurunan Sasaran Program Kegiatan Indikator"
        search_query = f"{user_query} {core_keywords}".strip()
        return {"search_query": search_query}
        
    def gather_context(self, plan: Dict[str, Any]) -> Dict[str, Any]:
        raw_context = retrieve_context(plan["search_query"])
        formatted = format_context_for_llm(raw_context)
        return {"context_text": formatted}
        
    def run(self, request: Dict[str, Any]) -> Generator[str, None, None]:
        plan = self.plan(request)
        context = self.gather_context(plan)
        
        # Simple NetworkX demonstration
        # In a full implementation, we'd extract entities and build edges
        G = nx.DiGraph()
        G.add_node("Sasaran")
        G.add_node("Program")
        G.add_edge("Sasaran", "Program")
        graph_info = f"Nodes: {G.nodes}, Edges: {G.edges}"
        
        system_prompt = (
            get_global_context_prompt() +
            "Anda adalah Asisten SAKIP yang ahli dalam meninjau pohon kinerja (Cascading).\n"
            "Tugas Anda:\n"
            "1. Evaluasi keselarasan hierarkis (cascading) dari Sasaran -> Program -> Kegiatan -> Subkegiatan.\n"
            "2. Identifikasi apakah ada 'broken chain' (rantai yang terputus) atau kegiatan yang tidak mendukung sasaran di atasnya.\n"
            "3. Pastikan untuk selalu menyertakan '[DRAFT: Harap periksa ulang]' di akhir jawaban Anda.\n\n"
            f"Konteks Graf Logis Terdeteksi (NetworkX): {graph_info}\n\n"
            f"{context['context_text']}"
        )
        
        user_message = request.get("query", "Tolong review keselarasan cascading kinerja berdasarkan dokumen terkait.")
        
        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_message}
        ]
        
        return call_llm_stream(messages)
        
    def validate(self, result: Dict[str, Any]) -> Dict[str, Any]:
        pass
