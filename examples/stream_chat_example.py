from api.dependencies import get_rag_engine

rag = get_rag_engine()

print("=" * 60)
print("Streaming Chat Example")
print("=" * 60)

for token in rag.stream_answer(
    "Explain semantic search."
):
    print(token, end="")