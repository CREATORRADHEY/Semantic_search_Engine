from context.adaptive_compressor import AdaptiveCompressor

text = """
Python supports object-oriented programming using classes and objects.
FastAPI builds REST APIs quickly.
FAISS performs vector similarity search.
Docker packages applications into containers.
Kubernetes orchestrates distributed containers.
Retrieval-Augmented Generation combines search with LLMs.
"""

query = "Explain FAISS and semantic search."

compressor = AdaptiveCompressor()

compressed = compressor.compress(
    query=query,
    text=text,
    max_tokens=18
)

print("=" * 60)
print("Adaptive Compression")
print("=" * 60)
print(compressed)