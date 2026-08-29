from embeddings.sentence_transformer_embedder import (
    SentenceTransformerEmbedder
)

from models.search_result import SearchResult

from retrieval.query_expansion import QueryExpander
from retrieval.rrf import ReciprocalRankFusion

from reranking.cross_encoder_reranker import (
    CrossEncoderReranker
)


class MultiQueryHybridRetriever:
    """
    Production Hybrid Retrieval Pipeline

    Query
      ↓
    Query Expansion
      ↓
    BM25 + FAISS Retrieval
      ↓
    Reciprocal Rank Fusion
      ↓
    CrossEncoder Reranking
      ↓
    Final Top-K Results
    """

    def __init__(
        self,
        bm25_retriever,
        faiss_retriever,
        query_expander: QueryExpander,
        embedder: SentenceTransformerEmbedder,
        reranker: CrossEncoderReranker | None = None
    ):

        self.bm25 = bm25_retriever
        self.faiss = faiss_retriever
        self.expander = query_expander
        self.embedder = embedder

        self.rrf = ReciprocalRankFusion()

        self.reranker = reranker

    def search(
        self,
        query: str,
        top_k: int = 5,
        rerank_top_k: int = 10
    ) -> list[SearchResult]:

        # -----------------------------------------
        # Step 1: Expand Query
        # -----------------------------------------

        expanded_queries = self.expander.expand(query)

        # -----------------------------------------
        # Step 2: Batch Embed Expanded Queries
        # -----------------------------------------

        query_embeddings = self.embedder.embed(
            expanded_queries
        )

        bm25_rankings = []
        faiss_rankings = []

        # -----------------------------------------
        # Step 3: Retrieve Candidates
        # -----------------------------------------

        for expanded_query, embedding in zip(
            expanded_queries,
            query_embeddings
        ):

            bm25_results = self.bm25.search(
                expanded_query,
                top_k=rerank_top_k
            )

            faiss_results = self.faiss.search(
                embedding,
                top_k=rerank_top_k
            )

            bm25_rankings.append(bm25_results)
            faiss_rankings.append(faiss_results)

        # -----------------------------------------
        # Step 4: Fuse Rankings
        # -----------------------------------------

        fused_results = self.rrf.fuse(
            bm25_rankings + faiss_rankings,
            top_k=rerank_top_k
        )

        # -----------------------------------------
        # Step 5: Neural Reranking
        # -----------------------------------------

        if self.reranker is not None:

            fused_results = self.reranker.rerank(
                query=query,
                results=fused_results,
                top_k=top_k
            )

        else:

            fused_results = fused_results[:top_k]

        return fused_results