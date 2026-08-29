from app.rag_engine import RAGEngine
from llm.mock_llm import MockLLM

# Use your existing retriever.
retriever = ...

engine = RAGEngine(
    retriever=retriever,
    llm=MockLLM()
)

questions = [
    "What is recursion?",
    "Give me an example.",
    "Why is it useful?"
]

for question in questions:

    print("=" * 60)
    print("USER:", question)

    answer = engine.ask(question)

    print("\nASSISTANT:\n")
    print(answer)