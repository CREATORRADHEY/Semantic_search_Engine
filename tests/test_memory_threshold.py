from memory.memory_manager import MemoryManager
from memory.memory_retriever import MemoryRetriever


def test_threshold_filter():

    manager = MemoryManager()
    manager.clear()

    manager.add_memory(
        "Explain FAISS",
        "Vector search."
    )

    retriever = MemoryRetriever(manager)

    results = retriever.retrieve(
        "football player",
        similarity_threshold=0.99
    )

    assert len(results) == 0