from embeddings.sentence_transformer_embedder import (
    SentenceTransformerEmbedder
)

from models.chunk import Chunk
from models.vector_record import VectorRecord

from retrieval.bm25_retriever import BM25Retriever
from retrieval.query_expansion import QueryExpander
from retrieval.multi_query_hybrid import (
    MultiQueryHybridRetriever
)

from vector_store.faiss_vector_store import (
    FAISSVectorStore
)


texts = [

    "Car insurance protects vehicle owners from financial losses.",

    "Vehicle insurance provides coverage for automobiles.",

    "Automobile insurance includes liability coverage.",

    "Artificial Intelligence powers semantic search systems.",

    "Machine Learning helps search ranking.",

    "Football is a popular sport."

]

chunks = []

for index, text in enumerate(texts):

    chunks.append(
        Chunk(
            document_id="hybrid-demo",
            text=text,
            chunk_index=index,
            metadata={
                "source": "demo"
            }
        )
    )

bm25 = BM25Retriever()

bm25.add_documents(chunks)

embedder = SentenceTransformerEmbedder()

embeddings = embedder.embed(texts)

faiss = FAISSVectorStore()

records = []

for chunk, embedding in zip(chunks, embeddings):

    records.append(
        VectorRecord(
            chunk=chunk,
            embedding=embedding
        )
    )

faiss.add_batch(records)

expander = QueryExpander(

    expansions={

        "car": [
            "vehicle",
            "automobile"
        ],

        "insurance": [
            "coverage"
        ]

    }

)

retriever = MultiQueryHybridRetriever(
    bm25,
    faiss,
    expander,
    embedder
)

query = "car insurance"

results = retriever.search(
    query,
    top_k=5
)

print("=" * 60)
print("Production Multi Query Hybrid Search")
print("=" * 60)
print()

for result in results:

    print(
        f"{result.score:.6f} | "
        f"{result.text}"
    )