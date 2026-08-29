from context.context_fusion import ContextFusionEngine

from memory.memory_record import MemoryRecord
from models.search_result import SearchResult

fusion = ContextFusionEngine()

memories = [
    (
        0.90,
        MemoryRecord(
            user_message="Explain FAISS",
            assistant_message="FAISS is a similarity search library.",
            embedding=[],
            metadata={"topic": "RAG"}
        )
    )
]

documents = [
    SearchResult(
        score=0.95,
        text="FAISS provides IndexFlatIP for exact cosine similarity search.",
        document_id="faiss.pdf",
        chunk_id="faiss_chunk_1",
        metadata={"source": "faiss.pdf"}
    ),
    SearchResult(
        score=0.82,
        text="Vector search is a core component of Retrieval-Augmented Generation.",
        document_id="rag.pdf",
        chunk_id="rag_chunk_1",
        metadata={"source": "rag.pdf"}
    )
]

context = fusion.build(
    memories=memories,
    documents=documents
)

print("=" * 60)
print("Context Fusion Output")
print("=" * 60)
print(context)