import time

from embeddings.sentence_transformer_embedder import (
    SentenceTransformerEmbedder
)

from models.chunk import Chunk
from models.vector_record import VectorRecord

from vector_store.memory_vector_store import (
    MemoryVectorStore
)

from vector_store.faiss_vector_store import (
    FAISSVectorStore
)


def build_records(
    embedder,
    count: int
):

    texts = [
        "Artificial Intelligence and Machine Learning"
    ] * count

    embeddings = embedder.embed(texts)

    records = []

    for index, embedding in enumerate(embeddings):

        chunk = Chunk(
            document_id="benchmark",
            text=texts[index],
            chunk_index=index
        )

        record = VectorRecord(
            chunk=chunk,
            embedding=embedding
        )

        records.append(record)

    return records


def benchmark_store(
    store,
    records,
    query_embedding,
    top_k=5
):

    start = time.perf_counter()

    for record in records:

        store.add(record)

    indexing_time = time.perf_counter() - start

    start = time.perf_counter()

    results = store.search(
        query_embedding,
        top_k=top_k
    )

    search_time = time.perf_counter() - start

    return (
        indexing_time,
        search_time,
        results
    )


def main():

    embedder = SentenceTransformerEmbedder()

    vector_count = 1000

    print("=" * 60)

    print(
        f"Building {vector_count} benchmark vectors..."
    )

    records = build_records(
        embedder,
        vector_count
    )

    query_embedding = embedder.embed(
        ["Artificial Intelligence"]
    )[0]

    print("=" * 60)

    # Memory Store

    memory_store = MemoryVectorStore()

    memory_index_time, memory_search_time, _ = (
        benchmark_store(
            memory_store,
            records,
            query_embedding
        )
    )

    # FAISS Store

    faiss_store = FAISSVectorStore()

    faiss_index_time, faiss_search_time, _ = (
        benchmark_store(
            faiss_store,
            records,
            query_embedding
        )
    )

    print()
    print("=" * 60)
    print("Vector Store Benchmark")
    print("=" * 60)

    print(
        f"Memory Indexing : "
        f"{memory_index_time:.6f} sec"
    )

    print(
        f"FAISS Indexing  : "
        f"{faiss_index_time:.6f} sec"
    )

    print()

    print(
        f"Memory Search   : "
        f"{memory_search_time:.6f} sec"
    )

    print(
        f"FAISS Search    : "
        f"{faiss_search_time:.6f} sec"
    )

    print("=" * 60)


if __name__ == "__main__":

    main()