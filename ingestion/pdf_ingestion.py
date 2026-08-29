import fitz
from pathlib import Path

from models.document import Document


class PDFIngestionEngine:

    def process(
        self,
        file_path: str
    ) -> Document:

        pdf = fitz.open(file_path)

        text = ""

        for page in pdf:

            text += page.get_text()

        pdf.close()

        return Document(
            filename=Path(file_path).name,
            source="pdf",
            text=text
        )