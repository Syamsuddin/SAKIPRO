from typing import Protocol, Dict, Any, List

class BaseAgent(Protocol):
    agent_name: str
    supported_commands: List[str]
    
    def plan(self, request: Dict[str, Any]) -> Dict[str, Any]:
        """Determine what context is needed."""
        ...
        
    def gather_context(self, plan: Dict[str, Any]) -> Dict[str, Any]:
        """Retrieve from database/storage."""
        ...
        
    def run(self, request: Dict[str, Any]) -> Dict[str, Any]:
        """Execute the AI pipeline."""
        ...
        
    def validate(self, result: Dict[str, Any]) -> Dict[str, Any]:
        """Ensure guardrails and schemas are respected."""
        ...
