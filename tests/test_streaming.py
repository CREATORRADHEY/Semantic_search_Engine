from llm.mock_llm import MockLLM


def test_streaming():

    llm = MockLLM()

    answer = llm.generate(
        "Hello"
    )

    words = answer.split()

    assert len(words) > 0