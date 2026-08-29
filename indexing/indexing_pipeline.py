from ingestion.pdf_ingestion import PDFIngestionEngine
from cleaning.text_cleaner import TextCleaningEngine
from chunking.recursive_chunker import RecursiveChunker

from embeddings.base_embedder import BaseEmbedder
from vector_store.base_vector_store import BaseVectorStore

from models.vector_record import VectorRecord


class IndexingPipeline:

    def __init__(
       self,
       ingestion: PDFIngestionEngine,
       cleaner: TextCleaningEngine,
       chunker: RecursiveChunker,
       embedder: BaseEmbedder,
       vector_store: BaseVectorStore
    ):

        self.ingestion = ingestion
        self.cleaner = cleaner
        self.chunker = chunker

        self.embedder = embedder
        self.vector_store = vector_store

    def index_pdf(
        self,
        file_path: str
    ):

        # Step 1: Read PDF
        document = self.ingestion.process(file_path)

        # Step 2: Clean Text
        document = self.cleaner.clean(document)

        # Step 3: Chunk Document
        chunks = self.chunker.process(document)

        # Step 4: Extract Chunk Text
        texts = [
            chunk.text
            for chunk in chunks
        ]

        # Step 5: Generate Embeddings
        embeddings = self.embedder.embed(texts)

        # Step 6: Store in Vector Store
        for chunk, embedding in zip(chunks, embeddings):

            record = VectorRecord(
                chunk=chunk,
                embedding=embedding
            )

            self.vector_store.add(record)
            