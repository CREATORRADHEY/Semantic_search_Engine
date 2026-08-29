from models.vector_record import VectorRecord
from models.search_result import SearchResult

from vector_store.base_vector_store import BaseVectorStore
from similarity.cosine_similarity import CosineSimilarity


class MemoryVectorStore(BaseVectorStore):

    def __init__(self):

        self.records = []

    def add(
        self,
        record: VectorRecord
    ):

        self.records.append(
            record
        )

    def search(
        self,
        query_embedding,
        top_k: int = 5,
        filters: dict | None = None
    ) -> list[SearchResult]:

        results = []

        for record in self.records:

            if filters:

                metadata = record.chunk.metadata

                matches = True

                for key, expected_value in filters.items():

                    if metadata.get(key) != expected_value:

                        matches = False

                        break

                if not matches:

                    continue

            score = CosineSimilarity.calculate(
                query_embedding,
                record.embedding
            )

            results.append(
                SearchResult(
                    score=float(score),
                    text=record.chunk.text,
                    metadata=record.chunk.metadata
                )
            )

        results.sort(
            key=lambda result: result.score,
            reverse=True
        )

        return results[:top_k]