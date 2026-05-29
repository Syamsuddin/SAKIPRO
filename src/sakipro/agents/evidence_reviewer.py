from typing import Dict, Any, Generator
from sakipro.agents.base import BaseAgent
from sakipro.memory.retrieval import retrieve_context, format_context_for_llm
from sakipro.ai.llm_client import call_llm_stream
from sakipro.core.config import get_global_context_prompt

class EvidenceReviewAgent(BaseAgent):
    agent_name = "Evidence Reviewer"
    supported_commands = ["/cek-evidence"]
    
    def plan(self, request: Dict[str, Any]) -> Dict[str, Any]:
        user_query = request.get("query", "").strip()
        core_keywords = "Bukti Kinerja Evidence Data Pendukung Lampiran Fisik Verifikasi Realisasi"
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
            "Anda adalah Asisten SAKIP yang ahli dalam memverifikasi bukti kinerja (Evidence).\n"
            "Tugas Anda:\n"
            "1. Hubungkan klaim kinerja dari LKjIP/PK dengan ketersediaan file bukti fisik (evidence).\n"
            "2. Analisis relevansi, verifiabilitas, dan kecukupan bukti tersebut.\n"
            "3. Pastikan untuk selalu menyertakan '[DRAFT: Harap periksa ulang]' di akhir jawaban Anda.\n\n"
            f"{context['context_text']}"
        )
        
        user_message = request.get("query", "Tolong review kelengkapan bukti kinerja (evidence) berdasarkan dokumen terkait.")
        
        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_message}
        ]
        
        return call_llm_stream(messages)
        
    def validate(self, result: Dict[str, Any]) -> Dict[str, Any]:
        pass
