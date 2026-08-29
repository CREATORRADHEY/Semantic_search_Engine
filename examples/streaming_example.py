import time

from llm.mock_llm import MockLLM


llm = MockLLM()

answer = llm.generate(
    "Explain Python recursion."
)

print("=" * 60)
print("Streaming Response")
print("=" * 60)

for word in answer.split():

    print(word, end=" ", flush=True)

    time.sleep(0.05)

print()