from memory.memory_manager import MemoryManager
from context.memory_compressor import MemoryCompressor


def test_memory_compressor():

    manager = MemoryManager()

    manager.clear()

    manager.add_memory(
        "Explain FAISS.",
        "Vector similarity search."
    )

    manager.add_memory(
        "Explain Docker.",
        "Container packaging."
    )

    compressor = MemoryCompressor()

    output = compressor.compress(
        manager.get_all_memories(),
        max_tokens=8
    )

    assert "FAISS" in output