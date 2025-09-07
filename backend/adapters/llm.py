import os

class LLMClient:
    """Simple adapter selecting provider via env var.

    Currently supports a LOCAL stub that returns deterministic text.
    Providers: OPENAI, GEMINI, LOCAL.
    """

    def __init__(self) -> None:
        self.provider = os.getenv("LLM_PROVIDER", "LOCAL").upper()

    def generate(self, prompt: str) -> str:
        if self.provider == "LOCAL":
            return "Stub answer for: " + prompt
        # Future real implementations would go here
        return "Unsupported provider"
