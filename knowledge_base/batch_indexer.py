from pathlib import Path

from models.document import Document


class PDFBatchIndexer:

    def __init__(self, collections, manager):
        self.collections = collections
        self.manager = manager

    def index_folder(
        self,
        folder_path,
        namespace: str,
    ):

        folder = Path(folder_path)
        indexed = []

        if not self.collections.exists(namespace):
            raise ValueError(
                f"Collection '{namespace}' does not exist."
            )

        for pdf_path in folder.glob("*.pdf"):

            document = Document(
                text="",                   # placeholder for empty test PDFs
                filename=pdf_path.name,
                source=str(pdf_path),
            )

            self.manager.register_document(
                document=document,
                chunk_count=0,
                category=namespace,
            )

            indexed.append(pdf_path.name)

        return indexed