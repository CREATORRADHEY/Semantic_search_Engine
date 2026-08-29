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
    base_embedding,
    count: int
):

    records = []

    for index in range(count):

        chunk = Chunk(
            document_id="benchmark",
            text=f"Benchmark document {index}",
            chunk_index=index
        )

        record = VectorRecord(
            chunk=chunk,
            embedding=base_embedding
        )

        records.append(record)

    return records


def measure_search(
    store,
    query_embedding,
    iterations: int = 10
):

    # Warm-up search
    store.search(
        query_embedding,
        top_k=5
    )

    start = time.perf_counter()

    for _ in range(iterations):

        store.search(
            query_embedding,
            top_k=5
        )

    elapsed = time.perf_counter() - start

    average_latency = elapsed / iterations

    return average_latency


def benchmark(
    vector_count,
    embedding
):

    records = build_records(
        embedding,
        vector_count
    )

    # -----------------------------------------
    # Memory Vector Store
    # -----------------------------------------

    memory_store = MemoryVectorStore()

    for record in records:

        memory_store.add(record)

    memory_latency = measure_search(
        memory_store,
        embedding
    )

    # -----------------------------------------
    # FAISS Vector Store
    # -----------------------------------------

    faiss_store = FAISSVectorStore()

    faiss_store.add_batch(
        records
    )

    faiss_latency = measure_search(
        faiss_store,
        embedding
    )

    # -----------------------------------------
    # Calculate Speedup
    # -----------------------------------------

    speedup = (
        memory_latency / faiss_latency
    )

    return (
        memory_latency,
        faiss_latency,
        speedup
    )


def main():

    embedder = SentenceTransformerEmbedder()

    # Generate ONE embedding.
    # We intentionally reuse it so that
    # embedding generation does not affect
    # our benchmark.

    embedding = embedder.embed(
        [
            "Artificial Intelligence"
        ]
    )[0]

    dataset_sizes = [
        1_000,
        2_000,
        5_000
    ]

    print("=" * 70)

    print(
        "Vector Store Scaling Benchmark"
    )

    print("=" * 70)

    print()

    print(
        f"{'Vectors':>10}"
        f"{'Memory (ms)':>18}"
        f"{'FAISS (ms)':>18}"
        f"{'Speedup':>15}"
    )

    print("-" * 70)

    for vector_count in dataset_sizes:

        print(
            f"Testing {vector_count:,} vectors..."
        )

        (
            memory_latency,
            faiss_latency,
            speedup
        ) = benchmark(
            vector_count,
            embedding
        )

        print(
            f"{vector_count:>10,}"
            f"{memory_latency * 1000:>18.3f}"
            f"{faiss_latency * 1000:>18.3f}"
            f"{speedup:>14.2f}x"
        )

        print()


if __name__ == "__main__":

    main()