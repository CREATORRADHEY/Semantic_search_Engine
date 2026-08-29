import faiss
import numpy as np

from memory.memory_record import MemoryRecord


class MemoryVectorStore:
    """
    FAISS vector database dedicated to conversation memories.
    """

    def __init__(self):
        self.index = None
        self.records: list[MemoryRecord] = []

    def _create_index(self, dimension: int):
        self.index = faiss.IndexFlatIP(dimension)

    def add(self, record: MemoryRecord):

        if self.index is None:
            self._create_index(len(record.embedding))

        vector = np.array([record.embedding], dtype=np.float32)

        faiss.normalize_L2(vector)

        self.index.add(vector)

        self.records.append(record)

    def add_batch(self, records: list[MemoryRecord]):

        if not records:
            return

        if self.index is None:
            self._create_index(len(records[0].embedding))

        vectors = np.array(
            [record.embedding for record in records],
            dtype=np.float32,
        )

        faiss.normalize_L2(vectors)

        self.index.add(vectors)

        self.records.extend(records)

    def search(
        self,
        query_embedding: list[float],
        top_k: int = 3,
    ) -> list[tuple[float, MemoryRecord]]:

        if self.index is None:
            return []

        query = np.array([query_embedding], dtype=np.float32)

        faiss.normalize_L2(query)

        scores, indices = self.index.search(query, top_k)

        results = []

        for score, idx in zip(scores[0], indices[0]):

            if idx == -1:
                continue

            results.append(
                (
                    float(score),
                    self.records[idx]
                )
            )

        return results

    def count(self):

        return len(self.records)