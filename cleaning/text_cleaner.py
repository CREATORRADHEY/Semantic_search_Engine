import re

from models.document import Document


class TextCleaningEngine:

    def clean(
        self,
        document: Document
    ) -> Document:

        text = document.text

        # Remove multiple spaces
        text = re.sub(r"[ \t]+", " ", text)

        # Normalize line endings
        text = text.replace("\r\n", "\n")

        # Remove excessive blank lines
        text = re.sub(r"\n{3,}", "\n\n", text)

        # Remove leading/trailing whitespace
        text = text.strip()

        return document.model_copy(
            update={
                "text": text
            }
        )