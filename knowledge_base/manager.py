from pathlib import Path
from uuid import uuid4
from datetime import datetime, UTC

from knowledge_base.registry import (
    KnowledgeRegistry,
    DocumentRegistryEntry,
)

from storage.faiss_storage import FAISSStorage


class KnowledgeBaseManager:

    def __init__(self):

        self.registry = KnowledgeRegistry()

        self.storage = FAISSStorage()

    # -----------------------------------------

    def register_document(
        self,
        document,
        chunk_count,
        category="general",
    ):

        document_id = getattr(
            document,
            "document_id",
            str(uuid4()),
        )

        filename = getattr(document, "filename", None)
        source = getattr(document, "source", None)

        if filename is None:
            filename = Path(document).name

        if source is None:
            source = str(document)

        entry = DocumentRegistryEntry(
            document_id=document_id,
            filename=filename,
            source=source,
            category=category,
            indexed_at=datetime.now(UTC).isoformat(),
            chunks=chunk_count,
        )

        self.registry.add(entry)

        return document_id

    # -----------------------------------------

    def save_registry(self, path):

        data = [
            entry.model_dump()
            for entry in self.registry.all()
        ]

        self.storage.save_json(data, path)

    def load_registry(self, path):

        data = self.storage.load_json(path)

        self.registry = KnowledgeRegistry()

        for item in data:

            self.registry.add(
                DocumentRegistryEntry(**item)
            )

    # -----------------------------------------

    def list_documents(self):

        return self.registry.all()