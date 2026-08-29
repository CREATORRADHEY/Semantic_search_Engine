from context.adaptive_compressor import AdaptiveCompressor
from context.memory_compressor import MemoryCompressor


class CompressionPipeline:

    def __init__(self):

        self.adaptive = AdaptiveCompressor()

        self.memory = MemoryCompressor()

    def compress(
        self,
        query,
        memory_records,
        knowledge_context,
        memory_budget=150,
        knowledge_budget=800
    ):

        compressed_memory = self.memory.compress(
            memory_records,
            max_tokens=memory_budget
        )

        compressed_knowledge = self.adaptive.compress(
            query=query,
            text=knowledge_context,
            max_tokens=knowledge_budget
        )

        return (
            "## Conversation Memory\n"
            f"{compressed_memory}\n\n"
            "## Knowledge Context\n"
            f"{compressed_knowledge}"
        )