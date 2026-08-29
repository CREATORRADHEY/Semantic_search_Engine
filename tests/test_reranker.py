from models.search_result import SearchResult

from reranking.cross_encoder_reranker import (
    CrossEncoderReranker
)


def test_cross_encoder_reranker():

    query = "car insurance"

    results = [

        SearchResult(
            document_id="1",
            chunk_id="1:0",
            text="Vehicle insurance covers automobiles.",
            score=0.12,
            metadata={}
        ),

        SearchResult(
            document_id="2",
            chunk_id="2:0",
            text="Artificial Intelligence powers search.",
            score=0.10,
            metadata={}
        )

    ]

    reranker = CrossEncoderReranker()

    reranked = reranker.rerank(
        query=query,
        results=results,
        top_k=2
    )

    assert len(reranked) == 2

    assert "insurance" in reranked[0].text.lower()