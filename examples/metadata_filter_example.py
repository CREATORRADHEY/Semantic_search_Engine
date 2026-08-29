from embeddings.sentence_transformer_embedder import (
    SentenceTransformerEmbedder
)

from models.chunk import Chunk
from models.vector_record import VectorRecord

from vector_store.faiss_vector_store import (
    FAISSVectorStore
)


embedder = SentenceTransformerEmbedder()

store = FAISSVectorStore()


documents = [

    (
        "Artificial Intelligence in Finance",
        {
            "filename": "finance.pdf",
            "source": "pdf",
            "department": "finance",
            "year": 2026,
            "page": 10
        }
    ),

    (
        "Artificial Intelligence in Healthcare",
        {
            "filename": "healthcare.pdf",
            "source": "pdf",
            "department": "healthcare",
            "year": 2026,
            "page": 15
        }
    ),

    (
        "Machine Learning Systems",
        {
            "filename": "ml.pdf",
            "source": "pdf",
            "department": "engineering",
            "year": 2024,
            "page": 20
        }
    ),

    (
        "Football Analytics",
        {
            "filename": "sports.pdf",
            "source": "pdf",
            "department": "sports",
            "year": 2025,
            "page": 5
        }
    )

]


texts = [
    document[0]
    for document in documents
]


embeddings = embedder.embed(
    texts
)


for index, (
    text,
    metadata,
    embedding
) in enumerate(
    zip(
        texts,
        [
            document[1]
            for document in documents
        ],
        embeddings
    )
):

    chunk = Chunk(

        document_id=f"document-{index}",

        text=text,

        chunk_index=0,

        metadata=metadata

    )

    record = VectorRecord(

        chunk=chunk,

        embedding=embedding

    )

    store.add(record)


query_embedding = embedder.embed(
    ["AI"]
)[0]


results = store.search(

    query_embedding,

    top_k=3,

    filters={
        "filename": "finance.pdf",
        "source": "pdf"
    }

)

print("=" * 60)

print("Filtered Search Results")

print("=" * 60)


for score, record in results:

    print(
        f"{score:.4f} -> "
        f"{record.chunk.text}"
    )