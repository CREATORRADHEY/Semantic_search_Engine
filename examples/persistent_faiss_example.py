import numpy as np
import faiss

from storage.faiss_storage import FAISSStorage


storage = FAISSStorage()

index = faiss.IndexFlatIP(384)

vectors = np.random.rand(3, 384).astype("float32")

index.add(vectors)

metadata = [
    {"filename": "rag.pdf"},
    {"filename": "python.pdf"},
    {"filename": "faiss.pdf"},
]

storage.save(index, metadata)

loaded_index, loaded_metadata = storage.load()

print("=" * 60)
print("Persistent FAISS")
print("=" * 60)

print("Vectors:", loaded_index.ntotal)
print("Metadata:", loaded_metadata)