from embeddings.sentence_transformer_embedder import (
    SentenceTransformerEmbedder
)

from similarity.cosine_similarity import CosineSimilarity

from compression.sentence_splitter import SentenceSplitter


class SentenceScorer:

    def __init__(self):

        self.embedder = SentenceTransformerEmbedder()

    def score(
        self,
        query: str,
        text: str
    ):

        sentences = SentenceSplitter.split(text)

        query_embedding = self.embedder.embed(
            [query]
        )[0]

        sentence_embeddings = self.embedder.embed(
            sentences
        )

        ranked = []

        for sentence, embedding in zip(
            sentences,
            sentence_embeddings
        ):

            similarity = CosineSimilarity.calculate(
                query_embedding,
                embedding
            )

            ranked.append(
                (
                    similarity,
                    sentence
                )
            )

        ranked.sort(
            key=lambda x: x[0],
            reverse=True
        )

        return ranked