from pathlib import Path

from knowledge_base.incremental_indexer import IncrementalIndexer


demo_dir = Path("knowledge_base/demo")
demo_dir.mkdir(parents=True, exist_ok=True)

pdf = demo_dir / "rag.pdf"

if not pdf.exists():
    pdf.write_text("Demo RAG PDF")


indexer = IncrementalIndexer()

print("=" * 60)
print("First Run")
print("=" * 60)

print(indexer.index(demo_dir))

print("=" * 60)
print("Second Run")
print("=" * 60)

print(indexer.index(demo_dir))