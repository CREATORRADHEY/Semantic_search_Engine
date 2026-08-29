from config.settings import settings


def test_settings_object():

    assert settings.DEFAULT_PROVIDER in [
        "openai",
        "gemini"
    ]

    assert settings.DEFAULT_OPENAI_MODEL

    assert settings.DEFAULT_GEMINI_MODEL