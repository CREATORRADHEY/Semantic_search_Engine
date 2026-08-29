from compression.extractive_compressor import (
    ExtractiveCompressor
)


def test_extractive_compressor():

    compressor = ExtractiveCompressor()

    text = (
        "FAISS performs vector similarity search. "
        "Docker packages containers. "
        "FastAPI builds APIs."
    )

    compressed = compressor.compress(
        query="vector similarity",
        text=text,
        max_sentences=1
    )

    assert "FAISS" in compressed
    assert "Docker" not in compressed