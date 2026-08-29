from context.token_allocator import TokenAllocator


class ContextFusionEngine:

    def __init__(self):
        self.allocator = TokenAllocator()

    def _truncate(self, text: str, budget: int):

        words = text.split()

        return " ".join(words[:budget])

    def build(
        self,
        memories,
        documents
    ):

        budgets = self.allocator.allocate()

        sections = []

        sections.append("## Conversation Memory")

        memory_budget = budgets["memory_budget"]

        used = 0

        for score, memory in memories:

            block = (
                f"User: {memory.user_message}\n"
                f"Assistant: {memory.assistant_message}"
            )

            block = self._truncate(block, 80)

            tokens = len(block.split())

            if used + tokens > memory_budget:
                break

            sections.append(block)
            sections.append("")

            used += tokens

        sections.append("## Knowledge Context")

        knowledge_budget = budgets["knowledge_budget"]

        used = 0

        for doc in documents:

            block = (
                f"[Source: {doc.metadata.get('source','unknown')}]\n"
                f"{doc.text}"
            )

            block = self._truncate(block, 120)

            tokens = len(block.split())

            if used + tokens > knowledge_budget:
                break

            sections.append(block)
            sections.append("---")

            used += tokens

        return "\n".join(sections)