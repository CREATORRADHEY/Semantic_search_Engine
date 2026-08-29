from context.context_fusion import ContextFusionEngine

from memory.memory_record import MemoryRecord
from models.search_result import SearchResult


def test_context_fusion():

    engine = ContextFusionEngine()

    memories = [
        (
            0.9,
            MemoryRecord(
                user_message="Explain FAISS",
                assistant_message="Vector similarity library.",
                embedding=[],
                metadata={"topic": "RAG"}
            )
        )
    ]

    documents = [
        SearchResult(
            score=0.9,
            text="FAISS supports IndexFlatIP.",
            document_id="faiss.pdf",
            chunk_id="chunk_001",
            metadata={"source": "faiss.pdf"}
        )
    ]

    context = engine.build(
        memories=memories,
        documents=documents
    )

    assert "Conversation Memory" in context
    assert "Knowledge Context" in context
    assert "Explain FAISS" in context
    assert "faiss.pdf" in context