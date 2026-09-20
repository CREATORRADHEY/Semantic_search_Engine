import json
from pathlib import Path

import faiss


class FAISSStorage:
    """
    Persistent FAISS storage layer.
    """

    def __init__(
        self,
        index_path="storage/faiss.index",
        metadata_path="storage/faiss_metadata.json",
    ):
        self.index_path = Path(index_path)
        self.metadata_path = Path(metadata_path)

    # -----------------------------
    # Persistent FAISS
    # -----------------------------

    def save(self, index, metadata):
        self.index_path.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        faiss.write_index(
            index,
            str(self.index_path),
        )

        with open(self.metadata_path, "w") as file:
            json.dump(metadata, file, indent=2)

    def load(self):
        if not self.index_path.exists():
            return None, []

        index = faiss.read_index(
            str(self.index_path)
        )

        metadata = []

        if self.metadata_path.exists():
            with open(self.metadata_path) as file:
                metadata = json.load(file)

        return index, metadata

    # -----------------------------
    # JSON Registry Helpers
    # -----------------------------

    def save_json(self, data, path):
        path = Path(path)

        path.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        with open(path, "w") as file:
            json.dump(data, file, indent=2)

    def load_json(self, path):
        path = Path(path)

        if not path.exists():
            return []

        with open(path) as file:
            return json.load(file)