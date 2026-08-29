from models.chunk import Chunk

from models.vector_record import VectorRecord

from vector_store.memory_vector_store import MemoryVectorStore


def test_add_record():

    store = MemoryVectorStore()

    chunk = Chunk(

        document_id="demo",

        text="AI",

        chunk_index=0

    )

    record = VectorRecord(

        chunk=chunk,

        embedding=[0.1, 0.2, 0.3]

    )

    store.add(record)

    assert len(store.records) == 1