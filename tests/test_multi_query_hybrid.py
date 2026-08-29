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

from vector_store.memory_vector_store import (
    MemoryVectorStore
)


def test_multi_query_hybrid():

    texts = [
        "Car insurance protects vehicles.",
        "Vehicle insurance offers coverage.",
        "Artificial Intelligence powers search."
    ]

    chunks = []

    for index, text in enumerate(texts):

        chunks.append(
            Chunk(
                document_id="test",
                text=text,
                chunk_index=index
            )
        )

    bm25 = BM25Retriever()
    bm25.add_documents(chunks)

    embedder = SentenceTransformerEmbedder()

    embeddings = embedder.embed(texts)

    memory = MemoryVectorStore()

    for chunk, embedding in zip(chunks, embeddings):

        memory.add(
            VectorRecord(
                chunk=chunk,
                embedding=embedding
            )
        )

    expander = QueryExpander(
        expansions={
            "car": [
                "vehicle"
            ]
        }
    )

    retriever = MultiQueryHybridRetriever(
        bm25,
        memory,
        expander,
        embedder
    )

    results = retriever.search(
        "car insurance",
        top_k=3
    )

    assert len(results) > 0

    assert "insurance" in results[0].text.lower()