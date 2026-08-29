from retrieval.query_expansion import (
    QueryExpander
)


expander = QueryExpander(

    expansions={

        "car": [
            "vehicle",
            "automobile"
        ],

        "ai": [
            "artificial intelligence",
            "machine intelligence"
        ],

        "search": [
            "retrieval",
            "information retrieval"
        ]

    }

)


queries = [

    "car insurance",

    "AI systems",

    "semantic search"

]


for query in queries:

    print("=" * 60)

    print(
        f"Original: {query}"
    )

    print()

    expanded_queries = (
        expander.expand(query)
    )

    for expanded_query in (
        expanded_queries
    ):

        print(
            f"  -> {expanded_query}"
        )
        