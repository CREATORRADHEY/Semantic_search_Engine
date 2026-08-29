from pydantic import BaseModel


class DocumentRegistryEntry(BaseModel):
    document_id: str
    filename: str
    source: str
    category: str
    indexed_at: str
    chunks: int


class KnowledgeRegistry:
    """
    In-memory registry of all indexed documents.
    Key = document_id
    Value = DocumentRegistryEntry
    """

    def __init__(self):
        self.documents: dict[str, DocumentRegistryEntry] = {}

    def add(self, entry: DocumentRegistryEntry):
        self.documents[entry.document_id] = entry

    def remove(self, document_id: str):
        self.documents.pop(document_id, None)

    def get(self, document_id: str):
        return self.documents.get(document_id)

    def all(self):
        return list(self.documents.values())

    def clear(self):
        self.documents = {}

    def __len__(self):
        return len(self.documents)