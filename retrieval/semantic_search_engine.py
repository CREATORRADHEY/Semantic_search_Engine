from embeddings.base_embedder import BaseEmbedder
from vector_store.base_vector_store import BaseVectorStore


class SemanticSearchEngine:

    def __init__(
        self,
        embedder: BaseEmbedder,
        vector_store: BaseVectorStore
    ):

        self.embedder = embedder
        self.vector_store = vector_store

    def search(
        self,
        query: str,
        top_k: int = 5
    ):

        query_embedding = self.embedder.embed(
            [query]
        )[0]

        return self.vector_store.search(
            query_embedding,
            top_k
        )