from context.extractive_compressor import ExtractiveCompressor


class AdaptiveCompressor:
    """
    Adaptive compressor compatible with both old and new APIs.
    """

    def __init__(self):
        self.extractive = ExtractiveCompressor()

    def compress(
        self,
        context=None,
        max_sentences=6,
        query=None,
        text=None,
        max_tokens=None,
    ):
        """
        Supports:

        OLD:
            compress(query=..., text=..., max_tokens=...)

        NEW:
            compress(context, max_sentences=...)
        """

        # Backward compatibility
        if text is not None:
            context = text

            if max_tokens is not None:
                max_sentences = max(1, max_tokens // 5)

        if context is None:
            return ""

        return self.extractive.compress(
            query=query or "",
            context=context,
            top_k=max_sentences,
        )