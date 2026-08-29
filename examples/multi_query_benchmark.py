import time

from embeddings.sentence_transformer_embedder import (
    SentenceTransformerEmbedder
)

from models.chunk import Chunk
from models.vector_record import VectorRecord

from retrieval.bm25_retriever import BM25Retriever
from retrieval.query_expansion import QueryExpander
from retrieval.multi_query_hybrid import (
    MultiQueryHybridRetriever
)

from vector_store.faiss_vector_store import (
    FAISSVectorStore
)


ITERATIONS = 20


texts = [
    "Car insurance protects vehicle owners.",
    "Vehicle insurance covers automobiles.",
    "Automobile coverage includes liability.",
    "Artificial Intelligence powers retrieval.",
    "Machine Learning improves ranking."
]

chunks = []

for index, text in enumerate(texts):

    chunks.append(
        Chunk(
            document_id="benchmark",
            text=text,
            chunk_index=index
        )
    )

bm25 = BM25Retriever()
bm25.add_documents(chunks)

embedder = SentenceTransformerEmbedder()

embeddings = embedder.embed(texts)

faiss = FAISSVectorStore()

for chunk, embedding in zip(chunks, embeddings):

    faiss.add(
        VectorRecord(
            chunk=chunk,
            embedding=embedding
        )
    )

expander = QueryExpander(
    expansions={
        "car": ["vehicle", "automobile"]
    }
)

hybrid = MultiQueryHybridRetriever(
    bm25,
    faiss,
    expander,
    embedder
)


query_embedding = embedder.embed(
    ["car insurance"]
)[0]


def benchmark(function):

    function()

    start = time.perf_counter()

    for _ in range(ITERATIONS):
        function()

    return (
        (time.perf_counter() - start)
        / ITERATIONS
    )


single_latency = benchmark(
    lambda: faiss.search(query_embedding)
)

multi_latency = benchmark(
    lambda: hybrid.search("car insurance")
)


print("=" * 60)
print("Single Query vs Multi Query")
print("=" * 60)
print()
print(f"Single Query : {single_latency*1000:.3f} ms")
print(f"Multi Query  : {multi_latency*1000:.3f} ms")