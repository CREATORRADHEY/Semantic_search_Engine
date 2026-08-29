from models.search_result import SearchResult


class ContextBuilder:
    """
    Builds an LLM-ready context from SearchResults.
    """

    def __init__(
        self,
        max_chunks: int = 5,
        max_characters: int = 1500
    ):

        self.max_chunks = max_chunks
        self.max_characters = max_characters

    def build(
        self,
        documents,
        memories=None
    ):

        sections = []

        if memories:

            sections.append("### Conversation Memory")

            for score, memory in memories:

                sections.append(
                    f"[Memory]\n"
                    f"User: {memory.user_message}\n"
                    f"Assistant: {memory.assistant_message}"
                )

            sections.append("")

        sections.append("### Knowledge Context")

        for result in documents:

            source = result.metadata.get("source", "unknown")

            sections.append(
                f"[Source: {source}]"
            )

            sections.append(result.text)

            sections.append("---")

        return "\n".join(sections)