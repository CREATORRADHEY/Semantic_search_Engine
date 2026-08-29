from citation.citation_builder import CitationBuilder

from models.search_result import SearchResult


results = [

    SearchResult(
        document_id="python",
        chunk_id="1",
        text="Python supports recursion.",
        score=9,
        metadata={"source": "python.pdf"}
    ),

    SearchResult(
        document_id="python",
        chunk_id="2",
        text="Recursive functions call themselves.",
        score=8,
        metadata={"source": "python.pdf"}
    ),

    SearchResult(
        document_id="algorithms",
        chunk_id="3",
        text="Divide and conquer often uses recursion.",
        score=8,
        metadata={"source": "algorithms.pdf"}
    )

]

builder = CitationBuilder()

citations = builder.build(results)

print("=" * 60)
print("Citations")
print("=" * 60)

print(builder.format(citations))