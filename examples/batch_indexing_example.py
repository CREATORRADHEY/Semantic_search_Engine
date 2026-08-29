from knowledge_base.collection_manager import (
    CollectionManager
)

from knowledge_base.manager import KnowledgeBaseManager

from knowledge_base.batch_indexer import (
    PDFBatchIndexer
)

collections = CollectionManager()

collections.create_collection(
    "AI"
)

knowledge_manager = KnowledgeBaseManager()

indexer = PDFBatchIndexer(
    collections,
    knowledge_manager
)

files = indexer.index_folder(
    folder_path="knowledge/AI",
    namespace="AI"
)

print("=" * 60)
print("Indexed Files")
print("=" * 60)

for file in files:

    print(file)