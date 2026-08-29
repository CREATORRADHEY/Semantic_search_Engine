class MemoryCompressor:

    def estimate_tokens(self, text):

        return max(1, len(text.split()))

    def compress(
        self,
        memories,
        max_tokens=150
    ):

        compressed = []

        used_tokens = 0

        for memory in memories:

            text = (
                f"User: {memory.user_message}\n"
                f"Assistant: {memory.assistant_message}"
            )

            tokens = self.estimate_tokens(text)

            if used_tokens + tokens > max_tokens:
                continue

            compressed.append(text)

            used_tokens += tokens

        return "\n\n".join(compressed)