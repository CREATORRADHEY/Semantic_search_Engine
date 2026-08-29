from compression.sentence_scorer import SentenceScorer

text = """
Python supports object-oriented programming using classes and objects.
FastAPI builds REST APIs quickly.
FAISS performs vector similarity search.
Docker packages applications into containers.
"""

query = "How does FAISS perform similarity search?"

scorer = SentenceScorer()

results = scorer.score(query, text)

print("=" * 60)
print("Sentence Similarity Ranking")
print("=" * 60)

for score, sentence in results:

    print(f"{score:.4f} | {sentence}")