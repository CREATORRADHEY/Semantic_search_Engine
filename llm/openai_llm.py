from openai import OpenAI

from config.settings import settings

from llm.base_llm import BaseLLM


class OpenAILLM(BaseLLM):

    def __init__(self):

        if not settings.OPENAI_API_KEY:
            raise ValueError(
                "OPENAI_API_KEY missing in .env"
            )

        self.client = OpenAI(
            api_key=settings.OPENAI_API_KEY
        )

        self.model = settings.DEFAULT_OPENAI_MODEL

    def generate(
        self,
        prompt: str
    ) -> str:

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response.choices[0].message.content