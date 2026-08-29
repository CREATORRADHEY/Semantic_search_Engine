from tokenization.tokenizer import Tokenizer


tokenizer = Tokenizer()

text = """
Artificial Intelligence is changing software engineering.
"""

tokens = tokenizer.encode(text)

print(f"Token Count: {len(tokens)}")
print(tokens)

decoded = tokenizer.decode(tokens)

print()
print(decoded)