from compression.extractive_compressor import (
    ExtractiveCompressor
)

text = """
Python supports object-oriented programming using classes and objects.
FastAPI builds REST APIs quickly.
FAISS performs vector similarity search.
Docker packages applications into containers.
"""

query = "Explain FAISS similarity search."

compressor = ExtractiveCompressor()

compressed = compressor.compress(
    query,
    text,
    max_sentences=2
)

print("=" * 60)
print("Compressed Context")
print("=" * 60)
print(compressed)