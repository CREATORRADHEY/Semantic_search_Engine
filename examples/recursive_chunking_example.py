from ingestion.pdf_ingestion import PDFIngestionEngine
from cleaning.text_cleaner import TextCleaningEngine
from chunking.recursive_chunker import RecursiveChunker


def main():
    ingestion = PDFIngestionEngine()
    cleaner = TextCleaningEngine()

    chunker = RecursiveChunker(
        chunk_size=500,
        overlap=50
    )

    # Step 1: Read PDF
    document = ingestion.process("documents/python.pdf")

    # Step 2: Clean Text
    clean_document = cleaner.process(document)

    # Step 3: Chunk
    chunks = chunker.process(clean_document)

    print("=" * 60)
    print(f"Total Chunks: {len(chunks)}")
    print("=" * 60)

    for chunk in chunks[:5]:
        print(f"\nChunk {chunk.chunk_index}")
        print("-" * 40)
        print(chunk.text)


if __name__ == "__main__":
    main() 