from typing import List

from chunking.base_chunker import BaseChunker
from models.chunk import Chunk
from models.document import Document


class OverlapChunker(BaseChunker):

    def __init__(
        self,
        chunk_size: int = 500,
        overlap: int = 100
    ):
        self.chunk_size = chunk_size
        self.overlap = overlap

    def process(self, document: Document) -> List[Chunk]:

        chunks = []

        text = document.text

        start = 0

        while start < len(text):

            end = min(start + self.chunk_size, len(text))

            chunk_text = text[start:end].strip()

            chunk = Chunk(
                document_id=document.id,
                text=chunk_text,
                chunk_index=len(chunks)
            )

            chunks.append(chunk)

            if end == len(text):
                break

            start = end - self.overlap

        return chunks

