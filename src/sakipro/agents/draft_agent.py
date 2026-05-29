from typing import Dict, Any, Generator
from sakipro.agents.base import BaseAgent
from sakipro.memory.retrieval import retrieve_context, format_context_for_llm
from sakipro.ai.llm_client import call_llm_stream
from sakipro.core.config import get_global_context_prompt

class DraftAgent(BaseAgent):
    agent_name = "Draft Agent"
    supported_commands = ["/draft"]
    
    def plan(self, request: Dict[str, Any]) -> Dict[str, Any]:
        query = request.get("query", "revisi redaksi indikator sasaran")
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
            "Anda adalah Asisten SAKIP yang ahli dalam menyusun draf (Drafting) usulan redaksional.\n"
            "Tugas Anda:\n"
            "1. Memberikan usulan perbaikan kalimat untuk indikator, program, atau sasaran yang tidak tepat.\n"
            "2. Usulan harus berorientasi pada Hasil (Outcome/Impact) sesuai kaidah SAKIP.\n"
            "3. Pastikan untuk selalu menyertakan '[DRAFT: Harap periksa ulang]' di akhir usulan Anda.\n\n"
            f"{context['context_text']}"
        )
        
        user_message = request.get("query", "Tolong berikan draf usulan perbaikan redaksi kinerja.")
        
        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_message}
        ]
        
        return call_llm_stream(messages)
        
    def validate(self, result: Dict[str, Any]) -> Dict[str, Any]:
        pass
