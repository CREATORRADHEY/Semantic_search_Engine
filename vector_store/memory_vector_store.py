from typing import List

from models.vector_record import VectorRecord
from models.search_result import SearchResult

from similarity.cosine_similarity import CosineSimilarity
from vector_store.base_vector_store import BaseVectorStore


class MemoryVectorStore(BaseVectorStore):

    def __init__(self):

        self.records: List[VectorRecord] = []

    def add(
        self,
        record: VectorRecord
    ):

        self.records.append(record)

    def search(
        self,
        query_embedding: List[float],
        top_k: int = 5
    ) -> List[SearchResult]:

        results = []

        for record in self.records:

            similarity = CosineSimilarity.calculate(
                query_embedding,
                record.embedding
            )

            results.append(
                SearchResult(
                    score=float(similarity),
                    text=record.chunk.text,
                    chunk_id=(
                        f"{record.chunk.document_id}:"
                        f"{record.chunk.chunk_index}"
                    ),
                    document_id=record.chunk.document_id,
                    metadata=record.chunk.metadata
                )
            )

        results.sort(
            key=lambda result: result.score,
            reverse=True
        )

        return results[:top_k]