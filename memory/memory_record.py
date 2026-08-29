from datetime import datetime
from uuid import uuid4

from pydantic import BaseModel, Field


class MemoryRecord(BaseModel):
    """
    One conversation memory stored inside the vector memory database.
    """

    memory_id: str = Field(default_factory=lambda: str(uuid4()))

    user_message: str

    assistant_message: str

    embedding: list[float]

    created_at: str = Field(
        default_factory=lambda: datetime.now().isoformat()
    )

    metadata: dict = Field(default_factory=dict)