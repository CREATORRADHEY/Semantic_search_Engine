from compression.sentence_scorer import SentenceScorer


def test_sentence_scorer():

    scorer = SentenceScorer()

    text = (
        "FAISS performs vector similarity search. "
        "Docker packages containers."
    )

    results = scorer.score(
        "vector search",
        text
    )

    top_score, top_sentence = results[0]

    assert "FAISS" in top_sentence