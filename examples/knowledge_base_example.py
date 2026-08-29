from models.document import Document

from knowledge_base.manager import (
    KnowledgeBaseManager
)


manager = KnowledgeBaseManager()

documents = [
    Document(
        filename="python.pdf",
        source="pdf",
        text="Python Guide"
    ),
    Document(
        filename="rag.pdf",
        source="pdf",
        text="RAG Guide"
    ),
    Document(
        filename="ml.pdf",
        source="pdf",
        text="Machine Learning Guide"
    )
]

for document in documents:

    manager.register_document(
        document,
        chunk_count=20,
        category="AI"
    )

manager.save_registry(
    "data/knowledge_base/registry.json"
)

print("=" * 60)
print("Indexed Documents")
print("=" * 60)

for document in manager.list_documents():

    print(
        document.filename,
        document.category,
        document.chunks
    )