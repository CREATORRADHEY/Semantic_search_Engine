from models.search_result import SearchResult
from reranking.cross_encoder_reranker import CrossEncoderReranker

# -----------------------------------------
# Query
# -----------------------------------------

query = "car insurance"

# -----------------------------------------
# Retrieved Results (Pretend these came from Hybrid Search)
# -----------------------------------------

results = [
    SearchResult(
        document_id="doc1",
        chunk_id="doc1:0",
        text="Vehicle insurance provides coverage for automobiles.",
        score=0.13,
        metadata={"source": "demo"}
    ),
    SearchResult(
        document_id="doc2",
        chunk_id="doc2:0",
        text="Car insurance protects vehicle owners from financial losses.",
        score=0.12,
        metadata={"source": "demo"}
    ),
    SearchResult(
        document_id="doc3",
        chunk_id="doc3:0",
        text="Artificial Intelligence powers semantic search systems.",
        score=0.06,
        metadata={"source": "demo"}
    ),
]

# -----------------------------------------
# Load CrossEncoder
# -----------------------------------------

reranker = CrossEncoderReranker()

# -----------------------------------------
# Rerank Results
# -----------------------------------------

reranked_results = reranker.rerank(
    query=query,
    results=results,
    top_k=3
)

# -----------------------------------------
# Display
# -----------------------------------------

print("=" * 60)
print("CrossEncoder Reranked Results")
print("=" * 60)

for result in reranked_results:
    print(f"{result.score:.4f} -> {result.text}")