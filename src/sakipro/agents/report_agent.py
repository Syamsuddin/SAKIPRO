from typing import Dict, Any, Generator
from sakipro.agents.base import BaseAgent
from sakipro.memory.retrieval import retrieve_context, format_context_for_llm
from sakipro.ai.llm_client import call_llm_stream
from sakipro.core.config import get_global_context_prompt

class ReportAgent(BaseAgent):
    agent_name = "Report Agent"
    supported_commands = ["/report"]
    
    def plan(self, request: Dict[str, Any]) -> Dict[str, Any]:
        user_query = request.get("query", "").strip()
        core_keywords = "LHE Laporan Hasil Evaluasi Rekomendasi Temuan Kesimpulan Kelemahan Kekuatan"
        search_query = f"{user_query} {core_keywords}".strip()
        return {"search_query": search_query}
        
    def gather_context(self, plan: Dict[str, Any]) -> Dict[str, Any]:
        raw_context = retrieve_context(plan["search_query"])
        formatted = format_context_for_llm(raw_context)
        return {"context_text": formatted}
        
    def run(self, request: Dict[str, Any]) -> Generator[str, None, None]:
        plan = self.plan(request)
        context = self.gather_context(plan)
        
        system_prompt = (
            get_global_context_prompt() +
            "Anda adalah Asisten SAKIP yang ahli dalam menyusun Laporan Hasil Evaluasi (LHE).\n"
            "Tugas Anda:\n"
            "1. Mensintesis atau merangkum seluruh temuan dari dokumen perencanaan hingga pelaporan (IKU, PK, Renstra, LKjIP, Cascading, Evidence).\n"
            "2. Susun ringkasan Laporan Hasil Evaluasi (LHE) yang mencakup: Kekuatan, Kelemahan Utama, dan Rekomendasi Strategis.\n"
            "3. Pastikan untuk selalu menyertakan '[DRAFT: Harap periksa ulang]' di akhir laporan Anda.\n\n"
            f"{context['context_text']}"
        )
        
        user_message = request.get("query", "Tolong buatkan draf ringkasan Laporan Hasil Evaluasi SAKIP.")
        
        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_message}
        ]
        
        return call_llm_stream(messages)
        
    def validate(self, result: Dict[str, Any]) -> Dict[str, Any]:
        pass
