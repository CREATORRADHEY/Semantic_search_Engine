from models.search_result import SearchResult

from retrieval.rrf import (
    ReciprocalRankFusion
)


# -----------------------------------------
# BM25 Results
# -----------------------------------------

bm25_results = [

    SearchResult(
        score=5.0,
        text="Document A",
        chunk_id="doc-a:0",
        document_id="doc-a"
    ),

    SearchResult(
        score=4.0,
        text="Document B",
        chunk_id="doc-b:0",
        document_id="doc-b"
    ),

    SearchResult(
        score=3.0,
        text="Document C",
        chunk_id="doc-c:0",
        document_id="doc-c"
    )

]


# -----------------------------------------
# FAISS Results
# -----------------------------------------

faiss_results = [

    SearchResult(
        score=0.9,
        text="Document C",
        chunk_id="doc-c:0",
        document_id="doc-c"
    ),

    SearchResult(
        score=0.8,
        text="Document A",
        chunk_id="doc-a:0",
        document_id="doc-a"
    ),

    SearchResult(
        score=0.7,
        text="Document D",
        chunk_id="doc-d:0",
        document_id="doc-d"
    )

]


# -----------------------------------------
# RRF
# -----------------------------------------

fusion = ReciprocalRankFusion()


results = fusion.fuse(
    [
        bm25_results,
        faiss_results
    ],
    top_k=4
)


# -----------------------------------------
# Display
# -----------------------------------------

print("=" * 60)

print("RRF Results")

print("=" * 60)


for result in results:

    print(
        f"{result.score:.6f} -> "
        f"{result.text}"
    )