from embeddings.sentence_transformer_embedder import (
    SentenceTransformerEmbedder
)

from retrieval.semantic_search_engine import (
    SemanticSearchEngine
)

from vector_store.memory_vector_store import (
    MemoryVectorStore
)

from models.chunk import Chunk
from models.vector_record import VectorRecord


texts = [
    "Artificial Intelligence",
    "Machine Learning",
    "Deep Learning",
    "Football",
    "Cats are animals",
    "Python is a programming language"
]

embedder = SentenceTransformerEmbedder()

store = MemoryVectorStore()

embeddings = embedder.embed(texts)

for i, text in enumerate(texts):

    chunk = Chunk(
        document_id="demo",
        text=text,
        chunk_index=i
    )

    record = VectorRecord(
        chunk=chunk,
        embedding=embeddings[i]
    )

    store.add(record)

engine = SemanticSearchEngine(
    embedder,
    store
)

results = engine.search(
    "AI",
    top_k=3
)

print("=" * 60)
print("Semantic Search Results")
print("=" * 60)

for score, record in results:

    print(
        f"{score:.4f} -> {record.chunk.text}"
    )