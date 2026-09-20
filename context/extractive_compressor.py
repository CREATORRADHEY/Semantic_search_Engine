from context.sentence_scorer import SentenceScorer


class ExtractiveCompressor:
    """
    Extracts the most relevant sentences from a context block.
    """

    def __init__(self):
        self.scorer = SentenceScorer()

    def compress(
        self,
        context: str,
        query: str,
        top_k: int = 5,
    ) -> str:

        if not context.strip():
            return ""

        sentences = [
            sentence.strip()
            for sentence in context.replace("\n", " ").split(".")
            if sentence.strip()
        ]

        ranked = self.scorer.rank(
            query=query,
            sentences=sentences,
        )

        selected = ranked[:top_k]

        if not selected:
            return ""

        return ". ".join(selected) + "."