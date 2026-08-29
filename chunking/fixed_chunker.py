from typing import List

from models.document import Document
from models.chunk import Chunk
from chunking.base_chunker import BaseChunker


class FixedChunker(BaseChunker):

    def __init__(self, chunk_size: int = 1000):
        self.chunk_size = chunk_size

    def process(self, document: Document) -> List[Chunk]:

        chunks = []

        text = document.text

        for i in range(0, len(text), self.chunk_size):

            chunk_text = text[i:i+self.chunk_size]

            chunk = Chunk(
                document_id=document.id,
                text=chunk_text,
                chunk_index=len(chunks)
            )

            chunks.append(chunk)

        return chunks