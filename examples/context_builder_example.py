from models.search_result import SearchResult

from context.context_builder import ContextBuilder


results = [

    SearchResult(
        document_id="doc1",
        chunk_id="1",
        text="Python supports object-oriented programming with classes and objects.",
        score=9.2,
        metadata={"source": "python.pdf"}
    ),

    SearchResult(
        document_id="doc2",
        chunk_id="2",
        text="Classes organize code into reusable components.",
        score=8.9,
        metadata={"source": "python.pdf"}
    ),

    SearchResult(
        document_id="doc3",
        chunk_id="3",
        text="Football is one of the world's most popular sports.",
        score=-10,
        metadata={"source": "sports.pdf"}
    )

]

builder = ContextBuilder(
    max_chunks=2,
    max_characters=300
)

context = builder.build(results)

print("=" * 60)
print("LLM Context")
print("=" * 60)
print(context)