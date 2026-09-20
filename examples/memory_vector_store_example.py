from memory.memory_manager import MemoryManager

manager = MemoryManager()

manager.clear()

manager.add_memory(
    "Explain semantic search",
    "Semantic search retrieves information using embeddings.",
)

manager.add_memory(
    "Explain FAISS",
    "FAISS is a library for efficient vector similarity search.",
)

manager.add_memory(
    "Explain Kubernetes",
    "Kubernetes orchestrates containers across clusters.",
)

results = manager.search(
    "vector search",
    top_k=3,
)

print("=" * 60)
print("Memory Search Results")
print("=" * 60)

for score, memory in results:

    print(f"{score:.4f}")
    print("User      :", memory.user_message)
    print("Assistant :", memory.assistant_message)
    print()