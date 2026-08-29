from memory.memory_manager import MemoryManager
from memory.memory_retriever import MemoryRetriever


def test_memory_retriever():

    manager = MemoryManager()

    manager.clear()

    manager.add_memory(
        "Explain FAISS.",
        "Vector similarity search."
    )

    retriever = MemoryRetriever(manager)
    results = retriever.retrieve(
    "vector similarity",
    top_k=1,
    similarity_threshold=None
)
    assert len(results) == 1

    score, memory = results[0]

    assert memory.user_message == "Explain FAISS."

    assert score > 0