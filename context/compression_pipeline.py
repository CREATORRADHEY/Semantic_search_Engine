from context.memory_compressor import MemoryCompressor
from context.extractive_compressor import ExtractiveCompressor
from context.adaptive_compressor import AdaptiveCompressor


class CompressionPipeline:
    """
    Enterprise Compression Pipeline.

    Compatible with both legacy tests and the new RAG engine.
    """

    def __init__(self):
        self.memory_compressor = MemoryCompressor()
        self.extractive = ExtractiveCompressor()
        self.adaptive = AdaptiveCompressor()

    def compress(
        self,
        context=None,
        question=None,
        max_sentences=6,
        query=None,
        memory_records=None,
        knowledge_context=None,
    ):
        """
        NEW API
            compress(context=..., question=...)

        OLD API
            compress(
                query=...,
                memory_records=...,
                knowledge_context=...
            )
        """

        # Legacy API support
        if knowledge_context is not None:
            question = query

            memory_context = self.memory_compressor.compress(
                memory_records or [],
                max_tokens=150,
            )

            context = (
                memory_context
                + "\n\n"
                + knowledge_context
            )

        if context is None:
            return ""

        compressed = self.extractive.compress(
            query=question or "",
            context=context,
            top_k=max_sentences,
        )

        compressed = self.adaptive.compress(
            context=compressed,
            query=question,
            max_sentences=max_sentences,
        )

        return compressed