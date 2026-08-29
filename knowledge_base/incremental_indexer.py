from pathlib import Path
import json

from utils.file_hash import sha256_file


class IncrementalIndexer:

    def __init__(self, registry_path="storage/hash_registry.json"):
        self.registry_path = Path(registry_path)
        self.registry_path.parent.mkdir(parents=True, exist_ok=True)

        if self.registry_path.exists():
            self.registry = json.loads(self.registry_path.read_text())
        else:
            self.registry = {}

    def save(self):
        self.registry_path.write_text(
            json.dumps(self.registry, indent=2)
        )

    def index(self, folder_path: str | Path):
        folder = Path(folder_path)

        indexed = []
        skipped = []

        for pdf in folder.glob("*.pdf"):

            current_hash = sha256_file(pdf)

            previous_hash = self.registry.get(pdf.name)

            if previous_hash == current_hash:
                skipped.append(pdf.name)
                continue

            self.registry[pdf.name] = current_hash
            indexed.append(pdf.name)

        self.save()

        return {
            "indexed": indexed,
            "skipped": skipped
        }