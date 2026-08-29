from embeddings.sentence_transformer_embedder import (
    SentenceTransformerEmbedder
)


embedder = SentenceTransformerEmbedder()

texts = [
    "Artificial Intelligence",
    "Machine Learning",
    "Cats are animals."
]

vectors = embedder.embed(texts)

print("=" * 60)

print(f"Total Embeddings: {len(vectors)}")

print("=" * 60)

for i, vector in enumerate(vectors):

    print(f"\nEmbedding {i}")

    print(f"Dimension: {len(vector)}")

    print(vector[:10])

    