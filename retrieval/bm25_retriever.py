from rank_bm25 import BM25Okapi

from models.chunk import Chunk
from models.search_result import SearchResult


class BM25Retriever:

    def __init__(self):

        self.chunks: list[Chunk] = []

        self.tokenized_documents = []

        self.bm25 = None

    def add_documents(
        self,
        chunks: list[Chunk]
    ):

        self.chunks.extend(
            chunks
        )

        self.tokenized_documents.extend(
            [
                self.tokenize(chunk.text)
                for chunk in chunks
            ]
        )

        self.bm25 = BM25Okapi(
            self.tokenized_documents
        )

    @staticmethod
    def tokenize(
        text: str
    ) -> list[str]:

        return text.lower().split()

    def search(
        self,
        query: str,
        top_k: int = 5
    ) -> list[SearchResult]:

        if not self.chunks:

            return []

        query_tokens = self.tokenize(
            query
        )

        scores = self.bm25.get_scores(
            query_tokens
        )

        ranked_indices = sorted(
            range(len(scores)),
            key=lambda index: scores[index],
            reverse=True
        )

        results = []

        for index in ranked_indices[:top_k]:

            chunk = self.chunks[index]

            results.append(
                SearchResult(
                    score=float(scores[index]),
                    text=chunk.text,
                    chunk_id=f"{chunk.document_id}:{chunk.chunk_index}",
                    document_id=chunk.document_id,
                    metadata=chunk.metadata
                )
            )

        return results