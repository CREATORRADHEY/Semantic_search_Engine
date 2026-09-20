from app.rag_engine import RAGEngine

from llm.mock_llm import MockLLM

from context.context_builder import ContextBuilder
from context.prompt_builder import PromptBuilder
from context.token_budget import TokenBudgetManager

from memory.conversation_memory import ConversationMemory
from memory.memory_manager import MemoryManager

from knowledge_base.manager import KnowledgeBaseManager

from retrieval.query_expansion import QueryExpander
from embeddings.sentence_transformer_embedder import (
    SentenceTransformerEmbedder,
)


class EmptyRetriever:

    def search(self, query, top_k=5):
        return []


embedder = SentenceTransformerEmbedder()

query_expander = QueryExpander(
    expansions={
        "semantic search": [
            "semantic retrieval",
            "vector search",
        ],
        "AI": [
            "artificial intelligence",
            "machine intelligence",
        ],
    }
)

rag_engine = RAGEngine(
    retriever=EmptyRetriever(),
    llm=MockLLM(),
    context_builder=ContextBuilder(),
    prompt_builder=PromptBuilder(),
    token_budget=TokenBudgetManager(),
    memory=ConversationMemory(),
    memory_manager=MemoryManager(),
    knowledge_manager=KnowledgeBaseManager(),
)


def get_rag_engine():
    return rag_engine