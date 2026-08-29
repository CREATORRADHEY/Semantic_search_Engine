from embeddings.sentence_transformer_embedder import (
    SentenceTransformerEmbedder
)

from models.chunk import Chunk
from models.vector_record import VectorRecord

from retrieval.bm25_retriever import (
    BM25Retriever
)

from retrieval.rrf import (
    ReciprocalRankFusion
)

from vector_store.faiss_vector_store import (
    FAISSVectorStore
)


# -----------------------------------------
# Create shared chunks
# -----------------------------------------

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
            document_id="hybrid-demo",
            text=text,
            chunk_index=index,
            metadata={
                "source": "demo"
            }
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
# Embeddings
# -----------------------------------------

embedder = SentenceTransformerEmbedder()

embeddings = embedder.embed(
    texts
)


# -----------------------------------------
# FAISS
# -----------------------------------------

faiss_store = FAISSVectorStore()

records = []

for chunk, embedding in zip(
    chunks,
    embeddings
):

    records.append(
        VectorRecord(
            chunk=chunk,
            embedding=embedding
        )
    )


faiss_store.add_batch(
    records
)


# -----------------------------------------
# Query
# -----------------------------------------

query = "FAISS IndexFlatIP"


# -----------------------------------------
# BM25 Search
# -----------------------------------------

bm25_results = bm25.search(
    query,
    top_k=3
)


# -----------------------------------------
# Semantic Search
# -----------------------------------------

query_embedding = embedder.embed(
    [query]
)[0]


faiss_results = faiss_store.search(
    query_embedding,
    top_k=3
)


# -----------------------------------------
# RRF
# -----------------------------------------

fusion = ReciprocalRankFusion()

hybrid_results = fusion.fuse(
    [
        bm25_results,
        faiss_results
    ],
    top_k=5
)


# -----------------------------------------
# Output
# -----------------------------------------

print("=" * 60)

print("HYBRID SEARCH RESULTS")

print("=" * 60)

print()

for result in hybrid_results:

    print(
        f"{result.score:.6f} -> "
        f"{result.text}"
    )