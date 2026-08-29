from typing import List

import tiktoken


class Tokenizer:

    def __init__(
        self,
        encoding_name: str = "cl100k_base"
    ):
        self.encoding = tiktoken.get_encoding(
            encoding_name
        )

    def encode(
        self,
        text: str
    ) -> List[int]:

        return self.encoding.encode(text)

    def decode(
        self,
        tokens: List[int]
    ) -> str:

        return self.encoding.decode(tokens)

    def count_tokens(
        self,
        text: str
    ) -> int:

        return len(
            self.encode(text)
        )