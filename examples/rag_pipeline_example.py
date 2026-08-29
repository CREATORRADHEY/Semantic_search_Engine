from app.rag_engine import RAGEngine

from llm.mock_llm import MockLLM

from retrieval.multi_query_hybrid import (
    MultiQueryHybridRetriever
)

# Reuse your retriever from previous chapters.
# Build BM25 + FAISS + Reranker exactly as before.

retriever = ...  # Existing pipeline

llm = MockLLM()

engine = RAGEngine(
    retriever=retriever,
    llm=llm
)

response = engine.ask(
    "Explain Python classes."
)

print("=" * 60)
print("RAG Engine Response")
print("=" * 60)
print(response)