from typing import Dict, Any, Generator
from sakipro.agents.base import BaseAgent
from sakipro.memory.retrieval import retrieve_context, format_context_for_llm
from sakipro.ai.llm_client import call_llm_stream
from sakipro.core.config import get_global_context_prompt

class AskAgent(BaseAgent):
    agent_name = "Ask Agent (Chat)"
    supported_commands = [] # Not bound to a specific slash command
    
    def plan(self, request: Dict[str, Any]) -> Dict[str, Any]:
        query = request.get("query", "")
        return {"search_query": query}
        
    def gather_context(self, plan: Dict[str, Any]) -> Dict[str, Any]:
        raw_context = retrieve_context(plan["search_query"])
        formatted = format_context_for_llm(raw_context)
        return {"context_text": formatted}
        
    def run(self, request: Dict[str, Any]) -> Generator[str, None, None]:
        plan = self.plan(request)
        context = self.gather_context(plan)
        
        system_prompt = (
            get_global_context_prompt() +
            "Anda adalah Asisten AI SAKIPRO yang bertugas menjawab pertanyaan umum atau berdiskusi "
            "dengan pengguna secara natural (bahasa manusiawi) berdasarkan dokumen yang telah di-scan.\n"
            "Tugas Anda:\n"
            "1. Jawab pertanyaan pengguna dengan ramah, profesional, dan ringkas.\n"
            "2. Gunakan konteks dokumen di bawah ini jika relevan untuk menjawab.\n"
            "3. Jika Anda mengutip data dari dokumen, wajib sertakan sumber referensinya (contoh: [Sumber: renstra.pdf]).\n"
            "4. Pastikan untuk selalu menyertakan '[DRAFT: Harap periksa ulang]' di akhir jawaban Anda.\n\n"
            f"Konteks Dokumen:\n{context['context_text']}"
        )
        
        user_message = request.get("query", "")
        
        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_message}
        ]
        
        return call_llm_stream(messages)
        
    def validate(self, result: Dict[str, Any]) -> Dict[str, Any]:
        pass
