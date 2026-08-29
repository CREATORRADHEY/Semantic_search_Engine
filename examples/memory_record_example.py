from memory.memory_record import MemoryRecord

memory = MemoryRecord(
    user_message="Explain semantic search.",
    assistant_message="Semantic search retrieves information using embeddings.",
    embedding=[0.1, 0.2, 0.3],
    metadata={
        "topic": "semantic-search",
        "chapter": 47
    }
)

print("=" * 60)
print("Memory Record Example")
print("=" * 60)

print(memory.model_dump_json(indent=2))