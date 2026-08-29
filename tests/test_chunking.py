from models.document import Document

from chunking.fixed_chunker import FixedChunker


def test_fixed_chunker():

    chunker = FixedChunker(

        chunk_size=5

    )

    document = Document(

        filename="demo",

        source="text",

        text="ABCDEFGHIJK"

    )

    chunks = chunker.process(

        document

    )

    assert len(chunks) == 3