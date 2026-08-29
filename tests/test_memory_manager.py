from memory.memory_manager import MemoryManager


def test_memory_manager():

    manager = MemoryManager()

    manager.clear()

    manager.add_memory(
        "Explain FAISS.",
        "Vector similarity search library."
    )

    manager.save()

    loaded = MemoryManager()

    memories = loaded.list_memories()

    assert len(memories) == 1

    assert memories[0].user_message == "Explain FAISS."