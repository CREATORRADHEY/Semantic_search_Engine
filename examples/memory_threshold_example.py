from memory.memory_manager import MemoryManager
from memory.memory_retriever import MemoryRetriever

manager = MemoryManager()
manager.clear()

manager.add_memory(
    "Explain FAISS",
    "Vector search."
)

manager.add_memory(
    "Explain Docker",
    "Containers."
)

manager.save()

retriever = MemoryRetriever(manager)

results = retriever.retrieve(
    "football player",
    similarity_threshold=0.35
)

print("=" * 60)
print("Threshold Example")
print("=" * 60)

print("Returned Memories:", len(results))