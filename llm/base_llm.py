from abc import ABC, abstractmethod


class BaseLLM(ABC):
    """
    Abstract interface for every LLM provider.
    """

    @abstractmethod
    def generate(
        self,
        prompt: str
    ) -> str:
        pass