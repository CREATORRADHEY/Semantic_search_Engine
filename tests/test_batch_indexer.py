from pathlib import Path

from knowledge_base.collection_manager import (
    CollectionManager
)

from knowledge_base.manager import KnowledgeBaseManager

from knowledge_base.batch_indexer import (
    PDFBatchIndexer
)


def test_batch_indexer(tmp_path):

    knowledge_dir = tmp_path / "AI"

    knowledge_dir.mkdir()

    (knowledge_dir / "rag.pdf").touch()

    (knowledge_dir / "agents.pdf").touch()

    collections = CollectionManager(
        registry_path=tmp_path / "collections.json"
    )

    collections.create_collection("AI")

    manager = KnowledgeBaseManager()

    indexer = PDFBatchIndexer(
        collections,
        manager
    )

    indexed = indexer.index_folder(
        folder_path=knowledge_dir,
        namespace="AI"
    )

    assert len(indexed) == 2