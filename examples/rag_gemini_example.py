from app.rag_engine import RAGEngine

from llm.gemini_llm import GeminiLLM

from retrieval.multi_query_hybrid import (
    MultiQueryHybridRetriever
)

retriever = ...  # Existing retriever.

engine = RAGEngine(
    retriever=retriever,
    llm=GeminiLLM()
)

answer = engine.ask(
    "Explain object-oriented programming."
)

print("=" * 60)
print("Gemini RAG Answer")
print("=" * 60)
print(answer)