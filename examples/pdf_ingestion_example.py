from ingestion.pdf_ingestion import PDFIngestionEngine

engine = PDFIngestionEngine()

document = engine.process("documents/python.pdf")

print(document)
