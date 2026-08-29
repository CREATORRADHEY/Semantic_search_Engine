from context.token_budget import TokenBudgetManager


def test_token_budget():

    manager = TokenBudgetManager(
        max_tokens=10
    )

    text = "Hello World " * 20

    trimmed = manager.trim_context(text)

    assert manager.estimate_tokens(trimmed) <= 10