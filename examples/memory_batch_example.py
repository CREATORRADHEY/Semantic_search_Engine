from embeddings.sentence_transformer_embedder import (
    SentenceTransformerEmbedder
)

from memory.memory_record import MemoryRecord
from memory.memory_vector_store import MemoryVectorStore


embedder = SentenceTransformerEmbedder()

store = MemoryVectorStore()

questions = [
    "Explain FAISS",
    "Explain Docker",
    "Explain Kubernetes",
    "Explain RAG",
    "Explain Embeddings"
]

answers = [
    "Vector similarity search library.",
    "Container platform.",
    "Container orchestration system.",
    "Retrieval-Augmented Generation.",
    "Embeddings convert text into vectors."
]

embeddings = embedder.embed(questions)

records = []

for i in range(len(questions)):
    records.append(
        MemoryRecord(
            user_message=questions[i],
            assistant_message=answers[i],
            embedding=embeddings[i]
        )
    )

store.add_batch(records)

print("=" * 60)
print("Batch Memory Index")
print("=" * 60)

print("Total Memories:", store.count())