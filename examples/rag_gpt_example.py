from app.rag_engine import RAGEngine

from llm.openai_llm import OpenAILLM

# Import YOUR production retriever.
from retrieval.multi_query_hybrid import (
    MultiQueryHybridRetriever
)

retriever = ...  # Existing retriever from previous chapters.

engine = RAGEngine(
    retriever=retriever,
    llm=OpenAILLM()
)

answer = engine.ask(
    "Explain recursion in Python."
)

print("=" * 60)
print("GPT RAG Answer")
print("=" * 60)
print(answer)