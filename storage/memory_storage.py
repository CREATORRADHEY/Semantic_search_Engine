from pathlib import Path
import json

import faiss

from memory.memory_record import MemoryRecord
from memory.memory_vector_store import MemoryVectorStore


class MemoryStorage:
    """
    Save and load conversation memories from disk.
    """

    def __init__(self, storage_path: str = "data/memory"):

        self.storage_path = Path(storage_path)

        self.storage_path.mkdir(
            parents=True,
            exist_ok=True
        )

        self.json_path = self.storage_path / "memory.json"
        self.index_path = self.storage_path / "memory.index"

    def save(
        self,
        vector_store: MemoryVectorStore
    ):

        records = [
            record.model_dump()
            for record in vector_store.records
        ]

        with open(self.json_path, "w") as file:
            json.dump(records, file, indent=2)

        if vector_store.index is not None:
            faiss.write_index(
                vector_store.index,
                str(self.index_path)
            )

    def load(self) -> MemoryVectorStore:

        vector_store = MemoryVectorStore()

        if not self.json_path.exists():
            return vector_store

        with open(self.json_path, "r") as file:
            records = json.load(file)

        vector_store.records = [
            MemoryRecord(**record)
            for record in records
        ]

        if self.index_path.exists():
            vector_store.index = faiss.read_index(
                str(self.index_path)
            )

        return vector_store