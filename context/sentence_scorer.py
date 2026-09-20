from embeddings.sentence_transformer_embedder import SentenceTransformerEmbedder
import numpy as np


class SentenceScorer:
    """
    Scores sentences by cosine similarity with the user's query.
    Used by ExtractiveCompressor.
    """

    def __init__(self):
        self.embedder = SentenceTransformerEmbedder()

    def rank(
        self,
        query: str,
        sentences: list[str],
    ) -> list[str]:

        if not sentences:
            return []

        query_embedding = self.embedder.embed([query])[0]

        sentence_embeddings = self.embedder.embed(sentences)

        scores = []

        for sentence, embedding in zip(sentences, sentence_embeddings):
            similarity = float(
                np.dot(query_embedding, embedding)
                / (
                    np.linalg.norm(query_embedding)
                    * np.linalg.norm(embedding)
                )
            )

            scores.append((similarity, sentence))

        scores.sort(reverse=True, key=lambda item: item[0])

        return [sentence for _, sentence in scores]