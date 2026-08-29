from models.chunk import Chunk

from retrieval.bm25_retriever import (
    BM25Retriever
)

from retrieval.query_expansion import (
    QueryExpander
)

from retrieval.multi_query_retriever import (
    MultiQueryRetriever
)


texts = [

    "Car insurance protects vehicle owners from financial losses.",

    "Vehicle insurance provides coverage for automobiles.",

    "Artificial Intelligence is changing software engineering.",

    "Machine Learning models learn patterns from data.",

    "Football is a popular sport."

]


chunks = []

for index, text in enumerate(texts):

    chunks.append(
        Chunk(
            document_id="multi-query-demo",
            text=text,
            chunk_index=index
        )
    )


# -----------------------------------------
# BM25
# -----------------------------------------

bm25 = BM25Retriever()

bm25.add_documents(
    chunks
)


# -----------------------------------------
# Query Expansion
# -----------------------------------------

expander = QueryExpander(

    expansions={

        "car": [
            "vehicle",
            "automobile"
        ]

    }

)


# -----------------------------------------
# Multi Query Retriever
# -----------------------------------------

retriever = MultiQueryRetriever(
    retriever=bm25,
    query_expander=expander
)


# -----------------------------------------
# Search
# -----------------------------------------

query = "car insurance"

results = retriever.search(
    query,
    top_k=5
)


# -----------------------------------------
# Display
# -----------------------------------------

print("=" * 60)

print("Multi-Query Search Results")

print("=" * 60)

print()

for result in results:

    print(
        f"{result.score:.4f} -> "
        f"{result.text}"
    )