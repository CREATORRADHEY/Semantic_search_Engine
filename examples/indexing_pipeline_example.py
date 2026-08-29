from ingestion.pdf_ingestion import PDFIngestionEngine
from cleaning.text_cleaner import TextCleaningEngine
from chunking.recursive_chunker import RecursiveChunker


from embeddings.sentence_transformer_embedder import (
    SentenceTransformerEmbedder
)

from indexing.indexing_pipeline import (
    IndexingPipeline
)

from retrieval.semantic_search_engine import (
    SemanticSearchEngine
)

from vector_store.memory_vector_store import (
    MemoryVectorStore
)


embedder = SentenceTransformerEmbedder()

store = MemoryVectorStore()

ingestion = PDFIngestionEngine()

cleaner = TextCleaningEngine()

chunker = RecursiveChunker()

pipeline = IndexingPipeline(
    ingestion=ingestion,
    cleaner=cleaner,
    chunker=chunker,
    embedder=embedder,
    vector_store=store
)

pipeline.index_pdf(
    "documents/python.pdf"
)

engine = SemanticSearchEngine(
    embedder,
    store
)

results = engine.search(
    "Claude Code",
    top_k=5
)

print("=" * 60)
print("Search Results")
print("=" * 60)

for score, record in results:

    print(f"{score:.4f}")

    print(record.chunk.text[:200])
    print("-" * 60)