from models.search_result import SearchResult

from retrieval.evaluation import (
    RetrievalEvaluator
)


# -----------------------------------------
# Simulated retrieval results
# -----------------------------------------

results = [

    SearchResult(
        score=0.95,
        text="FAISS is a library for similarity search.",
        chunk_id="doc:0",
        document_id="doc"
    ),

    SearchResult(
        score=0.82,
        text="Machine Learning models learn patterns.",
        chunk_id="doc:1",
        document_id="doc"
    ),

    SearchResult(
        score=0.75,
        text="IndexFlatIP performs inner product search.",
        chunk_id="doc:2",
        document_id="doc"
    ),

    SearchResult(
        score=0.50,
        text="Football is a popular sport.",
        chunk_id="doc:3",
        document_id="doc"
    )
]


# -----------------------------------------
# Ground truth
# -----------------------------------------

relevant_chunks = {
    "doc:0",
    "doc:2"
}


# -----------------------------------------
# Recall@K
# -----------------------------------------

recall = RetrievalEvaluator.recall_at_k(
    results,
    relevant_chunks,
    k=3
)


# -----------------------------------------
# Hit Rate@K
# -----------------------------------------

hit_rate = RetrievalEvaluator.hit_rate_at_k(
    results,
    relevant_chunks,
    k=3
)


# -----------------------------------------
# Reciprocal Rank
# -----------------------------------------

rr = RetrievalEvaluator.reciprocal_rank(
    results,
    relevant_chunks
)


# -----------------------------------------
# NDCG@K
# -----------------------------------------

relevance_scores = {

    "doc:0": 3.0,

    "doc:2": 2.0,

    "doc:1": 1.0,

    "doc:3": 0.0

}


ndcg = RetrievalEvaluator.ndcg_at_k(
    results,
    relevance_scores,
    k=3
)


# -----------------------------------------
# Output
# -----------------------------------------

print("=" * 60)

print("Retrieval Evaluation")

print("=" * 60)

print()

print(
    f"Recall@3   : {recall:.4f}"
)

print(
    f"Hit Rate@3 : {hit_rate:.4f}"
)

print(
    f"MRR        : {rr:.4f}"
)

print(
    f"NDCG@3     : {ndcg:.4f}"
)