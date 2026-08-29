from knowledge_base.incremental_indexer import IncrementalIndexer


def test_incremental_indexer(tmp_path):

    folder = tmp_path / "knowledge"
    folder.mkdir()

    pdf = folder / "rag.pdf"

    pdf.write_text("RAG PDF")

    indexer = IncrementalIndexer(
        registry_path=tmp_path / "hashes.json"
    )

    result = indexer.index(folder)

    assert len(result["indexed"]) == 1

    result = indexer.index(folder)

    assert len(result["indexed"]) == 0
    assert len(result["skipped"]) == 1