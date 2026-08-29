from context.prompt_builder import PromptBuilder


def test_prompt_builder():

    builder = PromptBuilder()

    prompt = builder.build(
        question="What is Python?",
        context="Python is a programming language."
    )

    assert "Question:" in prompt

    assert "Answer:" in prompt

    assert "Python is a programming language." in prompt