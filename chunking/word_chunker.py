from typing import List

from chunking.base_chunker import BaseChunker
from models.chunk import Chunk
from models.document import Document


class WordChunker(BaseChunker):

    def __init__(self, chunk_size: int = 500):
        self.chunk_size = chunk_size

    def process(self, document: Document) -> List[Chunk]:

        chunks = []

        text = document.text

        start = 0

        while start < len(text):

            end = start + self.chunk_size

            if end >= len(text):
                end = len(text)

            else:

                while end > start and text[end] != " ":
                    end -= 1

                if end == start:
                    end = start + self.chunk_size

            chunk_text = text[start:end].strip()

            chunk = Chunk(
                document_id=document.id,
                text=chunk_text,
                chunk_index=len(chunks)
            )

            chunks.append(chunk)

            start = end

        return chunks