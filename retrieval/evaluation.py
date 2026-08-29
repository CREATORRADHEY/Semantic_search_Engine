from math import log2

from models.search_result import SearchResult


class RetrievalEvaluator:

    @staticmethod
    def recall_at_k(
        results: list[SearchResult],
        relevant_chunk_ids: set[str],
        k: int
    ) -> float:

        if not relevant_chunk_ids:

            return 0.0

        retrieved_ids = {
            result.chunk_id
            for result in results[:k]
        }

        relevant_retrieved = (
            retrieved_ids
            & relevant_chunk_ids
        )

        return (
            len(relevant_retrieved)
            / len(relevant_chunk_ids)
        )

    @staticmethod
    def hit_rate_at_k(
        results: list[SearchResult],
        relevant_chunk_ids: set[str],
        k: int
    ) -> float:

        if not relevant_chunk_ids:

            return 0.0

        retrieved_ids = {
            result.chunk_id
            for result in results[:k]
        }

        return float(
            bool(
                retrieved_ids
                & relevant_chunk_ids
            )
        )

    @staticmethod
    def reciprocal_rank(
        results: list[SearchResult],
        relevant_chunk_ids: set[str]
    ) -> float:

        for rank, result in enumerate(
            results,
            start=1
        ):

            if result.chunk_id in relevant_chunk_ids:

                return 1.0 / rank

        return 0.0

    @staticmethod
    def ndcg_at_k(
        results: list[SearchResult],
        relevance_scores: dict[str, float],
        k: int
    ) -> float:

        if not relevance_scores:

            return 0.0

        dcg = 0.0

        for rank, result in enumerate(
            results[:k],
            start=1
        ):

            relevance = relevance_scores.get(
                result.chunk_id,
                0.0
            )

            dcg += (
                relevance
                / log2(rank + 1)
            )

        ideal_scores = sorted(
            relevance_scores.values(),
            reverse=True
        )[:k]

        idcg = 0.0

        for rank, relevance in enumerate(
            ideal_scores,
            start=1
        ):

            idcg += (
                relevance
                / log2(rank + 1)
            )

        if idcg == 0.0:

            return 0.0

        return dcg / idcg