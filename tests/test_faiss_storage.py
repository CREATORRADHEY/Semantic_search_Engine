from storage.faiss_storage import FAISSStorage


def test_json_storage(tmp_path):

    storage = FAISSStorage()

    path = tmp_path / "test.json"

    storage.save_json(
        {"hello": "world"},
        path
    )

    data = storage.load_json(path)

    assert data["hello"] == "world"