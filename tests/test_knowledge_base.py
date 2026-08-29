from models.document import Document

from knowledge_base.manager import (
    KnowledgeBaseManager
)


def test_save_and_load(tmp_path):

    manager = KnowledgeBaseManager()

    document = Document(
        document_id="1",
        filename="python.pdf",
        source="pdf",
        text="Python"
    )

    manager.register_document(
        document,
        chunk_count=12
    )

    path = tmp_path / "registry.json"

    manager.save_registry(path)

    new_manager = KnowledgeBaseManager()

    new_manager.load_registry(path)

    assert len(new_manager.list_documents()) == 1