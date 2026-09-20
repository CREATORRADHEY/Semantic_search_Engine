from app.rag_engine import RAGEngine


def test_streaming(mock_engine: RAGEngine):

    tokens = list(
        mock_engine.stream_answer(
            "Explain FAISS."
        )
    )

    assert len(tokens) > 1

    assert "FAISS" in "".join(tokens)