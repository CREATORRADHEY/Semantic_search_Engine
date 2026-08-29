from ingestion.pdf_ingestion import PDFIngestionEngine
from cleaning.text_cleaner import TextCleaningEngine


ingestion = PDFIngestionEngine()
cleaner = TextCleaningEngine()

document = ingestion.process("documents/python.pdf")

clean_document = cleaner.process(document)

print("=" * 60)
print(clean_document.text[:1000])