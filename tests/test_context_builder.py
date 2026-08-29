from models.search_result import SearchResult

from context.context_builder import ContextBuilder


def test_context_builder():

    results = [

        SearchResult(
            document_id="doc1",
            chunk_id="1",
            text="Python supports OOP.",
            score=9,
            metadata={"source": "python.pdf"}
        ),

        SearchResult(
            document_id="doc2",
            chunk_id="2",
            text="Classes organize code.",
            score=8,
            metadata={"source": "python.pdf"}
        )

    ]

    builder = ContextBuilder()

    context = builder.build(results)

    assert "Python supports OOP." in context

    assert "Classes organize code." in context