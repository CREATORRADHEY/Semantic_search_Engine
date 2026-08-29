from llm.mock_llm import MockLLM


def test_rag_engine():

    llm = MockLLM()

    response = llm.generate(
        "Python classes"
    )

    assert "MOCK RESPONSE" in response