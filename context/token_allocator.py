class TokenAllocator:
    """
    Allocates token budget between memories and knowledge chunks.
    """

    def __init__(
        self,
        total_budget: int = 1200,
        memory_ratio: float = 0.25,
    ):
        self.total_budget = total_budget
        self.memory_ratio = memory_ratio

    def allocate(self):

        memory_budget = int(
            self.total_budget * self.memory_ratio
        )

        knowledge_budget = (
            self.total_budget - memory_budget
        )

        return {
            "memory_budget": memory_budget,
            "knowledge_budget": knowledge_budget
        }