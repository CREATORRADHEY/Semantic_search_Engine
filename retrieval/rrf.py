from models.search_result import SearchResult


class ReciprocalRankFusion:

    def __init__(
        self,
        k: int = 60
    ):

        self.k = k

    def fuse(
        self,
        result_lists: list[list[SearchResult]],
        top_k: int = 5
    ) -> list[SearchResult]:

        scores = {}

        results_by_key = {}

        # -----------------------------------------
        # Process every retrieval result list
        # -----------------------------------------

        for results in result_lists:

            for rank, result in enumerate(
                results,
                start=1
            ):

                key = self._get_key(
                    result
                )

                rrf_score = (
                    1.0
                    / (
                        self.k + rank
                    )
                )

                scores[key] = (
                    scores.get(
                        key,
                        0.0
                    )
                    + rrf_score
                )

                results_by_key[key] = result

        # -----------------------------------------
        # Rank by fused RRF score
        # -----------------------------------------

        ranked_keys = sorted(
            scores,
            key=scores.get,
            reverse=True
        )

        # -----------------------------------------
        # Build final SearchResult objects
        # -----------------------------------------

        fused_results = []

        for key in ranked_keys[:top_k]:

            original_result = (
                results_by_key[key]
            )

            fused_results.append(
                SearchResult(
                    score=scores[key],
                    text=original_result.text,
                    chunk_id=original_result.chunk_id,
                    document_id=original_result.document_id,
                    metadata=original_result.metadata
                )
            )

        return fused_results

    @staticmethod
    def _get_key(
        result: SearchResult
    ) -> str:

        return result.chunk_id