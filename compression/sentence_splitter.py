import re


class SentenceSplitter:
    """
    Splits paragraphs into sentences.
    """

    @staticmethod
    def split(text: str):

        sentences = re.split(
            r"(?<=[.!?])\s+",
            text.strip()
        )

        return [
            sentence.strip()
            for sentence in sentences
            if sentence.strip()
        ]