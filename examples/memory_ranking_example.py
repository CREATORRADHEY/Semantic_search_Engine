from datetime import datetime, timedelta

from memory.memory_manager import MemoryManager
from memory.memory_record import MemoryRecord
from memory.memory_retriever import MemoryRetriever

manager = MemoryManager()
manager.clear()

store = manager.vector_store

store.add(
    MemoryRecord(
        user_message="Explain FAISS",
        assistant_message="Vector similarity library.",
        embedding=manager.embedder.embed(["Explain FAISS"])[0],
        created_at=(datetime.now() - timedelta(days=6)).isoformat(),
        metadata={"topic": "RAG"}
    )
)

store.add(
    MemoryRecord(
        user_message="Explain FAISS indexing",
        assistant_message="IndexFlatIP indexes vectors.",
        embedding=manager.embedder.embed(["Explain FAISS indexing"])[0],
        created_at=datetime.now().isoformat(),
        metadata={"topic": "RAG"}
    )
)

store.add(
    MemoryRecord(
        user_message="Explain Docker",
        assistant_message="Containers.",
        embedding=manager.embedder.embed(["Explain Docker"])[0],
        metadata={"topic": "DevOps"}
    )
)

retriever = MemoryRetriever(manager)

results = retriever.retrieve(
    "vector search library",
    top_k=3
)

print("=" * 60)
print("Memory Ranking Example")
print("=" * 60)

for score, memory in results:
    print(f"{score:.4f}")
    print(memory.user_message)
    print(memory.created_at)
    print()