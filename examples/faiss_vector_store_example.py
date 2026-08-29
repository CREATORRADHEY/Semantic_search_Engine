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


texts = [

    "Artificial Intelligence",

    "Machine Learning",

    "Deep Learning",

    "Football",

    "Pizza"

]


embeddings = embedder.embed(texts)


for index, (text, embedding) in enumerate(

    zip(
        texts,
        embeddings
    )

):

    chunk = Chunk(

        document_id="demo",

        text=text,

        chunk_index=index

    )

    record = VectorRecord(

        chunk=chunk,

        embedding=embedding

    )

    store.add(record)


query = embedder.embed(

    [

        "AI"

    ]

)[0]


results = store.search(

    query,

    top_k=3

)


print("=" * 60)

print("FAISS Search Results")

print("=" * 60)


for score, record in results:

    print(

        f"{score:.4f} -> {record.chunk.text}"

    )