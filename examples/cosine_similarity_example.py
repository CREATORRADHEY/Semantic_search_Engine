from embeddings.sentence_transformer_embedder import (
    SentenceTransformerEmbedder
)

from similarity.cosine_similarity import (
    CosineSimilarity
)

embedder = SentenceTransformerEmbedder()

texts = [
    "Artificial Intelligence",   # 0
    "Machine Learning",          # 1
    "Deep Learning",             # 2
    "Neural Networks",           # 3
    "Football",                  # 4
    "Pizza",                     # 5
    "Cats",                      # 6
    "Dogs"                       # 7
]

vectors = embedder.embed(texts)

print("=" * 60)
print("Semantic Similarity Scores")
print("=" * 60)

pairs = [
    ("AI ↔ Machine Learning", 0, 1),
    ("AI ↔ Deep Learning", 0, 2),
    ("AI ↔ Neural Networks", 0, 3),
    ("AI ↔ Football", 0, 4),
    ("AI ↔ Pizza", 0, 5),
    ("Cats ↔ Dogs", 6, 7),
    ("Football ↔ Pizza", 4, 5),
]

for name, i, j in pairs:
    score = CosineSimilarity.calculate(vectors[i], vectors[j])
    print(f"{name:<30}: {score:.4f}")


