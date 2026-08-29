from memory.memory_manager import MemoryManager


manager = MemoryManager()

manager.clear()

manager.add_memory(
    "Explain FAISS.",
    "FAISS performs efficient vector similarity search.",
    metadata={"topic": "RAG"}
)

manager.add_memory(
    "Explain Docker.",
    "Docker packages applications into containers.",
    metadata={"topic": "DevOps"}
)

manager.save()

print("=" * 60)
print("Stored Memories")
print("=" * 60)

for memory in manager.list_memories():

    print(memory.user_message)
    print(memory.metadata)
    print()