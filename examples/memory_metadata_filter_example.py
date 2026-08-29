from memory.memory_manager import MemoryManager
from memory.memory_retriever import MemoryRetriever

manager = MemoryManager()
manager.clear()

manager.add_memory(
    "Explain FAISS",
    "Vector search library.",
    metadata={"topic": "RAG"}
)

manager.add_memory(
    "Explain Docker",
    "Containers.",
    metadata={"topic": "DevOps"}
)

manager.save()

retriever = MemoryRetriever(manager)

results = retriever.retrieve(
    "Explain technology",
    metadata_filter={
        "topic": "RAG"
    }
)

print("=" * 60)
print("Metadata Filter Example")
print("=" * 60)

for score, memory in results:
    print(memory.user_message)
    print(memory.metadata)