from citation.citation_builder import CitationBuilder

from models.search_result import SearchResult


def test_citation_builder():

    results = [

        SearchResult(
            document_id="1",
            chunk_id="1",
            text="Python",
            score=1,
            metadata={"source": "python.pdf"}
        ),

        SearchResult(
            document_id="2",
            chunk_id="2",
            text="Python Again",
            score=1,
            metadata={"source": "python.pdf"}
        )

    ]

    builder = CitationBuilder()

    citations = builder.build(results)

    assert len(citations) == 1

    assert citations[0].source == "python.pdf"