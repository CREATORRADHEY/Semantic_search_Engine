from datetime import datetime

from memory.memory_record import MemoryRecord


class MemoryRetriever:
    """
    Retrieves relevant memories with similarity ranking,
    metadata filtering, recency bonus and deduplication.
    """

    def __init__(self, manager):
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

        for similarity, memory in candidates:

            if not isinstance(memory, MemoryRecord):
                continue

            if memory.memory_id in seen:
                continue

            seen.add(memory.memory_id)

            if (
                similarity_threshold is not None
                and similarity < similarity_threshold
            ):
                continue

            if metadata_filter:
                matched = all(
                    memory.metadata.get(key) == value
                    for key, value in metadata_filter.items()
                )

                if not matched:
                    continue

            created_at = memory.created_at

            if isinstance(created_at, str):
                try:
                    created_at = datetime.fromisoformat(created_at)
                except Exception:
                    created_at = now

            age_seconds = max(
                (now - created_at).total_seconds(),
                1,
            )

            recency_bonus = 1 / (1 + age_seconds / 86400)

            final_score = similarity + recency_bonus * 0.05

            ranked.append(
                (final_score, memory)
            )

        ranked.sort(
            key=lambda x: x[0],
            reverse=True,
        )

        return ranked[:top_k]