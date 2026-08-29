from memory.memory_manager import MemoryManager
from context.memory_compressor import MemoryCompressor

manager = MemoryManager()

manager.clear()

manager.add_memory(
    "Explain FAISS.",
    "FAISS performs vector similarity search."
)

manager.add_memory(
    "Explain Docker.",
    "Docker packages applications into containers."
)

manager.add_memory(
    "Explain Kubernetes.",
    "Kubernetes orchestrates containers."
)

compressor = MemoryCompressor()

history = compressor.compress(
    manager.get_all_memories(),
    max_tokens=18
)

print("=" * 60)
print("Compressed Memory")
print("=" * 60)
print(history)