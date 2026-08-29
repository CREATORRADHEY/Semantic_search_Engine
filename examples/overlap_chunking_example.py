from ingestion.pdf_ingestion import PDFIngestionEngine
from cleaning.text_cleaner import TextCleaningEngine
from chunking.overlap_chunker import OverlapChunker

ingestion = PDFIngestionEngine()
cleaner = TextCleaningEngine()

chunker = OverlapChunker(
    chunk_size=500,
    overlap=100
)

document = ingestion.process("documents/python.pdf")

clean_document = cleaner.process(document)

chunks = chunker.process(clean_document)

print("=" * 60)
print(f"Total Chunks : {len(chunks)}")
print("=" * 60)

for chunk in chunks[:3]:
    print(f"\nChunk {chunk.chunk_index}")
    print("-" * 40)
    print(chunk.text)