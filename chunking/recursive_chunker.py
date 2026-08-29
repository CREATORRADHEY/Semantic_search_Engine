from typing import List

from chunking.base_chunker import BaseChunker
from models.chunk import Chunk
from models.document import Document


class RecursiveChunker(BaseChunker):

    def __init__(
        self,
        chunk_size: int = 500,
        overlap: int = 50
    ):
        self.chunk_size = chunk_size
        self.overlap = overlap

        self.separators = [
            "\n\n",
            "\n",
            ". ",
            " ",
            ""
        ]

    def split_text(
        self,
        text: str,
        separators: List[str]
    ) -> List[str]:

        if len(text) <= self.chunk_size:
            return [text]

        if not separators:
            return [
                text[i:i + self.chunk_size]
                for i in range(
                    0,
                    len(text),
                    self.chunk_size
                )
            ]

        separator = separators[0]

        if separator == "":
            return [
                text[i:i + self.chunk_size]
                for i in range(
                    0,
                    len(text),
                    self.chunk_size
                )
            ]

        parts = text.split(separator)

        chunks = []

        current = ""

        for part in parts:

            candidate = current + separator + part if current else part

            if len(candidate) <= self.chunk_size:

                current = candidate

            else:

                if current:
                    chunks.extend(
                        self.split_text(
                            current,
                            separators[1:]
                        )
                    )

                current = part

        if current:
            chunks.extend(
                self.split_text(
                    current,
                    separators[1:]
                )
            )

        return chunks

    def apply_overlap(
        self,
        chunks: List[str]
    ) -> List[str]:

        if self.overlap <= 0:
            return chunks

        overlapped_chunks = []

        for index, chunk in enumerate(chunks):

            if index == 0:
                overlapped_chunks.append(chunk)
                continue

            previous_chunk = chunks[index - 1]

            overlap_text = previous_chunk[-self.overlap:]

            overlapped_chunks.append(
                overlap_text + chunk
            )

        return overlapped_chunks

    def process(
    self,
    document: Document
) -> List[Chunk]:

    texts = self.split_text(
        document.text,
        self.separators
    )

    chunks = []

    for index, text in enumerate(texts):

        chunks.append(

            Chunk(
                document_id=document.id,
                text=text,
                chunk_index=index,
                metadata={
                    "filename": document.filename,
                    "source": document.source
                }
            )

        )

    return chunks