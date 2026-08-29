from retrieval.rrf import ReciprocalRankFusion


class HybridRetriever:

    def __init__(
        self,
        bm25_retriever,
        vector_store,
        embedder,
        fusion: ReciprocalRankFusion | None = None
    ):

        self.bm25 = bm25_retriever

        self.vector_store = vector_store

        self.embedder = embedder

        self.fusion = (
            fusion
            if fusion is not None
            else ReciprocalRankFusion()
        )

    def search(
        self,
        query: str,
        top_k: int = 5
    ):

        # -----------------------------------------
        # BM25 retrieval
        # -----------------------------------------

        bm25_results = self.bm25.search(
            query,
            top_k=top_k
        )

        # -----------------------------------------
        # Semantic retrieval
        # -----------------------------------------

        query_embedding = self.embedder.embed(
            [query]
        )[0]

        vector_results = self.vector_store.search(
            query_embedding,
            top_k=top_k
        )

        # -----------------------------------------
        # Fusion
        # -----------------------------------------

        return self.fusion.fuse(
            [
                bm25_results,
                vector_results
            ],
            top_k=top_k
        )