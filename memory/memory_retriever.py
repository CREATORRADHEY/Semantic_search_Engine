from datetime import datetime

from memory.memory_manager import MemoryManager


class MemoryRetriever:
    """
    Production memory retrieval with ranking, recency bonus,
    metadata filtering, deduplication, and optional thresholding.
    """

    def __init__(self, manager: MemoryManager):
        self.manager = manager

    def retrieve(
        self,
        query: str,
        top_k: int = 3,
        similarity_threshold: float | None = 0.20,
        metadata_filter: dict | None = None,
    ):

        candidates = self.manager.search(
            query=query,
            top_k=20,
        )

        ranked = []
        seen = set()
        now = datetime.now()

        # Iterate over retrieved memories
        for similarity, memory in candidates:

            # Skip duplicate memories
            if memory.memory_id in seen:
                continue

            seen.add(memory.memory_id)

            # Optional similarity threshold
            if (
                similarity_threshold is not None
                and similarity < similarity_threshold
            ):
                continue

            # Optional metadata filtering
            if metadata_filter is not None:
                matched = all(
                    memory.metadata.get(key) == value
                    for key, value in metadata_filter.items()
                )

                if not matched:
                    continue

            # Recency bonus (last 7 days)
            created = datetime.fromisoformat(memory.created_at)
            age_hours = (now - created).total_seconds() / 3600

            recency_bonus = max(
                0,
                1 - age_hours / 168,
            )

            final_score = (
                similarity * 0.85
                + recency_bonus * 0.15
            )

            ranked.append((final_score, memory))

        ranked.sort(
            key=lambda x: x[0],
            reverse=True,
        )

        return ranked[:top_k]