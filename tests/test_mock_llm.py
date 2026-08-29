from llm.mock_llm import MockLLM


def test_mock_llm():

    llm = MockLLM()

    response = llm.generate(
        "Hello AI"
    )

    assert "MOCK RESPONSE" in response