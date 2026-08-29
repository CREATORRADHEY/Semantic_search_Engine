from compression.sentence_scorer import SentenceScorer


class AdaptiveCompressor:

    def __init__(self):

        self.scorer = SentenceScorer()

    def estimate_tokens(self, text: str):

        return max(1, len(text.split()))

    def compress(
        self,
        query: str,
        text: str,
        max_tokens: int = 120
    ):

        ranked = self.scorer.score(query, text)

        compressed = []

        used_tokens = 0

        for score, sentence in ranked:

            sentence_tokens = self.estimate_tokens(sentence)

            if used_tokens + sentence_tokens > max_tokens:
                continue

            compressed.append((sentence, score))

            used_tokens += sentence_tokens

        compressed.sort(key=lambda x: text.index(x[0]))

        return " ".join(sentence for sentence, _ in compressed)