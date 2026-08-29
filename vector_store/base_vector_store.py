from abc import ABC, abstractmethod
from typing import List

from models.vector_record import VectorRecord


class BaseVectorStore(ABC):

    @abstractmethod
    def add(
        self,
        record: VectorRecord
    ):
        pass

    @abstractmethod
    def search(
        self,
        query_embedding: List[float],
        top_k: int = 5
    ):
        pass