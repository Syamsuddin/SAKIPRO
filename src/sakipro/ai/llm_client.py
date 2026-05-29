import litellm
import logging

# Suppress annoying LiteLLM warnings about optional dependencies (e.g., botocore for bedrock)
litellm.suppress_debug_info = True
logging.getLogger("LiteLLM").setLevel(logging.ERROR)

from sakipro.core.config import settings

def call_llm_stream(messages: list[dict], model: str = settings.default_model):
    """Call LLM and yield streaming chunks."""
    try:
        response = litellm.completion(
            model=model,
            messages=messages,
            stream=True
        )
        for chunk in response:
            if chunk.choices[0].delta.content is not None:
                yield chunk.choices[0].delta.content
    except Exception as e:
        yield f"\n[Error memanggil AI: {e}]"

def call_llm(messages: list[dict], model: str = settings.default_model) -> str:
    """Call LLM synchronously."""
    try:
        response = litellm.completion(
            model=model,
            messages=messages
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"[Error memanggil AI: {e}]"
