from models.document import Document
from knowledge_base.manager import KnowledgeBaseManager


def test_registry():

    manager = KnowledgeBaseManager()

    document = Document(
        document_id="1",
        filename="python.pdf",
        source="pdf",
        text="Python"
    )

    manager.register_document(
        document,
        chunk_count=10
    )

    assert len(manager.list_documents()) == 1