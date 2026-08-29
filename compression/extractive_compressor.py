from compression.sentence_scorer import SentenceScorer
from compression.sentence_splitter import SentenceSplitter


class ExtractiveCompressor:

    def __init__(self):

        self.scorer = SentenceScorer()

    def compress(
        self,
        query: str,
        text: str,
        max_sentences: int = 2
    ):

        ranked = self.scorer.score(
            query,
            text
        )

        selected = ranked[:max_sentences]

        selected_sentences = {
            sentence
            for _, sentence in selected
        }

        ordered = SentenceSplitter.split(text)

        compressed = [
            sentence
            for sentence in ordered
            if sentence in selected_sentences
        ]

        return " ".join(compressed)