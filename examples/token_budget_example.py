from context.token_budget import TokenBudgetManager


context = """
Artificial Intelligence powers semantic retrieval systems.

Machine Learning helps ranking.

Python supports object-oriented programming.

""" * 100


manager = TokenBudgetManager(
    max_tokens=250
)

estimated = manager.estimate_tokens(
    context
)

trimmed = manager.trim_context(
    context
)

print("=" * 60)
print("Token Budget Example")
print("=" * 60)

print("Estimated Tokens :", estimated)

print(
    "Trimmed Tokens   :",
    manager.estimate_tokens(trimmed)
)