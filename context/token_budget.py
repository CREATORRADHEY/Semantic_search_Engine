class TokenBudgetManager:
    """
    Simple token budget estimator.

    Uses a character-to-token approximation.
    We'll replace this with exact tokenizers
    in Chapter 41.
    """

    def __init__(
        self,
        max_tokens: int = 3000,
        chars_per_token: int = 4
    ):

        self.max_tokens = max_tokens
        self.chars_per_token = chars_per_token

    def estimate_tokens(
        self,
        text: str
    ) -> int:

        return max(
            1,
            len(text) // self.chars_per_token
        )

    def trim_context(
        self,
        context: str
    ) -> str:

        estimated_tokens = self.estimate_tokens(
            context
        )

        if estimated_tokens <= self.max_tokens:
            return context

        max_characters = (
            self.max_tokens *
            self.chars_per_token
        )

        return context[:max_characters]