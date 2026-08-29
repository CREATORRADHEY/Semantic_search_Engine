from pathlib import Path
import json

import faiss
import numpy as np


class FAISSStorage:
    """
    Production storage layer for FAISS indexes + JSON metadata.

    Responsibilities
    ----------------
    1. Persist FAISS vector index.
    2. Load FAISS vector index.
    3. Save arbitrary JSON files.
    4. Load arbitrary JSON files.
    """

    def __init__(
        self,
        index_path="storage/faiss_index.bin",
        metadata_path="storage/faiss_metadata.json",
        dimension=384,
    ):
        self.index_path = Path(index_path)
        self.metadata_path = Path(metadata_path)
        self.dimension = dimension

        self.index_path.parent.mkdir(parents=True, exist_ok=True)
        self.metadata_path.parent.mkdir(parents=True, exist_ok=True)

    # ==========================================================
    # FAISS INDEX STORAGE
    # ==========================================================

    def save(self, index: faiss.Index, metadata: list):
        """Persist FAISS index and metadata."""
        faiss.write_index(index, str(self.index_path))

        with open(self.metadata_path, "w") as file:
            json.dump(metadata, file, indent=2)

    def load(self):
        """Load FAISS index and metadata."""

        if not self.index_path.exists():
            index = faiss.IndexFlatIP(self.dimension)
            return index, []

        index = faiss.read_index(str(self.index_path))

        if self.metadata_path.exists():
            metadata = json.loads(self.metadata_path.read_text())
        else:
            metadata = []

        return index, metadata

    # ==========================================================
    # JSON STORAGE HELPERS
    # ==========================================================

    def save_json(self, data, path):
        """
        Save any Python object as JSON.
        Used by KnowledgeBaseManager registry.
        """
        path = Path(path)
        path.parent.mkdir(parents=True, exist_ok=True)

        with open(path, "w") as file:
            json.dump(data, file, indent=2)

    def load_json(self, path):
        """
        Load JSON file.
        Returns [] if file doesn't exist.
        """
        path = Path(path)

        if not path.exists():
            return []

        with open(path) as file:
            return json.load(file)

    # ==========================================================
    # OPTIONAL VECTOR HELPERS
    # ==========================================================

    @staticmethod
    def normalize(vectors: np.ndarray):
        """Normalize embeddings for cosine similarity."""
        faiss.normalize_L2(vectors)
        return vectors