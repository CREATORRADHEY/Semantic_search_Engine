from embeddings.sentence_transformer_embedder import (
    SentenceTransformerEmbedder
)

from memory.memory_record import MemoryRecord
from memory.memory_vector_store import MemoryVectorStore

from storage.memory_storage import MemoryStorage


class MemoryManager:
    """
    High-level manager for persistent conversation memory.
    """

    def __init__(self):

        self.embedder = SentenceTransformerEmbedder()

        self.storage = MemoryStorage()

        self.vector_store = self.storage.load()

    def add_memory(
        self,
        user_message: str,
        assistant_message: str,
        metadata: dict | None = None
    ):

        embedding = self.embedder.embed(
            [user_message]
        )[0]

        record = MemoryRecord(
            user_message=user_message,
            assistant_message=assistant_message,
            embedding=embedding,
            metadata=metadata or {}
        )

        self.vector_store.add(record)

        return record

    def search(
        self,
        query: str,
        top_k: int = 3
    ):

        query_embedding = self.embedder.embed(
            [query]
        )[0]

        return self.vector_store.search(
            query_embedding,
            top_k=top_k
        )

    def list_memories(self):

        return self.vector_store.records

    def save(self):

        self.storage.save(
            self.vector_store
        )

    def clear(self):

        self.vector_store = MemoryVectorStore()

        self.storage.save(
            self.vector_store
        )

    def get_all_memories(self):
     return self.vector_store.records  
    