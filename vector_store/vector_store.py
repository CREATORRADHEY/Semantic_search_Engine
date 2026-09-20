import faiss
import numpy as np

from models.document import Document


class VectorStore:
    """
    Dense vector store backed by FAISS.

    Stores Document objects alongside their embeddings and supports
    cosine-similarity search using IndexFlatIP.
    """

    def __init__(self, dimension: int = 384):
        self.dimension = dimension
        self.index = faiss.IndexFlatIP(dimension)
        self.documents: list[Document] = []

    def add(self, embedding, document: Document):
        embedding = np.asarray(embedding, dtype=np.float32).reshape(1, -1)

        if embedding.shape[1] != self.dimension:
            raise ValueError(
                f"Embedding dimension {embedding.shape[1]} "
                f"does not match store dimension {self.dimension}."
            )

        faiss.normalize_L2(embedding)

        self.index.add(embedding)
        self.documents.append(document)

    def add_many(self, embeddings, documents):
        if len(embeddings) != len(documents):
            raise ValueError("Embeddings and documents length mismatch.")

        matrix = np.asarray(embeddings, dtype=np.float32)

        if matrix.ndim != 2:
            raise ValueError("Embeddings must be a 2D array.")

        if matrix.shape[1] != self.dimension:
            raise ValueError(
                f"Embedding dimension {matrix.shape[1]} "
                f"does not match store dimension {self.dimension}."
            )

        faiss.normalize_L2(matrix)

        self.index.add(matrix)
        self.documents.extend(documents)

    def search(self, query_embedding, top_k: int = 5):
        if self.index.ntotal == 0:
            return []

        query = np.asarray(query_embedding, dtype=np.float32).reshape(1, -1)

        if query.shape[1] != self.dimension:
            raise ValueError(
                f"Query dimension {query.shape[1]} "
                f"does not match store dimension {self.dimension}."
            )

        faiss.normalize_L2(query)

        scores, indices = self.index.search(
            query,
            min(top_k, self.index.ntotal),
        )

        results = []

        for score, idx in zip(scores[0], indices[0]):
            if idx == -1:
                continue

            results.append(
                (
                    float(score),
                    self.documents[idx],
                )
            )

        return results

    def count(self):
        return len(self.documents)

    def clear(self):
        self.index = faiss.IndexFlatIP(self.dimension)
        self.documents = []