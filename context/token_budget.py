class TokenBudget:
    """
    Simple token budget manager used by the RAG engine.

    We approximate tokens using whitespace-separated words so the
    project works without requiring a tokenizer dependency.
    """

    def __init__(self, max_tokens: int = 1200):
        self.max_tokens = max_tokens

    def estimate_tokens(self, text: str) -> int:
        if not text:
            return 0
        return len(text.split())

    def trim_context(self, context: str) -> str:
        if not context:
            return ""

        words = context.split()

        if len(words) <= self.max_tokens:
            return context

        return " ".join(words[: self.max_tokens])

    def remaining_budget(self, prompt: str) -> int:
        used = self.estimate_tokens(prompt)
        return max(self.max_tokens - used, 0)

    def fits(self, prompt: str, context: str) -> bool:
        total = (
            self.estimate_tokens(prompt)
            + self.estimate_tokens(context)
        )
        return total <= self.max_tokens


class TokenBudgetManager(TokenBudget):
    """
    Backward-compatible alias used by the unit tests.
    """
    pass