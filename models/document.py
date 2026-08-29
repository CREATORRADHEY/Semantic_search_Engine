from pydantic import BaseModel, Field
from typing import Dict, Any
from uuid import uuid4
from datetime import datetime, UTC


class Document(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid4()))
    filename: str
    source: str
    text: str
    metadata: Dict[str, Any] = Field(default_factory=dict)
    created_at: datetime = Field(default_factory=lambda: datetime.now(UTC))
    language: str = "en"


