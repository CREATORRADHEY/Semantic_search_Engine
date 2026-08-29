from memory.memory_manager import MemoryManager

from context.compression_pipeline import (
    CompressionPipeline
)


def test_compression_pipeline():

    manager = MemoryManager()

    manager.clear()

    manager.add_memory(
        "Explain FAISS",
        "Vector similarity search."
    )

    pipeline = CompressionPipeline()

    output = pipeline.compress(
        query="vector similarity",
        memory_records=manager.get_all_memories(),
        knowledge_context=(
            "FAISS performs vector similarity search."
        )
    )

    assert "FAISS" in output