from memory.memory_record import MemoryRecord
from memory.memory_vector_store import MemoryVectorStore


def test_memory_vector_store():

    store = MemoryVectorStore()

    memory = MemoryRecord(
        user_message="Explain FAISS",
        assistant_message="FAISS searches vectors.",
        embedding=[1.0, 0.0, 0.0]
    )

    store.add(memory)

    results = store.search(
        [1.0, 0.0, 0.0],
        top_k=1
    )

    assert len(results) == 1

    score, retrieved = results[0]

    assert retrieved.user_message == "Explain FAISS"

    assert score > 0.99

    assert store.count() == 1