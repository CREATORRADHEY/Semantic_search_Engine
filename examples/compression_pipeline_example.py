from memory.memory_manager import MemoryManager

from context.compression_pipeline import (
    CompressionPipeline
)

manager = MemoryManager()

manager.clear()

manager.add_memory(
    "Explain FAISS",
    "FAISS performs vector search."
)

manager.add_memory(
    "Explain Docker",
    "Docker packages applications."
)

knowledge = """
FAISS performs vector similarity search.
FastAPI builds APIs.
Docker packages applications.
Kubernetes orchestrates containers.
"""

pipeline = CompressionPipeline()

output = pipeline.compress(
    query="vector similarity",
    memory_records=manager.get_all_memories(),
    knowledge_context=knowledge,
    memory_budget=50,
    knowledge_budget=20
)

print("=" * 60)
print("Compression Pipeline")
print("=" * 60)
print(output)