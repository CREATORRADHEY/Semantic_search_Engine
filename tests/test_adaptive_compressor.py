from context.adaptive_compressor import AdaptiveCompressor


def test_adaptive_compressor():

    compressor = AdaptiveCompressor()

    text = (
        "FAISS performs vector similarity search. "
        "Docker packages containers. "
        "FastAPI builds APIs."
    )

    compressed = compressor.compress(
        query="vector similarity",
        text=text,
        max_tokens=10
    )

    assert "FAISS" in compressed