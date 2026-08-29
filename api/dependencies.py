from llm.mock_llm import MockLLM

from app.rag_engine import RAGEngine

from context.context_builder import ContextBuilder
from context.prompt_builder import PromptBuilder

from memory.conversation_memory import ConversationMemory

from retrieval.query_expansion import QueryExpander
from retrieval.multi_query_hybrid import MultiQueryHybridRetriever

from embeddings.sentence_transformer_embedder import SentenceTransformerEmbedder
from memory.memory_manager import MemoryManager

memory_manager = MemoryManager()

# -----------------------------------------------------
# Shared Components
# -----------------------------------------------------

embedder = SentenceTransformerEmbedder()

query_expander = QueryExpander(
    expansions={
        "car insurance": [
            "vehicle insurance",
            "automobile insurance",
        ],
        "AI systems": [
            "artificial intelligence systems",
            "machine intelligence systems",
        ],
        "semantic search": [
            "semantic retrieval",
            "semantic information retrieval",
        ],
    }
)

context_builder = ContextBuilder()
prompt_builder = PromptBuilder()
memory = ConversationMemory()


# -----------------------------------------------------
# Temporary Retriever (Chapter 46)
# -----------------------------------------------------

retriever = MultiQueryHybridRetriever(
    bm25_retriever=None,
    faiss_retriever=None,
    query_expander=query_expander,
    embedder=embedder,
)


# -----------------------------------------------------
# Singleton RAG Engine
# -----------------------------------------------------

from memory.memory_manager import MemoryManager

memory_manager = MemoryManager()

rag_engine = RAGEngine(
    retriever=retriever,
    llm=MockLLM(),
    context_builder=context_builder,
    prompt_builder=prompt_builder,
    token_budget=None,
    memory=memory,
    memory_manager=memory_manager
)

def get_rag_engine():
    return rag_engine

