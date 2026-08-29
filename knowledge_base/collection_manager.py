import json
from pathlib import Path

from knowledge_base.collection import Collection


class CollectionManager:

    def __init__(
        self,
        registry_path="storage/collections.json"
    ):

        self.registry_path = Path(registry_path)

        self.registry_path.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        if self.registry_path.exists():

            self.collections = json.loads(
                self.registry_path.read_text()
            )

        else:

            self.collections = {}

    def create_collection(
        self,
        namespace,
        description=None
    ):

        self.collections[namespace] = Collection(
            namespace=namespace,
            description=description
        ).model_dump()

        self.save()

    def list_collections(self):

        return list(self.collections.values())

    def exists(self, namespace):

        return namespace in self.collections

    def save(self):

        self.registry_path.write_text(
            json.dumps(
                self.collections,
                indent=2
            )
        )

        