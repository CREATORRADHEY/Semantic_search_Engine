from sentence_transformers import CrossEncoder

from models.search_result import SearchResult


class CrossEncoderReranker:
    """
    CrossEncoder-based reranker.

    Input:
        Query + Retrieved Search Results

    Output:
        Same Search Results sorted by CrossEncoder relevance.
    """

    def __init__(
        self,
        model_name: str = (
            "cross-encoder/ms-marco-MiniLM-L-6-v2"
        )
    ):

        self.model = CrossEncoder(model_name)

    def rerank(
        self,
        query: str,
        results: list[SearchResult],
        top_k: int = 5
    ) -> list[SearchResult]:

        if not results:
            return []

        sentence_pairs = [
            (query, result.text)
            for result in results
        ]

        scores = self.model.predict(
            sentence_pairs
        )

        reranked_results = []

        for result, score in zip(
            results,
            scores
        ):

            reranked_results.append(

                SearchResult(
                    document_id=result.document_id,
                    chunk_id=result.chunk_id,
                    text=result.text,
                    metadata=result.metadata,
                    score=float(score)
                )

            )

        reranked_results.sort(
            key=lambda result: result.score,
            reverse=True
        )

        return reranked_results[:top_k]