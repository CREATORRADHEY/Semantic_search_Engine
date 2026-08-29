from abc import ABC, abstractmethod
from typing import List

from models.document import Document
from models.chunk import Chunk


class BaseChunker(ABC):

    @abstractmethod
    def process(self, document: Document) -> List[Chunk]:
        pass

    