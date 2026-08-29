from memory.memory_record import MemoryRecord


def test_memory_record():

    memory = MemoryRecord(
        user_message="What is FAISS?",
        assistant_message="FAISS is a similarity search library.",
        embedding=[0.1, 0.2, 0.3]
    )

    assert memory.user_message == "What is FAISS?"

    assert memory.assistant_message.startswith("FAISS")

    assert len(memory.embedding) == 3

    assert memory.memory_id is not None

    assert memory.created_at is not None