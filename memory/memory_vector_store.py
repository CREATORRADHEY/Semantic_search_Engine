import faiss
import numpy as np


class MemoryVectorStore:

    def __init__(self):

        self.records = []
        self.dimension = None
        self.index = None

    # -----------------------------

    def _ensure_index(self, dimension):

        if self.index is None:
            self.dimension = dimension
            self.index = faiss.IndexFlatIP(dimension)

    # -----------------------------

    def add(self, record):

        embedding = np.array(
            record.embedding,
            dtype=np.float32,
        ).reshape(1, -1)

        self._ensure_index(embedding.shape[1])

        faiss.normalize_L2(embedding)

        self.index.add(embedding)

        self.records.append(record)

    # -----------------------------

    def search(self, query_embedding, top_k=3):

        if self.index is None or len(self.records) == 0:
            return []

        query = np.array(
            query_embedding,
            dtype=np.float32,
        ).reshape(1, -1)

        faiss.normalize_L2(query)

        scores, indices = self.index.search(
            query,
            min(top_k, len(self.records)),
        )

        results = []

        for score, idx in zip(scores[0], indices[0]):

            if idx == -1:
                continue

            if idx >= len(self.records):
                continue

            results.append(
                (float(score), self.records[idx])
            )

        return results

    # -----------------------------

    def count(self):

        return len(self.records)

    def clear(self):

        self.records.clear()

        if self.dimension is not None:
            self.index = faiss.IndexFlatIP(self.dimension)