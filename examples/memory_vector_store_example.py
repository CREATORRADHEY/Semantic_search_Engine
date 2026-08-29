from embeddings.sentence_transformer_embedder import (
    SentenceTransformerEmbedder
)

from memory.memory_record import MemoryRecord
from memory.memory_vector_store import MemoryVectorStore


embedder = SentenceTransformerEmbedder()

store = MemoryVectorStore()

conversations = [
    (
        "Explain FAISS",
        "FAISS is a library for efficient vector similarity search."
    ),
    (
        "Explain Docker",
        "Docker packages applications into containers."
    ),
    (
        "Explain Kubernetes",
        "Kubernetes orchestrates containers across clusters."
    ),
    (
        "Explain semantic search",
        "Semantic search retrieves information using embeddings."
    )
]

texts = [
    user
    for user, _ in conversations
]

embeddings = embedder.embed(texts)

for i, (user, assistant) in enumerate(conversations):

    memory = MemoryRecord(
        user_message=user,
        assistant_message=assistant,
        embedding=embeddings[i],
        metadata={"topic": "AI Engineering"}
    )

    store.add(memory)


query = "How does FAISS search vectors?"

query_embedding = embedder.embed([query])[0]

results = store.search(query_embedding, top_k=3)

print("=" * 60)
print("Memory Search Results")
print("=" * 60)

for score, memory in results:
    print(f"{score:.4f}")
    print("User      :", memory.user_message)
    print("Assistant :", memory.assistant_message)
    print()