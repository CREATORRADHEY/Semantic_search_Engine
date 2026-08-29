from models.search_result import SearchResult

from retrieval.query_expansion import (
    QueryExpander
)


class MultiQueryRetriever:

    def __init__(
        self,
        retriever,
        query_expander: QueryExpander
    ):

        self.retriever = retriever

        self.query_expander = (
            query_expander
        )

    def search(
        self,
        query: str,
        top_k: int = 5
    ) -> list[SearchResult]:

        expanded_queries = (
            self.query_expander.expand(
                query
            )
        )

        all_results = []

        seen_chunks = set()

        for expanded_query in (
            expanded_queries
        ):

            results = self.retriever.search(
                expanded_query,
                top_k=top_k
            )

            for result in results:

                if result.chunk_id in seen_chunks:

                    continue

                seen_chunks.add(
                    result.chunk_id
                )

                all_results.append(
                    result
                )

        all_results.sort(
            key=lambda result: result.score,
            reverse=True
        )

        return all_results[:top_k]