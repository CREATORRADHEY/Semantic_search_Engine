from models.citation import Citation
from models.search_result import SearchResult


class CitationBuilder:

    def build(
        self,
        results: list[SearchResult]
    ) -> list[Citation]:

        citations = []
        seen_sources = {}

        citation_index = 1

        for result in results:

            source = result.metadata.get(
                "source",
                "unknown"
            )

            if source in seen_sources:
                continue

            citations.append(
                Citation(
                    index=citation_index,
                    source=source,
                    document_id=result.document_id,
                    chunk_id=result.chunk_id
                )
            )

            seen_sources[source] = citation_index
            citation_index += 1

        return citations

    def format(
        self,
        citations: list[Citation]
    ) -> str:

        lines = []

        for citation in citations:

            lines.append(
                f"[{citation.index}] {citation.source}"
            )

        return "\n".join(lines)