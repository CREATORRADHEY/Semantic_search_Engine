import faiss
import numpy as np

from models.vector_record import VectorRecord
from models.search_result import SearchResult

from vector_store.base_vector_store import BaseVectorStore
from vector_store.metadata_filter import MetadataFilter
from storage.faiss_storage import FAISSStorage

class FAISSVectorStore(BaseVectorStore):

    def __init__(self):

        self.index = None

        self.records = []

    def _create_index(
        self,
        dimension: int
    ):

        self.index = faiss.IndexFlatIP(
            dimension
        )

    storage = FAISSStorage()

def save(self, path: str):
    storage.save_index(
        self.index,
        path
    )


def load(self, path: str):
    self.index = storage.load_index(path)

    def add(
        self,
        record: VectorRecord
    ):

        if self.index is None:

            self._create_index(
                len(record.embedding)
            )

        vector = np.array(
            [record.embedding],
            dtype=np.float32
        )

        faiss.normalize_L2(vector)

        self.index.add(vector)

        self.records.append(record)

    def add_batch(
        self,
        records: list[VectorRecord]
    ):

        if not records:

            return

        if self.index is None:

            self._create_index(
                len(records[0].embedding)
            )

        vectors = np.array(
            [
                record.embedding
                for record in records
            ],
            dtype=np.float32
        )

        faiss.normalize_L2(vectors)

        self.index.add(vectors)

        self.records.extend(records)

    def search(
        self,
        query_embedding,
        top_k: int = 5,
        filters: dict | None = None
    ) -> list[SearchResult]:

        if self.index is None:

            return []

        query = np.array(
            [query_embedding],
            dtype=np.float32
        )

        faiss.normalize_L2(query)

        search_k = self.index.ntotal

        scores, indices = self.index.search(
            query,
            search_k
        )

        results = []

        for score, index in zip(
            scores[0],
            indices[0]
        ):

            if index == -1:

                continue

            record = self.records[index]

            if filters:

                if not MetadataFilter.matches(
                    record.chunk.metadata,
                    filters
                ):

                    continue

            results.append(
                SearchResult(
                   score=float(score),
                    text=record.chunk.text,
                 chunk_id=(
                        f"{record.chunk.document_id}:"
                         f"{record.chunk.chunk_index}"
                         ),
                          document_id=record.chunk.document_id,
                          metadata=record.chunk.metadata
) 
            )

            if len(results) >= top_k:

                break

        return results

    