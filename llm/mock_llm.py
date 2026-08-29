from llm.base_llm import BaseLLM


class MockLLM(BaseLLM):
    """
    Fake LLM for testing the RAG pipeline.
    """

    def generate(
        self,
        prompt: str
    ) -> str:

        return (
            "MOCK RESPONSE\n\n"
            + prompt[:250]
        )