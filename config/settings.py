import os

from dotenv import load_dotenv

load_dotenv()


class Settings:

    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

    DEFAULT_PROVIDER = os.getenv(
        "DEFAULT_LLM_PROVIDER",
        "gemini"
    )

    DEFAULT_OPENAI_MODEL = os.getenv(
        "DEFAULT_OPENAI_MODEL",
        "gpt-5-mini"
    )

    DEFAULT_GEMINI_MODEL = os.getenv(
        "DEFAULT_GEMINI_MODEL",
        "gemini-2.5-flash"
    )


settings = Settings()