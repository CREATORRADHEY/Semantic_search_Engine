from pathlib import Path

from utils.file_hash import sha256_file


demo_dir = Path("knowledge_base/demo")
demo_dir.mkdir(parents=True, exist_ok=True)

pdf = demo_dir / "rag.pdf"

if not pdf.exists():
    pdf.write_text("Demo RAG PDF")

hash_value = sha256_file(pdf)

print("=" * 60)
print("SHA256 Example")
print("=" * 60)

print(hash_value)