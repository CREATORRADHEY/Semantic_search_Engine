from knowledge_base.collection_manager import (
    CollectionManager
)

manager = CollectionManager()

manager.create_collection(
    "AI",
    "Artificial Intelligence documents"
)

manager.create_collection(
    "Python",
    "Python programming books"
)

manager.create_collection(
    "Finance",
    "Finance and Insurance knowledge"
)

print("=" * 60)
print("Collections")
print("=" * 60)

for collection in manager.list_collections():

    print(collection["namespace"])

    