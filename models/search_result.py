from typing import Any

from pydantic import BaseModel, Field


class SearchResult(BaseModel):

    score: float

    text: str

    chunk_id: str

    document_id: str

    metadata: dict[str, Any] = Field(
        default_factory=dict
    )