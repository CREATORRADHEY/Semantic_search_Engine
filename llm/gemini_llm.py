from google import genai

from config.settings import settings

from llm.base_llm import BaseLLM


class GeminiLLM(BaseLLM):

    def __init__(self):

        if not settings.GEMINI_API_KEY:
            raise ValueError(
                "GEMINI_API_KEY missing in .env"
            )

        self.client = genai.Client(
            api_key=settings.GEMINI_API_KEY
        )

        self.model = settings.DEFAULT_GEMINI_MODEL

    def generate(
        self,
        prompt: str
    ) -> str:

        response = self.client.models.generate_content(
            model=self.model,
            contents=prompt
        )

        return response.text