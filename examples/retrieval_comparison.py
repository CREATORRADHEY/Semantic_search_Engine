from embeddings.sentence_transformer_embedder import (
    SentenceTransformerEmbedder
)

from models.chunk import Chunk
from models.vector_record import VectorRecord

from retrieval.bm25_retriever import (
    BM25Retriever
)

from retrieval.rrf import (
    ReciprocalRankFusion
)

from retrieval.evaluation import (
    RetrievalEvaluator
)

from vector_store.faiss_vector_store import (
    FAISSVectorStore
)


# -----------------------------------------
# Evaluation dataset
# -----------------------------------------

EVALUATION_DATASET = [

    {
        "query": "FAISS IndexFlatIP",
        "relevant_chunks": {
            "evaluation:0",
            "evaluation:3"
        }
    },

    {
        "query": "neural networks optimization",
        "relevant_chunks": {
            "evaluation:4"
        }
    },

    {
        "query": "software engineering artificial intelligence",
        "relevant_chunks": {
            "evaluation:1"
        }
    },

    {
        "query": "machine learning patterns",
        "relevant_chunks": {
            "evaluation:2"
        }
    }

]


# -----------------------------------------
# Dataset
# -----------------------------------------

TEXTS = [

    "FAISS is a library for efficient similarity search.",

    "Artificial Intelligence is changing software engineering.",

    "Machine Learning models learn patterns from data.",

    "IndexFlatIP performs exact inner product search in FAISS.",

    "Neural networks learn representations using optimization."

]


# -----------------------------------------
# Build chunks
# -----------------------------------------

def build_chunks():

    chunks = []

    for index, text in enumerate(TEXTS):

        chunks.append(
            Chunk(
                document_id="evaluation",
                text=text,
                chunk_index=index,
                metadata={
                    "source": "evaluation"
                }
            )
        )

    return chunks


# -----------------------------------------
# Build retrieval systems
# -----------------------------------------

def build_systems():

    chunks = build_chunks()

    embedder = SentenceTransformerEmbedder()

    embeddings = embedder.embed(
        TEXTS
    )

    # -------------------------------------
    # BM25
    # -------------------------------------

    bm25 = BM25Retriever()

    bm25.add_documents(
        chunks
    )

    # -------------------------------------
    # FAISS
    # -------------------------------------

    faiss_store = FAISSVectorStore()

    records = []

    for chunk, embedding in zip(
        chunks,
        embeddings
    ):

        records.append(
            VectorRecord(
                chunk=chunk,
                embedding=embedding
            )
        )

    faiss_store.add_batch(
        records
    )

    # -------------------------------------
    # RRF
    # -------------------------------------

    fusion = ReciprocalRankFusion()

    return (
        embedder,
        bm25,
        faiss_store,
        fusion
    )


# -----------------------------------------
# Evaluate one system
# -----------------------------------------

def evaluate_system(
    system_name,
    search_function,
    dataset
):

    recall_scores = []

    hit_scores = []

    mrr_scores = []

    ndcg_scores = []


    for item in dataset:

        query = item["query"]

        relevant_chunks = (
            item["relevant_chunks"]
        )

        results = search_function(
            query
        )

        recall = (
            RetrievalEvaluator.recall_at_k(
                results,
                relevant_chunks,
                k=3
            )
        )

        hit_rate = (
            RetrievalEvaluator.hit_rate_at_k(
                results,
                relevant_chunks,
                k=3
            )
        )

        mrr = (
            RetrievalEvaluator.reciprocal_rank(
                results,
                relevant_chunks
            )
        )

        relevance_scores = {
            chunk_id: 1.0
            for chunk_id in relevant_chunks
        }

        ndcg = (
            RetrievalEvaluator.ndcg_at_k(
                results,
                relevance_scores,
                k=3
            )
        )

        recall_scores.append(
            recall
        )

        hit_scores.append(
            hit_rate
        )

        mrr_scores.append(
            mrr
        )

        ndcg_scores.append(
            ndcg
        )


    count = len(dataset)


    print(
        f"{system_name:<10}"
        f"{sum(recall_scores) / count:>14.4f}"
        f"{sum(hit_scores) / count:>14.4f}"
        f"{sum(mrr_scores) / count:>14.4f}"
        f"{sum(ndcg_scores) / count:>14.4f}"
    )


# -----------------------------------------
# Main
# -----------------------------------------

def main():

    print("=" * 70)

    print(
        "BM25 vs FAISS vs HYBRID"
    )

    print("=" * 70)

    print()

    embedder, bm25, faiss_store, fusion = (
        build_systems()
    )


    # -------------------------------------
    # BM25
    # -------------------------------------

    def search_bm25(query):

        return bm25.search(
            query,
            top_k=3
        )


    # -------------------------------------
    # FAISS
    # -------------------------------------

    def search_faiss(query):

        query_embedding = embedder.embed(
            [query]
        )[0]

        return faiss_store.search(
            query_embedding,
            top_k=3
        )


    # -------------------------------------
    # Hybrid
    # -------------------------------------

    def search_hybrid(query):

        bm25_results = search_bm25(
            query
        )

        faiss_results = search_faiss(
            query
        )

        return fusion.fuse(
            [
                bm25_results,
                faiss_results
            ],
            top_k=3
        )


    print(
        f"{'System':<10}"
        f"{'Recall@3':>14}"
        f"{'Hit Rate':>14}"
        f"{'MRR':>14}"
        f"{'NDCG@3':>14}"
    )

    print("-" * 70)


    evaluate_system(
        "BM25",
        search_bm25,
        EVALUATION_DATASET
    )

    evaluate_system(
        "FAISS",
        search_faiss,
        EVALUATION_DATASET
    )

    evaluate_system(
        "HYBRID",
        search_hybrid,
        EVALUATION_DATASET
    )


    print()

    print("=" * 70)


if __name__ == "__main__":

    main()