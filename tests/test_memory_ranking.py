from memory.memory_manager import MemoryManager
from memory.memory_retriever import MemoryRetriever


def test_metadata_filter():

    manager = MemoryManager()
    manager.clear()

    manager.add_memory(
        "Explain FAISS",
        "Vector search.",
        metadata={"topic": "RAG"}
    )

    manager.add_memory(
        "Explain Docker",
        "Containers.",
        metadata={"topic": "DevOps"}
    )

    retriever = MemoryRetriever(manager)

    results = retriever.retrieve(
        "technology",
        metadata_filter={"topic": "RAG"},
        similarity_threshold=-1
    )

    assert len(results) == 1

    _, memory = results[0]

    assert memory.metadata["topic"] == "RAG"