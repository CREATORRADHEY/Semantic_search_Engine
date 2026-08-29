from typing import Any

from pydantic import BaseModel, Field


class Chunk(BaseModel):

    document_id: str

    text: str

    chunk_index: int

    metadata: dict[str, Any] = Field(
        default_factory=dict
    )