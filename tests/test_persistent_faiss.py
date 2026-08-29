import numpy as np
import faiss

from storage.faiss_storage import FAISSStorage


def test_persistent_faiss(tmp_path):

    storage = FAISSStorage(
        index_path=tmp_path / "index.bin",
        metadata_path=tmp_path / "metadata.json"
    )

    index = faiss.IndexFlatIP(384)

    vectors = np.random.rand(2, 384).astype("float32")

    index.add(vectors)

    metadata = [{"filename": "rag.pdf"}]

    storage.save(index, metadata)

    loaded_index, loaded_metadata = storage.load()

    assert loaded_index.ntotal == 2
    assert loaded_metadata[0]["filename"] == "rag.pdf"