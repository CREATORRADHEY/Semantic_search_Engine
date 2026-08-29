from knowledge_base.collection_manager import (
    CollectionManager
)


def test_collection_manager(tmp_path):

    manager = CollectionManager(
        registry_path=tmp_path / "collections.json"
    )

    manager.create_collection(
        "AI"
    )

    assert manager.exists("AI")

    assert len(manager.list_collections()) == 1