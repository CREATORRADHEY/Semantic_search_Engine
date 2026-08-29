from models.document import Document

from knowledge_base.manager import (
    KnowledgeBaseManager
)


manager = KnowledgeBaseManager()

manager.load_registry(
    "data/knowledge_base/registry.json"
)
new_document = Document(
    filename="fastapi.pdf",
    source="pdf",
    text="FastAPI Production Guide"
)

manager.register_document(
    new_document,
    chunk_count=35,
    category="Backend"
)

manager.save_registry(
    "data/knowledge_base/registry.json"
)

print("=" * 60)
print("Knowledge Base Updated")
print("=" * 60)

for document in manager.list_documents():

    print(document.filename)