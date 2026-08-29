from memory.memory_manager import MemoryManager
from memory.memory_retriever import MemoryRetriever


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

manager.save()

retriever = MemoryRetriever(manager)

results = retriever.retrieve(
    "vector search library",
    top_k=2
)

print("=" * 60)
print("Memory Retriever Example")
print("=" * 60)

for score, memory in results:

    print(f"Score : {score:.4f}")
    print(memory.user_message)
    print(memory.assistant_message)
    print()