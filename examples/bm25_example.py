from models.chunk import Chunk

from retrieval.bm25_retriever import (
    BM25Retriever
)


texts = [

    "FAISS is a library for efficient similarity search.",

    "Artificial Intelligence is changing software engineering.",

    "Machine Learning models learn patterns from data.",

    "IndexFlatIP performs exact inner product search in FAISS.",

    "Neural networks learn representations using optimization."

]


chunks = []

for index, text in enumerate(texts):

    chunks.append(
        Chunk(
            document_id="bm25-demo",
            text=text,
            chunk_index=index
        )
    )


retriever = BM25Retriever()

retriever.add_documents(
    chunks
)


queries = [

    "FAISS IndexFlatIP",

    "neural networks",

    "software engineering"

]


for query in queries:

    print("=" * 60)

    print(
        f"Query: {query}"
    )

    print("=" * 60)

    results = retriever.search(
        query,
        top_k=3
    )

    for result in results:

        print(
            f"{result.score:.4f} -> "
            f"{result.text}"
        )

    print()