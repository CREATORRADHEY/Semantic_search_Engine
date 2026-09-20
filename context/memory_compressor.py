class MemoryCompressor:
    """
    Compresses conversation memories into a compact prompt block.
    """

    def compress(
        self,
        memories,
        max_tokens: int = 150,
    ) -> str:

        if not memories:
            return ""

        compressed = []
        used_tokens = 0

        for memory in memories:

            text = (
                f"User: {memory.user_message}\n"
                f"Assistant: {memory.assistant_message}"
            )

            tokens = len(text.split())

            if used_tokens + tokens > max_tokens:
                break

            compressed.append(text)
            used_tokens += tokens

        return "\n\n".join(compressed)