class QueryExpander:

    def __init__(
        self,
        expansions: dict[str, list[str]]
    ):

        self.expansions = expansions

    def expand(
        self,
        query: str
    ) -> list[str]:

        normalized_query = (
            query.lower().strip()
        )

        queries = [
            query
        ]

        for keyword, alternatives in (
            self.expansions.items()
        ):

            if keyword in normalized_query:

                for alternative in alternatives:

                    expanded_query = (
                        normalized_query
                        .replace(
                            keyword,
                            alternative
                        )
                    )

                    queries.append(
                        expanded_query
                    )

        return list(
            dict.fromkeys(queries)
        )